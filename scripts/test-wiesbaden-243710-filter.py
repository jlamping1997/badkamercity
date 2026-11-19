"""Offline safety/contract tests; never connects to Shopify or Typesense."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "correction", Path(__file__).with_name("correct-wiesbaden-243710-filter.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class Fake:
    def __init__(self):
        self.doc = {"id": m.DOC_ID, "sku": m.SKU, "sku_exact": m.SKU,
                    "shopify_product_id": "gid://shopify/Product/" + m.DOC_ID,
                    "collection_handles": list(m.COLLECTIONS),
                    "collection_ids": list(m.COLLECTIONS.values()),
                    "price_cents": 25289, "title": "Geborsteld RVS",
                    "url": "unchanged", "published": True,
                    "extra": {"nested": ["keep", 7]}}
        self.schema_data = {"name": m.INDEX, "fields": [
            {"name": m.FIELD, "type": "int32", "optional": True, "facet": True}]}
        self.writes = []
        self.fail_public_after = False
        self.reject_patch = False
        self.reads = 0
        self.conflict_on_read = None
        self.path = None

    def schema(self):
        return copy.deepcopy(self.schema_data)

    def document(self):
        self.reads += 1
        if self.reads == self.conflict_on_read:
            self.doc["price_cents"] += 1
        return copy.deepcopy(self.doc)

    def patch(self, value):
        # At the exact write boundary, an intact full backup must already exist.
        assert self.path.exists()
        m.load_backup(self.path)
        if self.reject_patch:
            raise m.Blocked("PATCH: authenticatie/rechten geweigerd (HTTP 403); responsinhoud verborgen.")
        self.writes.append({m.FIELD: value})
        if value is None:
            self.doc.pop(m.FIELD, None)
        else:
            self.doc[m.FIELD] = value
        return copy.deepcopy(self.doc)

    def api(self, base, path, body=None):
        if path == "/health":
            return {"ok": True, "service": m.CONTAINER, "typesense_collection": m.INDEX}
        if path.startswith("/api/v1/profile/"):
            return {"filters": [{"field": m.FIELD, "type": "number_decimal", "data_type": "int32"}]}
        assert path == "/api/v1/search"
        assert body["q"] == m.SKU and body["collection"] == m.PROFILE
        assert body["filters"] == {}
        holes = body["ranges"].get(m.FIELD, {}).get("min")
        if holes is not None:
            assert body["ranges"][m.FIELD]["max"] == holes
        included = holes is None or self.doc.get(m.FIELD) == holes
        if self.fail_public_after and base.startswith("https") and self.doc.get(m.FIELD) == 1:
            included = False
        return {"found": int(included), "exact_sku": True,
                "collection": {"handle": m.PROFILE},
                "products": [{"id": m.DOC_ID, "sku": m.SKU}] if included else []}


class CorrectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "backup.json"
        self.api = Fake()
        self.api.path = self.path
        self.before = copy.deepcopy(self.api.doc)

    def run_mode(self, mode):
        return m.execute(self.api, mode, self.path)

    def test_inspect_is_read_only(self):
        result = self.run_mode("inspect")
        self.assertEqual(result["status"], "READ_ONLY")
        self.assertFalse(self.path.exists())
        self.assertFalse(self.api.writes)
        self.assertEqual(result["checks"]["public"]["1"]["found"], 0)

    def test_apply_preserves_every_other_field_and_checks_both_apis(self):
        result = self.run_mode("apply")
        self.assertEqual(self.api.doc, {**self.before, m.FIELD: 1})
        self.assertEqual(self.api.writes, [{m.FIELD: 1}])
        self.assertEqual(m.load_backup(self.path)["original"], self.before)
        self.assertEqual(result["status"], "APPLIED_VERIFIED")
        for endpoint in ("public", "local"):
            self.assertEqual(result["checks"][endpoint]["1"]["ids"], [m.DOC_ID])
            self.assertEqual(result["checks"][endpoint]["2"]["ids"], [])

    def test_rollback_removes_originally_absent_field(self):
        self.run_mode("apply")
        self.assertEqual(self.run_mode("rollback")["status"], "ROLLED_BACK_VERIFIED")
        self.assertEqual(self.api.doc, self.before)
        self.assertEqual(self.api.writes[-1], {m.FIELD: None})

    def test_rollback_restores_existing_integer(self):
        self.api.doc[m.FIELD] = 2
        self.before = copy.deepcopy(self.api.doc)
        self.run_mode("apply")
        self.run_mode("rollback")
        self.assertEqual(self.api.doc, self.before)
        self.assertEqual(self.api.writes[-1], {m.FIELD: 2})

    def test_idempotent_apply_keeps_original_backup(self):
        self.run_mode("apply")
        backup = self.path.read_bytes()
        self.assertEqual(self.run_mode("apply")["status"], "ALREADY_CORRECT_VERIFIED")
        self.assertEqual(self.path.read_bytes(), backup)
        self.assertEqual(len(self.api.writes), 1)

    def test_refuse_wrong_identity_collections_type_and_schema(self):
        mutations = [
            lambda: self.api.doc.update(id="other"),
            lambda: self.api.doc.update(sku="other"),
            lambda: self.api.doc.update(collection_handles=["wastafels"]),
            lambda: self.api.doc.update({m.FIELD: True}),
            lambda: self.api.schema_data.update(name="other"),
            lambda: self.api.schema_data["fields"][0].update(type="string"),
            lambda: self.api.schema_data["fields"][0].update(optional=False),
            lambda: self.api.schema_data["fields"][0].update(index=False),
        ]
        for mutate in mutations:
            self.api = Fake()
            self.api.path = self.path
            mutate()
            with self.assertRaises(m.Blocked):
                self.run_mode("apply")
            self.assertFalse(self.api.writes)
            self.assertFalse(self.path.exists())

    def test_refuse_change_between_backup_and_write(self):
        self.api.conflict_on_read = 2
        with self.assertRaisesRegex(m.Blocked, "na back-up"):
            self.run_mode("apply")
        self.assertFalse(self.api.writes)

    def test_api_failure_auto_restores_exact_original(self):
        self.api.fail_public_after = True
        with self.assertRaisesRegex(m.Blocked, "gecontroleerd hersteld"):
            self.run_mode("apply")
        self.assertEqual(self.api.doc, self.before)

    def test_concurrent_other_field_change_not_overwritten(self):
        self.api.conflict_on_read = 3
        with self.assertRaisesRegex(m.Blocked, "herstel NIET bevestigd"):
            self.run_mode("apply")
        self.assertEqual(self.api.doc["price_cents"], self.before["price_cents"] + 1)
        self.assertEqual(len(self.api.writes), 1)

    def test_manual_rollback_refuses_concurrent_other_changes(self):
        self.run_mode("apply")
        self.api.doc["extra"]["nested"].append("new")
        with self.assertRaisesRegex(m.Blocked, "Rollbackconflict"):
            self.run_mode("rollback")
        self.assertEqual(len(self.api.writes), 1)

    def test_corrupted_backup_refused(self):
        self.run_mode("apply")
        data = json.loads(self.path.read_text(encoding="utf-8"))
        data["payload"]["original"]["price_cents"] = 1
        self.path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(m.Blocked, "checksum"):
            self.run_mode("rollback")
        self.assertEqual(len(self.api.writes), 1)

    def test_rejected_write_reports_http_status_and_no_secret(self):
        self.api.reject_patch = True
        with self.assertRaisesRegex(m.Blocked, "HTTP 403"):
            self.run_mode("apply")
        self.assertEqual(self.api.doc, self.before)

    def test_verify_before_apply_fails(self):
        with self.assertRaisesRegex(m.Blocked, "nog niet aanwezig"):
            self.run_mode("verify")

    def test_verify_checks_complete_backup(self):
        self.run_mode("apply")
        self.assertEqual(self.run_mode("verify")["status"], "VERIFIED")
        self.api.doc["price_cents"] += 1
        with self.assertRaisesRegex(m.Blocked, "andere documentvelden"):
            self.run_mode("verify")

    def test_uncertain_write_response_restores_without_reapplying(self):
        real_patch = self.api.patch
        def timeout_once(value):
            result = real_patch(value)
            if value == 1:
                raise m.Blocked("PATCH: verbinding/TLS/time-out; geen automatische write-retry.")
            return result
        self.api.patch = timeout_once
        with self.assertRaisesRegex(m.Blocked, "gecontroleerd hersteld"):
            self.run_mode("apply")
        self.assertEqual(self.api.doc, self.before)
        self.assertEqual(self.api.writes, [{m.FIELD: 1}, {m.FIELD: None}])

    def test_wrong_api_index_and_choice_contract_block_before_backup(self):
        real_api = self.api.api
        for case in ("index", "profile"):
            def wrong_api(base, path, body=None):
                result = real_api(base, path, body)
                if path == "/health" and case == "index":
                    result["typesense_collection"] = "legacy-index"
                if path.startswith("/api/v1/profile") and case == "profile":
                    result["filters"][0]["type"] = "string"
                return result
            self.api.api = wrong_api
            with self.assertRaises(m.Blocked):
                self.run_mode("apply")
            self.assertFalse(self.path.exists())
            self.assertFalse(self.api.writes)

    def test_transport_blocks_any_other_mutation_before_network(self):
        with patch.object(m.urllib.request, "build_opener") as opener:
            cases = [(m.TS + "/collections/other/documents/123", "PATCH"),
                     (m.TS + f"/collections/{m.INDEX}/documents/import", "POST"),
                     (m.TS + m.DOC_PATH, "DELETE"),
                     ("https://example.invalid/", "PATCH")]
            for url, method in cases:
                with self.assertRaises(m.Blocked):
                    m.request_json(url, method=method, body={}, key="not-a-real-key")
            opener.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
