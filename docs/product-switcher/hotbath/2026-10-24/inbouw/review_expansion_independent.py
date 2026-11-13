import collections
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
sources = {part: json.loads((BASE / f'expansion-{part}.json').read_text()) for part in 'abc'}
live = json.loads((BASE / 'expansion-live-products.json').read_text())['products']
index = collections.defaultdict(list)
for product in live:
    for variant in product['variants']['nodes']:
        index[variant['sku']].append((product, variant))

ready = {}
models = set()
failures = []
source_counts = {}
for part, source in sources.items():
    count = 0
    for mapping in source['mappings']:
        if mapping['status'] != 'VERIFIED_BOOK':
            continue
        skus = mapping.get('approved_skus', mapping.get('approved_finish_skus', mapping['matched_skus']))
        finishes = mapping.get('book_colors', mapping.get('book_finishes', mapping.get('book_confirmed_finishes', [])))
        if skus:
            models.add(mapping['trim_model'])
        for sku in skus:
            body = mapping['body_sku']
            model = mapping['trim_model']
            if sku in ready and ready[sku]['body_sku'] != body:
                failures.append({'type':'conflicting_body', 'sku':sku})
            ready[sku] = {'body_sku':body,'trim_model':model}
            if not sku.startswith(model) or sku[len(model):] not in finishes:
                failures.append({'type':'unproven_finish', 'sku':sku,'part':part})
            if 'SPOM' in sku or 'SPOM' in body or sku.startswith('IBS'):
                failures.append({'type':'excluded', 'sku':sku})
            for candidate, role in [(sku,'trim'),(body,'body')]:
                matches = index[candidate]
                if len(matches) != 1:
                    failures.append({'type':'live_match_not_unique', 'sku':candidate,'role':role})
                    continue
                product, variant = matches[0]
                if product['status'] != 'ACTIVE' or not product.get('publishedAt') or not variant['availableForSale']:
                    failures.append({'type':'not_active_published_available', 'sku':candidate,'role':role})
                if product['variants']['pageInfo']['hasNextPage']:
                    failures.append({'type':'variants_incomplete', 'sku':candidate,'role':role})
                if role == 'trim' and product.get('included') and product['included']['value'] == 'true':
                    failures.append({'type':'body_already_included', 'sku':candidate})
            count += 1
    source_counts[part] = count

old = json.loads((BASE / 'book_mapping_review.json').read_text())
old_skus = {p['sku'] for m in old['mappings'] for p in m['current_trim_products']}
old_overlap = sorted(old_skus.intersection(ready))
if old_overlap:
    failures.append({'type':'old31_duplicate_skus','skus':old_overlap})
if len(models) != 94 or len(ready) != 460:
    failures.append({'type':'unexpected_counts','models':len(models),'skus':len(ready)})

consolidated_path = BASE/'expansion-consolidated.json'
consolidated_check = {'checked':False}
if consolidated_path.exists():
    consolidated = json.loads(consolidated_path.read_text())
    consolidated_rows = [s for r in consolidated['records'] for s in r['ready_skus']]
    consolidated_ready = {s['trim_sku']:s['body_sku'] for s in consolidated_rows}
    if len(consolidated_rows) != len(consolidated_ready):
        failures.append({'type':'consolidated_duplicate_ready_sku'})
    if consolidated_ready != {sku:r['body_sku'] for sku,r in ready.items()}:
        failures.append({'type':'consolidated_ready_set_differs'})
    for row in consolidated_rows:
        trim, variant = index[row['trim_sku']][0]
        body, body_variant = index[row['body_sku']][0]
        if row['trim_variant_id'] != variant['id'] or row['body_variant_id'] != body_variant['id'] or row['trim_product_id'] != trim['id'] or row['trim_handle'] != trim['handle']:
            failures.append({'type':'consolidated_identity_mismatch','sku':row['trim_sku']})
        if row['quantity_per_trim'] != 1:
            failures.append({'type':'consolidated_quantity_mismatch','sku':row['trim_sku']})
    if consolidated['summary']['installed'] is not False:
        failures.append({'type':'consolidated_wrong_installation_status'})
    consolidated_check = {'checked':True,'ready_rows':len(consolidated_rows),'same_as_independently_derived_set':consolidated_ready == {sku:r['body_sku'] for sku,r in ready.items()},'sha256':hashlib.sha256(consolidated_path.read_bytes()).hexdigest()}

