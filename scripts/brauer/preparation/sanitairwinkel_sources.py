"""Read literal retailer table cells; identity is never inferred from a URL."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

from retail_extract import parse


class TableCells(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.sections = []
        self.serial = 0
        self.row = None
        self.cell = None
        self.rows = []
        self.h1 = []
        self.in_h1 = False

    def handle_starttag(self, tag, attrs):
        if tag == 'section':
            self.serial += 1
            self.sections.append(self.serial)
        elif tag == 'tr':
            self.row = {'section': tuple(self.sections), 'cells': []}
        elif tag in {'td', 'th'} and self.row is not None:
            self.cell = []
        elif tag == 'h1':
            self.in_h1 = True

    def handle_data(self, text):
        if self.cell is not None:
            self.cell.append(text)
        if self.in_h1:
            self.h1.append(text)

    def handle_endtag(self, tag):
        if tag in {'td', 'th'} and self.cell is not None:
            value = re.sub(r'\s+', ' ', ''.join(self.cell)).strip()
            self.row['cells'].append(value)
            self.cell = None
        elif tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None
        elif tag == 'section' and self.sections:
            self.sections.pop()
        elif tag == 'h1':
            self.in_h1 = False


def extract(result):
    if urlparse(result['url']).hostname != 'www.sanitairwinkel.nl':
        raise ValueError('Only the allowed retailer host may be parsed here')
    parser = TableCells()
    parser.feed(result['text'])
    rows = []
    for row in parser.rows:
        cells = [x for x in row['cells'] if x]
        if len(cells) == 2:
            rows.append({**row, 'label': cells[0], 'value': cells[1]})
    identity_row = next((r for r in rows if r['label'] in {'Leveranciernummer', 'Fabrikantnummer'}), None)
    if identity_row is None:
        identity_row = next((r for r in rows if r['label'] == 'EAN'), None)
    if identity_row is None:
        return None, None
    scoped = [r for r in rows if r['section'] == identity_row['section']]
    page = {
        'url': result.get('final_url') or result['url'],
        'requested_url': result['url'],
        'ref': 'public-fetch:' + result['url'],
        'title': re.sub(r'\s+', ' ', ' '.join(parser.h1)).strip() or result.get('title', ''),
        'retrieval': 'public_live_fetch_html',
        'checked_on': '2026-11-08',
        'source_snapshot_note': 'Fresh anonymous literal HTML table-cell extraction, 2026-11-08; no manufacturer revision guarantee',
        'linked_documents': [u for u in result.get('links', []) if '.pdf' in u.lower()],
        'lines': [{'line': i + 1, 'text': r['label'] + ' | ' + r['value']} for i, r in enumerate(scoped)],
    }
    return page, parse(page)


def main():
    root = Path('prepared')
    response_files = sorted(Path('research/brauer25').glob('*fetch*.json'), key=lambda f: f.stat().st_mtime_ns)
    if not response_files:
        if (root / 'sanitairwinkel-observations25.json').exists():
            print(json.dumps({'saved_typed_records_retained': True, 'raw_responses': 0}))
            return
        raise SystemExit('Geen ruwe fetchresponses; bestaande getypeerde bronbestanden blijven behouden.')
    catalog = {p['sku']: p for p in json.loads((root / 'catalog.json').read_text())}
    by_ean = {p['ean']: p for p in catalog.values()}
    pages, records, outcomes = [], {}, {}
    for file in response_files:
        response = json.loads(file.read_text())
        for result in response.get('results', []):
            if not re.match(r'https://www\.sanitairwinkel\.nl/p/\d+/', result['url']):
                continue
            page, record = extract(result)
            product = catalog.get(record.get('sku')) if record else None
            exact = bool(product and record['ean'] == product['ean'] and str(record['brand']).lower() == 'brauer')
            comparison = bool(product and not record.get('ean') and str(record['brand']).lower() == 'brauer')
            outcome = {'url': result['url'], 'state': 'EXACT_IDENTITY' if exact else 'IDENTITY_NOT_PROVEN',
                       'sku': record.get('sku') if record else None, 'ean': record.get('ean') if record else None,
                       'brand': record.get('brand') if record else None, 'checked_on': '2026-11-08'}
            if not exact:
                if not record:
                    outcome['reason'] = 'Geen bruikbare identiteitstabel'
                elif not record.get('sku'):
                    outcome['reason'] = 'Fabrikantartikelnummer ontbreekt op de bronpagina'
                elif not product:
                    outcome['reason'] = 'Letterlijk fabrikantartikelnummer komt niet voor in onze catalogus'
                elif not record.get('ean'):
                    outcome['reason'] = 'EAN ontbreekt; alleen vergelijkingsbewijs, geen zelfstandige nieuwe specificatie'
                elif record.get('ean') != product['ean']:
                    outcome['reason'] = 'EAN wijkt af van onze catalogus'
                else:
                    outcome['reason'] = 'Merk niet exact BRAUER'
            if record and not record.get('sku') and record.get('ean') in by_ean:
                outcome['expected_catalog_sku'] = by_ean[record['ean']]['sku']
                outcome['reason'] = 'Fabrikantartikelnummer ontbreekt op deze bronpagina; geen zelfstandige aanvulling'
            if comparison:
                outcome['state'] = 'SKU_ONLY_COMPARISON'
            if exact or comparison:
                records[record['url']] = record
                pages.append(page)
                outcome['fields'] = len(record['fields'])
            outcomes[result['url']] = outcome
        for error in response.get('errors', []):
            if not re.match(r'https://www\.sanitairwinkel\.nl/p/\d+/', error.get('url', '')):
                continue
            outcomes[error.get('url', file.name)] = {'url': error.get('url'), 'state': 'FETCH_ERROR', 'error': error}
    for name, value in [('sanitairwinkel-observations25.json', list(records.values())), ('sanitairwinkel-outcomes25.json', list(outcomes.values()))]:
        (root / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    Path('research/brauer25/table-excerpts25.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'exact_records': sum(x['state'] == 'EXACT_IDENTITY' for x in outcomes.values()), 'comparison_records': sum(x['state'] == 'SKU_ONLY_COMPARISON' for x in outcomes.values()), 'identity_not_proven': sum(x['state'] == 'IDENTITY_NOT_PROVEN' for x in outcomes.values()), 'fetch_errors': sum(x['state'] == 'FETCH_ERROR' for x in outcomes.values())}))


if __name__ == '__main__':
    main()
