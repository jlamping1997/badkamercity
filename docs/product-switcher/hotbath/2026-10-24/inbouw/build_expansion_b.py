import json, re
from pathlib import Path
from collections import Counter

ROOT = Path('/workspace/scratch/6866aa3baeaf')
BASE = ROOT / 'hotbath-inbouw-20261024'
pages = json.loads((ROOT / 'hotbath-menu-20261024/book_pages.json').read_text())
snapshot = json.loads((ROOT / 'hotbath-menu-20261024/catalog_snapshot.json').read_text())
live = json.loads((BASE / 'expansion-live-products.json').read_text())
pairs = json.loads((BASE / 'expansion-b-pairs.json').read_text())
old = {m['trim_model'] for m in json.loads((BASE / 'book_mapping_review.json').read_text())['mappings']}
sku_index = {}
for p in snapshot['products']:
    for v in p['variants']['nodes']:
        sku_index.setdefault(v['sku'], []).append((p, v))
live_index = {v['sku']: (p, v) for p in live['products'] for v in p['variants']['nodes']}
known_finishes = set('CR GN BB AB WH AI PBP MBP BBP BCP BGP BL'.split())
rows = []
exceptions = [{
    'type': 'CATALOGUE_CODE_INCONSISTENCY', 'printed_page': 254, 'pdf_page': 256,
    'book_code': 'GLF0011EXT', 'likely_model': 'GLF011EXT',
    'note': 'Table literally says GLF0011EXT, heading GLF011. Existing original mapping for GLF011EXT is based on a separate explicit table on page358. Do not count this spelling as a new model or invent a matching shop SKU.'
}]
for pair in pairs:
    book_model, body = pair['trim'], pair['body']
    if book_model == 'GLF0011EXT':
        continue
    model = 'GL177EXT' if book_model == 'GL177' else book_model
    assert model not in old
    finish_set = set()
    evidence = []
    for printed in pair['pages']:
        text = pages[printed + 1]['text']
        pattern = r'Inbouwdeel\s+' + re.escape(body) + r'\s+Afbouwdeel\s+' + re.escape(book_model) + r'\.*\s+Totaal'
        hit = re.search(pattern, text)
        assert hit, (printed, model, body)
        end = text.find('Finish', hit.end())
        table_tail = text[hit.end():end if end >= 0 else None]
        finish_set.update(set(re.findall(r'\b[A-Z]{2,3}\b', table_tail)) & known_finishes)
        evidence.append({'printed_page': printed, 'pdf_page': printed + 2,
                         'exact_table_header': re.sub(r'\s+', ' ', hit.group(0)),
                         'visual_verified': True})
    notes = []
    status = 'VERIFIED_BOOK'
    match_type = 'DIRECT'
    selection_required = False
    if model == 'GL177EXT':
        assert 'GL177EXT...' in pages[250]['text']
        notes.append('Table uses GL177..; same-page drawing explicitly labels the upper trim GL177EXT... and lower rough-in HBCB177. Full page visually verified. This resolves the table abbreviation without a guessed alias.')
    if model == 'CB010H/CEXT':
        match_type = 'ALIAS_REVIEW'
        status = 'REVIEW'
        notes.append('Manufacturer combined H/C notation. No exact trim SKU in snapshot. Separate HBCB010H and HBCB010C products exist; do not treat HBCB010H/C as an orderable SKU or auto-resolve to either.')
    if model == 'CB7001EXT':
        status = 'REVIEW'
        selection_required = True
        notes.append('Same trim explicitly works with two different rough-ins: HBCB7001H horizontal, HBCB7001V vertical. These are alternatives, not parts to buy together. A horizontal/vertical choice is required; no single-body automatic mapping.')
    candidate_skus = sorted(s for s in sku_index if s.startswith(model) and s[len(model):] in known_finishes)
    matched_skus = sorted(s for s in candidate_skus if s[len(model):] in finish_set)
    other_finishes = sorted(set(candidate_skus) - set(matched_skus))
    body_rows = sku_index.get(body, [])
    body_matches = [v['sku'] for p, v in body_rows]
    body_valid = len(body_rows) == 1 and body_rows[0][0]['status'] == 'ACTIVE' and bool(body_rows[0][0].get('publishedAt'))
    if not body_valid and status != 'REVIEW':
        status = 'MISSING_BODY'
        notes.append('Exact rough-in SKU absent or not uniquely active/published in full earlier snapshot. Fresh exact-SKU search still required before stating absent from the live store.')
    if not matched_skus:
        notes.append('No exact book-finish trim SKU matched in snapshot; source relationship retained for coverage, not rollout.')
    live_conflicts = [s for s in matched_skus if s in live_index and (live_index[s][0].get('included') or {}).get('value') == 'true']
    deployment_hold = bool(live_conflicts)
    if live_conflicts:
        notes.append('Fresh Shopify data says inbouwdeel included for ' + ', '.join(live_conflicts) + '. Hold these SKUs for sale-content/data review to avoid charging twice. Manufacturer relationship remains proven. Other exact book-finish SKUs remain candidates when no included flag conflict exists.')
    ready_skus = [s for s in matched_skus if s not in live_conflicts] if status == 'VERIFIED_BOOK' and body_valid else []
    rows.append({
        'trim_model': model, 'book_trim_model': model if model == 'GL177EXT' else book_model,
        'book_table_model': book_model, 'body_sku': body, 'qty': 1,
        'printed_pages': pair['pages'], 'pdf_pages': [p + 2 for p in pair['pages']],
        'evidence': evidence, 'match_type': match_type,
        'book_finishes': sorted(finish_set), 'candidate_skus': candidate_skus,
        'matched_skus': matched_skus, 'unlisted_finish_skus': other_finishes,
        'approved_skus': ready_skus, 'body_catalog_skus': body_matches,
        'body_unique_active_published_snapshot': body_valid,
        'status': status, 'selection_required': selection_required,
        'live_included_flag_conflicts': live_conflicts,
        'deployment_data_review': deployment_hold, 'notes': notes, 'visual_verified': True,
    })
    if other_finishes:
        exceptions.append({'type': 'UNLISTED_FINISH_HOLD', 'trim_model': model,
                           'skus': other_finishes, 'printed_pages': pair['pages'],
                           'note': 'Existing trim SKU finish not listed in the cited manufacturer price table; no automatic scope expansion.'})

