"""Offline safety and mapping tests: python3 -m unittest -v test_index_sync.py"""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("sync", Path(__file__).with_name("index_sync.py"))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def product(pid, sku, product_type="Inloopdouche", price="254.00", metafields=None):
    return {"id": f"gid://shopify/Product/{pid}", "title": f"Wiesbaden test {sku}",
            "handle": "wiesbaden-test-" + sku.replace(".", "-"), "vendor": "Wiesbaden",
            "productType": product_type, "status": "ACTIVE", "updatedAt": "2026-10-22T00:00:00Z",
            "onlineStoreUrl": "https://badkamercity.nl/products/wiesbaden-test-" + sku.replace(".", "-"),
            "featuredMedia": {"image": {"url": "https://cdn.shopify.com/test.jpg"}},
            "variants": {"nodes": [{"sku": sku, "price": price}], "pageInfo": {"hasNextPage": False}},
            "collections": {"nodes": [{"id": "gid://shopify/Collection/123", "handle": "inloopdouches"}],
                            "pageInfo": {"hasNextPage": False}},
            "metafields": {"nodes": metafields or [], "pageInfo": {"hasNextPage": False}}}


def fixture(root):
    root = Path(root)
    base = [{"id": "101", "shopify_product_id": "101", "vendor": "Wiesbaden", "sku": "20.3755",
             "general_shopping": True, "product_type": "Inloopdouche", "f_breedte_mm": 800.0,
             "f_glaskleur": "Helder glas", "published": True, "collection_handles": ["inloopdouches"],
             "price_cents": 32900, "title": "Oud"},
            {"id": "103", "shopify_product_id": "103", "vendor": "Wiesbaden", "sku": "20.3700",
             "general_shopping": False, "product_type": "Kraanrozet", "published": True,
             "collection_handles": ["onderdelen"], "price_cents": 2000, "title": "Service"},
            {"id": "200", "shopify_product_id": "200", "vendor": "Hotbath", "sku": "HB1",
             "general_shopping": True, "product_type": "Kraan", "published": True,
             "collection_handles": ["kranen"], "price_cents": 10000}]
    schema = {"name": "old", "fields": [
        {"name": n, "type": t} for n, t in [
            ("id", "string"), ("shopify_product_id", "string"), ("sku", "string"),
            ("sku_exact", "string"), ("title", "string"), ("handle", "string"),
            ("vendor", "string"), ("product_type", "string"), ("source_productsoort", "string"),
            ("source_updated_at", "string"), ("url", "string"), ("image_url", "string"),
            ("price_cents", "int64"), ("published", "bool"), ("general_shopping", "bool"),
            ("collection_handles", "string[]"), ("collection_ids", "string[]"),
            ("f_productsoort", "string"), ("f_breedte_mm", "float"),
            ("f_glasdikte_mm", "float"), ("f_glaskleur", "string"), ("f_nano_coating", "bool")
        ]], "metadata": {"purpose": "test"}}
    profiles = {"__all__": {"products": 3, "shopping_products": 2, "filters": [], "allowed_filters": []},
                "inloopdouches": {"products": 1, "shopping_products": 1, "filters": ["test"], "allowed_filters": ["test"]},
                "onderdelen": {"products": 1, "shopping_products": 0, "filters": [], "allowed_filters": []}}
    service = product("103", "20.3700", product_type="Kraanrozet", price="20.00")
    service["collections"]["nodes"] = [{"id": "gid://shopify/Collection/456", "handle": "onderdelen"}]
    products = [
        product("101", "20.3755", price="329.00", metafields=[
            {"namespace": "bc_data", "key": "filter_manifest", "type": "json", "value": json.dumps({
                "sku": "20.3755", "values": {"breedte_mm": 800, "glasdikte_mm": 10,
                                                 "nano_coating": True, "glaskleur": "Helder glas"}})},
            {"namespace": "bc_filters", "key": "breedte_mm", "type": "number_decimal", "value": "900.0"}]),
        service,
        product("102", "20.3404", price="254.00", metafields=[
            {"namespace": "bc_filters", "key": "glasdikte_mm", "type": "number_decimal", "value": "8.0"}])
    ]
    paths = []
    for file, data in [("old.jsonl", base), ("snapshot.jsonl", products),
                       ("schema.json", schema), ("profiles.json", profiles)]:
        p = root / file
        p.write_text("".join(sync.canonical(row) + "\n" for row in data) if file.endswith("jsonl")
                     else sync.canonical(data), encoding="utf-8")
        paths.append(p)
    return paths


