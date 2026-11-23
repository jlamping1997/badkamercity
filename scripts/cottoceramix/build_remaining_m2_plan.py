"""Build private, row-gated m² drafts in coherent color-only families.

No network writes. Existing SKU identities are excluded before grouping. A bad
peer therefore does not block valid products elsewhere in the same source series.
"""

import argparse
import copy
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from build_import_plan import (
    chosen_thickness, make_input, normalized_finish, row_blockers, slug,
)
from subdivide_groups import SOURCE_CONFLICTS


REVISION = 'COTTO-05-2026-11-05'
BATCH_TAG = 'bc-cottoceramix-cotto05-20261105'
EXACT_SIZE_UNSUPPORTED_SKUS = {'KB5951', *(f'KV590{i}' for i in range(1, 8))}
OPTIONAL_SPEC_BLOCKERS = {
    'missing_identity_or_choice', 'missing_official_color', 'missing_official_series',
    'missing_finish', 'unconfirmed_finish', 'missing_positive_chosen_thickness',
    'nonbinary_finish', 'missing_positive_weight_kg_candidate', 'missing_weight',
    'weight_conflict', 'missing_positive_pieces_per_box',
    'missing_positive_chosen_dimensions', 'missing_size',
}
FINISH_CONTRADICTION_SKUS = {'GQR107M', 'MA1070', 'ES1271', 'EX1170', 'EX1171', 'MA1071'}
COLOR_CONFLICT_OMISSIONS = {'AT2144', 'AT2244', 'SN1565'}


def technical_tuple(row):
    """Only color may vary within the initial partition."""
    return (
        str(row.get('original_brand') or ''), str(row.get('series') or ''),
        str(row.get('model') or ''), str(row.get('category') or ''),
        normalized_finish(row), str(row.get('size') or ''),
        format(chosen_thickness(row).normalize(), 'f'),
    )


def explicit_title_family(row):
    """Known source-title distinctions; never infer a model from an SKU."""
    name = str(row.get('source_name') or '')
    if (row.get('original_brand'), row.get('series')) == ('Altair', 'Madrid'):
        match = re.match(r'^Madrid\s+(Liso|Metro)\b', name)
        if match:
            return 'Madrid ' + match.group(1)
    if (row.get('original_brand'), row.get('series')) == ('Tonalite', 'Wabisabi'):
        match = re.match(r'^(Shibusa|Wabisabi)\b', name)
        if match:
            return match.group(1)
    return None


def group_identity(technical, suffix=None):
    key = '|'.join([
        technical[0], technical[1], 'model:' + (technical[2] or '__base__'),
        'application:' + technical[3], 'finish:' + technical[4],
        'size:' + technical[5], 'thickness:' + technical[6],
    ] + ([suffix] if suffix else []))
    # Slug alone collapses punctuation and accents; the digest prevents collisions.
    digest = hashlib.sha256(key.encode()).hexdigest()[:10]
    stem = slug(key)[:160] + '-' + digest
    return key, 'COTTO-' + stem.upper(), 'cottoceramix-' + stem


def split_partition(rows):
    """Resolve known title families, then isolate any remaining ambiguity."""
    by_family = defaultdict(list)
    for row in rows:
        by_family[explicit_title_family(row)].append(row)
    partitions = []
    for family, members in sorted(by_family.items(), key=lambda x: str(x[0])):
        colors = [str(row['color']) for row in members]
        if len(set(colors)) == len(colors) and len(members) <= 50:
            suffix = 'source-title-family:' + family if family else None
            partitions.append((suffix, family, members))
        else:
            # No arbitrary partial color family or deduplication: each exact
            # source product remains available as an unambiguous singleton.
            for row in members:
                partitions.append(('singleton:' + row['sku'], family, [row]))
    return partitions


