import copy
import unittest

from build_shop_identity_review import compare,plan


def fixture():
    catalogue=[{'vendor':'BRAUER','sku':'TEST-A','ean':'1234567890123','handle_proposal':'brauer-test'}]
    controls=dict(status='PASS',store_domain='badkamercity.nl',shopify_writes=0,
                  **dict.fromkeys(['read_only','sku_positive','sku_negative_empty','barcode_positive',
                                   'handle_positive','handle_negative_empty','bulk_last_term_positive','no_vendor_filter'],True))
    page={'variants':{'nodes':[],'pageInfo':{'hasNextPage':False}},
          'products':{'nodes':[],'pageInfo':{'hasNextPage':False}}}
    response=[{'batch':0,'status':'COMPLETE','pages':[page]}]
    variant={'id':'variant-1','sku':'TEST-A','barcodes':{'nodes':[{'value':'1234567890123'}],
             'pageInfo':{'hasNextPage':False}},'product':{'id':'product-1','handle':'brauer-test','vendor':'BRAUER'}}
    return catalogue,controls,response,variant


class IdentityReviewTests(unittest.TestCase):
    def test_no_match_still_does_not_grant_import_permission(self):
        c,k,r,v=fixture();out=compare(c,plan(c),r,k)
        self.assertEqual(out['status_counts'],{'NO_EXISTING_IDENTITY_FOUND':1})
        self.assertFalse(out['import_allowed']);self.assertTrue(out['refresh_required_before_import'])
        self.assertFalse(out['linked_product_ids_assigned'])

    def test_full_identity_match_is_separate_from_permission_or_assignment(self):
        c,k,r,v=fixture();r[0]['pages'][0]['variants']['nodes']=[v]
        r[0]['pages'][0]['products']['nodes']=[v['product']]
        out=compare(c,plan(c),r,k)
        self.assertEqual(out['articles'][0]['status'],'MATCH_EXISTING_EXACT_BRAUER_SKU_EAN')
        self.assertFalse(out['articles'][0]['import_allowed'])
        self.assertFalse(out['articles'][0]['linked_product_id_assigned'])

    def test_wrong_ean_brand_or_sku_case_requires_review(self):
        for change in ['ean','brand','sku_case']:
            c,k,r,v=fixture()
            if change=='ean':v['barcodes']['nodes']=[{'value':'9999999999999'}]
            if change=='brand':v['product']['vendor']='Other'
            if change=='sku_case':v['sku']='test-a'
            r[0]['pages'][0]['variants']['nodes']=[v]
            self.assertEqual(compare(c,plan(c),r,k)['articles'][0]['status'],'IDENTITY_COLLISION_REVIEW')

    def test_barcode_alias_is_compared_without_leading_zero_guessing(self):
        c,k,r,v=fixture();v['sku']='OTHER';v['barcodes']['nodes']=[{'value':'9999999999999'},{'value':'1234567890123'}]
        r[0]['pages'][0]['variants']['nodes']=[v]
        self.assertEqual(compare(c,plan(c),r,k)['review_required_articles'],1)
        v['barcodes']['nodes']=[{'value':'01234567890123'}]
        self.assertEqual(compare(c,plan(c),r,k)['articles_with_existing_identity_or_handle'],0)

    def test_handle_collision_is_found_even_without_an_identifier_match(self):
        c,k,r,v=fixture();r[0]['pages'][0]['products']['nodes']=[v['product']]
        self.assertEqual(compare(c,plan(c),r,k)['articles'][0]['status'],'HANDLE_COLLISION_REVIEW')

    def test_duplicate_full_identities_are_not_silently_merged(self):
        c,k,r,v=fixture();other=copy.deepcopy(v);other['id']='variant-2'
        r[0]['pages'][0]['variants']['nodes']=[v,other]
        self.assertEqual(compare(c,plan(c),r,k)['articles'][0]['status'],'MULTIPLE_EXISTING_VARIANTS_REVIEW')

    def test_incomplete_or_duplicate_receipts_are_refused(self):
        c,k,r,v=fixture()
        for responses in [[],r+r]:
            with self.assertRaises(ValueError):compare(c,plan(c),responses,k)
        r[0]['pages'][0]['variants']['pageInfo']['hasNextPage']=True
        with self.assertRaises(ValueError):compare(c,plan(c),r,k)

    def test_controls_barcode_pagination_and_source_identity_are_required(self):
        c,k,r,v=fixture();bad=copy.deepcopy(k);bad['bulk_last_term_positive']=False
        with self.assertRaises(ValueError):compare(c,plan(c),r,bad)
        bad=copy.deepcopy(k);bad['store_domain']='other.example'
        with self.assertRaises(ValueError):compare(c,plan(c),r,bad)
        v['barcodes']['pageInfo']['hasNextPage']=True;r[0]['pages'][0]['variants']['nodes']=[v]
        with self.assertRaises(ValueError):compare(c,plan(c),r,k)
        c,k,r,v=fixture();work=plan(c);c[0]['ean']='9999999999999'
        with self.assertRaises(ValueError):compare(c,work,r,k)

    def test_source_ids_must_be_unique_strings(self):
        c,k,r,v=fixture()
        with self.assertRaises(ValueError):plan(c+c)
        c[0]['ean']=1234567890123
        with self.assertRaises(ValueError):plan(c)


if __name__=='__main__':unittest.main(verbosity=2)
