import copy
import unittest

from build_import_plan import availability, make_input, plan, row_blockers


def fixture(sku='EX01', color='Blauw'):
    return {
        'sku': sku, 'source_name': 'Voorbeeld ' + color + ' 7,5x15',
        'retail_brand': 'Cottoceramix', 'original_brand': 'Bronmerk',
        'series': 'Voorbeeld', 'color': color, 'model': None,
        'category': 'Tegels > Wandtegels', 'size': '7,5 x 15 cm',
        'length_cm': 7.5, 'width_cm': 15, 'finish': 'Glans',
        'thickness': '8 mm', 'm2_mode': True, 'sale_method': 'Doos',
        'source_pack': 'Pak 44st/0,5m²', 'm2_per_box': .5,
        'pieces_per_box': 44, 'unit_price': 79.95, 'box_price': 39.98,
        'weight_kg_candidate': 9.9, 'weight_status': 'Bronnen sluiten aan binnen 10 gram',
        'availability_import': '', 'stock_snapshot': 5,
        'manual_overrides': {}, 'flags': [],
        'source_url': 'https://cottoceramix.nl/artikel/1/voorbeeld.html',
        'raw_workbook': {'AE': 8, 'BE': 60, 'R': '1234567890128'},
        'live': {'fields': {'stock_level': '5', 'delivery_time': 'Op voorraad: 5', 'price': '39,98'},
                 'specs': {'Gerectificeerd': 'Nee'}, 'images': ['https://cottoceramix.nl/voorbeeld.jpg']},
    }


