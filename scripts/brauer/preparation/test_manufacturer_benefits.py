import copy
import json
from pathlib import Path
import tempfile
import unittest

from build_product_benefits import derive, approved_definition, build as build_benefits
from build_import_preparation import record, validate_targets, EXPECTED_TARGETS
from build_specifications import build as build_specs
from refine_supplier_door_mechanisms import refine
from test_product_benefits import sample


KEYS = ['hydrophobic_glass','cold_start','pvd_finish','frameless_glass',
        'sliding_door','pivot_sliding_door','glass_thickness','anti_slip']
DEFS = {k:{'brand':'BRAUER','status':'VERIFIED_DEFINITION',
           'sources':['https://www.brauerkranen.nl/site/test'],
           'primary_url':'https://www.brauerkranen.nl/site/test'} for k in KEYS}
TARGETS = {role:dict(zip(('namespace','key','type'),value),validations=[])
           for role,value in EXPECTED_TARGETS.items()}


def exact(values, typ='Nisdeuren', group='Nisdeur met draaideur profielloos'):
    p,e = sample(values, typ)
    p['source_refs'] = [{'file':'supplier.xlsx','sheet':'Data','row':2}]
    p['source'] = {'Merk':'BRAUER','Artikelcode':p['sku'],'EAN':p['ean'],
                   'Productgroep':group,'Productomschrijving':'glas draaiend/schuivend naar binnen',
                   'Serie':'Luminis','Kleur':'Chroom','Materiaal':'RVS,Glas','Afwerking':''}
    p['options'] = {'colour':'Chroom'}
    p['source_conflicts'] = {}
    return p,e


