import copy
import json
import unittest

from build_remaining_m2_plan import prepare, prepare_optional_singletons, sku_set
from test_import_plan import fixture


class RemainingM2PlanTests(unittest.TestCase):
    def test_bad_peer_does_not_contaminate_valid_source_colors(self):
        first, second, bad = fixture('A', 'Blauw'), fixture('B', 'Groen'), fixture('C', 'Rood')
        bad['weight_kg_candidate'] = None
        result = prepare([first, second, bad])
        self.assertEqual({p['sku'] for p in result['products']}, {'A', 'B'})
        self.assertEqual(result['groups'][0]['skus'], ['A', 'B'])
        self.assertEqual(result['held'][0]['sku'], 'C')

    def test_existing_identity_excluded_even_when_it_has_blockers(self):
        row = fixture()
        row['weight_kg_candidate'] = None
        result = prepare([row], ['EX01'])
        self.assertEqual(result['held'], [])
        self.assertEqual(result['products'], [])
        self.assertEqual(result['skipped'][0]['sku'], 'EX01')

    def test_admin_product_registry_excludes_exact_variant_skus(self):
        registry = [{'id': 'gid://shopify/Product/1', 'variants': {'nodes': [
            {'sku': 'EX01'}, {'sku': 'EX02'}]}}]
        self.assertEqual(sku_set(registry), {'EX01', 'EX02'})
        self.assertEqual(prepare([fixture()], sku_set(registry))['products'], [])

    def test_models_sizes_and_thickness_do_not_mix_under_color(self):
        rows = [fixture('A'), fixture('B'), fixture('C'), fixture('D')]
        rows[1]['model'] = 'Decoro'
        rows[2]['size'] = '10x10'
        rows[3]['thickness'] = '10 mm'
        self.assertEqual(len(prepare(rows)['groups']), 4)

    def test_known_exact_size_rounding_is_held_in_both_routes(self):
        row = fixture('KV5907')
        row['size'] = '59,5x59,5'
        result = prepare([row])
        self.assertEqual(result['products'], [])
        self.assertIn('renderer_exact_size_unsupported', result['held'][0]['reasons'])
        row.update(finish=None)
        result = prepare_optional_singletons([row])
        self.assertEqual(result['products'], [])
        self.assertIn('renderer_exact_size_unsupported', result['held'][0]['reasons'])

    def test_reviewed_exact_size_exception_only_releases_a_fixed_singleton(self):
        row = fixture('KV5907')
        row['size'] = '59,5x59,5'
        result = prepare_optional_singletons([row], reviewed_exact_size_singletons={'KV5907'})
        self.assertEqual(len(result['products']), 1)
        self.assertEqual(result['assignments'][0]['membership_skus'], ['KV5907'])
        self.assertTrue(result['products'][0]['reviewed_exact_size_singleton'])
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in result['products'][0]['input']['metafields']}
        self.assertEqual(mf['tiles.size'], '59,5x59,5')
        with self.assertRaises(ValueError):
            prepare_optional_singletons([fixture()], reviewed_exact_size_singletons={'EX01'})

    def test_optional_unknown_color_finish_thickness_never_persist_as_values(self):
        row = fixture()
        row.update(color=None, finish=None, thickness=None)
        row['raw_workbook'].pop('AE')
        row['flags'] = ['missing_official_color', 'missing_finish']
        result = prepare_optional_singletons([row])
        self.assertEqual(len(result['products']), 1)
        value = result['products'][0]['input']
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
        for key in ['tiles.color', 'tiles.execution', 'custom.kleur', 'custom.afwerking', 'bc_filters.tegel_dikte_mm']:
            self.assertNotIn(key, mf)
        specs = json.loads(mf['custom.complete_specificaties'])
        self.assertFalse(any(item['key'] in {'kleur', 'afwerking', 'dikte_mm'} for group in specs for item in group['items']))
        self.assertNotIn('in de kleur', value['descriptionHtml'])
        self.assertNotIn('met afwerking', value['descriptionHtml'])
        self.assertEqual(result['groups'][0]['skus'], ['EX01'])
        self.assertEqual(value['variants'][0]['price'], '39.98')
        self.assertEqual(value['variants'][0]['unitPriceMeasurement']['quantityValue'], .5)

    def test_optional_route_keeps_known_specs_and_omits_absent_series(self):
        row = fixture()
        row.update(series=None)
        row['flags'] = ['missing_official_series']
        value = prepare_optional_singletons([row])['products'][0]['input']
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
        self.assertEqual(mf['tiles.color'], 'Blauw')
        self.assertEqual(mf['tiles.execution'], 'Glans')
        self.assertNotIn('custom.serie', mf)
        self.assertNotIn('None', value['tags'])

    def test_optional_route_cannot_relax_price_or_identity(self):
        rows = [fixture('A'), fixture('B'), fixture('C')]
        for row in rows:
            row.update(color=None)
            row['flags'] = ['missing_official_color']
        rows[0]['m2_per_box'] = None
        rows[1]['box_price'] = 100
        rows[2]['source_name'] = None
        self.assertEqual(prepare_optional_singletons(rows)['products'], [])

    def test_optional_unknown_weight_is_absent_not_zero_in_all_contracts(self):
        row = fixture()
        row.update(weight_kg_candidate=None)
        row['flags'] = ['missing_weight', 'weight_conflict']
        value = prepare_optional_singletons([row])['products'][0]['input']
        self.assertNotIn('measurement', value['variants'][0]['inventoryItem'])
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
        self.assertNotIn('weight_kg_per_box', json.loads(mf['custom.bron_toelichtingen_json'])['tiles'])
        specs = json.loads(mf['custom.complete_specificaties'])
        self.assertFalse(any(item['key'] == 'gewicht_per_doos' for group in specs for item in group['items']))

    def test_optional_unresolved_positive_conflicting_weight_still_omitted(self):
        row = fixture()
        row['flags'] = ['weight_conflict']
        value = prepare_optional_singletons([row])['products'][0]['input']
        self.assertNotIn('measurement', value['variants'][0]['inventoryItem'])

    def test_optional_unknown_piece_count_and_dimensions_never_invent_one_or_zero(self):
        row = fixture()
        row.update(pieces_per_box=None, size=None, thickness=None)
        row['raw_workbook']['AE'] = 10  # legacy numeric data is not chosen thickness
        row['flags'] = ['missing_size']
        value = prepare_optional_singletons([row])['products'][0]['input']
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
        tile = json.loads(mf['custom.bron_toelichtingen_json'])['tiles']
        self.assertNotIn('pieces_per_box', tile)
        for key in ['tiles.size', 'bc_filters.tegel_lengte_mm', 'bc_filters.tegel_breedte_mm', 'bc_filters.tegel_dikte_mm']:
            self.assertNotIn(key, mf)
        self.assertNotIn('None', value['descriptionHtml'])
        self.assertNotIn('tegels, samen', value['descriptionHtml'])

    def test_finish_contradictions_hold_without_relabeling_them(self):
        row = fixture('GQR107M')
        row['source_name'] = 'Genesi26 Bianco Matt 13,2x40'
        row['finish'] = 'Glans'
        row['weight_kg_candidate'] = None
        result = prepare_optional_singletons([row])
        self.assertEqual(result['products'], [])
        self.assertIn('source_title_finish_conflict', result['held'][0]['reasons'])

    def test_explicit_color_conflict_is_omitted_without_replacing_source(self):
        row = fixture('AT2144', 'Sand')
        row.update(source_name='Striata Pearl 4,8x44,5', weight_kg_candidate=None)
        before = copy.deepcopy(row)
        result = prepare_optional_singletons([row])
        value = result['products'][0]['input']
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in value['metafields']}
        self.assertNotIn('tiles.color', mf)
        self.assertNotIn('custom.kleur', mf)
        self.assertEqual(value['title'], 'Cottoceramix Striata Pearl 4,8x44,5')
        self.assertEqual(value['variants'][0]['price'], '39.98')
        self.assertEqual(result['color_omission_ledger'][0]['original_color'], 'Sand')
        self.assertIsNone(result['color_omission_ledger'][0]['published_color'])
        self.assertEqual(result['source_rows'][0]['color'], 'Sand')
        self.assertEqual(row, before)

    def test_optional_singletons_do_not_silently_import_strict_rows(self):
        result = prepare_optional_singletons([fixture()])
        self.assertEqual(result['products'], [])
        self.assertEqual(result['summary']['strict_route_skipped'], 1)

    def test_madrid_title_model_wins_for_partition_without_rewriting_source(self):
        rows = [fixture('A'), fixture('B')]
        for row, kind in zip(rows, ['Liso', 'Metro']):
            row.update(original_brand='Altair', series='Madrid', model='Liso',
                       source_name='Madrid ' + kind + ' Blanco Brillo 10x20')
        result = prepare(rows)
        self.assertEqual(len(result['groups']), 2)
        self.assertTrue(any('Madrid Metro' in g['label'] for g in result['groups']))
        self.assertEqual(rows[1]['model'], 'Liso')

    def test_shibusa_and_wabisabi_do_not_share_duplicate_bianco_choice(self):
        rows = [fixture('A', 'Bianco'), fixture('B', 'Bianco')]
        for row, family in zip(rows, ['Shibusa', 'Wabisabi']):
            row.update(original_brand='Tonalite', series='Wabisabi', model=None,
                       source_name=family + ' Bianco 5x15')
        result = prepare(rows)
        self.assertEqual(len(result['groups']), 2)
        self.assertEqual({g['label'].split(' · ')[0] for g in result['groups']}, {'Shibusa', 'Wabisabi'})

    def test_unexplained_duplicate_color_is_isolated_not_dropped(self):
        result = prepare([fixture('A'), fixture('B'), fixture('C', 'Groen')])
        self.assertEqual(len(result['products']), 3)
        self.assertTrue(all(len(g['skus']) == 1 for g in result['groups']))

    def test_renderer_limit_never_silently_truncates(self):
        rows = [fixture(str(i), 'Kleur ' + str(i)) for i in range(51)]
        result = prepare(rows)
        self.assertEqual(len(result['products']), 51)
        self.assertEqual(len(result['groups']), 51)
        self.assertEqual(result['summary']['max_family_size'], 1)

    def test_chosen_fields_prices_and_manual_override_pass_through(self):
        row = fixture()
        row.update(size='11x22', thickness='8 mm', length_cm=11, width_cm=11,
                   m2_per_box=.64, unit_price=114.95, box_price=73.57)
        row['raw_workbook'].update(AE=10)
        row['manual_overrides']['price'] = True
        row['live']['fields']['price'] = '83,16'
        product = prepare([row])['products'][0]['input']
        meta = {m['namespace'] + '.' + m['key']: m['value'] for m in product['metafields']}
        self.assertEqual(product['variants'][0]['price'], '73.57')
        self.assertEqual(meta['bc_filters.tegel_breedte_mm'], '220.0')
        self.assertEqual(meta['bc_filters.tegel_dikte_mm'], '8.0')
        self.assertTrue(json.loads(meta['custom.bron_toelichtingen_json'])['tiles']['source']['manual_overrides']['price'])

    def test_piece_items_and_known_source_conflicts_stay_held(self):
        first, second = fixture('STUK'), fixture('VA3201')
        first.update(m2_mode=False, sale_method='Stuk')
        result = prepare([first, second])
        self.assertEqual(result['products'], [])
        self.assertIn('confirmed_source_attribute_conflict', result['held'][1]['reasons'])

    def test_deterministic_source_preserving_draft_only_plan(self):
        rows = [fixture('A', 'Blauw'), fixture('B', 'Groen')]
        before = copy.deepcopy(rows)
        result = prepare(rows)
        self.assertEqual(result, prepare(rows))
        self.assertEqual(rows, before)
        self.assertTrue(all(p['input']['status'] == 'DRAFT' for p in result['products']))
        self.assertFalse(result['summary']['writes_performed'])
        self.assertFalse(result['summary']['source_menu_exact_match_claimed'])
        self.assertTrue(all('id' not in p['input'] for p in result['products']))


if __name__ == '__main__':
    unittest.main()
