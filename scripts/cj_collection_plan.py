"""Plan missing memberships from verified Shopify fields; never writes to Shopify.

Input: JSON array of current product records with id, vendor, status,
source={type, value} and root/parent/opbouw/inbouw boolean membership flags.
Run: python scripts/cj_collection_plan.py export.json > plan.json
Re-read membership flags immediately before applying a plan. Do not run an old
plan directly: concurrent imports may have changed the shop.
"""
from __future__ import annotations
import json
import re
import sys
from typing import Any

TARGETS = {
    'root': 'gid://shopify/Collection/569428181258',
    'parent': 'gid://shopify/Collection/570058506506',
    'opbouw': 'gid://shopify/Collection/570059522314',
    'inbouw': 'gid://shopify/Collection/570059555082',
}
PATHS = {
    ('Kranen', 'Wastafelkranen', 'Opbouw wastafelkranen'): ('root', 'parent', 'opbouw'),
    ('Kranen', 'Wastafelkranen', 'Inbouw wastafelkranen'): ('root', 'parent', 'inbouw'),
}


def plan_products(products: list[dict[str, Any]]) -> dict[str, Any]:
    """Fail closed on missing identity, source or current membership evidence."""
    if not isinstance(products, list):
        raise ValueError('Expected a JSON array of current product records.')
    additions, unchanged, review = [], [], []
    seen: set[str] = set()
    for product in products:
        if not isinstance(product, dict):
            raise ValueError('Every product record must be an object.')
        pid = product.get('id')
        if not isinstance(pid, str) or not re.fullmatch(r'gid://shopify/Product/\d+', pid):
            raise ValueError('Invalid product GID; abort before generating a plan.')
        if pid in seen:
            raise ValueError(f'Duplicate product GID: {pid}')
        seen.add(pid)
        reason = None
        source = product.get('source')
        path = None
        if product.get('vendor') != 'Hotbath' or product.get('status') != 'ACTIVE':
            reason = 'Vendor or active status not verified.'
        elif not isinstance(source, dict) or source.get('type') != 'list.single_line_text_field':
            reason = 'Expected typed source_category_path is missing.'
        else:
            try:
                parsed = json.loads(source['value'])
                if not isinstance(parsed, list) or not all(isinstance(x, str) for x in parsed):
                    raise ValueError('Source path must be an array of strings.')
                path = tuple(parsed)
            except (KeyError, TypeError, ValueError):
                reason = 'Invalid source path.'
            if reason is None and path not in PATHS:
                reason = 'Source path is outside this reviewed mapping.'
        if reason is None:
            keys = PATHS[path]
            if any(type(product.get(k)) is not bool for k in keys):
                reason = 'Current membership evidence is incomplete.'
        if reason:
            review.append({'productId': pid, 'reason': reason})
            continue
        missing = [TARGETS[k] for k in keys if product[k] is False]
        if missing:
            additions.append({'productId': pid, 'source_path': list(path), 'add_to': missing})
        else:
            unchanged.append(pid)
    return {'mode': 'PLAN_ONLY', 'store': 'fpa9hu-i3.myshopify.com',
            'additions': additions, 'unchanged': unchanged, 'review': review,
            'membership_additions': sum(len(x['add_to']) for x in additions)}


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python scripts/cj_collection_plan.py export.json', file=sys.stderr)
        return 2
    try:
        with open(sys.argv[1], encoding='utf-8') as source:
            result = plan_products(json.load(source))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
