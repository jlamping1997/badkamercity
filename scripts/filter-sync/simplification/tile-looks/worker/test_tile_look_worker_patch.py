"""Meaningful local invariants; requires the reviewed private base worker.

No network, Docker, Shopify write, or worker installation is performed.
"""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import types
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SPEC = importlib.util.spec_from_file_location('tile_look_patch_tested', HERE / 'tile_look_worker_patch.py')
PATCH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PATCH)
WORKER = Path(os.environ.get('BC_TILE_LOOK_BASE_SOURCE', ROOT / 'more-colors-20261108/release/private-target-sync.py'))
API = Path(os.environ.get('BC_TILE_LOOK_API_SOURCE', ROOT / 'filter-implementation/acero-correction/private-current-app.py'))


def load(source):
    module = types.ModuleType('tile_look_worker_tested')
    module.__file__ = str(HERE / 'private-candidate-worker.py')
    exec(compile(source, module.__file__, 'exec'), module.__dict__)
    return module


DEFINITIONS = [
    {'key': 'kleur', 'field': 'f_kleur', 'label': 'Kleur', 'type': 'choice', 'data_type': 'string'},
    {'key': 'serie', 'field': 'f_serie', 'label': 'Serie', 'type': 'choice', 'data_type': 'string'},
    {'key': 'tegel_breedte_mm', 'field': 'f_tegel_breedte_mm', 'label': 'Breedte', 'type': 'range', 'data_type': 'float', 'unit': 'mm'},
    {'key': 'tegel_lengte_mm', 'field': 'f_tegel_lengte_mm', 'label': 'Lengte', 'type': 'range', 'data_type': 'float', 'unit': 'mm'},
    {'key': 'prijs', 'field': 'price_cents', 'label': 'Prijs', 'type': 'range', 'data_type': 'int64', 'unit': 'cent'},
    {'key': 'merk', 'field': 'vendor', 'label': 'Merk', 'type': 'choice', 'data_type': 'string'},
    {'key': 'productsoort', 'field': 'f_productsoort', 'label': 'Soort', 'type': 'choice', 'data_type': 'string'},
]
SCHEMA = {'name': 'fixture', 'fields': [
    {'name': 'id', 'type': 'string'},
    {'name': 'f_kleur', 'type': 'string[]', 'facet': True, 'optional': True},
    {'name': 'f_serie', 'type': 'string', 'facet': True, 'optional': True},
    {'name': 'f_productsoort', 'type': 'string', 'facet': True, 'optional': True},
    {'name': 'f_tegel_breedte_mm', 'type': 'float', 'facet': True, 'optional': True},
    {'name': 'f_tegel_lengte_mm', 'type': 'float', 'facet': True, 'optional': True},
    {'name': 'price_cents', 'type': 'int64'},
    {'name': 'vendor', 'type': 'string', 'facet': True},
]}
HANDLES = ('tegels', 'cottoceramix', 'marmerlook-tegels', 'wastafelkranen')
CATEGORIES = {f'gid://shopify/Collection/{i}': {'id': f'gid://shopify/Collection/{i}',
              'handle': handle, 'title': handle} for i, handle in enumerate(HANDLES, 1)}


def product(index, raw, tile=True, title=None):
    handles = ['tegels', 'cottoceramix'] if tile else ['wastafelkranen']
    if index in (2, 11):
        handles.append('marmerlook-tegels')
    links = [copy.deepcopy(c) for c in CATEGORIES.values() if c['handle'] in handles]
    return {'id': f'gid://shopify/Product/{index}',
        'title': title or f'Fixture tegel {index}', 'handle': f'fixture-tile-{index}',
        'vendor': 'Cottoceramix', 'productType': 'Vloertegel' if tile else 'Wastafelkraan',
        'status': 'ACTIVE', 'updatedAt': '2026-11-09T00:00:00Z',
        'onlineStoreUrl': f'https://example.test/products/fixture-{index}',
        'featuredMedia': {'image': {'url': f'https://example.test/{index}.jpg'}},
        'tile_look': {'value': raw, 'updatedAt': '2026-11-09T00:00:00Z'} if raw is not None else None,
        'color': {'value': 'Beige' if index % 2 else 'Wit'}, 'series': {'value': 'Fixture'},
        '_variants': [{'id': f'gid://shopify/ProductVariant/{index}', 'sku': f'LOOK-{index:02}', 'price': f'{20+index}.00'}],
        '_collections': links,
        '_filters': [{'id': f'gid://shopify/Metafield/{index}01', 'key': 'tegel_breedte_mm', 'value': '596'},
                     {'id': f'gid://shopify/Metafield/{index}02', 'key': 'tegel_lengte_mm', 'value': '596' if index % 2 else '1200'}]}


