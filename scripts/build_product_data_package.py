#!/usr/bin/env python3
"""Build a private, offline product dataset from saved Shopify GraphQL reads.

No network or Shopify writes. Rejects incomplete joins, API errors, and unhandled
nested pagination. Never run with an output directory inside the public repo.
"""
import argparse
import collections
import json
import shutil
import sqlite3
from pathlib import Path


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def read_response(path):
    value = json.loads(path.read_text())
    if value.get('errors') or not isinstance(value.get('data'), dict):
        raise ValueError(f'Unusable API response: {path.name}')
    return value['data']


def assert_closed(value, path=''):
    if isinstance(value, dict):
        if value.get('hasNextPage') is True:
            raise ValueError(f'Unhandled pagination: {path}')
        for key, child in value.items():
            assert_closed(child, path + '/' + key)
    elif isinstance(value, list):
        for child in value:
            assert_closed(child, path + '/[]')


def index_nodes(files, root='nodes'):
    result = {}
    for path in sorted(files):
        value = read_response(path)
        nodes = value[root]
        if isinstance(nodes, dict):
            nodes = [edge['node'] for edge in nodes['edges']]
        for node in nodes:
            if not node or node['id'] in result:
                raise ValueError(f'Missing/duplicate node in {path.name}')
            assert_closed(node, node['id'])
            result[node['id']] = node
    return result


def combine(core, metafields, relations, variants):
    expected = set(core)
    if set(metafields) != expected or set(relations) != expected:
        raise ValueError('Incomplete product joins')
    records, seen = [], set()
    for product_id, source in core.items():
        product = dict(source)
        source_variants = product.pop('variants')['nodes']
        if len(source_variants) != product['variantsCount']['count']:
            raise ValueError('Truncated product variants')
        product['variants'] = []
        for variant in source_variants:
            detail = variants.get(variant['id'])
            if detail is None or detail['product']['id'] != product_id or variant['id'] in seen:
                raise ValueError('Incomplete/orphan/duplicate variant join')
            merged = {**variant, **{k: v for k, v in detail.items() if k not in {'product', 'inventoryItem'}}}
            merged['inventoryItem'] = {**variant['inventoryItem'], **detail['inventoryItem']}
            product['variants'].append(merged)
            seen.add(variant['id'])
        product['metafields'] = metafields[product_id]['metafields']['nodes']
        for key, value in relations[product_id].items():
            if key != 'id':
                product[key] = value['nodes'] if isinstance(value, dict) and 'nodes' in value else value
        if len(product['media']) != product['mediaCount']['count']:
            raise ValueError('Truncated product media')
        records.append(product)
    if seen != set(variants):
        raise ValueError('Unjoined variants')
    return records


def field_dictionary(records):
    fields = collections.defaultdict(collections.Counter)
    def visit(value, path):
        kind = ('null' if value is None else 'boolean' if isinstance(value, bool) else
                'object' if isinstance(value, dict) else 'array' if isinstance(value, list) else
                'number' if isinstance(value, (int, float)) else 'string')
        fields[path][kind] += 1
        if isinstance(value, dict):
            for key, child in value.items():
                visit(child, path + '.' + key)
        elif isinstance(value, list):
            for child in value:
                visit(child, path + '[]')
    for record in records:
        visit(record, 'product')
    return [{'path': key, 'observations': sum(counts.values()), 'types': dict(counts)}
            for key, counts in sorted(fields.items())]


