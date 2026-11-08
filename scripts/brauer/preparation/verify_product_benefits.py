"""Read-only native XLSX comparison: preserved sheets and derived benefits."""
import argparse
from collections import Counter
import json
from pathlib import Path
import posixpath
import xml.etree.ElementTree as E
import zipfile
from build_product_benefits import approved_definition

NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


class NativeBook:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        self.strings = [''.join(x.itertext()) for x in E.fromstring(self.z.read('xl/sharedStrings.xml')).findall('s:si', NS)]
        self.names = [x.get('name') for x in E.fromstring(self.z.read('xl/workbook.xml')).findall('s:sheets/s:sheet', NS)]
        self.styles = E.fromstring(self.z.read('xl/styles.xml'))

    def value(self, cell):
        if cell is None:
            return ''
        if cell.get('t') == 'inlineStr':
            return ''.join(cell.find('s:is', NS).itertext())
        value = cell.find('s:v', NS)
        text = value.text or '' if value is not None else ''
        return self.strings[int(text)] if cell.get('t') == 's' else text

    def sheet(self, index):
        return E.fromstring(self.z.read(f'xl/worksheets/sheet{index+1}.xml'))

    def cell_records(self, index):
        return {c.get('r'): (self.value(c),
                E.tostring(c.find('s:f', NS)) if c.find('s:f', NS) is not None else None,
                c.get('t') in {'s', 'str', 'inlineStr'}, c.get('t') == 'e')
                for c in self.sheet(index).findall('.//s:c', NS)}

    def style(self, index):
        x = self.styles.find('s:cellXfs', NS)[index]
        result = dict(x.attrib)
        for attr, tag in [('fontId', 'fonts'), ('fillId', 'fills'), ('borderId', 'borders')]:
            number = int(result.pop(attr, '0'))
            result[attr] = E.tostring(self.styles.find('s:'+tag, NS)[number]).decode()
        num = int(result.pop('numFmtId', '0'))
        result['number_format'] = next((f.get('formatCode') for f in self.styles.findall('s:numFmts/s:numFmt', NS) if int(f.get('numFmtId')) == num), str(num))
        result['children'] = [E.tostring(c).decode() for c in x]
        return result

    def tables(self, index):
        parts = self.sheet(index).find('s:tableParts', NS)
        if parts is None:
            return []
        rels = E.fromstring(self.z.read(f'xl/worksheets/_rels/sheet{index+1}.xml.rels'))
        targets = {r.get('Id'): r.get('Target') for r in rels}
        result = []
        for part in parts:
            rid = part.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            target = targets[rid]
            name = target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl/worksheets', target))
            table = E.fromstring(self.z.read(name))
            # Package-local IDs may be regenerated; compare resolved native tables.
            table.attrib.pop('id', None)
            result.append(E.canonicalize(E.tostring(table).decode()))
        return result


def verify(root, workbook, source):
    old, new = NativeBook(source), NativeBook(workbook)
    if 'Pluspunten' in old.names:
        assert new.names == old.names
    else:
        assert new.names == old.names + ['Pluspunten']
    styles_old, styles_new = {}, {}
    cells_compared = 0
    unchanged = [i for i, name in enumerate(old.names) if name != 'Pluspunten']
    for i in unchanged:
        assert old.cell_records(i) == new.cell_records(i), old.names[i]+' values/formulas/types changed'
        a, b = old.sheet(i), new.sheet(i)
        for address, ac, bc in zip(old.cell_records(i), a.findall('.//s:c', NS), b.findall('.//s:c', NS)):
            ai, bi = int(ac.get('s', '0')), int(bc.get('s', '0'))
            if ai not in styles_old: styles_old[ai] = old.style(ai)
            if bi not in styles_new: styles_new[bi] = new.style(bi)
            assert styles_old[ai] == styles_new[bi], (old.names[i], address, 'style changed')
            cells_compared += 1
        for tag in ['sheetViews', 'sheetFormatPr', 'cols', 'mergeCells', 'conditionalFormatting', 'dataValidations', 'autoFilter']:
            assert [E.tostring(x) for x in a.findall('s:'+tag, NS)] == [E.tostring(x) for x in b.findall('s:'+tag, NS)], (old.names[i], tag)
        assert [r.attrib for r in a.findall('s:sheetData/s:row', NS)] == [r.attrib for r in b.findall('s:sheetData/s:row', NS)], old.names[i]+' row settings'
        assert old.tables(i) == new.tables(i), old.names[i]+' native tables changed'

    catalog = json.loads((root/'prepared/catalog.json').read_text())
    evidence = json.loads((root/'prepared/specification-evidence.json').read_text())
    definitions = json.loads((root/'prepared/manufacturer-features.json').read_text())['definitions']
    records = json.loads((root/'prepared/product-benefits.json').read_text())
    by = {p['sku']: p for p in catalog}
    assert len(records) == len(catalog) == 13161
    rules = Counter()
    for r in records:
        p = by[r['sku']]
        assert r['ean'] == p['ean'] == evidence[p['sku']]['ean']
        assert r['product_type'] == p['product_type']
        assert len(r['items']) <= 4
        assert len(set(x['text'] for x in r['items'])) == len(r['items'])
        for item in r['items']:
            assert 'compleet' not in item['text'].lower()
            assert item['basis']
            rules[item['rule']] += 1
            for key in item.get('definition_refs', []):
                assert approved_definition(definitions, key), (p['sku'], key)
            for f in item['basis']:
                if f.get('source') == 'supplier_record':
                    assert p['source'][f['field']] == f['value']
                    assert p['source']['Merk'] == 'BRAUER'
                    assert p['source']['Artikelcode'] == p['sku'] and p['source']['EAN'] == p['ean']
                    assert f['evidence']['source_refs'] == p['source_refs']
                    assert f['evidence']['fragment'] == f['value']
                else:
                    assert p['specifications'][f['field']] == f['value']
                    assert evidence[p['sku']]['facts'][f['field']] == f['evidence']
                assert f['field'] not in p.get('retail_review', {}).get('open_fields', [])
    rows = new.sheet(new.names.index('Pluspunten')).findall('s:sheetData/s:row', NS)
    rows = [r for r in rows if int(r.get('r')) >= 6]
    assert len(rows) == len(catalog)
    eans = 0
    for row, p, proof in zip(rows, catalog, records):
        cells = {c.get('r').rstrip('0123456789'): c for c in row}
        expected = [p['sku'], p['ean'], p['product_type'], p['title'],
                    *[proof['items'][i]['text'] if i < len(proof['items']) else '' for i in range(4)]]
        for col, value in zip('ABCDEFGH', expected):
            assert new.value(cells.get(col)) == value, (p['sku'], col)
        assert cells['A'].get('t') in {'s', 'str', 'inlineStr'}
        assert cells['B'].get('t') in {'s', 'str', 'inlineStr'}
        eans += 1
    errors = sum(c.get('t')=='e' for i in range(len(new.names)) for c in new.sheet(i).findall('.//s:c', NS))
    assert errors == 0
    return {'status': 'PASS', 'worksheets': len(new.names), 'original_sheets_preserved': len(unchanged),
            'original_cells_compared': cells_compared, 'original_cell_styles_and_native_tables_preserved': True,
            'benefit_article_rows_exact': len(rows), 'benefits_exact': sum(rules.values()),
            'articles_with_benefits': sum(bool(r['items']) for r in records), 'by_rule': dict(rules),
            'new_sheet_eans_as_text': eans, 'native_error_cells': errors, 'desktop_excel_tested': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('workbook', type=Path)
    parser.add_argument('source', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.root, args.workbook, args.source), ensure_ascii=False))
