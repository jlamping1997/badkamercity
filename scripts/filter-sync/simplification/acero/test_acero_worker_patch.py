"""Tests use private runtime/catalog fixtures through optional environment paths.

No product export or runtime source belongs in the public repository. The two
private fixture suites explicitly skip when those files are not provided.
"""
import ast
import copy
import importlib.util
import json
import os
from pathlib import Path
import sys
import types
import unittest

FOLDER = Path(__file__).resolve().parent
sys.path.insert(0, str(FOLDER))
import apply_acero_worker_patch as patch

WORKER = Path(os.environ.get('BC_ACERO_WORKER_SOURCE', FOLDER / 'private-current-sync.py'))
API = Path(os.environ.get('BC_ACERO_API_SOURCE', FOLDER / 'private-current-app.py'))
CATALOG = Path(os.environ.get('BC_ACERO_TILE_CATALOG', FOLDER.parent.parent / 'tile-filters/catalog-colors.json'))


def load(source):
    module = types.ModuleType('_bc_acero_worker_test')
    module.__file__ = str(FOLDER / 'candidate-sync.py')
    exec(compile(source, module.__file__, 'exec'), module.__dict__)
    return module


def doc(color='Acero', handles=None, vendor='Porcelanosa', series='Bottega'):
    return {'id': 'fixture', 'title': 'Tile fixture', 'vendor': vendor,
            'f_serie': series, 'collection_handles': ['tegels'] if handles is None else handles,
            'general_shopping': True, 'sku_exact': 'fixture', 'f_kleur': color,
            'f_tegel_breedte_mm': 596, 'f_tegel_lengte_mm': 596}


def enrich(module, source):
    docs = copy.deepcopy(source)
    module.enrich_b2c_documents(docs, [], {'fields': []})
    return docs


class SourceGuards(unittest.TestCase):
    def test_unreviewed_worker_rejected(self):
        for source in ('', 'print(1)', patch.MARKER, None, b'worker'):
            with self.subTest(source=type(source).__name__):
                with self.assertRaises(RuntimeError):
                    patch.patch_acero_worker(source)


