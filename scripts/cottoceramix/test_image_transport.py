import copy
import json
import unittest
from unittest.mock import patch

from build_import_plan import image_transport_source, make_input
from build_unit_plan import prepare as prepare_units
from test_import_plan import fixture
from test_unit_plan import unit_row


class ImageTransportTests(unittest.TestCase):
    def test_both_uppercase_extensions_change_without_other_path_changes(self):
        source = 'https://cottoceramix.nl/resize/SOURCE_Name.JPG/1000/490/True/my-seo.JPG'
        expected = 'https://cottoceramix.nl/resize/SOURCE_Name.jpg/1000/490/True/my-seo.jpg'
        self.assertEqual(image_transport_source(source), expected)

    def test_lowercase_is_idempotent_and_middle_text_is_untouched(self):
        source = 'https://cottoceramix.nl/resize/ABC.jpg/1000/1000/True/SEO.jpg'
        self.assertEqual(image_transport_source(source), source)
        self.assertEqual(image_transport_source(image_transport_source(source)), source)
        for name in ['JPG-middle', 'name.JPG.backup', 'name.JPGtext', 'name.Jpg']:
            value = 'https://cottoceramix.nl/resize/' + name
            self.assertEqual(image_transport_source(value), value)

    def test_other_hosts_routes_protocols_and_credentials_are_untouched(self):
        for value in ['https://example.org/resize/name.JPG', 'https://cottoceramix.nl.evil.test/resize/name.JPG',
                      'http://cottoceramix.nl/resize/name.JPG', 'https://cottoceramix.nl/images/name.JPG',
                      'https://name@cottoceramix.nl/resize/name.JPG', 'https://cottoceramix.nl:444/resize/name.JPG',
                      'not a URL', None]:
            with self.subTest(value=value):
                self.assertEqual(image_transport_source(value), value)

    def test_query_fragment_host_case_and_resize_parameters_are_preserved(self):
        value = 'HTTPS://WWW.COTTOCERAMIX.NL:443/resize/MY.JPG/823/411/False/SEO.JPG?file=keep.JPG&width=12#keep.JPG'
        expected = 'HTTPS://WWW.COTTOCERAMIX.NL:443/resize/MY.jpg/823/411/False/SEO.jpg?file=keep.JPG&width=12#keep.JPG'
        self.assertEqual(image_transport_source(value), expected)
        self.assertEqual(image_transport_source('https://cottoceramix.nl/resize/a.JPG?'), 'https://cottoceramix.nl/resize/a.jpg?')

    def test_m2_transport_only_changes_file_sources_not_metadata_or_prices(self):
        row = fixture()
        original = 'https://cottoceramix.nl/resize/BASE.JPG/1000/490/True/SEO.JPG'
        row['live']['images'] = [original]
        source_before = copy.deepcopy(row)
        with patch('build_import_plan.image_transport_source', side_effect=lambda url: url):
            previous = make_input(row, 'Test')
        current = make_input(row, 'Test')
        expected = copy.deepcopy(previous)
        expected['files'][0]['originalSource'] = image_transport_source(original)
        self.assertEqual(current, expected)
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in current['metafields']}
        self.assertEqual(json.loads(mf['custom.bron_toelichtingen_json'])['tiles']['source']['photo_sources'], [original])
        self.assertEqual(row, source_before)

    def test_unit_transport_only_changes_file_sources_not_metadata_or_prices(self):
        row = unit_row()
        original = 'https://cottoceramix.nl/resize/UNIT.JPG/1000/1000/True/UNIT-SEO.JPG'
        row['live']['images'] = [original]
        source_before = copy.deepcopy(row)
        with patch('build_unit_plan.image_transport_source', side_effect=lambda url: url):
            previous = prepare_units([row])['products'][0]['input']
        current = prepare_units([row])['products'][0]['input']
        expected = copy.deepcopy(previous)
        expected['files'][0]['originalSource'] = image_transport_source(original)
        self.assertEqual(current, expected)
        mf = {m['namespace'] + '.' + m['key']: m['value'] for m in current['metafields']}
        self.assertEqual(json.loads(mf['custom.bron_toelichtingen_json'])['tiles']['source']['photo_sources'], [original])
        self.assertEqual(row, source_before)


if __name__ == '__main__':
    unittest.main()
