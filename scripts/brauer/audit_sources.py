"""Read-only BRAUER source audit; never connects to Shopify or writes source files.

Usage: python audit_sources.py --sources /path/to/xlsx --output /private/audit
Requires openpyxl. Outputs are private working data, not public repository files.
"""
import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from openpyxl import load_workbook

FIELDS = ['Artikelcode', 'EAN', 'Merk', 'Productomschrijving',
          'Adviesverkoopprijs ex. Btw', 'Levertijd', 'Hoofdcategorie',
          'Productcategorie', 'Productgroep', 'Serie', 'Uitvoering',
          'Materiaal', 'Kleur', 'Afwerking']


def normalized(field, value):
    if value is None:
        return ''
    if field == 'EAN' and isinstance(value, (int, float)):
        return str(int(value))
    if field == 'Adviesverkoopprijs ex. Btw':
        return str(Decimal(str(value)).quantize(Decimal('.01')))
    # SKU punctuation, case and leading zeros are identities, never fuzzy-normalize.
    return str(value).strip()


def ean13_valid(value):
    return (len(value) == 13 and value.isdigit()
            and (sum(int(c) * (1 if i % 2 == 0 else 3)
                     for i, c in enumerate(value[:12])) + int(value[-1])) % 10 == 0)


def audit(source_dir, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(source_dir.glob('Prijslijst BRAUER *.xlsx'))
    if len(files) != 3:
        raise ValueError(f'Expected three BRAUER sources, found {len(files)}')
    by_sku, sources, observations = defaultdict(list), [], []
    for path in files:
        wb = load_workbook(path, read_only=True, data_only=True)
        count = 0
        for ws in wb.worksheets:
            rows = ws.iter_rows(values_only=True)
            headers = [str(x).strip() if x is not None else '' for x in next(rows)]
            if headers[:14] != FIELDS or any(headers[14:]):
                raise ValueError(f'Unexpected schema: {path.name}/{ws.title}: {headers}')
            for row, values in enumerate(rows, 2):
                if not any(v is not None for v in values):
                    continue
                if values[0] is None:
                    raise ValueError(f'Nonempty row without SKU: {path.name}:{row}')
                data = {k: normalized(k, v) for k, v in zip(FIELDS, values[:14])}
                item = {'source_file': path.name, 'source_sheet': ws.title,
                        'source_row': row, 'fields': data}
                by_sku[data['Artikelcode']].append(item)
                observations.append(item)
                count += 1
        wb.close()
        sources.append({'file': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'article_rows': count})

    conflicts, master = [], []
    for sku, items in sorted(by_sku.items()):
        resolved, differences = {}, []
        for field in FIELDS:
            values = sorted({x['fields'][field] for x in items if x['fields'][field] != ''})
            resolved[field] = values[0] if len(values) == 1 else ''
            if len(values) > 1:
                differences.append(field)
                conflicts.append({'sku': sku, 'field': field, 'values': values,
                                  'evidence': [{'file': x['source_file'], 'row': x['source_row'],
                                                'value': x['fields'][field]} for x in items]})
        master.append({'sku': sku, 'observations': len(items),
                       'programs': [x['source_file'] for x in items],
                       'conflict_fields': differences, 'fields': resolved,
                       'source_refs': [{k: v for k, v in x.items() if k != 'fields'} for x in items]})
    ean_to_skus = defaultdict(set)
    for item in observations:
        ean_to_skus[item['fields']['EAN']].add(item['fields']['Artikelcode'])
    ean_collisions = {ean: sorted(v) for ean, v in ean_to_skus.items() if len(v) > 1}
    summary = {
        'date': '2026-11-06', 'sources': sources, 'source_rows': len(observations),
        'unique_skus': len(by_sku), 'repeated_source_rows': len(observations) - len(by_sku),
        'skus_in_multiple_files': sum(len(v) > 1 for v in by_sku.values()),
        'occurrence_distribution': dict(Counter(str(len(v)) for v in by_sku.values())),
        'conflict_fields': dict(Counter(x['field'] for x in conflicts)),
        'skus_with_any_field_difference': len({x['sku'] for x in conflicts}),
        'invalid_eans': sorted({x['fields']['Artikelcode'] for x in observations
                                if not ean13_valid(x['fields']['EAN'])}),
        'ean_collisions_across_different_skus': ean_collisions,
        'price_conflict_skus': sorted({x['sku'] for x in conflicts
                                      if x['field'] == 'Adviesverkoopprijs ex. Btw'}),
        'future_availability_unique_skus': sorted({x['fields']['Artikelcode'] for x in observations
                                                  if '1-2-2027' in x['fields']['Levertijd']}),
        'future_availability_count': len({x['fields']['Artikelcode'] for x in observations
                                         if '1-2-2027' in x['fields']['Levertijd']}),
        'readiness': 'SOURCE_AUDIT_ONLY_NOT_AN_IMPORT_OR_PUBLICATION_PLAN',
        'conflict_policy': 'No field precedence by file date; conflicting fields unresolved.',
    }
    for name, value in [('source-observations.json', observations), ('master.json', master),
                        ('conflicts.json', conflicts), ('summary.json', summary)]:
        (output_dir / name).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    # Semicolon CSV for Dutch Excel. EAN remains an identifier in JSON; import CSV as text.
    with (output_dir / 'Brauer-artikeloverzicht.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        headers = ['Artikelcode', 'Bronregels', 'Bronverschillen', *FIELDS[1:],
                   'Verkoopprijs_Badkamercity', 'Gereed_voor_import', 'Bronverwijzingen']
        writer = csv.DictWriter(stream, fieldnames=headers, delimiter=';')
        writer.writeheader()
        for p in master:
            row = p['fields'].copy()
            row.update({'Artikelcode': p['sku'], 'Bronregels': p['observations'],
                        'Bronverschillen': ' | '.join(p['conflict_fields']),
                        'Verkoopprijs_Badkamercity': '', 'Gereed_voor_import': 'Nee - bronanalyse',
                        'Bronverwijzingen': ' | '.join(f"{x['source_file']}:{x['source_sheet']}:{x['source_row']}"
                                                     for x in p['source_refs'])})
            writer.writerow(row)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    audit(args.sources, args.output)
