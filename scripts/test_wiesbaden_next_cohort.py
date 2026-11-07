"""Offline tests for quarantine-aware deterministic Wiesbaden cohort selection."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

SCRIPT = Path(__file__).with_name('wiesbaden-next-cohort.py')
spec = importlib.util.spec_from_file_location('wiesbaden_next_cohort', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CohortSelectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.source = self.home / 'source.zip'
        self.registry = self.home / 'register.json'

    def store(self, records, quarantined=('A2',), applied=('A3',), protected=('A4',)):
        with ZipFile(self.source, 'w') as z:
            z.writestr('Wiesbaden_20261019/output/product-master.jsonl',
                       '\n'.join(json.dumps(x) for x in records) + '\n')
        self.registry.write_text(json.dumps({'total': len(quarantined),
            'groups': {'held': {'skus': list(quarantined)}},
            'applied_2026_10_21': list(applied),
            'protected_skus': list(protected)}), encoding='utf-8')

    @staticmethod
    def item(sku, type_name='Hoofddouche', **attrs):
        x = {'sku': sku, 'comparison_status': 'EXISTING_WIESBADEN',
            'source_brand': 'Wiesbaden', 'current_vendor': 'Wiesbaden',
            'current_product_type': type_name,
            'product_id': 'gid://shopify/Product/' + sku,
            'variant_id': 'gid://shopify/ProductVariant/' + sku,
            'source_url': 'https://www.wiesbaden.nl/product-' + sku + '.html',
            'source_evidence': {'http_status': 200, 'fetched_at': '2026-10-19T11:15:00Z'}}
        x.update(attrs)
        return x

    def test_strict_skip_quarantine_applied_protected(self):
        self.store([self.item(x) for x in ['A1', 'A2', 'A3', 'A4', 'A5']])
        d = module.select(self.source, self.registry, ['Hoofddouche:2'], 2)
        self.assertEqual([x['sku'] for x in d['selected']], ['A1', 'A5'])
        self.assertEqual(d['excluded_breakdown'], {'quarantine':1,'applied':1,'protected':1})
        self.assertTrue(d['read_only'])
        self.assertEqual(d['writes_confirmed'],0)
        self.assertEqual(d['source_sha256'],module.select(self.source,self.registry,['Hoofddouche:2'],2)['source_sha256'])

    def test_duplicate_source_sku_cannot_be_imported(self):
        self.store([self.item('A1'), self.item('A1')], (), (), ())
        with self.assertRaisesRegex(ValueError,'Not enough fresh'):
            module.select(self.source,self.registry,['Hoofddouche:1'],1)

    def test_bad_source_or_shop_ownership_skipped(self):
        self.store([self.item('A1',current_vendor='Other'),
                    self.item('A2',source_evidence={'http_status':404,'fetched_at':'x'}),
                    self.item('A3')],(),(),())
        d = module.select(self.source,self.registry,['Hoofddouche:1'],1)
        self.assertEqual([x['sku'] for x in d['selected']], ['A3'])

    def test_duplicate_or_overlap_in_registry_blocks_all(self):
        self.store([self.item('A1')], ('A2',), ('A2',), ())
        with self.assertRaisesRegex(ValueError,'overlap'):
            module.select(self.source,self.registry,['Hoofddouche:1'],1)
        self.store([self.item('A1')], ('A2','A2'), (), ())
        with self.assertRaisesRegex(ValueError,'Duplicate SKU'):
            module.select(self.source,self.registry,['Hoofddouche:1'],1)

    def test_quotas_must_equal_requested_count(self):
        self.store([self.item('A1')],(),(),())
        with self.assertRaisesRegex(ValueError,'Quota totals'):
            module.select(self.source,self.registry,['Hoofddouche:1'],2)

    def test_multi_type_quotas_sorted(self):
        self.store([self.item('A2','Handdouche'),self.item('A4','Hoofddouche'),
                    self.item('A3','Handdouche'),self.item('A1','Hoofddouche')],(),(),())
        d = module.select(self.source,self.registry,['Hoofddouche:2','Handdouche:2'],4)
        self.assertEqual([x['sku'] for x in d['selected']],['A1','A4','A2','A3'])
        self.assertEqual(len({x['sku'] for x in d['selected']}),4)


if __name__ == '__main__':
    unittest.main()
