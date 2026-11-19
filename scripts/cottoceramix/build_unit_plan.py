"""Build private DRAFT-only native piece/pack/set inputs from verified contracts.

This module performs no network writes. Unit products require the separately
reviewed unit renderer before publication; a draft readback alone is insufficient.
"""

import argparse
import copy
import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

from build_import_plan import (
    APPLICATIONS, FEED_FIELDS, PROTECTED_FIELDS, availability, chosen_dimensions,
    chosen_thickness, image_transport_source, money, normalized_finish, positive, public_url, slug, valid_ean,
)
from build_remaining_m2_plan import sku_set


REVISION = 'COTTO-05-UNIT-2026-11-05'
BATCH_TAG = 'bc-cottoceramix-unit-cotto05-20261105'
UNITS = {'stuk', 'pak', 'set'}


def dimensions(row):
    # Chosen Z is authoritative. Do not fill absent/nonstandard chosen sizes
    # using older numeric AB/AC values just to obtain a geometry filter.
    if not re.fullmatch(r'\d+(?:[.,]\d+)?\s*[x×]\s*\d+(?:[.,]\d+)?\s*(?:cm)?', str(row.get('size') or '').strip(), re.I):
        return None, None
    return chosen_dimensions(row)


def thickness(row):
    return chosen_thickness(row) if row.get('thickness') else None


def contract_blockers(row):
    contract = row.get('unit_contract') or {}
    reasons = set(contract.get('publication_hold_reasons') or [])
    if row.get('m2_mode') or row.get('sale_method') not in {'Stuk', 'Speciale set: m¹'}:
        reasons.add('not_an_explicit_source_unit_route')
    if not row.get('sku') or not row.get('source_name') or contract.get('sku') != row.get('sku'):
        reasons.add('missing_or_mismatched_source_identity')
    unit, count = contract.get('sale_unit'), positive(contract.get('unit_count'))
    if unit not in UNITS or count is None or count != count.to_integral_value() or (unit == 'stuk' and count != 1):
        reasons.add('invalid_native_unit_count')
    price, source_price = positive(contract.get('native_price')), positive(contract.get('source_price'))
    if price is None or source_price is None:
        reasons.add('missing_positive_confirmed_native_price')
    basis = contract.get('source_price_basis')
    if basis == 'per_piece':
        if count is not None and price is not None and source_price is not None and money(source_price * count) != money(price):
            reasons.add('native_pack_price_reconcile_error')
        increment = positive(contract.get('supplier_sale_increment'))
        if count is not None and increment != count:
            reasons.add('supplier_increment_native_count_mismatch')
    elif basis == 'per_12_piece_package':
        if count != 12 or unit != 'set' or price != source_price or positive(contract.get('supplier_sale_increment')) != 1:
            reasons.add('fixed_set_price_or_count_reconcile_error')
    else:
        reasons.add('unverified_source_price_basis')
    if contract.get('currency') != 'EUR' or contract.get('vat_basis') != 'incl_btw':
        reasons.add('unverified_currency_or_vat_basis')
    if (row.get('manual_overrides') or {}).get('price') and not contract.get('manual_price_override_verified'):
        reasons.add('manual_price_override_requires_explicit_contract')
    if not public_url(row.get('source_url')):
        reasons.add('untrusted_or_private_source_url')
    images = (row.get('live') or {}).get('images') or []
    if not images:
        reasons.add('missing_real_product_image')
    elif any(not public_url(url) for url in images):
        reasons.add('untrusted_or_private_image_url')
    weight = contract.get('weight_per_native_unit')
    if weight is not None and (positive(weight) is None or not contract.get('source_weight_basis')):
        reasons.add('unverified_native_weight_basis')
    return sorted(reasons)


def availability_for_native(row):
    lead, order, stock, manual = availability(row)
    contract = row['unit_contract']
    reason = None
    if not manual and contract['sale_unit'] == 'pak' and contract['source_price_basis'] == 'per_piece' and stock is not None and 0 < stock < Decimal(str(contract['unit_count'])):
        lead, order = 'Levertijd op aanvraag', 'Bestelartikel'
        reason = 'Source stock is positive but below the confirmed piece minimum for one whole native pack.'
    return lead, order, stock, manual, reason


