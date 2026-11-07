from pathlib import Path
from collections import Counter
from decimal import Decimal
import json,unittest,tempfile,copy,sys
from media_inventory import article_for_name,inventory
from preflight import check,REQUIRED

ROOT=Path(sys.argv[1]) if len(sys.argv)>1 and not sys.argv[1].startswith('-') else Path('prepared')
if len(sys.argv)>1 and not sys.argv[1].startswith('-'):sys.argv.pop(1)
catalog=json.loads((ROOT/'catalog.json').read_text());families=json.loads((ROOT/'families.json').read_text());by_sku={p['sku']:p for p in catalog};by_id={g['id']:g for g in families}
def active(axis,state,group):
 if not axis.get('show_only_if_multiple') and axis['key']!='cutouts':return True
 candidates=[by_sku[s] for s in group['skus'] if all(by_sku[s]['options'].get(k)==state.get(k) for k in axis.get('depends_on',[]))]
 return len({p['options'].get(axis['key']) for p in candidates if p['options'].get(axis['key']) is not None})>1
def matches(group,state):
 return [by_sku[s] for s in group['skus'] if all((not active(a,state,group)) or (a.get('show_only_if_multiple') or a['key']=='cutouts') and state.get(a['key']) is None or by_sku[s]['options'].get(a['key'])==state.get(a['key']) for a in group['axes'])]
class Tests(unittest.TestCase):
 def test_full_identity_and_money(self):
  self.assertEqual(len(catalog),13161);self.assertEqual(len(by_sku),13161);self.assertEqual(len({p['ean'] for p in catalog}),13161);self.assertEqual(len({p['handle_proposal'] for p in catalog}),13161)
  for p in catalog:
   cents=int(Decimal(p['advice_ex_vat'])*100);self.assertEqual(int(Decimal(p['price_incl_vat'])*100),(cents*121+50)//100,p['sku']);self.assertFalse(p['import_allowed']);self.assertEqual(p['publications'],[])
  self.assertEqual(sum(bool(p['future_available_date']) for p in catalog),163)
 def test_group_partition_and_contract(self):
  self.assertEqual(Counter(s for g in families for s in g['skus']),Counter(by_sku.keys()))
  for g in families:
   colour=[a for a in g['axes'] if a['key']=='colour']
   if colour:self.assertEqual(g['axes'][0]['key'],'colour');self.assertEqual(colour[0]['visible_limit'],6)
   self.assertFalse(g['same_as_compatibility']);self.assertEqual(g['missing_combination'],'VISIBLE_DISABLED')
   self.assertLessEqual(len({by_sku[s]['source']['Materiaal'] for s in g['skus']}),1)
   if g['product_type']=='Spiegelkasten' and colour:self.assertEqual(colour[0]['kind'],'decor_sample')
 def test_reachability(self):
  for g in families:
   ps=[by_sku[s] for s in g['skus']];keys=[a['key'] for a in g['axes'] if not a.get('show_only_if_multiple') and a['key']!='cutouts'];seen={0};queue=[0]
   while queue:
    i=queue.pop()
    for j,q in enumerate(ps):
     if j not in seen and sum(ps[i]['options'].get(k)!=q['options'].get(k) for k in keys)<=1:seen.add(j);queue.append(j)
   self.assertEqual(len(seen),len(ps),g['id'])
 def test_real_combinations(self):
  # Exhaustive article/axis transitions. Missing candidates must never get a fallback SKU.
  valid=rejected=ambiguous=0
  for g in families:
   for sku in g['skus']:
    p=by_sku[sku];self.assertIn(p,matches(g,p['options']))
    for a in g['axes']:
     if not active(a,p['options'],g):continue
     for value in a['values']:
      state={**p['options'],a['key']:value};found=matches(g,state)
      if not found:rejected+=1;continue
      valid+=1
      if len(found)>1:ambiguous+=1
      for q in found:
       for b in g['axes']:
        if b['key']!=a['key'] and active(b,state,g) and state.get(b['key']) is not None:self.assertEqual(q['options'].get(b['key']),state[b['key']])
  (ROOT/'transition-check.json').write_text(json.dumps({'valid':valid,'missing_rejected':rejected,'ambiguous_never_auto_selected':ambiguous}))
 def test_approved_examples(self):
  p=by_sku['SK-IMD60LCH'];g=by_id[p['family_id']];door=next(a for a in g['axes'] if a['key']=='door')
  self.assertTrue(active(door,p['options'],g));self.assertFalse(active(door,{**p['options'],'width':'80'},g));self.assertEqual(len(matches(g,{**p['options'],'door':None})),2)
  self.assertNotEqual(by_sku['HK-AD120LCH']['family_id'],by_sku['HK-AD160CH']['family_id']);self.assertEqual(by_sku['HK-AD120LCH']['product_type'],'Halfhoge kasten')
  self.assertNotEqual(by_sku['OK-TR80CH']['family_id'],by_sku['OK-TRO80CH']['family_id'])
  self.assertEqual(by_id[by_sku['WT-AU1000HW']['family_id']]['sku_count'],13)
  self.assertEqual(by_sku['5-CE-001']['family_id'],by_sku['5-CE-002']['family_id'])
  self.assertEqual(by_sku['5-CE-001']['family_id'],by_sku['5-CE-003']['family_id'])
  for p in catalog:self.assertNotIn('Edition',p['title'])
 def test_conflicts_and_duplicates_stay_held(self):
  critical={p['sku'] for p in catalog if 'BRONCONFLICT' in p['data_issues']};self.assertEqual(len(critical),27)
  duplicate={p['sku'] for p in catalog if 'KEUZECOMBINATIE_NIET_UNIEK' in p['data_issues']};self.assertEqual(len(duplicate),12)
  for sku in critical|duplicate:self.assertEqual(by_sku[sku]['group_status'],'CONTROLEREN')
  self.assertEqual(sum('MAATBRONCONFLICT' in p['data_issues'] for p in catalog),3)
  self.assertTrue(by_sku['5-CE-001']['specifications']['Hoogte kraan'].startswith('Te bevestigen'))
 def test_exact_filename_matching(self):
  skus={'5-CE-001','5-CE-001-HD1','HK-AD120LCH','HK-AD120RCH'}
  self.assertEqual(article_for_name('5-CE-001-HD1_01',skus),'5-CE-001-HD1');self.assertEqual(article_for_name('5-ce-001_T',skus),'5-CE-001');self.assertIsNone(article_for_name('5-CE-001-HD99',skus));self.assertIsNone(article_for_name('5-CE-0010',skus));self.assertEqual(article_for_name('HK-AD120RCH_1',skus),'HK-AD120RCH')
 def test_first_image_needs_explicit_order(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/'5-CE-001_front.jpg').write_bytes(b'test');(p/'5-CE-001_02.jpg').write_bytes(b'test');r=inventory([by_sku['5-CE-001']],p);self.assertIn('EERSTE_AFBEELDING_KIEZEN',r['articles']['5-CE-001']['issues']);self.assertFalse(r['import_allowed'])
 def test_release_is_blocked_even_if_flags_changed(self):
  gate=json.loads((ROOT/'release-gate.json').read_text());self.assertFalse(check(ROOT/'catalog.json',gate)['import_allowed'])
  for k in REQUIRED:gate[k]=True
  self.assertFalse(check(ROOT/'catalog.json',gate)['import_allowed'])
if __name__=='__main__':unittest.main(verbosity=2)
