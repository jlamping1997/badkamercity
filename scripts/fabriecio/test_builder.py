import copy
import itertools
import unittest

from builder import build_plan, delivery


def fixture(dimensions=None):
    dimensions = dimensions or {"kleur": ["Wit", "Mat Wit"], "maat": ["170x80cm", "180x85cm"]}
    records, shopify = [], []
    combinations = list(itertools.product(*dimensions.values()))
    skus = {values: f"SKU_{i}" for i, values in enumerate(combinations, 1)}
    for i, values in enumerate(combinations, 1):
        sku = skus[values]
        selected = dict(zip(dimensions, values))
        row = {
            "sku": sku, "title": "Source " + sku, "source_url": f"https://fabriecio.nl/product/{sku.lower()}/",
            "group_id": "fabriecio-fixture", "observed_at": "2026-11-05T10:00:00+00:00",
            "selected_options": selected, "menus": [],
            "stock_messages": [{"text": "Op voorraad", "class": "stock in-stock"}],
            "delivery_messages": [],
        }
        for key, choices in dimensions.items():
            menu = {"key": key, "label": key.capitalize(), "selected": selected[key], "values": []}
            for value in choices:
                target_options = {**selected, key: value}
                target_sku = skus[tuple(target_options.values())]
                menu["values"].append({
                    "value": value, "target_sku": target_sku,
                    "target_url": f"https://fabriecio.nl/product/{target_sku.lower()}/",
                    "current": target_sku == sku,
                })
            row["menus"].append(menu)
        records.append(row)
        shopify.append({
            "id": f"gid://shopify/Product/{i}", "handle": f"fabriecio-sku-{i}",
            "vendor": "Fabriecio", "title": "Stored " + sku, "status": "ACTIVE",
            "variants": {"nodes": [{"id": f"gid://shopify/ProductVariant/{i}", "sku": sku,
                "inventoryQuantity": 2, "inventoryPolicy": "DENY"}]},
            "featuredMedia": {"preview": {"image": {"url": f"https://cdn.shopify.com/files/{i}.jpg"}}},
        })
    catalogue = {"created_at": "2026-11-05", "products": records,
        "groups": [{"id": "fabriecio-fixture", "skus": list(skus.values())}]}
    return catalogue, shopify


