"""Scope/invariant tests; private runtime and catalog fixtures are optional."""
import ast
import copy
import importlib.util
import json
import os
from pathlib import Path
import types
import unittest

FOLDER = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('cotto_worker_template_tested', FOLDER / 'cotto_worker_patch_template.py')
TEMPLATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TEMPLATE)
WORKER = Path(os.environ.get('BC_COTTO_WORKER_SOURCE', FOLDER / 'private-current-sync.py'))
API = Path(os.environ.get('BC_COTTO_API_SOURCE', FOLDER / 'private-current-app.py'))
CATALOG = Path(os.environ.get('BC_COTTO_TILE_CATALOG', FOLDER / 'private-tile-catalog.json'))
FROZEN = FOLDER / 'apply_cotto_worker_patch.py'

FIXTURE_RULES = [
    {'series': 'Fixture Coast', 'exact_color': 'Ash', 'colors': ['Beige'], 'confidence': .90},
    {'series': 'Fixture Rock', 'exact_color': 'Ash', 'colors': ['Grijs'], 'confidence': .90},
    {'series': 'Fixture Coast', 'exact_color': 'Cloud', 'colors': ['Grijs', 'Wit'], 'confidence': .80},
]


def load_worker(source):
    module = types.ModuleType('bc_cotto_worker_test')
    module.__file__ = str(FOLDER / 'private-candidate-sync.py')
    exec(compile(source, module.__file__, 'exec'), module.__dict__)
    return module


def patch_module(rules):
    module = types.ModuleType('bc_cotto_patch_test')
    exec(compile((FOLDER / 'cotto_worker_patch_template.py').read_text(), '<pure-cotto-patch>', 'exec'), module.__dict__)
    module.SCOPED_RULES = rules
    return module


def doc(color='Ash', series='Fixture Coast', vendor='Cottoceramix', handles=None):
    return {'id': 'fixture', 'title': 'Fixture Coast Ash tile', 'vendor': vendor,
            'f_serie': series, 'collection_handles': ['tegels'] if handles is None else handles,
            'general_shopping': True, 'sku_exact': 'fixture', 'f_kleur': color,
            'f_tegel_breedte_mm': 596, 'f_tegel_lengte_mm': 596}


def enrich(module, source):
    result = copy.deepcopy(source)
    module.enrich_b2c_documents(result, [], {'fields': []})
    return result


class SourceAndRuleGuards(unittest.TestCase):
    def namespace(self):
        normalize = lambda value: str(value).strip().casefold()
        return {'normalize': normalize,
                'normalize_series': lambda value: normalize(value).replace('-r', ''),
                'TAXONOMY': ('Wit', 'Grijs', 'Beige', 'Bruin'),
                'OWNER_RULES': [('Cottoceramix', 'Malaga', 'Bone', ['Wit'], 'Wit')]}

    def test_unreviewed_source_rejected(self):
        for source in (None, b'bytes', '', 'print(1)', TEMPLATE.MARKER):
            with self.assertRaises(RuntimeError):
                TEMPLATE.patch_cotto_worker(source)

    def test_conflicting_normalized_series_rules_rejected(self):
        rules = [dict(FIXTURE_RULES[0], series='Fixture'),
                 dict(FIXTURE_RULES[0], series='Fixture-R', colors=['Grijs'])]
        with self.assertRaisesRegex(RuntimeError, 'Tegenstrijdige'):
            TEMPLATE.reviewed_rule_map(rules, self.namespace())

    def test_identical_normalized_aliases_allowed_once(self):
        rules = [dict(FIXTURE_RULES[0], series='Fixture'),
                 dict(FIXTURE_RULES[0], series='Fixture-R')]
        self.assertEqual(TEMPLATE.reviewed_rule_map(rules, self.namespace()), {('fixture', 'ash'): ['Beige']})

    def test_invalid_confidence_and_color_values_rejected(self):
        values = [None, True, .69, 1.1, float('nan'), '0.9']
        for value in values:
            with self.assertRaises(RuntimeError):
                TEMPLATE.reviewed_rule_map([dict(FIXTURE_RULES[0], confidence=value)], self.namespace())
        for colors in (None, [], ['Overige kleuren'], ['Wit', 'Wit'], [{}]):
            with self.assertRaises(RuntimeError):
                TEMPLATE.reviewed_rule_map([dict(FIXTURE_RULES[0], colors=colors)], self.namespace())

    def test_existing_owner_and_acero_rules_cannot_be_overridden(self):
        for rule in [dict(FIXTURE_RULES[0], series='Malaga', exact_color='Bone', colors=['Beige']),
                     dict(FIXTURE_RULES[0], exact_color='Acero', colors=['Beige'])]:
            with self.assertRaises(RuntimeError):
                TEMPLATE.reviewed_rule_map([rule], self.namespace())

    def test_colors_ordered_by_existing_taxonomy(self):
        self.assertEqual(TEMPLATE.reviewed_rule_map([FIXTURE_RULES[2]], self.namespace()),
                         {('fixture coast', 'cloud'): ['Wit', 'Grijs']})