unique = lambda field, predicate=lambda r: True: sorted({s for r in rows if predicate(r) for s in r[field]})
report = {
    'schema': 'hotbath-inbouw-expansion-part-b-v1', 'read_only': True,
    'source_pdf': str(ROOT / 'upload/Hotbath%20Catalogus%20Editie%2018.pdf'),
    'source_snapshot': str(ROOT / 'hotbath-menu-20261024/catalog_snapshot.json'),
    'source_live_candidate_read': str(BASE / 'expansion-live-products.json'),
    'coverage': {'printed_page_from': 170, 'printed_page_to': 329,
                 'pdf_page_from': 172, 'pdf_page_to': 331,
                 'method': 'Searched all160 extracted pages for inbouwdeel, afbouwdeel, afdekset, apart bestellen, exclusief, EXT; extracted explicit price-table pairs; visually verified EVERY new pair header in four contact sheets and full exceptional pages190/249. IBS complete-set lists excluded from paid addon relations.',
                 'header_contact_sheets': [f'expansion-b-headers-{i}.png' for i in range(1,5)],
                 'full_page_visuals': ['expansion-b-page190.png','expansion-b-page249.png'],
                 'limits': 'Body existence is full earlier snapshot, not full live vendor scan. Fresh live read is candidate-ID scope. Product/variant availability must be refreshed before deployment. No storefront changes.'},
    'summary': {
        'new_relation_rows': len(rows), 'new_unique_models': len({r['trim_model'] for r in rows}),
        'new_candidate_unique_skus': len(unique('candidate_skus')),
        'new_book_finish_unique_skus': len(unique('matched_skus')),
        'new_simple_ready_models_snapshot': len({r['trim_model'] for r in rows if r['approved_skus']}),
        'new_simple_ready_unique_skus_snapshot': len(unique('approved_skus')),
        'status_rows': dict(Counter(r['status'] for r in rows)),
        'unlisted_finish_unique_skus': len(unique('unlisted_finish_skus')),
        'live_included_flag_conflict_skus': len(unique('live_included_flag_conflicts')),
        'no_matching_trim_models': sorted({r['trim_model'] for r in rows if not r['matched_skus']}),
    },
    'mappings': rows, 'exceptions': exceptions,
}
(BASE / 'expansion-b.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report['summary'], ensure_ascii=False, indent=2))
