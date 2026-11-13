import unittest

from collect_choices import normalize, parse_page


class SourceParserTests(unittest.TestCase):
    def test_component_stock_does_not_become_product_eta(self):
        raw = b'''<html><link rel="canonical" href="https://fabriecio.nl/product/set/">
        <div class="summary entry-summary"><h1 class="product_title">Set</h1>
        <div class="bundled_item_cart_details"><p class="stock out-of-stock">Verwacht: Week 6</p></div>
        <div class="bundle_availability"><p class="stock insufficient-stock">Insufficient stock</p></div>
        </div><table class="shop_attributes"><tr><th>Typenummer</th><td>SET_1</td></tr></table></html>'''
        record = parse_page(raw, "https://fabriecio.nl/product/set/")
        self.assertEqual(record["sku"], "SET_1")
        self.assertEqual([x["text"] for x in record["stock_messages"]], ["Insufficient stock"])
        self.assertEqual([x["text"] for x in record["component_stock_messages"]], ["Verwacht: Week 6"])
        self.assertNotIn("Verwacht: Week 6", record["delivery_messages"])

    def test_explicit_link_and_current_value_are_preserved(self):
        raw = b'''<html><link rel="canonical" href="https://fabriecio.nl/product/white/">
        <div class="summary"><h1 class="product_title">White</h1><span class="sku">W1</span>
        <table class="iconic-wlv-variations"><tr class="iconic-wlv-variations__row iconic-wlv-variations__row--pa_kleur">
        <strong class="iconic-wlv-variations__label">Kleur</strong><span data-iconic-wlv-selected-term-label="Wit"></span>
        <li class="iconic-wlv-terms__term--current" data-iconic-wlv-term-label="Wit"><span>Wit</span></li>
        <li data-iconic-wlv-term-label="Mat Wit"><a href="https://b2b.fabriecio.nl/product/matte/">Mat Wit</a></li>
        </tr></table></div></html>'''
        record = parse_page(raw, "https://fabriecio.nl/product/white/")
        menu = record["menus"][0]
        self.assertEqual(menu["key"], "kleur")
        self.assertEqual(menu["selected"], "Wit")
        self.assertEqual([x["value"] for x in menu["values"]], ["Wit", "Mat Wit"])
        self.assertEqual(menu["values"][1]["target_url"], "https://fabriecio.nl/product/matte/")
        self.assertEqual(menu["values"][0]["target_url"], record["source_url"])

    def test_missing_option_target_is_reported_not_guessed(self):
        record = {"sku": "W1", "source_url": "https://fabriecio.nl/product/white/", "menus": [{"key": "kleur", "values": [{"value": "Mat Wit", "target_url": "https://fabriecio.nl/product/missing/", "current": False}]}], "selected_options": {"kleur": "Wit"}}
        result = normalize([record], {"products": [{"url": record["source_url"]}]})
        self.assertEqual(result["summary"]["unresolved_option_count"], 1)
        self.assertIsNone(record["menus"][0]["values"][0]["target_sku"])


if __name__ == "__main__":
    unittest.main()
