import copy
import unittest

from build_product_benefits import derive
from build_import_preparation import record
from test_manufacturer_benefits import DEFS, TARGETS, exact
from test_product_benefits import sample


class CurationTests(unittest.TestCase):
    def test_every_missing_or_held_set_component_blocks_the_complete_label(self):
        fields = ['Hoofddouche inbegrepen', 'Handdouche inbegrepen',
                  'Doucheslang inbegrepen', 'Inbouwdeel inbegrepen']
        for field in fields:
            for bad in ['', None, 'Nee']:
                p,e=sample({**dict.fromkeys(fields,'Ja'),field:bad})
                self.assertNotIn('complete_shower_set',[i['rule'] for i in derive(p,e,DEFS)])
            p,e=sample(dict.fromkeys(fields,'Ja'))
            p['retail_review']={'open_fields':[field]}
            self.assertNotIn('complete_shower_set',[i['rule'] for i in derive(p,e,DEFS)])

    def test_set_does_not_infer_body_from_glijstang_or_title(self):
        p,e=sample({'Hoofddouche inbegrepen':'Ja','Handdouche inbegrepen':'Ja',
                    'Doucheslang inbegrepen':'Ja','Glijstang inbegrepen':'Ja'})
        p['title']='Complete doucheset, alles inbegrepen'
        self.assertEqual(derive(p,e,DEFS),[])

    def test_material_is_literal_scoped_and_not_inferred_from_colour(self):
        for material,text in [('MDF gelakt','Gelakt MDF'),('Massief eiken vingerlas','Massief eiken')]:
            p,e=sample({'Materiaal':material},'Onderkasten')
            self.assertEqual([i['text'] for i in derive(p,e,DEFS)],[text])
            p['product_type']='Ladefronten'
            self.assertEqual(derive(p,e,DEFS),[])
        p,e=sample({'Materiaal':'MFC'},'Onderkasten');p['title']='Eiken onderkast'
        p['options']={'colour':'Eiken bruin'}
        self.assertEqual(derive(p,e,DEFS),[])
        p,e=sample({'Materiaal':'MDF gelakt'},'Onderkasten')
        p['source_conflicts']={'Materiaal':['MFC','MDF gelakt']}
        self.assertEqual(derive(p,e,DEFS),[])

    def test_softclose_names_drawers_only_when_drawers_are_proved(self):
        p,e=sample({'Softclose':'Ja','Aantal lades':'2'},'Onderkasten')
        self.assertEqual([i['text'] for i in derive(p,e,DEFS)],['Softclose lades'])
        p,e=sample({'Softclose':'Ja'},'Onderkasten')
        self.assertEqual([i['text'] for i in derive(p,e,DEFS)],['Zachte sluiting'])

    def test_lighting_is_one_point_and_led_does_not_fill_an_empty_slot(self):
        p,e=sample({'Dimbaar':'Ja','Lichtkleur instelbaar':'Ja','Verlichting':'Directe verlichting (LED)'},'Spiegels')
        self.assertEqual([i['text'] for i in derive(p,e,DEFS)],['Dimbare verlichting met kleurkeuze'])
        p,e=sample({'Verlichting':'Directe verlichting (LED)'},'Spiegels')
        self.assertEqual(derive(p,e,DEFS),[])
        p,e=sample({'Verlichting':'Ja'},'Spiegelkasten')
        self.assertEqual([i['text'] for i in derive(p,e,DEFS)],['Verlichting inbegrepen'])

    def test_no_installation_or_material_performance_promises_are_added(self):
        p,e=sample({'Materiaal':'MDF gelakt','Softclose':'Ja','Aantal lades':'2'},'Onderkasten')
        self.assertEqual([i['text'] for i in derive(p,e,DEFS)],['Gelakt MDF','Softclose lades'])
        self.assertTrue(all(not any(term in i['text'].lower() for term in ['waterdicht','vochtbestendig','duurzaam','perfect']) for i in derive(p,e,DEFS)))

    def test_offline_plan_rejects_four_points_instead_of_silently_truncating(self):
        p,e=exact({});p.update(price_incl_vat='121.00',import_allowed=False)
        b={'sku':p['sku'],'ean':p['ean'],'items':[{'text':str(i)} for i in range(4)]}
        with self.assertRaises(ValueError):record(p,b,TARGETS)


if __name__ == '__main__':
    unittest.main(verbosity=2)
