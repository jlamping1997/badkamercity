#!/usr/bin/env python3
import json
import unittest
import build_colour_supplemental as supplement

class SupplementalColourTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data,cls.proof,cls.metadata=supplement.build()
        cls.catalog=json.loads((supplement.core.SOURCE/'catalog_snapshot.json').read_text())['products']
        cls.by_handle={p['handle']:p for p in cls.catalog}
        cls.by_sku={supplement.core.sku_of(p):p for p in cls.catalog}

    def test_exact_letter_models_only(self):
        for sku in ['RAARCR1','RAARFAKECR','SWIROUCR1','RAAS50CR']:
            self.assertIsNone(supplement.decode_letters(sku))
        self.assertEqual(supplement.decode_letters('RAARBCP'),('RAAR','BCP','Geborsteld koper PVD'))

    def test_accessories_keep_full_identity_and_only_colour_varies(self):
        self.assertEqual(self.metadata['pure_letter_model_counts'],{'RAAR':9,'RAAS':9,'SWIROU':6})
        for group in self.data['groups']:
            if not group['id'].startswith('hotbath-colour-'):continue
            self.assertEqual([m['key'] for m in group['menus']],['kleur'])
            signatures={supplement.strip_literal_identity(self.by_handle[r['handle']]['title'],supplement.core.sku_of(self.by_handle[r['handle']])) for r in group['products']}
            self.assertEqual(len(signatures),1)

    def test_sds_dimensions_are_literal_and_fixed_hand_titles_not_mixed(self):
        group=next(g for g in self.data['groups'] if 'sds32' in g['id'])
        self.assertEqual(len(group['products']),15)
        self.assertEqual(next(m['values'] for m in group['menus'] if m['key']=='dikte_hoofddouche'),['8 mm','15 mm'])
        for row in group['products']:
            actual=supplement.parse_sds_literal(self.by_handle[row['handle']])
            self.assertEqual(actual[0],row['options'])
        for sku in ['SDS32IX1','SDS32IX14','SDS32IX15']:
            self.assertIsNone(supplement.parse_sds_literal(self.by_sku[sku]))

    def test_current_eligible_products_and_unique_tuples(self):
        handles=[]
        for group in self.data['groups']:
            supplement.core.assert_group(group)
            for row in group['products']:
                self.assertIsNone(supplement.core.exclusion(self.by_handle[row['handle']]))
                self.assertNotEqual(supplement.core.sku_of(self.by_handle[row['handle']]),'SDS32BGP')
                handles.append(row['handle'])
        self.assertEqual(len(handles),len(set(handles)))

    def test_merge_preserves_all_replaced_group_members(self):
        self.assertEqual(self.metadata['new_connections_vs_stable_input'],27)
        stable=json.loads((supplement.HERE/'groups-input.json').read_text())['groups']
        previous={r['handle'] for g in stable if g['id'] in supplement.SDS_REPLACE for r in g['products']}
        current={r['handle'] for g in self.data['groups'] for r in g['products']}
        self.assertEqual(len(previous),12)
        self.assertTrue(previous<=current)

if __name__=='__main__':unittest.main(verbosity=2)
