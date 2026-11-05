"""Create a private, deterministic draft plan. This module makes no network writes."""

import argparse
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from urllib.parse import urlsplit


APPLICATIONS = {
    'Tegels > Vloertegels': ('Vloertegel', 'Vloertegels'),
    'Tegels > Wandtegels': ('Wandtegel', 'Wandtegels'),
    'Tegels > Mozaïek': ('Mozaïek', 'Mozaïektegels'),
}
BLOCK_FLAGS = {
    'missing_current_feed', 'missing_official_series', 'missing_official_color',
    'missing_finish', 'nonbinary_finish', 'missing_size', 'missing_weight',
    'weight_conflict', 'separate_non_m2_order_path', 'missing_box_price_basis',
}
FEED_FIELDS = ['supplier_stock', 'delivery_time', 'orderable', 'feed_checked_at']
PROTECTED_FIELDS = [
    'title', 'vendor', 'handle', 'descriptionHtml', 'seo', 'menu_relationships',
    'manual_box_corrections', 'manual_price_corrections', 'manual_finish_corrections',
]


def decimal(value):
    try:
        return Decimal(str(value).replace(',', '.'))
    except (InvalidOperation, ValueError, TypeError):
        return None


def positive(value):
    value = decimal(value)
    return value if value is not None and value.is_finite() and value > 0 else None


