"""Derive short customer benefits from approved facts of the same exact article.

No research, variant inheritance, installation-wide promises or Shopify writes.
"""
import argparse
from collections import Counter
import copy
import json
from pathlib import Path
from urllib.parse import urlparse

VERSION = 'brauer-benefits-3-curated'
MAX_BENEFITS = 3
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
FURNITURE = {'Onderkasten', 'Fonteinkasten', 'Halfhoge kasten', 'Hoge kasten', 'Bijkasten', 'Spiegelkasten'}
FURNITURE_MATERIALS = {
    'MDF gelakt': 'Gelakt MDF',
    'Massief eiken doorlopende lamellen': 'Massief eiken',
    'Massief eiken vingerlas': 'Massief eiken',
    'Massief eiken doorlopende vingerlas': 'Massief eiken',
}
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
        bundle_has_body = add('complete_shower_set', 'Complete doucheset',
                             core + [('Doucheslang inbegrepen', yes), ('Inbouwdeel inbegrepen', yes)])
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
        if typ != 'Losse inbouwthermostaten':
            add('thermostatic', 'Thermostaatkraan', [('Thermostatisch', yes)])
    if typ in TAPS or typ == 'Handdouches en houders':
        modes = specifications.get('Aantal straalstanden handdouche')
        if modes in {'2', '3', '4', '5', '6'}:
            add('handshower_modes', f'Handdouche met {modes} standen',
                [('Handdouche inbegrepen', yes), ('Aantal straalstanden handdouche', {modes})]
                if typ == 'Inbouwdouchesets' else [('Aantal straalstanden handdouche', {modes})])
    if typ in TAPS:
        if approved_definition(definitions, 'cold_start'):
            add('cold_start', 'Koud water in de middenstand', [('Koudestartfunctie', yes)], 'cold_start')
        else:
            add('cold_start', 'Met koudestartfunctie', [('Koudestartfunctie', yes)])
    if typ in GLASS:
        if approved_definition(definitions, 'hydrophobic_glass'):
            add('glass_coating', 'Water- en vuilafstotende coating', [('Glascoating', yes)], 'hydrophobic_glass')
        else:
            add('glass_coating', 'Met glascoating', [('Glascoating', yes)])
        add('reversible_glass', 'Links of rechts te monteren',
            [('Montage', {'Links/rechts', 'Links of rechts te monteren'})])
    if typ in FURNITURE:
        material = specifications.get('Materiaal')
        if material in FURNITURE_MATERIALS:
            add('furniture_material', FURNITURE_MATERIALS[material], [('Materiaal', {material})])
        if typ == 'Onderkasten' and fact('Aantal lades', {'1', '2', '3', '4'}):
            add('soft_close', 'Softclose lades', [('Softclose', yes), ('Aantal lades', {'1', '2', '3', '4'})])
        elif typ == 'Spiegelkasten' and fact('Aantal deuren', {'1', '2', '3', '4'}):
            add('soft_close', 'Softclose deuren', [('Softclose', yes), ('Aantal deuren', {'1', '2', '3', '4'})])
        else:
            add('soft_close', 'Zachte sluiting', [('Softclose', yes)])
    if typ in GLASS:
        profile_holds = {'Type profiel/bevestiging', 'Bevestiging glas', 'Productgroep'}
        if (not blocked.intersection(profile_holds)
                and specifications.get('Type profiel/bevestiging') != 'Met profiel'
                and specifications.get('Bevestiging glas') != 'Muurprofiel'):
            add('frameless_glass', 'Profielloos', [], 'frameless_glass',
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
    if typ in LIGHTS and specifications.get('Verlichting') != 'Nee':
        lighting = add('adjustable_dimmable_light', 'Dimbare verlichting met kleurkeuze',
                       [('Dimbaar', yes), ('Lichtkleur instelbaar', yes)])
        if not lighting:
            lighting = add('dimmable_light', 'Dimbare verlichting', [('Dimbaar', yes)])
            lighting = add('adjustable_light_colour', 'Instelbare lichtkleur', [('Lichtkleur instelbaar', yes)]) or lighting
        if typ == 'Spiegelkasten' and not lighting:
            add('included_cabinet_light', 'Verlichting inbegrepen',
                [('Verlichting', {'Ja', 'Directe verlichting', 'Binnen- en buitenverlichting',
                                  'Directe verlichting (LED)', 'Indirecte LED-verlichting'})])
    if typ == 'Douchebakken':
        add('anti_slip', 'Antislip douchebak', [('Antislip', yes)], 'anti_slip')
    if typ == 'Opbouwnissen':
        add('hidden_storage', 'Verborgen opbergruimte', [('Verborgen opbergruimte', yes)])
    # A small fixed order expresses the buying decision; never fill empty slots.
    if typ == 'Inbouwdouchesets':
        order = ['complete_shower_set', 'thermostatic', 'pvd_finish', 'handshower_modes',
                 'included_body', 'cold_start', 'rotating_outlet']
    elif typ in FURNITURE:
        order = ['furniture_material', 'soft_close', 'adjustable_dimmable_light',
                 'dimmable_light', 'adjustable_light_colour', 'included_cabinet_light']
    elif typ in GLASS:
        order = ['frameless_glass', 'sliding_door', 'pivot_sliding_door', 'glass_coating', 'reversible_glass']
    else:
        order = ['included_body', 'rotating_outlet', 'cold_start', 'thermostatic', 'pvd_finish',
                 'handshower_modes', 'adjustable_dimmable_light', 'dimmable_light',
                 'adjustable_light_colour', 'anti_slip', 'hidden_storage']
    rank = {rule: i for i, rule in enumerate(order)}
    items.sort(key=lambda item: rank.get(item['rule'], len(order)))
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
               'complete_set_claims': counts['complete_shower_set'],
               'complete_set_policy': 'Complete doucheset only when head shower, hand shower, hose and inbuilt body are positively proved for that exact inbuilt set. No promise that every installation accessory is included.',
               'display_policy': 'At most three short distinct buying reasons; fewer or none allowed. One set-content point, combined lighting functions; generic LED, thickness and MFC remain specifications.',
               'shopify_writes': 0, 'import_allowed': False}
    for path, obj in [('product-benefits.json', records),
                      ('product-benefits-summary.json', summary)]:
        (prepared / path).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    print(json.dumps(build(parser.parse_args().root), ensure_ascii=False))
