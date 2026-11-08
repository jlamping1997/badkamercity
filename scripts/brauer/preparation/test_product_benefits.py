import copy
import unittest
from build_product_benefits import derive


def sample(values, typ='Inbouwdouchesets'):
    product = {'sku': 'TEST-A', 'ean': '1234567890123', 'vendor': 'BRAUER',
               'product_type': typ, 'specifications': values}
    evidence = {'ean': product['ean'], 'facts': {
        k: {'kind': 'supplier', 'field': k, 'fragment': v,
            'source_refs': [{'file': 'test.xlsx', 'sheet': 'Test', 'row': 2}]}
        for k, v in values.items()}}
    return product, evidence


class BenefitsTests(unittest.TestCase):
    def test_complete_set_is_one_point_and_keeps_component_proof(self):
        p, e = sample({k: 'Ja' for k in ['Hoofddouche inbegrepen', 'Handdouche inbegrepen',
                                        'Doucheslang inbegrepen', 'Inbouwdeel inbegrepen']})
        result = derive(p, e)
        self.assertEqual([x['text'] for x in result], ['Complete doucheset'])
        self.assertEqual(len(result[0]['basis']), 4)

    def test_unknown_or_negative_inclusion_never_becomes_complete_bundle(self):
        for value in [None, '', 'Nee']:
            p, e = sample({'Hoofddouche inbegrepen': 'Ja', 'Handdouche inbegrepen': 'Ja',
                           'Doucheslang inbegrepen': 'Ja', 'Inbouwdeel inbegrepen': value})
            texts = [r['text'] for r in derive(p, e)]
            self.assertEqual(texts, [])

    def test_explicit_rotating_enum_and_boolean_and_conflicts(self):
        for values in [{'Draaibare uitloop': 'Ja'}, {'Uitvoering uitloop': 'Draaibaar'}]:
            p, e = sample(values, 'Opbouwwastafelkranen')
            self.assertEqual(derive(p, e)[0]['text'], 'Draaibare uitloop')
        p, e = sample({'Draaibare uitloop': 'Nee', 'Uitvoering uitloop': 'Draaibaar'}, 'Opbouwwastafelkranen')
        self.assertEqual(derive(p, e), [])
        p, e = sample({'Uitvoering uitloop': 'Draaibaar'}, 'Opbouwwastafelkranen')
        p['retail_review'] = {'open_fields': ['Draaibare uitloop']}
        self.assertEqual(derive(p, e), [])

    def test_field_holds_are_respected_and_unrelated_facts_retained(self):
        p, e = sample({'Inbouwdeel inbegrepen': 'Ja', 'Thermostatisch': 'Ja'})
        p['retail_review'] = {'open_fields': ['Inbouwdeel inbegrepen']}
        self.assertEqual([r['text'] for r in derive(p, e)], ['Thermostaatkraan'])

    def test_no_variant_title_or_option_inheritance_and_no_identity_guess(self):
        p, e = sample({})
        p.update(title='complete draaibare inbouwset met softclose', options={'inbouwdeel': 'Ja'})
        self.assertEqual(derive(p, e), [])
        p, e = sample({'Inbouwdeel inbegrepen': 'Ja'})
        for key, wrong in [('ean', '9999999999999'), ('vendor', 'OTHER')]:
            altered = copy.deepcopy(p); altered[key] = wrong
            self.assertEqual(derive(altered, e), [])

    def test_missing_proof_and_excluded_source_rejected(self):
        p, e = sample({'Inbouwdeel inbegrepen': 'Ja'})
        self.assertEqual(derive(p, {'ean': p['ean'], 'facts': {}}), [])
        e['facts']['Inbouwdeel inbegrepen']['url'] = 'https://www.badkamervoorjou.nl/test'
        self.assertEqual(derive(p, e), [])

    def test_glass_and_furniture_features_are_scoped(self):
        values = {'Glascoating': 'Ja', 'Softclose': 'Ja', 'Montage': 'Links of rechts te monteren'}
        p, e = sample(values, 'Nisdeuren')
        self.assertEqual([r['rule'] for r in derive(p, e)], ['glass_coating', 'reversible_glass'])
        p['product_type'] = 'Onderkasten'
        self.assertEqual([r['text'] for r in derive(p, e)], ['Zachte sluiting'])
        p['product_type'] = 'Ladefronten'
        self.assertEqual(derive(p, e), [])

    def test_maximum_three_and_no_duplicate_body_benefit(self):
        p, e = sample({**{k: 'Ja' for k in ['Hoofddouche inbegrepen', 'Handdouche inbegrepen',
                                           'Doucheslang inbegrepen', 'Inbouwdeel inbegrepen',
                                           'Thermostatisch', 'Koudestartfunctie']},
                       'Aantal straalstanden handdouche': '3', 'Draaibare uitloop': 'Ja'})
        result = derive(p, e)
        self.assertEqual(len(result), 3)
        self.assertNotIn('included_body', [x['rule'] for x in result])
        self.assertEqual(len(set(x['text'] for x in result)), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