def products():
    # Twelve different source cases, including source aliases and unknowns.
    return [product(i, raw) for i, raw in enumerate(
        ('Stone', 'marmerlook', 'WOOD LOOK', 'Betonlook', 'metal', 'Terrazzo',
         'uni', 'decoratie', 'Zellige', 'Mystery supplier value', 'Marble', None), 1)] + [
         product(13, 'marmerlook', tile=False), product(14, None, title='Marmerlook marmeren houtlook travertin')]


def prepared(module, rows):
    definitions = module._bc_simple_definitions(copy.deepcopy(DEFINITIONS))
    schema = module._bc_add_variant_schema(copy.deepcopy(SCHEMA))
    schema = module._bc_simple_schema(schema)
    docs, stats, issues = module.normalize_products(copy.deepcopy(rows), copy.deepcopy(CATEGORIES), definitions, schema)
    stats.update(module.enrich_b2c_documents(docs, definitions, schema))
    profiles = module.make_profiles(docs, copy.deepcopy(CATEGORIES), {}, definitions)
    snapshot = {'profiles': profiles, 'variant_aliases_v1': True,
                'exact': sorted({alias for doc in docs for alias in doc['sku_aliases']})}
    module._bc_simple_snapshot(snapshot, docs)
    return docs, stats, issues, definitions, schema, snapshot


class ConfigGuards(unittest.TestCase):
    def test_unreviewed_source_is_rejected(self):
        for value in (None, b'worker', '', 'print(1)', PATCH.MARKER):
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                PATCH.patch_tile_look_worker(value)

    def test_conflicting_normalized_aliases_are_rejected(self):
        with self.assertRaises(RuntimeError):
            PATCH.reviewed_configuration(aliases={'Stone-LOOK': 'Marmerlook'})

    def test_unknown_target_and_bad_vocabularies_are_rejected(self):
        for taxonomy in ([], ['Only'], ['Stone', 'stone'], ['Stone look', 'Marmerlook'], [None, 'Effen']):
            with self.subTest(taxonomy=taxonomy), self.assertRaises(RuntimeError):
                PATCH.reviewed_configuration(taxonomy)
        with self.assertRaises(RuntimeError):
            PATCH.reviewed_configuration(aliases={'unknown': 'New category'})

    def test_taxonomy_subset_is_supported_without_invalid_default_aliases(self):
        taxonomy, aliases = PATCH.reviewed_configuration(('Steenlook', 'Marmerlook'), {'rotslook': 'Steenlook'})
        self.assertEqual(taxonomy, ('Steenlook', 'Marmerlook'))
        self.assertEqual(set(aliases.values()), set(taxonomy))
        self.assertEqual(aliases['rotslook'], 'Steenlook')


class WorkerIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not WORKER.is_file() or not API.is_file():
            raise RuntimeError('Explicit private worker/API fixtures are required; no skipped integration proof')
        cls.source = WORKER.read_text()
        cls.api = API.read_text()
        cls.patched = PATCH.patch_tile_look_worker(cls.source)

    def setUp(self):
        self.old, self.new = load(self.source), load(self.patched)

    def test_hashes_and_single_deterministic_hook(self):
        self.assertEqual(hashlib.sha256(self.source.encode()).hexdigest(), PATCH.BASE_WORKER_SHA256)
        self.assertEqual(hashlib.sha256(self.api.encode()).hexdigest(), PATCH.API_SHA256)
        self.assertEqual(self.patched.count(PATCH.MARKER), 1)
        self.assertEqual(self.patched, PATCH.patch_tile_look_worker(self.source))
        with self.assertRaises(RuntimeError):
            PATCH.patch_tile_look_worker(self.patched)

    def test_export_adds_only_existing_tiles_look(self):
        old = self.old.QUERIES['bulkProducts']; new = self.new.QUERIES['bulkProducts']
        fragment = 'tile_look: metafield(namespace: "tiles", key: "look") { value updatedAt }'
        self.assertEqual(new.count(fragment), 1)
        separator = '\\n ' if '\\n ' in old else '\n '
        self.assertEqual(new.replace(separator + fragment, '', 1), old)
        for key in set(self.old.QUERIES) - {'bulkProducts'}:
            self.assertEqual(self.old.QUERIES[key], self.new.QUERIES[key])

    def test_at_least_twelve_source_cases_and_unknowns(self):
        rows = products(); before = copy.deepcopy(rows)
        docs, *_ = prepared(self.new, rows)
        by_id = {doc['id']: doc for doc in docs}
        expected = ('Steenlook', 'Marmerlook', 'Houtlook', 'Betonlook', 'Metaallook',
                    'Terrazzo', 'Effen', 'Decoratief', 'Handvormlook', None, 'Marmerlook', None)
        for index, look in enumerate(expected, 1):
            with self.subTest(index=index):
                self.assertEqual(by_id[str(index)].get(PATCH.FIELD), look)
        self.assertEqual(rows, before)

    def test_non_tile_and_titles_are_not_classified(self):
        docs, *_ = prepared(self.new, products())
        by_id = {doc['id']: doc for doc in docs}
        self.assertNotIn(PATCH.FIELD, by_id['13'])
        self.assertNotIn(PATCH.FIELD, by_id['14'])

    def test_exact_aliases_do_not_turn_into_substring_or_free_classifiers(self):
        for value in ('Stone special', 'Mozaïek', 'Vintage', 'Marmerlook met een naam', ['Marmerlook'], 3, True):
            with self.subTest(value=value):
                self.assertIsNone(self.new._bc_tile_look_normalize(value))
        self.assertEqual(self.new._bc_tile_look_normalize('  WOOD-LOOK  '), 'Houtlook')

    def test_all_old_document_values_prices_images_and_source_memberships_are_preserved(self):
        old = prepared(self.old, products())[0]
        new = prepared(self.new, products())[0]
        stripped = [{k: v for k, v in doc.items() if k != PATCH.FIELD} for doc in new]
        self.assertEqual(stripped, old)
        self.assertTrue(all(doc['collection_handles'] == old[i]['collection_handles'] for i, doc in enumerate(new)))

    def test_prior_flags_and_color_format_counters_are_preserved(self):
        old = prepared(self.old, products())[-1]
        new = prepared(self.new, products())[-1]
        self.assertTrue(new['tile_looks_v1'])
        for key, value in old.items():
            if key != 'profiles':
                with self.subTest(key=key):
                    self.assertEqual(value, new[key])
        required = ('variant_aliases_v1', 'filter_simplification_v1', 'tile_format_codes_v1',
                    'acero_gray_v1', 'cotto_visual_colors_v1', 'tile_bone_beige_v1', 'more_tile_colors_v1')
        self.assertTrue(all(new.get(key) is True for key in required))

    def test_tile_and_cotto_look_facets_are_visible_closed_and_max_two_open(self):
        *_, snapshot = prepared(self.new, products())
        for handle in ('tegels', 'cottoceramix'):
            profile = snapshot['profiles'][handle]
            fields = [f for f in profile['filters'] if f['field'] == PATCH.FIELD]
            self.assertEqual(len(fields), 1)
            self.assertFalse(fields[0]['ui']['default_open'])
            self.assertEqual(fields[0]['ui']['section'], 'primary')
            self.assertEqual(fields[0]['ui']['control'], 'checkbox')
            self.assertLessEqual(sum(f['ui']['default_open'] for f in profile['filters']), 2)

    def test_cotto_remains_general_and_its_deferred_format_filter_is_not_added(self):
        *_, snapshot = prepared(self.new, products())
        cotto = snapshot['profiles']['cottoceramix']
        self.assertEqual(cotto['b2c_policy']['group'], 'general')
        self.assertNotIn('f_tegel_formaat', [f['field'] for f in cotto['filters']])
        self.assertNotIn('f_tegel_formaat', [f['field'] for f in cotto['allowed_filters']])

    def test_singleton_profiles_keep_valid_filter_allowed_but_do_not_show_false_choice(self):
        *_, snapshot = prepared(self.new, products())
        profile = snapshot['profiles']['marmerlook-tegels']
        self.assertIn(PATCH.FIELD, [f['field'] for f in profile['allowed_filters']])
        self.assertNotIn(PATCH.FIELD, [f['field'] for f in profile['filters']])
        self.assertTrue(any(f['field'] == PATCH.FIELD and f['reason'] == 'no_distinction'
                            for f in profile['b2c_policy']['suppressed']))

    def test_non_tile_profiles_do_not_gain_visible_look_facet(self):
        *_, snapshot = prepared(self.new, products())
        profile = snapshot['profiles']['wastafelkranen']
        self.assertNotIn(PATCH.FIELD, [f['field'] for f in profile['filters']])

    def test_schema_is_optional_and_conflicting_schema_is_rejected(self):
        schema = self.new._bc_simple_schema(copy.deepcopy(SCHEMA))
        look = next(f for f in schema['fields'] if f['name'] == PATCH.FIELD)
        self.assertEqual(look, {'name': PATCH.FIELD, 'type': 'string', 'facet': True, 'optional': True})
        bad = copy.deepcopy(SCHEMA)
        bad['fields'].append(dict(look, type='string[]'))
        with self.assertRaises(RuntimeError):
            self.new._bc_simple_schema(bad)

    def test_a_conflicting_definition_is_rejected(self):
        definitions = copy.deepcopy(DEFINITIONS)
        definitions.append({'key': 'tegel_uitstraling', 'field': PATCH.FIELD,
                            'type': 'range', 'data_type': 'float'})
        with self.assertRaises(RuntimeError):
            self.new._bc_simple_definitions(definitions)

    def test_snapshot_rejects_drift_and_missing_prior_flags(self):
        docs, *_, snapshot = prepared(self.new, products())
        altered = copy.deepcopy(docs); altered[0][PATCH.FIELD] = 'Marmerlook'
        with self.assertRaises(RuntimeError):
            self.new._bc_simple_snapshot({'variant_aliases_v1': True}, altered)
        with self.assertRaises(RuntimeError):
            self.new._bc_simple_snapshot({}, docs)

    def test_unknown_source_is_reported_and_does_not_get_an_other_bucket(self):
        docs, stats, issues, *_ = prepared(self.new, products())
        self.assertNotIn(PATCH.FIELD, next(d for d in docs if d['id'] == '10'))
        self.assertEqual(stats['tile_look_unrecognized_source_products'], 1)
        self.assertTrue(any(i['issue'] == 'unrecognized_tiles_look_value' for i in issues))
        self.assertNotIn('Overige', self.new._BC_TILE_LOOK_TAXONOMY)

    def test_current_legacy_look_names_are_supported(self):
        expected = {'Terrazzolook': 'Terrazzo', 'Marmerlook': 'Marmerlook',
                    'Steenlook': 'Steenlook', 'Patroontegels': 'Decoratief',
                    'Betonlook': 'Betonlook', 'Metaallook': 'Metaallook',
                    'Design': 'Decoratief', 'Houtlook': 'Houtlook', 'Effen': 'Effen'}
        for raw, canonical in expected.items():
            with self.subTest(raw=raw):
                self.assertEqual(self.new._bc_tile_look_normalize(raw), canonical)

    def test_new_stage_cases_have_exact_sets_or_and_unknown_and_facet_proof(self):
        docs, *_, snapshot = prepared(self.new, products())
        cases, facets = self.new.make_cases(docs, snapshot)
        look_cases = [c for c in cases if PATCH.FIELD in c['body'].get('filters', {})]
        self.assertGreaterEqual(len(look_cases), 20)
        self.assertTrue(any('OF-selectie' in c['name'] for c in look_cases))
        self.assertTrue(any('gecombineerd' in c['name'] for c in look_cases))
        for case in look_cases:
            expected = [d['id'] for d in self.new.selected(docs, snapshot, case['body'])]
            self.assertEqual(case['expected_ids'], expected)
        look_facets = [f for f in facets if f['field'] == PATCH.FIELD]
        self.assertEqual({f['body']['collection'] for f in look_facets}, {'tegels', 'cottoceramix'})
        for facet in look_facets:
            self.assertEqual(facet['expected_counts']['Marmerlook'], 2)

    def test_api_source_remains_byte_identical(self):
        self.assertEqual(self.new.patch_api(self.api), self.api)

    def test_existing_b2c_profile_checks_and_new_source_check_pass(self):
        docs, *_, snapshot = prepared(self.new, products())
        checks = self.new.check_b2c_profiles(docs, snapshot)
        self.assertTrue(checks)
        self.assertTrue(all(c['passed'] for c in checks), checks)


