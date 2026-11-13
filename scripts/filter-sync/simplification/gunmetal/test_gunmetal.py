"""Isolated classifier, worker-composition and release gate tests; no live writes."""
import ast
import collections
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import types
import unittest
from unittest.mock import patch

HERE=Path(__file__).resolve().parent
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result);return result
P=module('gunmetal_patch_tests',HERE/'gunmetal_worker_patch.py')
A=module('gunmetal_apply_tests',HERE/'apply_gunmetal_filter.py')

def original_colors():
    source=(HERE.parent/'simple_worker_patch.py').read_text()
    tree=ast.parse(source)
    color_source=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(getattr(t,'id','')=='COLOR_SOURCE' for t in n.targets))
    ns={'__name__':'test_color_rules'};exec(compile(color_source,'<existing-public-color-rules>','exec'),ns);return ns

class Colors(unittest.TestCase):
    def setUp(self):
        self.before=original_colors();self.after=original_colors();exec(P.COLOR_PATCH,self.after)
    def test_gunmetal_spellings_and_finishes(self):
        for raw in ['Gunmetal','Gun metal','Gun-metal','gun_metal','Geborsteld gunmetal PVD','Mat Gunmetal','Gunmetal black','Zwart gunmetal']:
            with self.subTest(raw=raw):self.assertEqual(self.after['classify_color'](raw)['colors'],['Gunmetal'])
    def test_gray_and_aged_iron_are_preserved(self):
        for raw in ['Grijs','Grey','Antraciet','Verouderd ijzer','Dark steel']:
            self.assertEqual(self.after['classify_color'](raw),self.before['classify_color'](raw))
    def test_multiple_colors_retained(self):
        for raw,expected in [('Gunmetal/chroom',['Gunmetal','Zilver']),('wit/gun metal',['Wit','Gunmetal']),('Gunmetal + grijs',['Gunmetal','Grijs'])]:
            self.assertEqual(self.after['classify_color'](raw)['colors'],expected)
    def test_unrelated_names_do_not_match(self):
        for raw in ['Gunmetallic','Shotgun metal','Metal','Mettal','']:
            self.assertEqual(self.after['classify_color'](raw),self.before['classify_color'](raw))
    def test_all_existing_rule_labels_keep_non_gunmetal_results(self):
        candidates=list(self.before['TAXONOMY'])+list(self.before['CONVENTIONAL'])+list(self.before['NO_COLOR'])
        for key,pattern in self.before['RULES']['patterns'].items():
            candidates.extend(pattern.split('(?:')[-1].split(')')[0].split('|'))
        count=0
        for raw in candidates:
            if self.after['_bc_gunmetal_pattern'].search(raw):continue
            for value in (raw,'Geborsteld '+raw,raw+'/chroom'):
                self.assertEqual(self.after['classify_color'](value),self.before['classify_color'](value),value);count+=1
        self.assertGreater(count,300)
    def test_taxonomy_order_and_document_source_preserved(self):
        self.assertEqual(tuple(v for v in self.after['TAXONOMY'] if v!='Gunmetal'),self.before['TAXONOMY'])
        doc={'f_kleur':'Geborsteld gunmetal PVD','vendor':'Hotbath','title':'keep title','price':14900};saved=copy.deepcopy(doc)
        self.assertEqual(self.after['normalize_document_colors'](doc),['Gunmetal']);self.assertEqual(doc,saved)

class Composition(unittest.TestCase):
    def setUp(self):
        self.source='import sys\n\ndef prepare():\n    schema = {}\n    for key in ("default_sorting_field", "metadata"):\n        schema.pop(key, None)\n    return schema\n\nvalue = 1\n\nif __name__ == "__main__":\n    print(value)\n'
        self.guard=patch.object(P,'BASE_WORKER_SHA256',hashlib.sha256(self.source.encode()).hexdigest());self.guard.start();self.addCleanup(self.guard.stop)
    def test_exact_insertion_and_reverse(self):
        result=P.patch_worker(self.source);self.assertEqual(P.original_source(result),self.source);self.assertEqual(P.patch_worker(result),result);compile(result,'<test>','exec')
    def test_unknown_base_stops(self):
        with self.assertRaises(RuntimeError):P.patch_worker(self.source+'# other change\n')
    def test_changed_patch_stops(self):
        result=P.patch_worker(self.source).replace('Gunmetal-selectie','Other-selectie')
        with self.assertRaises(RuntimeError):P.patch_worker(result)
    def test_later_human_change_is_preserved(self):
        result=P.patch_worker(self.source)+'# human change\n'
        with self.assertRaises(RuntimeError):P.patch_worker(result)

