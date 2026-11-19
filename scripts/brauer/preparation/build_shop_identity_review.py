"""Plan store-wide identifier reads or compare their saved read-only receipts.

This utility has no network transport, credentials, product writes or importer.
The connector performs the queries; this module verifies complete coverage.
"""
import argparse
from collections import Counter,defaultdict
import hashlib
import json
from pathlib import Path


def identities(catalogue):
    if any(p.get('vendor')!='BRAUER' for p in catalogue):raise ValueError('BRAUER catalogue required')
    rows=[{'sku':p['sku'],'ean':p['ean'],'handle':p['handle_proposal']} for p in catalogue]
    for key in ['sku','ean','handle']:
        if any(not isinstance(x[key],str) or not x[key] for x in rows) or len({x[key] for x in rows})!=len(rows):
            raise ValueError('Nonempty unique string identities required')
    return rows


def identity_hash(rows):
    return hashlib.sha256(json.dumps(rows,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def plan(catalogue):
    rows=identities(catalogue);batches=[]
    for start in range(0,len(rows),50):
        part=rows[start:start+50]
        batches.append({'batch':len(batches),'articles':part,
          'variant_query':' OR '.join(term for p in part for term in ['sku:'+json.dumps(p['sku']),'barcode:'+json.dumps(p['ean'])]),
          'handle_query':' OR '.join('handle:'+json.dumps(p['handle']) for p in part)})
    return {'schema':'brauer-read-only-identity-worklist-1','articles':len(rows),'batches':batches,
            'identity_sha256':identity_hash(rows),'shopify_writes':0,'import_allowed':False}


def compare(catalogue,worklist,responses,controls):
    expected=plan(catalogue)
    if worklist!=expected:raise ValueError('Worklist changed or no longer matches the catalogue identities')
    required=['read_only','sku_positive','sku_negative_empty','barcode_positive',
              'handle_positive','handle_negative_empty','bulk_last_term_positive','no_vendor_filter']
    if (controls.get('status')!='PASS' or any(controls.get(k) is not True for k in required)
        or controls.get('store_domain')!='badkamercity.nl' or controls.get('shopify_writes')!=0):
        raise ValueError('Verified read-only search controls on the intended store are required')
    batch_ids=[x['batch'] for x in responses]
    if len(batch_ids)!=len(set(batch_ids)) or set(batch_ids)!=set(range(len(expected['batches']))):
        raise ValueError('Every query batch must be received exactly once')
    variants={};products={};query_pages=0
    for response in responses:
        pages=response.get('pages',[])
        if response.get('status')!='COMPLETE' or not pages:raise ValueError('Incomplete query receipt')
        last=pages[-1]
        if last['variants']['pageInfo']['hasNextPage'] or last['products']['pageInfo']['hasNextPage']:
            raise ValueError('Pagination is not finished')
        query_pages+=len(pages)
        for page in pages:
            for variant in page['variants']['nodes']:
                if variant['barcodes']['pageInfo']['hasNextPage']:raise ValueError('Barcode aliases not fully read')
                if variant['id'] in variants and variants[variant['id']]!=variant:
                    raise ValueError('Variant changed during the read; recheck its identity')
                variants[variant['id']]=variant
            for product in page['products']['nodes']:
                if product['id'] in products and products[product['id']]!=product:
                    raise ValueError('Product changed during the read; recheck its handle')
                products[product['id']]=product
    skus=defaultdict(dict);eans=defaultdict(dict);handles=defaultdict(list)
    for v in variants.values():
        if v.get('sku'):skus[v['sku'].strip().casefold()][v['id']]=v
        for b in v['barcodes']['nodes']:eans[b['value']][v['id']]=v
    for product in products.values():handles[product['handle']].append(product)
    rows=[]
    for identity in identities(catalogue):
        found=dict(skus.get(identity['sku'].strip().casefold(),{}));found.update(eans.get(identity['ean'],{}))
        found=list(found.values());handle_products=handles.get(identity['handle'],[])
        exact=[v for v in found if v['sku']==identity['sku']
               and identity['ean'] in {b['value'] for b in v['barcodes']['nodes']}
               and v['product']['vendor'].strip().casefold()=='brauer']
        other_handles=[p for p in handle_products if p['id'] not in {v['product']['id'] for v in exact}]
        if len(found)>1:state='MULTIPLE_EXISTING_VARIANTS_REVIEW'
        elif other_handles:state='HANDLE_COLLISION_REVIEW'
        elif len(exact)==1:state='MATCH_EXISTING_EXACT_BRAUER_SKU_EAN'
        elif found:state='IDENTITY_COLLISION_REVIEW'
        else:state='NO_EXISTING_IDENTITY_FOUND'
        rows.append({'sku':identity['sku'],'ean':identity['ean'],'handle_proposal':identity['handle'],
                     'status':state,'existing_variants':found,'existing_handle_products':handle_products,
                     'import_allowed':False,'linked_product_id_assigned':False})
    counts=Counter(row['status'] for row in rows)
    return {'schema':'brauer-read-only-shop-identity-review-1','status':'COMPLETE_READ_ONLY',
      'store_domain':controls['store_domain'],'started_on':controls.get('started_on'),'finished_on':controls.get('finished_on'),
      'articles_compared':len(rows),'query_batches':len(responses),'query_pages':query_pages,
      'unique_variant_search_hits':len(variants),'unique_handle_search_hits':len(products),
      'articles_with_existing_identity_or_handle':sum(row['status']!='NO_EXISTING_IDENTITY_FOUND' for row in rows),
      'review_required_articles':sum(row['status'].endswith('_REVIEW') for row in rows),'status_counts':dict(counts),
      'catalog_identity_sha256':expected['identity_sha256'],'scope':'All catalogue SKU, EAN and proposed handle values searched across the connected store without a vendor filter; exact returned values compared.',
      'search_controls':'PASS','refresh_required_before_import':True,'shopify_writes':0,'import_allowed':False,
      'linked_product_ids_assigned':False,'not_an_import_release':True,'articles':rows}


def build(root,plan_only=False):
    p=root/'prepared';catalogue=json.loads((p/'catalog.json').read_text())
    if plan_only:
        result=plan(catalogue);destination=p/'shop-identity-worklist30.json'
    else:
        work=json.loads((p/'shop-identity-worklist30.json').read_text())
        responses=[json.loads(line) for line in (p/'shop-identity-responses30.jsonl').read_text().splitlines() if line.strip()]
        controls=json.loads((p/'shop-identity-controls30.json').read_text())
        result=compare(catalogue,work,responses,controls);destination=p/'shop-identity-review30.json'
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return {k:v for k,v in result.items() if k not in {'articles','batches'}}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('root',nargs='?',type=Path,default=Path('.'))
    parser.add_argument('--plan-only',action='store_true');args=parser.parse_args()
    print(json.dumps(build(args.root,args.plan_only),ensure_ascii=False))
