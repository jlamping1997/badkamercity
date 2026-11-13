"""Prepare draft single-SKU products, using private input files; no Shopify writes."""
import argparse
import html
import json
from pathlib import Path


def prepare(parent, working, proofs):
    assert parent['vendor'] == 'Lagoo'
    assert not parent['variants']['pageInfo']['hasNextPage']
    variants = parent['variants']['nodes']
    assert 1 < len(variants) <= 50
    source = {row['sku']: row for row in working['variants']}
    menus = [{'key': option['name'].lower(), 'label': option['name'],
              'order': index + 1, 'display_type': 'buttons'}
             for index, option in enumerate(parent['options'])]
    destinations, inputs = [], []
    for variant in variants:
        sku = variant['sku']
        item, proof = source[sku], proofs[sku]
        assert item['article'] not in ('LVS1', 'LVS2', 'LVS3')
        assert not item.get('protected') and not item.get('skipImport')
        assert proof['fileId'].startswith('gid://shopify/MediaImage/')
        assert '/files/lagoo-official-' in proof['url']
        assert proof['evidence'] in ('manufacturer_sku', 'image_identity_and_visual_check', 'owner_approved')
        assert item['descriptionSource'] == 'lagoo.nl'
        assert all(v['value'] == item['options'][v['name']] for v in variant['selectedOptions'])
        handle = 'lagoo-' + sku.lower()
        title = item['title'].replace(' —', ' ' + item['article'] + ' —', 1)
        options = {v['name'].lower(): v['value'] for v in variant['selectedOptions']}
        destinations.append({'handle': handle, 'url': '/products/' + handle,
                             'title': title, 'options': options,
                             'sort_order': len(destinations) + 1})
        description = ''.join('<p>' + html.escape(p).replace('\n', '<br>') + '</p>'
                              for p in item['description'].split('\n\n') if p.strip())
        documents = [d for d in item['documents'] if d.get('owned') and not d.get('suggested')]
        if documents:
            description += '<h3>Documenten en handleidingen</h3><ul>'
            for document in documents:
                assert '/files/lagoo-official-' in document['url']
                description += '<li><a href="' + html.escape(document['url'], quote=True) + '" target="_blank" rel="noopener">' + html.escape(document['title']) + '</a></li>'
            description += '</ul>'
        single_variant = {key: variant[key] for key in ('sku', 'price', 'compareAtPrice', 'taxable')}
        single_variant['inventoryItem'] = {key: variant['inventoryItem'][key]
                                          for key in ('tracked', 'requiresShipping')}
        single_variant['optionValues'] = [{'optionName': v['name'], 'name': v['value']}
                                          for v in variant['selectedOptions']]
        single_variant['file'] = {'id': proof['fileId']}
        inputs.append({'handle': handle, 'title': title, 'vendor': 'Lagoo',
                       'status': 'DRAFT', 'productType': parent['productType'],
                       'tags': sorted(set(parent['tags'] + ['Lagoo-productlinks-2026-11-03'])),
                       'descriptionHtml': description,
                       'productOptions': [{'name': v['name'], 'position': index + 1,
                                           'values': [{'name': v['value']}]}
                                          for index, v in enumerate(variant['selectedOptions'])],
                       'files': [{'id': proof['fileId']}], 'variants': [single_variant],
                       'metafields': [{key: field[key] for key in ('namespace', 'key', 'type', 'value')}
                                     for field in parent['metafields']['nodes']
                                     if field['namespace'] == 'custom' and field['key'] == 'serie']})
    assert len({p['handle'] for p in destinations}) == len(variants)
    assert len({tuple(sorted(p['options'].items())) for p in destinations}) == len(variants)
    data = {'groups': [{'id': 'lagoo-' + parent['id'].split('/')[-1],
                        'menus': menus, 'products': destinations}]}
    for product in inputs:
        product['metafields'].append({'namespace': 'custom', 'key': 'lagoo_choices',
                                     'type': 'json', 'value': json.dumps(data, ensure_ascii=False)})
    return inputs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('parent', 'working', 'proofs', 'output'):
        parser.add_argument('--' + name, required=True, type=Path)
    args = parser.parse_args()
    products = prepare(json.loads(args.parent.read_text()), json.loads(args.working.read_text()),
                       json.loads(args.proofs.read_text()))
    args.output.write_text(json.dumps(products, ensure_ascii=False, indent=2))
    print(json.dumps({'drafts': len(products), 'photosPerProduct': 1,
                      'realProductDestinations': len(products), 'shopifyWrites': 0}))
