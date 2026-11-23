"""Tile-color scopes and finite source-empty recovery invariants.

Private runtime/catalog/live-variant fixtures are optional and never published.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import types
import unittest

FOLDER = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('more_template_tested', FOLDER / 'more_worker_patch_template.py')
TEMPLATE = importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(TEMPLATE)
PATCH_SPEC = importlib.util.spec_from_file_location('more_frozen_patch_tested', FOLDER / 'apply_more_worker_patch.py')
PATCH = importlib.util.module_from_spec(PATCH_SPEC);PATCH_SPEC.loader.exec_module(PATCH)
WORKER = Path(os.environ.get('BC_MORE_WORKER_SOURCE', FOLDER / 'private-current-sync.py'))
API = Path(os.environ.get('BC_MORE_API_SOURCE', FOLDER / 'private-current-app.py'))
CATALOG = Path(os.environ.get('BC_MORE_TILE_CATALOG', FOLDER / 'private-tile-catalog.json'))
VARIANTS = Path(os.environ.get('BC_MORE_VARIANT_METADATA', FOLDER / 'private-variant-metadata.json'))


def load(source):
    module=types.ModuleType('more_worker_test');module.__file__=str(FOLDER/'private-candidate-sync.py')
    exec(compile(source,module.__file__,'exec'),module.__dict__);return module


def enrich(module,source):
    result=copy.deepcopy(source);module.enrich_b2c_documents(result,[],{'fields':[]});return result


def fixture_doc():
    rule=PATCH.FALLBACK_RULES[0]
    return {'id':'fixture','title':'Fixture title','handle':rule['handle'],'vendor':'Cottoceramix',
            'f_serie':'Fixture','collection_handles':['tegels'],'general_shopping':True,
            'sku_exact':rule['sku'].casefold(),'sku_aliases':[rule['sku'].casefold()],
            'price_varies':False,'f_kleur':None,'f_tegel_breedte_mm':596,
            'f_tegel_lengte_mm':596,'price_cents':12345,'image_url':'https://example.test/tile.jpg'}


def fixture_documents():
    metadata={r['handle']:r for r in json.loads(VARIANTS.read_text())['rows']}
    docs=[]
    for row in json.loads(CATALOG.read_text())['rows']:
        item={'id':row['id'],'title':row['title'],'handle':row['handle'],'vendor':row['vendor'],
              'f_serie':(row.get('series') or {}).get('value') or '',
              'collection_handles':['tegels'],'general_shopping':True,'sku_exact':'unrelated-fixture',
              'sku_aliases':['unrelated-fixture'],'price_varies':False,
              'f_kleur':row.get('resolved_color') or None,'price_cents':12345,
              'image_url':'https://example.test/unchanged.jpg'}
        live=metadata.get(row['handle'])
        if live:
            if live['title']!=row['title']:raise RuntimeError('Private fixture title differs from fresh metadata')
            variants=live['variants']['nodes']
            if len(variants)!=1 or live['variants']['pageInfo']['hasNextPage']:raise RuntimeError('Fixture variants are not the reviewed single SKU')
            item['sku_exact']=variants[0]['sku'].casefold();item['sku_aliases']=[variants[0]['sku'].casefold()]
            item['image_url']=((live.get('featuredMedia') or {}).get('image') or {}).get('url') or ''
        for key,field in [('width','f_tegel_breedte_mm'),('length','f_tegel_lengte_mm')]:
            value=(row.get(key) or {}).get('value')
            if value:item[field]=float(value)
        docs.append(item)
    return docs


class SourceAndDataGuards(unittest.TestCase):
    def namespace(self):
        return {'normalize':lambda v:str(v).strip().casefold(),
                'normalize_series':lambda v:str(v).strip().casefold().replace('-r',''),
                'TAXONOMY':('Wit','Grijs','Beige','Bruin','Blauw','Groen','Multicolor'),
                'classify_color':lambda raw,ctx:{'colors':[],'confidence':'UNRESOLVED'}}

    def test_unreviewed_source_rejected(self):
        for source in (None,b'worker','',TEMPLATE.MARKER,'print(1)'):
            with self.assertRaises(RuntimeError):TEMPLATE.patch_more_worker(source)

    def test_normalization_conflicts_rejected(self):
        first={'vendor':'Cottoceramix','series':'Fixture','exact_color':'Cloud','colors':['Wit'],'confidence':.9}
        second=dict(first,series='Fixture-R',colors=['Grijs'])
        with self.assertRaises(RuntimeError):TEMPLATE.reviewed_scoped_rules([first,second],self.namespace())

    def test_visual_rules_cannot_override_confirmed_prior_rule(self):
        ns=self.namespace();ns['classify_color']=lambda raw,ctx:{'colors':['Beige'],'confidence':'OWNER_CONFIRMED'}
        rule={'vendor':'Porcelanosa','series':'Fixture','exact_color':'Bone','colors':['Wit'],'confidence':.9}
        with self.assertRaises(RuntimeError):TEMPLATE.reviewed_scoped_rules([rule],ns)

    def test_invalid_scope_confidence_and_base_colors_rejected(self):
        rule={'vendor':'Cottoceramix','series':'Fixture','exact_color':'Cloud','colors':['Wit'],'confidence':.9}
        for value in (None,True,.69,1.1,float('nan'),'0.9'):
            with self.assertRaises(RuntimeError):TEMPLATE.reviewed_scoped_rules([dict(rule,confidence=value)],self.namespace())
        with self.assertRaises(RuntimeError):TEMPLATE.reviewed_scoped_rules([dict(rule,colors=['Overige kleuren'])],self.namespace())

    def test_fallback_requires_known_provenance_hash_and_vendor(self):
        rule=dict(PATCH.FALLBACK_RULES[0]);rule['colors']=['Wit']
        for invalid in (dict(rule,provenance='GUESSED'),dict(rule,title_sha256='bad'),dict(rule,vendor='Other'),dict(rule,sku='')):
            with self.assertRaises(RuntimeError):TEMPLATE.reviewed_fallback_rules([invalid],self.namespace())

    def test_conflicting_same_handle_recovery_rejected(self):
        first=dict(PATCH.FALLBACK_RULES[0],colors=['Wit']);second=dict(first,colors=['Grijs'])
        with self.assertRaises(RuntimeError):TEMPLATE.reviewed_fallback_rules([first,second],self.namespace())


@unittest.skipUnless(WORKER.is_file(),'private a8dd worker source not provided')
class WorkerIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=WORKER.read_text();cls.target=PATCH.patch_more_worker(cls.source)
        cls.old,cls.new=load(cls.source),load(cls.target)

    def setUp(self):
        # Synthetic identity/provenance tests must not alter another test's rules.
        self.old,self.new=load(self.source),load(self.target)

    def matching_doc(self):
        source=fixture_doc();rule=copy.deepcopy(self.new._BC_MORE_COLOR_FALLBACKS[source['handle']])
        # Synthetic identity remains local; the production rules themselves stay unchanged.
        rule['title_sha256']=hashlib.sha256(source['title'].encode()).hexdigest()
        self.new._BC_MORE_COLOR_FALLBACKS[source['handle']]=rule
        return source,rule

    def test_scoped_vendor_series_tile_and_raw_match_only(self):
        for vendor in ('Cottoceramix','Porcelanosa'):
            rule=next(r for r in PATCH.SCOPED_RULES if r['vendor']==vendor)
            doc=fixture_doc();doc.update(vendor=vendor,f_serie=rule['series'],f_kleur=rule['exact_color'],handle='unrelated')
            expected=[c for c in self.new._BC_SIMPLE_COLORS['TAXONOMY'] if c in rule['colors']]
            result=enrich(self.new,[doc])[0];self.assertEqual(result['f_kleur'],expected);self.assertEqual(result['f_kleur_exact'],rule['exact_color'])
            for change in ({'vendor':'Other'},{'f_serie':'Other'},{'f_serie':None},{'f_kleur':rule['exact_color']+' new'},{'collection_handles':['cottoceramix']}):
                altered={**doc,**change};self.assertEqual(enrich(self.old,[altered]),enrich(self.new,[altered]))

    def test_missing_color_recovery_keeps_blank_source_and_provenance(self):
        source,rule=self.matching_doc();result=enrich(self.new,[source])[0]
        self.assertEqual(result['f_kleur'],rule['colors']);self.assertEqual(result['f_kleur_exact'],'')
        self.assertIsNone(source['f_kleur']);self.assertNotIn('f_kleur_exact',source)
        snapshot={};self.new._bc_simple_snapshot(snapshot,[result])
        self.assertIs(snapshot['more_tile_colors_v1'],True);self.assertEqual(snapshot['more_missing_color_products'],1)
        record=snapshot['more_missing_color_provenance'][result['id']]
        self.assertEqual(record['provenance'],rule['provenance']);self.assertIs(record['source_color_missing'],True)
        self.assertNotIn('',snapshot['filter_color_aliases'])

    def test_current_nonempty_source_including_other_is_never_overwritten(self):
        source,rule=self.matching_doc()
        for raw in ('Blauw','Opaque new color','Overige kleuren'):
            altered=dict(source,f_kleur=raw);self.assertEqual(enrich(self.old,[altered]),enrich(self.new,[altered]));self.assertEqual(self.new._BC_MORE_COLOR_RECOVERED,{})
        altered=dict(source,f_kleur_exact='Original manufacturer name')
        self.assertEqual(enrich(self.old,[altered]),enrich(self.new,[altered]));self.assertEqual(self.new._BC_MORE_COLOR_RECOVERED,{})

    def test_nonempty_color_created_by_prior_layer_is_preserved(self):
        source,rule=self.matching_doc();previous=self.new._bc_more_original_enrich
        def prior_color(docs,definitions,schema):
            stats=previous(docs,definitions,schema);docs[0]['f_kleur']=['Wit'];docs[0]['f_kleur_exact']='';return stats
        try:
            self.new._bc_more_original_enrich=prior_color;result=enrich(self.new,[source])[0]
            self.assertEqual(result['f_kleur'],['Wit']);self.assertEqual(self.new._BC_MORE_COLOR_RECOVERED,{})
        finally:self.new._bc_more_original_enrich=previous

    def test_stale_title_handle_vendor_tile_or_sku_skips_recovery(self):
        source,rule=self.matching_doc()
        cases=[{'title':source['title']+' changed'},{'handle':'unknown-handle'},{'vendor':'Porcelanosa'},
               {'collection_handles':['wastafelkranen']},{'sku_exact':'wrong','sku_aliases':['wrong']}]
        for change in cases:
            altered={**source,**change};self.assertEqual(enrich(self.old,[altered]),enrich(self.new,[altered]));self.assertEqual(self.new._BC_MORE_COLOR_RECOVERED,{})

    def test_new_multi_sku_or_varying_price_family_skips_recovery(self):
        source,rule=self.matching_doc()
        for change in ({'sku_aliases':[rule['sku'],'other-variant']},{'price_varies':True},{'sku_aliases':[None]},{'sku_aliases':'wrong-type'}):
            altered={**source,**change};self.assertEqual(enrich(self.old,[altered]),enrich(self.new,[altered]));self.assertEqual(self.new._BC_MORE_COLOR_RECOVERED,{})

    def test_casefolded_actual_sku_and_missing_alias_fallback_work(self):
        source,rule=self.matching_doc()
        for change in ({'sku_aliases':[rule['sku'].swapcase()]},{'sku_aliases':None},{'sku_aliases':[]}):
            result=enrich(self.new,[{**source,**change}])[0];self.assertEqual(result['f_kleur'],rule['colors']);self.assertEqual(result['f_kleur_exact'],'')

    def test_recovery_registry_is_reset_for_each_generation(self):
        source,rule=self.matching_doc();enrich(self.new,[source]);self.assertEqual(len(self.new._BC_MORE_COLOR_RECOVERED),1)
        enrich(self.new,[dict(source,title='changed')]);self.assertEqual(self.new._BC_MORE_COLOR_RECOVERED,{})

    def test_prior_owner_bone_acero_and_cotto_rules_unchanged(self):
        docs=[]
        for i,(vendor,series,raw) in enumerate([('Porcelanosa','Bottega','Acero'),('Cottoceramix','Malaga','Bone'),('Cottoceramix','Waves','Micro Chip')]):
            d=fixture_doc();d.update(id=str(i),vendor=vendor,f_serie=series,f_kleur=raw,handle='unrelated');docs.append(d)
        self.assertEqual(enrich(self.old,docs),enrich(self.new,docs))
        self.assertEqual(self.old._BC_SIMPLE_COLORS['COTTO_VISUAL_SCOPED_RULES'],self.new._BC_SIMPLE_COLORS['COTTO_VISUAL_SCOPED_RULES'])

    def test_scoped_rules_do_not_spread_into_unapproved_compound_components(self):
        rule=PATCH.SCOPED_RULES[0];d=fixture_doc();d.update(vendor=rule['vendor'],f_serie=rule['series'],f_kleur=rule['exact_color']+'/White',handle='unrelated')
        self.assertEqual(enrich(self.old,[d]),enrich(self.new,[d]))

    def test_wrong_recovered_color_or_raw_source_rejected(self):
        source,rule=self.matching_doc();docs=enrich(self.new,[source]);docs[0]['f_kleur']=['Overige kleuren']
        self.assertFalse(self.new._bc_more_recovery_check(docs))
        with self.assertRaises(RuntimeError):self.new._bc_simple_snapshot({},docs)
        docs=enrich(self.new,[source]);docs[0]['f_kleur_exact']='Invented manufacturer color';self.assertFalse(self.new._bc_more_recovery_check(docs))

    def test_idempotence_hashes_and_drift_guards(self):
        self.assertEqual(PATCH._sha(self.target),PATCH.PATCHED_WORKER_SHA256);self.assertEqual(PATCH.patch_more_worker(self.target),self.target)
        for source in (self.source+'\n',self.target+'\n'):
            with self.assertRaises(RuntimeError):PATCH.patch_more_worker(source)

    def test_other_functions_ast_unchanged(self):
        def functions(source):
            return [ast.dump(n,include_attributes=False) for n in ast.parse(source).body
                    if isinstance(n,ast.FunctionDef) and n.name not in ('enrich_b2c_documents','_bc_simple_snapshot','check_b2c_profiles')
                    and not n.name.startswith('_bc_more_')]
        self.assertEqual(functions(self.source),functions(self.target))

    @unittest.skipUnless(API.is_file(),'private API source not provided')
    def test_api_byte_identical(self):
        source=API.read_bytes();self.assertEqual(self.new.patch_api(source.decode()).encode(),source)

    @unittest.skipUnless(CATALOG.is_file() and VARIANTS.is_file(),'private catalog/live variant metadata not provided')
    def test_full_catalog_573_products_only_and_exact_provenance(self):
        docs=fixture_documents();before=enrich(self.old,docs);after=enrich(self.new,docs)
        recovered=set(self.new._BC_MORE_COLOR_RECOVERED);changed=[(a,b) for a,b in zip(before,after) if a!=b]
        self.assertEqual(len(changed),573);self.assertEqual(len(recovered),418);self.assertEqual(len(self.new._bc_more_scoped_targets(after)),155)
        self.assertEqual(sum(d.get('f_kleur')==['Overige kleuren'] for d in before),155)
        self.assertEqual(sum(d.get('f_kleur')==['Overige kleuren'] for d in after),0)
        self.assertEqual(sum('f_kleur' not in d for d in before),561);self.assertEqual(sum('f_kleur' not in d for d in after),143)
        for a,b in zip(before,after):
            exclude={'f_kleur','f_kleur_exact'} if b['id'] in recovered else {'f_kleur'}
            self.assertEqual({k:v for k,v in a.items() if k not in exclude},{k:v for k,v in b.items() if k not in exclude})
            if b['id'] in recovered:self.assertNotIn('f_kleur_exact',a);self.assertEqual(b['f_kleur_exact'],'')
        self.assertEqual(len(self.new._bc_bone_targets(after)),65);self.assertTrue(self.new._bc_bone_check(after));self.assertTrue(self.new._bc_acero_check(after));self.assertTrue(self.new._bc_cotto_check(after))
        self.assertEqual(self.old._bc_simple_tile_code_map(before),self.new._bc_simple_tile_code_map(after));self.assertEqual(len(self.new._bc_simple_tile_code_map(after)),132)
        snapshot={};self.new._bc_simple_snapshot(snapshot,after)
        self.assertEqual(snapshot['more_missing_color_counts'],{'OFFICIAL_COTTO_BMN':353,'TITLE_EXPLICIT_COLOR':65})
        self.assertEqual(snapshot['more_missing_color_products'],418);self.assertNotIn('',snapshot['filter_color_aliases'])


if __name__=='__main__':unittest.main()
