"""Derive short customer benefits from approved facts of the same exact article.

No research, variant inheritance, complete-set promise or Shopify writes.
"""
import argparse
from collections import Counter
import copy
import json
from pathlib import Path
from urllib.parse import urlparse

VERSION = 'brauer-benefits-2'
MAX_BENEFITS = 4
TAPS = {
    'Inbouwdouchesets', 'Inbouwbadkranen', 'Opbouwbadkranen',
    'Opbouwdouchekranen', 'Inbouwwastafelkranen', 'Opbouwwastafelkranen',
    'Inbouwfonteinkranen', 'Opbouwfonteinkranen', 'Vrijstaande badkranen',
    'Losse inbouwthermostaten', 'Douchepanelen', 'Uitlopen',
}
GLASS = {'Douchecabines', 'Nisdeuren', 'Inloopdouches', 'Badwanden', 'Losse glasdelen', 'Setgebonden glasdelen'}
KINDS = {'supplier', 'previous_exact_sku_audit', 'retailer_exact_sku_ean'}
FRAMELESS_GROUPS = {
    'Badwand profielloos', 'Douchecabine met draaideur profielloos',
    'Nisdeur met draaideur profielloos', 'Nisdeur 2-delig met draaideur profielloos',
    'Pendeldeuren profielloos', 'Inloopdouche profielloos',
    'Inloopdouche met zijwand profielloos',
}
SLIDING_GROUPS = {'Douchecabine met schuifdeur met profiel', 'Nisdeur 2-delig met schuifdeur met profiel'}
PIVOT_SLIDING_GROUPS = {'Douchecabine met draai-schuifdeur met profiel',
                       'Nisdeur 2-delig met draai-schuifdeur met profiel',
                       'Nisdeur met draai-schuifdeur met profiel'}
LIGHTS = {'Spiegels', 'Spiegelkasten', 'Lichtlijsten voor spiegelkasten', 'Opbouwverlichting'}
REQUIRED_DEFINITIONS = {'hydrophobic_glass', 'cold_start', 'pvd_finish', 'frameless_glass',
                        'sliding_door', 'pivot_sliding_door', 'glass_thickness', 'anti_slip'}


def approved_definition(definitions, key):
    d = (definitions or {}).get(key, {})
    hosts = {'www.brauerkranen.nl', 'brauerkranen.nl', 'www.brauerbadkamers.nl',
             'brauerbadkamers.nl', 'topa-import.com', 'www.topa-import.com'}
    urls = d.get('sources', [])
    if (d.get('brand') != 'BRAUER' or d.get('status') != 'VERIFIED_DEFINITION'
            or not urls or any(urlparse(u).scheme != 'https' or urlparse(u).hostname not in hosts for u in urls)):
        return None
    return d


