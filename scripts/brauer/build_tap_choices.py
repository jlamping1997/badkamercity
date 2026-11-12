import argparse
import copy
from datetime import datetime, timezone
from decimal import Decimal
import json
from pathlib import Path
import re

from refine_visual_choices import HANDLE_LABELS, GLASS_CHOICE_FAMILIES, refine_group

OPBOUW = 'BRAUER-46A454F9A15BDAA9'
COLOURS = {'CE': 'Chroom', 'S': 'Zwart', 'NG': 'RVS-kleurig', 'GM': 'Gunmetal',
           'GK': 'Koper', 'GG': 'Goud', 'CF': 'Coffee'}
EXECUTIONS = ['Laag', 'Verhoogd', 'Hoog, ronde uitloop', 'Hoog, platte uitloop']


def cents(value):
    amount = Decimal(str(value)) * 100
    assert amount >= 0 and amount == amount.to_integral_value()
    return int(amount)


def is_priced_group(group):
    return group['id'] in GLASS_CHOICE_FAMILIES or any(a['key'] in ('finish', 'handshower', 'arm', 'tap_holes') for a in group['axes'])


def attach_prices(group, variants, checked_at):
    result = copy.deepcopy(group)
    if not is_priced_group(result):
        return result
    for product in result['products']:
        source = variants[product['variant_id']]
        assert source['id'] == product['variant_id'] and source['sku'] == product['sku']
        assert source['product']['id'] == product['id'] and source['product']['handle'] == product['handle']
        assert source['product']['vendor'].upper() == 'BRAUER' and source['product']['status'] == 'ACTIVE'
        product['price_cents'] = cents(source['price'])
    result.update(price_order=True, price_currency='EUR', price_checked_at=checked_at)
    return result


def build_opbouw_group(live, checked_at):
    products = []
    public = [p for p in live if p['productType'] == 'Opbouwwastafelkranen']
    for product in public:
        assert product['vendor'].upper() == 'BRAUER' and product['status'] == 'ACTIVE'
        assert product['onlineStoreUrl'] and len(product['variants']['nodes']) == 1
        variant = product['variants']['nodes'][0]
        title = product['title']
        match = re.fullmatch(r'BRAUER Standaard (Carving |Stripe )?(lage|verhoogde|hoge) opbouw wastafelkraan( met draaibare (ronde|platte) uitloop)? model ([A-E]) (.+)', title)
        assert match, title
        finish, height, _, spout, handle, colour_text = match.groups()
        sku = re.fullmatch(r'5-(CE|S|NG|GM|GK|GG|CF)-(001|002|003)(?:-([A-Z]+[0-9]))?', variant['sku'])
        assert sku, variant['sku']
        colour = COLOURS[sku[1]]
        assert colour.lower() in colour_text.lower() or (colour == 'Zwart' and 'zwart' in colour_text.lower())
        assert sku[2] == {'lage': '001', 'verhoogde': '002', 'hoge': '003'}[height]
        assert (height == 'hoge') == bool(spout)
        execution = {'lage': 'Laag', 'verhoogde': 'Verhoogd'}.get(height, 'Hoog, ' + str(spout) + ' uitloop')
        image = (((product.get('featuredMedia') or {}).get('preview') or {}).get('image') or {}).get('url', '')
        assert not image or image.startswith('https://cdn.shopify.com/')
        products.append({'id': product['id'], 'variant_id': variant['id'], 'sku': variant['sku'],
                         'handle': product['handle'], 'url': '/products/' + product['handle'], 'image': image,
                         'price_cents': cents(variant['price']), 'options': {'colour': colour,
                         'finish': (finish or '').strip() or 'Standaard', 'handle': handle,
                         'height_execution': execution}})
    assert len(products) >= 2 and len({p['id'] for p in products}) == len(products)
    assert len({tuple(p['options'].values()) for p in products}) == len(products)
    images = {}
    refs = {'A': ('5-CE-001', 730), 'B': ('5-CE-001-HD5', 1000),
            'C': ('5-CE-001-HD3', 730), 'D': ('5-CE-001-HD4', 900), 'E': ('5-CE-001-HD1', 930)}
    for key, (sku, x) in refs.items():
        source = next(p for p in products if p['sku'] == sku)
        assert source['options'] == {'colour': 'Chroom', 'finish': 'Standaard', 'handle': key, 'height_execution': 'Laag'}
        images[key] = {'sku': sku, 'image': source['image'], 'represents': 'handle_shape_in_chrome',
                       'crop': {'x': x, 'y': 60, 'width': 1800 - x, 'height': 650,
                                'source_width': 2000, 'source_height': 2000}}
    axes = [{'key': 'colour', 'label': 'Kleur', 'kind': 'product_first_image', 'values': list(COLOURS.values())},
            {'key': 'finish', 'label': 'Afwerking greep', 'kind': 'finish_detail_photo', 'values': ['Standaard', 'Carving', 'Stripe']},
            {'key': 'handle', 'label': 'Hendel', 'kind': 'handle_detail_photo', 'values': list(HANDLE_LABELS),
             'labels': dict(HANDLE_LABELS), 'images': images,
             'help': 'De foto toont de hendelvorm in chroom. Kleur en afwerking kies je hierboven. Grijze opties zijn niet combineerbaar met je andere keuzes.'},
            {'key': 'height_execution', 'label': 'Uitvoering', 'kind': 'product_first_image', 'values': EXECUTIONS}]
    return refine_group({'version': 1, 'id': OPBOUW, 'axes': axes, 'products': products,
                         'price_order': True, 'price_currency': 'EUR', 'price_checked_at': checked_at})


