import copy
import json
from pathlib import Path


FAMILY = 'BRAUER-F3F2437BF3BB2A5C'
FINISH_LABELS = {'Stripe': 'Streepjes', 'Carving': 'Gekarteld', 'Standaard': 'Glad'}
HANDLE_LABELS = {'A': 'Lang en smal', 'B': 'Kort en smal', 'C': 'Breed en plat',
                 'D': 'Smal en plat', 'E': 'Dikkere greep'}


def refine_group(group):
    group = copy.deepcopy(group)
    for axis in group['axes']:
        if axis['key'] == 'finish':
            assert set(axis['values']) <= FINISH_LABELS.keys()
            axis['labels'] = {v: FINISH_LABELS[v] for v in axis['values']}
        if group['id'] == FAMILY and axis['key'] == 'handle':
            photos = json.loads(Path(__file__).with_name('storefront_handle_photos.json').read_text())
            assert set(photos) == set(axis['values'])
            for code, photo in photos.items():
                source = next(p for p in group['products'] if p['sku'] == photo['sku'])
                assert source['image'] == photo['image']
                assert source['options'] == {'colour': 'Chroom', 'finish': 'Standaard',
                    'handle': code[0] + '1', 'spout': 'Rechte', 'wall_finish': 'Rozetten'}
                assert photo['represents'] == 'handle_shape_in_chrome'
            axis['kind'] = 'handle_detail_photo'
            axis['label'] = 'Hendel'
            axis['labels'] = {code: HANDLE_LABELS[code[0]] + (' · links' if code[1] == '2' else ' · rechts')
                              for code in axis['values']}
            axis['images'] = photos
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
            assert before['products'] == after['products']
            path.write_text(json.dumps(after, ensure_ascii=False, separators=(',', ':')) + '\n')
            changed.append(path.name)
    print(json.dumps({'changed_groups': len(changed), 'files': changed}))
