import copy
import json
import unittest
from pathlib import Path
import build_supplemental_groups as compiler

class SupplementalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.remaining=json.loads((compiler.HERE/'coverage_remaining.json').read_text())
        cls.book=json.loads((compiler.BASE/'book_rules.json').read_text())

    def test_exact_book_members_and_hole_patterns_stay_separate(self):
        groups,review,records=compiler.gent_groups(self.remaining,self.book)
        self.assertEqual([len(g['products']) for g in groups],[3,2])
        self.assertEqual(review,[])
        self.assertEqual(len(records),5)
        self.assertEqual(groups[0]['menus'][1]['values'],['Laag','Medium','Hoog'])
        self.assertEqual(groups[1]['menus'][1]['values'],['Laag','Hoog'])

    def test_spom_publication_and_title_conflicts_do_not_enter(self):
        for key,value in [('title','Hotbath SPOM voorbeeld'),('publishedAt',None),('title','Hotbath Wastafelmengkraan - Hoog - GT003IX')]:
            remaining=copy.deepcopy(self.remaining)
            row=next(p for p in remaining['products'] if p['variants']['nodes'][0]['sku']=='GT003IX')
            row[key]=value
            groups,review,records=compiler.gent_groups(remaining,self.book)
            self.assertNotIn('GT003IX',{r['sku'] for r in records})
            self.assertTrue(review)

    def test_hidden_fixed_function_is_not_a_height_choice(self):
        remaining=copy.deepcopy(self.remaining)
        row=next(p for p in remaining['products'] if p['variants']['nodes'][0]['sku']=='GT003IX')
        row['title']+=' thermostatisch'
        groups,review,records=compiler.gent_groups(remaining,self.book)
        self.assertNotIn('GT003IX',{r['sku'] for r in records})
        self.assertTrue(any(r['reason']=='GENT_UNMODELED_FIXED_TITLE_DIFFERENCE' for r in review))

    def test_ibs33_suffixes_cannot_enter_gent_or_supplemental(self):
        groups,review,records=compiler.gent_groups(self.remaining,self.book)
        self.assertFalse(any(r['sku'].startswith('IBS33') for r in records))

    def test_combined_export_has_unique_real_published_handles(self):
        rails=json.loads((compiler.HERE/'rails_supplemental.json').read_text())
        groups,review=compiler.combine(self.remaining,self.book,rails)
        self.assertEqual(review['group_count'],9)
        self.assertEqual(review['product_count'],234)
        self.assertTrue(review['rails_included'])

if __name__=='__main__':unittest.main(verbosity=2)
