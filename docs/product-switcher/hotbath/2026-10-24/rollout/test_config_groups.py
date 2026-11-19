#!/usr/bin/env python3
import copy
import json
import unittest
from pathlib import Path

import build_config_groups as compiler

SOURCE = Path('/workspace/scratch/6866aa3baeaf/hotbath-menu-20261024')


class ConfigGroupsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((SOURCE/'catalog_snapshot.json').read_text())
        cls.book = json.loads((SOURCE/'book_rules.json').read_text())
        cls.existing = json.loads((SOURCE/'baseline/product-switcher-data.json').read_text())
        cls.rules = {x['id']: x for x in cls.book['families'] if x['id'] in compiler.FAMILIES}

    def test_exact_family_boundaries(self):
        self.assertEqual(compiler.family_for_sku('IBS7009BCP127'), ('IBS7009','BCP','127'))
        self.assertEqual(compiler.family_for_sku('IBS20ABCP1'), ('IBS20A','BCP','1'))
        self.assertEqual(compiler.family_for_sku('IBS12ACR'), ('IBS12A','CR',''))
        self.assertIsNone(compiler.family_for_sku('TEST-HOTBATH-IBS70CR347'))

    def test_official_combined_options_and_default(self):
        expected={'kleur':'Geborsteld koper PVD','breedte_diameter_hoofddouche':'20 cm','type_bevestiging_hoofddouche':'Plafondbuis 15 cm','type_handdouche':'Rond model','bevestiging_handdouche':'Glijstang'}
        self.assertEqual(compiler.decode('IBS7009','BCP','127',self.rules),expected)
        self.assertEqual(compiler.decode('IBS1','CR','',self.rules)['type_handdouche'],'Staafmodel')

    def test_buddy_round_default_is_not_mislabeled_staff(self):
        self.assertEqual(compiler.decode('IBS12','CR','',self.rules)['type_handdouche'],'Rond ABS (Ø13 cm)')
        self.assertEqual(compiler.decode('IBS12','CR','1',self.rules)['type_handdouche'],'Rond, 3 standen (Ø13 cm)')

    def test_unknown_options_and_family_finish_cannot_enter(self):
        for family,color,suffix in [('IBS70','CR','23'),('IBS70','CR','77'),('IBS70','CR','21'),('IBS70','CR','6'),('IBS1','BCP','')]:
            with self.assertRaises(ValueError): compiler.decode(family,color,suffix,self.rules)

    def test_spom_excluded_in_any_identity_field(self):
        row=next(x for x in self.catalog['products'] if x['variants']['nodes'][0]['sku']=='IBS70CR')
        for field in ['title','handle','sku']:
            changed=copy.deepcopy(row)
            if field=='sku':changed['variants']['nodes'][0]['sku']='SPOM-IBS70CR'
            else:changed[field]+=' SPOM service'
            self.assertEqual(compiler.eligible(changed),(False,'SPOM_EXCLUDED'))

    def test_draft_and_unpublished_are_excluded(self):
        row=next(x for x in self.catalog['products'] if x['variants']['nodes'][0]['sku']=='IBS70CR')
        for key,value in [('status','DRAFT'),('publishedAt',None)]:
            changed=copy.deepcopy(row);changed[key]=value
            self.assertEqual(compiler.eligible(changed),(False,'NOT_ACTIVE_AND_PUBLISHED'))

    def test_without_rail_is_not_parsed_as_with_rail(self):
        options=compiler.decode('IBS1','CR','12',self.rules)
        title='Hotbath IBS1 Buddy chroom met ronde 3 standen handdouche 20cm hoofddouche met plafondbuis 15cm zonder glijstang'
        findings,keys=compiler.title_check(title,'IBS1',options,'12')
        self.assertEqual(findings,[])
        self.assertIn('bevestiging_handdouche',keys)

    def test_real_wrong_diameter_and_component_conflicts_remain_held(self):
        _,review,_=compiler.build(self.catalog,self.book,self.existing)
        actual={x.get('sku'):x for x in review['cases']}
        self.assertIn('TITLE_OVERHEAD_DIAMETER_CONFLICT',actual['IBS20AGN357']['findings'])
        self.assertIn('TITLE_EMBEDDED_COMPONENT_COLOR_CONFLICT',actual['IBS20BBP']['findings'])
        self.assertIn('TITLE_CONTROL_CONFLICT',actual['IBS20BCP']['findings'])

    def test_all_generated_tuples_are_unique_and_current(self):
        data,review,mapping=compiler.build(self.catalog,self.book,self.existing)
        self.assertEqual(len(data['groups']),8)
        self.assertEqual(mapping['product_count'],1536)
        current={x['handle'] for x in self.catalog['products']}
        all_handles=[]
        for group in data['groups']:
            tuples=[tuple(p['options'][key] for key in compiler.KEYS) for p in group['products']]
            self.assertEqual(len(tuples),len(set(tuples)))
            self.assertTrue({p['handle'] for p in group['products']}<=current)
            all_handles.extend(p['handle'] for p in group['products'])
        self.assertEqual(len(all_handles),len(set(all_handles)))

    def test_duplicate_cannot_silently_choose_one_article(self):
        catalog=copy.deepcopy(self.catalog)
        row=copy.deepcopy(next(x for x in catalog['products'] if x['variants']['nodes'][0]['sku']=='IBS70CR'))
        row['id']='gid://shopify/Product/999';row['handle']='duplicate-example'
        catalog['products'].append(row)
        data,review,_=compiler.build(catalog,self.book,self.existing)
        self.assertNotIn('hotbath-cobber-ibs70-inbouw-doucheset',{g['id'] for g in data['groups']})
        self.assertTrue(any(x['reason']=='DUPLICATE_OR_MIXED_EXISTING_GROUP' for x in review['cases']))

    def test_unknown_existing_group_cannot_be_overwritten(self):
        catalog=copy.deepcopy(self.catalog)
        row=next(x for x in catalog['products'] if x['variants']['nodes'][0]['sku']=='IBS70CR')
        row['group']={'value':'unreviewed-group'}
        data,review,_=compiler.build(catalog,self.book,self.existing)
        self.assertNotIn('unreviewed-group',{g['id'] for g in data['groups']})
        self.assertTrue(any(x['reason']=='UNKNOWN_EXISTING_GROUP_NOT_OVERRIDDEN' for x in review['cases']))

    def test_current_and_json_group_conflict_is_retained_for_review(self):
        catalog=copy.deepcopy(self.catalog)
        row=next(x for x in catalog['products'] if x['variants']['nodes'][0]['sku']=='IBS70CR')
        row['group']={'value':'current-known-group'}
        existing=copy.deepcopy(self.existing)
        existing['groups'].extend([
            {'id':'current-known-group','products':[],'menus':[]},
            {'id':'json-known-group','products':[{'handle':row['handle']}],'menus':[]},
        ])
        data,review,_=compiler.build(catalog,self.book,existing)
        self.assertFalse(any('ibs70-' in g['id'] for g in data['groups']))
        conflict=next(x for x in review['cases'] if x.get('family')=='IBS70')
        self.assertEqual(conflict['existing_group_ids'],['current-known-group','json-known-group'])

    def test_multiple_explicit_title_colors_do_not_silently_win_by_length(self):
        options=compiler.decode('IBS70','BCP','',self.rules)
        title='Hotbath Cobber IBS70 geborsteld koper PVD 20cm hoofddouche wandarm staafhanddouche wandhouder met chroom kraan'
        findings,_=compiler.title_check(title,'IBS70',options,'')
        self.assertIn('TITLE_COLOR_CONFLICT',findings)


if __name__=='__main__': unittest.main(verbosity=2)
