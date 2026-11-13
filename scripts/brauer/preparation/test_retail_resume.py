"""Regression checks for safe continuation from typed evidence, without HTTP."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from resume_retail_sources import technical_page, typed_record, merge_records


class ResumeTests(unittest.TestCase):
    def test_pending_url_record_takes_precedence_without_losing_other_urls(self):
        old = [{'url': 'a', 'value': 'old'}, {'url': 'b', 'value': 'keep'}]
        new = [{'url': 'a', 'value': 'new'}]
        self.assertEqual(merge_records(old, new), [{'url': 'a', 'value': 'new'}, {'url': 'b', 'value': 'keep'}])
        with self.assertRaises(ValueError):
            merge_records([], new)

    def test_html_only_technical_table_not_recommendations_or_reviews(self):
        target = {'sku': 'EXACT', 'ean': '0123456789012', 'url': 'https://www.badkamerxxl.nl/exact'}
        result = {'url': target['url'], 'title': 'Brauer exact', 'text': '''<h1>Related product dimensions</h1>
          <p>Breedte</p><p>999 cm</p>Specificaties<strong>Product</strong>
          <p>Fabrikantnummer</p><p>EXACT</p><p>EAN</p><p>0123456789012</p><p>Merk</p><p>Brauer</p>
          <p>Hoogte</p><p>42 cm</p><p>Met verlichting</p><p>Met sifon</p>
          <strong>Bijlagen</strong><p>Breedte</p><p>888 cm</p>'''}
        record = typed_record(technical_page(result, target))
        self.assertEqual((record['sku'], record['ean'], record['brand']), ('EXACT', target['ean'], 'Brauer'))
        self.assertEqual(record['checked_on'], '2026-11-08')
        self.assertEqual([(x['label'], x['value']) for x in record['fields']], [('Hoogte', '42 cm')])

    def test_no_identity_table_returns_no_usable_page(self):
        self.assertIsNone(technical_page({'url': 'x', 'title': 'Brauer', 'text': '<h1>Brauer</h1><p>42 cm</p>'}, {'url': 'x', 'sku': 'EXACT'}))

    def test_empty_raw_folder_cannot_erase_prepared_records(self):
        script = Path(__file__).with_name('retail_extract.py').resolve()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'prepared').mkdir()
            target = root / 'prepared/retail-observations.json'
            original = b'[{"url":"https://www.badkamerxxl.nl/retained"}]\n'
            target.write_bytes(original)
            run = subprocess.run([sys.executable, str(script)], cwd=root, capture_output=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertEqual(target.read_bytes(), original)

    def test_saved_resumption_survives_without_raw_fetch_responses(self):
        script = Path(__file__).with_name('resume_retail_sources.py').resolve()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'prepared').mkdir()
            (root / 'research/brauer-retail').mkdir(parents=True)
            inputs = {'retail-observations.json': [{'url': 'old'}],
                      'retail-observations-pending.json': [{'url': 'pending'}],
                      'retail-lookup-resume-targets.json': [],
                      'retail-observations-resumed.json': [{'url': 'resumed'}],
                      'retail-resume-outcomes.json': [{'url': 'resumed', 'state': 'TECHNICAL_TABLE_SAVED'}]}
            for name, data in inputs.items():
                (root / 'prepared' / name).write_text(json.dumps(data))
            run = subprocess.run([sys.executable, str(script)], cwd=root, capture_output=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(len(json.loads((root / 'prepared/retail-observations.json').read_text())), 3)
            self.assertEqual(json.loads((root / 'prepared/retail-resume-outcomes.json').read_text()), inputs['retail-resume-outcomes.json'])

    def test_partial_raw_folder_merges_without_erasing_other_records(self):
        script = Path(__file__).with_name('retail_extract.py').resolve()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'prepared').mkdir()
            (root / 'research/brauer-retail').mkdir(parents=True)
            target = root / 'prepared/retail-observations.json'
            target.write_text(json.dumps([{'url': 'retained', 'sku': 'OLD'}]))
            page = {'url': 'fresh', 'title': 'Brauer', 'ref': 'fixture', 'lines': []}
            (root / 'research/brauer-retail/table-excerpts-test.json').write_text(json.dumps([page]))
            run = subprocess.run([sys.executable, str(script)], cwd=root, capture_output=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual([r['url'] for r in json.loads(target.read_text())], ['retained', 'fresh'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
