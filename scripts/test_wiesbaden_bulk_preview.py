#!/usr/bin/env python3
"""13 offline regressietests; geef de originele (private) Wiesbaden datarun ZIP mee."""
import importlib.util
import json
import sys
import tempfile
import unittest
from collections import Counter, defaultdict
from pathlib import Path

MODULE = Path(__file__).with_name("wiesbaden-bulk-preview.py")
spec=importlib.util.spec_from_file_location("wiesbaden_bulk_preview",MODULE)
bulk=importlib.util.module_from_spec(spec)
spec.loader.exec_module(bulk)


class WiesbadenPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=Path(INPUT_ZIP)
        cls.db=(bulk.Snapshot if hasattr(bulk,"Snapshot") else bulk.Datarun)(cls.source)
        read_json=(cls.db.data if hasattr(cls.db,"data") else cls.db.json)
        read_records=(cls.db.records if hasattr(cls.db,"records") else cls.db.jsonl)
        cls.master=read_records("product-master.jsonl")
        mkindex=(bulk.row_index if hasattr(bulk,"row_index") else bulk.keyed)
        cls.categories, cls.dups_cat=mkindex(read_json("category-import-proposal.json"),"cat")
        cls.specs, cls.dups_spec=mkindex(read_json("complete-specifications-proposal.json"),"spec")
        cls.filters=defaultdict(list)
        for f in read_json("filter-field-proposal.json"): cls.filters[f["sku"]].append(f)
        cls.products, cls.dups=mkindex(cls.master,"master")
        cls.selection=(bulk.select_products(cls.master) if hasattr(bulk,"select_products") else bulk.selection(cls.master,50))

    def proposal(self,sku,changes=None):
        p=self.products[sku]
        return bulk.evaluate(p,self.categories.get(sku),changes or self.filters[sku],
                             self.specs.get(sku,{}),self.dups|self.dups_cat|self.dups_spec)

    def test_sample_50_nine_profiles(self):
        self.assertEqual(len(self.selection),50)
        self.assertEqual(len({p["sku"] for p in self.selection}),50)
        self.assertEqual(Counter(p["current_product_type"] for p in self.selection),
                         Counter({name:config[0] for name,config in bulk.PROFILES.items()}))

    def test_regression_skus_pinned(self):
        self.assertTrue({"24.3710","29.8007"}.issubset({p["sku"] for p in self.selection}))

    def test_only_existing_wiesbaden(self):
        for p in self.selection:
            self.assertEqual((p["comparison_status"],p["source_brand"],p["current_vendor"]),
                             ("EXISTING_WIESBADEN","Wiesbaden","Wiesbaden"))
            self.assertRegex(p["product_id"],r"^gid://shopify/Product/\d+$")

    def test_preserve_reviewed_243710(self):
        p=self.proposal("24.3710")
        self.assertEqual(p["status"],"EXISTING_REVIEWED_DO_NOT_REPLACE")
        self.assertIn("304",p["content_proposal"]["title"])
        self.assertNotIn("Grant",p["content_proposal"]["title"])
        self.assertFalse(p["write_permissions"]["shopify"])

    def test_part_conflict_298007_blocks(self):
        p=self.proposal("29.8007")
        self.assertIn("COLOUR_CONFLICT_TITLE_VS_BASISKLEUR",p["issues_blocking"])
        self.assertIn("PART_TYPE_CONFLICT_MODEL_INBOUWDEEL_VS_AFBOUWDEEL",p["issues_blocking"])
        self.assertIn("PART_COMPATIBILITY_NOT_VERIFIED",p["issues_blocking"])

    def test_wrong_category_241600_blocks(self):
        self.assertIn("CATEGORY_INCOMPATIBLE_WITH_PRODUCT_TYPE",self.proposal("24.1600")["issues_blocking"])

    def test_false_boolean_not_missing(self):
        self.assertIs(next(f for f in self.proposal("24.3710")["facts"] if f["label"]=="Zelfsluitend")["value"],False)

    def test_numeric_filter_parses_strictly(self):
        p=self.proposal("24.3710")
        flt=next(f for f in p["filters_proposal"] if f["field"]=="bc_filters.aantal_kraangaten")
        self.assertIs(type(flt["value"]),int)
        self.assertEqual(flt["value"],1)

    def test_boolean_filter_stays_boolean(self):
        flt=next(f for f in self.proposal("24.3710")["filters_proposal"] if f["field"]=="bc_filters.coldstart")
        self.assertIs(flt["value"],True)

    def test_changed_source_is_held(self):
        items=[dict(f) for f in self.filters["24.3710"]]
        items[0]["source_value"]="MANIPULATED SOURCE"
        self.assertTrue(any(f["reason"]=="FILTER_SOURCE_VALUE_CHANGED"
                            for f in self.proposal("24.3710",items)["filters_needing_review"]))

    def test_seo_html_and_provenance(self):
        for row in self.selection:
            p=self.proposal(row["sku"])
            copy=p["content_proposal"]
            self.assertLessEqual(len(copy["seo"]["title"]),60)
            self.assertLessEqual(len(copy["seo"]["description"]),155)
            self.assertNotRegex(copy["description_html"],r"<script|\bonclick\s*=")
            self.assertNotRegex(copy["seo"]["title"],r"\b(?:FSC|KIWA|EAN|GTIN)\b")
            self.assertTrue(all(f.get("source_sha256") for f in p["facts"]))

    def test_parts_and_sets_never_prematurely_approved(self):
        for row in self.selection:
            p=self.proposal(row["sku"])
            kind=bulk.PROFILES[row["current_product_type"]][4]
            if kind=="PART":self.assertIn("PART_COMPATIBILITY_NOT_VERIFIED",p["issues_blocking"])
            if kind=="SET":self.assertIn("SET_COMPONENTS_NOT_VERIFIED",p["issues_blocking"])

    def test_idempotent_50_outputs(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)
            first=bulk.run(self.source,out,50)
            digest=(out/"products"/"24.3710.json").read_bytes()
            again=bulk.run(self.source,out,50)
            self.assertEqual((first["generated"],again["generated"],again["reused"]),(50,0,50))
            self.assertEqual(digest,(out/"products"/"24.3710.json").read_bytes())


if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("Gebruik: python scripts/test_wiesbaden_bulk_preview.py PAD_NAAR_DATARUN.zip")
    INPUT_ZIP=sys.argv[1]
    sys.argv=[sys.argv[0]]
    unittest.main(verbosity=2)
