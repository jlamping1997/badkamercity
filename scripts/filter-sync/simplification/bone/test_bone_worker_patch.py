"""Exact Bone tile ownership rule and previous Cotto-release invariants."""
import ast
import copy
import importlib.util
import json
import os
from pathlib import Path
import types
import unittest

FOLDER = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('bone_patch_tested', FOLDER / 'apply_bone_worker_patch.py')
PATCH = importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(PATCH)
WORKER = Path(os.environ.get('BC_BONE_WORKER_SOURCE', FOLDER / 'private-current-sync.py'))
API = Path(os.environ.get('BC_BONE_API_SOURCE', FOLDER / 'private-current-app.py'))
CATALOG = Path(os.environ.get('BC_BONE_TILE_CATALOG', FOLDER / 'private-tile-catalog.json'))
ORIGINAL = Path(os.environ.get('BC_BONE_ORIGINAL_WORKER_SOURCE', FOLDER / 'private-original-sync.py'))


def load(source):
    m=types.ModuleType('bc_bone_test_worker');m.__file__=str(FOLDER/'private-candidate-sync.py')
    exec(compile(source,m.__file__,'exec'),m.__dict__);return m


def doc(color='Bone',vendor='Porcelanosa',series='Fixture',handles=None):
    return {'id':'fixture','title':'Fixture tile','vendor':vendor,'f_serie':series,
            'collection_handles':['tegels'] if handles is None else handles,
            'general_shopping':True,'sku_exact':'fixture','f_kleur':color,
            'f_tegel_breedte_mm':596,'f_tegel_lengte_mm':596}


def enrich(module,source):
    result=copy.deepcopy(source);module.enrich_b2c_documents(result,[],{'fields':[]});return result


class SourceGuard(unittest.TestCase):
    def test_unreviewed_source_rejected(self):
        for source in (None,b'worker','',PATCH.MARKER,'print(1)'):
            with self.assertRaises(RuntimeError):PATCH.patch_bone_worker(source)