@unittest.skipUnless(WORKER.is_file(), 'private reviewed current worker not provided')
class FixtureWorkerIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = WORKER.read_text()
        cls.patch = patch_module(FIXTURE_RULES)
        cls.target = cls.patch.patch_cotto_worker(cls.source)
        cls.patch.PATCHED_WORKER_SHA256 = cls.patch._sha(cls.target)
        cls.old, cls.new = load_worker(cls.source), load_worker(cls.target)

    def test_only_exact_vendor_series_tile_and_color_match(self):
        self.assertEqual(enrich(self.new, [doc()])[0]['f_kleur'], ['Beige'])
        self.assertEqual(enrich(self.new, [doc(series='Fixture Rock')])[0]['f_kleur'], ['Grijs'])
        for source in [doc(vendor='Porcelanosa'), doc(series='Fixture Other'),
                       doc(color='Ash New'), doc(handles=['cottoceramix']),
                       doc(handles=['wastafelkranen']), doc(handles=['tegels-extra'])]:
            self.assertEqual(enrich(self.old, [source]), enrich(self.new, [source]))

    def test_case_normalization_and_raw_source_preserved(self):
        source = doc(color=' ASH ', series='fixture coast', vendor='COTTOCERAMIX')
        new = enrich(self.new, [source])[0]
        self.assertEqual(new['f_kleur'], ['Beige'])
        self.assertEqual(new['f_kleur_exact'], ' ASH ')
        self.assertEqual(source['f_kleur'], ' ASH ')

    def test_missing_or_ambiguous_explicit_series_does_not_use_new_rule(self):
        for value in (None, '', ['Fixture Coast', 'Fixture Rock']):
            source = doc(series=value)
            source['title'] = 'Fixture Coast Ash tile'
            self.assertEqual(enrich(self.old, [source]), enrich(self.new, [source]))

    def test_inference_status_and_existing_owner_rule_preserved(self):
        colors = self.new._BC_SIMPLE_COLORS
        result = colors['classify_color']('Ash', {'vendor': 'Cottoceramix', 'series': 'Fixture Coast',
                                                'is_tile': True, 'cotto_explicit_series': True})
        self.assertEqual(result['confidence'], 'INFERRED_VISUAL')
        existing = doc(color='Bone', series='Malaga')
        self.assertEqual(enrich(self.old, [existing]), enrich(self.new, [existing]))
        acero = doc(color='Acero', series='Bottega', vendor='Porcelanosa')
        self.assertEqual(enrich(self.old, [acero]), enrich(self.new, [acero]))
        self.assertEqual(enrich(self.new, [acero])[0]['f_kleur'], ['Grijs'])

    def test_size_codes_and_other_document_fields_identical(self):
        source = [dict(doc(), id='one'), dict(doc(), id='two', f_tegel_lengte_mm=1196),
                  dict(doc(), id='three', f_tegel_lengte_mm=1500)]
        old, new = enrich(self.old, source), enrich(self.new, source)
        for a, b in zip(old, new):
            self.assertEqual({k:v for k,v in a.items() if k != 'f_kleur'},
                             {k:v for k,v in b.items() if k != 'f_kleur'})
        self.assertEqual([d['f_tegel_formaat'] for d in new],
                         ['60 × 60 cm', '60 × 120 cm', '60 × 150 cm'])

    def test_snapshot_flags_counts_and_wrong_color_rejected(self):
        docs = enrich(self.new, [doc()]);snapshot = {}
        self.new._bc_simple_snapshot(snapshot, docs)
        self.assertIs(snapshot['cotto_visual_colors_v1'], True)
        self.assertIs(snapshot['acero_gray_v1'], True)
        self.assertEqual(snapshot['cotto_visual_color_products'], 1)
        docs[0]['f_kleur'] = ['Grijs']
        self.assertFalse(self.new._bc_cotto_check(docs))
        with self.assertRaises(RuntimeError):
            self.new._bc_simple_snapshot({}, docs)

    def test_idempotence_and_hash_drift_guards(self):
        self.assertEqual(self.patch.patch_cotto_worker(self.target), self.target)
        for source in (self.source + '\n', self.target + '\n'):
            with self.assertRaises(RuntimeError):
                self.patch.patch_cotto_worker(source)

    def test_only_snapshot_and_profile_functions_changed(self):
        def functions(source):
            return [ast.dump(node, include_attributes=False) for node in ast.parse(source).body
                    if isinstance(node, ast.FunctionDef)
                    and node.name not in ('_bc_simple_snapshot', 'check_b2c_profiles')
                    and not node.name.startswith('_bc_cotto_')]
        self.assertEqual(functions(self.source), functions(self.target))

    @unittest.skipUnless(API.is_file(), 'private reviewed API source not provided')
    def test_api_source_byte_identical(self):
        source = API.read_bytes()
        self.assertEqual(self.new.patch_api(source.decode()).encode(), source)


