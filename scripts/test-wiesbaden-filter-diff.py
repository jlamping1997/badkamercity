#!/usr/bin/env python3
"""Focused checks: missing is not blank, definitions gate writes, CAS is retained."""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("filters", Path(__file__).with_name("wiesbaden-filter-diff.py"))
filters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(filters)


class FilterDiffTests(unittest.TestCase):
    def fixture(self):
        candidate = {"namespace": "bc_filters", "key": "kleur", "type": "single_line_text_field", "value": "Wit", "source_label": "Kleur", "source_value": "Wit"}
        manifest = {"items": [{"sku": "001.1000", "product_id": "gid://shopify/Product/1", "metafields": [{"key": "complete_specificaties"}], "filter_candidates": [candidate]}]}
        snapshot = {"pagination_complete": True, "products": [{"id": "gid://shopify/Product/1", "hasOnlyDefaultVariant": True,
                    "metafields": {"nodes": [], "pageInfo": {"hasNextPage": False}}}]}
        definition = {"id": "definition1", "namespace": "bc_filters", "key": "kleur", "ownerType": "PRODUCT", "type": {"name": "single_line_text_field"},
                      "access": {"admin": "PUBLIC_READ_WRITE"}, "validations": []}
        return manifest, snapshot, {"pagination_complete": True, "definitions": [definition]}

    def test_create_if_absent_and_blank_never_overwrites(self):
        m, s, d = self.fixture()
        result = filters.build(m, s, d)
        self.assertIsNone(result["items"][0]["metafields"][0]["compareDigest"])
        self.assertEqual(result["items"][0]["sku"], "001.1000")
        m["items"][0]["filter_candidates"][0]["value"] = ""
        s["products"][0]["metafields"]["nodes"] = [{"namespace": "bc_filters", "key": "kleur", "type": "single_line_text_field", "value": "Zwart", "compareDigest": "abc"}]
        self.assertEqual(filters.build(m, s, d)["items"][0]["metafields"], [])

    def test_cas_updates_equal_skip_and_definition_constraints(self):
        m, s, d = self.fixture()
        current = {"namespace": "bc_filters", "key": "kleur", "type": "single_line_text_field", "value": "Zwart", "compareDigest": "abc"}
        s["products"][0]["metafields"]["nodes"] = [current]
        self.assertEqual(filters.build(m, s, d)["items"][0]["metafields"][0]["compareDigest"], "abc")
        current["value"] = "Wit"
        self.assertEqual(filters.build(m, s, d)["summary"]["unchanged_fields"], 1)
        d["definitions"][0]["validations"] = [{"name": "choices", "value": '["Zwart"]'}]
        self.assertEqual(filters.build(m, s, d)["items"][0]["metafields"], [])

    def test_incomplete_connection_and_protected_product_cannot_write(self):
        m, s, d = self.fixture()
        s["products"][0]["metafields"]["pageInfo"]["hasNextPage"] = True
        self.assertEqual(filters.build(m, s, d)["items"][0]["metafields"], [])
        m["items"][0]["metafields"] = []
        self.assertEqual(filters.build(m, s, d)["items"], [])


if __name__ == "__main__":
    unittest.main()
