"""Prefer explicit compound door mechanisms in the exact original supplier row.

Only refines a prior generic supplier parse. No external identity or dimensions
are inferred, and prior values and evidence are retained in an audit file.
"""
import argparse
import copy
import json
from pathlib import Path

GROUPS = {'Douchecabine met draai-schuifdeur met profiel',
          'Nisdeur 2-delig met draai-schuifdeur met profiel',
          'Nisdeur met draai-schuifdeur met profiel'}


def refine(product, evidence):
    source = product.get('source', {})
    if source.get('Productgroep') not in GROUPS:
        return None
    if (product.get('vendor') != 'BRAUER' or source.get('Merk') != 'BRAUER'
            or source.get('Artikelcode') != product['sku'] or source.get('EAN') != product['ean']
            or evidence.get('ean') != product['ean']):
        raise ValueError('Exact original supplier brand/SKU/EAN required')
    before = product['specifications'].get('Deursysteem')
    if before == 'Draai-schuifdeur':
        return None
    old_proof = evidence['facts'].get('Deursysteem', {})
    if (before != 'Draaideur' or old_proof.get('kind') != 'supplier'
            or old_proof.get('field') != 'Productomschrijving' or old_proof.get('fragment') != 'draaiend'
            or 'Deursysteem' in product.get('retail_review', {}).get('open_fields', [])
            or not product.get('source_refs')):
        raise ValueError('Unexpected door value or hold; retain it for review')
    proof = {'kind':'supplier','field':'Productgroep','fragment':'draai-schuifdeur',
             'source_refs':copy.deepcopy(product['source_refs']),'url':None,
             'supplier_refinement_rule':'explicit_compound_door_mechanism'}
    audit = {'sku':product['sku'],'ean':product['ean'],'field':'Deursysteem',
             'before':before,'after':'Draai-schuifdeur','previous_evidence':copy.deepcopy(old_proof),
             'new_evidence':copy.deepcopy(proof),
             'reason':'Original supplier Productgroep explicitly states the compound mechanism; the previous description parse only matched draaiend.'}
    product['specifications']['Deursysteem'] = 'Draai-schuifdeur'
    matched = 0
    for group in product['customer_specifications']:
        for item in group['items']:
            if item['label'] == 'Deursysteem':
                assert item['value'] == before
                item['value'] = 'Draai-schuifdeur'; matched += 1
    assert matched == 1
    evidence['facts']['Deursysteem'] = proof
    return audit


def build(root):
    prepared = root/'prepared'
    catalog = json.loads((prepared/'catalog.json').read_text())
    evidence = json.loads((prepared/'specification-evidence.json').read_text())
    history_path = prepared/'supplier-door-refinements.json'
    history = json.loads(history_path.read_text()) if history_path.exists() else {'rule':'explicit_compound_door_mechanism','changes':[]}
    known = {x['sku'] for x in history['changes']}
    changed = []
    for p in catalog:
        change = refine(p, evidence[p['sku']])
        if change:
            if p['sku'] in known:
                raise ValueError('Duplicate historic correction; do not erase history')
            history['changes'].append(change); changed.append(change)
    if changed:
        rows = json.loads((prepared/'specification-sheet-data.json').read_text())
        by = {p['sku']:p for p in catalog}
        touched = {x['sku'] for x in changed}
        for row in rows['rows']:
            if row[0] in touched:
                p = by[row[0]]
                row[10] = '\n'.join(f"{i['label']}: {i['value']}" for g in p['customer_specifications'] for i in g['items'] if i['label'] not in {'Merk','Artikelnummer','EAN'})
        for name, value in [('catalog.json',catalog),('specification-evidence.json',evidence),
                            ('specification-sheet-data.json',rows),('supplier-door-refinements.json',history)]:
            (prepared/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    return {'status':'PASS','refined_this_run':len(changed),'historic_refinements':len(history['changes']),
            'fields_added':0,'fields_removed':0,'new_external_product_facts':0,'import_allowed':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path('.'))
    print(json.dumps(build(parser.parse_args().root)))
