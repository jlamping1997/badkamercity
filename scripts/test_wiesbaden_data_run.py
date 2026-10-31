"""Regression checks for the read-only source collector; no live requests."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("wiesbaden_source_run", Path(__file__).with_name("wiesbaden-data-run.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def api():
    return {"uid": "test-uid", "sku": "24.3710", "name": "Test wastafelkraan",
            "url_key": "test-wastafelkraan", "url_suffix": ".html",
            "price_range": {"minimum_price": {"regular_price": {"value": 209}}},
            "categories": [{"uid": "leaf", "name": "Opbouw", "url_path": "kranen/wastafelkranen/opbouw",
                "breadcrumbs": [{"category_uid": "middle", "category_name": "Wastafelkranen", "category_level": 4},
                                {"category_uid": "root", "category_name": "Kranen", "category_level": 3}]}]}


def fixture(sku="24.3710"):
    return ('''<main><h1>Test wastafelkraan</h1><div class="product-info-main">
      <div class="product-description"><p>Productuitleg.</p></div>
      <script>const noise = 'Adviesprijs: € 999,00';</script>
      <span>Adviesprijs: € 209,00</span>
      <table class="additional-attributes"><tr><th>SKU</th><td>''' + sku + '''</td></tr>
      <tr><th>Merk</th><td>Wiesbaden</td></tr><tr><th>Coldstart</th><td>Ja</td></tr>
      <tr><th>Met afvoerplug</th><td>Nee</td></tr><tr><th>Hoogte</th><td></td></tr>
      <tr><th>EAN</th><td>1234567890123</td></tr></table>
      <a href="https://korverholland.compano.com/Handleidingen/24.3710.pdf">Download</a>
      <a href="https://example.test/24.3712.pdf">Ander product</a>
      </div><script>const images=[{"imageUrl":"https:\\/\\/korverholland.compano.com\\/Productafbeeldingen\\/24.3710.jpg",
      "imageLabel":"Product","isMainImage":true,"type":"image"},
      {"imageUrl":"https://korverholland.compano.com/Lijntekeningen/24.3710.jpg","type":"line_drawings"}];</script>
      </main>''').encode()


class SourceTests(unittest.TestCase):
    def parse(self, body=None, product=None):
        return m.parse_page(body or fixture(), product or api(), {"url": m.BASE + "test.html"})

    def test_real_extraction_shape_and_noise_exclusion(self):
        p = self.parse()
        self.assertEqual(p["advice_price_displayed_eur"], "209.00")
        self.assertFalse(p["issues"])
        self.assertEqual(p["description_text_source"], "Productuitleg.")
        self.assertEqual(p["source_brand"], "Wiesbaden")

    def test_wrong_sku_never_passes_identity_gate(self):
        self.assertIn("PAGE_SKU_MISSING_OR_MISMATCH", self.parse(fixture("24.3712"))["issues"])

    def test_ean_is_not_a_specification_or_matching_key(self):
        p = self.parse()
        self.assertFalse(any(x["label"] == "EAN" for x in p["specifications"]))
        self.assertTrue(any(x["label"] == "EAN" for x in p["specifications_raw"]))
        self.assertEqual(m.sku_key(" 00.0123 "), "00.0123")
        self.assertNotEqual(m.sku_key("24.3710"), m.sku_key("243710"))

    def test_empty_is_distinct_from_no(self):
        values = {x["label"]: x["value"] for x in self.parse()["specifications"]}
        self.assertEqual(values["Met afvoerplug"], "Nee")
        self.assertEqual(values["Hoogte"], "")

    def test_breadcrumbs_ordered_by_level(self):
        self.assertEqual([x["name"] for x in self.parse()["source_breadcrumb_paths"][0]],
                         ["Kranen", "Wastafelkranen", "Opbouw"])

    def test_images_and_drawings_are_separate_and_unescaped(self):
        media = self.parse()["images"]
        self.assertEqual([x["kind"] for x in media], ["image", "line_drawings"])
        self.assertTrue(all("\\" not in x["url"] for x in media))
        self.assertEqual(len(self.parse()["documents"]), 1)

    def test_price_disagreement_blocks_unreviewed_import(self):
        product = api()
        product["price_range"]["minimum_price"]["regular_price"]["value"] = 252.89
        self.assertIn("HTML_API_ADVICE_PRICE_CONFLICT", self.parse(product=product)["issues"])

    def test_only_https_manufacturer_urls_can_be_requested(self):
        with tempfile.TemporaryDirectory() as root:
            for url in ["https://evil.test/", "http://www.wiesbaden.nl/"]:
                with self.assertRaises(ValueError):
                    m.Source(root).fetch(url, "test")

    def test_incomplete_store_snapshot_cannot_prove_missing_products(self):
        with tempfile.TemporaryDirectory() as root:
            m.write_json(Path(root)/"shopify/snapshot-manifest.json", {"global_sku_index_complete": False})
            with self.assertRaisesRegex(ValueError, "Incomplete Shopify snapshot"):
                m.build(root)

    def test_generic_tax_functions_do_not_prove_selected_price_mode(self):
        mode, evidence = m.price_tax_basis("const finalPriceExclTaxKey='basePrice';", "209.00")
        self.assertEqual(mode, "NOT_VERIFIED")
        self.assertIsNone(evidence)

    def test_selected_price_component_and_amount_must_match(self):
        config = ('regularPriceKey: regularPriceExclTaxKey, finalPriceKey: finalPriceExclTaxKey, '
                  'activeProductsPriceData: false, initialFinalPrice: 209, calculatedFinalPrice: false')
        self.assertTrue(m.price_tax_basis(config, "209.00")[0].startswith("EXCL_TAX"))
        self.assertEqual(m.price_tax_basis(config, "252.89")[0], "NOT_VERIFIED")

    def test_tax_comparison_does_not_treat_exclusive_price_as_discount(self):
        record = {"advice_price_displayed_eur":"209.00", "price_tax_status":"EXCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT"}
        proposal = m.price_proposal(record, "252.89", True)
        self.assertEqual(proposal["status"], "MATCHES_CURRENT_STORE_PRICE")
        self.assertEqual(proposal["proposed_advice_incl_eur"], "252.89")
        record["advice_price_displayed_eur"] = "0.00"
        self.assertIsNone(m.price_proposal(record, None, True)["proposed_advice_incl_eur"])

    def test_inclusive_price_is_not_taxed_twice(self):
        record = {"advice_price_displayed_eur":"252.89", "price_tax_status":"INCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT"}
        self.assertEqual(m.price_proposal(record, "252.89", True)["status"], "MATCHES_CURRENT_STORE_PRICE")


if __name__ == "__main__":
    unittest.main()
