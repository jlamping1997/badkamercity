import copy
import json
import unittest

from build_import_plan import make_input
from test_import_plan import fixture
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


if __name__ == '__main__':
    unittest.main()