visual_checks = [
    {'trim_model':'GT187EXT','body_sku':'HBCB177','printed_page':35,'pdf_page':37,'finishes':['IX'],'result':'PASS','detail':'Drawing and price table independently identify the same trim and body.'},
    {'trim_model':'GY005DEXT20','body_sku':'HBGY031','printed_page':127,'pdf_page':129,'finishes':['GN','TB','MBP','BBP'],'result':'PASS','detail':'Left20cm table is explicitly GY005DEXT20, right table is GY005DEXT25; both bodies HBGY031. Table heading and suffixes read directly.'},
    {'trim_model':'KHDS3EXT','body_sku':'HBKHDS3','printed_page':176,'pdf_page':178,'finishes':['CR','GN','BB','AB','WH','AI','PBP','MBP','BBP','BCP'],'result':'PASS','detail':'AI has an explicit dedicated price row, resolving the omission from p367. The cross-source ready list may include KHDS3EXTAI.'},
    {'trim_model':'PB009QEXT','body_sku':'HBPB009','printed_page':196,'pdf_page':198,'finishes':['CR','GN','BB','AB','WH','AI','PBP','MBP','BBP','BCP'],'result':'PASS','detail':'Right square model table separately names PB009QEXT and HBPB009. No column swapping.'},
    {'trim_model':'CW011EXT','body_sku':'HBCB011','printed_page':232,'pdf_page':234,'finishes':['CR','GN','BBP'],'result':'PASS','detail':'Right table and drawings say HBCB011, not inferred HBCW011.'},
    {'trim_model':'GL177EXT','body_sku':'HBCB177','printed_page':249,'pdf_page':251,'finishes':['CR','GN','BGP','BBP'],'result':'PASS_WITH_PRODUCT_DATA_HOLD','detail':'Table abbreviation GL177 resolved by visible GL177EXT drawing label and HBCB177 body label. GN is sole ready SKU; CR/BBP/BGP held due fresh included=true.'},
]
hashes = {f'expansion-{p}.json':hashlib.sha256((BASE/f'expansion-{p}.json').read_bytes()).hexdigest() for p in 'abc'}
hashes['expansion-live-products.json'] = hashlib.sha256((BASE/'expansion-live-products.json').read_bytes()).hexdigest()
result = {
    'schema':'hotbath-inbouw-expansion-independent-review-v1',
    'reviewer':'inbouw_expand_c','read_only':True,
    'verdict':'PASS_READY_FOR_IMPLEMENTATION_CANDIDATES' if not failures else 'HOLD',
    'installation_status':'NOT_IMPLEMENTED_NOT_DEPLOYED',
    'new_ready_models':len(models),'new_ready_unique_skus':len(ready),
    'source_ready_sku_counts_before_cross_source_dedup':source_counts,
    'prior31_overlap_skus':old_overlap,'failures':failures,
    'checks':{
        'exact_model_and_explicit_finish':not any(x['type']=='unproven_finish' for x in failures),
        'single_body_per_ready_sku':not any(x['type']=='conflicting_body' for x in failures),
        'fresh_exact_trim_and_body_identity_active_published_available':not failures,
        'included_true_excluded':not any(x['type']=='body_already_included' for x in failures),
        'spom_and_ibs_excluded':not any(x['type']=='excluded' for x in failures),
        'review_missing_body_and_rails_not_promoted':True,
        'all_c_ready_skus_duplicate_of_a_or_b':source_counts['a']+source_counts['b']==len(ready),
    },
    'visual_sample_checks':visual_checks,
    'cross_source_resolution':{
        'sku':'KHDS3EXTAI','resolution':'CONFIRMED_FROM_PRINTED176',
        'action':'Use B explicit table evidence; C page367 omission alone no longer requires a hold.'
    },
    'limits':[
        'Independent review inspected six representative source pages plus mechanical checks of all candidate records; it does not claim a second visual read of every page.',
        'Ready means a source-backed implementation candidate with verified current identifiers, not a deployed product-page or tested cart implementation.',
        'Consolidated output was still being written; this review validates the three source datasets and derives expected deduplicated output independently.',
        'Availability and identity should be refreshed again at implementation or deployment time.'
    ],
    'source_sha256':hashes,
    'consolidated_output_check':consolidated_check,
}
if consolidated_check['checked']:
    result['limits'].remove('Consolidated output was still being written; this review validates the three source datasets and derives expected deduplicated output independently.')
(BASE/'expansion-independent-review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['verdict','new_ready_models','new_ready_unique_skus','failures']},indent=2))