class ImportPlanTests(unittest.TestCase):
    def test_box_area_is_packing_not_geometric_bounding_box(self):
        row = fixture()
        value = make_input(row, 'Bronmerk|Voorbeeld')
        self.assertEqual(value['variants'][0]['unitPriceMeasurement']['quantityValue'], .5)
        self.assertEqual(value['variants'][0]['price'], '39.98')
        self.assertNotEqual(.075 * .15 * 44, .5)

    def test_cent_rounding_uses_decimal_half_up(self):
        row = fixture()
        row.update(m2_per_box=.7, unit_price=134.95, box_price=94.47)
        self.assertNotIn('box_price_reconcile_error', row_blockers(row))

    def test_chosen_source_size_wins_over_legacy_excel_numeric_dimensions(self):
        row = fixture()
        row.update(size='11x22', length_cm=11, width_cm=11)
        value = make_input(row, 'Bronmerk|Voorbeeld')
        meta = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
        self.assertEqual(meta['bc_filters.tegel_lengte_mm'], '110.0')
        self.assertEqual(meta['bc_filters.tegel_breedte_mm'], '220.0')

    def test_chosen_source_thickness_wins_over_legacy_excel_numeric_thickness(self):
        row = fixture()
        row['raw_workbook']['AE'] = 10
        row['thickness'] = '8 mm'
        value = make_input(row, 'Bronmerk|Voorbeeld')
        meta = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
        self.assertEqual(meta['bc_filters.tegel_dikte_mm'], '8.0')

    def test_manual_price_basis_wins_over_conflicting_feed_price(self):
        row = fixture()
        row['manual_overrides']['price'] = True
        row['live']['fields']['price'] = '83,16'
        row.update(m2_per_box=.64, unit_price=114.95, box_price=73.57)
        value = make_input(row, 'Bronmerk|Voorbeeld')
        self.assertEqual(value['variants'][0]['price'], '73.57')
        self.assertEqual(value['status'], 'DRAFT')

    def test_ambiguous_same_choice_motifs_hold_the_whole_group(self):
        first, second = fixture('A'), fixture('B')
        first['model'], second['model'] = 'Basis', 'Decor'
        result = plan([first, second])
        self.assertEqual(result['products'], [])
        self.assertIn('ambiguous_choice_tuple', result['held'][0]['reasons'])

    def test_missing_weight_holds_whole_group(self):
        first, second = fixture('A'), fixture('B', 'Groen')
        second['weight_kg_candidate'] = None
        self.assertEqual(plan([first, second])['summary']['held_products'], 2)

    def test_piece_item_never_gets_m2_native_pricing(self):
        row = fixture()
        row.update(m2_mode=False, sale_method='Stuk')
        self.assertEqual(plan([row])['products'], [])

    def test_group_larger_than_fifty_is_held_without_silent_truncation(self):
        rows = [fixture(str(i), 'Kleur ' + str(i)) for i in range(51)]
        result = plan(rows)
        self.assertEqual(result['summary']['held_products'], 51)
        self.assertIn('group_exceeds_renderer_limit_50', result['groups'][0]['blockers'])

    def test_placeholder_or_private_image_is_not_publishable(self):
        row = fixture()
        row['live']['images'] = ['https://logic4cdn.azureedge.net/no-img.svg']
        self.assertIn('untrusted_or_private_image_url', row_blockers(row))
        row['live']['images'] = ['https://cottoceramix.nl/img.jpg?token=private']
        self.assertIn('untrusted_or_private_image_url', row_blockers(row))

    def test_bad_ean_is_omitted_without_inventing_another(self):
        row = fixture()
        row['raw_workbook']['R'] = '1234567890123'
        variant = make_input(row, 'Bronmerk|Voorbeeld')['variants'][0]
        self.assertNotIn('barcodes', variant)
        self.assertEqual(variant['sku'], 'EX01')

    def test_existing_identity_never_gets_a_product_set_update(self):
        row = fixture()
        result = plan([row], {'EX01': 'gid://shopify/Product/1'})
        self.assertEqual(result['products'], [])
        self.assertEqual(result['skipped'][0]['product_id'], 'gid://shopify/Product/1')
        row['weight_kg_candidate'] = None
        result = plan([row], {'EX01': 'gid://shopify/Product/1'})
        self.assertEqual(result['held'], [])
        self.assertEqual(result['summary']['existing_skipped'], 1)

    def test_verified_menu_evidence_is_explicit_and_complete(self):
        row = fixture()
        evidence = [{'verified': True, 'group_key': 'Bronmerk|Voorbeeld', 'skus': ['EX01'], 'source_urls': [row['source_url']]}]
        self.assertFalse(plan([row])['products'][0]['publishable_after_readback'])
        result = plan([row], evidence=evidence)
        self.assertTrue(result['products'][0]['publishable_after_readback'])
        self.assertNotIn('id', result['products'][0]['input'])
        evidence[0]['source_urls'] = ['https://other.invalid/example']
        with self.assertRaises(ValueError):
            plan([row], evidence=evidence)

    def test_duplicate_source_identity_aborts_instead_of_overwriting(self):
        with self.assertRaises(ValueError):
            plan([fixture(), fixture()])

    def test_unknown_delivery_is_not_invented(self):
        row = fixture()
        row['live']['fields'].update(stock_level='0', delivery_time='heeft onbekende levertijd')
        self.assertEqual(availability(row)[0], 'Levertijd op aanvraag')
        self.assertEqual(availability(row)[1], 'Bestelartikel')

    def test_manual_stock_confirmation_does_not_invent_a_quantity(self):
        row = fixture()
        row.update(availability_import='Op voorraad', stock_snapshot=0, manual_overrides={'availability': True})
        lead, order, stock, manual = availability(row)
        self.assertEqual((lead, order, stock, manual), ('Op voorraad', 'Voorraadartikel', 0, True))

    def test_plan_is_reproducible_and_does_not_mutate_sources(self):
        rows = [fixture()]
        before = copy.deepcopy(rows)
        self.assertEqual(plan(rows), plan(rows))
        self.assertEqual(rows, before)
        self.assertEqual(plan(rows)['summary']['writes_performed'], False)


if __name__ == '__main__':
    unittest.main()
