#!/usr/bin/env python3
"""Build bounded, exact-ID routing for the existing Hotbath V2 menu engine.

No network or Shopify writes. Complete groups stay together in a data asset.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit


ROUTE_SNIPPET = 'bc-hotbath-menu-route'
SOURCE_SNIPPET = 'bc-hotbath-menu-source'
ASSET_PREFIX = 'bc-hotbath-menu-data-'
DEFAULT_MAX_ASSET_BYTES = 300_000
DEFAULT_MAX_HELPER_BYTES = 98_000
DEFAULT_MAX_GROUPS_PER_ASSET = 80
DISABLED_ROUTE = '__NO_MENU__'
AUTHORIZED_COLOUR_ADDITIONS = {
    'hotbath-archie-ar105ext-inbouw-wastafelmengkraan-rvs316': {'AR105EXT18IX', 'AR105EXT25IX'},
    'hotbath-archie-arhf-inbouwthermostaat-afbouwdeel': {'ARHF011IX', 'ARHF012IX', 'ARHF013IX', 'ARHF014IX', 'ARHF015IX'},
}
HELD_SKUS = {'SDS32BGP', 'IBS33BGP4', 'IBS20AGN357', 'IBS20BBP', 'IBS20BCP'}


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n'


def sha256(value):
    return hashlib.sha256(value).hexdigest()


def numeric_id(product):
    value = str(product.get('id', '')).rsplit('/', 1)[-1]
    if not value.isdigit():
        raise ValueError(f'Invalid product ID for {product.get("handle")}')
    return int(value)


def variants(product):
    return product.get('variants', {}).get('nodes', [])


def is_spom(product):
    texts = [product.get('title', ''), product.get('handle', '')]
    texts.extend(v.get('sku', '') or '' for v in variants(product))
    return 'SPOM' in ' '.join(texts).upper()


def is_test(product):
    return product.get('title', '').upper().startswith('TEST') or any(
        str(v.get('sku', '')).upper().startswith('TEST') for v in variants(product)
    )


def eligible(product):
    return product.get('status') == 'ACTIVE' and bool(product.get('publishedAt')) and not is_spom(product) and not is_test(product)


def current_group(product):
    value = product.get('group')
    return str(value.get('value', '') if isinstance(value, dict) else value or '').strip()


def groups_from(value):
    if isinstance(value, list):
        return value
    if isinstance(value, dict) and isinstance(value.get('groups'), list):
        return value['groups']
    raise ValueError('Expected a groups array or {groups:[...]}')


def group_signature(group):
    return json.dumps(group, sort_keys=True, ensure_ascii=False, separators=(',', ':'))


def clean_group(group, catalog, *, existing=False):
    result = copy.deepcopy(group)
    gid = str(result.get('id', '')).strip()
    if not gid or '\n' in gid or '\r' in gid or '||' in gid:
        raise ValueError('Missing or unsafe group ID')
    removed = []
    records = []
    for record in result.get('products', []):
        handle = record.get('handle')
        product = catalog.get(handle)
        if product is None:
            raise ValueError(f'{gid}: unknown current product {handle}')
        held = HELD_SKUS.intersection(str(v.get('sku', '')).upper() for v in variants(product))
        if held:
            raise ValueError(f'{gid}: unresolved title/SKU conflict is on hold: {", ".join(sorted(held))}')
        if is_spom(product):
            removed.append(handle)
            continue
        if not eligible(product):
            raise ValueError(f'{gid}: inactive, unpublished or test product {handle}')
        records.append(record)
    result['products'] = records
    if removed:
        for menu in result.get('menus', []):
            actual = {str(r.get('options', {}).get(menu['key'], '')).strip() for r in records}
            menu['values'] = [x for x in menu.get('values', []) if str(x).strip() in actual]
    if len(records) < 2:
        return None, removed, [r['handle'] for r in records] if existing else []
    return result, removed, []


def validate_group(group, catalog):
    gid = group['id']
    menus = group.get('menus', [])
    keys = [m.get('key') for m in menus]
    if not keys or any(not isinstance(k, str) or not k for k in keys) or len(set(keys)) != len(keys):
        raise ValueError(f'{gid}: invalid or duplicate menu fields')
    rows = group['products']
    handles = [r['handle'] for r in rows]
    if len(handles) != len(set(handles)):
        raise ValueError(f'{gid}: duplicate product handles')
    tuples = set()
    varying = False
    for menu in menus:
        vals = [str(v).strip() for v in menu.get('values', [])]
        if not vals or len(vals) != len(set(vals)):
            raise ValueError(f'{gid}: missing or duplicate values for {menu["key"]}')
        actual = {str(r.get('options', {}).get(menu['key'], '')).strip() for r in rows}
        if '' in actual or not actual.issubset(vals):
            raise ValueError(f'{gid}: missing option or value absent from menu {menu["key"]}')
        varying = varying or len(actual) > 1
    if not varying:
        raise ValueError(f'{gid}: no real choice varies')
    for row in rows:
        handle = row['handle']
        path = urlsplit(str(row.get('url', '')))
        if path.netloc and path.netloc not in {'badkamercity.nl', 'www.badkamercity.nl', 'fpa9hu-i3.myshopify.com'}:
            raise ValueError(f'{gid}: off-origin URL for {handle}')
        if path.path.rstrip('/') != '/products/' + handle:
            raise ValueError(f'{gid}: URL does not identify handle {handle}')
        choice = tuple(str(row.get('options', {}).get(k, '')).strip() for k in keys)
        if choice in tuples:
            raise ValueError(f'{gid}: duplicate choice tuple {choice}')
        tuples.add(choice)
        actual_group = current_group(catalog[handle])
        if actual_group and actual_group != gid:
            raise ValueError(f'{gid}: {handle} has another existing group {actual_group}')


def validate_option_additions(value, existing, catalog):
    """Authorize only the seven documented, additive Archie IX colour labels."""
    if value is None:
        return {}
    if not isinstance(value, dict) or not isinstance(value.get('additions'), list):
        raise ValueError('Expected option-additions sidecar {additions:[...]}')
    old_rows = {(g['id'], r['handle']): r for g in existing for r in g['products']}
    approved = {}
    for addition in value['additions']:
        gid, handle = addition.get('group_id'), addition.get('handle')
        key = (gid, handle)
        sku = addition.get('sku')
        if key in approved:
            raise ValueError(f'{gid}: duplicate colour addition for {handle}')
        if gid not in AUTHORIZED_COLOUR_ADDITIONS or sku not in AUTHORIZED_COLOUR_ADDITIONS[gid]:
            raise ValueError(f'{gid}: colour addition outside authorized Archie IX scope')
        if addition.get('key') != 'kleur' or addition.get('value') != 'RVS 316':
            raise ValueError(f'{gid}: colour addition must identify verified IX finish RVS 316')
        old = old_rows.get(key)
        if old is None or 'kleur' in old.get('options', {}):
            raise ValueError(f'{gid}: colour addition must extend an old record without a colour')
        product = catalog.get(handle)
        if product is None or sku not in {v.get('sku') for v in variants(product)}:
            raise ValueError(f'{gid}: colour addition SKU does not match current product {handle}')
        approved[key] = {k: addition[k] for k in ['group_id', 'handle', 'key', 'value', 'sku']}
    return approved


def prepare_groups(incoming, existing, catalog, *, option_additions=None):
    existing_map = {g['id']: g for g in existing}
    approved_additions = validate_option_additions(option_additions, existing, catalog)
    used_additions = set()
    incoming_map = {}
    for group in incoming:
        gid = group.get('id')
        if gid in incoming_map:
            raise ValueError(f'Duplicate input group {gid}')
        incoming_map[gid] = group
    output = []
    disabled = set()
    removed = set()
    unchanged = []
    augmented = []
    cleaned_existing = []
    for gid, original in existing_map.items():
        original_clean, gone, remaining = clean_group(original, catalog, existing=True)
        removed.update(gone)
        disabled.update(remaining)
        proposed = incoming_map.pop(gid, None)
        if original_clean is None:
            if proposed is not None:
                proposed_clean, more_gone, _ = clean_group(proposed, catalog)
                removed.update(more_gone)
                if proposed_clean is not None:
                    original_clean = proposed_clean
                    disabled.difference_update(r['handle'] for r in proposed_clean['products'])
                else:
                    continue
            else:
                continue
        if proposed is not None:
            proposed_clean, more_gone, _ = clean_group(proposed, catalog)
            removed.update(more_gone)
            if proposed_clean is None:
                raise ValueError(f'{gid}: cannot replace a usable existing group with a singleton')
            proposed_records = {r['handle']: r for r in proposed_clean['products']}
            for old in original_clean['products']:
                key = (gid, old['handle'])
                expected = copy.deepcopy(old)
                if key in approved_additions:
                    expected.setdefault('options', {})['kleur'] = approved_additions[key]['value']
                    used_additions.add(key)
                if proposed_records.get(old['handle']) != expected:
                    raise ValueError(f'{gid}: existing record changed or removed: {old["handle"]}')
            original_keys = [m['key'] for m in original_clean['menus']]
            proposed_keys = [m['key'] for m in proposed_clean['menus']]
            has_additions = any(group_id == gid for group_id, _ in approved_additions)
            expected_keys = original_keys + (['kleur'] if has_additions else [])
            if proposed_keys != expected_keys:
                raise ValueError(f'{gid}: existing menu fields changed')
            if has_additions:
                if proposed_clean['menus'][:-1] != original_clean['menus']:
                    raise ValueError(f'{gid}: original menu definitions changed during colour addition')
                actual_colours = {r.get('options', {}).get('kleur') for r in proposed_clean['products']}
                if None in actual_colours or len(actual_colours) < 2:
                    raise ValueError(f'{gid}: added colour must be a complete, varying choice')
            selected = proposed_clean
        else:
            selected = original_clean
        if group_signature(selected) == group_signature(original):
            unchanged.append(gid)
            continue
        validate_group(selected, catalog)
        output.append(selected)
        (cleaned_existing if gone else augmented).append(gid)
    for gid, proposed in incoming_map.items():
        group, gone, _ = clean_group(proposed, catalog)
        removed.update(gone)
        if group is None:
            continue
        validate_group(group, catalog)
        output.append(group)
    membership = {}
    for group in output:
        for record in group['products']:
            handle = record['handle']
            if handle in membership and membership[handle] != group['id']:
                raise ValueError(f'{handle} is in multiple rollout groups')
            membership[handle] = group['id']
    if set(approved_additions) != used_additions:
        raise ValueError('Unused option-additions authorization: sidecar and proposed records differ')
    return sorted(output, key=lambda g: g['id']), {
        'unchanged_existing_group_ids': sorted(unchanged),
        'augmented_existing_group_ids': sorted(augmented),
        'spom_cleaned_existing_group_ids': sorted(cleaned_existing),
        'spom_input_records_removed': sorted(removed),
        'disabled_product_handles': sorted(disabled),
        'new_group_ids': sorted(g['id'] for g in output if g['id'] not in existing_map),
        'authorized_existing_colour_additions': [approved_additions[key] for key in sorted(used_additions)],
    }


def pack_assets(groups, max_bytes, max_groups):
    chunks = []
    current = []
    for group in groups:
        solo = compact({'groups': [group]}).encode()
        if len(solo) > max_bytes:
            raise ValueError(f'Group {group["id"]} exceeds asset byte limit ({len(solo)} > {max_bytes})')
        proposed = current + [group]
        if current and (len(proposed) > max_groups or len(compact({'groups': proposed}).encode()) > max_bytes):
            chunks.append(current)
            current = [group]
        else:
            current = proposed
    if current:
        chunks.append(current)
    assets = {}
    mapping = {}
    for i, chunk in enumerate(chunks, 1):
        filename = f'{ASSET_PREFIX}{i:03d}.json'
        content = compact({'groups': chunk})
        assets['assets/' + filename] = content
        for group in chunk:
            mapping[group['id']] = filename
    return assets, mapping


def liquid_literal(value):
    if '\n' in value or '\r' in value:
        raise ValueError('Liquid string cannot contain newlines')
    return "'" + value.replace('\\', '\\\\').replace("'", "\\'") + "'"


def doc_header(text, params):
    return '{% doc %}\n' + text + '\n' + '\n'.join(params) + '\n{% enddoc %}\n'


def id_part(mapping):
    grouped = defaultdict(list)
    for pid, key in sorted(mapping.items()):
        grouped[key].append(pid)
    lines = ['{%- liquid', '  case product.id']
    for key, ids in sorted(grouped.items()):
        lines.append('    when ' + ', '.join(str(x) for x in ids))
        lines.append('      echo ' + liquid_literal(str(key)))
    lines += ['  endcase', '-%}', '']
    return doc_header('Returns an exact product-ID route key.', ['@param {product} product - Current product.']) + '\n'.join(lines)


def source_part(mapping):
    lines = ['{%- liquid', '  case route_key']
    for key, value in sorted(mapping.items()):
        lines += [f'    when {key}', '      echo ' + liquid_literal(value)]
    lines += ['  endcase', '-%}', '']
    return doc_header('Returns a verified group ID and data asset.', ['@param {number} route_key - Exact generated route key.']) + '\n'.join(lines)


def bounded_routing_helpers(id_mapping, source_mapping, max_bytes):
    outputs = {}
    specs = [
        (ROUTE_SNIPPET, id_mapping, id_part, 'product.id', 'product: product', ['@param {product} product - Current product.']),
        (SOURCE_SNIPPET, source_mapping, source_part, 'route_key', 'route_key: bc_hotbath_route_key_number', ['@param {string} key - Generated route key.']),
    ]
    stats = {}
    for name, mapping, maker, bucket_key, render_arg, params in specs:
        for count in [1, 3, 7, 13, 29, 53]:
            buckets = [dict() for _ in range(count)]
            for key, value in mapping.items():
                buckets[key % count][key] = value
            contents = [maker(bucket) for bucket in buckets]
            if max([len(x.encode()) for x in contents], default=0) <= max_bytes:
                break
        else:
            raise ValueError('Unable to bound routing helpers')
        if count == 1 and name == ROUTE_SNIPPET:
            outputs['snippets/' + name + '.liquid'] = contents[0]
        else:
            for i, content in enumerate(contents):
                outputs[f'snippets/{name}-{i:02d}.liquid'] = content
            lines = ['{%- liquid']
            if name == SOURCE_SNIPPET:
                lines += ["  assign bc_hotbath_route_key_number = key | plus: 0", f'  assign bc_hotbath_route_bucket = bc_hotbath_route_key_number | modulo: {count}']
            else:
                lines += [f'  assign bc_hotbath_route_bucket = {bucket_key} | modulo: {count}']
            lines.append('  case bc_hotbath_route_bucket')
            for i in range(count):
                lines += [f'    when {i}', f"      render '{name}-{i:02d}', {render_arg}"]
            lines += ['  endcase', '-%}', '']
            outputs['snippets/' + name + '.liquid'] = doc_header('Routes a generated Hotbath menu lookup to one bounded part.', params) + '\n'.join(lines)
        stats[name] = {'part_count': count, 'largest_part_bytes': max([len(x.encode()) for x in contents], default=0)}
    return outputs, stats


def patch_main(source):
    beginning = '  {%- liquid\n    capture current_switch_group\n'
    start = source.find(beginning)
    if start < 0 or source.count(beginning) != 1:
        raise ValueError('Main product switch-group anchor missing or ambiguous')
    end = source.find('\n    capture current_group\n', start)
    if end < 0:
        raise ValueError('Legacy group anchor missing')
    lines = [
        '  {%- liquid',
        '    assign bc_hotbath_menu_excluded = false',
        '    assign bc_hotbath_menu_disabled = false',
        '    assign bc_hotbath_menu_title = product.title | upcase',
        '    assign bc_hotbath_menu_handle = product.handle | upcase',
        "    if bc_hotbath_menu_title contains 'SPOM' or bc_hotbath_menu_handle contains 'SPOM'",
        '      assign bc_hotbath_menu_excluded = true',
        '    endif',
        '    for bc_hotbath_menu_variant in product.variants',
        '      assign bc_hotbath_menu_sku = bc_hotbath_menu_variant.sku | upcase',
        "      if bc_hotbath_menu_sku contains 'SPOM'",
        '        assign bc_hotbath_menu_excluded = true',
        '        break',
        '      endif',
        '    endfor',
        '    capture current_switch_group',
        '      echo product.metafields.custom.switch_group.value | default: product.metafields.custom.switch_group',
        '    endcapture',
        '    assign current_switch_group = current_switch_group | strip',
        "    assign bc_switcher_data_url = ''",
        '    if bc_hotbath_menu_excluded',
        "      assign current_switch_group = ''",
        '    else',
        '      capture bc_hotbath_route_key',
        f"        render '{ROUTE_SNIPPET}', product: product",
        '      endcapture',
        '      assign bc_hotbath_route_key = bc_hotbath_route_key | strip',
        '      if bc_hotbath_route_key != blank',
        '        capture bc_hotbath_route',
        f"          render '{SOURCE_SNIPPET}', key: bc_hotbath_route_key",
        '        endcapture',
        "        assign bc_hotbath_route_parts = bc_hotbath_route | strip | split: '||'",
        '        assign bc_hotbath_routed_group = bc_hotbath_route_parts[0] | strip',
        f"        if bc_hotbath_routed_group == '{DISABLED_ROUTE}'",
        '          assign bc_hotbath_menu_disabled = true',
        "          assign current_switch_group = ''",
        '        elsif bc_hotbath_routed_group != blank',
        '          if current_switch_group == blank',
        '            assign current_switch_group = bc_hotbath_routed_group',
        '          endif',
        '          if current_switch_group == bc_hotbath_routed_group',
        '            assign bc_hotbath_data_asset = bc_hotbath_route_parts[1] | strip',
        '            if bc_hotbath_data_asset != blank',
        '              assign bc_switcher_data_url = bc_hotbath_data_asset | asset_url',
        '            endif',
        '          endif',
        '        endif',
        '      endif',
        '    endif',
    ]
    result = source[:start] + '\n'.join(lines) + source[end:]
    old = '    assign current_group = current_group | strip\n'
    new = old + "    if bc_hotbath_menu_excluded or bc_hotbath_menu_disabled\n      assign current_group = ''\n    endif\n"
    if result.count(old) != 1:
        raise ValueError('Legacy group strip anchor missing or ambiguous')
    result = result.replace(old, new, 1)
    old = '{%- if current_switch_group == blank and product_group_source_collection != blank and current_group != blank -%}'
    result = result.replace(old, '{%- if bc_hotbath_menu_excluded == false and bc_hotbath_menu_disabled == false and current_switch_group == blank and product_group_source_collection != blank and current_group != blank -%}', 1)
    old = '  {%- if current_switch_group == blank -%}\n    <!-- BC SWITCHER DEBUG:'
    new = '  {%- if bc_hotbath_menu_excluded == false and bc_hotbath_menu_disabled == false and current_switch_group == blank -%}\n    <!-- BC SWITCHER DEBUG:'
    if result.count(old) != 1:
        raise ValueError('Legacy JSON anchor missing or ambiguous')
    result = result.replace(old, new, 1)
    old = "          {%- if product.metafields.bc_sunshower.configuration.value != blank or current_switch_group != blank or current_group != blank or product.has_only_default_variant == false -%}\n            {{ bc_buybox_options_markup }}\n          {%- endif -%}"
    new = "          {%- if bc_hotbath_menu_excluded == false and bc_hotbath_menu_disabled == false -%}\n" + old + '\n          {%- endif -%}'
    if result.count(old) != 1:
        raise ValueError('Final options render anchor missing or ambiguous')
    return result.replace(old, new, 1)


def build(source_dir, groups_path, existing_path, catalog_path, output_dir, *, option_additions_path=None, max_asset_bytes=DEFAULT_MAX_ASSET_BYTES, max_helper_bytes=DEFAULT_MAX_HELPER_BYTES, max_groups_per_asset=DEFAULT_MAX_GROUPS_PER_ASSET):
    snapshot = json.loads(catalog_path.read_text())
    catalog_rows = snapshot['products'] if isinstance(snapshot, dict) else snapshot
    catalog = {p['handle']: p for p in catalog_rows}
    if len(catalog) != len(catalog_rows):
        raise ValueError('Duplicate current catalog handles')
    existing = groups_from(json.loads(existing_path.read_text()))
    incoming = groups_from(json.loads(groups_path.read_text()))
    option_additions = json.loads(option_additions_path.read_text()) if option_additions_path else None
    groups, preparation = prepare_groups(incoming, existing, catalog, option_additions=option_additions)
    assets, group_assets = pack_assets(groups, max_asset_bytes, max_groups_per_asset)
    id_mapping = {}
    source_mapping = {}
    for ordinal, group in enumerate(groups, 1):
        source_mapping[ordinal] = group['id'] + '||' + group_assets[group['id']]
        for record in group['products']:
            pid = numeric_id(catalog[record['handle']])
            if pid in id_mapping:
                raise ValueError('Duplicate routed product ID')
            id_mapping[pid] = ordinal
    if preparation['disabled_product_handles']:
        ordinal = len(groups) + 1
        source_mapping[ordinal] = DISABLED_ROUTE + '||'
        for handle in preparation['disabled_product_handles']:
            id_mapping[numeric_id(catalog[handle])] = ordinal
    helpers, helper_stats = bounded_routing_helpers(id_mapping, source_mapping, max_helper_bytes)
    source_main = (source_dir / 'sections/main-product.liquid').read_text()
    source_snippet = (source_dir / 'snippets/bc-product-switcher.liquid').read_text()
    source_js = (source_dir / 'assets/bc-product-switcher.js').read_bytes()
    if 'data-bc-preserve-position' not in source_snippet or 'data-switcher-data-url' not in source_snippet:
        raise ValueError('Source V2 snippet lacks scoped data/position support')
    if "data_url: bc_switcher_data_url" not in source_main:
        raise ValueError('Source section does not pass its scoped V2 data URL')
    outputs = {'sections/main-product.liquid': patch_main(source_main), **helpers, **assets}
    for filename, value in outputs.items():
        path = output_dir / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value)
    manifest = {
        'schema': 'hotbath-menu-rollout-v1',
        'scope': 'UNPUBLISHED_THEME_ONLY',
        'source_catalog_raw_sha256': sha256(catalog_path.read_bytes()),
        'existing_menu_data_raw_sha256': sha256(existing_path.read_bytes()),
        'input_groups_raw_sha256': sha256(groups_path.read_bytes()),
        'option_additions_raw_sha256': sha256(option_additions_path.read_bytes()) if option_additions_path else None,
        'groups_written': len(groups),
        'product_ids_routed': len(id_mapping),
        'menu_records_written': sum(len(g['products']) for g in groups),
        'spom_products_in_catalog': sum(is_spom(p) for p in catalog_rows),
        'spom_records_in_output': sum(is_spom(catalog[r['handle']]) for g in groups for r in g['products']),
        'held_skus_excluded': sorted(HELD_SKUS),
        'asset_count': len(assets),
        'asset_max_bytes': max([len(x.encode()) for x in assets.values()], default=0),
        'asset_limit_bytes': max_asset_bytes,
        'helper_stats': helper_stats,
        'helper_max_bytes': max([len(x.encode()) for x in helpers.values()], default=0),
        'helper_limit_bytes': max_helper_bytes,
        'existing_v2_js_changed': False,
        'existing_v2_js_sha256': sha256(source_js),
        'existing_shared_dataset_changed': False,
        'product_metafield_mutations': False,
        **preparation,
        'changed_files': [{'filename': name, 'size_bytes': (output_dir / name).stat().st_size, 'sha256': sha256((output_dir / name).read_bytes())} for name in outputs],
    }
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    (output_dir.parent / 'rollout-theme-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    (output_dir.parent / 'routing-index.json').write_text(json.dumps({'product_id_to_route': id_mapping, 'route_to_source': source_mapping}, ensure_ascii=False, indent=2) + '\n')
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, required=True)
    parser.add_argument('--groups', type=Path, required=True)
    parser.add_argument('--existing-data', type=Path, required=True)
    parser.add_argument('--catalog', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--option-additions-sidecar', type=Path)
    parser.add_argument('--max-asset-bytes', type=int, default=DEFAULT_MAX_ASSET_BYTES)
    parser.add_argument('--max-helper-bytes', type=int, default=DEFAULT_MAX_HELPER_BYTES)
    parser.add_argument('--max-groups-per-asset', type=int, default=DEFAULT_MAX_GROUPS_PER_ASSET)
    args = parser.parse_args()
    manifest = build(args.source_dir, args.groups, args.existing_data, args.catalog, args.output_dir, option_additions_path=args.option_additions_sidecar, max_asset_bytes=args.max_asset_bytes, max_helper_bytes=args.max_helper_bytes, max_groups_per_asset=args.max_groups_per_asset)
    print(json.dumps({k: v for k, v in manifest.items() if k not in {'changed_files', 'unchanged_existing_group_ids', 'augmented_existing_group_ids', 'new_group_ids'}}, ensure_ascii=False))


if __name__ == '__main__':
    main()
