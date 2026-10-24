#!/usr/bin/env python3
"""Targeted regressions for optional conflicts, existing data, and fact binding."""
import importlib.util
import json
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("enrichment", Path(__file__).with_name("wiesbaden-enrichment-plan.py"))
enrichment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(enrichment)


class EnrichmentTests(unittest.TestCase):
    def test_reviewed_material_conflict_omits_only_the_exact_source_value(self):
        facts = [{"label": "SKU", "value": "28.8083"}, {"label": "Merk", "value": "Wiesbaden"},
                 {"label": "Materiaal", "value": "Messing"}, {"label": "Met overloop", "value": "Nee"}]
        product = {"sku": "28.8083", "name": "Alonzo", "specifications": facts}
        proposal = {"value": [{"group": "Product", "items": [{"key": "fabrikantnummer" if f["label"] == "SKU" else enrichment.slug(f["label"]),
                    "label": f["label"], "value": f["value"]} for f in facts]}]}
        conflict = {("materiaal", "Messing"): "REVIEWED_CSV_CACHE_MATERIAL_CONFLICT"}
        groups, omitted, keys = enrichment.clean_specs(product, proposal, conflict)
        self.assertNotIn("materiaal", keys)
        self.assertIn("met_overloop", keys)
        rows = [{"proposed_field": "bc_filters.materiaal", "proposed_type": "single_line_text_field", "proposed_value": "Messing",
                 "source_label": "Materiaal", "source_value": "Messing", "mapping_status": "TYPED_VALUE_CANDIDATE"}]
        self.assertEqual(enrichment.filter_candidates(rows, {f["key"]: f["value"] for g in groups for f in g["items"]})[0], [])
        facts[2]["value"] = proposal["value"][0]["items"][2]["value"] = "RVS"
        self.assertIn("materiaal", enrichment.clean_specs(product, proposal, conflict)[2])

    def test_explicit_bath_set_omits_conflicts_and_keeps_other_negative_facts(self):
        facts = [{"label": k, "value": v} for k, v in (("SKU", "29.2080"), ("Merk", "Wiesbaden"),
                 ("Met uitloop", "Nee"), ("Geschikt voor bad (inbouw in muur)", "Nee"),
                 ("Met douchegarnituur", "Nee"), ("Met hoofddouche", "Nee"), ("Coldstart", "Nee"), ("Aantal", "0"))]
        product = {"name": "Caral inbouwthermostaat 2 stopkranen compleet met baduitloop 20 cm en 3 standen handdouche chroom", "specifications": facts}
        proposal = {"value": [{"group": "Product", "items": [{"key": "fabrikantnummer" if f["label"] == "SKU" else enrichment.slug(f["label"]),
                    "label": f["label"], "value": f["value"]} for f in facts]}]}
        groups, omitted, keys = enrichment.clean_specs(product, proposal)
        self.assertEqual(keys, {"fabrikantnummer", "merk", "met_hoofddouche", "coldstart", "aantal"})
        self.assertEqual({x["key"] for x in omitted}, {"met_uitloop", "geschikt_voor_bad_inbouw_in_muur", "met_douchegarnituur"})
        flat = {f["key"]: f["value"] for g in groups for f in g["items"]}
        self.assertEqual(flat["coldstart"], "Nee")
        self.assertEqual(flat["aantal"], "0")

    def test_named_shower_set_omits_only_conflicting_fields_and_filters(self):
        facts = [{"label": k, "value": v} for k, v in (("SKU", "29.4090"), ("Merk", "Wiesbaden"),
                 ("Met hoofddouche", "Nee"), ("Geschikt voor douche", "Nee"),
                 ("Met douchegarnituur", "Nee"), ("Met afsluiter", "Nee"), ("Coldstart", "Nee"))]
        product = {"name": "Caral 2 stopkranen compleet met hoofddouche 30 cm", "specifications": facts}
        proposal = {"value": [{"group": "Product", "items": [{"key": "fabrikantnummer" if f["label"] == "SKU" else enrichment.slug(f["label"]),
                    "label": f["label"], "value": f["value"]} for f in facts]}]}
        groups, omitted, keys = enrichment.clean_specs(product, proposal)
        self.assertEqual(keys, {"fabrikantnummer", "merk", "coldstart"})
        self.assertEqual(len(omitted), 4)
        rows = [{"proposed_field": "bc_filters.met_hoofddouche", "proposed_type": "boolean", "proposed_value": False,
                 "source_label": "Met hoofddouche", "source_value": "Nee", "mapping_status": "TYPED_VALUE_CANDIDATE"}]
        self.assertEqual(enrichment.filter_candidates(rows, {f["key"]: f["value"] for g in groups for f in g["items"]})[0], [])
        groups, omitted, keys = enrichment.clean_specs(product, proposal, {("coldstart", "Nee"): "REVIEWED_CONFLICT"})
        self.assertNotIn("coldstart", keys)

    def test_conflict_omits_one_field_and_retains_no_zero(self):
        facts = [{"label": k, "value": v} for k, v in (("SKU", "001.1000"), ("Merk", "Wiesbaden"),
                 ("Kleur", "Wit"), ("Kleur", "Zwart"), ("Met overloop", "Nee"), ("Aantal", "0"),
                 ("Aantal kraangaten", "14-gats"), ("Inkoopprijs", "79.31"))]
        product = {"name": "Test", "specifications": facts, "issues": []}
        proposal = {"value": [{"group": "Product", "items": [{"key": "fabrikantnummer" if f["label"] == "SKU" else enrichment.slug(f["label"]),
                    "label": f["label"], "value": f["value"]} for f in facts]}]}
        groups, omitted, keys = enrichment.clean_specs(product, proposal)
        flat = {f["key"]: f["value"] for g in groups for f in g["items"]}
        self.assertEqual(flat, {"fabrikantnummer": "001.1000", "merk": "Wiesbaden", "met_overloop": "Nee", "aantal": "0"})
        self.assertNotIn("79.31", json.dumps(groups))
        self.assertIn("aantal_kraangaten", {x["key"] for x in omitted})

    def test_documents_are_exact_https_assets_and_preserve_existing(self):
        base = "https://korverholland.compano.com/Data/Lijntekeningen/"
        product = {"sku": "24.3710", "documents": [{"url": base + "24.371.pdf"}, {"url": "http://example.test/24.3710.pdf"}],
                   "images": [{"kind": "image", "url": base + "24.3710-photo.jpg"},
                              {"kind": "line_drawings", "url": base + "24.3710.jpg"}]}
        self.assertEqual(enrichment.document_urls(product), [base + "24.3710.jpg"])
        existing = "https://kh-compano.b-cdn.net/Data/Lijntekeningen/24.3710.jpg"
        target = {"id": "gid://shopify/Product/1", "variants": {"nodes": [{"sku": "24.3710"}]}, "collections": [],
                  "completeSpecs": None, "contentReview": None,
                  "technicalDocs": {"type": "list.url", "value": json.dumps([existing]), "compareDigest": "old"}}
        fields, _ = enrichment.target_fields(target, [], enrichment.document_urls(product), {"fabrikantnummer"}, [], "https://www.wiesbaden.nl/test", {}, "2026-10-21")
        self.assertNotIn("technische_documenten", {x["key"] for x in fields})
        marker = json.loads(next(x["value"] for x in fields if x["key"] == "content_review"))
        self.assertEqual(marker["product_id"], "1")
        self.assertIsNone(fields[0]["compareDigest"])
        target["contentReview"] = {"value": "{}", "compareDigest": "reviewed"}
        self.assertEqual(enrichment.target_fields(target, [], [], set(), [], "url", {}, "date")[0], [])

    def test_filters_bind_to_retained_exact_source_fact(self):
        rows = [{"proposed_field": "bc_filters.kleur", "proposed_type": "single_line_text_field",
                 "proposed_value": "Wit", "source_label": "Kleur", "source_value": "Wit", "mapping_status": "TYPED_VALUE_CANDIDATE"}]
        self.assertEqual(enrichment.filter_candidates(rows, {"kleur": "Zwart"})[0], [])
        self.assertEqual(enrichment.filter_candidates(rows, {"kleur": "Wit"})[0][0]["value"], "Wit")
        self.assertEqual(enrichment.filter_candidates(rows + rows, {"kleur": "Wit"})[0], [])
        rows[0]["proposed_value"] = "Zwart"
        self.assertEqual(enrichment.filter_candidates(rows, {"kleur": "Wit"})[0], [])


if __name__ == "__main__":
    unittest.main()
