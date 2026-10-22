import copy
import importlib.util
import json
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('plan', Path(__file__).parents[1] / 'scripts/cj_collection_plan.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def fixture():
    return {'id': 'gid://shopify/Product/10534562365706', 'vendor': 'Hotbath', 'status': 'ACTIVE',
            'source': {'type': 'list.single_line_text_field', 'value': json.dumps(['Kranen', 'Wastafelkranen', 'Opbouw wastafelkranen'])},
            'root': False, 'parent': False, 'opbouw': False, 'inbouw': False}


class CollectionPlanTests(unittest.TestCase):
    def test_exact_path_adds_three(self):
        self.assertEqual(module.plan_products([fixture()])['membership_additions'], 3)

    def test_rerun_is_noop(self):
        item = fixture()
        item.update(root=True, parent=True, opbouw=True)
        self.assertEqual(module.plan_products([item])['membership_additions'], 0)

    def test_partial_membership_preserved(self):
        item = fixture()
        item.update(root=True, opbouw=True)
        self.assertEqual(module.plan_products([item])['additions'][0]['add_to'], [module.TARGETS['parent']])

    def test_no_title_inference(self):
        item = fixture()
        item.update(title='Koperen opbouw wastafelkraan', source=None)
        self.assertEqual(len(module.plan_products([item])['review']), 1)

    def test_other_vendor_not_touched(self):
        item = fixture()
        item['vendor'] = 'Wiesbaden'
        self.assertEqual(module.plan_products([item])['membership_additions'], 0)

    def test_draft_not_touched(self):
        item = fixture()
        item['status'] = 'DRAFT'
        self.assertEqual(module.plan_products([item])['membership_additions'], 0)

    def test_bad_json_review(self):
        item = fixture()
        item['source']['value'] = 'broken'
        self.assertEqual(len(module.plan_products([item])['review']), 1)

    def test_unknown_path_review(self):
        item = fixture()
        item['source']['value'] = '["Kranen", "Vloermontage"]'
        self.assertEqual(len(module.plan_products([item])['review']), 1)

    def test_missing_membership_not_assumed_false(self):
        item = fixture()
        del item['parent']
        self.assertEqual(len(module.plan_products([item])['review']), 1)

    def test_wrong_path_type_review(self):
        item = fixture()
        item['source']['type'] = 'json'
        self.assertEqual(len(module.plan_products([item])['review']), 1)

    def test_inbouw_not_added_to_opbouw(self):
        item = fixture()
        item['source']['value'] = '["Kranen", "Wastafelkranen", "Inbouw wastafelkranen"]'
        result = module.plan_products([item])
        self.assertIn(module.TARGETS['inbouw'], result['additions'][0]['add_to'])
        self.assertNotIn(module.TARGETS['opbouw'], result['additions'][0]['add_to'])

    def test_duplicates_abort(self):
        with self.assertRaises(ValueError):
            module.plan_products([fixture(), fixture()])

    def test_input_unchanged(self):
        items = [fixture()]
        before = copy.deepcopy(items)
        module.plan_products(items)
        self.assertEqual(items, before)

    def test_invalid_identity_aborts(self):
        item = fixture()
        item['id'] = '10534562365706'
        with self.assertRaises(ValueError):
            module.plan_products([item])


if __name__ == '__main__':
    unittest.main()