def money(value):
    return str(Decimal(str(value)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


def slug(value):
    value = unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')


def public_url(value):
    parsed = urlsplit(str(value or ''))
    return parsed.scheme == 'https' and parsed.hostname in {'cottoceramix.nl', 'www.cottoceramix.nl'} and not parsed.query and not parsed.username


def image_transport_source(value):
    """Use the proven JPEG route without rewriting the source photo identity."""
    if not isinstance(value, str):
        return value
    try:
        parsed = urlsplit(value)
        trusted = (parsed.scheme == 'https' and parsed.hostname in {'cottoceramix.nl', 'www.cottoceramix.nl'}
                   and parsed.username is None and parsed.password is None and parsed.port in {None, 443})
    except ValueError:
        return value
    prefix = re.match(r'https://[^/?#]+', value, re.I)
    if not trusted or not prefix or not parsed.path.startswith('/resize/'):
        return value
    start, end = prefix.end(), prefix.end() + len(parsed.path)
    if value[start:end] != parsed.path:
        return value
    path = re.sub(r'\.JPG(?=/|$)', '.jpg', parsed.path)
    return value[:start] + path + value[end:]


def valid_ean(value):
    value = str(value or '')
    return len(value) == 13 and value.isdigit() and sum(int(v) * (1 if i % 2 == 0 else 3) for i, v in enumerate(value)) % 10 == 0


def group_key(row):
    return str(row.get('original_brand') or '') + '|' + str(row.get('series') or '')


def normalized_finish(row):
    return {'mat': 'Mat', 'glans': 'Glans', 'glanzend': 'Glans'}.get(str(row.get('finish') or '').strip().lower())


def chosen_dimensions(row):
    value = str(row.get('size') or '').strip()
    match = re.fullmatch(r'(\d+(?:[.,]\d+)?)\s*[x×]\s*(\d+(?:[.,]\d+)?)\s*(?:cm)?', value, re.I)
    if match:
        return tuple(positive(part) for part in match.groups())
    return positive(row.get('length_cm')), positive(row.get('width_cm'))


def chosen_thickness(row):
    value = str(row.get('thickness') or '').strip()
    match = re.fullmatch(r'(\d+(?:[.,]\d+)?)\s*mm', value, re.I)
    if match:
        return positive(match.group(1))
    if value:
        return None
    return positive((row.get('raw_workbook') or {}).get('AE'))


def choice_tuple(row):
    return (APPLICATIONS.get(row.get('category'), ('',))[0], str(row.get('color') or ''), normalized_finish(row), str(row.get('size') or ''), str(chosen_thickness(row)))


def row_blockers(row):
    reasons = set(row.get('flags', [])) & BLOCK_FLAGS
    if not row.get('m2_mode') or row.get('sale_method') != 'Doos':
        reasons.add('separate_non_m2_order_path')
    if row.get('category') not in APPLICATIONS:
        reasons.add('unmapped_product_application')
    for field in ['m2_per_box', 'pieces_per_box', 'unit_price', 'box_price', 'weight_kg_candidate']:
        if positive(row.get(field)) is None:
            reasons.add('missing_positive_' + field)
    length, width = chosen_dimensions(row)
    if length is None or width is None:
        reasons.add('missing_positive_chosen_dimensions')
    if chosen_thickness(row) is None:
        reasons.add('missing_positive_chosen_thickness')
    units = positive(row.get('pieces_per_box'))
    if units is not None and units != units.to_integral_value():
        reasons.add('noninteger_pieces_per_box')
    area, price, total = (positive(row.get(f)) for f in ['m2_per_box', 'unit_price', 'box_price'])
    if area is not None and price is not None and total is not None and money(area * price) != money(total):
        reasons.add('box_price_reconcile_error')
    if not normalized_finish(row):
        reasons.add('unconfirmed_finish')
    if not public_url(row.get('source_url')):
        reasons.add('untrusted_or_private_product_url')
    images = (row.get('live') or {}).get('images') or []
    if not images:
        reasons.add('missing_product_image')
    elif any(not public_url(url) for url in images):
        reasons.add('untrusted_or_private_image_url')
    if not row.get('source_name') or not row.get('sku') or not row.get('series') or not row.get('color'):
        reasons.add('missing_identity_or_choice')
    return sorted(reasons)


def evidence_map(evidence, rows):
    result = {}
    known = {row['sku'] for row in rows}
    for item in evidence or []:
        if item.get('verified') is not True or not item.get('group_key'):
            raise ValueError('Menu evidence must explicitly be verified and have a group_key')
        if not item.get('source_urls') or any(not public_url(url) for url in item['source_urls']):
            raise ValueError('Menu evidence must have public Cottoceramix product URLs')
        skus = item.get('skus')
        if not skus or len(skus) != len(set(skus)) or not set(skus) <= known:
            raise ValueError('Evidence needs an exact, unique known SKU set')
        for sku in skus:
            if sku in result:
                raise ValueError('A SKU belongs to more than one verified menu group: ' + sku)
            result[sku] = item
    return result


def availability(row):
    live = row.get('live') or {}
    fields = live.get('fields') or {}
    overrides = row.get('manual_overrides') or {}
    confirmed = str(row.get('availability_import') or '').strip()
    manual = bool(overrides.get('availability'))
    stock = decimal(row.get('stock_snapshot') if manual else fields.get('stock_level'))
    if manual and confirmed:
        lead = confirmed
    elif stock is not None and stock > 0:
        lead = 'Op voorraad bij leverancier'
    else:
        lead = str(fields.get('delivery_time') or confirmed or 'Levertijd op aanvraag').strip()
        if 'onbekend' in lead.lower():
            lead = 'Levertijd op aanvraag'
    order = 'Voorraadartikel' if (manual and 'op voorraad' in confirmed.lower()) or (stock is not None and stock > 0) else 'Bestelartikel'
    return lead, order, stock, manual


def make_input(row, key, collections=None, source_snapshot=None, allow_missing_optional=False):
    application, product_type = APPLICATIONS[row['category']]
    finish = normalized_finish(row)
    color = row.get('color')
    if allow_missing_optional:
        finish, color = finish or '', color or ''
    source_name = str(row['source_name']).strip()
    title = 'Cottoceramix ' + source_name
    handle = 'cottoceramix-' + slug(source_name) + '-' + slug(row['sku'])
    lead, order, stock, manual_stock = availability(row)
    raw = row.get('raw_workbook') or {}
    live = row.get('live') or {}
    fields = live.get('fields') or {}
    specs = live.get('specs') or {}
    length, width = chosen_dimensions(row)
    if allow_missing_optional and not row.get('size'):
        length, width = None, None
    box = float(positive(row['m2_per_box']))
    pieces_value = positive(row.get('pieces_per_box'))
    weight_value = positive(row.get('weight_kg_candidate'))
    pieces = int(pieces_value) if pieces_value is not None else None
    weight = float(weight_value) if weight_value is not None else None
    if allow_missing_optional and set(row.get('flags') or []) & {'missing_weight', 'weight_conflict'}:
        weight = None
    if not allow_missing_optional and (pieces is None or weight is None):
        raise ValueError('Strict m² input requires confirmed piece count and weight')
    notes = []
    barcode = fields.get('ean') or raw.get('R')
    if not valid_ean(barcode):
        notes.append('Invalid or missing EAN omitted; SKU remains the import identity.')
    source = {
        'supplier': 'Cottoceramix', 'store_brand': 'Cottoceramix', 'original_brand': row.get('original_brand'),
        'source_sku': row['sku'], 'source_name': source_name, 'source_series': row['series'],
        'product_url': row['source_url'], 'stock_boxes': float(stock) if stock is not None else None,
        'raw_delivery_time': fields.get('delivery_time'), 'manual_availability_override': manual_stock,
        'manual_overrides': row.get('manual_overrides') or {}, 'price_basis': 'incl_btw_per_m2',
        'source_box_price': fields.get('price'), 'source_pack': row.get('source_pack'),
        'source_ean': str(barcode or ''), 'photo_sources': live['images'], 'specification_sources': specs,
        'weight_source': row.get('weight_status'), 'data_notes': notes,
        'source_revision': 'COTTO-03-2026-11-05',
        'source_snapshot_generated_at': source_snapshot,
        'source_snapshot_timezone': 'not supplied by source',
        'current_inventory_verified': False,
        'dimensions_source': 'Chosen size Z/AA; legacy Excel AB/AC are not authoritative when they differ',
        'thickness_source': 'Chosen thickness AF; legacy Excel AE is not authoritative when it differs',
        'feed_contract': {'automated_fields': FEED_FIELDS, 'protected_fields': PROTECTED_FIELDS, 'price_updates': 'Require explicit pricing policy and preserve manual price/packing overrides'},
    }
    tile = {
        'm2_per_box': box, 'pieces_per_box': pieces, 'lead_time': lead, 'order_type': order,
        'price_per_m2': {'amount': money(row['unit_price']), 'currency_code': 'EUR'},
        'price_per_box': {'amount': money(row['box_price']), 'currency_code': 'EUR'},
        'sale_unit': 'doos', 'weight_kg_per_box': weight, 'color_picker_layout': 'expandable_grid',
        'source': source,
    }
    if allow_missing_optional:
        if pieces is None:
            del tile['pieces_per_box']
        if weight is None:
            del tile['weight_kg_per_box']
    if positive(raw.get('BE')) is not None:
        tile['boxes_per_pallet'] = float(positive(raw['BE']))
    mf = []
    def meta(namespace, field, kind, value):
        if value is None or value == '':
            return
        mf.append({'namespace': namespace, 'key': field, 'type': kind, 'value': json.dumps(value, ensure_ascii=False, separators=(',', ':')) if kind == 'json' else str(value)})
    simple = {
        'tiles': {'group_id': 'COTTO-' + slug(key).upper(), 'group_label': row['series'], 'color': color, 'size': row['size'], 'execution': finish, 'application': application},
        'custom': {'artikelnummer': row['sku'], 'leverancier_artikelnummer': row['sku'], 'switch_group': 'cottoceramix-' + slug(key), 'serie': row['series'], 'kleur': color, 'afwerking': finish, 'afmetingen_original': row['size']},
        'bc_filters': {'kleur': color, 'afwerking': finish, 'glansgraad': finish, 'serie': row['series'], 'tegel_toepassing': application, 'verkoopeenheid': 'Doos'},
    }
    for namespace, pairs in simple.items():
        for field, value in pairs.items():
            meta(namespace, field, 'single_line_text_field', value)
    def item(field, label, value):
        return {'key': field, 'label': label, 'value': value}
    groups = [
        {'group': 'Product', 'items': [item('artikelnummer', 'Artikelnummer', row['sku']), item('merk', 'Merk', 'Cottoceramix'), item('serie', 'Serie', row['series']), item('productsoort', 'Productsoort', application)]},
        {'group': 'Maatvoering', 'items': [item('lengte_cm', 'Lengte', str(float(length)).replace('.', ',') + ' cm' if length is not None else None), item('breedte_cm', 'Breedte', str(float(width)).replace('.', ',') + ' cm' if width is not None else None)]},
        {'group': 'Eigenschappen', 'items': [item('kleur', 'Kleur', color), item('afwerking', 'Afwerking', finish)]},
        {'group': 'Verpakking', 'items': [item('stuks_per_doos', 'Stuks per doos', pieces), item('m2_per_doos', 'Oppervlakte per doos', str(box).replace('.', ',') + ' m²'), item('verkoopeenheid', 'Verkoopeenheid', 'Doos'), item('gewicht_per_doos', 'Gewicht per doos', str(weight).replace('.', ',') + ' kg' if weight is not None else None)]},
    ]
    for field, label, spec in [('antislipwaarde', 'Antislipwaarde', 'Antislip'), ('slijtgroep', 'Slijtgroep', 'Slijtgroep'), ('vorstbestendig', 'Vorstbestendig', 'Vorstbestendig'), ('gerectificeerd', 'Gerectificeerd', 'Gerectificeerd')]:
        if specs.get(spec):
            groups[2]['items'].append(item(field, label, specs[spec]))
    thickness = chosen_thickness(row)
    if allow_missing_optional and not row.get('thickness'):
        thickness = None
    if thickness is not None:
        meta('bc_filters', 'tegel_dikte_mm', 'number_decimal', float(thickness))
        groups[1]['items'].append(item('dikte_mm', 'Dikte', str(float(thickness)).replace('.', ',') + ' mm'))
    for field, value in [('tegel_lengte_mm', length), ('tegel_breedte_mm', width)]:
        if value is not None:
            meta('bc_filters', field, 'number_decimal', float(positive(value) * 10))
    meta('custom', 'leverancier_voorraad', 'boolean', 'true' if order == 'Voorraadartikel' else 'false')
    meta('custom', 'bron_toelichtingen_json', 'json', {'tiles': tile})
    if allow_missing_optional:
        for group in groups:
            group['items'] = [item for item in group['items'] if item['value'] is not None and item['value'] != '']
        groups = [group for group in groups if group['items']]
    meta('custom', 'complete_specificaties', 'json', groups)
    description = '<p>' + html.escape(title) + ' is een ' + html.escape(application.lower())
    if color or not allow_missing_optional:
        description += ' in de kleur ' + html.escape(color)
    if finish or not allow_missing_optional:
        description += ', met afwerking ' + html.escape(finish.lower())
    description += '.</p><p>Een doos bevat '
    if pieces is not None:
        description += str(pieces) + ' tegels, samen '
    description += str(box).replace('.', ',') + ' m². Bereken het aantal hele dozen met de tegelcalculator.</p>'
    variant = {
        'sku': row['sku'], 'price': money(row['box_price']), 'taxable': True, 'inventoryPolicy': 'CONTINUE',
        'inventoryItem': {'tracked': False, 'requiresShipping': True, 'measurement': {'weight': {'unit': 'KILOGRAMS', 'value': weight}}},
        'optionValues': [{'optionName': 'Title', 'name': 'Default Title'}], 'showUnitPrice': True,
        'unitPriceMeasurement': {'quantityUnit': 'M2', 'quantityValue': box, 'referenceUnit': 'M2', 'referenceValue': 1},
    }
    if allow_missing_optional and weight is None:
        del variant['inventoryItem']['measurement']
    if valid_ean(barcode):
        variant['barcodes'] = [{'type': 'EAN', 'value': str(barcode)}]
    value = {
        'title': title, 'handle': handle, 'vendor': 'Cottoceramix', 'productType': product_type,
        'templateSuffix': 'tegels', 'status': 'DRAFT', 'descriptionHtml': description,
        'seo': {'title': title[:55] + ' | Badkamercity', 'description': (title + '. Kies de kleur en het formaat en bereken het aantal dozen.')[:160]},
        'tags': ['Cottoceramix', 'bc-cottoceramix-cotto03-20261105', 'Tegels', application, 'tegelgroep:' + slug(key), str(row['series'])],
        'productOptions': [{'name': 'Title', 'values': [{'name': 'Default Title'}]}],
        'variants': [variant], 'metafields': mf,
        'files': [{'originalSource': image_transport_source(url), 'contentType': 'IMAGE', 'alt': title + ('' if i == 0 else ' – afbeelding ' + str(i + 1))} for i, url in enumerate(live['images'])],
    }
    if allow_missing_optional and not row.get('series'):
        value['tags'].pop()  # Do not persist str(None) as an invented series tag.
    if collections and row['category'] in collections:
        value['collections'] = list(collections[row['category']])
    return value


def plan(rows, existing=None, evidence=None, collections=None, source_snapshot=None):
    existing = existing or {}
    by_sku = Counter(row.get('sku') for row in rows)
    if any(not sku or n > 1 for sku, n in by_sku.items()):
        raise ValueError('Source SKU identities must be nonempty and globally unique')
    proof = evidence_map(evidence, rows)
    grouped = defaultdict(list)
    for row in rows:
        grouped[proof[row['sku']]['group_key'] if row['sku'] in proof else group_key(row)].append(row)
    product_plan, group_plan, held = [], [], []
    skipped = [{'sku': row['sku'], 'product_id': existing[row['sku']], 'reason': 'existing_identity_never_upserted_by_new_product_plan'} for row in rows if row['sku'] in existing]
    for key, members in sorted(grouped.items()):
        reasons = set()
        if len(members) > 50:
            reasons.add('group_exceeds_renderer_limit_50')
        if len(set(choice_tuple(row) for row in members)) != len(members):
            reasons.add('ambiguous_choice_tuple')
        if len({row['category'] for row in members}) > 1:
            reasons.add('mixed_application_group_requires_explicit_adapter')
        for row in members:
            reasons.update(row_blockers(row))
        verified = all(row['sku'] in proof for row in members)
        group = {'group_key': key, 'group_id': 'COTTO-' + slug(key).upper(), 'skus': [r['sku'] for r in members], 'source_menu_verified': verified, 'draft_ready': not reasons, 'publishable_after_readback': not reasons and verified, 'blockers': sorted(reasons)}
        group_plan.append(group)
        if reasons:
            held.extend({'sku': row['sku'], 'group_key': key, 'reasons': sorted(reasons)} for row in members if row['sku'] not in existing)
            continue
        for row in members:
            if row['sku'] in existing:
                continue
            value = make_input(row, key, collections, source_snapshot)
            product_plan.append({'sku': row['sku'], 'group_key': key, 'input': value, 'publishable_after_readback': verified, 'fingerprint': hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()})
    handles = [r['input']['handle'] for r in product_plan]
    if len(handles) != len(set(handles)):
        raise ValueError('Generated handles collide')
    summary = {'source_products': len(rows), 'draft_products': len(product_plan), 'held_products': len(held), 'existing_skipped': len(skipped), 'candidate_groups': len(group_plan), 'draft_ready_groups': sum(g['draft_ready'] for g in group_plan), 'menu_verified_groups': sum(g['source_menu_verified'] for g in group_plan), 'publishable_only_after_readback': sum(p['publishable_after_readback'] for p in product_plan), 'hold_reasons': dict(Counter(reason for row in held for reason in row['reasons'])), 'writes_performed': False, 'status': 'DRY_RUN_ONLY'}
    return {'products': product_plan, 'groups': group_plan, 'held': held, 'skipped': skipped, 'summary': summary}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-json', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--existing-json', type=Path)
    parser.add_argument('--menu-evidence', type=Path)
    parser.add_argument('--collections-json', type=Path)
    parser.add_argument('--source-snapshot')
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    destination = args.output_dir.resolve()
    if destination == repo or repo in destination.parents:
        parser.error('Private source plans must be written outside the public Git worktree')
    load = lambda path: json.loads(path.read_text()) if path else None
    existing = load(args.existing_json) or {}
    if isinstance(existing, list):
        existing = {r['sku']: r['product_id'] for r in existing}
    result = plan(load(args.source_json), existing, load(args.menu_evidence), load(args.collections_json), args.source_snapshot)
    destination.mkdir(parents=True, exist_ok=True)
    for key, value in result.items():
        (destination / (key + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2))
    (destination / 'product-set-variables.jsonl').write_text(''.join(json.dumps({'input': row['input']}, ensure_ascii=False, separators=(',', ':')) + '\n' for row in result['products']))
    print(json.dumps(result['summary'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
