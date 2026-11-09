"""Remove proved synonyms from presentation without changing source facts."""
from copy import deepcopy

POLICY = 'brauer-specification-display-1'
HEAD_PRODUCTS = {'Inbouwdouchesets', 'Douchepanelen', 'Hoofddouches'}
TAPS = {'Opbouwwastafelkranen', 'Inbouwwastafelkranen', 'Opbouwfonteinkranen',
        'Inbouwfonteinkranen', 'Opbouwbadkranen', 'Inbouwbadkranen',
        'Vrijstaande badkranen', 'Opbouwdouchekranen', 'Inbouwdouchesets',
        'Losse inbouwthermostaten', 'Douchepanelen'}
RULES = (
    ('headshower_size', 'Maat hoofddouche', 'Diameter hoofddouche', HEAD_PRODUCTS),
    ('on_off_control', 'Bediening voor aan/uit', 'Bediening aan/uit', TAPS),
    ('door_mechanism', 'Type deur', 'Deursysteem', {'Nisdeuren', 'Douchecabines'}),
)


def project(product):
    """Return new groups and a removal ledger; exact label/value/scope only."""
    groups = deepcopy(product['customer_specifications'])
    if product.get('vendor') != 'BRAUER':
        return groups, []
    items = [i for g in groups for i in g['items']]
    by_label = {i['label']: i for i in items}
    if len(by_label) != len(items):
        raise ValueError('Duplicate input labels require review')
    held = set(product.get('retail_review', {}).get('open_fields', []))
    held.update(product.get('measurement_hold', {}).get('fields', []))
    held.update(product.get('source_conflicts', {}))
    removed = []
    for rule, alias, canonical, types in RULES:
        if product.get('product_type') not in types or {alias, canonical} & held:
            continue
        left, right = by_label.get(alias), by_label.get(canonical)
        if (left is None or right is None or not isinstance(left['value'], str)
                or not left['value'].strip() or left['value'] != right['value']):
            continue
        removed.append({'rule': rule, 'removed': deepcopy(left), 'retained': deepcopy(right)})
    suppressed = {r['removed']['label'] for r in removed}
    for group in groups:
        group['items'] = [i for i in group['items'] if i['label'] not in suppressed]
    return [g for g in groups if g['items']], removed
