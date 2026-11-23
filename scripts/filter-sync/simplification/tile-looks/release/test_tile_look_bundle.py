"""Standalone transport, real candidate contract, and live-route adapter tests.

All network/system operations are mocked. Private fixtures remain local.
"""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import Mock


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


M = module(HERE / 'apply_tile_look_filter.py', 'look_bundle_installer_template')
B = module(HERE / 'build_tile_look_filter.py', 'look_bundle_builder')
WORKER = ROOT / 'more-colors-20261108/release/private-target-sync.py'
API = ROOT / 'filter-implementation/acero-correction/private-current-app.py'
PATCH = HERE.parent / 'worker/tile_look_worker_patch.py'


class StandaloneBundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.output = Path(cls.temp.name) / 'repair_tile_look_filter.py'
        cls.manifest = B.build(WORKER, API, PATCH, cls.output)
        cls.text = cls.output.read_text()
        cls.bundle = module(cls.output, 'look_frozen_installer_tested')

    def test_ascii_roundtrip_and_exact_target_hash(self):
        self.assertTrue(self.text.isascii())
        self.assertEqual(self.manifest['installer_sha256'], M.sha256(self.output.read_bytes()))
        base = WORKER.read_bytes()
        patched = self.bundle.compose_worker(base, self.bundle.PATCH_SOURCES)
        self.assertEqual(M.sha256(patched), self.manifest['target_worker_sha256'])
        self.assertEqual(M.sha256(patched), '79f676d035fdd6d250e2daec51b886d1aa54c117707718d7ea9695300c21c43d')
        self.assertEqual(self.bundle.load_worker(patched).patch_api(API.read_text()), API.read_text())
        self.assertEqual(tuple(self.bundle.TARGET_LOOK_TAXONOMY), tuple(self.manifest['taxonomy']))
        self.assertEqual(len(self.manifest['required_snapshot_flags']), 8)

    def test_no_private_worker_api_or_catalog_ids_are_embedded(self):
        self.assertNotIn(WORKER.read_text(), self.text)
        self.assertNotIn(API.read_text(), self.text)
        self.assertNotIn('gid://shopify/Product/', self.text)
        self.assertEqual(set(self.bundle.PATCH_SOURCES), {'worker'})
        self.assertIs(self.manifest['private_runtime_sources_embedded'], False)
        self.assertIs(self.manifest['private_catalog_or_product_ids_embedded'], False)

    def test_changed_api_bytes_are_rejected_even_if_ast_is_the_same(self):
        original = API.read_bytes()
        changed = Path(self.temp.name) / 'changed-api.py'
        changed.write_bytes(b'\n' + original)
        self.assertEqual(M.ast_digest(original), M.ast_digest(changed.read_bytes()))
        target = Path(self.temp.name) / 'must-not-exist-api.py'
        with self.assertRaises(RuntimeError):
            B.build(WORKER, changed, PATCH, target)
        self.assertFalse(target.exists())

    def test_changed_worker_is_rejected_before_output(self):
        changed = Path(self.temp.name) / 'changed-worker.py'
        changed.write_bytes(WORKER.read_bytes() + b'\n')
        target = Path(self.temp.name) / 'must-not-exist-worker.py'
        with self.assertRaises(RuntimeError):
            B.build(changed, API, PATCH, target)
        self.assertFalse(target.exists())

    def test_bundling_is_deterministic(self):
        output = Path(self.temp.name) / 'same-content-other-name.py'
        manifest = B.build(WORKER, API, PATCH, output)
        self.assertEqual(output.read_bytes(), self.output.read_bytes())
        self.assertEqual(manifest['installer_sha256'], self.manifest['installer_sha256'])

    def test_actual_3496_candidate_snapshot_matches_frozen_lifecycle_contract(self):
        tests = module(HERE.parent / 'worker/test_tile_look_worker_patch.py', 'look_real_contract_fixtures')
        tests.CurrentCatalogRegression.setUpClass()
        snapshot = tests.CurrentCatalogRegression.results[1][3]
        self.assertTrue(self.bundle.validate_look_snapshot(snapshot))
        self.assertEqual(snapshot['tile_look_products'], 358)
        self.assertEqual(snapshot['tile_look_missing_products'], 3138)