def snapshot():
    flags=('variant_aliases_v1','filter_simplification_v1','tile_format_codes_v1','acero_gray_v1','cotto_visual_colors_v1','tile_bone_beige_v1','more_tile_colors_v1','tile_looks_v1','gunmetal_v1','recommendations_v1','cinto_widths_v1')
    field={'field':'f_tegel_uitstraling','type':'choice','data_type':'string','ui':{'default_open':False,'control':'checkbox','section':'primary'}}
    return {**dict.fromkeys(flags,True),'recommendation_preview':{'__all__':['test-1']},'collection':'test_index','tile_look_source':'tiles.look','tile_look_taxonomy':['Steenlook','Marmerlook'],'tile_look_products':2,'tile_look_missing_products':0,'tile_look_counts':{'Steenlook':1,'Marmerlook':1},'gunmetal_products':1,'gunmetal_scope_counts':{'__all__':1,'badgrepen':1},'simple_color_counts':{'Gunmetal':1,'Grijs':2},'filter_color_aliases':{'Gunmetal':'Gunmetal','Grijs':'Grijs','Geborsteld gunmetal PVD':'Gunmetal'},'profiles':{key:{'shopping_products':2,'filters':[field],'allowed_filters':[field],'b2c_policy':{'group':group,'tile_looks_v1':True}} for key,group in [('tegels','tile'),('cottoceramix','general')]}}

class ReleaseGates(unittest.TestCase):
    def setUp(self):
        self.lifecycle,_=A.dependencies()
        fake_patch=types.SimpleNamespace(patch_worker=lambda s:s+'\n# candidate\n',BASE_WORKER_SHA256='base')
        A.configure(self.lifecycle,fake_patch,b'base worker')
    def test_valid_snapshot_and_existing_layers(self):
        self.assertTrue(self.lifecycle.validate_look_snapshot(snapshot()));self.assertIn('tile_looks_v1',self.lifecycle.PRIOR_FLAGS);self.assertIn('gunmetal_v1',self.lifecycle.REQUIRED_FLAGS)
    def test_each_existing_flag_required(self):
        for flag in self.lifecycle.REQUIRED_FLAGS:
            value=snapshot();value[flag]=False
            with self.subTest(flag=flag),self.assertRaises(RuntimeError):self.lifecycle.validate_look_snapshot(value)
    def test_old_gray_alias_rejected(self):
        value=snapshot();value['filter_color_aliases']['Geborsteld gunmetal PVD']='Grijs'
        with self.assertRaises(RuntimeError):self.lifecycle.validate_look_snapshot(value)
    def test_wrong_or_zero_counts_rejected(self):
        for key,value in [('gunmetal_products',0),('gunmetal_products',True),('gunmetal_scope_counts',{'__all__':2})]:
            s=snapshot();s[key]=value
            with self.subTest(key=key),self.assertRaises(RuntimeError):self.lifecycle.validate_look_snapshot(s)
    def test_look_contract_is_still_checked(self):
        value=snapshot();value['tile_look_source']='wrong'
        with self.assertRaises(RuntimeError):self.lifecycle.validate_look_snapshot(value)
    def test_no_api_mutation(self):
        self.assertEqual(self.lifecycle.BASE_API_SHA256,A.BASE_API_SHA256);self.assertEqual(self.lifecycle.TARGET_API_SHA256,A.BASE_API_SHA256)

class WorkerHooks(unittest.TestCase):
    def test_source_sets_aliases_profiles_and_or_cases(self):
        colors=original_colors()
        def prior_snapshot(s,docs):
            s['simple_color_counts']=dict(collections.Counter(c for d in docs if d['general_shopping'] for c in d['f_kleur']))
        ns={'_BC_SIMPLE_COLORS':colors,'collections':collections,'_bc_simple_strings':lambda v:[v] if isinstance(v,str) else (v or []),'_bc_simple_aliases':lambda docs:{'Grijs':'Grijs'},'make_profiles':lambda *a:{'badgrepen':{'b2c_policy':{'color_value_aliases':{}}}},'_bc_simple_snapshot':prior_snapshot,'check_b2c_profiles':lambda *a:[],'make_cases':lambda *a:([],[]),'_bc_simple_schema':lambda schema:copy.deepcopy(schema),'enrich_b2c_documents':lambda *args:{}}
        exec(P.insertion(),ns)
        docs=[{'id':'gm','f_kleur_exact':'Geborsteld gunmetal PVD','f_kleur':['Gunmetal'],'general_shopping':True,'collection_handles':['badgrepen']},{'id':'gray','f_kleur_exact':'Verouderd ijzer','f_kleur':['Grijs'],'general_shopping':True,'collection_handles':['badgrepen']},{'id':'private','f_kleur_exact':'Gunmetal','f_kleur':['Gunmetal'],'general_shopping':False,'collection_handles':['badgrepen']}]
        saved=copy.deepcopy(docs);ns['enrich_b2c_documents'](docs,{},{});s={'profiles':{'badgrepen':{}}};ns['_bc_simple_snapshot'](s,docs);self.assertEqual(s['gunmetal_products'],1);self.assertEqual([{k:v for k,v in doc.items() if k!='bc_recommendation_rank'} for doc in docs],saved)
        cases,_=ns['make_cases'](docs,s);self.assertEqual(cases[0]['expected_ids'],['gm']);self.assertEqual(cases[1]['expected_ids'],['gray']);self.assertEqual(set(cases[2]['expected_ids']),{'gm','gray'})
        self.assertEqual(ns['_bc_simple_aliases'](docs)['Gun metal'],'Gunmetal');self.assertEqual(ns['make_profiles'](docs,None,None,None)['badgrepen']['b2c_policy']['color_value_aliases']['Gunmetal'],'Gunmetal')
        docs[0]['f_kleur']=['Grijs']
        with self.assertRaises(RuntimeError):ns['_bc_simple_snapshot']({},docs)

