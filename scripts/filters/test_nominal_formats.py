import copy
import unittest
from decimal import Decimal
from nominal_formats import (TileContext, ReviewedManifest, classify_pair,
                             approved_rule_from_decision, pair, format_key)

RECT=TileContext(shape='rectangular',measure_basis='piece')

class NominalTests(unittest.TestCase):
    def test_owner_596_square(self):
        x=classify_pair('596','596',context=RECT)
        self.assertEqual((x.status,x.format_key,x.label,x.delta_mm),('OWNER_APPROVED_RULE','60x60','60 × 60 cm',('4','4')))
        self.assertTrue(x.eligible_for_plan)

    def test_owner_side_rule_on_real_pair_outside_short_target_list(self):
        x=classify_pair('1500','596',context=RECT)
        self.assertEqual((x.status,x.format_key,x.delta_mm),('OWNER_APPROVED_RULE','60x150',('4','0')))
        self.assertEqual(x.raw_pair_mm,('596','1500'))

    def test_orientation_is_one_format(self):
        a=classify_pair('1200','596',context=RECT)
        b=classify_pair('596','1200',context=RECT)
        self.assertEqual(a.format_key,b.format_key)
        self.assertEqual(a.format_key,'60x120')
        self.assertEqual(a.raw_input_mm,('1200','596'))
        self.assertNotEqual(a.raw_input_mm,b.raw_input_mm)

    def test_unapproved_other_rounding_not_promoted(self):
        for raw in ['593','595','599']:
            with self.subTest(raw=raw):
                x=classify_pair(raw,raw,context=RECT)
                self.assertEqual(x.format_key,'60x60')
                self.assertEqual(x.status,'PROPOSED')
                self.assertFalse(x.eligible_for_plan)
                with self.assertRaises(ValueError):approved_rule_from_decision(x,context=RECT)

    def test_mixed_owner_and_proposal_is_proposal(self):
        x=classify_pair('596','1193',context=RECT)
        self.assertEqual((x.format_key,x.status),('60x120','PROPOSED'))

    def test_common_293_nominal_300_pairs(self):
        for a,b,key in [('293','293','30x30'),('293','593','30x60')]:
            with self.subTest(a=a,b=b):
                x=classify_pair(a,b,context=RECT)
                self.assertEqual((x.format_key,x.status),(key,'PROPOSED'))
                self.assertFalse(x.eligible_for_plan)

    def test_established_fractional_formats_unchanged(self):
        for a,b,key in [('75','300','7.5x30'),('112.5','450','11.25x45'),('125','250','12.5x25')]:
            with self.subTest(key=key):
                x=classify_pair(a,b,context=RECT)
                self.assertEqual((x.format_key,x.status,x.delta_mm),(key,'EXACT_RECOGNIZED',('0','0')))

    def test_33_point_5_not_forced_to_33_point_3(self):
        x=classify_pair('335','335',context=RECT)
        self.assertEqual((x.format_key,x.status),('33.5x33.5','EXACT_RECOGNIZED'))

    def test_absolute_tolerance(self):
        self.assertEqual(classify_pair('583','583',context=RECT).status,'BLOCKED_UNKNOWN')
        self.assertEqual(classify_pair('1175','1175',context=RECT).status,'BLOCKED_UNKNOWN')

    def test_relative_tolerance_protects_small_values(self):
        x=classify_pair('72','300',context=RECT)
        self.assertEqual(x.status,'BLOCKED_UNKNOWN')
        y=classify_pair('74','297',context=RECT)
        self.assertEqual((y.format_key,y.status),('7.5x30','PROPOSED'))

    def test_ambiguous_pair_not_arbitrarily_rounded(self):
        x=classify_pair('334','334',context=RECT)
        self.assertEqual(x.status,'BLOCKED_AMBIGUOUS')
        self.assertIsNone(x.format_key)
        self.assertIn('33,3 × 33,3 cm',x.candidates)
        self.assertIn('33,5 × 33,5 cm',x.candidates)

    def test_no_cartesian_pair_invention(self):
        keys={classify_pair(a,b,context=RECT).format_key for a,b in [('600','1200'),('800','800')]}
        self.assertEqual(keys,{'60x120','80x80'})
        self.assertNotIn('60x80',keys)
        self.assertNotIn('80x120',keys)

    def test_mosaic_sheet_nonrectangular_missing_context(self):
        contexts=[TileContext('rectangular','piece',title='Mozaïek 30x30'),
                  TileContext('rectangular','piece',title='Mosaic white'),
                  TileContext('rectangular','sheet'),TileContext('hexagon','piece'),
                  TileContext('unknown','piece'),TileContext('round','piece'),
                  TileContext('rectangular','unknown')]
        for ctx in contexts:
            with self.subTest(ctx=ctx):self.assertEqual(classify_pair('596','596',context=ctx).status,'BLOCKED_CONTEXT')

    def test_observed_shape_names_need_review_even_for_exact_pair(self):
        for word in ['Octogono','Octagon','Hexa','Hexagono','Escama','Scale']:
            with self.subTest(word=word):
                ctx=TileContext('square','piece',title='Cottoceramix '+word+' 20x20')
                self.assertEqual(classify_pair('200','200',context=ctx).status,'BLOCKED_CONTEXT')
        # A colour word beginning with Fan must not be treated as a fan shape.
        self.assertEqual(classify_pair('200','200',context=TileContext('square','piece',title='Fango 20x20')).status,'EXACT_RECOGNIZED')

    def test_unit_is_explicit_and_not_inferred(self):
        self.assertEqual(classify_pair('59.6','59.6',context=TileContext('square','piece',source_unit='cm')).status,'BLOCKED_CONTEXT')
        self.assertEqual(classify_pair('59.6 cm','596',context=RECT).status,'BLOCKED_INVALID')

    def test_invalid_inputs(self):
        for v in [None,0,-1,'','NaN','Infinity',float('nan'),True,'1,2.3','1e3','600 mm']:
            with self.subTest(v=v):self.assertEqual(classify_pair(v,'600',context=RECT).status,'BLOCKED_INVALID')

    def test_decimal_and_comma_inputs(self):
        x=classify_pair('112,5',Decimal('450.0'),context=RECT)
        self.assertEqual(x.format_key,'11.25x45')
        self.assertEqual(x.label,'11,25 × 45 cm')

    def test_reviewed_manifest_scope_and_orientation(self):
        doc={'version':'tile-nominal-v1','unit':'mm','rules':[
            {'raw_mm':['1175','1175'],'nominal_mm':['1200','1200'],'status':'SOURCE_VERIFIED',
             'approval_basis':'manufacturer-nominal-size-record','scope':{'vendor':'Example','series':'A'}}]}
        before=copy.deepcopy(doc);m=ReviewedManifest(doc)
        x=classify_pair('1175','1175',context=TileContext('square','piece',vendor='Example',series='A'),reviewed=m)
        self.assertEqual((x.status,x.format_key),('SOURCE_VERIFIED','120x120'))
        self.assertTrue(x.eligible_for_plan)
        self.assertEqual(doc,before)
        self.assertEqual(classify_pair('1175','1175',context=TileContext('square','piece',vendor='Example',series='B'),reviewed=m).status,'BLOCKED_UNKNOWN')

    def test_proposals_cannot_be_imported_as_reviewed_rules(self):
        with self.assertRaises(ValueError):ReviewedManifest({'version':'tile-nominal-v1','unit':'mm','rules':[
            {'raw_mm':['593','593'],'nominal_mm':['600','600'],'status':'PROPOSED','approval_basis':'draft'}]})

    def test_duplicate_reversed_rule_conflicts(self):
        base={'status':'SOURCE_VERIFIED','approval_basis':'test','nominal_mm':['600','1200']}
        with self.assertRaises(ValueError):ReviewedManifest({'version':'tile-nominal-v1','unit':'mm','rules':[
            {**base,'raw_mm':['596','1193']},{**base,'raw_mm':['1193','596']}]})

    def test_vendor_series_override_global_without_touching_raw(self):
        base={'status':'SOURCE_VERIFIED','approval_basis':'test','raw_mm':['1175','1175']}
        m=ReviewedManifest({'version':'tile-nominal-v1','unit':'mm','rules':[
            {**base,'nominal_mm':['1200','1200']},
            {**base,'nominal_mm':['1175','1175'],'scope':{'vendor':'Example','series':'A'}}]})
        x=classify_pair('1175','1175',context=TileContext('square','piece',vendor='Example',series='A'),reviewed=m)
        self.assertEqual((x.raw_pair_mm,x.nominal_pair_mm),(('1175','1175'),('1175','1175')))

    def test_series_without_vendor_is_not_global(self):
        with self.assertRaises(ValueError):ReviewedManifest({'version':'tile-nominal-v1','unit':'mm','rules':[
            {'raw_mm':['596','596'],'nominal_mm':['600','600'],'status':'SOURCE_VERIFIED','approval_basis':'test','scope':{'series':'A'}}]})

    def test_context_guard_cannot_be_bypassed_by_reviewed_mapping(self):
        m=ReviewedManifest({'version':'tile-nominal-v1','unit':'mm','rules':[
            {'raw_mm':['596','596'],'nominal_mm':['600','600'],'status':'SOURCE_VERIFIED','approval_basis':'test'}]})
        self.assertEqual(classify_pair('596','596',context=TileContext('round','piece'),reviewed=m).status,'BLOCKED_CONTEXT')

    def test_owner_mapping_export_is_explicit(self):
        ctx=TileContext('square','piece',vendor='Porcelanosa',series='Example')
        x=classify_pair('596','596',context=ctx);r=approved_rule_from_decision(x,context=ctx)
        self.assertEqual(r['scope'],{'vendor':'Porcelanosa','series':'Example'})
        self.assertEqual(r['raw_mm'],['596','596'])
        self.assertEqual(r['nominal_mm'],['600','600'])

    def test_duplicate_target_definitions_do_not_create_ambiguity(self):
        x=classify_pair('596','596',context=RECT,targets=[('600','600'),('600.0','600')])
        self.assertEqual(x.status,'OWNER_APPROVED_RULE')

    def test_misspelled_scope_cannot_become_global(self):
        for scope in [{'brand':'Example'},{'vendor':None},'Example']:
            with self.subTest(scope=scope),self.assertRaises(ValueError):
                ReviewedManifest({'version':'tile-nominal-v1','unit':'mm','rules':[
                    {'raw_mm':['596','596'],'nominal_mm':['600','600'],'status':'SOURCE_VERIFIED','approval_basis':'test','scope':scope}]})

    def test_missing_evidence_and_malformed_pairs_fail_closed(self):
        base={'raw_mm':['596','596'],'nominal_mm':['600','600'],'status':'SOURCE_VERIFIED','approval_basis':'test'}
        cases=[{**base,'approval_basis':None},{**base,'approval_basis':123},
               {**base,'raw_mm':'596x596'},{**base,'nominal_mm':['600']},
               {**base,'raw_mm':{'596':'596','600':'600'}}]
        for row in cases:
            with self.subTest(row=row),self.assertRaises(ValueError):
                ReviewedManifest({'version':'tile-nominal-v1','unit':'mm','rules':[row]})

    def test_export_cannot_relabel_unsupported_context(self):
        decision=classify_pair('596','596',context=RECT)
        with self.assertRaises(ValueError):approved_rule_from_decision(decision,context=TileContext('hexagon','piece'))

if __name__=='__main__':unittest.main()