def sample_snapshot():
    definition = {'key': 'tegel_uitstraling', 'field': M.LOOK_FIELD, 'label': 'Uitstraling',
                  'type': 'choice', 'data_type': 'string'}
    visible = {**definition, 'distinct_values': 2, 'coverage_pct': 100.0,
               'ui': {'control': 'checkbox', 'section': 'primary', 'default_open': False}}
    return {'generation': 'new', 'collection': 'new_index',
            **{flag: True for flag in M.REQUIRED_FLAGS},
            'tile_look_source': 'tiles.look', 'tile_look_taxonomy': ['Steenlook', 'Marmerlook'],
            'tile_look_products': 2, 'tile_look_missing_products': 0,
            'tile_look_counts': {'Steenlook': 1, 'Marmerlook': 1},
            'profiles': {handle: {'shopping_products': 2, 'filters': [copy.deepcopy(visible)],
                'allowed_filters': [copy.deepcopy(definition)], 'b2c_policy': {'group': group,
                'tile_looks_v1': True, 'default_open_fields': []}}
                for handle, group in [('tegels', 'tile'), ('cottoceramix', 'general')]}}


class LiveLookAdapterTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = sample_snapshot()
        self.mode = 'success'
        self.worker = types.SimpleNamespace(probe=Mock(side_effect=self.probe))

    def probe(self, url, body=None):
        if url.endswith('/health'):
            return {'ok': True, 'typesense_collection': 'manual_index' if self.mode == 'wrong_generation' else 'new_index'}, {}
        if '/api/v1/profile/' in url:
            handle = url.rsplit('/', 1)[-1]
            profile = self.snapshot['profiles'][handle]
            fields = copy.deepcopy(profile['filters'])
            if self.mode == 'open_cotto' and handle == 'cottoceramix':
                fields[0]['ui']['default_open'] = True
            return {'filters': fields, 'filter_policy': copy.deepcopy(profile['b2c_policy'])}, {}
        if url.endswith('/api/v1/search'):
            value = body['filters'][M.LOOK_FIELD][0]
            count = self.snapshot['tile_look_counts'].get(value, 0)
            if self.mode == 'wrong_count' and value == 'Steenlook':
                count += 1
            return {'found': count, 'collection': {'handle': 'tegels'}}, {}
        raise AssertionError('Unexpected route')

    def test_local_and_public_routes_match_dynamic_profiles_and_counts(self):
        checks = M.verify_live_look_routes(self.worker, self.snapshot)
        self.assertEqual(len(checks), 12)
        self.assertTrue(all(check['passed'] for check in checks), checks)
        self.assertTrue(any(check['name'].startswith('Lokale') for check in checks))
        self.assertTrue(any(check['name'].startswith('Publieke') for check in checks))

    def test_wrong_live_count_is_not_marked_passed(self):
        self.mode = 'wrong_count'
        checks = M.verify_live_look_routes(self.worker, self.snapshot)
        bad = [check for check in checks if not check['passed']]
        self.assertEqual(len(bad), 2)
        self.assertTrue(all(check['name'].endswith('Steenlook') for check in bad))

    def test_open_cotto_facet_is_not_marked_passed(self):
        self.mode = 'open_cotto'
        checks = M.verify_live_look_routes(self.worker, self.snapshot)
        bad = [check for check in checks if not check['passed']]
        self.assertEqual(len(bad), 2)
        self.assertTrue(all(check['name'].endswith('cottoceramix') for check in bad))

    def test_manual_generation_change_stops_count_probes(self):
        self.mode = 'wrong_generation'
        checks = M.verify_live_look_routes(self.worker, self.snapshot)
        self.assertEqual(len(checks), 2)
        self.assertTrue(all(not check['passed'] for check in checks))
        self.assertEqual(self.worker.probe.call_count, 2)


if __name__ == '__main__':
    unittest.main()