class CurrentCatalogRegression(unittest.TestCase):
    """Actual 3,496 identities/source fields, fixed fixture-only prices.

    Prices are intentionally not a new live-price claim; they are constant test
    payloads whose byte-for-byte preservation between workers is checked.
    """
    @classmethod
    def setUpClass(cls):
        source = WORKER.read_text()
        cls.old, cls.new = load(source), load(PATCH.patch_tile_look_worker(source))
        live = json.loads((ROOT / 'tile-look-20261109/shopify-live-look-private.json').read_text())['rows']
        colors = json.loads((ROOT / 'tile-filters/catalog-colors.json').read_text())['rows']
        by_id = {row['id']: row for row in colors}
        if len(live) != 3496 or set(by_id) != {row['id'] for row in live}:
            raise RuntimeError('Current look/catalog fixtures no longer share the reviewed 3496 identities')
        categories = {}
        products = []
        for row in live:
            prior = by_id[row['id']]
            if (row['handle'], row['title'], row['vendor']) != (prior['handle'], prior['title'], prior['vendor']):
                raise RuntimeError('Source fixture drift must be reviewed')
            if row['collections']['pageInfo']['hasNextPage'] or row['variants']['pageInfo']['hasNextPage']:
                raise RuntimeError('Fixture child pagination is incomplete')
            links = [dict(c, title=c['handle']) for c in row['collections']['nodes']]
            for category in links:
                categories[category['id']] = category
            variants = [dict(v, price='100.00') for v in row['variants']['nodes']]
            filters = []
            for key, original in [('tegel_breedte_mm', 'width'), ('tegel_lengte_mm', 'length')]:
                raw = (prior.get(original) or {}).get('value')
                if raw:
                    filters.append({'key': key, 'value': raw})
            raw_color = prior.get('resolved_color')
            products.append({'id': row['id'], 'title': row['title'], 'handle': row['handle'],
                'vendor': row['vendor'], 'productType': (prior.get('application') or {}).get('value') or 'Tegel',
                'status': 'ACTIVE', 'updatedAt': row['updatedAt'],
                'onlineStoreUrl': prior['onlineStoreUrl'],
                'featuredMedia': {'image': {'url': 'https://example.test/preserved-fixture-image.jpg'}},
                'tile_look': row['look'], 'color': {'value': raw_color} if raw_color else None,
                'series': prior.get('series'), '_collections': links,
                '_variants': variants, '_filters': filters})
        cls.products, cls.categories = products, categories
        cls.results = []
        for module in (cls.old, cls.new):
            definitions = module._bc_simple_definitions(copy.deepcopy(DEFINITIONS))
            schema = module._bc_simple_schema(module._bc_add_variant_schema(copy.deepcopy(SCHEMA)))
            docs, stats, issues = module.normalize_products(copy.deepcopy(products), copy.deepcopy(categories), definitions, schema)
            stats.update(module.enrich_b2c_documents(docs, definitions, schema))
            profiles = module.make_profiles(docs, categories, {}, definitions)
            snapshot = {'profiles': profiles, 'variant_aliases_v1': True,
                        'exact': sorted({alias for d in docs for alias in d['sku_aliases']})}
            module._bc_simple_snapshot(snapshot, docs)
            cls.results.append((docs, stats, issues, snapshot))

    def test_all_3496_existing_document_values_are_preserved(self):
        old, new = self.results[0][0], self.results[1][0]
        self.assertEqual(len(old), 3496)
        self.assertEqual([{k: v for k, v in d.items() if k != PATCH.FIELD} for d in new], old)

    def test_all_358_legacy_sources_map_and_3138_empty_sources_stay_empty(self):
        new = self.results[1][3]
        self.assertEqual(new['tile_look_products'], 358)
        self.assertEqual(new['tile_look_missing_products'], 3138)
        self.assertEqual(new['tile_look_counts'], {'Terrazzo': 22, 'Marmerlook': 59,
            'Steenlook': 116, 'Decoratief': 61, 'Betonlook': 46,
            'Metaallook': 6, 'Houtlook': 43, 'Effen': 5})
        self.assertEqual(self.results[1][1].get('tile_look_unrecognized_source_products', 0), 0)

    def test_prior_actual_color_and_format_regressions_are_preserved(self):
        old_docs, _, _, old = self.results[0]
        new_docs, _, _, new = self.results[1]
        for key, value in old.items():
            if key != 'profiles':
                self.assertEqual(value, new[key], key)
        self.assertEqual(new['acero_gray_products'], 27)
        self.assertEqual(new['tile_bone_beige_products'], 65)
        self.assertEqual(new['cotto_visual_color_products'], 353)
        self.assertEqual(new['more_scoped_color_products'], 155)
        self.assertEqual(new['more_missing_color_products'], 418)
        self.assertEqual(len(new['tile_format_codes']), 132)
        self.assertEqual(sum(bool(d.get('f_kleur')) for d in new_docs), 3353)
        for label, expected in [('60 × 60 cm', 159), ('60 × 120 cm', 58), ('60 × 150 cm', 92)]:
            self.assertEqual(sum(d.get('f_tegel_formaat') == label for d in old_docs), expected)
            self.assertEqual(sum(d.get('f_tegel_formaat') == label for d in new_docs), expected)


if __name__ == '__main__':
    unittest.main()