def prepare(rows, existing_skus=(), collections=None, source_snapshot=None):
    counts = Counter(row.get('sku') for row in rows)
    if any(not sku or count != 1 for sku, count in counts.items()):
        raise ValueError('Source SKU identities must be nonempty and globally unique')
    existing = set(existing_skus)
    skipped, held, candidates = [], [], []
    for row in rows:
        sku = row['sku']
        if sku in existing:
            skipped.append({'sku': sku, 'reason': 'existing_identity_never_upserted'})
            continue
        reasons = row_blockers(row)
        if sku in EXACT_SIZE_UNSUPPORTED_SKUS:
            reasons = sorted(set(reasons + ['renderer_exact_size_unsupported']))
        if sku in SOURCE_CONFLICTS:
            reasons = sorted(set(reasons + ['confirmed_source_attribute_conflict']))
        if sku in FINISH_CONTRADICTION_SKUS:
            reasons = sorted(set(reasons + ['source_title_finish_conflict']))
        if reasons:
            held.append({'sku': sku, 'reasons': reasons})
        else:
            candidates.append(row)
    grouped = defaultdict(list)
    for row in candidates:
        grouped[technical_tuple(row)].append(row)
    products, groups, assignments = [], [], []
    for technical, members in sorted(grouped.items()):
        for suffix, title_family, subset in split_partition(sorted(members, key=lambda r: r['sku'])):
            key, group_id, switch_group = group_identity(technical, suffix)
            label_parts = [title_family or technical[1]]
            if technical[2] and not title_family:
                label_parts.append(technical[2])
            label_parts += [technical[4], technical[5], technical[6] + ' mm']
            label = ' · '.join(label_parts)
            skus = sorted(row['sku'] for row in subset)
            notes = [
                'Partitioned by explicit brand/series/model/application/finish/size/thickness.',
                'Only color varies; exact supplier-menu equivalence is not claimed.',
            ]
            if title_family:
                notes.append('Additional source product-title family: ' + title_family)
            if suffix and suffix.startswith('singleton:'):
                notes.append('Singleton prevents duplicate color or renderer-limit ambiguity.')
            groups.append({
                'group_key': key, 'group_id': group_id, 'switch_group': switch_group,
                'label': label, 'skus': skus, 'publication_safe': True,
                'source_menu_exact_match_claimed': False, 'proof_notes': notes,
            })
            for row in subset:
                value = make_input(row, key, collections, source_snapshot)
                value['tags'] = [BATCH_TAG if tag == 'bc-cottoceramix-cotto03-20261105' else tag for tag in value['tags']]
                updates = {'tiles.group_id': group_id, 'tiles.group_label': label, 'custom.switch_group': switch_group}
                for mf in value['metafields']:
                    name = mf['namespace'] + '.' + mf['key']
                    if name in updates:
                        mf['value'] = updates[name]
                    if name == 'custom.bron_toelichtingen_json':
                        data = json.loads(mf['value'])
                        data['tiles']['source']['source_revision'] = REVISION
                        mf['value'] = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
                products.append({
                    'sku': row['sku'], 'group_key': key, 'input': value,
                    'publishable_after_readback': True,
                    'technical_group_review_passed': True,
                    'source_menu_exact_match_claimed': False,
                    'fingerprint': hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
                })
                assignments.append({
                    'sku': row['sku'], 'group_key': key, 'group_id': group_id,
                    'group_label': label, 'switch_group': switch_group,
                    'membership_skus': skus, 'publication_safe': True,
                })
    if len({row['input']['handle'] for row in products}) != len(products):
        raise ValueError('Generated handles collide')
    if len({group['group_id'] for group in groups}) != len(groups):
        raise ValueError('Group IDs collide')
    summary = {
        'source_products': len(rows), 'draft_products': len(products),
        'existing_skipped': len(skipped), 'held_products': len(held),
        'technical_color_families': len(groups),
        'max_family_size': max((len(g['skus']) for g in groups), default=0),
        'hold_reasons': dict(Counter(reason for row in held for reason in row['reasons'])),
        'writes_performed': False, 'status': 'DRY_RUN_ONLY',
        'source_menu_exact_match_claimed': False,
    }
    return {'products': products, 'groups': groups, 'assignments': assignments,
            'held': held, 'skipped': skipped, 'source_rows': copy.deepcopy(candidates),
            'summary': summary}


