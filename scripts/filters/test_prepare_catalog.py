import copy
import unittest
from prepare_catalog import prepare


class PreparationTests(unittest.TestCase):
    def row(self,id,w,l,title='Regular tile'):
        return {'id':str(id),'handle':'tile-'+str(id),'title':title,'vendor':'Example',
                'width':{'value':str(w)},'length':{'value':str(l)},'size':{'value':'59.6x59.6'}}

    def test_all_assumed_context_rows_remain_not_production_eligible(self):
        source={'public_index_count':3,'rows':[self.row(1,596,596),self.row(2,600,1200),self.row(3,593,593)]}
        before=copy.deepcopy(source);out=prepare(source,expected_count=3)
        self.assertEqual(source,before)
        self.assertEqual(out['summary']['changed_candidate_products'],2)
        self.assertEqual(out['summary']['production_eligible_products'],0)
        self.assertEqual(out['summary']['candidate_format_counts'],{'60x60':2,'60x120':1})
        self.assertTrue(any(r['engine_eligible_under_assumed_context'] for r in out['rows']))
        self.assertTrue(all(not r['eligible_for_plan'] and not r['context_verified'] and not r['production_eligible'] for r in out['rows']))

    def test_mosaic_is_excluded_and_no_mat_finish_false_positive(self):
        out=prepare({'public_index_count':3,'rows':[self.row(1,300,300,'Mozaïek White'),self.row(2,300,300,'Tile Mat white'),self.row(3,300,300,'Hexagon White')]},expected_count=3)
        self.assertEqual([r['status'] for r in out['rows']],['BLOCKED_CONTEXT','EXACT_RECOGNIZED','BLOCKED_CONTEXT'])
        self.assertEqual(out['summary']['unresolved_products'],2)

    def test_scope_and_duplicate_guards(self):
        with self.assertRaises(ValueError):prepare({'rows':[self.row(1,596,596)]},expected_count=1)
        with self.assertRaises(ValueError):prepare({'public_index_count':1,'rows':[self.row(1,596,596)]},expected_count=2)
        with self.assertRaises(ValueError):prepare({'public_index_count':2,'rows':[self.row(1,596,596),self.row(1,596,596)]},expected_count=2)

    def test_unusual_valid_sizes_are_retained_not_called_missing(self):
        out=prepare({'public_index_count':2,'rows':[self.row(1,50,150),self.row(2,62,250)]},expected_count=2)
        self.assertEqual([r['status'] for r in out['rows']],['EXACT_RETAINED','EXACT_RETAINED'])
        self.assertEqual([r['format_key'] for r in out['rows']],['5x15','6.2x25'])
        self.assertEqual(out['summary']['unresolved_products'],0)
        self.assertEqual(out['summary']['changed_candidate_products'],0)

    def test_actual_octogono_titles_not_assumed_rectangular(self):
        out=prepare({'public_index_count':1,'rows':[self.row(1,200,200,'Cottoceramix Niza Octogono Valeta Verde 20x20')]},expected_count=1)
        row=out['rows'][0]
        self.assertEqual(row['status'],'BLOCKED_CONTEXT')
        self.assertIsNone(row['format_key'])
        self.assertFalse(row['context_verified'])

if __name__=='__main__':unittest.main()