class ManufacturerTests(unittest.TestCase):
    def test_coating_requires_exact_article_fact_and_does_not_promise_factory_treatment(self):
        p,e = exact({'Glascoating':'Ja'})
        r = derive(p,e,DEFS)
        point = next(x for x in r if x['rule']=='glass_coating')
        self.assertEqual(point['text'],'Met water- en vuilafstotende glascoating')
        self.assertEqual(point['definition_refs'],['hydrophobic_glass'])
        for val in ['Nee','',None]:
            p,e = exact({'Glascoating':val})
            self.assertNotIn('glass_coating',[x['rule'] for x in derive(p,e,DEFS)])

    def test_unverified_or_unrelated_manufacturer_definition_is_not_used(self):
        for change in [{'brand':'OTHER'},{'status':'PENDING'},{'sources':['https://unrelated.invalid/a']},
                       {'sources':['http://www.brauerkranen.nl/a']}]:
            d = copy.deepcopy(DEFS);d['hydrophobic_glass'].update(change)
            self.assertIsNone(approved_definition(d,'hydrophobic_glass'))

    def test_original_supplier_group_needs_its_own_full_identity(self):
        p,e = exact({})
        self.assertIn('frameless_glass',[x['rule'] for x in derive(p,e,DEFS)])
        p['source']['EAN']='9999999999999'
        self.assertNotIn('frameless_glass',[x['rule'] for x in derive(p,e,DEFS)])
        p['source']['EAN']=p['ean'];p['source']['Productgroep']='Inloopdouche met profiel'
        self.assertNotIn('frameless_glass',[x['rule'] for x in derive(p,e,DEFS)])

    def test_sliding_mechanism_does_not_override_contradictory_or_held_field(self):
        p,e = exact({'Deursysteem':'Schuifdeur'},group='Nisdeur 2-delig met schuifdeur met profiel')
        self.assertIn('sliding_door',[x['rule'] for x in derive(p,e,DEFS)])
        p['retail_review']={'open_fields':['Deursysteem']}
        self.assertNotIn('sliding_door',[x['rule'] for x in derive(p,e,DEFS)])
        p.pop('retail_review');p['specifications']['Deursysteem']='Draaideur'
        self.assertNotIn('sliding_door',[x['rule'] for x in derive(p,e,DEFS)])

    def test_pvd_is_not_inferred_from_colour_or_product_name(self):
        p,e = exact({},'Opbouwwastafelkranen')
        p['title']='PVD goud';p['source']['Kleur']='PVD goud';p['options']['colour']='Goud'
        self.assertNotIn('pvd_finish',[x['rule'] for x in derive(p,e,DEFS)])
        p,e = exact({'Coating':'PVD'},'Opbouwwastafelkranen')
        self.assertIn('PVD-afwerking',[x['text'] for x in derive(p,e,DEFS)])

    def test_lighting_functions_do_not_infer_led_or_heating(self):
        p,e = exact({'Dimbaar':'Ja','Lichtkleur instelbaar':'Ja'},'Spiegels')
        self.assertEqual([x['rule'] for x in derive(p,e,DEFS)],['dimmable_light','adjustable_light_colour'])
        p['specifications']['Verlichting']='Nee'
        self.assertEqual(derive(p,e,DEFS),[])

    def test_known_six_mm_is_not_promoted_to_eight_mm(self):
        p,e = exact({'Glasdikte':'6 mm'})
        self.assertNotIn('glass_thickness',[x['rule'] for x in derive(p,e,DEFS)])
        p,e = exact({'Glasdikte':'8 mm'})
        self.assertIn('glass_thickness',[x['rule'] for x in derive(p,e,DEFS)])

    def test_missing_registry_preserves_prepared_benefits(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'prepared').mkdir();path=root/'prepared/product-benefits.json';path.write_text('keep')
            with self.assertRaises(FileNotFoundError):build_benefits(root)
            self.assertEqual(path.read_text(),'keep')

    def test_compound_mechanism_refines_only_expected_supplier_parse(self):
        p,e = exact({'Deursysteem':'Draaideur'},group='Nisdeur met draai-schuifdeur met profiel')
        p['customer_specifications']=[{'group':'Uitvoering','items':[{'label':'Deursysteem','value':'Draaideur'}]}]
        e['facts']['Deursysteem'].update(field='Productomschrijving',fragment='draaiend')
        change=refine(p,e)
        self.assertEqual(change['before'],'Draaideur');self.assertEqual(change['after'],'Draai-schuifdeur')
        self.assertEqual(change['previous_evidence']['fragment'],'draaiend')
        self.assertIsNone(refine(p,e))
        self.assertIn('pivot_sliding_door',[x['rule'] for x in derive(p,e,DEFS)])

    def test_canonical_supplier_parser_prioritizes_explicit_compound_group(self):
        p,e = exact({},group='Nisdeur met draai-schuifdeur met profiel')
        groups,proof,_,_=build_specs(p,{})
        value=next(i['value'] for g in groups for i in g['items'] if i['label']=='Deursysteem')
        self.assertEqual(value,'Draai-schuifdeur');self.assertEqual(proof['Deursysteem']['field'],'Productgroep')

    def test_unexpected_retail_or_held_value_is_not_silently_refined(self):
        p,e = exact({'Deursysteem':'Draaideur'},group='Nisdeur met draai-schuifdeur met profiel')
        e['facts']['Deursysteem']['kind']='retailer_exact_sku_ean'
        with self.assertRaises(ValueError):refine(p,e)

    def test_display_limit_keeps_original_benefits_first(self):
        p,e = exact({'Glascoating':'Ja','Montage':'Links of rechts te monteren','Coating':'PVD','Glasdikte':'8 mm'})
        all_points=derive(p,e,DEFS,limit=None);visible=derive(p,e,DEFS)
        self.assertEqual(len(all_points),5);self.assertEqual(len(visible),4)
        self.assertEqual([x['rule'] for x in visible[:2]],['glass_coating','reversible_glass'])

    def test_import_record_preserves_price_and_never_sets_release_or_stock(self):
        p,e=exact({})
        p.update(title='Test',handle_proposal='test',description='Test',price_incl_vat='121.00',vat_rate='0.21',
                 family_id='family',customer_specifications=[],media={'images':[],'pdfs':[]},
                 data_issues=[],specification_review={'missing_essential_fields':[]},future_available_date=None,import_allowed=False,
                 user_additions={'Jouw aanvulling techniek':'Eigen gecontroleerde aanvulling'})
        b={'sku':p['sku'],'ean':p['ean'],'items':[]}
        r=record(p,b,TARGETS)
        self.assertEqual(r['product_data']['price_incl_vat'],'121.00');self.assertFalse(r['import_allowed'])
        self.assertEqual(r['review']['user_additions'],p['user_additions'])
        self.assertNotIn('status',r['product_data']);self.assertNotIn('inventory_quantity',r['product_data'])
        fields={m['key']:m for m in r['metafield_values']}
        self.assertEqual(fields['pluspunten']['type'],'list.single_line_text_field')
        self.assertEqual(json.loads(fields['pluspunten']['value']),[])
        self.assertEqual(json.loads(fields['complete_specificaties']['value']),p['customer_specifications'])
        self.assertEqual(fields['switch_group']['value'],p['family_id'])
        b['ean']='9999999999999'
        with self.assertRaises(ValueError):record(p,b,TARGETS)
        b['ean']=p['ean'];p['import_allowed']=True
        with self.assertRaises(ValueError):record(p,b,TARGETS)

    def test_existing_target_schema_change_requires_a_new_review(self):
        snapshot={'status':'READ_ONLY_DEFINITIONS_VERIFIED','owner_type':'PRODUCT','targets':copy.deepcopy(TARGETS)}
        self.assertEqual(validate_targets(snapshot),TARGETS)
        for role,field,value in [('benefits','type','single_line_text_field'),
                                 ('specifications','validations',[{'name':'max','value':'1'}]),
                                 ('choice_group','key','different_group')]:
            changed=copy.deepcopy(snapshot);changed['targets'][role][field]=value
            with self.assertRaises(ValueError):validate_targets(changed)


if __name__ == '__main__':
    unittest.main(verbosity=2)
