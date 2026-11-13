import copy
import json
import unittest

from build_import_plan import make_input
from build_remaining_m2_plan import prepare_optional_singletons
from build_unit_plan import prepare as prepare_units
from test_import_plan import fixture
from test_unit_plan import unit_row
from verify_readback import verify


def planned(sku='EX01', color='Blauw'):
    row = fixture(sku, color)
    return {'sku': sku, 'group_key': 'Bronmerk|Voorbeeld', 'input': make_input(row, 'Bronmerk|Voorbeeld')}


def admin_product(expected, identity=1):
    data = copy.deepcopy(expected['input'])
    files = data.pop('files')
    data.pop('productOptions')
    data['id'] = 'gid://shopify/Product/' + str(identity)
    data['options'] = [{'name': 'Title', 'values': ['Default Title']}]
    data['metafields'] = {'nodes': data['metafields'], 'pageInfo': {'hasNextPage': False}}
    variants = data['variants']
    for index, variant in enumerate(variants):
        variant['id'] = 'gid://shopify/ProductVariant/' + str(identity * 100 + index)
        variant.pop('optionValues')
        variant['selectedOptions'] = [{'name': 'Title', 'value': 'Default Title'}]
        variant['barcode'] = variant.pop('barcodes', [{}])[0].get('value')
    data['variants'] = {'nodes': variants, 'pageInfo': {'hasNextPage': False}}
    data['media'] = {'nodes': [
        {'id': 'gid://shopify/MediaImage/' + str(identity * 100 + index),
         'alt': file['alt'], 'status': 'READY', 'mediaContentType': 'IMAGE',
         'image': {'url': 'https://cdn.shopify.com/example-' + str(identity) + '-' + str(index) + '.jpg', 'altText': file['alt']}}
        for index, file in enumerate(files)
    ], 'pageInfo': {'hasNextPage': False}}
    data['collections'] = {'nodes': [{'id': identity} for identity in data.get('collections', [])], 'pageInfo': {'hasNextPage': False}}
    return data


def group_references(products):
    references = json.dumps([product['id'] for product in products])
    for product in products:
        product['metafields']['nodes'].append({'namespace': 'tiles', 'key': 'group_products', 'type': 'list.product_reference', 'value': references})