@unittest.skipUnless(WORKER.is_file() and CATALOG.is_file() and FROZEN.is_file(),
                     'final frozen patch and private runtime/catalog not provided')
class FinalCatalogIntegration(unittest.TestCase):
    def test_final_rules_only_change_target_colors_and_keep_entire_other_catalog(self):
        namespace = {'__name__': 'final_cotto_worker_patch_test'}
        exec(compile(FROZEN.read_text(), str(FROZEN), 'exec'), namespace)
        source = WORKER.read_text();target = namespace['patch_cotto_worker'](source)
        self.assertEqual(namespace['_sha'](target), namespace['PATCHED_WORKER_SHA256'])
        old, new = load_worker(source), load_worker(target)
        sources = []
        for row in json.loads(CATALOG.read_text())['rows']:
            item = doc(row.get('resolved_color') or '', (row.get('series') or {}).get('value') or '', row['vendor'])
            item.update(id=row['id'], title=row['title'])
            for key, field in [('width', 'f_tegel_breedte_mm'), ('length', 'f_tegel_lengte_mm')]:
                value = (row.get(key) or {}).get('value')
                if value:
                    item[field] = float(value)
                else:
                    item.pop(field, None)
            sources.append(item)
        before, after = enrich(old, sources), enrich(new, sources)
        changed = 0
        for a, b in zip(before, after):
            if a != b:
                changed += 1
                self.assertIsNotNone(new._bc_cotto_expected_color(b))
                self.assertEqual(b['f_kleur'], new._bc_cotto_expected_color(b))
            self.assertEqual({k:v for k,v in a.items() if k != 'f_kleur'},
                             {k:v for k,v in b.items() if k != 'f_kleur'})
        self.assertGreater(changed, 0)
        self.assertTrue(new._bc_cotto_check(after))
        self.assertTrue(new._bc_acero_check(after))
        self.assertEqual(old._bc_simple_tile_code_map(before), new._bc_simple_tile_code_map(after))
        self.assertEqual(len(new._bc_simple_tile_code_map(after)), 132)
        if API.is_file():
            api = API.read_bytes()
            self.assertEqual(new.patch_api(api.decode()).encode(), api)


if __name__ == '__main__':
    unittest.main()