def derive(product, evidence, definitions=None, limit=MAX_BENEFITS):
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

    def source_fact(field, accepted):
        source = product.get('source', {})
        if (source.get('Merk') != 'BRAUER' or source.get('Artikelcode') != product['sku']
                or source.get('EAN') != product['ean'] or field in blocked
                or source.get(field) not in accepted or not product.get('source_refs')):
            return None
        return {'field': field, 'value': source[field], 'source': 'supplier_record',
                'evidence': {'kind': 'supplier', 'field': field, 'fragment': source[field],
                             'source_refs': copy.deepcopy(product['source_refs']), 'url': None}}

    def add(rule, text, required, definition_id=None, supplier_fields=None):
        proofs = [fact(field, accepted) for field, accepted in required]
        proofs.extend(source_fact(field, accepted) for field, accepted in (supplier_fields or []))
        if not all(proofs):
            return False
        if definition_id and not approved_definition(definitions, definition_id):
            return False
        item = {'rule': rule, 'text': text, 'basis': proofs}
        if definition_id:
            item['definition_refs'] = [definition_id]
        items.append(item)
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
        if approved_definition(definitions, 'cold_start'):
            add('cold_start', 'Coldstart: koud water in de middenstand', [('Koudestartfunctie', yes)], 'cold_start')
        else:
            add('cold_start', 'Met koudestartfunctie', [('Koudestartfunctie', yes)])
    if typ in GLASS:
        if approved_definition(definitions, 'hydrophobic_glass'):
            add('glass_coating', 'Met water- en vuilafstotende glascoating', [('Glascoating', yes)], 'hydrophobic_glass')
        else:
            add('glass_coating', 'Met glascoating', [('Glascoating', yes)])
        add('reversible_glass', 'Links of rechts te monteren',
            [('Montage', {'Links/rechts', 'Links of rechts te monteren'})])
    if typ in {'Onderkasten', 'Spiegelkasten'}:
        add('soft_close', 'Softclose sluiting', [('Softclose', yes)])
    # The original benefits retain their position; new features follow them.
    if typ in GLASS:
        profile_holds = {'Type profiel/bevestiging', 'Bevestiging glas', 'Productgroep'}
        if (not blocked.intersection(profile_holds)
                and specifications.get('Type profiel/bevestiging') != 'Met profiel'
                and specifications.get('Bevestiging glas') != 'Muurprofiel'):
            add('frameless_glass', 'Profielloze uitvoering', [], 'frameless_glass',
                [('Productgroep', FRAMELESS_GROUPS)])
        door_holds = {'Productgroep', 'Deursysteem', 'Type deur', 'Draairichting deur'}
        if typ in {'Nisdeuren', 'Douchecabines'} and not blocked.intersection(door_holds):
            mode = specifications.get('Deursysteem')
            if mode in (None, '', 'Schuifdeur', '1 schuifdeur'):
                add('sliding_door', 'Schuifdeur zonder draaicirkel', [], 'sliding_door',
                    [('Productgroep', SLIDING_GROUPS)])
            if mode in (None, '', 'Draai-schuifdeur'):
                add('pivot_sliding_door', 'Draai-schuifdeur', [], 'pivot_sliding_door',
                    [('Productgroep', PIVOT_SLIDING_GROUPS)])
    add('pvd_finish', 'PVD-afwerking', [('Coating', {'PVD'})], 'pvd_finish')
    if typ in GLASS:
        add('glass_thickness', 'Glas van 8 mm dik', [('Glasdikte', {'8 mm'})], 'glass_thickness')
    if typ in LIGHTS and specifications.get('Verlichting') != 'Nee':
        add('dimmable_light', 'Dimbare verlichting', [('Dimbaar', yes)])
        add('adjustable_light_colour', 'Instelbare lichtkleur', [('Lichtkleur instelbaar', yes)])
        add('led_light', 'LED-verlichting', [('Verlichting', {'Directe verlichting (LED)', 'Indirecte LED-verlichting'})])
    if typ == 'Douchebakken':
        add('anti_slip', 'Antislip douchebak', [('Antislip', yes)], 'anti_slip')
    if typ == 'Opbouwnissen':
        add('hidden_storage', 'Verborgen opbergruimte', [('Verborgen opbergruimte', yes)])
    return items[:limit] if limit is not None else items


def build(root):
    prepared = root / 'prepared'
    # Missing research configuration must not silently erase a previous run.
    registry = json.loads((prepared / 'manufacturer-features.json').read_text())
    definitions = registry['definitions']
    if not all(approved_definition(definitions, key) for key in REQUIRED_DEFINITIONS):
        raise ValueError('Missing or unverified manufacturer feature definition; no outputs written')
    catalog = json.loads((prepared / 'catalog.json').read_text())
    evidence = json.loads((prepared / 'specification-evidence.json').read_text())
    records = []
    counts = Counter()
    eligible_counts = Counter()
    for product in catalog:
        eligible = derive(product, evidence.get(product['sku'], {}), definitions, limit=None)
        items = eligible[:MAX_BENEFITS]
        eligible_counts.update(item['rule'] for item in eligible)
        counts.update(item['rule'] for item in items)
        records.append({'sku': product['sku'], 'ean': product['ean'],
                        'product_type': product['product_type'], 'items': items})
    summary = {'version': VERSION, 'articles': len(catalog),
               'articles_with_benefits': sum(bool(r['items']) for r in records),
               'benefits': sum(len(r['items']) for r in records),
               'maximum_per_article': MAX_BENEFITS, 'by_rule': dict(sorted(counts.items())),
               'eligible_before_display_limit': sum(eligible_counts.values()),
               'eligible_by_rule': dict(sorted(eligible_counts.items())),
               'manufacturer_definition_count': len(definitions),
               'new_external_facts': 0, 'benefit_generator_specification_writes': 0,
               'complete_set_claims': 0, 'shopify_writes': 0, 'import_allowed': False}
    for path, obj in [('product-benefits.json', records),
                      ('product-benefits-summary.json', summary)]:
        (prepared / path).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    print(json.dumps(build(parser.parse_args().root), ensure_ascii=False))
