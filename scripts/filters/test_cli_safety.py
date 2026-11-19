import tempfile
import unittest
from pathlib import Path

from prepare_catalog import output_paths


class OutputSafety(unittest.TestCase):
    def test_default_keeps_private_results_next_to_private_input(self):
        with tempfile.TemporaryDirectory() as d:
            source=Path(d)/'private-catalog.json'
            source.write_text('{"private":"source"}')
            output,stats=output_paths(source)
            self.assertEqual(output.parent,source.parent)
            self.assertEqual(stats.parent,source.parent)
            self.assertEqual(source.read_text(),'{"private":"source"}')

    def test_input_cannot_be_used_as_output(self):
        with tempfile.TemporaryDirectory() as d:
            source=Path(d)/'catalog.json'
            source.write_text('unchanged')
            with self.assertRaises(ValueError):output_paths(source,source)
            self.assertEqual(source.read_text(),'unchanged')

    def test_implicit_summary_cannot_overwrite_input(self):
        with tempfile.TemporaryDirectory() as d:
            source=Path(d)/'format-summary.json'
            source.write_text('unchanged')
            with self.assertRaises(ValueError):output_paths(source,source.with_name('result.json'))
            self.assertEqual(source.read_text(),'unchanged')


if __name__=='__main__':unittest.main()
