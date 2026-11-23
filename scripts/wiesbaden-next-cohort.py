#!/usr/bin/env python3
"""Select only untouched, exactly matched Wiesbaden Shopify SKUs from a frozen source run.

Read-only. Never uploads products or touches the public shop. The selected SKUs
still require a product-specific source check and a fresh Shopify read/write gate.
"""
import argparse
import hashlib
import json
from collections import Counter
from datetime import date
from pathlib import Path
from zipfile import ZipFile


def select(source_zip: Path, register_json: Path, quotas: list[str], max_count: int) -> dict:
    registry = json.loads(register_json.read_text(encoding='utf-8'))
    groups = registry.get('groups', {})
    quarantined = [sku for v in groups.values() for sku in v['skus']]
    applied = registry.get('applied_2026_10_21', [])
    protected = registry.get('protected_skus', [])
    if len(quarantined) != len(set(quarantined)):
        raise ValueError('Duplicate SKU in quarantine register')
    if len(applied) != len(set(applied)):
        raise ValueError('Duplicate SKU in applied history')
    if set(quarantined) & set(applied + protected) or set(applied) & set(protected):
        raise ValueError('Quarantine/applied/protected groups overlap')
    if registry['total'] != len(quarantined):
        raise ValueError('Quarantine total does not match SKU list')
    skip = set(quarantined + applied + protected)
    wanted = []
    for term in quotas:
        kind, sep, count = term.rpartition(':')
        if not sep or not kind or not count.isdecimal() or int(count) < 1:
            raise ValueError(f'Invalid quota: {term!r}; expected Type:count')
        if kind in [q[0] for q in wanted]:
            raise ValueError(f'Duplicate type quota {kind!r}')
        wanted.append((kind, int(count)))
    if not wanted or sum(n for _, n in wanted) != max_count:
        raise ValueError('Quota totals must equal --count')
    with ZipFile(source_zip) as zipf:
        name = next((n for n in zipf.namelist() if n.endswith('/output/product-master.jsonl')), None)
        if name is None:
            raise ValueError('Source archive missing product-master.jsonl')
        raw = zipf.read(name)
    matches = []
    for line in raw.splitlines():
        item = json.loads(line)
        evidence = item.get('source_evidence') or {}
        if not (item.get('comparison_status') == 'EXISTING_WIESBADEN'
                and item.get('source_brand') == 'Wiesbaden'
                and item.get('current_vendor') == 'Wiesbaden'
                and item.get('product_id', '').startswith('gid://shopify/Product/')
                and item.get('variant_id', '').startswith('gid://shopify/ProductVariant/')
                and evidence.get('http_status') == 200
                and item.get('source_url', '').startswith('https://www.wiesbaden.nl/')):
            continue
        matches.append(item)
    counts = Counter(x['sku'] for x in matches)
    selected = []
    for kind, limit in wanted:
        eligible = sorted((p for p in matches if p['current_product_type'] == kind
                           and p['sku'] not in skip and counts[p['sku']] == 1), key=lambda p:p['sku'])
        if len(eligible) < limit:
            raise ValueError(f'Not enough fresh {kind}: {len(eligible)} < {limit}; nothing written')
        for x in eligible[:limit]:
            selected.append({'sku': x['sku'], 'product_id': x['product_id'],
                'variant_id': x['variant_id'], 'current_product_type': kind,
                'source_url': x['source_url'],
                'source_checked_at': x['source_evidence']['fetched_at'],
                'source_http_status': x['source_evidence']['http_status'],
                'proposal_status': 'NOT_REVIEWED_NO_WRITES'})
    if len(selected) != max_count or len({x['sku'] for x in selected}) != max_count:
        raise ValueError('Selection is not exactly the required number of unique SKUs')
    return {'schema': 'wiesbaden-read-only-next-cohort-v1', 'created_on': date.today().isoformat(),
            'source_name': source_zip.name, 'source_sha256': hashlib.sha256(source_zip.read_bytes()).hexdigest(),
            'registry_name': register_json.name, 'excluded_total': len(skip),
            'excluded_breakdown': {'quarantine': len(quarantined), 'applied': len(applied), 'protected': len(protected)},
            'quotas': dict(wanted), 'count': len(selected), 'read_only': True,
            'writes_confirmed': 0, 'selected': selected}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source', type=Path, required=True)
    ap.add_argument('--registry', type=Path, required=True)
    ap.add_argument('--quota', action='append', required=True, help='e.g. Hoofddouche:31; repeat per product type')
    ap.add_argument('--count', type=int, default=50)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    result = select(args.source, args.registry, args.quota, args.count)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    txt = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output.exists() and args.output.read_text(encoding='utf-8') == txt:
        print('Unchanged manifest: ' + str(args.output))
    else:
        args.output.write_text(txt, encoding='utf-8')
        print('Saved ' + str(args.output))
    print(f"Selected {result['count']} unique SKUs; excluded {result['excluded_total']} already handled")


if __name__ == '__main__':
    main()
