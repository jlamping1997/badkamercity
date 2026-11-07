import unittest,json,copy
from pathlib import Path
from retail_extract import parse
from enrich_retail_specifications import normalized,applicable,collect
from preflight import check,REQUIRED

catalog=json.loads(Path('prepared/catalog.json').read_text());by={p['sku']:p for p in catalog};report=json.loads(Path('prepared/retail-enrichment-report.json').read_text());observations=json.loads(Path('prepared/retail-observations.json').read_text());ev=json.loads(Path('prepared/specification-evidence.json').read_text())
class RetailTests(unittest.TestCase):
 def test_exact_identity_rejects_wrong_ean_brand_and_requested_code(self):
  good=next(r for r in observations if r['sku']=='OK-JY100CH');p=by[good['sku']]
  for field,value in [('ean','0000000000000'),('brand','Fortifura'),('requested_sku','OK-JY80CH')]:
   r=copy.deepcopy(good);r[field]=value;facts,rejected,_=collect([p],[r],{});self.assertFalse(facts);self.assertEqual(len(rejected),1)
 def test_every_added_field_has_identity_and_observed_value(self):
  for x in report['changes']:
   if x['action']!='AANGEVULD':continue
   p=by[x['sku']];e=ev[x['sku']]['facts'][x['field']]
   self.assertEqual(p['specifications'][x['field']],x['new']);self.assertEqual(e['identity'],{'sku':p['sku'],'ean':p['ean'],'brand':'BRAUER'})
   self.assertTrue(any(r['sku']==p['sku'] and r['ean']==p['ean'] and r['brand']=='Brauer' and r['url']==e['url'] for r in observations))
 def test_units_and_synonyms_do_not_create_false_conflicts(self):
  self.assertEqual(normalized('Lengte','150 cm'),normalized('Lengte','1500 mm'))
  self.assertEqual(normalized('Uitvoering uitloop','Vaste uitloop'),normalized('Uitvoering uitloop','Vast'))
  self.assertEqual(normalized('Aantal grepen','Eengreeps'),normalized('Aantal grepen','1'))
  self.assertEqual(normalized('Wandafwerking','Met achterplaat'),normalized('Wandafwerking','Afdekplaat'))
 def test_set_dimensions_and_outlier_hose_are_not_applied(self):
  p=by['5-CE-403'];self.assertNotIn('Diameter',p['specifications']);self.assertNotIn('Lengte doucheslang',p['specifications'])
  self.assertEqual(p['specifications']['Diameter handdouche'],'2,4 cm')
  self.assertEqual(p['specifications']['Diameter hoofddouche'],'25 cm')
  self.assertFalse(applicable(by['5-CE-235'],{'label':'Hoogte','value':'4 cm'})[0]);self.assertNotIn('Hoogte',by['5-CE-235']['specifications'])
 def test_boolean_absence_is_not_false_and_section_is_scoped(self):
  page={'url':'https://www.badkamerxxl.nl/test','title':'Brauer test','ref':'fixture','lines':[{'line':i+1,'text':t} for i,t in enumerate(['Fabrikantnummer','5-CE-403','EAN','8720724565693','Merk','Brauer','Met verlichting','Handdouche','Breedte/diameter douchekop','2,4 cm','Hoofddouche','Breedte/diameter hoofddouche','25 cm','Bijlagen'])]}
  fields=parse(page)['fields'];self.assertNotIn('Verlichting',[f['label'] for f in fields]);self.assertIn('Diameter handdouche',[f['label'] for f in fields]);self.assertIn('Diameter hoofddouche',[f['label'] for f in fields])
 def test_html_child_labels_are_not_generic_field_values(self):
  page={'url':'https://www.sanitairwinkel.nl/test','title':'Brauer test','ref':'fixture','retrieval':'public_live_fetch_html','lines':[{'line':i+1,'text':t} for i,t in enumerate(['Leveranciernummer','5-CE-403','EAN','8720724565693','Merk','Brauer','Vorm handdouche','Staafmodel','Materiaal deur','Glas','Technische documenten'])]}
  fields=parse(page)['fields'];self.assertNotIn(('Vorm','handdouche'),[(f['label'],f['value']) for f in fields]);self.assertNotIn(('Materiaal','deur'),[(f['label'],f['value']) for f in fields])
 def test_conflicting_old_retail_fields_are_withheld(self):
  self.assertNotIn('Hoogte kraan',by['5-CE-003']['specifications']);self.assertNotIn('Lengte uitloop',by['5-CE-004']['specifications'])
  self.assertNotIn('Inbouwdiepte',by['5-CE-004-B4']['specifications']);self.assertNotIn('Lengte uitloop',by['5-CE-004-B4']['specifications'])
  # A new live refresh resolved the old 59/60 cached discrepancy: both current tables say 59.
  self.assertEqual(by['SK-IM60LCH']['specifications']['Breedte'],'59 cm');self.assertGreaterEqual(len(ev['SK-IM60LCH']['facts']['Breedte']['corroborating_urls']),2)
  self.assertEqual(by['SK-IM60LCH']['specifications']['Hoogte'],'70 cm')
 def test_drawing_resolution_and_no_sibling_inheritance(self):
  self.assertEqual(by['GS-GTC1H12090200CE']['specifications']['Glasdikte'],'8 mm')
  self.assertEqual(ev['GS-GTC1H12090200CE']['facts']['Glasdikte']['verification'],'LINKED_DRAWING_CHECKED')
  if 'Breedte' in by['OK-JY100DA']['specifications']:
   self.assertEqual(ev['OK-JY100DA']['facts']['Breedte']['identity']['sku'],'OK-JY100DA')
  else:self.assertNotIn('Breedte',by['OK-JY100DA']['specifications'])
 def test_secondary_source_cannot_be_ignored_when_it_contradicts(self):
  self.assertNotIn('Breedte',by['SP-GA100RH']['specifications'])
  self.assertTrue(any(d['sku']=='SP-GA100RH' and d['field']=='Breedte' and d['status']=='OPEN' and any(v['identity']=='SKU_MERK_ONLY' for v in d['candidates']) for d in report['differences']))
 def test_supplier_resolution_preserves_exact_fact_and_disagreement_history(self):
  sku='GS-CLI1H100200CE'
  self.assertEqual(by[sku]['specifications']['Glas'],'Helder glas')
  self.assertEqual(ev[sku]['facts']['Glas']['kind'],'supplier')
  d=next(d for d in report['differences'] if d['sku']==sku and d['field']=='Glas')
  self.assertEqual(d['status'],'RESOLVED_SUPPLIER_CORROBORATED')
  self.assertTrue(any(v['value']=='Brons rook' for v in d['candidates']))
  self.assertTrue(any(v['value']=='Helder' and v['identity']=='SKU_EAN_MERK' for v in d['candidates']))
  self.assertEqual(d['resolution']['supplier_source_refs'],ev[sku]['facts']['Glas']['source_refs'])
 def test_retail_ledger_matches_current_evidence(self):
  actual={(p['sku'],label,p['specifications'][label]) for p in catalog for label,e in ev[p['sku']]['facts'].items() if e['kind']=='retailer_exact_sku_ean'}
  ledger={(x['sku'],x['field'],x['new']) for x in report['changes'] if x['action']=='AANGEVULD'}
  self.assertEqual(actual,ledger)
 def test_extra_fields_keep_identity_units_and_component_scope(self):
  self.assertFalse(applicable(by['5-CE-403'],{'label':'Diameter plug','value':'64 mm'})[0])
  self.assertFalse(applicable(by['SK-IM60LCH'],{'label':'Plaats bediening','value':'Links'})[0])
  page={'url':'https://www.badkamerxxl.nl/test','title':'Brauer test','ref':'fixture','retrieval':'public_live_fetch_html','lines':[{'line':i+1,'text':t} for i,t in enumerate(['Fabrikantnummer','5-NG-008','EAN','4260483795992','Merk','Brauer','Diameter plug','64 mm','Aansluitmaat sifon','1.1/4"','Met handdouche','Bijlagen'])]}
  fields=parse(page)['fields'];self.assertIn(('Diameter plug','64 mm'),[(x['label'],x['value']) for x in fields]);self.assertIn(('Aansluitmaat sifon','1 1/4"'),[(x['label'],x['value']) for x in fields]);self.assertNotIn('Handdouche inbegrepen',[x['label'] for x in fields])
 def test_gate_blocks_review_flag_only_changes(self):
  gate=json.loads(Path('prepared/release-gate.json').read_text());self.assertFalse(gate['retail_specifications_reviewed'])
  for f in REQUIRED:gate[f]=True
  result=check('prepared/catalog.json',gate);self.assertFalse(result['import_allowed']);self.assertTrue(any(x.startswith('RETAIL_FIELDS_UNRESOLVED:') for x in result['reasons']))
if __name__=='__main__':unittest.main(verbosity=2)
