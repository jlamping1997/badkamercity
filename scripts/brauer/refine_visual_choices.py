import copy
import json
from pathlib import Path


FAMILY = 'BRAUER-F3F2437BF3BB2A5C'
FINISH_LABELS = {'Stripe': 'Streepjes', 'Carving': 'Gekarteld', 'Standaard': 'Glad'}
HANDLE_LABELS = {'A': 'Lang en smal', 'B': 'Kort en smal', 'C': 'Breed en plat',
                 'D': 'Smal en plat', 'E': 'Dikkere greep'}
SPOUT_POSITION = {'1': 'Links', '2': 'Rechts'}
GLASS_CHOICE_FAMILIES = {'BRAUER-3C0BAEF46A48EBEB', 'BRAUER-27F77BA3CF0A2583', 'BRAUER-05DF137B439F0639'}


def original_products(group):
    products = copy.deepcopy(group['products'])
    if group['id'] == FAMILY:
        for product in products:
            options = product['options']
            if 'handle_code' in options:
                code = options.pop('handle_code')
                assert options['handle'] == code[0]
                assert options.pop('spout_position') == SPOUT_POSITION[code[1]]
                options['handle'] = code
    return products


def refine_group(group):
    group = copy.deepcopy(group)
    for axis in group['axes']:
        if axis['key'] == 'tap_holes':
            axis['label'] = 'Kraangaten'
            axis['labels'] = {v: {'0': 'Geen kraangat', '1': '1 kraangat', '2': '2 kraangaten'}[v] for v in axis['values']}
        if axis['key'] == 'bowls':
            axis['label'] = 'Spoelbakken'
            axis['labels'] = {v: v + (' spoelbak' if v == '1' else ' spoelbakken') for v in axis['values']}
        if group['id'] in GLASS_CHOICE_FAMILIES and axis['key'] == 'hinge':
            axis['label'] = 'Deurbevestiging'
            axis['labels'] = {v: {'Scharnieren aan de muur': 'Aan de muur',
                                  'Scharnieren aan de glaswand': 'Aan de glaswand'}[v] for v in axis['values']}
        if group['id'] in GLASS_CHOICE_FAMILIES and axis['key'] == 'side':
            axis['label'] = 'Breedte zijwand'
        if axis['key'] == 'finish':
            assert set(axis['values']) <= FINISH_LABELS.keys()
            axis['labels'] = {v: FINISH_LABELS[v] for v in axis['values']}
        if axis['key'] == 'spout':
            axis.setdefault('labels', {}).update({v: 'Recht' if v == 'Rechte' else v
                                                 for v in axis['values']})
        if group['id'] == FAMILY and axis['key'] == 'handle':
            photos = json.loads(Path(__file__).with_name('storefront_handle_photos.json').read_text())
            assert set(axis['values']) in (set(photos), set(HANDLE_LABELS))
            for code in HANDLE_LABELS:
                photo = photos[code + '1']
                source = next(p for p in group['products'] if p['sku'] == photo['sku'])
                assert source['image'] == photo['image']
                expected = {'colour': 'Chroom', 'finish': 'Standaard', 'handle': code + '1',
                            'spout': 'Rechte', 'wall_finish': 'Rozetten'}
                assert next(p for p in original_products(group) if p['sku'] == photo['sku'])['options'] == expected
                assert photo['represents'] == 'handle_shape_in_chrome'
            axis.update(kind='handle_detail_photo', label='Hendel', values=list(HANDLE_LABELS),
                        labels=dict(HANDLE_LABELS), images={code: photos[code + '1'] for code in HANDLE_LABELS})
    if group['id'] == FAMILY:
        for product in group['products']:
            options = product['options']
            code = options.get('handle_code', options['handle'])
            assert len(code) == 2 and code[0] in HANDLE_LABELS and code[1] in SPOUT_POSITION
            options.update(handle=code[0], handle_code=code, spout_position=SPOUT_POSITION[code[1]])
        if not any(axis['key'] == 'spout_position' for axis in group['axes']):
            index = next(i for i, axis in enumerate(group['axes']) if axis['key'] == 'spout') + 1
            group['axes'].insert(index, {'key': 'spout_position', 'label': 'Plaatsing uitloop',
                                         'kind': 'text', 'values': ['Links', 'Rechts']})
    return group


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('theme', type=Path)
    args = parser.parse_args()
    changed = []
    for path in sorted((args.theme / 'assets').glob('bc-brauer-*.json')):
        before = json.loads(path.read_text())
        if not isinstance(before, dict) or 'axes' not in before:
            continue
        after = refine_group(before)
        if before != after:
            assert original_products(before) == original_products(after)
            path.write_text(json.dumps(after, ensure_ascii=False, separators=(',', ':')) + '\n')
            changed.append(path.name)
    print(json.dumps({'changed_groups': len(changed), 'files': changed}))
