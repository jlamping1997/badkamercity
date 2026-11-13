"""Read-only publication gate for planned Cottoceramix products and Admin readbacks."""

import argparse
import json
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
from pathlib import Path


OPTIONAL_COTTO_METAFIELDS = {
    ('tiles', 'color'), ('tiles', 'execution'), ('tiles', 'size'),
    ('custom', 'kleur'), ('custom', 'afwerking'), ('custom', 'serie'),
    ('custom', 'afmetingen_original'), ('bc_filters', 'kleur'),
    ('bc_filters', 'afwerking'), ('bc_filters', 'glansgraad'), ('bc_filters', 'serie'),
    ('bc_filters', 'tegel_dikte_mm'), ('bc_filters', 'tegel_lengte_mm'),
    ('bc_filters', 'tegel_breedte_mm'),
}


class HTMLTokens(HTMLParser):
    VOID_ELEMENTS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tokens = []

    def handle_starttag(self, tag, attrs):
        self.tokens.append(('void' if tag in self.VOID_ELEMENTS else 'start', tag, tuple(sorted(attrs, key=lambda item: item[0]))))

    def handle_startendtag(self, tag, attrs):
        self.tokens.append(('void' if tag in self.VOID_ELEMENTS else 'selfclose', tag, tuple(sorted(attrs, key=lambda item: item[0]))))

    def handle_endtag(self, tag):
        self.tokens.append(('end', tag))

    def handle_data(self, data):
        if self.tokens and self.tokens[-1][0] == 'text':
            self.tokens[-1] = ('text', self.tokens[-1][1] + data)
        elif data:
            self.tokens.append(('text', data))

    def handle_comment(self, data):
        self.tokens.append(('comment', data))

    def handle_decl(self, decl):
        self.tokens.append(('decl', decl))

    def unknown_decl(self, data):
        self.tokens.append(('unknown_decl', data))

    def handle_entityref(self, name):
        self.tokens.append(('entity', name))

    def handle_charref(self, name):
        self.tokens.append(('charref', name))


def html_equal(actual, expected):
    if not isinstance(actual, str) or not isinstance(expected, str):
        return False
    try:
        first, second = HTMLTokens(), HTMLTokens()
        first.feed(actual)
        first.close()
        second.feed(expected)
        second.close()
        return first.tokens == second.tokens
    except (ValueError, AssertionError):
        return False


def nodes(value):
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        if isinstance(value.get('nodes'), list):
            return value['nodes']
        if isinstance(value.get('edges'), list):
            return [edge.get('node') for edge in value['edges'] if edge.get('node')]
    return []


def products_in(value):
    found = defaultdict(list)
    def walk(item):
        if isinstance(item, dict):
            if str(item.get('id', '')).startswith('gid://shopify/Product/') and 'variants' in item:
                found[item['id']].append(item)
                return
            if item.get('type') == 'text' and isinstance(item.get('text'), str):
                try:
                    walk(json.loads(item['text']))
                except ValueError:
                    pass
            for child in item.values():
                walk(child)
        elif isinstance(item, list):
            for child in item:
                walk(child)
    walk(value)
    unique, conflicting = [], []
    for identity, records in found.items():
        first = records[0]
        if any(record != first for record in records[1:]):
            conflicting.append(identity)
        unique.append(first)
    return unique, conflicting


def decimal_equal(actual, expected):
    try:
        return Decimal(str(actual)) == Decimal(str(expected))
    except InvalidOperation:
        return False


def metafield_equal(actual, expected):
    if actual.get('type') != expected['type']:
        return False
    if expected['type'] == 'json' or expected['type'].startswith('list.'):
        try:
            return json.loads(actual.get('value', '')) == json.loads(expected['value'])
        except (ValueError, TypeError):
            return False
    if expected['type'].startswith('number_'):
        return decimal_equal(actual.get('value'), expected['value'])
    return actual.get('value') == expected['value']