class ReadbackGateTests(unittest.TestCase):
    def setUp(self):
        self.plans = [planned(), planned('EX02', 'Groen')]
        self.products = [admin_product(plan, index + 1) for index, plan in enumerate(self.plans)]

    def assert_group_blocked(self, result, field):
        self.assertEqual(result['status'], 'HOLD')
        self.assertEqual(len(result['blocked_groups']), 1)
        self.assertEqual(set(result['blocked_groups'][0]['skus']), {'EX01', 'EX02'})
        self.assertEqual(result['readback_pass_skus'], [])
        self.assertIn(field, {error['field'] for error in result['errors']})

    def test_complete_exact_api_readback_passes_without_mutating_input(self):
        before = copy.deepcopy(self.products)
        result = verify(self.plans, self.products)
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(result['failure_count'], 0)
        self.assertEqual(result['readback_pass_skus'], ['EX01', 'EX02'])
        self.assertGreater(result['checks'], 50)
        self.assertFalse(result['writes_performed'])
        self.assertEqual(self.products, before)

    def test_price_change_blocks_other_unchanged_group_member(self):
        self.products[0]['variants']['nodes'][0]['price'] = '39.99'
        self.assert_group_blocked(verify(self.plans, self.products), 'variant.price')

    def test_equivalent_html_entities_pass_without_rewriting_the_readback(self):
        self.plans[0]['input']['descriptionHtml'] = '<p>Rose d&#x27;Antan &amp; Blue</p>'
        self.products[0]['descriptionHtml'] = "<p>Rose d'Antan &amp; Blue</p>"
        before = copy.deepcopy(self.products)
        self.assertEqual(verify(self.plans, self.products)['status'], 'PASS')
        self.assertEqual(before, self.products)

    def test_html_tag_text_and_escaped_active_markup_changes_still_block_group(self):
        self.plans[0]['input']['descriptionHtml'] = '<p>Rose d&#x27;Antan</p>'
        for actual in ["<p>Rose d'Antan gewijzigd</p>", "<div>Rose d'Antan</div>"]:
            self.products[0]['descriptionHtml'] = actual
            self.assert_group_blocked(verify(self.plans, self.products), 'product.descriptionHtml')
        self.plans[0]['input']['descriptionHtml'] = '<p>&lt;script&gt;alert(1)&lt;/script&gt;</p>'
        self.products[0]['descriptionHtml'] = '<p><script>alert(1)</script></p>'
        self.assert_group_blocked(verify(self.plans, self.products), 'product.descriptionHtml')

    def test_changed_packaging_metadata_blocks_group(self):
        meta = next(value for value in self.products[0]['metafields']['nodes'] if value['key'] == 'bron_toelichtingen_json')
        data = json.loads(meta['value'])
        data['tiles']['m2_per_box'] = .6
        meta['value'] = json.dumps(data)
        self.assert_group_blocked(verify(self.plans, self.products), 'metafield.custom.bron_toelichtingen_json')

    def test_processing_or_missing_photo_blocks_group(self):
        self.products[0]['media']['nodes'][0]['status'] = 'PROCESSING'
        self.assert_group_blocked(verify(self.plans, self.products), 'media.ready')
        self.products[0]['media']['nodes'] = []
        self.assert_group_blocked(verify(self.plans, self.products), 'media.count')

    def test_missing_readback_and_incomplete_connection_fail_closed(self):
        self.assert_group_blocked(verify(self.plans, self.products[:1]), 'identity.unique_product')
        self.products[0]['media']['pageInfo']['hasNextPage'] = True
        self.assert_group_blocked(verify(self.plans, self.products), 'readback.media_complete')

    def test_same_sku_on_two_product_ids_is_blocked(self):
        extra = admin_product(self.plans[0], 3)
        self.assert_group_blocked(verify(self.plans, self.products + [extra]), 'identity.unique_product')

    def test_conflicting_duplicate_snapshots_are_not_silently_selected(self):
        extra = copy.deepcopy(self.products[0])
        extra['title'] += ' gewijzigd'
        self.assert_group_blocked(verify(self.plans, self.products + [extra]), 'identity.consistent_readback')

    def test_group_references_must_cover_the_whole_group(self):
        group_references(self.products)
        self.assertEqual(verify(self.plans, self.products, require_group_refs=True)['status'], 'PASS')
        references = self.products[0]['metafields']['nodes'][-1]
        references['value'] = json.dumps([self.products[0]['id']])
        self.assert_group_blocked(verify(self.plans, self.products, require_group_refs=True), 'menu.complete_references')

    def test_wrapped_mcp_readbacks_and_equivalent_numeric_encoding_are_supported(self):
        number = next(value for value in self.products[0]['metafields']['nodes'] if value['key'] == 'tegel_dikte_mm')
        number['value'] = '8.000'
        for product in self.products:
            product['options'] = [{'name': 'Title', 'optionValues': [{'name': 'Default Title'}]}]
            variant = product['variants']['nodes'][0]
            barcode = variant.pop('barcode')
            variant['barcodes'] = {'nodes': [{'type': 'EAN', 'value': barcode}] if barcode else []}
        wrapped = {'content': [{'type': 'text', 'text': json.dumps({'data': {'nodes': self.products}})}]}
        self.assertEqual(verify(self.plans, wrapped)['status'], 'PASS')

    def test_active_status_requires_explicit_expected_active_sku(self):
        self.products[0]['status'] = 'ACTIVE'
        self.assert_group_blocked(verify(self.plans, self.products), 'product.status')
        self.assertEqual(verify(self.plans, self.products, active_skus=['EX01'])['status'], 'PASS')

    def optional_pair(self):
        row = fixture()
        row.update(color=None, finish=None, thickness=None, weight_kg_candidate=None)
        row['raw_workbook'].pop('AE')
        row['flags'] = ['missing_official_color', 'missing_finish', 'missing_weight']
        plan = prepare_optional_singletons([row])['products'][0]
        return plan, admin_product(plan)

    def test_optional_native_zero_is_only_a_default_not_verified_weight(self):
        plan, product = self.optional_pair()
        product['variants']['nodes'][0]['inventoryItem']['measurement'] = {'weight': {'unit': 'KILOGRAMS', 'value': 0}}
        result = verify([plan], [product])
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(result['unconfirmed_physical_weight_skus'], ['EX01'])
        self.assertNotIn('weight.value', result['checks_by_field'])
        self.assertEqual(result['checks_by_field']['weight.platform_default_only'], 1)

    def test_optional_absent_native_weight_is_accepted_and_unconfirmed(self):
        plan, product = self.optional_pair()
        result = verify([plan], [product])
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(result['unconfirmed_physical_weight_skus'], ['EX01'])

    def test_optional_unexplained_positive_native_weight_is_blocked(self):
        plan, product = self.optional_pair()
        product['variants']['nodes'][0]['inventoryItem']['measurement'] = {'weight': {'unit': 'KILOGRAMS', 'value': 9.9}}
        result = verify([plan], [product])
        self.assertEqual(result['status'], 'HOLD')
        self.assertIn('weight.platform_default_only', {e['field'] for e in result['errors']})

    def test_optional_weight_cannot_reappear_as_a_display_specification(self):
        plan, product = self.optional_pair()
        mf = next(m for m in product['metafields']['nodes'] if m['key'] == 'complete_specificaties')
        value = json.loads(mf['value'])
        value[0]['items'].append({'key': 'gewicht_per_doos', 'label': 'Gewicht per doos', 'value': '0 kg'})
        mf['value'] = json.dumps(value)
        result = verify([plan], [product])
        self.assertEqual(result['status'], 'HOLD')
        self.assertIn('weight.sourced_display_absent', {e['field'] for e in result['errors']})

    def test_optional_unknown_fields_cannot_reappear_as_extra_metafields(self):
        plan, product = self.optional_pair()
        for namespace, key, kind, value in [('tiles', 'color', 'single_line_text_field', 'Blauw'), ('bc_filters', 'tegel_dikte_mm', 'number_decimal', '8')]:
            with self.subTest(field=key):
                actual = copy.deepcopy(product)
                actual['metafields']['nodes'].append({'namespace': namespace, 'key': key, 'type': kind, 'value': value})
                result = verify([plan], [actual])
                self.assertEqual(result['status'], 'HOLD')
                self.assertIn('metafield.absent.' + namespace + '.' + key, {e['field'] for e in result['errors']})

    def test_optional_singleton_self_reference_is_complete(self):
        plan, product = self.optional_pair()
        group_references([product])
        self.assertEqual(verify([plan], [product], require_group_refs=True)['status'], 'PASS')

    def test_strict_weight_still_requires_exact_source_value(self):
        self.products[0]['variants']['nodes'][0]['inventoryItem']['measurement']['weight']['value'] = 0
        self.assert_group_blocked(verify(self.plans, self.products), 'weight.value')

    def test_native_units_have_no_reference_area_measurement(self):
        plan = prepare_units([unit_row()])['products'][0]
        product = admin_product(plan)
        result = verify([plan], [product])
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(result['checks_by_field']['unit_price.not_configured'], 1)
        self.assertNotIn('unit_price.quantityValue', result['checks_by_field'])
        product['variants']['nodes'][0]['unitPriceMeasurement'] = {'quantityUnit': None, 'referenceUnit': None, 'quantityValue': 0, 'referenceValue': 0}
        self.assertEqual(verify([plan], [product])['status'], 'PASS')

    def test_native_pack_cannot_acquire_a_hidden_m2_measurement(self):
        row = unit_row(unit='pak', count=10, price='99.50')
        row['unit_contract']['source_price'] = '9.95'
        plan = prepare_units([row])['products'][0]
        product = admin_product(plan)
        product['variants']['nodes'][0]['unitPriceMeasurement'] = {'quantityUnit': 'M2', 'referenceUnit': 'M2', 'quantityValue': .5, 'referenceValue': 1}
        result = verify([plan], [product])
        self.assertEqual(result['status'], 'HOLD')
        self.assertIn('unit_price.not_configured', {e['field'] for e in result['errors']})

    def test_unknown_native_weight_cannot_reappear_in_unit_tile_contract(self):
        row = unit_row(unit='pak', count=10, price='99.50')
        row['unit_contract']['source_price'] = '9.95'
        plan = prepare_units([row])['products'][0]
        product = admin_product(plan)
        mf = next(m for m in product['metafields']['nodes'] if m['key'] == 'bron_toelichtingen_json')
        tile = json.loads(mf['value'])
        tile['tiles']['weight_kg_per_unit'] = 0
        mf['value'] = json.dumps(tile)
        result = verify([plan], [product])
        self.assertEqual(result['status'], 'HOLD')
        self.assertIn('weight.sourced_display_absent', {e['field'] for e in result['errors']})


if __name__ == '__main__':
    unittest.main()
