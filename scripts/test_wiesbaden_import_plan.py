import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("plan", Path(__file__).with_name("wiesbaden-import-plan.py"))
plan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan)


def product(name, path=None):
    return {"name": name, "categories": [{"url_path": "bekijk-assortiment/"+path}] if path else []}


class PlanTests(unittest.TestCase):
    def test_complete_tap_has_specific_source_category(self):
        self.assertEqual(plan.classify(product("304 wastafelkraan", "kranen/wastafelkranen/opbouw"))[0], "opbouw-wastafelkranen")

    def test_trim_part_is_not_complete_shower(self):
        self.assertEqual(plan.classify(product("Dreams afbouwdeel thermostatische douchekraan", "douche/douchekranen/inbouwkranen"))[0], "afbouwdelen-voor-kranen")

    def test_bath_set_not_shower_set(self):
        self.assertEqual(plan.classify(product("Caral inbouwthermostaat compleet met baduitloop"))[0], "inbouw-badkranen")

    def test_one_pack_thermostat_is_not_fountain_set(self):
        target, kind, reason = plan.classify(product("one-pack inbouwthermostaatset rond type 202"))
        self.assertNotEqual(target, "fonteinsets")
        self.assertIn("REVIEW", reason)
        self.assertEqual(plan.classify(product("One pack Leto fontein 33 cm"))[0], "fonteinsets")

    def test_spare_mirror_glass_is_not_shower_glass(self):
        self.assertIsNone(plan.classify(product("Glas voor spiegel"))[0])

    def test_main_tap_not_included_hand_shower(self):
        self.assertEqual(plan.classify(product("Keukenkraan met handdouche"))[0], "keukenkranen")

    def test_included_seat_not_main_product(self):
        self.assertEqual(plan.classify(product("Vesta wandcloset met toiletzitting"))[0], "hangtoiletten")

    def test_ambiguous_part_stays_for_review(self):
        self.assertIsNone(plan.classify(product("Houder voor handdouche"))[0])

    def test_boolean_false_is_preserved(self):
        d = {"key":"coldstart", "type":{"name":"boolean"}}
        self.assertEqual(plan.cast("Nee", d), (False, "TYPED_VALUE_CANDIDATE"))

    def test_measurement_needs_explicit_unit(self):
        d = {"key":"hoogte_mm", "type":{"name":"number_decimal"}}
        self.assertEqual(plan.cast("120 cm", d)[0], "1200")
        self.assertEqual(plan.cast("120", d)[1], "SOURCE_UNIT_MISSING_REVIEW")
        self.assertIsNone(plan.cast('1/2"', d)[0])

    def test_complete_specs_preserve_zero_and_negative_answer(self):
        groups = plan.grouped_specs({"specifications":[{"label":"Met afvoerplug","value":"Nee"},
                  {"label":"Aantal","value":"0"},{"label":"Hoogte","value":""}]})
        self.assertEqual([x["value"] for g in groups for x in g["items"]], ["Nee", "0"])

    def test_conflicting_filter_aliases_remain_for_review(self):
        definitions = [{"key":"met_overloop", "name":"Met overloop", "type":{"name":"boolean"}}]
        record = {"specifications":[{"label":"Overloop","value":"Nee"},
                                    {"label":"Met overloopgat","value":"Ja"}]}
        candidates = plan.filter_candidates(record, definitions)
        self.assertEqual(len(candidates), 2)
        self.assertTrue(all(x["mapping_status"] == "CONFLICTING_SOURCE_FACTS_REVIEW" for x in candidates))

    def test_existing_numeric_value_is_compared_as_number(self):
        snapshots = {"p": {"updatedAt":"2026-10-19T10:00:00Z", "metafields":{"nodes":[
            {"namespace":"custom", "key":"hoogte_mm", "type":"number_decimal", "value":"1200.0"}]}}}
        result = plan.current_change("p", "custom.hoogte_mm", "1200", snapshots)
        self.assertEqual(result["change_status"], "SAME_VALUE")
        self.assertEqual(result["current_value"], "1200.0")

    def test_generic_material_does_not_become_writable_fact(self):
        d = {"key":"materiaal", "type":{"name":"single_line_text_field"}}
        self.assertEqual(plan.cast("Overig", d), (None, "GENERIC_SOURCE_VALUE_REVIEW"))

    def test_explicit_hole_count_is_numeric_without_guessing(self):
        d = {"key":"aantal_kraangaten", "type":{"name":"number_integer"}}
        self.assertEqual(plan.cast("1-gats", d), ("1", "TYPED_VALUE_CANDIDATE"))
        self.assertIsNone(plan.cast("Optioneel", d)[0])


if __name__ == "__main__":
    unittest.main()