class SyncTests(unittest.TestCase):
    def test_price_is_inclusive_and_not_multiplied_by_vat(self):
        self.assertEqual(sync.cents("254.00"), 25400)
        self.assertEqual(sync.cents("100.01"), 10001)
        for invalid in ("0.00", "2.005", "NaN", "-5.00", ""):
            with self.assertRaises(ValueError):
                sync.cents(invalid)

    def test_typed_filter_validation(self):
        self.assertEqual(sync.typed("8.0", "float"), 8.0)
        self.assertTrue(sync.typed("true", "bool"))
        with self.assertRaises(ValueError): sync.typed("weet niet", "bool")
        with self.assertRaises(ValueError): sync.typed("8.2", "int32")

    def test_prepare_preserves_other_brands_and_service_rules(self):
        with tempfile.TemporaryDirectory() as temp:
            paths = fixture(temp)
            report = sync.build(*paths, Path(temp) / "out")
            self.assertEqual(report["old_wiesbaden"], 2)
            self.assertEqual(report["shopify_wiesbaden"], 3)
            self.assertEqual(report["new_wiesbaden"], 1)
            docs = {d["id"]: d for d in sync.read_jsonl(Path(temp) / "out/documents.jsonl")}
            self.assertEqual(len(docs), 4)
            self.assertEqual(docs["200"]["price_cents"], 10000)
            self.assertFalse(docs["103"]["general_shopping"])
            self.assertEqual(docs["101"]["f_breedte_mm"], 900.0)
            self.assertEqual(docs["101"]["f_glasdikte_mm"], 10.0)
            self.assertTrue(docs["101"]["f_nano_coating"])
            self.assertEqual(docs["102"]["price_cents"], 25400)
            counts = json.loads((Path(temp) / "out/profiles.json").read_text())
            self.assertEqual(counts["inloopdouches"]["products"], 2)
            self.assertEqual(counts["inloopdouches"]["filters"], ["test"])
            self.assertEqual(counts["__all__"]["shopping_products"], 3)
            self.assertEqual((Path(temp) / "out/documents.jsonl").stat().st_mode & 0o777, 0o600)

    def test_missing_old_product_stops_without_deletion(self):
        with tempfile.TemporaryDirectory() as temp:
            paths = fixture(temp)
            lines = sync.read_jsonl(paths[1])
            paths[1].write_text("".join(sync.canonical(row) + "\n" for row in lines if not row["id"].endswith("103")))
            with self.assertRaisesRegex(ValueError, "missing from Shopify snapshot"):
                sync.build(*paths, Path(temp) / "out")

    def test_unknown_service_classification_stops(self):
        with tempfile.TemporaryDirectory() as temp:
            paths = fixture(temp)
            rows = sync.read_jsonl(paths[1])
            rows[2]["productType"] = "Unknown service part"
            paths[1].write_text("".join(sync.canonical(row) + "\n" for row in rows))
            with self.assertRaisesRegex(ValueError, "No unambiguous service"):
                sync.build(*paths, Path(temp) / "out")

    def test_bad_manifest_identity_stops(self):
        with tempfile.TemporaryDirectory() as temp:
            paths = fixture(temp)
            rows = sync.read_jsonl(paths[1])
            rows[0]["metafields"]["nodes"][0]["value"] = json.dumps({"sku": "wrong", "values": {}})
            paths[1].write_text("".join(sync.canonical(row) + "\n" for row in rows))
            with self.assertRaisesRegex(ValueError, "Invalid canonical"):
                sync.build(*paths, Path(temp) / "out")

    def test_stage_requires_secret_before_writes(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "not configured"):
                sync.stage("/tmp/nonexistent")

    def test_stage_refuses_existing_collection_before_write(self):
        with tempfile.TemporaryDirectory() as temp:
            paths = fixture(temp)
            sync.build(*paths, Path(temp) / "out")
            with patch.dict(os.environ, {"TYPESENSE_API_KEY": "fake"}):
                with patch.object(sync, "request_json", return_value={"num_documents": 0}) as mock:
                    with self.assertRaisesRegex(ValueError, "already exists"):
                        sync.stage(Path(temp) / "out")
                    self.assertEqual(mock.call_count, 1)

    def test_capture_refuses_missing_credentials(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "not configured"):
                sync.capture("/tmp/no-credentials.jsonl")

    def test_private_write_not_in_git_checkout(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / ".git").mkdir()
            with self.assertRaises(ValueError):
                sync.write_private(Path(temp) / "secrets.json", "{}")


if __name__ == "__main__":
    unittest.main()
