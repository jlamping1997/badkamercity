"""Build public theme choices from the prepared catalog and a fresh Shopify identity read.

The source directory and the identity export are private inputs, never committed.
Only exact public product facts and reviewed choice groups enter the theme.
"""
import argparse
import json
from collections import Counter
from pathlib import Path


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n')


def build(prepared, live_path, theme, report_path):
    catalog = {p['sku']: p for p in json.loads((prepared / 'catalog.json').read_text())}
    families = json.loads((prepared / 'families.json').read_text())
    live = json.loads(live_path.read_text())
    by_sku = {}
    for product in live:
        assert product['vendor'].upper() == 'BRAUER'
        assert product['status'] == 'ACTIVE' and product['onlineStoreUrl']
        assert product['variantsCount']['count'] == 1
        variant = product['variants']['nodes'][0]
        assert variant['sku'] not in by_sku
        by_sku[variant['sku']] = product
    assert set(catalog) == set(by_sku)
    routes = [[] for _ in range(8)]
    report = {'groups': 0, 'products': 0, 'held_groups': [], 'single_article_groups': 0,
              'files': [], 'identity_errors': 0, 'missing_first_images': 0}
    for family in families:
        if family['status'] != 'VOORBEREID':
            report['held_groups'].append({'id': family['id'], 'articles': family['sku_count']})
            continue
        if family['sku_count'] < 2:
            report['single_article_groups'] += 1
            continue
        assert family['axes']
        keys = {axis['key'] for axis in family['axes']}
        for axis in family['axes']:
            keys.update(axis.get('depends_on', []))
        signatures = Counter(tuple(catalog[s]['options'].get(a['key']) for a in family['axes'])
                             for s in family['skus'])
        assert all(count == 1 for count in signatures.values()), family['id']
        products = []
        for sku in family['skus']:
            source, product = catalog[sku], by_sku[sku]
            assert source['family_id'] == family['id']
            assert source['handle_proposal'] == product['handle']
            variant = product['variants']['nodes'][0]
            assert variant['sku'] == sku
            image = ((product.get('featuredMedia') or {}).get('preview') or {}).get('image') or {}
            image_url = image.get('url', '')
            assert not image_url or image_url.startswith('https://cdn.shopify.com/')
            report['missing_first_images'] += not bool(image_url)
            products.append({'id': product['id'], 'variant_id': variant['id'], 'sku': sku,
                             'handle': product['handle'], 'url': '/products/' + product['handle'],
                             'image': image_url,
                             'options': {key: source['options'].get(key) for key in sorted(keys)}})
        group = {'version': 1, 'id': family['id'], 'axes': family['axes'], 'products': products}
        filename = 'assets/bc-brauer-' + family['id'][7:].lower() + '.json'
        write_json(theme / filename, group)
        report['files'].append(filename)
        by_bucket = {}
        for product in products:
            numeric_id = int(product['id'].split('/')[-1])
            by_bucket.setdefault((numeric_id // 32768) % 8, []).append(numeric_id)
        for bucket, ids in by_bucket.items():
            routes[bucket].append('  when ' + ' or '.join(map(str, ids)) + '\n' +
                                  "    echo '" + family['id'] + '||' + filename[7:] + "'\n")
        report['groups'] += 1
        report['products'] += len(products)
    for bucket, cases in enumerate(routes):
        filename = f'snippets/bc-brauer-route-{bucket}.liquid'
        (theme / filename).write_text('{% doc %}\nRoutes verified Brauer product IDs to their prepared choice group.\n@param {product} product - Exact current product.\n{% enddoc %}\n{%- liquid\n  case product.id\n' + ''.join(cases) +
                                     '  endcase\n-%}\n')
        report['files'].append(filename)
    write_json(report_path, report)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('prepared', type=Path)
    parser.add_argument('live', type=Path)
    parser.add_argument('theme', type=Path)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    result = build(args.prepared, args.live, args.theme, args.report)
    print(json.dumps({key: value for key, value in result.items() if key != 'files'}))
