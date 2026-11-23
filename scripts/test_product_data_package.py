import unittest
from build_product_data_package import assert_closed, combine, field_dictionary


class ProductDataChecks(unittest.TestCase):
    def fixture(self):
        variant={'id':'gid://shopify/ProductVariant/9007199254740993','price':'12.00','compareAtPrice':None,'sku':'00123','inventoryItem':{'id':'i','tracked':False}}
        core={'p':{'id':'p','variants':{'nodes':[variant]},'variantsCount':{'count':1},'mediaCount':{'count':0}}}
        mf={'p':{'id':'p','metafields':{'nodes':[]}}}
        relations={'p':{'id':'p','media':{'nodes':[]},'collections':{'nodes':[]}}}
        detail={variant['id']:{'id':variant['id'],'product':{'id':'p'},'inventoryItem':{'id':'i','unitCost':None}}}
        return core,mf,relations,detail

    def test_identity_decimal_and_null_survive_join(self):
        records=combine(*self.fixture());variant=records[0]['variants'][0]
        self.assertEqual(variant['id'],'gid://shopify/ProductVariant/9007199254740993')
        self.assertEqual((variant['sku'],variant['price'],variant['compareAtPrice']),('00123','12.00',None))
        self.assertIs(variant['inventoryItem']['tracked'],False)
        self.assertIn('unitCost',variant['inventoryItem'])

    def test_missing_product_layer_fails(self):
        core,mf,relations,details=self.fixture()
        with self.assertRaisesRegex(ValueError,'Incomplete product'):combine(core,{},relations,details)

    def test_orphan_and_truncated_media_fail(self):
        core,mf,relations,details=self.fixture()
        next(iter(details.values()))['product']['id']='other'
        with self.assertRaisesRegex(ValueError,'orphan'):combine(core,mf,relations,details)
        core,mf,relations,details=self.fixture();core['p']['mediaCount']['count']=1
        with self.assertRaisesRegex(ValueError,'media'):combine(core,mf,relations,details)

    def test_nested_pagination_and_field_types(self):
        with self.assertRaisesRegex(ValueError,'pagination'):assert_closed({'inventory':{'pageInfo':{'hasNextPage':True}}})
        fields={x['path']:x['types'] for x in field_dictionary([{'flag':False,'value':None},{'flag':True,'value':''}])}
        self.assertEqual(fields['product.flag'],{'boolean':2})
        self.assertEqual(fields['product.value'],{'null':1,'string':1})


if __name__=='__main__':unittest.main()
