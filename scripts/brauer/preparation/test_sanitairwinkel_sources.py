import unittest
from sanitairwinkel_sources import extract


def page(body):
    return {'url': 'https://www.sanitairwinkel.nl/p/1/brauer-test', 'title': 'Generic site title', 'text': body}


class SanitairwinkelTests(unittest.TestCase):
    def test_actual_table_cells_keep_context_and_ignore_other_sections(self):
        source = page('''<section><table><tr><td>Hoogte</td><td>999 cm</td></tr></table></section>
          <section><table><tr><td></td><td>Leveranciernummer</td><td>EXACT</td></tr>
          <tr><td>EAN</td><td>0123456789012</td></tr><tr><td>Merk</td><td>Brauer</td></tr>
          <tr><td>Hoogte</td><td>42 cm</td></tr></table></section>
          <section><table><tr><td>Breedte</td><td>888 cm</td></tr></table></section>''')
        excerpt, record = extract(source)
        self.assertEqual((record['sku'], record['ean'], record['brand']), ('EXACT', '0123456789012', 'Brauer'))
        self.assertEqual([(f['label'], f['value']) for f in record['fields']], [('Hoogte', '42 cm')])
        self.assertIn('Hoogte | 42 cm', [r['text'] for r in excerpt['lines']])

    def test_no_manufacturer_code_is_not_reconstructed_from_ean(self):
        _, record = extract(page('<section><table><tr><td>EAN</td><td>0123456789012</td></tr><tr><td>Merk</td><td>Brauer</td></tr><tr><td>Breedte</td><td>99 cm</td></tr></table></section>'))
        self.assertIsNone(record['sku'])
        self.assertEqual(record['ean'], '0123456789012')

    def test_missing_boolean_cell_is_unknown_explicit_no_is_retained(self):
        _, record = extract(page('<section><table><tr><td>Leveranciernummer</td><td>EXACT</td></tr><tr><td>Met verlichting</td><td></td></tr><tr><td>Met sifon</td><td>Nee</td></tr></table></section>'))
        self.assertEqual([(f['label'], f['value']) for f in record['fields']], [('Sifon inbegrepen', 'Nee')])

    def test_inline_enum_value_is_not_mistaken_for_the_next_boolean_label(self):
        _, record = extract(page('<section><table><tr><td>Leveranciernummer</td><td>EXACT</td></tr><tr><td>Uitvoering uitloop</td><td>Draaibare uitloop</td></tr></table></section>'))
        self.assertEqual([(f['label'], f['value']) for f in record['fields']], [('Uitvoering uitloop', 'Draaibare uitloop')])

    def test_only_allowed_retailer_host_is_accepted(self):
        source = page('')
        source['url'] = 'https://not-an-allowed-source.example/product'
        with self.assertRaises(ValueError):
            extract(source)


if __name__ == '__main__':
    unittest.main(verbosity=2)
