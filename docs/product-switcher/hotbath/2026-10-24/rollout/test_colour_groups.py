#!/usr/bin/env python3
"""Regression checks for real catalogue exclusions and safe menu grouping."""
import copy
import json
import unittest
from pathlib import Path

import build_colour_groups as compiler

HERE=Path(__file__).resolve().parent

class ColourGroupsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=compiler.SOURCE
        cls.catalog=json.loads((cls.source/'catalog_snapshot.json').read_text())['products']
        cls.by_handle={p['handle']:p for p in cls.catalog}
        cls.by_sku={compiler.sku_of(p):p for p in cls.catalog}
        cls.old=json.loads((cls.source/'baseline/product-switcher-data.json').read_text())['groups']
        cls.groups=json.loads((HERE/'colour_groups.json').read_text())['groups']
        cls.group_index={g['id']:g for g in cls.groups}
        cls.provenance=json.loads((HERE/'colour_provenance.json').read_text())
        cls.review=json.loads((HERE/'colour_review.json').read_text())
        cls.records={p['handle']:p for g in cls.groups for p in g['products']}
        cls.additions=json.loads((HERE/'colour_option_additions.json').read_text())['additions']

    def test_real_spom_inside_title_is_excluded(self):
        self.assertEqual(compiler.exclusion(self.by_sku['G50']),'SPOM_EXCLUDED_BY_USER')
        self.assertNotIn(self.by_sku['G50']['handle'],self.records)
        self.assertEqual(sum('SPOM' in ' '.join([compiler.sku_of(p),p['title'],p['handle']]).upper() for p in self.catalog),697)

    def test_spom_test_draft_and_unpublished_gates(self):
        row=self.by_sku['BAA03CR']
        for field in ['title','handle','sku']:
            changed=copy.deepcopy(row)
            if field=='sku':changed['variants']['nodes'][0]['sku']='SPOM-BAA03CR'
            else:changed[field]+=' SPOM'
            self.assertEqual(compiler.exclusion(changed),'SPOM_EXCLUDED_BY_USER')
        for key,value in [('status','DRAFT'),('publishedAt',None)]:
            changed=copy.deepcopy(row);changed[key]=value
            self.assertEqual(compiler.exclusion(changed),'NOT_ACTIVE_PUBLISHED')
        changed=copy.deepcopy(row);changed['variants']['nodes'][0]['sku']='TEST-BAA03CR'
        self.assertEqual(compiler.exclusion(changed),'TEST_EXCLUDED')

    def test_old_groups_and_product_records_stay_unchanged(self):
        for group in self.old:
            self.assertIn(group['id'],self.group_index)
            for record in group['products']:
                actual=copy.deepcopy(self.records[record['handle']])
                allowed=next((a for a in self.additions if a['group_id']==group['id'] and a['handle']==record['handle']),None)
                if allowed:
                    self.assertEqual(actual['options'].pop(allowed['key']),allowed['value'])
                self.assertEqual(record,actual)

    def test_colour_option_addition_allowlist_is_limited_and_source_verified(self):
        self.assertEqual(len(self.additions),7)
        self.assertEqual({a['group_id'] for a in self.additions},set(compiler.ADDITIVE_COLOUR_GROUPS))
        for a in self.additions:
            self.assertEqual(a['key'],'kleur')
            self.assertEqual(compiler.sku_of(self.by_handle[a['handle']]),a['sku'])
            self.assertEqual(a['colour_code'],'IX')
            self.assertEqual(a['sources']['book_finish']['pdf_page'],63)
            self.assertEqual(a['sources']['book_finish']['manufacturer_label'],'RVS 316')

    def test_group_tuples_and_global_product_ownership_are_unique(self):
        handles=[]
        for group in self.groups:
            compiler.assert_group(group)
            for p in group['products']:
                self.assertIn(p['handle'],self.by_handle)
                self.assertIsNone(compiler.exclusion(self.by_handle[p['handle']]))
                handles.append(p['handle'])
        self.assertEqual(len(handles),len(set(handles)))

    def test_source_conflicts_never_enter_new_menus(self):
        for sku in compiler.SOURCE_CONFLICT_HOLDS | {'SDS32BGP','IBS33BGP4'}:
            self.assertNotIn(self.by_sku[sku]['handle'],self.records)

    def test_exclusive_book_families_not_duplicated(self):
        old_handles={p['handle'] for g in self.old for p in g['products']}
        for handle in self.records:
            if handle in old_handles:continue
            parsed=compiler.audit.split_sku(compiler.sku_of(self.by_handle[handle]))
            self.assertNotIn(parsed['model'],compiler.EXCLUSIVE_IBS)

    def test_full_title_config_has_one_group_per_model_and_literal_values(self):
        models=[]
        for gid,proof in self.provenance.items():
            if proof['basis']!='CATALOG_TITLE_VERIFIED_NOT_BOOK_OPTION_DECODE':continue
            models.append(proof['model'])
            group=self.group_index[gid]
            for record in group['products']:
                p=self.by_handle[record['handle']]
                parsed=compiler.audit.split_sku(compiler.sku_of(p))
                options,residual,missing=compiler.parse_title_configuration(p,parsed,proof['literal_fields'])
                self.assertFalse(missing)
                self.assertEqual(residual,proof['residual_signature'])
                self.assertEqual({k:options[k] for k in proof['literal_fields']},record['options'])
        self.assertEqual(len(models),len(set(models)))
        self.assertEqual(set(models),{'IBS2','IBS21','IBS22','IBS23','IBS24','IBS5','IBS5A','IBSX70','M538'})

    def test_without_rail_and_round_three_modes_read_correctly(self):
        p=self.by_sku['IBS2CR125']
        options,residual,missing=compiler.parse_title_configuration(p,compiler.audit.split_sku('IBS2CR125'))
        self.assertFalse(missing)
        self.assertEqual(options['bevestiging_handdouche'],'Wandhouder')
        self.assertEqual(options['type_handdouche'],'Rond model - 3 standen')

    def test_fixed_config_fallback_only_exposes_colour(self):
        fully_merged={p['model'] for p in self.provenance.values() if p['basis']=='CATALOG_TITLE_VERIFIED_NOT_BOOK_OPTION_DECODE'}
        found=[]
        for gid,proof in self.provenance.items():
            if proof['basis']!='COLOUR_ONLY_CONFIG_FIXED':continue
            self.assertNotIn(proof['model'],fully_merged)
            group=self.group_index[gid]
            self.assertEqual([m['key'] for m in group['menus']],['kleur'])
            for row in group['products']:
                parsed=compiler.audit.split_sku(compiler.sku_of(self.by_handle[row['handle']]))
                self.assertEqual(parsed['model'],proof['model'])
                self.assertEqual(parsed['configuration_suffix'],proof['configuration_suffix'])
            found.append(gid)
        self.assertEqual(len(found),25)

    def test_book_spout_lengths_keep_trim_and_complete_separate(self):
        for family in ['cb105ext','cb105text']:
            group=self.group_index['hotbath-book-'+family+'-keuzes']
            self.assertEqual(len(group['products']),20)
            self.assertEqual(next(m['values'] for m in group['menus'] if m['key']=='uitlooplengte'),['18 cm','25 cm'])
            for row in group['products']:
                parsed=compiler.audit.split_sku(compiler.sku_of(self.by_handle[row['handle']]))
                self.assertIn(parsed['model'],{family.upper()+'18',family.upper()+'25'})
        ext={r['handle'] for r in self.group_index['hotbath-book-cb105ext-keuzes']['products']}
        text={r['handle'] for r in self.group_index['hotbath-book-cb105text-keuzes']['products']}
        self.assertFalse(ext & text)

if __name__=='__main__':unittest.main(verbosity=2)
