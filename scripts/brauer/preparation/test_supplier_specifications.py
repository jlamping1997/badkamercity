import unittest,json,copy
from pathlib import Path
from enrich_supplier_specifications import candidates

catalog=json.loads(Path('prepared/catalog.json').read_text());by={p['sku']:p for p in catalog};ev=json.loads(Path('prepared/specification-evidence.json').read_text());report=json.loads(Path('prepared/supplier-enrichment-report.json').read_text())

class SupplierTests(unittest.TestCase):
 def test_all_additions_have_literal_supplier_evidence(self):
  for x in report['additions']:
   p=by[x['sku']];e=ev[p['sku']]['facts'][x['field']]
   self.assertEqual(p['specifications'][x['field']],x['new']);self.assertEqual(e['kind'],'supplier');self.assertEqual(e['identity'],{'sku':p['sku'],'ean':p['ean'],'brand':'BRAUER'})
   self.assertIn(e['fragment'].lower(),p['source'][e['field']].lower());self.assertTrue(e['source_refs']);self.assertEqual(x['rule'],e['supplier_extension_rule'])
 def test_no_inference_from_model_codes_or_missing_words(self):
  p=copy.deepcopy(by['5-CE-003']);p['source']['Productomschrijving']='Wastafelkraan chroom';p['source']['Uitvoering']=''
  self.assertEqual(candidates(p),[])
  p['source']['Productomschrijving']='Wastafelkraan met staaf handdouche';self.assertNotIn('Aantal straalstanden handdouche',[x['label'] for x in candidates(p)])
 def test_orientation_is_separate_from_mounting_location(self):
  p=by['FO-LA401AN'];self.assertEqual(p['specifications']['Montage'],'Op een wastafelonderkast');self.assertEqual(p['specifications']['Links/rechts te plaatsen'],'Ja')
 def test_explicit_negatives_and_model_names_keep_their_meaning(self):
  rows=[x for x in report['additions'] if x['field']=='Grepen inbegrepen'];self.assertTrue(rows);self.assertTrue(all(x['new']=='Nee' for x in rows))
  for x in report['additions']:
   if x['field']=='Uitvoering':self.assertEqual(x['new'],by[x['sku']]['source']['Uitvoering'])
  self.assertFalse(report['differences'])

if __name__=='__main__':unittest.main(verbosity=2)
