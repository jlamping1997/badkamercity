"""Offline mapping checks; optional integration uses the reviewed private source.

BC_VARIANT_SOURCE_FILE can point at a local copy of the deployed worker.
The integration only executes module definitions, never its CLI/main routine.
"""
import copy
from decimal import Decimal
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import Mock


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("variant_worker_patch", HERE / "variant_worker_patch.py")
patcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(patcher)
HELPERS = {"Decimal": Decimal, "re": re}
exec(compile(patcher.HELPERS, "<variant-helpers>", "exec"), HELPERS)
SOURCE = Path(os.environ.get("BC_VARIANT_SOURCE_FILE",
              str(HERE.parents[2] / "search-runtime-current" / "sync.py")))


def variant(identity=1, sku="TEST-1", price="10.00"):
    return {"id": "gid://shopify/ProductVariant/" + str(identity), "sku": sku, "price": price}


def product(identity=1, variants=None):
    return {"id": "gid://shopify/Product/" + str(identity), "title": "Testproduct " + str(identity),
            "handle": "testproduct-" + str(identity), "vendor": "Testmerk", "productType": "Testproduct",
            "status": "ACTIVE", "onlineStoreUrl": "https://example.test/products/testproduct-" + str(identity),
            "updatedAt": "2026-11-05T00:00:00Z", "_variants": variants if variants is not None else [variant()],
            "_collections": [{"id": "gid://shopify/Collection/1", "handle": "testproducten"}],
            "_filters": [], "featuredMedia": None}


def schema():
    return {"name": "legacy", "fields": [
        {"name": name, "type": kind, "optional": True}
        for name, kind in [("title", "string"), ("sku", "string"), ("sku_exact", "string"),
                           ("price_cents", "int64"), ("f_productsoort", "string"),
                           ("f_kleur", "string"), ("f_serie", "string")]]}


DEFINITIONS = [{"key": key, "field": field, "data_type": "string", "type": "string", "label": label}
               for key, field, label in [("kleur", "f_kleur", "Kleur"), ("serie", "f_serie", "Serie")]]
CATEGORIES = {"gid://shopify/Collection/1": {"id": "gid://shopify/Collection/1",
              "handle": "testproducten", "title": "Testproducten"}}


class VariantSummaryTests(unittest.TestCase):
    def summary(self, variants):
        return HELPERS["_bc_variant_summary"](product(variants=variants))

    def test_sixteen_options_keep_all_skus_and_choose_lowest_price(self):
        variants = [variant(100 + index, "TEST-" + str(index), str(40 - index) + ".00")
                    for index in range(16)]
        result = self.summary(variants)
        self.assertEqual(result["variant"]["id"], variants[-1]["id"])
        self.assertEqual(result["sku_aliases"], sorted("test-" + str(index) for index in range(16)))
        self.assertTrue(result["price_varies"])
        self.assertEqual(result["variant_count"], 16)

    def test_equal_prices_use_numeric_variant_id_independent_of_order(self):
        first = variant(10, "TEN")
        second = variant(2, "TWO")
        self.assertEqual(self.summary([first, second])["variant"], second)
        self.assertEqual(self.summary([second, first])["variant"], second)
        self.assertFalse(self.summary([first, second])["price_varies"])

    def test_real_zero_price_is_preserved(self):
        result = self.summary([variant(1, "ZERO", "0.00"), variant(2)])
        self.assertEqual(result["variant"]["sku"], "ZERO")
        self.assertTrue(result["price_varies"])

    def test_secondary_invalid_price_stops_before_any_index_import(self):
        for value in ["NaN", "Infinity", "-0.01", "1.001", "", None, True]:
            with self.subTest(value=value), self.assertRaisesRegex(RuntimeError, "variantprijs"):
                self.summary([variant(1), variant(2, "BAD", value)])

    def test_empty_variant_export_is_refused(self):
        with self.assertRaisesRegex(RuntimeError, "Geen varianten"):
            self.summary([])

    def test_missing_or_duplicate_variant_identity_is_refused(self):
        for variants in [[{"sku": "MISSING", "price": "1.00"}], [variant(), variant()]]:
            with self.subTest(variants=variants), self.assertRaises(RuntimeError):
                self.summary(variants)

    def test_aliases_are_deduplicated_normalized_and_never_invented(self):
        result = self.summary([variant(1, " AbC "), variant(2, "abc"), variant(3, None), variant(4, "")])
        self.assertEqual(result["sku_aliases"], ["abc"])
        self.assertEqual(result["variant"]["sku"], " AbC ")

    def test_schema_adds_optional_fields_without_mutating_legacy(self):
        original = schema()
        before = copy.deepcopy(original)
        result = HELPERS["_bc_add_variant_schema"](original)
        self.assertEqual(original, before)
        self.assertEqual(result["fields"][:-2], original["fields"])
        self.assertEqual(result["fields"][-2], {"name": "sku_aliases", "type": "string[]", "facet": True, "optional": True})
        self.assertEqual(HELPERS["_bc_add_variant_schema"](result), result)

    def test_conflicting_schema_field_is_refused(self):
        original = schema()
        original["fields"].append({"name": "sku_aliases", "type": "string", "optional": True})
        with self.assertRaisesRegex(RuntimeError, "variantschemaveld"):
            HELPERS["_bc_add_variant_schema"](original)

    def test_probe_handles_reused_sku_without_duplicate_product_cards(self):
        docs = [{"id": "2", "sku_exact": "primary", "sku_aliases": ["primary", "secondary"],
                 "price_cents": 1000, "price_varies": True},
                {"id": "1", "sku_exact": "other", "sku_aliases": ["other", "secondary"],
                 "price_cents": 1200, "price_varies": False}]
        sample = HELPERS["_bc_variant_probe"](docs)
        self.assertEqual(sample["query"], "secondary")
        self.assertEqual(set(sample["expected"]), {"1", "2"})
        self.assertIsNone(HELPERS["_bc_variant_probe"]([]))

    def test_hot_check_rejects_wrong_price_or_missing_aliases(self):
        namespace = dict(HELPERS)
        expected = {"1": {"sku_aliases": ["a", "b"], "price_cents": 1000, "price_varies": True}}
        snapshot = {"variant_probe": {"query": "b", "expected": expected}}
        for fields, passes in [(expected["1"], True), ({**expected["1"], "price_cents": 1100}, False),
                               ({"price_cents": 1000, "price_varies": True}, False)]:
            namespace["probe"] = lambda *args, fields=fields: ({"found": 1, "products": [{"id": "1", **fields}]}, {})
            exec(compile(patcher.HELPERS, "<variant-helpers>", "exec"), namespace)
            result = namespace["_bc_variant_hot_check"](snapshot, "http://example.test", "Test")
            self.assertEqual(result[0]["passed"], passes)

    def test_unknown_worker_bytes_are_never_patched(self):
        with self.assertRaisesRegex(RuntimeError, "Workerhash"):
            patcher.patch_worker("print('different worker')\n")