def verify(plans, readback, active_skus=None, require_group_refs=False):
    if isinstance(plans, dict):
        plans = plans.get('products', [])
    active_skus = set(active_skus or [])
    if len({plan['sku'] for plan in plans}) != len(plans):
        raise ValueError('Planned SKU identities must be unique')
    actual_products, conflicting_ids = products_in(readback)
    by_sku = defaultdict(list)
    for product in actual_products:
        for variant in nodes(product.get('variants')):
            if variant.get('sku'):
                by_sku[variant['sku']].append(product)
    expected_groups = defaultdict(list)
    for plan in plans:
        expected_groups[plan['group_key']].append(plan['sku'])
    checks, errors, unconfirmed_weight_skus = Counter(), [], []
    def record(sku, field, condition, actual=None, expected=None):
        checks[field] += 1
        if not condition:
            errors.append({'sku': sku, 'field': field, 'actual': actual, 'expected': expected})
    for plan in plans:
        sku, expected = plan['sku'], plan['input']
        records = by_sku.get(sku, [])
        record(sku, 'identity.unique_product', len(records) == 1, len(records), 1)
        if len(records) != 1:
            continue
        actual = records[0]
        record(sku, 'identity.consistent_readback', actual['id'] not in conflicting_ids, actual['id'])
        for field in ['title', 'handle', 'vendor', 'productType', 'templateSuffix', 'seo']:
            record(sku, 'product.' + field, actual.get(field) == expected.get(field), actual.get(field), expected.get(field))
        record(sku, 'product.descriptionHtml', html_equal(actual.get('descriptionHtml'), expected.get('descriptionHtml')), actual.get('descriptionHtml'), expected.get('descriptionHtml'))
        desired_status = 'ACTIVE' if sku in active_skus else expected.get('status', 'DRAFT')
        record(sku, 'product.status', actual.get('status') == desired_status, actual.get('status'), desired_status)
        record(sku, 'product.tags', sorted(actual.get('tags', [])) == sorted(expected.get('tags', [])), actual.get('tags'), expected.get('tags'))
        option_values = [{'name': item.get('name'), 'values': item.get('values') if 'values' in item else [value.get('name') for value in nodes(item.get('optionValues'))]} for item in actual.get('options', [])]
        record(sku, 'product.options', option_values == [{'name': 'Title', 'values': ['Default Title']}], option_values)
        for field in ['variants', 'metafields', 'media', 'collections']:
            connection = actual.get(field)
            record(sku, 'readback.' + field + '_present', connection is not None)
            if isinstance(connection, dict) and 'pageInfo' in connection:
                record(sku, 'readback.' + field + '_complete', connection['pageInfo'].get('hasNextPage') is False, connection['pageInfo'])
        variants = nodes(actual.get('variants'))
        record(sku, 'variant.count', len(variants) == 1, len(variants), 1)
        if len(variants) == 1:
            got, wanted = variants[0], expected['variants'][0]
            for field in ['sku', 'taxable', 'inventoryPolicy', 'showUnitPrice']:
                record(sku, 'variant.' + field, got.get(field) == wanted[field], got.get(field), wanted[field])
            record(sku, 'variant.price', decimal_equal(got.get('price'), wanted['price']), got.get('price'), wanted['price'])
            measurement = got.get('unitPriceMeasurement') or {}
            desired_measurement = wanted.get('unitPriceMeasurement')
            if desired_measurement is not None:
                for field in ['quantityUnit', 'referenceUnit']:
                    record(sku, 'unit_price.' + field, measurement.get(field) == desired_measurement[field], measurement.get(field), desired_measurement[field])
                for field in ['quantityValue', 'referenceValue']:
                    record(sku, 'unit_price.' + field, decimal_equal(measurement.get(field), desired_measurement[field]), measurement.get(field), desired_measurement[field])
            else:
                unconfigured = not measurement.get('quantityUnit') and not measurement.get('referenceUnit') and all(measurement.get(field) is None or decimal_equal(measurement.get(field), 0) for field in ['quantityValue', 'referenceValue'])
                record(sku, 'unit_price.not_configured', unconfigured, measurement, 'no reference-unit measurement configured for native piece/pack/set')
            selected = got.get('selectedOptions')
            record(sku, 'variant.selected_options', selected == [{'name': 'Title', 'value': 'Default Title'}], selected)
            if 'barcodes' in got:
                barcodes = nodes(got['barcodes']) if isinstance(got['barcodes'], dict) else got['barcodes']
                values = sorted((entry.get('type'), entry.get('value')) for entry in barcodes)
                desired = sorted((entry['type'], entry['value']) for entry in wanted.get('barcodes', []))
                record(sku, 'variant.barcodes', values == desired, values, desired)
            else:
                barcode = got.get('barcode')
                desired = wanted.get('barcodes', [{}])[0].get('value')
                record(sku, 'variant.barcode_read', 'barcode' in got)
                record(sku, 'variant.barcode', (barcode or None) == desired, barcode, desired)
            inventory = got.get('inventoryItem') or {}
            for field in ['tracked', 'requiresShipping']:
                record(sku, 'inventory.' + field, inventory.get(field) == wanted['inventoryItem'][field], inventory.get(field), wanted['inventoryItem'][field])
            weight = (inventory.get('measurement') or {}).get('weight') or {}
            desired_weight = (wanted['inventoryItem'].get('measurement') or {}).get('weight')
            if desired_weight is not None:
                record(sku, 'weight.unit', weight.get('unit') == desired_weight['unit'], weight.get('unit'), desired_weight['unit'])
                record(sku, 'weight.value', decimal_equal(weight.get('value'), desired_weight['value']), weight.get('value'), desired_weight['value'])
            else:
                # A new Shopify variant can expose a zero-valued platform default
                # after the input omitted weight. That is not a verified physical
                # weight and must not be promoted into a displayed specification.
                unconfirmed_weight_skus.append(sku)
                value = weight.get('value')
                record(sku, 'weight.platform_default_only', value is None or decimal_equal(value, 0), value, 'absent or zero platform default; physical weight remains unknown')
        actual_meta = {(m.get('namespace'), m.get('key')): m for m in nodes(actual.get('metafields'))}
        expected_meta = {(m['namespace'], m['key']): m for m in expected['metafields']}
        for wanted in expected['metafields']:
            got = actual_meta.get((wanted['namespace'], wanted['key']))
            record(sku, 'metafield.' + wanted['namespace'] + '.' + wanted['key'], got is not None and metafield_equal(got, wanted), got.get('value') if got else None, wanted['value'])
        if expected.get('vendor') == 'Cottoceramix':
            for namespace, key in sorted(OPTIONAL_COTTO_METAFIELDS - set(expected_meta)):
                record(sku, 'metafield.absent.' + namespace + '.' + key, (namespace, key) not in actual_meta, actual_meta.get((namespace, key)), 'absent; source fact not supplied')
        if sku in unconfirmed_weight_skus:
            try:
                tile = json.loads(actual_meta[('custom', 'bron_toelichtingen_json')]['value'])['tiles']
                specs = json.loads(actual_meta[('custom', 'complete_specificaties')]['value'])
                weight_items = [item for group in specs for item in group.get('items', [])
                                if 'gewicht' in str(item.get('key', '')).lower()
                                or 'weight' in str(item.get('key', '')).lower()
                                or 'gewicht' in str(item.get('label', '')).lower()
                                or 'weight' in str(item.get('label', '')).lower()]
                omitted = not {'weight_kg_per_box', 'weight_kg_per_unit'} & set(tile) and not weight_items
            except (KeyError, ValueError, TypeError, AttributeError):
                omitted = False
            record(sku, 'weight.sourced_display_absent', omitted, expected='no weight field in tile contract or displayed specs')
        desired_collection_ids = set(expected.get('collections', []))
        actual_collection_ids = {collection.get('id') for collection in nodes(actual.get('collections'))}
        record(sku, 'collections.expected_membership', desired_collection_ids <= actual_collection_ids, sorted(actual_collection_ids), sorted(desired_collection_ids))
        media = nodes(actual.get('media'))
        wanted_files = expected.get('files', [])
        record(sku, 'media.count', len(media) == len(wanted_files), len(media), len(wanted_files))
        record(sku, 'media.unique_ids', len({item.get('id') for item in media}) == len(media) and all(item.get('id') for item in media))
        for index, item in enumerate(media):
            record(sku, 'media.ready', item.get('status') == 'READY', item.get('status'), 'READY')
            record(sku, 'media.image_type', item.get('mediaContentType') == 'IMAGE', item.get('mediaContentType'), 'IMAGE')
            record(sku, 'media.url', str((item.get('image') or {}).get('url', '')).startswith('https://'))
            if index < len(wanted_files):
                alt = item.get('alt') if 'alt' in item else (item.get('image') or {}).get('altText')
                record(sku, 'media.alt_order', alt == wanted_files[index]['alt'], alt, wanted_files[index]['alt'])
        if require_group_refs:
            got = actual_meta.get(('tiles', 'group_products')) or {}
            try:
                references = json.loads(got.get('value', ''))
            except (ValueError, TypeError):
                references = []
            wanted_ids = [by_sku[member][0]['id'] for member in expected_groups[plan['group_key']] if len(by_sku.get(member, [])) == 1]
            record(sku, 'menu.complete_references', len(wanted_ids) == len(expected_groups[plan['group_key']]) and len(references) == len(set(references)) and set(references) == set(wanted_ids), references, wanted_ids)
    group_failures = defaultdict(list)
    sku_group = {plan['sku']: plan['group_key'] for plan in plans}
    for error in errors:
        group_failures[sku_group[error['sku']]].append(error)
    groups = [{'group_key': key, 'skus': skus, 'readback_pass': key not in group_failures, 'failure_count': len(group_failures.get(key, []))} for key, skus in sorted(expected_groups.items())]
    blocked_groups = [group for group in groups if not group['readback_pass']]
    return {'status': 'PASS' if not errors else 'HOLD', 'planned_products': len(plans), 'readback_products': len(actual_products), 'checks': sum(checks.values()), 'checks_by_field': dict(checks), 'failure_count': len(errors), 'errors': errors, 'groups': groups, 'blocked_groups': blocked_groups, 'readback_pass_skus': [sku for group in groups if group['readback_pass'] for sku in group['skus']], 'unconfirmed_physical_weight_skus': unconfirmed_weight_skus, 'scope': 'Exact planned Admin field and media readiness comparison only. Absent/zero platform-default weight does not verify physical weight. Source correctness, publication channels, checkout and visual image identity are independent gates.', 'writes_performed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--planned', type=Path, required=True)
    parser.add_argument('--readback', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--active-skus', type=Path)
    parser.add_argument('--require-group-refs', action='store_true')
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    destination = args.output.resolve()
    if destination == repo or repo in destination.parents:
        parser.error('Private readback reports must be written outside the public Git worktree')
    load = lambda file: json.loads(file.read_text())
    result = verify(load(args.planned), load(args.readback), load(args.active_skus) if args.active_skus else None, args.require_group_refs)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({key: result[key] for key in ['status', 'planned_products', 'readback_products', 'checks', 'failure_count', 'writes_performed']}))
    raise SystemExit(0 if result['status'] == 'PASS' else 2)


if __name__ == '__main__':
    main()
