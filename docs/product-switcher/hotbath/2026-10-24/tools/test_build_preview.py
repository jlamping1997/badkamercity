import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import build_preview as builder


ROOT = Path(__file__).resolve().parent


class HotbathPreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "catalog_snapshot.json").read_text())
        cls.data, cls.rows = builder.build_data(cls.catalog)
        cls.group = cls.data["groups"][0]
        cls.by_sku = {row["sku"]: row for row in cls.rows}

    def test_default_set_matches_official_book(self):
        self.assertEqual(builder.sku_options("IBS70CR"), {
            "kleur": "Chroom",
            "breedte_diameter_hoofddouche": "20 cm",
            "type_bevestiging_hoofddouche": "Wandarm",
            "type_handdouche": "Staafmodel",
            "bevestiging_handdouche": "Wandhouder",
        })

    def test_combined_option_codes_match_official_book(self):
        self.assertEqual(builder.sku_options("IBS70BCP127"), {
            "kleur": "Geborsteld koper PVD",
            "breedte_diameter_hoofddouche": "20 cm",
            "type_bevestiging_hoofddouche": "Plafondbuis 15 cm",
            "type_handdouche": "Rond model",
            "bevestiging_handdouche": "Glijstang",
        })
        self.assertEqual(builder.sku_options("IBS70AI1357")["breedte_diameter_hoofddouche"], "30 cm")

    def test_other_families_and_test_skus_never_enter_scope(self):
        for sku in ["IBS7009CR", "IBSW70CR", "TEST-HOTBATH-IBS70CR347", "HBCB7067", "CB7067EXTCR"]:
            with self.subTest(sku=sku):
                self.assertIsNone(builder.sku_options(sku))
        self.assertEqual(len(self.rows), 359)
        self.assertFalse(any(row["sku"].startswith("TEST") for row in self.rows))

    def test_missing_ai4_is_not_fabricated_or_replaced(self):
        self.assertNotIn("IBS70AI4", self.by_sku)
        desired = builder.sku_options("IBS70AI4")
        self.assertFalse(any(row["options"] == desired for row in self.rows))
        self.assertIn("IBS70AI", self.by_sku)
        self.assertIn("IBS70AI5", self.by_sku)

    def test_wall_and_freestanding_dispensers_remain_separate_color_groups(self):
        all_handles = set()
        for model in ["BAA09", "BAA10"]:
            data, rows = builder.build_color_data(self.catalog, model)
            group = data["groups"][0]
            self.assertEqual(len(rows), 12)
            self.assertEqual([menu["key"] for menu in group["menus"]], ["kleur"])
            self.assertEqual(len(group["menus"][0]["values"]), 12)
            self.assertTrue(all(row["sku"].startswith(model) for row in rows))
            self.assertFalse(all_handles & {row["handle"] for row in rows})
            all_handles.update(row["handle"] for row in rows)

    def test_existing_baa03_eight_records_are_preserved_and_four_colors_added(self):
        shared = json.loads((ROOT / "baseline/product-switcher-data.json").read_text())
        group_id = builder.COLOR_GROUPS["BAA03"]["id"]
        original = next(group for group in shared["groups"] if group["id"] == group_id)
        before = copy.deepcopy(original)
        data, rows = builder.build_color_data(self.catalog, "BAA03", original)
        augmented = data["groups"][0]
        self.assertEqual(original, before)
        self.assertEqual(augmented["products"][:8], original["products"])
        self.assertEqual(len(augmented["products"]), 12)
        self.assertEqual({row["sku"] for row in rows if not row["current_group"]}, {"BAA03CR", "BAA03BB", "BAA03WH", "BAA03BGP"})
        self.assertEqual(augmented["id"], original["id"])

    def test_current_mixed_title_format_has_same_real_sku_tuple(self):
        actual = self.by_sku["IBS70CR347"]
        self.assertEqual(actual["options"], builder.sku_options("IBS70CR347"))
        self.assertIn("Ø 25 cm", actual["title"])

    def test_every_choice_tuple_maps_to_exactly_one_real_url(self):
        keys = [menu["key"] for menu in self.group["menus"]]
        tuples = [tuple(row["options"][key] for key in keys) for row in self.rows]
        self.assertEqual(len(tuples), len(set(tuples)))
        self.assertEqual(len(self.rows), len({row["url"] for row in self.rows}))
        for row in self.rows:
            self.assertEqual(row["url"], "/products/" + row["handle"])
            for menu in self.group["menus"]:
                self.assertIn(row["options"][menu["key"]], menu["values"])

    def test_scope_allowlist_matches_full_handles_only(self):
        snippet = builder.scope_snippet(self.rows)
        first = self.rows[0]["handle"]
        self.assertIn("|" + first + "|", snippet)
        self.assertIn("prepend: '|' | append: '|'", snippet)
        self.assertNotIn("TEST-HOTBATH", snippet)
        self.assertNotIn("ibs7009", snippet)
        self.assertIn("product.vendor == 'Hotbath'", snippet)

    def test_disagreement_or_duplicate_cannot_build_a_menu(self):
        duplicate = copy.deepcopy(self.catalog)
        original = next(product for product in duplicate["products"] if product["variants"]["nodes"][0]["sku"] == "IBS70CR")
        duplicate["products"].append(copy.deepcopy(original))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            builder.build_data(duplicate)
        mismatch = copy.deepcopy(self.catalog)
        product = next(product for product in mismatch["products"] if product["variants"]["nodes"][0]["sku"] == "IBS70CR")
        product["title"] = product["title"].replace("20cm hoofddouche", "30cm hoofddouche")
        with self.assertRaisesRegex(ValueError, "disagreement"):
            builder.build_data(mismatch)

    def test_existing_group_has_priority_and_unrelated_assets_stay_unchanged(self):
        source = ROOT / "baseline/preview-source"
        before_js = (source / "assets/bc-product-switcher.js").read_bytes()
        baseline_shared = (ROOT / "baseline/product-switcher-data.json").read_bytes()
        shared = json.loads(baseline_shared)
        cb003_before = next(group for group in shared["groups"] if group["id"] == "hotbath-cobber-cb003-wastafelkraan")
        self.assertEqual(len(cb003_before["products"]), 62)
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "theme"
            manifest = builder.run(source, ROOT / "catalog_snapshot.json", output)
            patched_main = (output / "sections/main-product.liquid").read_text()
            self.assertIn("if current_switch_group == blank\n      capture current_switch_group", patched_main)
            self.assertIn("data_url: bc_switcher_data_url", patched_main)
            after_js = (output / "assets/bc-product-switcher.js").read_bytes()
            before_matching = before_js.decode().split("  function findExactMatch", 1)[1].split("  function getDisplayType", 1)[0]
            after_matching = after_js.decode().split("  function findExactMatch", 1)[1].split("  function getDisplayType", 1)[0]
            self.assertEqual(before_matching, after_matching)
            self.assertIn("root?.dataset?.bcPreservePosition === 'true'", after_js.decode())
            self.assertFalse((output / "assets/product-switcher-data.json").exists())
            self.assertFalse(manifest["shopify_product_mutations"])
            self.assertFalse(manifest["shared_switcher_dataset_changed"])
            self.assertEqual(manifest["group_count"], 4)
            self.assertEqual(manifest["product_count"], 395)
            self.assertEqual(manifest["newly_linked_product_count"], 387)
            self.assertNotIn("when 'hotbath-cobber-cb003-wastafelkraan'", patched_main)
            self.assertIn("when 'hotbath-more-handdoekhaak-verouderd-messing-baa03ab'", patched_main)
            scope = (output / "snippets/bc-hotbath-preview-group.liquid").read_text()
            self.assertIn("|hotbath-baa03cr|", scope)
            self.assertNotIn("|hotbath-more-handdoekhaak-verouderd-messing-baa03ab|", scope)
        self.assertEqual(baseline_shared, (ROOT / "baseline/product-switcher-data.json").read_bytes())
        self.assertEqual(cb003_before, next(group for group in json.loads(baseline_shared)["groups"] if group["id"] == cb003_before["id"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