def sku_set(value):
    if isinstance(value, dict):
        if value.get('sku'):
            return {value['sku']}
        if 'variants' in value:
            return sku_set(value['variants']['nodes'])
        if 'nodes' in value:
            return sku_set(value['nodes'])
        return set(value)
    result = set()
    for row in value:
        if isinstance(row, dict):
            result.update(sku_set(row))
        elif isinstance(row, str) and row:
            result.add(row)
        else:
            raise ValueError('Existing registry contains an unsupported identity')
    return result


def prepare_optional_singletons(rows, existing_skus=(), collections=None, source_snapshot=None,
                                reviewed_exact_size_singletons=()):
    """Keep firm commercial/identity gates, omit unknown optional facts.

    Fully specified rows remain the strict route's responsibility. Singleton
    references ensure absent color/finish/thickness cannot imply a cross-product
    combination or choice that the source did not establish.
    """
    counts = Counter(row.get('sku') for row in rows)
    if any(not sku or count != 1 for sku, count in counts.items()):
        raise ValueError('Source SKU identities must be nonempty and globally unique')
    existing = set(existing_skus)
    reviewed_exact = set(reviewed_exact_size_singletons)
    if not reviewed_exact <= EXACT_SIZE_UNSUPPORTED_SKUS:
        raise ValueError('Reviewed exact-size exception is limited to the eight explicit baseline-reviewed SKUs')
    products, groups, assignments, candidates, held, skipped, color_omission_ledger = [], [], [], [], [], [], []
    for row in sorted(rows, key=lambda r: r['sku']):
        sku = row['sku']
        if sku in existing:
            skipped.append({'sku': sku, 'reason': 'existing_identity_never_upserted'})
            continue
        original_reasons = set(row_blockers(row))
        reasons = original_reasons - OPTIONAL_SPEC_BLOCKERS
        if not row.get('source_name'):
            reasons.add('missing_source_product_name')
        if sku in SOURCE_CONFLICTS:
            reasons.add('confirmed_source_attribute_conflict')
        if sku in FINISH_CONTRADICTION_SKUS:
            reasons.add('source_title_finish_conflict')
        if sku in EXACT_SIZE_UNSUPPORTED_SKUS and sku not in reviewed_exact:
            reasons.add('renderer_exact_size_unsupported')
        if reasons:
            held.append({'sku': sku, 'reasons': sorted(reasons)})
            continue
        if not original_reasons and sku not in reviewed_exact:
            skipped.append({'sku': sku, 'reason': 'fully_specified_row_belongs_to_strict_route'})
            continue
        key = 'optional-singleton|' + sku
        digest = hashlib.sha256(key.encode()).hexdigest()[:10]
        group_id = 'COTTO-OPTIONAL-' + slug(sku).upper() + '-' + digest.upper()
        switch_group = 'cottoceramix-optional-' + slug(sku) + '-' + digest
        label = str(row.get('series') or row['source_name'])
        input_row = row
        if sku in COLOR_CONFLICT_OMISSIONS:
            input_row = copy.deepcopy(row)
            input_row['color'] = None
            original_reasons.add('source_title_color_conflict_omitted')
            color_omission_ledger.append({
                'sku': sku, 'source_name': row['source_name'],
                'original_color': row.get('color'), 'published_color': None,
                'reason': 'Explicit source product title and official color disagree; neither replacement color inferred.',
            })
        value = make_input(input_row, key, collections, source_snapshot, allow_missing_optional=True)
        value['tags'] = [BATCH_TAG if tag == 'bc-cottoceramix-cotto03-20261105' else tag for tag in value['tags']]
        updates = {'tiles.group_id': group_id, 'tiles.group_label': label, 'custom.switch_group': switch_group}
        for mf in value['metafields']:
            name = mf['namespace'] + '.' + mf['key']
            if name in updates:
                mf['value'] = updates[name]
            if name == 'custom.bron_toelichtingen_json':
                data = json.loads(mf['value'])
                data['tiles']['source']['source_revision'] = REVISION
                data['tiles']['source']['optional_specifications_omitted'] = sorted(original_reasons)
                if sku in reviewed_exact:
                    data['tiles']['source']['exact_size_static_singleton_review'] = {
                        'review': 'COTTO-05 actual MAIN fixed-format singleton review',
                        'source_size': row.get('size'),
                        'restriction': 'Remain a singleton until the exact-size renderer is published.',
                    }
                if sku in COLOR_CONFLICT_OMISSIONS:
                    data['tiles']['source']['conflicting_color_omitted'] = {
                        'original_color': row.get('color'), 'source_name': row['source_name'],
                        'reason': 'Explicit title/color contradiction; no replacement inferred.',
                    }
                mf['value'] = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
        present = {m['namespace'] + '.' + m['key'] for m in value['metafields']}
        for name, field_value in updates.items():
            if name not in present:
                namespace, field = name.split('.', 1)
                value['metafields'].append({'namespace': namespace, 'key': field, 'type': 'single_line_text_field', 'value': field_value})
        product = {
            'sku': sku, 'group_key': key, 'input': value,
            'publishable_after_readback': True, 'technical_group_review_passed': True,
            'source_menu_exact_match_claimed': False,
            'optional_specifications_omitted': sorted(original_reasons),
            'fingerprint': hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        }
        if sku in reviewed_exact:
            product['reviewed_exact_size_singleton'] = True
        products.append(product)
        candidates.append(copy.deepcopy(row))
        groups.append({
            'group_key': key, 'group_id': group_id, 'switch_group': switch_group,
            'label': label, 'skus': [sku], 'publication_safe': True,
            'source_menu_exact_match_claimed': False,
            'proof_notes': ['Exact source SKU singleton; unknown optional facts omitted, not inferred.'],
        })
        assignments.append({
            'sku': sku, 'group_key': key, 'group_id': group_id,
            'group_label': label, 'switch_group': switch_group,
            'membership_skus': [sku], 'publication_safe': True,
        })
    summary = {
        'source_products': len(rows), 'draft_products': len(products),
        'existing_skipped': sum(x['reason'] == 'existing_identity_never_upserted' for x in skipped),
        'strict_route_skipped': sum(x['reason'] == 'fully_specified_row_belongs_to_strict_route' for x in skipped),
        'held_products': len(held), 'technical_color_families': len(groups),
        'max_family_size': 1 if products else 0,
        'hold_reasons': dict(Counter(reason for row in held for reason in row['reasons'])),
        'writes_performed': False, 'status': 'DRY_RUN_ONLY',
        'source_menu_exact_match_claimed': False, 'route': 'optional_specs_singletons',
        'conflicting_colors_omitted': len(color_omission_ledger),
        'reviewed_exact_size_singletons': sum(p.get('reviewed_exact_size_singleton') is True for p in products),
    }
    return {'products': products, 'groups': groups, 'assignments': assignments,
            'held': held, 'skipped': skipped, 'source_rows': candidates,
            'color_omission_ledger': color_omission_ledger, 'summary': summary}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-json', required=True, type=Path)
    parser.add_argument('--existing-json', action='append', default=[], type=Path)
    parser.add_argument('--collections-json', type=Path)
    parser.add_argument('--source-snapshot')
    parser.add_argument('--optional-spec-singletons', action='store_true')
    parser.add_argument('--allow-reviewed-exact-size-singletons', action='store_true')
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    if args.allow_reviewed_exact_size_singletons and not args.optional_spec_singletons:
        parser.error('Reviewed exact-size releases require the fixed singleton route')
    repo = Path(__file__).resolve().parents[2]
    destination = args.output_dir.resolve()
    if destination == repo or repo in destination.parents:
        parser.error('Private source plans must stay outside the public Git worktree')
    load = lambda path: json.loads(path.read_text())
    existing = set().union(*(sku_set(load(path)) for path in args.existing_json))
    builder = prepare_optional_singletons if args.optional_spec_singletons else prepare
    extras = {'reviewed_exact_size_singletons': EXACT_SIZE_UNSUPPORTED_SKUS} if args.allow_reviewed_exact_size_singletons else {}
    result = builder(load(args.source_json), existing,
                     load(args.collections_json) if args.collections_json else None,
                     args.source_snapshot, **extras)
    destination.mkdir(parents=True, exist_ok=True)
    for key, value in result.items():
        (destination / (key + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    (destination / 'product-set-variables.jsonl').write_text(''.join(
        json.dumps({'input': row['input']}, ensure_ascii=False, separators=(',', ':')) + '\n'
        for row in result['products']))
    print(json.dumps(result['summary'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
