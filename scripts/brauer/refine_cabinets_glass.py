import argparse
import copy
from datetime import datetime, timezone
from decimal import Decimal
import json
from pathlib import Path
import re


def refine(theme, sources):
    variants = {v['id']: v for v in sources}
    changed = []
    counts = {'cabinet_groups': 0, 'cabinet_products': 0, 'glass_groups': 0, 'glass_products': 0}
    timestamp = datetime.now(timezone.utc).isoformat()
    for path in sorted((theme / 'assets').glob('bc-brauer-*.json')):
        group = json.loads(path.read_text())
        if 'axes' not in group:
            continue
        cabinet = any(a['key'] == 'cutouts' for a in group['axes'])
        glass = all(p['sku'].startswith('GS-') for p in group['products'])
        if not (cabinet or glass):
            continue
        before = copy.deepcopy(group['products'])
        titles = []
        for product in group['products']:
            source = variants[product['variant_id']]
            assert source['sku'] == product['sku']
            assert source['product']['id'] == product['id']
            assert source['product']['handle'] == product['handle']
            assert source['product']['status'] == 'ACTIVE' and source['product']['vendor'] == 'BRAUER'
            title = source['product']['title'].lower()
            titles.append(title)
            amount = Decimal(source['price']) * 100
            assert amount >= 0 and amount == amount.to_integral_value()
            product['price_cents'] = int(amount)
            if cabinet:
                assert re.search(r'onderkast ' + re.escape(product['options']['width']) + r'\b', title), title
                assert re.search(r'\b' + product['options']['drawers'] + r' (?:softclose )?(?:lades|laden)\b', title), title
                assert re.search(r'\b' + product['options']['cutouts'] + r' (?:sifon )?uitsparing(?:en)?\b', title), title
        group.update(price_order=True, price_currency='EUR', price_checked_at=timestamp)
        for axis in group['axes']:
            if cabinet and axis['key'] == 'drawers':
                axis.update(label='Aantal laden', labels={v: v + ' laden' for v in axis['values']})
            if cabinet and axis['key'] == 'cutouts':
                axis.update(label='Afvoeruitsparingen', labels={v: v + (' uitsparing' if v == '1' else ' uitsparingen') for v in axis['values']}, help='Stem het aantal afvoeruitsparingen af op de wastafel die je erop plaatst.')
            if glass and axis['key'] == 'colour':
                axis['label'] = 'Kleur beslag'
            if glass and axis['key'] == 'hinge':
                axis['help'] = 'Aan de muur: de deur scharniert aan de wand. Aan de glaswand: de deur scharniert aan het vaste glaspaneel.'
            if glass and axis['key'] in ('width', 'depth'):
                axis['label'] = {'width': 'Breedte (nominale maat)', 'depth': 'Diepte (nominale maat)'}[axis['key']]
                axis['help'] = 'Controleer de exacte inbouwmaat in de specificaties en montagetekening.'
            if glass and axis['key'] == 'width' and any(a['key'] == 'hinge' for a in group['axes']):
                sizes = {}
                for product, title in zip(group['products'], titles):
                    match = re.search(r'nisdeur 2-delig helder glas (\d+)x200 omkeerbaar met draaideur (\d+) aan (muur|glas)', title)
                    assert match, title
                    width, door, _ = match.groups()
                    assert width == product['options']['width']
                    sizes.setdefault(width, set()).add(door)
                assert all(len(v) == 1 for v in sizes.values())
                axis['labels'] = {w: f'{w} cm · deur {next(iter(d))} cm' for w, d in sizes.items()}
        if glass:
            if all('nisdeur' in t and 'schuif' in t for t in titles):
                group['glass_help'] = 'Glazen schuifdeur voor plaatsing in een nis.'
            elif all('nisdeur' in t and 'naar binnen draaiend' in t for t in titles):
                group['glass_help'] = 'Glazen douchedeur voor plaatsing in een nis; draait naar binnen.'
            elif all('nisdeur 2-delig' in t and 'void' in t for t in titles):
                group['glass_help'] = 'Tweedelige nisdeur: een draaideur met een vast glaspaneel.'
            elif all('pendeldeuren' in t for t in titles):
                group['glass_help'] = 'Pendeldeuren voor plaatsing in een nis.'
            elif all('nisdeur' in t for t in titles):
                group['glass_help'] = 'Glazen douchedeur voor plaatsing in een nis.'
        for old, new in zip(before, group['products']):
            assert {k: v for k, v in old.items() if k != 'price_cents'} == {k: v for k, v in new.items() if k != 'price_cents'}
        path.write_text(json.dumps(group, ensure_ascii=False, separators=(',', ':')) + '\n')
        changed.append('assets/' + path.name)
        key = 'cabinet' if cabinet else 'glass'
        counts[key + '_groups'] += 1
        counts[key + '_products'] += len(group['products'])
    return {**counts, 'files': changed, 'verified_at': timestamp}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('theme', type=Path)
    parser.add_argument('variants', type=Path)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    report = refine(args.theme, json.loads(args.variants.read_text()))
    args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'files'}))