@unittest.skipUnless(WORKER.is_file(),'private cc13 worker source not provided')
class BoneIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=WORKER.read_text();cls.target=PATCH.patch_bone_worker(cls.source)
        cls.old,cls.new=load(cls.source),load(cls.target)

    def test_all_tile_brands_and_case_variants_use_owner_confirmed_beige(self):
        for vendor in ('Cottoceramix','Porcelanosa','Fixture Tile'):
            for raw in ('Bone','BONE',' bone ','BoNe'):
                value=enrich(self.new,[doc(raw,vendor)])[0]
                self.assertEqual(value['f_kleur'],['Beige']);self.assertEqual(value['f_kleur_exact'],raw)
        result=self.new._BC_SIMPLE_COLORS['classify_color']('Bone',{'vendor':'Cottoceramix','series':'Malaga','is_tile':True})
        self.assertEqual(result['confidence'],'OWNER_CONFIRMED')

    def test_latest_owner_rule_overrides_only_exact_malaga_bone(self):
        source=doc(vendor='Cottoceramix',series='Malaga')
        self.assertEqual(enrich(self.old,[source])[0]['f_kleur'],['Wit'])
        self.assertEqual(enrich(self.new,[source])[0]['f_kleur'],['Beige'])
        pearl=doc('Pearl','Cottoceramix','Souk')
        self.assertEqual(enrich(self.old,[pearl]),enrich(self.new,[pearl]))

    def test_non_tile_and_compound_colors_unchanged(self):
        for handles in ([],['wastafelkranen'],['cottoceramix'],['tegels-extra']):
            source=doc(handles=handles);self.assertEqual(enrich(self.old,[source]),enrich(self.new,[source]))
        for vendor,series in [('Porcelanosa','Fixture'),('Cottoceramix','Malaga'),('Cottoceramix','Arka')]:
            for raw in ('Bone acero','Bone-acero','Bone/White','Bone/Black','Bone New','White Bone'):
                source=doc(raw,vendor,series);self.assertEqual(enrich(self.old,[source]),enrich(self.new,[source]))

    def test_missing_series_still_allows_exact_tile_owner_rule(self):
        source=doc(series=None);after=enrich(self.new,[source])[0]
        self.assertEqual(after['f_kleur'],['Beige']);self.assertEqual(after['f_kleur_exact'],'Bone')

    def test_prior_cotto_rules_and_acero_unchanged(self):
        sources=[doc('Ash','Cottoceramix','Casablanca'),doc('Micro Chip','Cottoceramix','Waves'),
                 doc('Acero','Porcelanosa','Bottega'),doc('Acero','Cottoceramix','Malaga')]
        self.assertEqual(enrich(self.old,sources),enrich(self.new,sources))
        self.assertEqual(self.old._BC_SIMPLE_COLORS['COTTO_VISUAL_SCOPED_RULES'],
                         self.new._BC_SIMPLE_COLORS['COTTO_VISUAL_SCOPED_RULES'])

    def test_all_other_fields_sizes_and_codes_unchanged(self):
        sources=[dict(doc(),id='a'),dict(doc(),id='b',f_tegel_lengte_mm=1196),dict(doc(),id='c',f_tegel_lengte_mm=1500)]
        before,after=enrich(self.old,sources),enrich(self.new,sources)
        for a,b in zip(before,after):self.assertEqual({k:v for k,v in a.items() if k!='f_kleur'},{k:v for k,v in b.items() if k!='f_kleur'})
        self.assertEqual(self.old._bc_simple_tile_code_map(before),self.new._bc_simple_tile_code_map(after))

    def test_flags_count_and_wrong_color_rejected(self):
        docs=enrich(self.new,[doc()]);snapshot={};self.new._bc_simple_snapshot(snapshot,docs)
        for flag in ('filter_simplification_v1','tile_format_codes_v1','acero_gray_v1','cotto_visual_colors_v1','tile_bone_beige_v1'):
            self.assertIs(snapshot[flag],True)
        self.assertEqual(snapshot['tile_bone_beige_products'],1)
        docs[0]['f_kleur']=['Wit'];self.assertFalse(self.new._bc_bone_check(docs))
        with self.assertRaises(RuntimeError):self.new._bc_simple_snapshot({},docs)

    def test_idempotence_and_hash_drift_guards(self):
        self.assertEqual(PATCH._sha(self.target),PATCH.PATCHED_WORKER_SHA256)
        self.assertEqual(PATCH.patch_bone_worker(self.target),self.target)
        for source in (self.source+'\n',self.target+'\n'):
            with self.assertRaises(RuntimeError):PATCH.patch_bone_worker(source)

    def test_other_functions_ast_unchanged(self):
        def functions(source):
            return [ast.dump(n,include_attributes=False) for n in ast.parse(source).body
                    if isinstance(n,ast.FunctionDef) and n.name not in ('_bc_simple_snapshot','check_b2c_profiles')
                    and not n.name.startswith('_bc_bone_')]
        self.assertEqual(functions(self.source),functions(self.target))

    @unittest.skipUnless(API.is_file(),'private API source not provided')
    def test_api_byte_identical(self):
        source=API.read_bytes();self.assertEqual(self.new.patch_api(source.decode()).encode(),source)

    @unittest.skipUnless(CATALOG.is_file() and ORIGINAL.is_file(),'private catalog/original worker not provided')
    def test_full_catalog_54_upgrade_changes_407_combined_changes(self):
        rows=json.loads(CATALOG.read_text())['rows'];docs=[]
        for row in rows:
            item=doc(row.get('resolved_color') or '',row['vendor'],(row.get('series') or {}).get('value') or '')
            item.update(id=row['id'],title=row['title'])
            for key,field in [('width','f_tegel_breedte_mm'),('length','f_tegel_lengte_mm')]:
                value=(row.get(key) or {}).get('value')
                if value:item[field]=float(value)
                else:item.pop(field,None)
            docs.append(item)
        before,after=enrich(self.old,docs),enrich(self.new,docs);original=enrich(load(ORIGINAL.read_text()),docs)
        changes=[(a,b) for a,b in zip(before,after) if a!=b]
        self.assertEqual(len(changes),54);self.assertEqual(sum(a!=b for a,b in zip(original,after)),407)
        self.assertEqual(len(self.new._bc_bone_targets(after)),65)
        self.assertTrue(self.new._bc_bone_check(after));self.assertTrue(self.new._bc_acero_check(after));self.assertTrue(self.new._bc_cotto_check(after))
        for a,b in zip(before,after):
            self.assertEqual({k:v for k,v in a.items() if k!='f_kleur'},{k:v for k,v in b.items() if k!='f_kleur'})
            if a!=b:self.assertEqual(a['f_kleur_exact'],'Bone');self.assertEqual(b['f_kleur'],['Beige'])
        self.assertEqual(sum('f_kleur' not in d for d in before),sum('f_kleur' not in d for d in after))
        self.assertEqual(self.old._bc_simple_tile_code_map(before),self.new._bc_simple_tile_code_map(after))
        self.assertEqual(len(self.new._bc_simple_tile_code_map(after)),132)


if __name__=='__main__':unittest.main()
