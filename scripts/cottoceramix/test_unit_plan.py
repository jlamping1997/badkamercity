import copy
import json
import unittest

from build_unit_plan import availability_for_native, contract_blockers, prepare
from test_import_plan import fixture


def unit_row(sku='UNIT1', color='Blauw', unit='stuk', count=1, price='3.45'):
    row = fixture(sku, color)
    row.update(m2_mode=False, sale_method='Stuk', source_pack='st.', model='Rand',
               m2_per_box=None, pieces_per_box=None, unit_price=None, box_price=None)
    row['flags'] = ['separate_non_m2_order_path']
    row['unit_contract'] = {
        'sku': sku, 'kind': 'SINGLE_PIECE' if count == 1 else 'FIXED_MULTIPLE_OF_PIECES',
        'sale_unit': unit, 'unit_count': count, 'native_price': price,
        'source_price': price if count == 1 else str(float(price) / count),
        'source_price_basis': 'per_piece', 'supplier_sale_increment': count,
        'weight_per_native_unit': .32 if count == 1 else None,
        'source_weight_basis': 'Explicit source weight per native unit' if count == 1 else None,
        'publication_hold_reasons': [], 'proof_notes': ['Exact source-unit contract'],
        'currency': 'EUR', 'vat_basis': 'incl_btw',
    }
    return row


def parsed(plan):
    value = plan['products'][0]['input']
    mf = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
    return value, mf, json.loads(mf['custom.bron_toelichtingen_json'])['tiles']


