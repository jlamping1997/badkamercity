import unittest,json,copy
from pathlib import Path
from build_rails_supplemental import build,parse
BASE=Path(__file__).parent
class RailsTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.r=json.loads((BASE/'coverage_remaining.json').read_text());cls.e=json.loads((BASE/'groups-input.json').read_text());cls.h=json.loads((BASE/'colour_review.json').read_text())['excluded_products']
 def result(self,r=None,e=None,h=None):return build(r or self.r,e or self.e,self.h if h is None else h)
 def test_real_known_groups(self):
  x=self.result();self.assertEqual(x['metrics'],{'selected':236,'ready_groups':7,'ready_products':229,'review':7,'excluded':0})
  handles=[p['handle'] for g in x['groups'] for p in g['products']];self.assertEqual(len(set(handles)),229)
 def test_shape_and_switch_classes_separate(self):
  x=self.result();self.assertEqual(len(x['groups']),7)
  self.assertTrue(all('RARVM' not in p['title'] for g in x['groups'] for p in g['products']))
  self.assertEqual([f['family'] for f in x['families']],['RARH','RARV','RAS','RAS8050','RASS','RASS8050','RASV'])
 def test_dimensions_are_real_menu_values(self):
  x=self.result();g=next(g for g in x['groups'] if g['id']=='hotbath-rails-rass-sets')
  self.assertEqual(next(m for m in g['menus'] if m['key']=='lengte')['values'],['50 cm','80 cm'])
  self.assertEqual(next(m for m in g['menus'] if m['key']=='aantal_stangen')['values'],['1 stang','2 stangen','3 stangen','4 stangen'])
 def test_hidden_fixed_term_rejected(self):
  r=copy.deepcopy(self.r);r['products'][0]['title']+=' met extra geïntegreerde schakelaar'
  x=self.result(r);self.assertTrue(any(q.get('sku')=='RASS80-2CR' and q['reason']=='TITLE_TEMPLATE_OR_FIXED_FEATURE_CONFLICT' for q in x['review']))
  self.assertFalse(any(p['handle']==r['products'][0]['handle'] for g in x['groups'] for p in g['products']))
 def test_spom_unpublished_and_hold_excluded(self):
  for mode in ('SPOM','published','hold'):
   r=copy.deepcopy(self.r);p=r['products'][0];h={}
   if mode=='SPOM':p['title']+=' SPOM'
   if mode=='published':p['publishedAt']=None
   if mode=='hold':h[p['handle']]='SOURCE_CONFLICT_HELD_FOR_REVIEW'
   x=self.result(r,h=h);self.assertTrue(any(q['handle']==p['handle'] for q in x['excluded']))
 def test_existing_owner_is_preserved(self):
  e=copy.deepcopy(self.e);e['groups'].append({'id':'already-owned','products':[{'handle':self.r['products'][0]['handle']}]})
  x=self.result(e=e);self.assertTrue(any(q['reason']=='EXISTING_GROUP_RECONCILIATION_REQUIRED' for q in x['excluded']))
 def test_unsupported_vertical_finish_not_imported(self):
  with self.assertRaisesRegex(ValueError,'FINISH_NOT_CONFIRMED'):parse('RASV135-1PBP','irrelevant')
 def test_inbouwpart_not_part_of_parse_grammar(self):
  for sku in ('MBASES2','RASS50','RASS50T','RARVM135-1TB'):
   with self.assertRaisesRegex(ValueError,'UNKNOWN_EXACT_RAILS_MODEL'):parse(sku,'irrelevant')
 def test_duplicate_tuple_blocks_whole_family(self):
  r=copy.deepcopy(self.r);p=copy.deepcopy(r['products'][0]);p['handle']+='-duplicate';r['products'].append(p)
  x=self.result(r);self.assertFalse(any(g['id']=='hotbath-rails-rass-sets' for g in x['groups']));self.assertTrue(any(q['reason']=='DUPLICATE_CHOICE_TUPLES' for q in x['review']))
if __name__=='__main__':unittest.main(verbosity=2)