class BuilderTests(unittest.TestCase):
    def test_malmo_choices_preserve_source_order_and_urls(self):
        catalogue, shopify = fixture()
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["choice_products"], 4)
        self.assertEqual(result["holds"], [])
        for row, source in zip(result["updates"], catalogue["products"]):
            group = row["choices"]["groups"][0]
            self.assertEqual(group["menus"][0]["values"], ["Wit", "Mat Wit"])
            self.assertEqual(group["menus"][1]["values"], ["170x80cm", "180x85cm"])
            destinations = {tuple(sorted(x["options"].items())): x for x in group["products"]}
            for menu in source["menus"]:
                for choice in menu["values"]:
                    wanted = {**source["selected_options"], menu["key"]: choice["value"]}
                    target = destinations[tuple(sorted(wanted.items()))]
                    self.assertTrue(target["url"].startswith("/products/fabriecio-sku-"))
                    self.assertTrue(target["swatch_url"].startswith("https://cdn.shopify.com/"))

    def test_verlavio_and_supplier_brand_keep_exact_sku_matching(self):
        catalogue, shopify = fixture()
        for index, product in enumerate(shopify):
            product["vendor"] = "Verlavio" if index % 2 else "Fabriecio"
            product["title"] = "Verlavio " + product["variants"]["nodes"][0]["sku"]
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["choice_products"], 4)
        self.assertEqual(result["holds"], [])
        self.assertEqual(result["summary"]["missing_active_shopify_source_skus"], [])
        for row in result["updates"]:
            self.assertTrue(all(p["title"].startswith("Verlavio ") for p in row["choices"]["groups"][0]["products"]))

    def test_large_group_uses_complete_local_neighborhood(self):
        catalogue, shopify = fixture({"kleur": [str(i) for i in range(6)],
            "maat": [str(i) for i in range(3)], "vorm": ["Rond", "Vierkant"],
            "uitvoering": ["Muur", "Plafond"]})
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["choice_products"], 72)
        self.assertEqual(result["summary"]["max_payload_products"], 10)
        self.assertTrue(all(len(row["choices"]["groups"][0]["products"]) == 10 for row in result["updates"]))

    def test_wrong_source_link_holds_family(self):
        catalogue, shopify = fixture()
        source = catalogue["products"][0]
        source["menus"][0]["values"][1].update({
            "target_url": catalogue["products"][3]["source_url"], "target_sku": "SKU_4"})
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["choice_products"], 0)
        self.assertEqual(result["summary"]["held_groups"], 1)
        self.assertIn("source_link_changes_other_option", {issue["reason"] for issue in result["holds"][0]["issues"]})

    def test_missing_source_target_holds_family(self):
        catalogue, shopify = fixture()
        catalogue["products"][0]["menus"][0]["values"][1]["target_url"] = "https://evil.example/product/x/"
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["choice_products"], 0)
        self.assertTrue(result["holds"])

    def test_duplicate_shopify_sku_is_not_guessed(self):
        catalogue, shopify = fixture()
        other = copy.deepcopy(shopify[0]);other["id"] += "9";shopify.append(other)
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["choice_products"], 0)
        self.assertEqual(result["summary"]["eligible_products"], 3)

    def test_duplicate_source_sku_cannot_write_delivery_twice(self):
        catalogue, shopify = fixture()
        other = copy.deepcopy(catalogue["products"][0])
        other["stock_messages"] = [{"text": "Niet op voorraad"}]
        catalogue["products"].append(other)
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["eligible_products"], 3)
        self.assertNotIn("SKU_1", {row["sku"] for row in result["updates"]})
        self.assertEqual(len(result["updates"]), len({row["product_id"] for row in result["updates"]}))

    def test_invalid_source_url_cannot_write_delivery(self):
        catalogue, shopify = fixture()
        catalogue["products"][0]["source_url"] = "https://evil.example/product/sku_1/"
        result = build_plan(catalogue, shopify)
        self.assertEqual(result["summary"]["eligible_products"], 3)
        self.assertNotIn("SKU_1", {row["sku"] for row in result["updates"]})

    def test_duplicate_complete_combination_holds_family(self):
        catalogue, shopify = fixture()
        catalogue["products"][1]["selected_options"] = dict(catalogue["products"][0]["selected_options"])
        result = build_plan(catalogue, shopify)
        reasons = {x["reason"] for h in result["holds"] for x in h["issues"]}
        self.assertIn("duplicate_complete_combination", reasons)
        self.assertEqual(result["summary"]["choice_products"], 0)

    def test_archived_target_has_disabled_value_but_no_url(self):
        catalogue, shopify = fixture()
        shopify[2]["status"] = "ARCHIVED"
        result = build_plan(catalogue, shopify)
        row = result["updates"][0]
        group = row["choices"]["groups"][0]
        self.assertEqual(group["menus"][0]["values"], ["Wit", "Mat Wit"])
        self.assertNotIn(shopify[2]["handle"], {r["handle"] for r in group["products"]})
        self.assertEqual(result["summary"]["eligible_products"], 3)

    def test_unknown_quantity_does_not_create_fake_stock(self):
        catalogue, shopify = fixture()
        shopify[0]["variants"]["nodes"][0].update(inventoryQuantity=0, inventoryPolicy="DENY")
        result = build_plan(catalogue, shopify)
        self.assertTrue(result["updates"][0]["delivery"]["in_stock"])
        self.assertIn("source_available_shopify_quantity_zero_deny", result["summary"]["warnings"])
        self.assertNotIn("inventoryQuantity", result["updates"][0])

    def test_expected_week_is_verbatim_not_invented_date(self):
        catalogue, _ = fixture();source = catalogue["products"][0]
        source["stock_messages"] = [{"text": "Verwacht: Week 50"}]
        source["delivery_messages"] = ["Verwacht: Week 50"]
        value, warnings = delivery(source)
        self.assertFalse(value["in_stock"])
        self.assertEqual(value["expected_text"], "Verwacht: Week 50")
        self.assertEqual(warnings, [])

    def test_conflicting_stock_is_unknown(self):
        catalogue, _ = fixture();source = catalogue["products"][0]
        source["stock_messages"].append({"text": "Verwacht: Week 6"})
        value, warnings = delivery(source)
        self.assertIsNone(value["in_stock"])
        self.assertIsNone(value["expected_text"])
        self.assertIn("conflicting_source_stock_or_expectation", warnings)

    def test_own_bundle_insufficient_stock_is_unavailable(self):
        catalogue, _ = fixture();source = catalogue["products"][0]
        source["stock_messages"] = [{"text": "Insufficient stock", "class": "stock out-of-stock"}]
        value, warnings = delivery(source)
        self.assertFalse(value["in_stock"])
        self.assertIsNone(value["expected_text"])
        self.assertNotIn("no_explicit_source_stock_state", warnings)

    def test_discontinued_is_explicit_and_has_no_expected_date(self):
        catalogue, _ = fixture();source = catalogue["products"][0]
        source["stock_messages"] = [{"text": "Nooit meer Leverbaar"}]
        value, warnings = delivery(source)
        self.assertTrue(value["discontinued"])
        self.assertFalse(value["in_stock"])
        self.assertIsNone(value["expected_text"])
        self.assertIn("source_discontinued", warnings)


if __name__ == "__main__":
    unittest.main()