class UnitPlanTests(unittest.TestCase):
    def test_piece_uses_exact_native_price_without_area_measurement(self):
        value, mf, tile = parsed(prepare([unit_row()]))
        variant = value['variants'][0]
        self.assertEqual(variant['price'], '3.45')
        self.assertFalse(variant['showUnitPrice'])
        self.assertNotIn('unitPriceMeasurement', variant)
        self.assertEqual((tile['order_mode'], tile['sale_unit'], tile['unit_count']), ('unit', 'stuk', 1))
        for name in ['m2_per_box', 'price_per_m2', 'price_per_box', 'pieces_per_box']:
            self.assertNotIn(name, tile)
        self.assertNotIn('pak van', value['title'])
        self.assertIn('barcodes', variant)

    def test_pack_price_enforces_whole_confirmed_piece_multiple(self):
        row = unit_row(unit='pak', count=10, price='99.50')
        row['unit_contract']['source_price'] = '9.95'
        value, mf, tile = parsed(prepare([row]))
        self.assertEqual(value['variants'][0]['price'], '99.50')
        self.assertEqual(tile['unit_count'], 10)
        self.assertEqual(tile['source']['supplier_order_quantity_per_native_unit'], 10)
        self.assertIn('pak van 10 stuks', value['title'])
        self.assertNotIn('barcodes', value['variants'][0])
        self.assertEqual(tile['source']['source_ean'], '1234567890128')
        row['unit_contract']['native_price'] = '9.95'
        self.assertIn('native_pack_price_reconcile_error', contract_blockers(row))

    def test_priced_set12_does_not_multiply_feed_price_again_or_claim_coverage(self):
        row = unit_row(unit='set', count=12, price='203.40')
        row.update(sale_method='Speciale set: m¹', source_pack='Pak 12st/7,2m¹')
        row['unit_contract'].update(kind='SOURCE_FIXED_SET_12', source_price='203.40',
                                    source_price_basis='per_12_piece_package', supplier_sale_increment=1)
        value, mf, tile = parsed(prepare([row]))
        self.assertEqual(value['variants'][0]['price'], '203.40')
        self.assertEqual(tile['source']['supplier_order_quantity_per_native_unit'], 1)
        self.assertEqual(tile['source']['source_pack'], 'Pak 12st/7,2m¹')
        self.assertIn('set van 12 stuks', value['title'])
        self.assertNotIn('7,2', value['descriptionHtml'])
        self.assertNotIn('m¹', mf['custom.complete_specificaties'])
        row['source_name'] += ' set van 12'
        value, mf, tile = parsed(prepare([row]))
        self.assertEqual(value['title'].count('set van 12'), 1)

    def test_unit_weight_comes_only_from_verified_native_contract(self):
        row = unit_row()
        row['weight_kg_candidate'] = 99.9
        value, mf, tile = parsed(prepare([row]))
        self.assertEqual(value['variants'][0]['inventoryItem']['measurement']['weight']['value'], .32)
        row['unit_contract'].update(weight_per_native_unit=None, source_weight_basis=None)
        value, mf, tile = parsed(prepare([row]))
        self.assertNotIn('measurement', value['variants'][0]['inventoryItem'])
        self.assertNotIn('weight_kg_per_unit', tile)
        self.assertNotIn('gewicht_per_besteleenheid', mf['custom.complete_specificaties'])

    def test_unknown_facts_are_omitted_and_force_a_singleton(self):
        rows = [unit_row('A'), unit_row('B', 'Groen')]
        for row in rows:
            row.update(color=None, series=None, finish=None, size=None, thickness=None)
        result = prepare(rows)
        self.assertEqual(len(result['groups']), 2)
        value, mf, tile = parsed(result)
        for name in ['tiles.color', 'tiles.execution', 'tiles.size', 'custom.serie', 'bc_filters.tegel_dikte_mm', 'bc_filters.tegel_lengte_mm']:
            self.assertNotIn(name, mf)
        self.assertNotIn('None', value['tags'])
        self.assertNotIn('None', value['descriptionHtml'])

    def test_only_complete_explicit_model_color_families_are_grouped(self):
        rows = [unit_row('A'), unit_row('B', 'Groen')]
        result = prepare(rows)
        self.assertEqual(len(result['groups']), 1)
        self.assertEqual(result['groups'][0]['skus'], ['A', 'B'])
        rows[1]['model'] = None
        self.assertEqual(len(prepare(rows)['groups']), 2)

    def test_confirmed_strip_profiles_group_without_inventing_wall_application(self):
        rows = [unit_row('A', 'Lime', 'pak', 10, '99.50'), unit_row('B', 'Mint', 'pak', 10, '99.50')]
        for row in rows:
            row.update(category='Tegels > Sierstrips en afwerking', series='Casablanca', model='Rounded Edge',
                       size='1,1x15', thickness='9 mm')
            row['source_name'] = 'Casablanca Rounded Edge ' + row['color'] + ' 1,1x15'
            row['unit_contract']['source_price'] = '9.95'
        result = prepare(rows)
        self.assertEqual(len(result['groups']), 1)
        self.assertEqual(result['groups'][0]['skus'], ['A', 'B'])
        value, mf, tile = parsed(result)
        self.assertEqual(mf['tiles.application'], 'Tegels')

    def test_literal_title_profile_separates_overbroad_official_model(self):
        rows = [unit_row('A', 'Blauw'), unit_row('B', 'Groen')]
        for row, profile in zip(rows, ['Cirkel-In', 'Cirkel-Out']):
            row.update(series='Färgblock', model='Matt', finish='Mat')
            row['source_name'] = 'Färgblock Decoro ' + profile + ' ' + row['color'] + ' Matt 7,5 x 15 cm'
        self.assertEqual(len(prepare(rows)['groups']), 2)
        rows[1]['model'] = 'Rand'
        rows[1]['unit_contract'].update(sale_unit='pak', unit_count=10, source_price='.345', native_price='3.45', supplier_sale_increment=10)
        self.assertEqual(len(prepare(rows)['groups']), 2)

    def test_duplicate_color_is_not_dropped_or_merged(self):
        result = prepare([unit_row('A'), unit_row('B')])
        self.assertEqual(len(result['products']), 2)
        self.assertEqual(len(result['groups']), 2)

    def test_stock_below_whole_pack_minimum_is_not_a_stock_promise(self):
        row = unit_row(unit='pak', count=10, price='99.50')
        row['unit_contract']['source_price'] = '9.95'
        row['live']['fields']['stock_level'] = '7'
        result = prepare([row])
        value, mf, tile = parsed(result)
        self.assertEqual(tile['source']['stock_units'], 7)
        self.assertEqual((tile['lead_time'], tile['order_type']), ('Levertijd op aanvraag', 'Bestelartikel'))
        self.assertEqual(len(result['availability_guards']), 1)
        row['manual_overrides']['availability'] = True
        row['availability_import'] = 'Op voorraad'
        self.assertEqual(availability_for_native(row)[0], 'Op voorraad')

    def test_generic_category_is_not_falsely_assigned_as_wall_or_floor(self):
        row = unit_row()
        row['category'] = 'Tegels > Plinten'
        value, mf, tile = parsed(prepare([row]))
        self.assertEqual(value['productType'], 'Tegels')
        self.assertEqual(mf['tiles.application'], 'Tegels')
        self.assertEqual(tile['source']['source_category'], 'Tegels > Plinten')
        self.assertNotIn('collections', value)
        self.assertEqual(value['tags'].count('Tegels'), 1)

    def test_missing_real_photo_or_unverified_price_is_held(self):
        first, second = unit_row('A'), unit_row('B')
        first['live']['images'] = []
        second['manual_overrides']['price'] = True
        result = prepare([first, second])
        self.assertEqual(result['products'], [])
        self.assertIn('missing_real_product_image', result['held'][0]['reasons'])
        self.assertIn('manual_price_override_requires_explicit_contract', result['held'][1]['reasons'])

    def test_existing_identities_and_draft_publication_dependency_are_preserved(self):
        rows = [unit_row('A'), unit_row('B')]
        before = copy.deepcopy(rows)
        result = prepare(rows, existing_skus=['A'])
        self.assertEqual([p['sku'] for p in result['products']], ['B'])
        self.assertEqual(result['skipped'][0]['sku'], 'A')
        self.assertEqual(result['products'][0]['input']['status'], 'DRAFT')
        self.assertFalse(result['products'][0]['publishable_after_readback'])
        self.assertTrue(result['products'][0]['requires_unit_renderer_publication'])
        self.assertEqual(rows, before)
        self.assertEqual(result, prepare(rows, existing_skus=['A']))


if __name__ == '__main__':
    unittest.main()