def make_unit_input(row, key, label, group_id, switch_group, source_snapshot=None, mosaic_tags=()):
    contract = row['unit_contract']
    unit, count = contract['sale_unit'], int(contract['unit_count'])
    application, product_type = APPLICATIONS.get(row.get('category'), ('Tegels', 'Tegels'))
    title = 'Cottoceramix ' + row['source_name'].strip()
    if unit == 'pak':
        title += ' – pak van ' + str(count) + ' stuks'
    elif unit == 'set' and not re.search(r'\bset\s+van\s+' + str(count) + r'\b', row['source_name'], re.I):
        title += ' – set van ' + str(count) + ' stuks'
    lead, order, stock, manual, stock_guard = availability_for_native(row)
    live, raw = row.get('live') or {}, row.get('raw_workbook') or {}
    fields, specs = live.get('fields') or {}, live.get('specs') or {}
    color, finish, series = row.get('color'), normalized_finish(row), row.get('series')
    length, width = dimensions(row)
    thick = thickness(row)
    weight = contract.get('weight_per_native_unit')
    barcode = fields.get('ean') or raw.get('R')
    source = {
        'supplier': 'Cottoceramix', 'store_brand': 'Cottoceramix',
        'original_brand': row.get('original_brand'), 'source_sku': row['sku'],
        'source_name': row['source_name'], 'source_series': series,
        'source_category': row.get('category'), 'product_url': row['source_url'],
        'stock_units': float(stock) if stock is not None else None,
        'stock_unit_basis': 'supplier feed units; per piece for per_piece price basis, per package for per_12_piece_package',
        'raw_delivery_time': fields.get('delivery_time'),
        'manual_availability_override': manual, 'manual_overrides': row.get('manual_overrides') or {},
        'availability_guard': stock_guard, 'price_basis': 'incl_btw_per_' + unit,
        'source_price_basis': contract['source_price_basis'], 'source_price': contract['source_price'],
        'native_price': contract['native_price'], 'supplier_sale_increment': contract['supplier_sale_increment'],
        'supplier_order_quantity_per_native_unit': count if contract['source_price_basis'] == 'per_piece' else 1,
        'source_pack': row.get('source_pack'), 'source_ean': str(barcode or ''),
        'native_barcode_omission': 'Source EAN is per piece; no multipack GTIN inferred.' if unit == 'pak' else None,
        'photo_sources': live['images'], 'specification_sources': specs,
        'weight_source': contract.get('source_weight_basis'),
        'unit_contract': copy.deepcopy(contract), 'source_revision': REVISION,
        'source_snapshot_generated_at': source_snapshot,
        'source_snapshot_timezone': 'not supplied by source', 'current_inventory_verified': False,
        'linear_coverage_omitted': True,
        'feed_contract': {'automated_fields': FEED_FIELDS, 'protected_fields': PROTECTED_FIELDS + ['native_unit_count', 'supplier_order_quantity_per_native_unit'],
                          'price_updates': 'Preserve verified source basis; multiply per-piece prices by native unit_count only for fixed packs.'},
    }
    tile = {'order_mode': 'unit', 'sale_unit': unit, 'unit_count': count,
            'lead_time': lead, 'order_type': order, 'color_picker_layout': 'expandable_grid', 'source': source}
    if weight is not None:
        tile['weight_kg_per_unit'] = weight
    meta = []
    def mf(namespace, field, kind, value):
        if value is None or value == '':
            return
        meta.append({'namespace': namespace, 'key': field, 'type': kind,
                     'value': json.dumps(value, ensure_ascii=False, separators=(',', ':')) if kind == 'json' else str(value)})
    common = {
        'tiles': {'group_id': group_id, 'group_label': label, 'color': color,
                  'size': row.get('size'), 'execution': finish, 'application': application},
        'custom': {'artikelnummer': row['sku'], 'leverancier_artikelnummer': row['sku'],
                   'switch_group': switch_group, 'serie': series, 'kleur': color,
                   'afwerking': finish, 'afmetingen_original': row.get('size')},
        'bc_filters': {'kleur': color, 'afwerking': finish, 'glansgraad': finish,
                       'serie': series, 'tegel_toepassing': application,
                       'verkoopeenheid': {'stuk': 'Stuk', 'pak': 'Pak', 'set': 'Set'}[unit]},
    }
    for namespace, pairs in common.items():
        for field, value in pairs.items():
            mf(namespace, field, 'single_line_text_field', value)
    for field, value in [('tegel_lengte_mm', length), ('tegel_breedte_mm', width)]:
        if value is not None:
            mf('bc_filters', field, 'number_decimal', float(value * 10))
    if thick is not None:
        mf('bc_filters', 'tegel_dikte_mm', 'number_decimal', float(thick))
    mf('custom', 'leverancier_voorraad', 'boolean', 'true' if order == 'Voorraadartikel' else 'false')
    mf('custom', 'bron_toelichtingen_json', 'json', {'tiles': tile})
    def item(field, name, value):
        return {'key': field, 'label': name, 'value': value}
    groups = [
        {'group': 'Product', 'items': [item('artikelnummer', 'Artikelnummer', row['sku']), item('merk', 'Merk', 'Cottoceramix'), item('serie', 'Serie', series), item('productsoort', 'Productsoort', application)]},
        {'group': 'Maatvoering', 'items': [item('lengte_cm', 'Lengte', str(float(length)).replace('.', ',') + ' cm' if length is not None else None), item('breedte_cm', 'Breedte', str(float(width)).replace('.', ',') + ' cm' if width is not None else None), item('dikte_mm', 'Dikte', str(float(thick)).replace('.', ',') + ' mm' if thick is not None else None)]},
        {'group': 'Eigenschappen', 'items': [item('kleur', 'Kleur', color), item('afwerking', 'Afwerking', finish)]},
        {'group': 'Verpakking', 'items': [item('verkoopeenheid', 'Verkoopeenheid', {'stuk': 'Stuk', 'pak': 'Pak', 'set': 'Set'}[unit]), item('stuks_per_besteleenheid', 'Stuks per besteleenheid', count), item('gewicht_per_besteleenheid', 'Gewicht per besteleenheid', str(weight).replace('.', ',') + ' kg' if weight is not None else None)]},
    ]
    for field, name, source_name in [('vorstbestendig', 'Vorstbestendig', 'Vorstbestendig'), ('gerectificeerd', 'Gerectificeerd', 'Gerectificeerd')]:
        if specs.get(source_name):
            groups[2]['items'].append(item(field, name, specs[source_name]))
    for group in groups:
        group['items'] = [value for value in group['items'] if value['value'] is not None and value['value'] != '']
    mf('custom', 'complete_specificaties', 'json', [g for g in groups if g['items']])
    description = '<p>' + html.escape(title) + '.'
    if color:
        description += ' Kleur: ' + html.escape(color) + '.'
    if finish:
        description += ' Afwerking: ' + html.escape(finish.lower()) + '.'
    description += '</p><p>' + ('Je bestelt dit artikel per stuk.' if unit == 'stuk' else ('Een pak' if unit == 'pak' else 'Een set') + ' bevat ' + str(count) + ' stuks.') + '</p>'
    inventory = {'tracked': False, 'requiresShipping': True}
    if weight is not None:
        inventory['measurement'] = {'weight': {'unit': 'KILOGRAMS', 'value': weight}}
    variant = {'sku': row['sku'], 'price': money(contract['native_price']), 'taxable': True,
               'inventoryPolicy': 'CONTINUE', 'inventoryItem': inventory,
               'optionValues': [{'optionName': 'Title', 'name': 'Default Title'}], 'showUnitPrice': False}
    if unit != 'pak' and valid_ean(barcode):
        variant['barcodes'] = [{'type': 'EAN', 'value': str(barcode)}]
    tags = ['Cottoceramix', BATCH_TAG, 'Tegels', application, 'tegelgroep:' + slug(key)]
    if series:
        tags.append(str(series))
    if row.get('category') == 'Tegels > Mozaïek':
        tags.extend(mosaic_tags)
    return {'title': title, 'handle': 'cottoceramix-' + slug(row['source_name']) + '-' + slug(row['sku']),
            'vendor': 'Cottoceramix', 'productType': product_type, 'templateSuffix': 'tegels',
            'status': 'DRAFT', 'descriptionHtml': description,
            'seo': {'title': title[:55] + ' | Badkamercity', 'description': (title + '. Bekijk de uitvoering, prijs en leverinformatie.')[:160]},
            'tags': list(dict.fromkeys(tags)), 'productOptions': [{'name': 'Title', 'values': [{'name': 'Default Title'}]}],
            'variants': [variant], 'metafields': meta,
            'files': [{'originalSource': image_transport_source(url), 'contentType': 'IMAGE', 'alt': title + ('' if i == 0 else ' – afbeelding ' + str(i + 1))} for i, url in enumerate(live['images'])]}


