"""Plan metadata-only, technically coherent subgroups without Shopify writes."""

import argparse
import copy
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from build_import_plan import slug


MODEL_SPLITS = {'Natucer|Fan', 'Quintessenza|Marea', 'Vives|Micra-R', 'Vives|Root', 'Vives|Zero', 'Wow|Roots'}
SOURCE_CONFLICTS = {
    'VA3201': 'Chosen series sizes disagree with current source names for Doha-R; no format correction guessed.',
    'VA3202': 'Chosen size 32x100 disagrees with current source name 32x99.',
    'VA3203': 'Chosen size 32x101 disagrees with current source name 32x99.',
    'MAR128L': 'Source name says Oro Lucido while chosen finish is Mat; finish requires confirmation.',
    'MAR129L': 'Chosen finish is Glans but source color label contains Matt; color label requires confirmation.',
    'MAR130L': 'Chosen finish is Glans but source color label contains Matt; color label requires confirmation.',
    'MAR131L': 'Chosen finish is Glans but source color label contains Matt; color label requires confirmation.',
    'MAR132L': 'Chosen finish is Glans but source color label contains Matt; color label requires confirmation.',
}


def metadata(row):
    return {m['namespace'] + '.' + m['key']: m['value'] for m in row['input']['metafields']}


def complete_color_combinations(rows):
    values = [metadata(row) for row in rows]
    colors = {m['tiles.color'] for m in values}
    for current in values:
        for color in colors:
            if not any(candidate['tiles.color'] == color and all(candidate.get(field) == current.get(field) for field in ['tiles.application', 'tiles.execution', 'tiles.size', 'bc_filters.tegel_dikte_mm']) for candidate in values):
                return False
    return True


