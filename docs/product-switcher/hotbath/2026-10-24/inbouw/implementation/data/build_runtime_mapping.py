"""Compile exact Hotbath body-addon routes from book and explicit merchant decisions.

This writes preview source/data only. It never calls Shopify or deletes products.
"""
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[1]
PRIOR = PROJECT / 'hotbath-inbouw-20261024'


def load(path):
    return json.loads(Path(path).read_text())


def numeric(gid):
    part = str(gid).rsplit('/', 1)[-1]
    assert part.isdigit(), gid
    return part


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fresh', type=Path, default=ROOT / 'fresh-products.json')
    ap.add_argument('--output-dir', type=Path, default=ROOT)
    args = ap.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    fresh = load(args.fresh)
    products = fresh.get('products', fresh.get('nodes', fresh.get('data', {}).get('nodes')))
    assert isinstance(products, list) and products, 'Expected fresh Shopify products list'
    by_id = {}
    by_sku = collections.defaultdict(list)
    for product in products:
        if product is None:
            continue
        assert product['id'] not in by_id, 'Duplicate fresh product ID'
        assert not product['variants']['pageInfo']['hasNextPage'], 'Variant pagination unfinished'
        by_id[product['id']] = product
        for variant in product['variants']['nodes']:
            by_sku[variant['sku']].append((product, variant))

    merchant = load(ROOT / 'merchant-decisions.json')
    original = load(PRIOR / 'book_mapping_review.json')
    finishes = load(ROOT / 'original-direct-finishes.json')
    finish_rows = finishes['mappings']
    finish_by_model = {row['trim_model']: row for row in finish_rows}
    assert len(finish_by_model) == 26
    original_candidates = []
    for model in original['mappings']:
        if model['current_trim_sku_match'] != 'DIRECT':
            continue
        finish = finish_by_model[model['trim_model']]
        assert finish['body_sku'] == model['body_sku']
        assert finish['visual_verified']
        for product in model['current_trim_products']:
            original_candidates.append({
                'trim_sku': product['sku'], 'trim_product_id': product['product_id'],
                'trim_model': model['trim_model'], 'body_sku': model['body_sku'],
                'source_kind': 'MANUFACTURER_BOOK_ORIGINAL_DIRECT',
                'source_pages': [s['printed_page'] for s in model['sources']],
                'source_finish_approved': product['sku'] in finish['approved_skus'],
            })

    expanded = load(PRIOR / 'expansion-consolidated.json')
    expansion_candidates = []
    for model in expanded['records']:
        for product in model['ready_skus']:
            expansion_candidates.append({
                **product, 'trim_model': model['trim_model'],
                'source_kind': 'MANUFACTURER_BOOK_EXPANSION',
                'source_pages': model['printed_pages'], 'source_finish_approved': True,
            })
    assert len(expansion_candidates) == 460
    merchant_candidates = [{
        **row, 'source_kind': 'MERCHANT_EXPLICIT_CONFIRMATION_2026-10-24',
        'source_pages': [], 'source_finish_approved': True,
    } for row in merchant['mapped_articles']]
    candidates = original_candidates + expansion_candidates + merchant_candidates
    assert len(candidates) == 722
    assert len({row['trim_sku'] for row in candidates}) == len(candidates)

    excluded = {row['trim_sku'] for row in merchant['excluded_articles']}
    assert len(excluded) == 70
    routes = []
    held = []
    for candidate in candidates:
        sku = candidate['trim_sku']
        body_sku = candidate['body_sku']
        reasons = []
        if sku in excluded:
            reasons.append('MERCHANT_NO_BODY_ADDON')
        if not candidate['source_finish_approved']:
            reasons.append('BOOK_FINISH_NOT_EXACTLY_CONFIRMED')
        if 'SPOM' in sku or 'SPOM' in body_sku or sku.startswith('IBS'):
            reasons.append('OUTSIDE_BODY_ADDON_SCOPE')
        trim_matches = by_sku.get(sku, [])
        body_matches = by_sku.get(body_sku, [])
        if len(trim_matches) != 1:
            reasons.append('TRIM_EXACT_SKU_NOT_UNIQUE_OR_MISSING')
        if len(body_matches) != 1:
            reasons.append('BODY_EXACT_SKU_NOT_UNIQUE_OR_MISSING')
        if len(trim_matches) == 1:
            product, variant = trim_matches[0]
            if product['id'] != candidate['trim_product_id']:
                reasons.append('TRIM_PRODUCT_ID_CHANGED')
            if len(product['variants']['nodes']) != 1:
                reasons.append('TRIM_REQUIRES_MULTIVARIANT_DESIGN')
            if product.get('vendor', '').strip().casefold() != 'hotbath':
                reasons.append('TRIM_VENDOR_MISMATCH')
            if product['status'] != 'ACTIVE' or not product.get('publishedAt') or not variant['availableForSale'] or float(variant['price']) <= 0:
                reasons.append('TRIM_NOT_CURRENTLY_SELLABLE')
            if (product.get('included') or {}).get('value') == 'true':
                reasons.append('TRIM_SAYS_BODY_ALREADY_INCLUDED')
            if 'SPOM' in (product['title'] + ' ' + product['handle']).upper():
                reasons.append('TRIM_SPOM_REFERENCE_EXCLUDED')
        if len(body_matches) == 1:
            body, body_variant = body_matches[0]
            if len(body['variants']['nodes']) != 1:
                reasons.append('BODY_REQUIRES_MULTIVARIANT_DESIGN')
            if body.get('vendor', '').strip().casefold() != 'hotbath':
                reasons.append('BODY_VENDOR_MISMATCH')
            if body['status'] != 'ACTIVE' or not body.get('publishedAt') or not body_variant['availableForSale'] or float(body_variant['price']) <= 0:
                reasons.append('BODY_NOT_CURRENTLY_SELLABLE')
            if body['id'] == candidate['trim_product_id']:
                reasons.append('SELF_RELATION')
        if reasons:
            held.append({**candidate, 'reasons': reasons})
            continue

        product, variant = trim_matches[0]
        body, body_variant = body_matches[0]
        for value in [sku, body_sku, product['handle'], body['handle']]:
            assert '|' not in value and '\n' not in value and '\r' not in value
        route = {
            'trim_model': candidate['trim_model'], 'trim_sku': sku,
            'trim_product_id': product['id'], 'trim_variant_id': variant['id'],
            'trim_handle': product['handle'], 'body_sku': body_sku,
            'body_product_id': body['id'], 'body_variant_id': body_variant['id'],
            'body_handle': body['handle'], 'quantity_per_trim': 1,
            'source_kind': candidate['source_kind'], 'source_pages': candidate['source_pages'],
        }
        routes.append(route)

    routes.sort(key=lambda row: int(numeric(row['trim_product_id'])))
    assert not (excluded & {row['trim_sku'] for row in routes})
    assert len({row['trim_product_id'] for row in routes}) == len(routes)
    assert len({row['trim_variant_id'] for row in routes}) == len(routes)

    lines = [
        '{%- comment -%}',
        'Exact verified Hotbath add-on routes. Generated; do not guess or broaden prefixes.',
        'Output: trimVariantId|trimSku|bodyHandle|bodySku|bodyVariantId|quantity.',
        'The purchase snippet must re-check exact IDs/SKUs and current Shopify availability.',
        '{%- endcomment -%}',
        '{%- case product.id -%}',
    ]
    for row in routes:
        value = '|'.join([
            numeric(row['trim_variant_id']), row['trim_sku'], row['body_handle'],
            row['body_sku'], numeric(row['body_variant_id']), '1',
        ])
        lines.append("{%- when " + numeric(row['trim_product_id']) + " -%}" + value)
    lines.append('{%- endcase -%}')
    liquid = '\n'.join(lines) + '\n'
    assert len(liquid.encode()) < 256000, 'Split route snippet before exceeding 256KB'
    (args.output_dir / 'bc-product-inbouw-data.liquid').write_text(liquid)

    summary = {
        'candidate_articles': len(candidates), 'ready_articles': len(routes),
        'ready_models': len({r['trim_model'] for r in routes}),
        'ready_by_source': dict(collections.Counter(r['source_kind'] for r in routes)),
        'held_articles': len(held), 'merchant_excluded_articles': len(excluded),
        'merchant_mapped_articles': len(merchant_candidates),
        'runtime_body_count': len({r['body_sku'] for r in routes}),
        'snippet_bytes': len(liquid.encode()), 'product_deletions': 0,
    }
    inputs = [args.fresh, ROOT / 'merchant-decisions.json', ROOT / 'original-direct-finishes.json', PRIOR / 'book_mapping_review.json', PRIOR / 'expansion-consolidated.json']
    output = {
        'schema': 'hotbath-body-addon-runtime-v1', 'date': '2026-10-24',
        'status': 'VALIDATED_DATA_FOR_PREVIEW_NOT_PUBLISHED',
        'summary': summary, 'mappings': routes, 'held': held,
        'merchant_exclusions': merchant['excluded_articles'],
        'input_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
        'price_policy': 'Read current linked Shopify product variant price at render/cart time; no prices in route.',
        'complete_set_policy': 'No IBS or explicit included-body records in this addon mapping.',
    }
    (args.output_dir / 'compiled-mapping.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(summary, indent=2))
    print('Held:', [(h['trim_sku'], h['reasons']) for h in held])


if __name__ == '__main__':
    main()
