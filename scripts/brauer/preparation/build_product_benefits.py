"""Derive short customer benefits from approved facts of the same exact article.

No research, variant inheritance, complete-set promise or Shopify writes.
"""
import argparse
from collections import Counter
import copy
import json
from pathlib import Path

VERSION = 'brauer-benefits-1'
MAX_BENEFITS = 4
TAPS = {
    'Inbouwdouchesets', 'Inbouwbadkranen', 'Opbouwbadkranen',
    'Opbouwdouchekranen', 'Inbouwwastafelkranen', 'Opbouwwastafelkranen',
    'Inbouwfonteinkranen', 'Opbouwfonteinkranen', 'Vrijstaande badkranen',
    'Losse inbouwthermostaten', 'Douchepanelen', 'Uitlopen',
}
GLASS = {'Douchecabines', 'Nisdeuren', 'Inloopdouches', 'Badwanden', 'Losse glasdelen', 'Setgebonden glasdelen'}
KINDS = {'supplier', 'previous_exact_sku_audit', 'retailer_exact_sku_ean'}


def derive(product, evidence):
    """Return display text together with the exact already-approved field proof."""
    if (product.get('vendor') != 'BRAUER' or not product.get('sku')
            or not product.get('ean') or evidence.get('ean') != product['ean']):
        return []
    specifications = product.get('specifications', {})
    blocked = set(product.get('retail_review', {}).get('open_fields', []))
    blocked.update(product.get('measurement_hold', {}).get('fields', []))
    blocked.update(product.get('source_conflicts', {}))
    facts = evidence.get('facts', {})

    def fact(field, accepted=None):
        value = specifications.get(field)
        proof = facts.get(field, {})
        if (field in blocked or value in (None, '') or proof.get('kind') not in KINDS
                or not proof.get('field') or not proof.get('fragment')
                or (accepted is not None and value not in accepted)):
            return None
        if proof['kind'] == 'supplier':
            if not proof.get('source_refs'):
                return None
        elif not proof.get('url'):
            return None
        if 'badkamervoorjou.nl' in str(proof).lower():
            return None
        return {'field': field, 'value': value, 'evidence': copy.deepcopy(proof)}

    items = []

    def add(rule, text, required):
        proofs = [fact(field, accepted) for field, accepted in required]
        if not all(proofs):
            return False
        items.append({'rule': rule, 'text': text, 'basis': proofs})
        return True

    typ = product.get('product_type')
    yes = {'Ja'}
    bundle_has_body = False
    if typ == 'Inbouwdouchesets':
        core = [('Hoofddouche inbegrepen', yes), ('Handdouche inbegrepen', yes)]
        bundle_has_body = add('shower_bundle_with_body',
                             'Inclusief hoofd- en handdouche, slang en inbouwdeel',
                             core + [('Doucheslang inbegrepen', yes), ('Inbouwdeel inbegrepen', yes)])
        if not bundle_has_body:
            if not add('shower_bundle_with_hose', 'Hoofd- en handdouche met doucheslang',
                       core + [('Doucheslang inbegrepen', yes)]):
                add('shower_bundle', 'Met hoofd- en handdouche', core)
    if typ in TAPS:
        if not bundle_has_body:
            add('included_body', 'Inclusief inbouwdeel', [('Inbouwdeel inbegrepen', yes)])
        # Explicit contradictions suppress the whole outlet benefit.
        outlet_fields = {'Draaibare uitloop', 'Uitvoering uitloop'}
        negative = (specifications.get('Draaibare uitloop') == 'Nee'
                    or specifications.get('Uitvoering uitloop') in {'Vaste uitloop', 'Niet draaibaar'})
        if not negative and not blocked.intersection(outlet_fields):
            if not add('rotating_outlet', 'Draaibare uitloop', [('Draaibare uitloop', yes)]):
                add('rotating_outlet', 'Draaibare uitloop', [('Uitvoering uitloop', {'Draaibaar', 'Draaibare uitloop'})])
        add('thermostatic', 'Thermostatische bediening', [('Thermostatisch', yes)])
    if typ in TAPS or typ == 'Handdouches en houders':
        modes = specifications.get('Aantal straalstanden handdouche')
        if modes in {'2', '3', '4', '5', '6'}:
            add('handshower_modes', f'Handdouche met {modes} straalstanden',
                [('Handdouche inbegrepen', yes), ('Aantal straalstanden handdouche', {modes})]
                if typ == 'Inbouwdouchesets' else [('Aantal straalstanden handdouche', {modes})])
    if typ in TAPS:
        add('cold_start', 'Met koudestartfunctie', [('Koudestartfunctie', yes)])
    if typ in GLASS:
        add('glass_coating', 'Glas voorzien van coating', [('Glascoating', yes)])
        add('reversible_glass', 'Links of rechts te monteren',
            [('Montage', {'Links/rechts', 'Links of rechts te monteren'})])
    if typ in {'Onderkasten', 'Spiegelkasten'}:
        add('soft_close', 'Softclose sluiting', [('Softclose', yes)])
    return items[:MAX_BENEFITS]


def build(root):
    prepared = root / 'prepared'
    catalog = json.loads((prepared / 'catalog.json').read_text())
    evidence = json.loads((prepared / 'specification-evidence.json').read_text())
    records = []
    counts = Counter()
    for product in catalog:
        items = derive(product, evidence.get(product['sku'], {}))
        counts.update(item['rule'] for item in items)
        records.append({'sku': product['sku'], 'ean': product['ean'],
                        'product_type': product['product_type'], 'items': items})
    summary = {'version': VERSION, 'articles': len(catalog),
               'articles_with_benefits': sum(bool(r['items']) for r in records),
               'benefits': sum(len(r['items']) for r in records),
               'maximum_per_article': MAX_BENEFITS, 'by_rule': dict(sorted(counts.items())),
               'new_external_facts': 0, 'specification_fields_changed': 0,
               'complete_set_claims': 0, 'shopify_writes': 0, 'import_allowed': False}
    for path, obj in [('product-benefits.json', records),
                      ('product-benefits-summary.json', summary)]:
        (prepared / path).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    print(json.dumps(build(parser.parse_args().root), ensure_ascii=False))