def add_opbouw_routes(theme, group):
    for bucket in range(8):
        path = theme / f'snippets/bc-brauer-route-{bucket}.liquid'
        body = path.read_text()
        ids = [p['id'].split('/')[-1] for p in group['products']
               if (int(p['id'].split('/')[-1]) // 32768) % 8 == bucket]
        if not ids:
            continue
        if OPBOUW in body:
            body = re.sub(r"  when [0-9 or]+\n    echo 'BRAUER-46A454F9A15BDAA9\|\|bc-brauer-46a454f9a15bdaa9.json'\n", '', body)
        assert not any(re.search(r'\b' + value + r'\b', body) for value in ids)
        case = '  when ' + ' or '.join(ids) + "\n    echo '" + OPBOUW + "||bc-brauer-46a454f9a15bdaa9.json'\n"
        assert body.count('  endcase') == 1
        path.write_text(body.replace('  endcase', case + '  endcase'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('theme', type=Path)
    parser.add_argument('prices', type=Path)
    parser.add_argument('opbouw_live', type=Path, nargs='?')
    args = parser.parse_args()
    checked_at = datetime.now(timezone.utc).isoformat()
    variants = {p['id']: p for p in json.loads(args.prices.read_text())}
    changed = []
    for path in (args.theme / 'assets').glob('bc-brauer-*.json'):
        group = json.loads(path.read_text())
        if not isinstance(group, dict) or 'axes' not in group or (group['id'] == OPBOUW and args.opbouw_live):
            continue
        if not any(p['variant_id'] in variants for p in group['products']):
            continue
        after = attach_prices(refine_group(group), variants, checked_at)
        if after != group:
            path.write_text(json.dumps(after, ensure_ascii=False, separators=(',', ':')) + '\n')
            changed.append(path.name)
    opbouw_count = 0
    if args.opbouw_live:
        opbouw = build_opbouw_group(json.loads(args.opbouw_live.read_text()), checked_at)
        (args.theme / 'assets/bc-brauer-46a454f9a15bdaa9.json').write_text(json.dumps(opbouw, ensure_ascii=False, separators=(',', ':')) + '\n')
        add_opbouw_routes(args.theme, opbouw)
        opbouw_count = len(opbouw['products'])
    print(json.dumps({'priced_groups': len(changed), 'priced_products': len(variants), 'opbouw_products': opbouw_count}))