class RecommendedOrder(unittest.TestCase):
    def setUp(self):
        self.ns={'collections':collections,'_bc_simple_strings':lambda v:[v] if isinstance(v,str) else (v or []),'_bc_simple_schema':lambda s:copy.deepcopy(s),'enrich_b2c_documents':lambda *a:{},'_bc_simple_snapshot':lambda *a:None}
        exec(P.RECOMMENDATION_HELPERS,self.ns)
    def doc(self,id,vendor='Hotbath',series='Cobber',image=True,extra=0):
        return {'id':str(id),'vendor':vendor,'f_productsoort':'Wastafelkraan','f_serie':series,'sku_exact':'SKU'+str(id),'image_url':'https://example.invalid/photo.jpg' if image else '', 'price_cents':14900,'general_shopping':True,'collection_handles':['wastafelkranen'],**{'f_test_'+str(i):'value' for i in range(extra)}}
    def test_series_and_brands_alternate_before_second_finish(self):
        docs=[self.doc(i) for i in range(20)]+[self.doc(30,'Wiesbaden','Caral'),self.doc(31,'Hotbath','Archie')]
        ordered=self.ns['_bc_rank_recommendations'](docs)
        self.assertEqual(len({self.ns['_bc_recommendation_group'](d) for d in ordered[:3]}),3)
    def test_richer_data_leads_within_group(self):
        docs=[self.doc('sparse'),self.doc('complete',extra=10)]
        self.assertEqual(self.ns['_bc_rank_recommendations'](docs)[0]['id'],'complete')
    def test_missing_image_follows_all_image_records(self):
        docs=[self.doc(i,image=False,extra=20) for i in range(10)]+[self.doc(20),self.doc(21)]
        ordered=self.ns['_bc_rank_recommendations'](docs)
        self.assertTrue(all(d['image_url'] for d in ordered[:2]));self.assertTrue(all(not d['image_url'] for d in ordered[2:]))
    def test_repeated_and_input_order_independent(self):
        docs=[self.doc(i,vendor='V'+str(i%4),extra=i%7) for i in range(70)]
        a=[d['id'] for d in self.ns['_bc_rank_recommendations'](copy.deepcopy(docs))]
        b=[d['id'] for d in self.ns['_bc_rank_recommendations'](list(reversed(copy.deepcopy(docs))))]
        self.assertEqual(a,b);self.assertEqual(set(a[:24])&set(a[24:48]),set());self.assertEqual(len(set(a)),70)
    def test_only_internal_rank_is_added(self):
        docs=[self.doc(i) for i in range(7)];saved=copy.deepcopy(docs);self.ns['_bc_rank_recommendations'](docs)
        self.assertEqual([{k:v for k,v in d.items() if k!='bc_recommendation_rank'} for d in docs],saved)
        self.assertEqual({d['bc_recommendation_rank'] for d in docs},set(range(1,8)))
    def test_duplicate_id_rejected(self):
        with self.assertRaises(RuntimeError):self.ns['_bc_rank_recommendations']([self.doc(1),self.doc(1)])
    def test_internal_schema_field_and_default_sort(self):
        old={'fields':[{'name':'id','type':'string'}]};schema=self.ns['_bc_simple_schema'](old);self.ns['_bc_recommendation_schema_default'](schema)
        self.assertEqual(schema['default_sorting_field'],'bc_recommendation_rank');self.assertEqual(old,{'fields':[{'name':'id','type':'string'}]})
        with self.assertRaises(RuntimeError):self.ns['_bc_simple_schema'](schema)
    def test_actual_two_mirror_widths_required(self):
        docs=[self.doc(1,'Wiesbaden','Cinto'),self.doc(2,'Wiesbaden','Cinto')]
        for d,sku,mm in zip(docs,['38.4177','38.4178'],[600,800]):d.update(sku_exact=sku,f_breedte_mm=mm,f_diameter_mm=mm)
        self.ns['_bc_rank_recommendations'](docs);s={};self.ns['_bc_simple_snapshot'](s,docs);self.assertTrue(s['cinto_widths_v1'])
        docs[0]['f_breedte_mm']=30;self.ns['_bc_simple_snapshot'](s,docs);self.assertFalse(s['cinto_widths_v1'])

if __name__=='__main__':unittest.main()
