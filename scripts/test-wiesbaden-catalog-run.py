#!/usr/bin/env python3
"""Focused price/identity/privacy regressions; synthetic data only, no network."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("catalog", Path(__file__).with_name("wiesbaden-catalog-run.py"))
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


def row(sku="24.3710", price="149.50"):
    return {"productcode": sku, "merk": "Wiesbaden", catalog.PRICE_COLUMN: price,
            "productnaam": "Testkraan", "description": "", "afmeting": "", "kleur": "",
            "inkoopprijs (excl. btw)": "79.31", "in_voorraad": "Ja", "barcode": "1234567890123",
            "main_image": "https://example.test/a.jpg", "afbeeldingscode": "https://example.test/a.jpg",
            "gallery": "https://example.test/a.jpg;https://example.test/b.jpg", "lijntekening": "https://example.test/drawing.jpg"}


def snapshot(sku="24.3710", price="149.00"):
    return {"pagination_complete": True, "products": [{"id": "gid://shopify/Product/1", "vendor": "Wiesbaden",
            "title": "Approved title", "descriptionHtml": "Approved description", "metafields": [{"value": "keep"}],
            "variants": {"nodes": [{"id": "gid://shopify/ProductVariant/2", "sku": sku, "price": price}]}}]}


class CatalogTests(unittest.TestCase):
    def test_price_boundaries_and_no_double_rounding(self):
        for amount, basis, expected in [("80", "ex", "96.80"), ("120", "ex", "145.00"),
                ("149.49", "incl", "149.00"), ("149.50", "incl", "150.00"),
                ("100", "incl", "100.00"), ("99.995", "incl", "100.00"),
                ("100.01", "incl", "100.00"), ("100.50", "incl", "101.00"),
                ("100.41", "ex", "121.00"), ("12,345", "incl", "12.35")]:
            with self.subTest(amount=amount, basis=basis):
                self.assertEqual(catalog.sale_price(amount, basis), expected)
        for invalid in ("", "0", "-1", "NaN", "1.000,00", "0.001"):
            self.assertIsNone(catalog.sale_price(invalid, "incl"))
        with self.assertRaises(ValueError):
            catalog.sale_price("209", "guess_from_header")

    def test_exact_sku_keeps_zeros_and_mismatches(self):
        self.assertEqual(catalog.sku_key(" 001.3710 "), "001.3710")
        with self.assertRaises(ValueError):
            catalog.sku_key(24.371)
        manifest = catalog.prepare([row()], "hash", "incl", "test", snapshot("24.371"))
        self.assertEqual(manifest["items"][0]["status"], "MISSING_CANDIDATE")
        self.assertNotIn("variant_price", manifest["items"][0]["changes"])

    def test_only_price_changes_and_blank_fields_preserve(self):
        item = catalog.prepare([row()], "hash", "incl", "test", snapshot())["items"][0]
        self.assertEqual(item["changes"], {"variant_price": {"id": "gid://shopify/ProductVariant/2", "price": "150.00"}})
        self.assertNotIn("candidate", item)
        item = catalog.prepare([row(price="")], "hash", "incl", "test", snapshot())["items"][0]
        self.assertEqual(item["changes"], {})
        self.assertEqual(item["status"], "PRICE_UNUSABLE_PRESERVE_EXISTING")

    def test_public_candidate_whitelist_and_media(self):
        manifest = catalog.prepare([row()], "hash", "incl", "test", {"pagination_complete": True, "products": []})
        candidate = manifest["items"][0]["candidate"]
        self.assertEqual(candidate["media_urls"], ["https://example.test/a.jpg", "https://example.test/b.jpg"])
        for forbidden in ("79.31", "inkoop", "in_voorraad", "barcode", "1234567890123", "drawing.jpg", "source_description"):
            self.assertNotIn(forbidden, json.dumps(candidate))

    def test_completeness_duplicates_and_no_false_success(self):
        self.assertEqual(catalog.prepare([row()], "hash", "incl", "test")["items"][0]["status"], "UNMATCHED_UNVERIFIED")
        data = catalog.prepare([row(), row()], "hash", "incl", "test", snapshot())
        self.assertEqual(data["summary"]["statuses"], {"BLOCKED_SOURCE_IDENTITY": 2})
        self.assertEqual(data["summary"]["executed_writes"], 0)
        duplicate = snapshot()
        duplicate["products"].append(duplicate["products"][0])
        self.assertEqual(catalog.prepare([row()], "hash", "incl", "test", duplicate)["items"][0]["status"], "BLOCKED_DUPLICATE_SHOPIFY_SKU")

    def test_checkpoint_requires_matching_manifest_and_readback(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "journal.json"
            catalog.checkpoint(path, "run1", "op1", "planned")
            with self.assertRaises(ValueError):
                catalog.checkpoint(path, "run2", "op1", "applied")
            with self.assertRaises(ValueError):
                catalog.checkpoint(path, "run1", "op1", "verified")
            catalog.checkpoint(path, "run1", "op1", "verified", {"readback_price": "150.00"})
            self.assertEqual(json.loads(path.read_text())["operations"]["op1"]["state"], "verified")


if __name__ == "__main__":
    unittest.main()