def family_tuple(row):
    contract = row['unit_contract']
    length, width = dimensions(row)
    thick, finish = thickness(row), normalized_finish(row)
    complete = row.get('category') and all(row.get(f) for f in ['series', 'color', 'model', 'size']) and finish and thick and length and width
    if not complete:
        return ('singleton', row['sku'])
    # A source model can be too broad (for example Färgblock model "Matt").
    # Keep the literal profile name after removing only established color,
    # chosen size, finish word and package count. This distinguishes profiles
    # without asserting a new model or grouping translated/ambiguous colors.
    color_pattern = re.compile(r'(?<!\w)' + re.escape(str(row['color'])) + r'(?!\w)', re.I)
    if len(list(color_pattern.finditer(row['source_name']))) != 1:
        return ('singleton', row['sku'])
    stem = color_pattern.sub(' ', row['source_name'])
    parts = re.findall(r'\d+(?:[.,]\d+)?', str(row['size']))
    number_pattern = lambda value: re.escape(value).replace(r'\.', '[.,]').replace(',', '[.,]')
    size_pattern = re.compile(r'(?<!\d)' + number_pattern(parts[0]) + r'\s*[x×]\s*' + number_pattern(parts[1]) + r'(?!\d)(?:\s*cm\b)?', re.I)
    if not size_pattern.search(stem):
        return ('singleton', row['sku'])
    stem = size_pattern.sub(' ', stem)
    finish_words = r'\b(?:mat|matt|mate)\b' if finish == 'Mat' else r'\b(?:glans|glanzend|glossy|brillo|lucido)\b'
    stem = re.sub(finish_words, ' ', stem, flags=re.I)
    stem = re.sub(r'\bset\s+van\s+' + str(contract['unit_count']) + r'\b', ' ', stem, flags=re.I)
    stem = slug(stem)
    if not stem:
        return ('singleton', row['sku'])
    return (str(row.get('original_brand') or ''), row['series'], row['model'], row['category'],
            finish, row['size'], format(thick.normalize(), 'f'), contract['sale_unit'], str(contract['unit_count']),
            'source-title-family:' + stem)


