"""Bundle reviewed data for a later importer, with every release still blocked.

This is an offline data plan using a read-only definition snapshot. It contains no Shopify operations,
publication state, invented stock or executable import transport.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
from build_shop_identity_review import identities, identity_hash
from build_specification_display import build as build_display_audit
from specification_display import POLICY as DISPLAY_POLICY, project as display_specifications


EXPECTED_TARGETS = {
    'benefits': ('custom', 'pluspunten', 'list.single_line_text_field'),
    'specifications': ('custom', 'complete_specificaties', 'json'),
    'choice_group': ('custom', 'switch_group', 'single_line_text_field'),
}


def validate_targets(snapshot):
    if snapshot.get('status') != 'READ_ONLY_DEFINITIONS_VERIFIED' or snapshot.get('owner_type') != 'PRODUCT':
        raise ValueError('A verified read-only product definition snapshot is required')
    targets = snapshot.get('targets', {})
    if set(targets) != set(EXPECTED_TARGETS):
        raise ValueError('All three existing field targets must be checked')
    for role, expected in EXPECTED_TARGETS.items():
        target = targets[role]
        if tuple(target.get(k) for k in ('namespace', 'key', 'type')) != expected or target.get('validations') != []:
            raise ValueError('Definition/type/validation changed; review before rebuilding')
    return targets


def record(product, benefits, targets):
    if (product['vendor'] != 'BRAUER' or product['sku'] != benefits['sku']
            or product['ean'] != benefits['ean'] or product['import_allowed'] is not False):
        raise ValueError('Exact BRAUER/SKU/EAN and blocked article state required')
    texts = [b['text'] for b in benefits['items']]
    if len(texts) > 3 or len(texts) != len(set(texts)):
        raise ValueError('At most three distinct approved benefits required')
    price = product['price_incl_vat']
    if not isinstance(price, str) or Decimal(price).quantize(Decimal('0.01')) != Decimal(price):
        raise ValueError('Preserve the supplied VAT-inclusive decimal price string')
    display_groups, _ = display_specifications(product)
    return {
        'schema':'brauer-offline-import-preparation-2', 'import_allowed':False,
        'release_state':'PREPARED_BLOCKED',
        'identity':{'manufacturer':'BRAUER','sku':product['sku'],'ean':product['ean']},
        'product_data':{'title':product['title'],'vendor':'BRAUER','product_type':product['product_type'],
                        'handle_proposal':product['handle_proposal'],'description':product['description'],
                        'price_incl_vat':price,'vat_rate':product['vat_rate'],
                        'specifications':display_groups,'benefits':texts},
        'configuration':{'family_id':product['family_id'],'option_values':product['options']},
        'metafield_values':[
            {**{k:targets[role][k] for k in ('namespace','key','type')},
             'value':json.dumps(value,ensure_ascii=False,separators=(',',':')) if role != 'choice_group' else value}
            for role,value in [('specifications',display_groups),
                               ('benefits',texts),('choice_group',product['family_id'])]
        ],
        'media':product['media'],
        'review':{'data_issues':product['data_issues'],
                  'user_additions':product.get('user_additions',{}),
                  'source_conflicts':product.get('source_conflicts',{}),
                  'missing_chosen_essential_fields':product['specification_review']['missing_essential_fields'],
                  'retail_open_fields':product.get('retail_review',{}).get('open_fields',[]),
                  'future_available_date':product['future_available_date']},
        'evidence_files':{'article':'catalog.json','technical_facts':'specification-evidence.json',
                          'benefits':'product-benefits.json','choice_groups':'families.json',
                          'field_definitions':'field-targets28.json'},
    }


def build(root):
    prepared = root/'prepared'
    gate = json.loads((prepared/'release-gate.json').read_text())
    if gate.get('import_allowed') is not False:
        raise ValueError('This builder only handles blocked offline preparation')
    targets = validate_targets(json.loads((prepared/'field-targets28.json').read_text()))
    products = json.loads((prepared/'catalog.json').read_text())
    shop_path=prepared/'shop-identity-review30.json'
    shop_review=None
    if shop_path.exists():
        checked=json.loads(shop_path.read_text())
        if (checked.get('status')!='COMPLETE_READ_ONLY' or checked.get('articles_compared')!=len(products)
            or checked.get('catalog_identity_sha256')!=identity_hash(identities(products))
            or checked.get('shopify_writes')!=0 or checked.get('import_allowed') is not False
            or checked.get('search_controls')!='PASS' or checked.get('linked_product_ids_assigned') is not False):
            raise ValueError('Shop identity review is incomplete or does not match these article identities')
        shop_review={k:checked[k] for k in ['status','store_domain','articles_compared','query_batches','query_pages',
            'articles_with_existing_identity_or_handle','review_required_articles','status_counts',
            'catalog_identity_sha256','started_on','finished_on','refresh_required_before_import','linked_product_ids_assigned']}
        shop_review['file']='shop-identity-review30.json'
    benefits = json.loads((prepared/'product-benefits.json').read_text())
    policy = json.loads((prepared/'product-benefits-summary.json').read_text())
    if policy.get('maximum_per_article') != 3:
        raise ValueError('Import preparation requires the reviewed three-benefit policy')
    by = {r['sku']:r for r in benefits}
    if len(by) != len(benefits) or set(by) != {p['sku'] for p in products}:
        raise ValueError('Benefit identities do not partition the catalogue')
    display_audit = build_display_audit(root)
    rows = [record(p, by[p['sku']], targets) for p in products]
    paths = ['catalog.json','specification-evidence.json','product-benefits.json',
             'manufacturer-features.json','families.json','release-gate.json','field-plan.json','field-targets28.json',
             'product-benefits-summary.json']
    hashes = {p:hashlib.sha256((prepared/p).read_bytes()).hexdigest() for p in paths}
    for name in ['specification-display-summary31.json','specification-display-history31.json',
                 'specification-display-review31.json']:
        hashes[name] = hashlib.sha256((prepared/name).read_bytes()).hexdigest()
    if shop_review:
        for name in ['shop-identity-review30.json','shop-identity-controls30.json',
                     'shop-identity-worklist30.json','shop-identity-responses30.jsonl']:
            hashes[name]=hashlib.sha256((prepared/name).read_bytes()).hexdigest()
    payload = ''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows)
    destination = prepared/'import-preparation.jsonl'
    destination.write_text(payload)
    readiness = {
        'schema':'brauer-import-readiness-2','status':'PREPARED_BLOCKED','import_allowed':False,
        'articles':len(rows),'unique_skus':len(by),'unique_eans':len({r['identity']['ean'] for r in rows}),
        'sku_per_product':1,'articles_with_benefits':sum(bool(r['product_data']['benefits']) for r in rows),
        'benefits':sum(len(r['product_data']['benefits']) for r in rows),
        'maximum_benefits_per_article':3,'benefit_policy_version':policy['version'],
        'specification_display_policy':DISPLAY_POLICY,
        'specification_display':{k:v for k,v in display_audit.items() if k != 'source_sha256'},
        'price_policy':'Exact supplier-derived price incl. 21% VAT retained; no extra VAT multiplication',
        'inventory_quantities_assigned':False,'shopify_writes':0,'executable_importer_included':False,
        'product_benefit_destination':'custom.pluspunten',
        'benefit_mapping_status':'EXISTING_DEFINITION_TYPE_VERIFIED_RENDERER_PENDING',
        'existing_field_targets':targets,'metafield_values_prepared':3*len(rows),
        'definition_check_is_not_renderer_or_import_approval':True,
        'shop_identity_comparison':shop_review,
        'data_plan':'import-preparation.jsonl','data_plan_sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),
        'source_sha256':hashes,'release_gate_preserved':True,
        'blocking_steps':['Receive complete official media','Inventory and review exact media links',
                          'Resolve required article/source issues','Shop-wide SKU/EAN/handle comparison',
                          'Recheck existing field and collection mappings','Verify integration in an unpublished theme',
                          'Review a representative full product and selector pilot','Explicit merchant import release'],
        'official_manuals_are_research_only':True,'official_complete_media_received':False,
        'technical_completion_not_inferred_from_benefits':True,
    }
    (prepared/'import-readiness.json').write_text(json.dumps(readiness,ensure_ascii=False,indent=2)+'\n')
    return {k:v for k,v in readiness.items() if k not in {'source_sha256','blocking_steps'}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    print(json.dumps(build(parser.parse_args().root),ensure_ascii=False))
