import copy
import json
import unittest
from pathlib import Path

from analyze_numeric_sets import analyse, parse_options

BASE = Path('/workspace/scratch/6866aa3baeaf/hotbath-menu-20261024')


class NumericSetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((BASE/'catalog_snapshot.json').read_text())
        cls.existing = json.loads((BASE/'baseline/product-switcher-data.json').read_text())

    def product(self, sku):
        return next(p for p in self.catalog['products'] if p['variants']['nodes'][0]['sku'] == sku)

    def test_complete_current_rows_have_unique_real_choices(self):
        result = analyse(self.catalog, self.existing)
        self.assertEqual(result['metrics']['ready_records'], 465)
        self.assertEqual(result['metrics']['ready_groups'], 5)
        self.assertFalse(result['review'])
        self.assertEqual(len({r['handle'] for r in result['records']}), 465)
        for group in result['groups']:
            keys = [m['key'] for m in group['menus']]
            self.assertEqual(len({tuple(p['options'][k] for k in keys) for p in group['products']}), len(group['products']))

    def test_known_thermostat_and_mixer_compositions_stay_separate(self):
        one, a = parse_options('IBS-ACE1001', self.product('IBS-ACE1001')['title'])
        two, b = parse_options('IBS-ACE2102', self.product('IBS-ACE2102')['title'])
        self.assertNotEqual(one, two)
        self.assertEqual(a['breedte_diameter_hoofddouche'], '20 cm')
        self.assertEqual(a['type_handdouche'], 'Staafmodel')
        self.assertEqual(b['kleur'], 'Geborsteld messing PVD')
        self.assertEqual(b['breedte_diameter_hoofddouche'], '23 cm Velvet')
        self.assertEqual(b['type_handdouche'], '3 standen')
        self.assertEqual(b['type_bevestiging_hoofddouche'], 'Plafondbuis 30 cm')

    def test_control_title_conflict_is_not_decoded_from_number(self):
        title=self.product('IBS-ACE1001')['title'].replace('thermostatisch', 'mengkraan')
        with self.assertRaisesRegex(ValueError, 'CONTROL_TITLE_CONFLICT'):
            parse_options('IBS-ACE1001', title)

    def test_spom_in_title_excludes_product(self):
        c=copy.deepcopy(self.catalog)
        p=next(p for p in c['products'] if p['variants']['nodes'][0]['sku']=='IBS-ACE1001')
        p['title'] += ' SPOM replacement'
        result=analyse(c,self.existing)
        self.assertFalse(any(r['sku']=='IBS-ACE1001' for r in result['records']))
        self.assertTrue(any(r['sku']=='IBS-ACE1001' and r['reason']=='SPOM_OR_TEST' for r in result['excluded']))

    def test_unpublished_color_never_enters_group(self):
        c=copy.deepcopy(self.catalog)
        p=next(p for p in c['products'] if p['variants']['nodes'][0]['sku']=='IBS-ACE1001')
        p['publishedAt']=None
        result=analyse(c,self.existing)
        self.assertFalse(any(r['sku']=='IBS-ACE1001' for r in result['records']))

    def test_duplicate_tuple_blocks_family_instead_of_arbitrary_pick(self):
        c=copy.deepcopy(self.catalog)
        p=copy.deepcopy(self.product('IBS-ACE1001'));p['id']='new-id';p['handle']='other-handle';p['variants']['nodes'][0]['sku']='IBS-ACE1999'
        c['products'].append(p)
        result=analyse(c,self.existing)
        family=next(x for x in result['families'] if x['family']=='ace_thermostatic_2way')
        self.assertIn('DUPLICATE_CHOICE_TUPLES',family['reason_flags'])
        self.assertFalse(any(g['id']==family['group_id'] for g in result['groups']))

    def test_existing_membership_is_not_silently_overwritten(self):
        c=copy.deepcopy(self.catalog)
        p=next(p for p in c['products'] if p['variants']['nodes'][0]['sku']=='IBS-ACE1001')
        p['group']={'value':'existing-other-family'}
        result=analyse(c,self.existing)
        family=next(x for x in result['families'] if x['family']=='ace_thermostatic_2way')
        self.assertIn('EXISTING_GROUP_RECONCILIATION_REQUIRED',family['reason_flags'])

    def test_fixed_threeway_group_exposes_only_color(self):
        result=analyse(self.catalog,self.existing)
        group=next(g for g in result['groups'] if g['id']=='hotbath-ace-numeric-3weg-velvet-inbouw-doucheset')
        self.assertEqual([m['key'] for m in group['menus']],['kleur'])
        self.assertEqual(len(group['products']),6)

    def test_hidden_fixed_title_difference_cannot_become_color_choice(self):
        c=copy.deepcopy(self.catalog)
        p=next(p for p in c['products'] if p['variants']['nodes'][0]['sku']=='COBBER4001')
        p['title'] += ' met extra onderdeel'
        result=analyse(c,self.existing)
        family=next(x for x in result['families'] if x['family']=='cobber_beam_mixer_set')
        self.assertIn('UNMODELED_FIXED_TITLE_DIFFERENCE',family['reason_flags'])

    def test_hidden_ace_fixed_model_term_blocks_five_choice_family(self):
        c=copy.deepcopy(self.catalog)
        p=next(p for p in c['products'] if p['variants']['nodes'][0]['sku']=='IBS-ACE1001')
        p['title'] += ' met extra watervalfunctie'
        result=analyse(c,self.existing)
        family=next(x for x in result['families'] if x['family']=='ace_thermostatic_2way')
        self.assertIn('UNMODELED_FIXED_TITLE_DIFFERENCE',family['reason_flags'])
        self.assertEqual(family['status'],'REVIEW')
        self.assertFalse(any(g['id']==family['group_id'] for g in result['groups']))


if __name__=='__main__':unittest.main(verbosity=2)
