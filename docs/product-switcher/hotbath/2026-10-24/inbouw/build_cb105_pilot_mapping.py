"""Prepare an exact, source-backed CB105 add-on proposal. Never writes Shopify."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODELS = {
    'CB105EXT18': ('HBCB105', 170, 172),
    'CB105EXT25': ('HBCB105', 170, 172),
    'CB105TEXT18': ('HBCB105T', 171, 173),
    'CB105TEXT25': ('HBCB105T', 171, 173),
}
FINISHES = {'CR', 'GN', 'BB', 'AB', 'WH', 'AI', 'PBP', 'MBP', 'BBP', 'BCP'}

def build():
    live = json.loads((HERE / 'shopify-cb105-family.json').read_text())
    book = json.loads((HERE / 'book_mapping_review.json').read_text())
    assert not live['pageInfo']['hasNextPage'], 'Incomplete product read'
    indexed = {}
    for product in live['nodes']:
        variants = product['variants']
        assert not variants['pageInfo']['hasNextPage']
        assert len(variants['nodes']) == 1, 'Variant selection requires review'
        variant = variants['nodes'][0]
        sku = variant['sku']
        assert sku and sku not in indexed, 'Empty or duplicate SKU'
        assert product['status'] == 'ACTIVE' and product['publishedAt']
        indexed[sku] = (product, variant)
    book_models = {row['trim_model']: row for row in book['mappings']}
    records = []
    for model, (body_sku, printed_page, pdf_page) in MODELS.items():
        source = book_models[model]
        assert source['body_sku'] == body_sku
        assert source['body_quantity_per_trim_unit'] == 1
        assert any(e['table_pair_present'] and e['printed_page'] == printed_page and e['pdf_page'] == pdf_page for e in source['evidence'])
        body_product, body_variant = indexed[body_sku]
        assert body_variant['availableForSale']
        expected = {model + finish for finish in FINISHES}
        assert {p['sku'] for p in source['current_trim_products']} == expected
        for sku in sorted(expected):
            product, variant = indexed[sku]
            assert product.get('included') == {'type': 'boolean', 'value': 'false'}, 'Inclusion unknown or included'
            assert 'afbouwdeel' in product['title'].lower()
            assert not product.get('components'), 'Existing component data needs review'
            assert 'SPOM' not in sku and not sku.startswith('IBS')
            assert body_product['id'] != product['id'] and body_variant['id'] != variant['id']
            records.append({
                'trim_sku': sku, 'trim_model': model,
                'trim_product_id': product['id'], 'trim_variant_id': variant['id'],
                'trim_handle': product['handle'],
                'body_sku': body_sku, 'body_product_id': body_product['id'],
                'body_variant_id': body_variant['id'], 'body_handle': body_product['handle'],
                'body_quantity_per_trim_unit': 1,
                'body_included_in_trim': False,
                'source': {'catalogue': 'Hotbath Editie 18', 'printed_page': printed_page, 'pdf_page': pdf_page},
                'compatibility_status': 'VERIFIED_BOOK_AND_CURRENT_SHOPIFY',
                'deployment_status': 'PROPOSAL_NOT_INSTALLED',
            })
    assert len(records) == 40
    assert len({r['trim_sku'] for r in records}) == 40
    assert len({r['trim_variant_id'] for r in records}) == 40
    return {
        'schema': 'hotbath-inbouw-exact-pilot-proposal-v1',
        'generated_for_date': '2026-10-24', 'read_only': True, 'installed': False,
        'source_hashes': {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in ['shopify-cb105-family.json', 'book_mapping_review.json']},
        'price_policy': 'Read current body price from the Shopify product at render/cart time; no fixed price in mapping.',
        'quantity_policy': 'Add body quantity equal to requested trim quantity when Yes is explicitly selected; never deduplicate globally by SKU.',
        'selection_policy': 'Preserve explicit Yes/No only for a verified switch to a trim requiring the same body; otherwise ask the choice again.',
        'records': records,
    }

if __name__ == '__main__':
    result = build()
    (HERE / 'cb105-pilot-mapping.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    checks = {'result': 'PASS', 'records': len(result['records']), 'models': len(MODELS), 'bodies': 2, 'unique_exact_variants': True, 'all_explicitly_without_body': True, 'book_table_pairs_verified': True, 'both_body_targets_current_active_published_sellable': True, 'installed': False, 'browser_or_cart_test_of_new_feature': 'NOT_IMPLEMENTED_NOT_TESTED'}
    (HERE / 'pilot-mapping-verification.json').write_text(json.dumps(checks, indent=2) + '\n')
    print(json.dumps(checks))