@unittest.skipUnless(WORKER.is_file(), 'private reviewed worker fixture not provided')
class ReviewedWorkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = WORKER.read_text()
        cls.target = patch.patch_acero_worker(cls.source)
        cls.old = load(cls.source)
        cls.new = load(cls.target)

    def test_hashes_idempotence_and_changed_source_guard(self):
        self.assertEqual(patch._sha(self.target), patch.PATCHED_WORKER_SHA256)
        self.assertEqual(patch.patch_acero_worker(self.target), self.target)
        for source in (self.source + '\n', self.target + '\n'):
            with self.assertRaises(RuntimeError):
                patch.patch_acero_worker(source)

    def test_only_known_tile_membership_enables_rule(self):
        for handles in (['tegels'], ['betonlook-tegels'], ['wandtegels'], ['vloertegels']):
            before = doc(handles=handles)
            old = enrich(self.old, [before])[0]
            new = enrich(self.new, [before])[0]
            self.assertEqual(old['f_kleur'], ['Zilver'])
            self.assertEqual(new['f_kleur'], ['Grijs'])
            self.assertEqual(new['f_kleur_exact'], 'Acero')
            self.assertEqual(before['f_kleur'], 'Acero')
        for handles in ([], ['kranen'], ['wastafelkranen'], ['cottoceramix'], ['tegels-extra']):
            before = doc(handles=handles, vendor='Fixture steel', series='Fixture')
            self.assertEqual(enrich(self.new, [before]), enrich(self.old, [before]))

    def test_case_whitespace_and_exact_only(self):
        for color in ('Acero', 'ACERO', ' acero ', 'AcErO'):
            after = enrich(self.new, [doc(color)])[0]
            self.assertEqual(after['f_kleur'], ['Grijs'])
            self.assertEqual(after['f_kleur_exact'], color)
        for color in ('Bone acero', 'Bone-acero', 'Acero inoxidable', 'RVS', 'Caliza', 'Goud', 'Groen'):
            source = [doc(color)]
            self.assertEqual(enrich(self.new, source), enrich(self.old, source))

    def test_existing_owner_rule_kept(self):
        source = [doc(vendor='Cottoceramix', series='Malaga')]
        self.assertEqual(enrich(self.new, source), enrich(self.old, source))
        self.assertEqual(enrich(self.new, source)[0]['f_kleur'], ['Grijs'])

    def test_exact_dimensions_and_format_codes_unchanged(self):
        source = [dict(doc(), id='one'), dict(doc(), id='two', f_tegel_lengte_mm=1196),
                  dict(doc(), id='three', f_tegel_lengte_mm=1500)]
        old, new = enrich(self.old, source), enrich(self.new, source)
        for a, b in zip(old, new):
            self.assertEqual({k:v for k,v in a.items() if k != 'f_kleur'},
                             {k:v for k,v in b.items() if k != 'f_kleur'})
        self.assertEqual([d['f_tegel_formaat'] for d in new], ['60 × 60 cm', '60 × 120 cm', '60 × 150 cm'])
        self.assertTrue(self.new._bc_simple_check_tile_codes(new, self.new._bc_simple_tile_code_map(new)))

    def test_snapshot_records_rule_and_rejects_wrong_color(self):
        docs = enrich(self.new, [doc()])
        snapshot = {}
        self.new._bc_simple_snapshot(snapshot, docs)
        self.assertTrue(snapshot['acero_gray_v1'])
        self.assertEqual(snapshot['acero_gray_products'], 1)
        self.assertTrue(snapshot['filter_simplification_v1'])
        self.assertTrue(snapshot['tile_format_codes_v1'])
        self.assertEqual(snapshot['filter_color_aliases']['Acero'], 'Grijs')
        docs[0]['f_kleur'] = ['Zilver']
        self.assertFalse(self.new._bc_acero_check(docs))
        with self.assertRaises(RuntimeError):
            self.new._bc_simple_snapshot({}, docs)
        docs[0]['f_kleur'] = ['Grijs', 'Zilver']
        self.assertFalse(self.new._bc_acero_check(docs))

    def test_unrelated_worker_functions_ast_unchanged(self):
        old_nodes = [node for node in ast.parse(self.source).body if isinstance(node, ast.FunctionDef)]
        new_nodes = [node for node in ast.parse(self.target).body if isinstance(node, ast.FunctionDef)]
        names = {'enrich_b2c_documents', '_bc_simple_snapshot', 'check_b2c_profiles'}
        old = [ast.dump(node, include_attributes=False) for node in old_nodes if node.name not in names]
        new = [ast.dump(node, include_attributes=False) for node in new_nodes
               if node.name not in names and not node.name.startswith('_bc_acero_')]
        self.assertEqual(old, new)

    @unittest.skipUnless(API.is_file(), 'private reviewed API fixture not provided')
    def test_api_is_byte_identical(self):
        source = API.read_bytes()
        self.assertEqual(self.new.patch_api(source.decode()).encode(), source)
        self.assertEqual(self.new.patch_api(source.decode()), self.old.patch_api(source.decode()))

    @unittest.skipUnless(CATALOG.is_file(), 'private tile catalog fixture not provided')
    def test_real_catalog_only_26_changes_in_27_exact_acero_tiles(self):
        rows = json.loads(CATALOG.read_text())['rows']
        sources = []
        for row in rows:
            item = doc(row.get('resolved_color') or '', vendor=row['vendor'],
                       series=(row.get('series') or {}).get('value') or '')
            item.update(id=row['id'], title=row['title'])
            for key, field in [('width', 'f_tegel_breedte_mm'), ('length', 'f_tegel_lengte_mm')]:
                value = (row.get(key) or {}).get('value')
                if value:
                    item[field] = float(value)
                else:
                    item.pop(field, None)
            sources.append(item)
        old, new = enrich(self.old, sources), enrich(self.new, sources)
        targets = self.new._bc_acero_targets(new)
        self.assertEqual(len(targets), 27)
        self.assertEqual(sum(a != b for a,b in zip(old,new)), 26)
        for a,b in zip(old,new):
            if a != b:
                self.assertEqual(a['f_kleur'], ['Zilver'])
                self.assertEqual(b['f_kleur'], ['Grijs'])
                self.assertEqual(b['f_kleur_exact'], 'Acero')
                self.assertEqual({k:v for k,v in a.items() if k != 'f_kleur'},
                                 {k:v for k,v in b.items() if k != 'f_kleur'})
        self.assertTrue(self.new._bc_acero_check(new))
        self.assertEqual(self.new._bc_simple_tile_code_map(new), self.old._bc_simple_tile_code_map(old))
        self.assertEqual(len(self.new._bc_simple_tile_code_map(new)), 132)


if __name__ == '__main__':
    unittest.main()
