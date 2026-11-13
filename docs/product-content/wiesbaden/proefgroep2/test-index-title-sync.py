"""Offline safety tests; no network, Docker, Shopify or production writes."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("sync", Path(__file__).with_name("sync-wiesbaden-proefgroep2-index-titles.py"))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class Fake:
    def __init__(self):
        self.docs = {i["id"]: {"id": i["id"], "sku": i["sku"], "sku_exact": i["sku"],
                    "shopify_product_id": "gid://shopify/Product/" + i["id"],
                    "collection_handles": i["collections"], "title": i["old_title"],
                    "price_cents": 12345, "inventory_quantity": 7, "f_serie": "unchanged",
                    "image_url": "https://example.invalid/image.jpg"} for i in sync.PLAN}
        self.originals = copy.deepcopy(self.docs)
        self.writes = []
        self.fail_after_commit = None

    def schema(self):
        return {"name": sync.INDEX, "fields": [{"name": "title", "type": "string"}]}

    def document(self, item):
        return copy.deepcopy(self.docs[item["id"]])

    def patch(self, item, title):
        self.writes.append((item["id"], title))
        self.docs[item["id"]]["title"] = title
        if self.fail_after_commit == item["id"]:
            self.fail_after_commit = None
            raise sync.Blocked("Ambiguous timeout after successful PATCH")

    def api(self, base, path, body=None):
        if path == "/health":
            return {"ok": True, "typesense_collection": sync.INDEX, "service": sync.CONTAINER}
        match = next(i for i in sync.PLAN if body["q"] in (i["sku"], i["q"]))
        doc = self.docs[match["id"]]
        return {"collection": {"handle": match["profile"]}, "found": 1,
                "exact_sku": body["q"] == match["sku"], "products": [copy.deepcopy(doc)]}


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old_root, self.old_backup = sync.BACKUP_ROOT, sync.BACKUP
        sync.BACKUP_ROOT = Path(self.tmp.name)
        sync.BACKUP = sync.BACKUP_ROOT / "backup.json"
        self.api = Fake()

    def tearDown(self):
        sync.BACKUP_ROOT, sync.BACKUP = self.old_root, self.old_backup
        self.tmp.cleanup()

    def test_inspect_never_writes_or_backs_up(self):
        result = sync.execute(self.api, "inspect")
        self.assertEqual(result["status"], "READ_ONLY")
        self.assertEqual(self.api.writes, [])
        self.assertFalse(sync.BACKUP.exists())

    def test_apply_only_titles_and_private_full_backup(self):
        result = sync.execute(self.api, "apply")
        self.assertEqual(result["status"], "APPLIED_VERIFIED")
        self.assertEqual(len(self.api.writes), 7)
        self.assertEqual(len(result["checks"]), 28)
        self.assertEqual(sync.BACKUP.stat().st_mode & 0o777, 0o600)
        self.assertEqual(sync.load_backup()["originals"], self.api.originals)
        for item in sync.PLAN:
            self.assertEqual(self.api.docs[item["id"]], {**self.api.originals[item["id"]], "title": item["title"]})

    def test_repeat_apply_is_idempotent(self):
        sync.execute(self.api, "apply")
        initial = sync.BACKUP.read_bytes()
        self.api.writes.clear()
        sync.execute(self.api, "apply")
        self.assertEqual(self.api.writes, [])
        self.assertEqual(sync.BACKUP.read_bytes(), initial)

    def test_restore_only_titles_and_full_readback(self):
        sync.execute(self.api, "apply")
        result = sync.execute(self.api, "restore")
        self.assertEqual(result["status"], "RESTORED_VERIFIED")
        self.assertEqual(self.api.docs, self.api.originals)

    def test_identity_mismatch_no_write(self):
        self.api.docs[sync.PLAN[0]["id"]]["sku_exact"] = "OTHER"
        with self.assertRaises(sync.Blocked):
            sync.execute(self.api, "apply")
        self.assertEqual(self.api.writes, [])

    def test_other_title_mismatch_no_write(self):
        self.api.docs[sync.PLAN[0]["id"]]["title"] = "Edited elsewhere"
        with self.assertRaises(sync.Blocked):
            sync.execute(self.api, "apply")
        self.assertEqual(self.api.writes, [])

    def test_collection_change_no_write(self):
        self.api.docs[sync.PLAN[0]["id"]]["collection_handles"] = ["different"]
        with self.assertRaises(sync.Blocked):
            sync.execute(self.api, "apply")
        self.assertEqual(self.api.writes, [])

    def test_backup_corruption_no_write(self):
        sync.save_backup(self.api.docs)
        data = json.loads(sync.BACKUP.read_text())
        data["payload"]["originals"][sync.PLAN[0]["id"]]["price_cents"] += 1
        sync.BACKUP.write_text(json.dumps(data))
        with self.assertRaises(sync.Blocked):
            sync.execute(self.api, "apply")
        self.assertEqual(self.api.writes, [])

    def test_concurrent_other_field_edit_preserved_on_restore(self):
        sync.execute(self.api, "apply")
        item = sync.PLAN[-1]
        self.api.docs[item["id"]]["price_cents"] = 99999
        self.api.writes.clear()
        with self.assertRaises(sync.Blocked):
            sync.execute(self.api, "restore")
        self.assertEqual(self.api.writes, [])
        self.assertEqual(self.api.docs[item["id"]]["price_cents"], 99999)

    def test_ambiguous_patch_timeout_restores_all_applied_titles(self):
        self.api.fail_after_commit = sync.PLAN[2]["id"]
        with self.assertRaisesRegex(sync.Blocked, "hersteld en gecontroleerd"):
            sync.execute(self.api, "apply")
        self.assertEqual(self.api.docs, self.api.originals)

    def test_wrong_active_index_stops_before_writes(self):
        self.api.schema = lambda: {"name": "other", "fields": [{"name": "title", "type": "string"}]}
        with self.assertRaises(sync.Blocked):
            sync.execute(self.api, "apply")
        self.assertEqual(self.api.writes, [])

    def test_unscoped_patch_or_fields_blocked_before_network(self):
        base = sync.TS + "/collections/" + sync.INDEX + "/documents/"
        with self.assertRaises(sync.Blocked):
            sync.request_json(base + sync.PLAN[0]["id"], method="PATCH", body={"price": 1}, key="test")
        with self.assertRaises(sync.Blocked):
            sync.request_json(base + "not-allowed", method="PATCH", body={"title": "x"}, key="test")


if __name__ == "__main__":
    unittest.main()