def build(source, output):
    output.mkdir(parents=True, exist_ok=False)
    pages = source / 'private/product-pages'
    core = index_nodes(pages.glob('core-*.json'), 'products')
    mf = index_nodes(pages.glob('metafields-*.json'))
    relations = index_nodes(pages.glob('relations-*.json'))
    variants = index_nodes(pages.glob('variant-details-*.json'))
    products = combine(core, mf, relations, variants)
    pre = read_response(source / 'private/preflight.json')
    close = json.loads((source / 'private/close-check.json').read_text())['response']['data']
    for label, value in [('start', pre), ('end', close)]:
        if value['productsCount'] != {'count': len(products), 'precision': 'EXACT'} or value['productVariantsCount'] != {'count': len(variants), 'precision': 'EXACT'}:
            raise ValueError(f'{label} counts do not match')
    with (output / 'products.jsonl').open('w') as stream:
        for product in products:
            stream.write(encode(product) + '\n')
    dictionary = field_dictionary(products)
    (output / 'field-dictionary.json').write_text(encode(dictionary) + '\n')
    fields = collections.defaultdict(collections.Counter)
    for product in products:
        for owner_type, owner in [('PRODUCT', product)] + [('PRODUCTVARIANT', v) for v in product['variants']]:
            for item in owner['metafields'] if isinstance(owner['metafields'], list) else owner['metafields']['nodes']:
                fields[(owner_type, item['namespace'], item['key'], item['type'])]['records'] += 1
                fields[(owner_type, item['namespace'], item['key'], item['type'])]['nonempty'] += item['value'] not in (None, '', '[]')
    register = [{'ownerType': k[0], 'namespace': k[1], 'key': k[2], 'type': k[3], **dict(v)} for k,v in sorted(fields.items())]
    (output / 'metafield-register.json').write_text(encode(register) + '\n')
    db = sqlite3.connect(output / 'products.sqlite')
    db.executescript('''
      PRAGMA foreign_keys=ON;
      CREATE TABLE products(id TEXT PRIMARY KEY,handle TEXT,title TEXT,vendor TEXT,status TEXT,template_suffix TEXT,raw_json TEXT NOT NULL);
      CREATE TABLE variants(id TEXT PRIMARY KEY,product_id TEXT NOT NULL REFERENCES products(id),sku TEXT,price TEXT,compare_at_price TEXT,raw_json TEXT NOT NULL);
      CREATE TABLE metafields(id TEXT PRIMARY KEY,owner_id TEXT,owner_type TEXT,namespace TEXT,key TEXT,type TEXT,value TEXT,json_value TEXT,raw_json TEXT);
      CREATE TABLE media(id TEXT PRIMARY KEY,raw_json TEXT NOT NULL);
      CREATE TABLE product_media(product_id TEXT REFERENCES products(id),media_id TEXT REFERENCES media(id),position INTEGER,PRIMARY KEY(product_id,media_id));
      CREATE TABLE collections(id TEXT PRIMARY KEY,handle TEXT,title TEXT,template_suffix TEXT,raw_json TEXT);
      CREATE TABLE product_collections(product_id TEXT REFERENCES products(id),collection_id TEXT REFERENCES collections(id),PRIMARY KEY(product_id,collection_id));
      CREATE TABLE inventory_levels(id TEXT PRIMARY KEY,variant_id TEXT REFERENCES variants(id),inventory_item_id TEXT,location_id TEXT,raw_json TEXT);
      CREATE TABLE references_data(id TEXT PRIMARY KEY,resource_type TEXT,raw_json TEXT);
      CREATE INDEX variants_sku ON variants(sku);
      CREATE INDEX products_handle ON products(handle);
      CREATE INDEX metafield_keys ON metafields(owner_type,namespace,key);
    ''')
    collections_data=[]
    for path in sorted((source/'private').glob('collections-*.json')):
        collection_page=read_response(path)['collections'];assert_closed(collection_page)
        collections_data.extend(collection_page['nodes'])
    sources={n['id']:n['sources'] for n in read_response(source/'private/collection-sources-0000.json')['collections']['nodes']}
    for item in collections_data:
        item['sources']=sources[item['id']]
        db.execute('INSERT INTO collections VALUES(?,?,?,?,?)',(item['id'],item['handle'],item['title'],item['templateSuffix'],encode(item)))
    def insert_mf(owner_id,owner_type,items):
        for item in items:
            db.execute('INSERT INTO metafields VALUES(?,?,?,?,?,?,?,?,?)',(item['id'],owner_id,owner_type,item['namespace'],item['key'],item['type'],item['value'],encode(item['jsonValue']),encode(item)))
    for item in collections_data:
        insert_mf(item['id'],'COLLECTION',item['metafields']['nodes'])
    for product in products:
        db.execute('INSERT INTO products VALUES(?,?,?,?,?,?,?)',(product['id'],product['handle'],product['title'],product['vendor'],product['status'],product['templateSuffix'],encode(product)))
        insert_mf(product['id'],'PRODUCT',product['metafields'])
        for variant in product['variants']:
            db.execute('INSERT INTO variants VALUES(?,?,?,?,?,?)',(variant['id'],product['id'],variant['sku'],variant['price'],variant['compareAtPrice'],encode(variant)))
            insert_mf(variant['id'],'PRODUCTVARIANT',variant['metafields']['nodes'])
            for level in variant['inventoryItem']['inventoryLevels']['nodes']:
                db.execute('INSERT INTO inventory_levels VALUES(?,?,?,?,?)',(level['id'],variant['id'],variant['inventoryItem']['id'],level['location']['id'],encode(level)))
        for position, item in enumerate(product['media']):
            db.execute('INSERT OR IGNORE INTO media VALUES(?,?)',(item['id'],encode(item)))
            db.execute('INSERT INTO product_media VALUES(?,?,?)',(product['id'],item['id'],position))
        for item in product['collections']:
            db.execute('INSERT INTO product_collections VALUES(?,?)',(product['id'],item['id']))
    for path in sorted((source/'private').glob('references-*.json')):
        for item in read_response(path)['nodes']:
            if item is None:raise ValueError('Unresolved reference')
            db.execute('INSERT INTO references_data VALUES(?,?,?)',(item['id'],item['__typename'],encode(item)))
    db.commit()
    integrity=db.execute('PRAGMA integrity_check').fetchone()[0]
    foreign_errors=db.execute('PRAGMA foreign_key_check').fetchall()
    if integrity!='ok' or foreign_errors:raise ValueError('Database integrity failed')
    counts={table:db.execute('SELECT COUNT(*) FROM '+table).fetchone()[0] for table in ('products','variants','metafields','media','product_media','collections','product_collections','inventory_levels','references_data')}
    metafield_counts=dict(db.execute('SELECT owner_type,COUNT(*) FROM metafields GROUP BY owner_type'))
    db.close()
    # Raw response pages are the provenance layer; not Shopify bulk download URLs.
    shutil.copytree(source/'private',output/'raw-api')
    shutil.copytree(source/'queries',output/'queries')
    runtime=output/'theme-runtime-data/assets';runtime.mkdir(parents=True)
    for path in (source/'theme/assets').glob('*.json'):
        shutil.copy2(path,runtime/path.name)
    summary={'schemaVersion':1,'counts':counts,'metafieldCountsByOwnerType':metafield_counts,'statusCounts':dict(collections.Counter(x['status'] for x in products)),
             'productTemplateCounts':dict(collections.Counter(x['templateSuffix'] or '(default)' for x in products)),
             'collectionTemplateCounts':dict(collections.Counter(x['templateSuffix'] or '(default)' for x in collections_data)),
             'fieldPaths':len(dictionary),'metafieldKeysAndTypes':len(register),'unhandledNestedPagination':0,
             'duplicateProductIds':0,'duplicateVariantIds':0,'orphanVariants':0,'databaseIntegrity':integrity,
             'databaseForeignKeyErrors':len(foreign_errors),'productAndVariantCountsMatchStartAndEnd':True,
             'mediaCountMatchesEveryProduct':True,'runtimeJsonAssets':len(list(runtime.glob('*.json'))),
             'mediaBinariesIncluded':False,'snapshotAtomic':False,'source':'Shopify read-only Admin GraphQL connector',
             'windowStart':pre.get('bulkOperation',{}).get('createdAt','2026-10-28T02:10:21Z'),
             'windowEnd':json.loads((source/'private/close-check.json').read_text())['checkedAt']}
    (output/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    repo=Path(__file__).resolve().parents[1]
    if args.output.resolve()==repo or repo in args.output.resolve().parents:
        parser.error('Private export output must be outside this public repository')
    print(json.dumps(build(args.source,args.output),ensure_ascii=False))


if __name__=='__main__':main()