@unittest.skipUnless(SOURCE.is_file(), "Reviewed private worker source not present")
class ReviewedWorkerIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text()
        if hashlib.sha256(cls.source.encode()).hexdigest() != patcher.BASE_WORKER_SHA256:
            raise AssertionError("The supplied integration worker is not the reviewed version")
        cls.patched = patcher.patch_worker(cls.source)

    def load(self, source=None):
        namespace = {"__name__": "_offline_worker_test", "__file__": str(SOURCE)}
        exec(compile(source or self.patched, "<offline-worker>", "exec"), namespace)
        return namespace

    def normalize(self, namespace, products):
        return namespace["normalize_products"](products, CATEGORIES, DEFINITIONS,
                 namespace.get("_bc_add_variant_schema", lambda value: value)(schema()))

    def test_single_variant_fields_remain_exactly_the_same(self):
        fixture = product()
        fixture["manifest"] = {"value": json.dumps({"format": "verified-product-filters-v1",
                              "sku": "TEST-1", "values": {"kleur": "RVS", "serie": "Testserie"}})}
        original = self.normalize(self.load(self.source), [copy.deepcopy(fixture)])[0][0]
        current = self.normalize(self.load(), [copy.deepcopy(fixture)])[0][0]
        self.assertEqual(current.pop("sku_aliases"), ["test-1"])
        self.assertFalse(current.pop("price_varies"))
        self.assertEqual(current, original)

    def test_sixteen_variants_create_one_product_and_no_variant_manifest_inheritance(self):
        namespace = self.load()
        fixture = product(variants=[variant(100 + index, "TEST-" + str(index), str(40 - index) + ".00")
                                    for index in range(16)])
        fixture["manifest"] = {"value": json.dumps({"format": "verified-product-filters-v1",
                              "sku": "TEST-15", "values": {"kleur": "Invented variant color"}})}
        fixture["color"] = {"value": "Geborsteld RVS"}
        docs, stats, issues = self.normalize(namespace, [fixture])
        self.assertEqual(len(docs), 1)
        self.assertEqual(docs[0]["id"], "1")
        self.assertEqual(docs[0]["price_cents"], 2500)
        self.assertEqual(docs[0]["sku"], "TEST-15")
        self.assertEqual(docs[0]["f_kleur"], "Geborsteld RVS")
        self.assertEqual(docs[0]["collection_ids"], ["gid://shopify/Collection/1"])
        self.assertEqual(stats["multi_variant_products"], 1)
        self.assertEqual(stats["variants"], 16)
        snapshot = {"variant_aliases_v1": True, "exact": docs[0]["sku_aliases"],
                    "profiles": {"__all__": {"service_category": False, "filters": [], "allowed_filters": []}}}
        for sku in docs[0]["sku_aliases"]:
            self.assertEqual([item["id"] for item in namespace["selected"](docs, snapshot, {"q": sku})], ["1"])

    def test_spom_exclusion_and_explicit_product_fields_survive(self):
        namespace = self.load()
        fixtures = [product(1, [variant(1, "SPOM1"), variant(2, "SPOM2")]),
                    product(2, [variant(3, "SPOM3"), variant(4, "RETAIL")])]
        fixtures[1]["_filters"] = [{"key": "serie", "value": "Testserie", "updatedAt": "2026-11-05T00:00:00Z"}]
        docs, _, _ = self.normalize(namespace, fixtures)
        self.assertFalse(docs[0]["general_shopping"])
        self.assertTrue(docs[1]["general_shopping"])
        self.assertEqual(docs[1]["f_serie"], "Testserie")

    def test_rvs_policy_still_normalizes_aliases_and_preserves_pvd(self):
        namespace = self.load()
        fixtures = [product(1, [variant(1), variant(2)]), product(2, [variant(3), variant(4)])]
        fixtures[0]["color"] = {"value": "RVS geborsteld"}
        fixtures[1]["color"] = {"value": "Geborsteld RVS PVD"}
        docs, _, _ = self.normalize(namespace, fixtures)
        namespace["enrich_b2c_documents"](docs, DEFINITIONS, schema())
        self.assertEqual([item["f_kleur"] for item in docs], ["Geborsteld RVS", "Geborsteld RVS PVD"])

    def test_prepare_stages_alias_schema_snapshot_and_api_checks_without_activation(self):
        namespace = self.load()
        fixtures = [product(1, [variant(1, "PRIMARY", "10.00"), variant(2, "SECONDARY", "20.00")])]
        profile = {"title": "Alle producten", "products": 1, "shopping_products": 1,
                   "service_category": False, "b2c_policy": {"review_required": False},
                   "filters": [], "allowed_filters": []}
        class FakeTypesense:
            legacy = "legacy"
            staged = None
            documents = None
            path = staticmethod(lambda name: "/collections/" + name)
            def call(self, path, method="GET", body=None):
                if path == "/collections/legacy": return schema()
                if method == "POST": self.staged = json.loads(body)
                return None
            def import_docs(self, name, docs): self.documents = copy.deepcopy(docs)
            def export(self, name): return copy.deepcopy(self.documents)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "sync"
            root.mkdir()
            live = Path(temp) / "live"
            live.mkdir()
            (live / "filter_definitions.json").write_text(json.dumps(DEFINITIONS))
            (live / "profiles.json").write_text("{}")
            (live / "app.py").write_text("# Original API remains unchanged\n")
            api_checks = Mock(return_value=[{"name": "Isolated API checks", "passed": True}])
            namespace.update(ROOT=root, LIVE=live, SNAPSHOT=live / "bc_sync/active.json",
                log=lambda message: None,
                source_fingerprint=lambda *args: {"count": 1},
                parse_export=lambda path: copy.deepcopy(fixtures),
                make_profiles=lambda *args: {"__all__": copy.deepcopy(profile)},
                independent_memberships=lambda *args: [], check_b2c_profiles=lambda *args: [],
                check_api=api_checks,
                patch_api=lambda source: source)
            shop = Mock()
            shop.collection_map.return_value = CATEGORIES
            shop.export.return_value = 1
            ts = FakeTypesense()
            directory = namespace["prepare"](shop, ts)
            snapshot = json.loads((directory / "snapshot.json").read_text())
            self.assertTrue(snapshot["variant_aliases_v1"])
            self.assertEqual(snapshot["exact"], ["primary", "secondary"])
            self.assertEqual(snapshot["variant_probe"]["query"], "secondary")
            self.assertEqual(snapshot["profiles"]["__all__"]["products"], 1)
            self.assertEqual(len(ts.documents), 1)
            self.assertEqual({field["name"] for field in ts.staged["fields"]} - {field["name"] for field in schema()["fields"]},
                             {"sku_aliases", "price_varies"})
            api_checks.assert_called_once()
            self.assertEqual(api_checks.call_args.args[1]["variant_probe"], snapshot["variant_probe"])
            self.assertFalse(namespace["SNAPSHOT"].exists())
            self.assertEqual((live / "app.py").read_text(), "# Original API remains unchanged\n")

    def test_worker_patch_preserves_other_definitions_and_cli(self):
        original = __import__("ast").parse(self.source)
        changed = __import__("ast").parse(self.patched)
        before = {node.name: __import__("ast").dump(node) for node in original.body
                  if isinstance(node, (__import__("ast").FunctionDef, __import__("ast").ClassDef))}
        after = {node.name: __import__("ast").dump(node) for node in changed.body
                 if isinstance(node, (__import__("ast").FunctionDef, __import__("ast").ClassDef))}
        expected = {"normalize_products", "patch_api", "selected", "make_cases", "check_api", "prepare", "hot_checks"}
        self.assertEqual({name for name in before if before[name] != after[name]}, expected)
        self.assertEqual(before["activate"], after["activate"])
        self.assertEqual(before["restore_transaction"], after["restore_transaction"])
        self.assertEqual(before["main"], after["main"])


if __name__ == "__main__":
    unittest.main()
