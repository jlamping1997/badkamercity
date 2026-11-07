"""Full-catalog evidence, identity preservation and important extraction boundaries."""
import unittest,json,hashlib
from pathlib import Path
from build_specifications import build,ALIASES

c=json.loads(Path('prepared/catalog.json').read_text()); by={p['sku']:p for p in c}
ev=json.loads(Path('prepared/specification-evidence.json').read_text())
class SpecificationTests(unittest.TestCase):
 def test_every_visible_field_has_evidence(self):
  for p in c:
   items=[i for g in p['customer_specifications'] for i in g['items']]
   self.assertEqual(len(items),len({i['key'] for i in items}),p['sku'])
   self.assertEqual({i['label']:i['value'] for i in items},p['specifications'])
   self.assertEqual(set(p['specifications']),set(ev[p['sku']]['facts']))
   for label,e in ev[p['sku']]['facts'].items():
    self.assertTrue(e['fragment']);self.assertEqual(ev[p['sku']]['ean'],p['ean'])
    if e['kind']=='supplier':self.assertTrue(e['source_refs'])
    else:self.assertTrue(e['url']);self.assertTrue(p.get('previous_exact_sku_verification'))
   self.assertEqual(p['specifications']['Artikelnummer'],p['sku'])
   self.assertFalse(any('Te bevestigen' in i['value'] for i in items))
 def test_existing_business_state_unchanged(self):
  baseline=json.loads(Path('prepared/specification-baseline.json').read_text())
  for p in c:
   original={k:v for k,v in p.items() if k not in {'specifications','customer_specifications','specification_review'}}
   digest=hashlib.sha256(json.dumps(original,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
   self.assertEqual(digest,baseline[p['sku']],p['sku'])
 def test_conflicted_values_are_absent(self):
  for p in c:
   for field in p['source_conflicts']:self.assertNotIn(field,p['specifications'])
   for field in p.get('measurement_hold',{}).get('fields',[]):self.assertNotIn(ALIASES.get(field,field),p['specifications'])
 def test_no_nominal_dimensions_become_physical(self):
  for p in c:
   for label,e in ev[p['sku']]['facts'].items():
    if label in {'Breedte','Diepte','Hoogte','Lengte'} and e['kind']=='supplier':self.assertRegex(e['fragment'],r'\b(?:mm|cm)\b',p['sku'])
  self.assertNotIn('Breedte',by['OK-JY100CH']['specifications'])
  self.assertEqual(by['OK-JY120-4CH']['specifications']['Breedte'],'119 cm')
 def test_singular_plural_and_explicit_negative(self):
  self.assertEqual(by['SK-IM60LCH']['specifications']['Aantal deuren'],'1')
  self.assertEqual(by['WT-AU1000LHW']['specifications']['Aantal spoelbakken'],'1')
  self.assertEqual(by['WT-AU1000LHW']['specifications']['Aantal kraangaten'],'0')
  self.assertEqual(by['OK-JY80CH']['specifications']['Aantal sifonuitsparingen'],'1')
  self.assertEqual(by['SK-IM60LCH']['specifications']['Verlichting'],'Nee')
  self.assertNotIn('Verlichting',by['HK-AD120LCH']['specifications'])
  self.assertEqual(by['5-CE-018RR']['specifications']['Inbouwdeel inbegrepen'],'Ja')
  self.assertNotIn('Inbouwdeel inbegrepen',by['5-GG-024']['specifications'])
 def test_keys_groups_and_identity(self):
  self.assertEqual(len(c),13161);self.assertEqual(len({p['product_type'] for p in c}),76)
  for p in c:
   self.assertNotIn('Artikelrol',p['specifications']);self.assertNotIn('Breedtemaat bron',p['specifications'])
   self.assertFalse(p['import_allowed']);self.assertEqual(p['media']['images'],[])
   self.assertEqual(p['publications'],[])
if __name__=='__main__':unittest.main(verbosity=2)