def prepare(plans, normalized, reviewed_groups):
    source = {row['sku']: row for row in normalized}
    changes = set(reviewed_groups)
    groups = defaultdict(list)
    descriptors = {}
    for original in plans:
        sku, parent = original['sku'], original['group_key']
        row = source[sku]
        mf = metadata(original)
        if sku in SOURCE_CONFLICTS:
            key = 'HOLD|' + sku
            descriptor = {'group_label': str(row['series']) + ' · Controle nodig', 'notes': [SOURCE_CONFLICTS[sku]], 'publication_safe': False, 'origin': parent}
        elif parent not in changes:
            key = parent
            descriptor = {'group_label': mf['tiles.group_label'], 'notes': ['Previously reviewed coherent complete group retained.'], 'publication_safe': True, 'origin': parent}
        else:
            model = row.get('model') if parent in MODEL_SPLITS else None
            finish = mf['tiles.execution']
            key = parent + '|model:' + str(model or '__base__') + '|finish:' + finish
            label_parts = [str(row['series'])] + ([str(model)] if model else []) + [finish]
            descriptor = {'group_label': ' · '.join(label_parts), 'notes': ['Official source series and chosen finish define this family.', 'Official model H: ' + (str(model) if model else 'empty; no extra model asserted'), 'Only existing exact SKUs are included; missing combinations are not created.'], 'publication_safe': True, 'origin': parent}
        groups[key].append(original)
        descriptors[key] = descriptor
    final_groups = {}
    for key, members in groups.items():
        descriptor = descriptors[key]
        if descriptor['origin'] in changes and descriptor['publication_safe'] and not complete_color_combinations(members):
            split = defaultdict(list)
            for row in members:
                mf = metadata(row)
                split[(mf['tiles.size'], mf.get('bc_filters.tegel_dikte_mm', '0'))].append(row)
            for (size, thickness), subset in split.items():
                subkey = key + '|size:' + size + '|thickness:' + thickness
                subdescriptor = copy.deepcopy(descriptor)
                subdescriptor['group_label'] += ' · ' + size + ' · ' + thickness.rstrip('0').rstrip('.') + ' mm'
                subdescriptor['notes'].append('Partitioned by explicit source size/thickness because color would otherwise silently change a technical choice.')
                final_groups[subkey] = (subset, subdescriptor)
        else:
            final_groups[key] = (members, descriptor)
    result, assignments, group_register = [], [], []
    for key, (members, descriptor) in sorted(final_groups.items()):
        member_skus = sorted(row['sku'] for row in members)
        group_id = 'COTTO-' + slug(key).upper()
        switch_group = 'cottoceramix-' + slug(key)
        if descriptor['origin'] not in changes and descriptor['publication_safe']:
            first = metadata(members[0])
            group_id, switch_group = first['tiles.group_id'], first['custom.switch_group']
        if not complete_color_combinations(members):
            raise ValueError('Subdivision still changes another color choice: ' + key)
        if len(members) > 50:
            raise ValueError('Subdivision exceeds renderer limit: ' + key)
        group_register.append({'group_key': key, 'group_id': group_id, 'label': descriptor['group_label'], 'skus': member_skus, 'publication_safe': descriptor['publication_safe'], 'proof_notes': descriptor['notes'], 'source_menu_exact_match_claimed': False})
        for old in members:
            new = copy.deepcopy(old)
            new['original_group_key'] = old['group_key']
            new['group_key'] = key
            new['technical_group_review_passed'] = descriptor['publication_safe']
            updates = {'tiles.group_id': group_id, 'tiles.group_label': descriptor['group_label'], 'custom.switch_group': switch_group}
            for m in new['input']['metafields']:
                name = m['namespace'] + '.' + m['key']
                if name in updates:
                    m['value'] = updates[name]
            new['fingerprint'] = hashlib.sha256(json.dumps(new['input'], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
            for field, expected in old['input'].items():
                if field != 'metafields' and new['input'][field] != expected:
                    raise ValueError('Non-menu field changed: ' + field)
            old_meta, new_meta = metadata(old), metadata(new)
            if any(value != new_meta[name] for name, value in old_meta.items() if name not in updates):
                raise ValueError('Non-menu metafield changed: ' + old['sku'])
            result.append(new)
            assignments.append({'sku': new['sku'], 'original_group_key': old['group_key'], 'group_key': key, 'group_id': group_id, 'group_label': descriptor['group_label'], 'switch_group': switch_group, 'membership_skus': member_skus, 'publication_safe': descriptor['publication_safe'], 'proof_notes': descriptor['notes']})
    if len({item['group_id'] for item in group_register}) != len(group_register):
        raise ValueError('Subgroup IDs collide after normalization')
    return {'products': result, 'assignments': assignments, 'groups': group_register, 'publication_safe_skus': sorted(item['sku'] for item in assignments if item['publication_safe']), 'unresolved': [{'sku': sku, 'reason': reason} for sku, reason in SOURCE_CONFLICTS.items() if sku in {row['sku'] for row in plans}], 'writes_performed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--planned', required=True, type=Path)
    parser.add_argument('--normalized', required=True, type=Path)
    parser.add_argument('--publication-review', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    destination = args.output_dir.resolve()
    if destination == repo or repo in destination.parents:
        parser.error('Private plans must be written outside the public Git worktree')
    load = lambda path: json.loads(path.read_text())
    review = load(args.publication_review)
    changed = {row['group_key'] for row in review['groups'] if row['decision'] != 'ALLOW_AFTER_FULL_READBACK'}
    result = prepare(load(args.planned), load(args.normalized), changed)
    destination.mkdir(parents=True, exist_ok=True)
    names = {'products': 'final-products', 'assignments': 'final-group-assignments', 'groups': 'final-groups', 'publication_safe_skus': 'publication-safe-skus', 'unresolved': 'unresolved-skus'}
    for key, name in names.items():
        (destination / (name + '.json')).write_text(json.dumps(result[key], ensure_ascii=False, indent=2))
    ready = [row for row in result['assignments'] if row['publication_safe']]
    (destination / 'group-assignments-ready.json').write_text(json.dumps(ready, ensure_ascii=False, indent=2))
    print(json.dumps({'products': len(result['products']), 'groups': len(result['groups']), 'safe_products': len(ready), 'unresolved': len(result['unresolved']), 'writes_performed': False}))


if __name__ == '__main__':
    main()
