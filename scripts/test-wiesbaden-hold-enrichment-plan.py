#!/usr/bin/env python3
"""Release regressions: protected identities, missing CSV, exact source allowlists."""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("holds", Path(__file__).with_name("wiesbaden-hold-enrichment-plan.py"))
holds = importlib.util.module_from_spec(spec)
spec.loader.exec_module(holds)


class HoldReleaseTests(unittest.TestCase):
    def test_verified_rules_cannot_release_protected_missing_csv_or_existing_review(self):
        rule = {"sku": "001.1000", "product_id": "product1", "variant_id": "variant1", "identity_verified": True,
                "disposition": "RELEASE_WITH_FIELD_OMISSIONS"}
        source = {"sku": "001.1000", "source_brand": "Wiesbaden", "source_url": "https://www.wiesbaden.nl/test",
                  "source_evidence": {"url": "https://www.wiesbaden.nl/test", "http_status": 200, "sha256": "a" * 64}}
        target = {"id": "product1", "vendor": "Wiesbaden", "variants": {"nodes": [{"id": "variant1", "sku": "001.1000"}], "pageInfo": {"hasNextPage": False}},
                  "contentReview": None, "completeSpecs": None}
        current = {"id": "product1", "hasOnlyDefaultVariant": True}
        rows, held = [{"merk": "Wiesbaden"}], {"001.1000"}
        self.assertTrue(holds.identity_ok(rule, source, target, current, rows, held, set()))
        self.assertFalse(holds.identity_ok(rule, source, target, current, rows, held, held))
        self.assertFalse(holds.identity_ok(rule, source, target, current, [], held, set()))
        target["contentReview"] = {"value": "{}"}
        self.assertFalse(holds.identity_ok(rule, source, target, current, rows, held, set()))
        target["contentReview"] = None
        target["variants"]["nodes"][0]["sku"] = "001.100"
        self.assertFalse(holds.identity_ok(rule, source, target, current, rows, held, set()))
        for blocked in holds.PLATFORM_BLOCKED:
            rule["sku"] = source["sku"] = target["variants"]["nodes"][0]["sku"] = blocked
            self.assertFalse(holds.identity_ok(rule, source, target, current, rows, {blocked}, set()))

    def test_allowlist_omits_only_reviewed_fields_and_rejects_modified_facts(self):
        facts = [{"label": k, "value": v} for k, v in (("SKU", "001.1000"), ("Merk", "Wiesbaden"), ("Serie", "Conflict"), ("Met overloop", "Nee"))]
        source = {"sku": "001.1000", "name": "Test", "specifications": facts}
        proposal = {"value": [{"group": "Product", "items": [{"key": "fabrikantnummer" if f["label"] == "SKU" else holds.enrichment.slug(f["label"]),
                    "label": f["label"], "value": f["value"]} for f in facts]}]}
        approved = [{"group": "Product", "items": [x.copy() for x in proposal["value"][0]["items"] if x["key"] != "serie"]}]
        rule = {"allow_spec_keys": ["fabrikantnummer", "merk", "met_overloop"], "exclude_spec_keys": ["serie"], "approved_spec_groups": approved}
        groups, omitted, keys = holds.reviewed_groups(source, proposal, rule)
        self.assertEqual(keys, {"fabrikantnummer", "merk", "met_overloop"})
        self.assertIn({"key": "serie", "reason": "REVIEWED_HOLD_FIELD_OMISSION"}, omitted)
        self.assertEqual(groups[0]["items"][-1]["value"], "Nee")
        approved[0]["items"][-1]["value"] = "Ja"
        with self.assertRaises(ValueError):
            holds.reviewed_groups(source, proposal, rule)


if __name__ == "__main__":
    unittest.main()
