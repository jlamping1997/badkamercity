"""Resume from saved typed records; never replace them from an empty raw folder.

Anonymous fetch responses are reduced to the literal technical-table excerpt.
Only enrich_retail_specifications decides whether exact identity permits a fact.
"""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from retail_extract import parse


class TextNodes(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style'}:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.skip = max(0, self.skip - 1)

    def handle_data(self, value):
        text = re.sub(r'\s+', ' ', value).strip()
        if text and not self.skip:
            self.nodes.append(text)


def technical_page(result, target):
    parser = TextNodes()
    parser.feed(result['text'])
    nodes = parser.nodes
    identity = next((i for i, x in enumerate(nodes) if x in {'Fabrikantnummer', 'Leveranciernummer'}), None)
    if identity is None:
        return None
    starts = [i for i, x in enumerate(nodes[:identity]) if x == 'Specificaties']
    if not starts:
        return None
    start = starts[-1]
    end = next((i for i in range(identity + 1, len(nodes)) if nodes[i] in {'Bijlagen', 'Technische documenten', 'Ervaringen met dit product'}), len(nodes))
    excerpt = nodes[start:end]
    return {
        'title': result.get('title', ''),
        'url': result.get('final_url') or result['url'],
        'requested_url': target['url'],
        'requested_sku': target['sku'],
        'ref': 'public-fetch:' + target['url'],
        'retrieval': 'public_live_fetch_html',
        'checked_on': '2026-11-08',
        'source_snapshot_note': 'Fresh anonymous public HTML extraction, 2026-11-08; no source revision guarantee',
        'lines': [{'line': i + 1, 'text': text} for i, text in enumerate(excerpt)],
        'linked_documents': [],
    }


def typed_record(page):
    record = parse(page)
    record['checked_on'] = '2026-11-08'
    return record


def merge_records(*groups):
    if not groups or not groups[0]:
        raise ValueError('Existing typed source records are required')
    merged = {}
    for group in groups:
        for record in group:
            if not record.get('url'):
                raise ValueError('Typed source record without source URL')
            merged[record['url']] = record
    return list(merged.values())


def main():
    root = Path('prepared')
    original = json.loads((root / 'retail-observations.json').read_text())
    pending = json.loads((root / 'retail-observations-pending.json').read_text())
    target_path = root / 'retail-lookup-resume-targets.json'
    if not target_path.exists():
        target_path = root / 'retail-lookup-pending.json'
    targets = {r['url']: r for r in json.loads(target_path.read_text())}
    pages, records, outcomes = [], [], []
    response_files = sorted(Path('research/brauer-retail').glob('retry-fetch-*.json'))
    if not response_files and (root / 'retail-observations-resumed.json').exists():
        records = json.loads((root / 'retail-observations-resumed.json').read_text())
        outcomes = json.loads((root / 'retail-resume-outcomes.json').read_text())
        excerpt_path = Path('research/brauer-retail/table-excerpts-resumed.json')
        if excerpt_path.exists():
            pages = json.loads(excerpt_path.read_text())
    for file in response_files:
        response = json.loads(file.read_text())
        for result in response.get('results', []):
            target = targets[result['url']]
            page = technical_page(result, target)
            record = typed_record(page) if page else None
            outcome = {'sku': target['sku'], 'ean': target['ean'], 'url': target['url'], 'file': file.name,
                       'state': 'TECHNICAL_TABLE_SAVED' if record else 'NO_TECHNICAL_TABLE', 'checked_on': '2026-11-08'}
            if record:
                pages.append(page)
                records.append(record)
                outcome['identity_exact'] = record['sku'] == target['sku'] and record['ean'] == target['ean'] and str(record['brand']).lower() == 'brauer'
                outcome['fields'] = len(record['fields'])
            outcomes.append(outcome)
        for error in response.get('errors', []):
            outcomes.append({'url': error.get('url'), 'state': 'FETCH_ERROR', 'error': error, 'file': file.name, 'checked_on': '2026-11-08'})
    merged = merge_records(original, pending, records)
    for name, obj in [('retail-observations.json', merged), ('retail-observations-resumed.json', records), ('retail-resume-outcomes.json', outcomes)]:
        (root / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    Path('research/brauer-retail/table-excerpts-resumed.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'existing': len(original), 'pending': len(pending), 'resumed': len(records), 'merged': len(merged), 'outcomes': len(outcomes)}))


if __name__ == '__main__':
    main()
