import copy
import os
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import types
import unittest

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get('BC_FILTER_RUNTIME_DIR', '/not-configured')) / 'sync.py'
sys.path.insert(0, str(ROOT))
from simple_worker_patch import patch_simple_worker

def load():
    value = patch_simple_worker(BASE.read_text())
    module = types.ModuleType('_bc_simple_worker_test')
    module.__file__ = str(ROOT/'candidate-sync.py')
    sys.modules[module.__name__] = module
    exec(compile(value, module.__file__, 'exec'), module.__dict__)
    return module

def definitions():
    fields = {}
    for path in (Path(os.environ.get('BC_FILTER_PROFILE_DIR', '/not-configured'))).glob('*.json'):
        data = json.loads(path.read_text()).get('data', {})
        for value in data.get('filters', []):
            d = {k:copy.deepcopy(v) for k,v in value.items() if k in {'field','key','label','data_type','type','unit'}}
            d['type'] = 'range' if value['type'].startswith('number_') else 'choice'
            fields[value['field']] = d
    return list(fields.values())

@unittest.skipUnless(BASE.is_file(), 'private runtime source is not bundled')
class SimpleWorkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load()

    def test_source_guards_and_idempotence(self):
        base = BASE.read_text()
        result = patch_simple_worker(base)
        self.assertEqual(patch_simple_worker(result), result)
        for value in (base+'\n# change', result+'\n# changed reviewed code'):
            with self.assertRaises(RuntimeError): patch_simple_worker(value)

    def test_schema_only_new_index_fields(self):
        original = {'name':'stage_only','fields':[{'name':'f_kleur','type':'string','facet':True,'optional':True},{'name':'price_cents','type':'int64'}]}
        result = self.m._bc_simple_schema(original)
        fields = {f['name']:f for f in result['fields']}
        self.assertEqual(original['fields'][0]['type'], 'string')
        self.assertEqual(fields['f_kleur']['type'], 'string[]')
        self.assertEqual(fields['price_cents'], original['fields'][1])
        self.assertTrue(fields['f_tegel_formaat']['facet'])
        with self.assertRaises(RuntimeError): self.m._bc_simple_schema({'fields':[]})

    def test_actual_pair_only_and_special_exact(self):
        tile = {'f_tegel_breedte_mm':596,'f_tegel_lengte_mm':596,'title':'Matte wandtegel'}
        self.assertEqual(self.m._bc_simple_tile_label(tile), '60 × 60 cm')
        self.assertEqual(tile['f_tegel_breedte_mm'], 596)
        self.assertEqual(self.m._bc_simple_tile_label({**tile,'f_tegel_lengte_mm':1196}), '60 × 120 cm')
        self.assertEqual(self.m._bc_simple_tile_label({**tile,'title':'Mozaïek mat'}), '59,6 × 59,6 cm')
        self.assertEqual(self.m._bc_simple_tile_label({**tile,'f_tegel_breedte_mm':75,'f_tegel_lengte_mm':300}), '7,5 × 30 cm')
        self.assertIsNone(self.m._bc_simple_tile_label({'f_breedte_mm':596,'f_lengte_mm':596}))
        self.assertIsNone(self.m._bc_simple_tile_label({**tile,'f_tegel_breedte_mm':True}))

    def test_array_selection_unique_union_and_legacy(self):
        docs = [dict(id='1',f_kleur=['Wit','Beige'],collection_handles=['tegels'],general_shopping=True,sku_exact='a'),dict(id='2',f_kleur=['Beige'],collection_handles=['tegels'],general_shopping=True,sku_exact='b'),dict(id='3',f_kleur=['Zilver'],collection_handles=['kranen'],general_shopping=True,sku_exact='c')]
        snap = {'profiles':{'__all__':{'service_category':False}},'exact':[], 'filter_color_aliases':{'Geborsteld RVS':'Zilver','RVS':'Zilver'}}
        self.assertEqual([d['id'] for d in self.m.selected(docs,snap,{'filters':{'f_kleur':['Wit','Beige']}})], ['1','2'])
        self.assertEqual([d['id'] for d in self.m.selected(docs,snap,{'filters':{'f_kleur':['RVS']}})], ['3'])
        self.assertEqual(self.m.distinct_values([['Beige','Wit'],['Beige']]), ['Beige','Wit'])

    def test_producttype_aliases_do_not_change_raw_values(self):
        self.assertEqual(self.m.TYPE_LABELS.get('Wastafelonderkast'), 'Onderkast')
        self.assertEqual(self.m.TYPE_LABELS.get('Inbouwwastafelkraan'), 'Inbouw wastafelkraan')
        self.assertEqual(self.m.TYPE_LABELS.get('Speciale uitvoering'), None)

    def test_material_and_placement_groups_keep_technical_subtypes(self):
        values = ['RVS','Roestvrij staal','Stainless steel','RVS 316','Solid surface','Solid Surface']
        source = list(values)
        ui = self.m.filter_ui('f_materiaal',{'type':'choice','data_type':'string'},'general',values,'more',False)
        groups = {v['label']:v['exact_values'] for v in ui['option_groups']}
        self.assertEqual(set(groups['RVS']),{'RVS','Roestvrij staal','Stainless steel'})
        self.assertEqual(groups['RVS 316'],['RVS 316'])
        self.assertEqual(set(groups['Solid surface']),{'Solid surface','Solid Surface'})
        self.assertEqual(values,source)
        ui = self.m.filter_ui('f_kraanmontage',{'type':'choice','data_type':'string'},'general',['inbouw','Inbouw','Opbouw'],'primary',True)
        self.assertCountEqual(next(g['exact_values'] for g in ui['option_groups'] if g['label']=='Inbouw'),['inbouw','Inbouw'])

    def test_composed_api_planner_uses_real_worker_snapshot(self):
        sys.path.insert(0,str(ROOT.parent))
        from simple_api_patch import patch_simple_api
        import ast
        from types import SimpleNamespace
        class HttpError(Exception):
            pass
        class Body(SimpleNamespace):
            def copy(self,update): return Body(**{**vars(self),**update})
        docs = [dict(id='1',f_kleur=['Wit','Beige'],f_kleur_exact='Everest',vendor='Cottoceramix',f_serie='Himalayas',collection_handles=['tegels'],general_shopping=True,sku_exact='a',f_tegel_formaat='60 × 60 cm'),dict(id='2',f_kleur=['Zilver'],f_kleur_exact='Geborsteld RVS PVD',collection_handles=['kranen'],general_shopping=True,sku_exact='b')]
        defs = [{'field':'f_kleur','type':'choice','data_type':'string'},{'field':'f_tegel_formaat','type':'choice','data_type':'string'}]
        snapshot = {'profiles':{'__all__':{'allowed_filters':defs,'filters':defs,'service_category':False}},'exact':[],'collection':'stage_only','variant_aliases_v1':True}
        self.m._bc_simple_snapshot(snapshot,docs)
        source = patch_simple_api((Path(os.environ.get('BC_FILTER_RUNTIME_DIR', '/not-configured'))/'app.py').read_text())
        tree = ast.parse(source)
        functions = [n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'quote','plan','_bc_simple_request','_bc_simple_facet_limit'}]
        ns = {'_bc_snapshot':lambda:snapshot,'HTTPException':HttpError}
        exec(compile(ast.Module(body=functions,type_ignores=[]),'<composed-planner>', 'exec'),ns)
        request = Body(collection='__all__',filters={'f_kleur':['Everest','Beige'],'f_tegel_formaat':['60 × 60 cm']},ranges={},q='*',sort='relevance',page=1,per_page=24,include_facets=True)
        plan = ns['plan'](request)
        self.assertIn('f_kleur:=[`Wit`,`Beige`]',plan[2][0]['filter_by'])
        self.assertIn('f_tegel_formaat:=`60 × 60 cm`',plan[2][0]['filter_by'])
        self.assertEqual([d['id'] for d in self.m.selected(docs,snapshot,vars(request))],['1'])
        request.filters = {'f_kleur':['RVS']}
        self.assertIn('f_kleur:=`Zilver`',ns['plan'](request)[2][0]['filter_by'])
        self.assertEqual([d['id'] for d in self.m.selected(docs,snapshot,vars(request))],['2'])

    def test_real_catalog_preparation_and_profile_guards(self):
        rows = json.loads((Path(os.environ.get('BC_FILTER_TILE_CATALOG', '/not-configured'))).read_text())['rows']
        docs = []
        for row in rows:
            doc = {'id':row['id'].rsplit('/',1)[-1], 'sku':'fixture', 'sku_exact':'fixture', 'sku_aliases':['fixture'], 'price_varies':False,
                   'title':row['title'],'vendor':row['vendor'],'product_type':'Tegel','f_productsoort':'Tegel', 'price_cents':0,
                   'general_shopping':True,'collection_handles':['tegels']}
            for source,target in [('width','f_tegel_breedte_mm'),('length','f_tegel_lengte_mm')]:
                if row.get(source) and row[source].get('value'):
                    doc[target] = float(row[source]['value'])
            if row.get('resolved_color'): doc['f_kleur'] = row['resolved_color']
            if row.get('series') and row['series'].get('value'):doc['f_serie'] = row['series']['value']
            docs.append(doc)
        original = copy.deepcopy(docs)
        defs = self.m._bc_simple_definitions(definitions())
        schema = {'fields':[{'name':d['field']} for d in defs]}
        stats = self.m.enrich_b2c_documents(docs,defs,schema)
        self.assertEqual(len(docs),3496)
        self.assertEqual(sum('f_tegel_formaat' in d for d in docs),3490)
        self.assertEqual(len({d['f_tegel_formaat'] for d in docs if 'f_tegel_formaat' in d}),132)
        for before,after in zip(original,docs):
            for field in ('id','title','vendor','price_cents','f_tegel_breedte_mm','f_tegel_lengte_mm'):
                self.assertEqual(before.get(field),after.get(field))
            if before.get('f_kleur'):self.assertEqual(before['f_kleur'],after['f_kleur_exact'])
        cats = {'fixture':{'handle':'tegels','title':'Tegels'}}
        profiles = self.m.make_profiles(docs,cats,{},defs)
        snapshot = {'profiles':profiles,'exact':['fixture']}
        self.m._bc_simple_snapshot(snapshot,docs)
        checks = self.m.check_b2c_profiles(docs,snapshot)
        self.assertTrue(all(c['passed'] for c in checks),checks)
        fields = [f['field'] for f in profiles['tegels']['filters']]
        self.assertEqual(fields[0],'f_tegel_formaat')
        self.assertEqual(next(f for f in profiles['tegels']['filters'] if f['field']=='f_tegel_breedte_mm')['ui']['section'],'more')
        self.assertLessEqual(max(f['coverage_pct'] for p in profiles.values() for f in p['filters']),100)
        self.assertLessEqual(len(snapshot['simple_color_counts']),19)
        cases,facets = self.m.make_cases(docs,snapshot)
        count_case = next(c for c in facets if c['field']=='f_tegel_formaat')
        self.assertEqual(sum(count_case['expected_counts'].values()),3490)
        summary = {'published_tiles':len(docs),'tile_formats':len(snapshot['simple_tile_counts']),
                   'color_groups':len(snapshot['simple_color_counts']),'missing_color':sum('f_kleur' not in d for d in docs),
                   'stats':stats,'checks':checks,'case_count':len(cases),'facet_case_count':len(facets)}
        (ROOT/'worker-validation.json').write_text(json.dumps(summary,indent=2))

if __name__ == '__main__':
    unittest.main()
