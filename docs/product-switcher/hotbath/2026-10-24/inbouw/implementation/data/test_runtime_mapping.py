"""Guard tests for source/merchant decisions and the exact Shopify variant route."""
import copy
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FRESH_PATH = ROOT / 'fresh-products.json'


class MappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The command entry point below strips the custom argument before unittest sees it.
        cls.fresh_path = FRESH_PATH
        cls.fresh = json.loads(cls.fresh_path.read_text())
        cls.products = cls.fresh.get('products', cls.fresh.get('nodes', cls.fresh.get('data', {}).get('nodes')))
        cls.temp = tempfile.TemporaryDirectory(prefix='mapping-qa-', dir=ROOT)
        cls.baseline = cls.compile(cls.products, 'baseline')

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    @classmethod
    def compile(cls, products, name, expect_success=True):
        folder = Path(cls.temp.name) / name
        folder.mkdir()
        source = folder / 'fresh.json'
        source.write_text(json.dumps({'products': products}))
        run = subprocess.run([sys.executable, str(ROOT / 'build_runtime_mapping.py'), '--fresh', str(source), '--output-dir', str(folder)], capture_output=True, text=True)
        if not expect_success:
            return run
        if run.returncode:
            raise AssertionError(run.stderr)
        result = json.loads((folder / 'compiled-mapping.json').read_text())
        result['_liquid'] = (folder / 'bc-product-inbouw-data.liquid').read_text()
        return result

    def products_copy(self):
        return copy.deepcopy(self.products)

    @staticmethod
    def find(products, sku):
        return next(p for p in products if p and any(v['sku'] == sku for v in p['variants']['nodes']))

    def test_all_merchant_exclusions_absent(self):
        excluded = {row['trim_sku'] for row in self.baseline['merchant_exclusions']}
        self.assertEqual(len(excluded), 70)
        self.assertFalse(excluded & {row['trim_sku'] for row in self.baseline['mappings']})

    def test_exact_route_contract(self):
        route_rows = re.findall(r'\{%- when (\d+) -%\}([^\n]+)', self.baseline['_liquid'])
        mapping = {row['trim_product_id'].rsplit('/', 1)[1]: row for row in self.baseline['mappings']}
        self.assertEqual(len(route_rows), len(mapping))
        self.assertEqual(len({row[0] for row in route_rows}), len(mapping))
        for product_id, value in route_rows:
            row = mapping[product_id]
            self.assertEqual(value.split('|'), [row['trim_variant_id'].rsplit('/', 1)[1], row['trim_sku'], row['body_handle'], row['body_sku'], row['body_variant_id'].rsplit('/', 1)[1], '1'])
        self.assertLess(len(self.baseline['_liquid'].encode()), 256000)

    def test_included_body_cannot_be_charged_again(self):
        products = self.products_copy()
        self.find(products, 'CB105EXT18CR')['included'] = {'type': 'boolean', 'value': 'true'}
        result = self.compile(products, 'included')
        self.assertNotIn('CB105EXT18CR', {row['trim_sku'] for row in result['mappings']})
        self.assertEqual(len(result['mappings']), len(self.baseline['mappings']) - 1)

    def test_unavailable_body_blocks_all_its_routes(self):
        products = self.products_copy()
        self.find(products, 'HBCB105')['variants']['nodes'][0]['availableForSale'] = False
        result = self.compile(products, 'unavailable')
        self.assertFalse(any(row['body_sku'] == 'HBCB105' for row in result['mappings']))
        expected = [row for row in self.baseline['mappings'] if row['body_sku'] != 'HBCB105']
        self.assertEqual(result['mappings'], expected)

    def test_duplicate_body_sku_is_not_guessed(self):
        products = self.products_copy()
        duplicate = copy.deepcopy(self.find(products, 'HBCB105'))
        duplicate['id'] = 'gid://shopify/Product/99999999999'
        duplicate['variants']['nodes'][0]['id'] = 'gid://shopify/ProductVariant/99999999999'
        products.append(duplicate)
        result = self.compile(products, 'duplicate-body')
        self.assertFalse(any(row['body_sku'] == 'HBCB105' for row in result['mappings']))

    def test_changed_trim_sku_does_not_keep_old_relation(self):
        products = self.products_copy()
        self.find(products, 'CB105EXT18CR')['variants']['nodes'][0]['sku'] = 'UNRELATED-SKU'
        result = self.compile(products, 'changed-sku')
        self.assertNotIn('CB105EXT18CR', {row['trim_sku'] for row in result['mappings']})
        self.assertEqual(len(result['mappings']), len(self.baseline['mappings']) - 1)

    def test_unpublished_trim_is_held(self):
        products = self.products_copy()
        self.find(products, 'CB105EXT18CR')['publishedAt'] = None
        result = self.compile(products, 'unpublished')
        self.assertNotIn('CB105EXT18CR', {row['trim_sku'] for row in result['mappings']})

    def test_incomplete_variants_fail_closed(self):
        products = self.products_copy()
        self.find(products, 'CB105EXT18CR')['variants']['pageInfo']['hasNextPage'] = True
        run = self.compile(products, 'incomplete', expect_success=False)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('Variant pagination unfinished', run.stderr)

    def test_missing_plain_body_not_substituted(self):
        body_skus = {v['sku'] for p in self.products if p for v in p['variants']['nodes']}
        if 'HBCB010' in body_skus:
            self.skipTest('Exact plain body is present in fresh read')
        self.assertNotIn('B010EXTGN', {row['trim_sku'] for row in self.baseline['mappings']})
        held = next(row for row in self.baseline['held'] if row['trim_sku'] == 'B010EXTGN')
        self.assertIn('BODY_EXACT_SKU_NOT_UNIQUE_OR_MISSING', held['reasons'])


if __name__ == '__main__':
    FRESH_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'fresh-products.json'
    unittest.main(argv=[sys.argv[0]], verbosity=2)