def prepare(rows, existing_skus=(), source_snapshot=None, mosaic_tags=()):
    if len({r.get('sku') for r in rows}) != len(rows) or any(not r.get('sku') for r in rows):
        raise ValueError('Source unit SKU identities must be nonempty and unique')
    existing, held, skipped, candidates = set(existing_skus), [], [], []
    for row in rows:
        if row['sku'] in existing:
            skipped.append({'sku': row['sku'], 'reason': 'existing_identity_never_upserted'})
            continue
        reasons = contract_blockers(row)
        if reasons:
            held.append({'sku': row['sku'], 'reasons': reasons})
        else:
            candidates.append(row)
    families = defaultdict(list)
    for row in candidates:
        families[family_tuple(row)].append(row)
    resolved = []
    for family, members in sorted(families.items()):
        if len(members) > 50 or len({r.get('color') for r in members}) != len(members):
            resolved.extend((('singleton', r['sku']), [r]) for r in members)
        else:
            resolved.append((family, members))
    products, groups, assignments, availability_guards = [], [], [], []
    for family, members in resolved:
        key = 'unit|' + '|'.join(family)
        digest = hashlib.sha256(key.encode()).hexdigest()[:10]
        stem = slug(key)[:160] + '-' + digest
        group_id, switch_group = 'COTTO-UNIT-' + stem.upper(), 'cottoceramix-unit-' + stem
        first = members[0]
        label = first['source_name'] if family[0] == 'singleton' else ' · '.join([first['series'], first['model'], first['size'], normalized_finish(first)])
        skus = sorted(r['sku'] for r in members)
        groups.append({'group_key': key, 'group_id': group_id, 'switch_group': switch_group,
                       'label': label, 'skus': skus, 'technical_source_safe': True,
                       'publication_safe': False, 'requires_unit_renderer_publication': True,
                       'source_menu_exact_match_claimed': False})
        for row in sorted(members, key=lambda r: r['sku']):
            value = make_unit_input(row, key, label, group_id, switch_group, source_snapshot, mosaic_tags)
            products.append({'sku': row['sku'], 'group_key': key, 'input': value,
                             'technical_group_review_passed': True, 'publishable_after_readback': False,
                             'requires_unit_renderer_publication': True, 'source_menu_exact_match_claimed': False,
                             'fingerprint': hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()})
            assignments.append({'sku': row['sku'], 'group_key': key, 'group_id': group_id,
                                'group_label': label, 'switch_group': switch_group, 'membership_skus': skus,
                                'publication_safe': False, 'requires_unit_renderer_publication': True})
            lead, order, stock, manual, reason = availability_for_native(row)
            if reason:
                availability_guards.append({'sku': row['sku'], 'source_stock': float(stock),
                                            'native_count': row['unit_contract']['unit_count'],
                                            'lead_time': lead, 'order_type': order, 'reason': reason})
    if len({p['input']['handle'] for p in products}) != len(products) or len({g['group_id'] for g in groups}) != len(groups):
        raise ValueError('Native unit handles or group identities collide')
    return {'products': products, 'groups': groups, 'assignments': assignments,
            'held': held, 'skipped': skipped, 'source_rows': copy.deepcopy(candidates),
            'availability_guards': availability_guards,
            'summary': {'source_products': len(rows), 'draft_products': len(products),
                        'held_products': len(held), 'existing_skipped': len(skipped),
                        'technical_families': len(groups),
                        'grouped_products': sum(len(g['skus']) for g in groups if len(g['skus']) > 1),
                        'native_units': dict(Counter(r['unit_contract']['sale_unit'] for r in candidates)),
                        'known_native_weights': sum(r['unit_contract'].get('weight_per_native_unit') is not None for r in candidates),
                        'writes_performed': False, 'status': 'DRAFT_ONLY_UNIT_PREVIEW_REQUIRED'}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-json', type=Path, required=True)
    parser.add_argument('--existing-json', action='append', default=[], type=Path)
    parser.add_argument('--source-snapshot')
    parser.add_argument('--mosaic-tag', action='append', default=[])
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    repo, destination = Path(__file__).resolve().parents[2], args.output_dir.resolve()
    if destination == repo or repo in destination.parents:
        parser.error('Private source plans must stay outside the public Git worktree')
    load = lambda p: json.loads(p.read_text())
    existing = set().union(*(sku_set(load(p)) for p in args.existing_json))
    result = prepare(load(args.source_json), existing, args.source_snapshot, args.mosaic_tag)
    destination.mkdir(parents=True, exist_ok=True)
    for key, value in result.items():
        (destination / (key + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    (destination / 'product-set-variables.jsonl').write_text(''.join(json.dumps({'input': r['input']}, ensure_ascii=False, separators=(',', ':')) + '\n' for r in result['products']))
    print(json.dumps(result['summary'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
