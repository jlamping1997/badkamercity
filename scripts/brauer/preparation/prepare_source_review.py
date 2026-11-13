"""Resolve only supported mounting-word differences while retaining their history."""
import argparse
import copy
import json
from pathlib import Path

from enrich_retail_specifications import normalized


def resolution(product,evidence,difference):
    if difference.get('status')!='OPEN' or difference.get('field')!='Montage':return None
    allowed={'Topbladen':'Vrijhangend aan de wand','Inbouwdouchesets':'Inbouw','Vrijstaande badkranen':'Vrijstaand'}
    typ=product['product_type'];base=product['specifications'].get('Montage')
    source=product['source'];proof=evidence['facts'].get('Montage',{})
    if (typ not in allowed or base!=allowed[typ] or product.get('vendor')!='BRAUER'
        or source.get('Merk')!='BRAUER' or source.get('Artikelcode')!=product['sku']
        or source.get('EAN')!=product['ean'] or evidence.get('ean')!=product['ean']
        or proof.get('kind')!='supplier' or proof.get('source_refs')!=product['source_refs']
        or not proof.get('fragment') or proof['fragment'].lower() not in source.get(proof.get('field'),'').lower()
        or 'Montage' in product.get('source_conflicts',{})
        or 'Montage' in product.get('measurement_hold',{}).get('fields',[])):
        return None
    norm=lambda value:normalized('Montage',value,product_type=typ)
    matching=[v for v in difference['candidates'] if v.get('identity')=='SKU_EAN_MERK'
              and v.get('ean')==product['ean'] and norm(v['value'])==norm(base)]
    if not matching:return None
    return {'value':base,'basis':'SUPPLIER_AND_EXACT_RETAILER',
            'supplier_source_refs':copy.deepcopy(proof['source_refs']),
            'corroborating_url':matching[0]['url'],
            'reason':'Literal exact supplier mounting retained; exact BRAUER/SKU/EAN retailer table corroborates it. Top-board ophangen is a broader wording of the existing suspended mounting, not a new location fact.',
            'scope':'This exact article and mounting field only; no dimensions or sibling inheritance.'}


def build(root):
    p=root/'prepared'
    catalogue={x['sku']:x for x in json.loads((p/'catalog.json').read_text())}
    proof=json.loads((p/'specification-evidence.json').read_text())
    report=json.loads((p/'retail-enrichment-report.json').read_text())
    resolutions=json.loads((p/'retail-resolutions.json').read_text())
    history_path=p/'source-review-history30.json'
    history=json.loads(history_path.read_text()) if history_path.exists() else {'task':'BRAUER-30','changes':[]}
    known={(x['sku'],x['field']) for x in history['changes']}
    added=0
    for item in report['differences']:
        result=resolution(catalogue[item['sku']],proof[item['sku']],item)
        if result is None:continue
        slot=resolutions.setdefault(item['sku'],{})
        if item['field'] in slot:
            if slot[item['field']]!=result:raise ValueError('Do not replace a previous resolution')
            continue
        slot[item['field']]=result
        key=(item['sku'],item['field'])
        if key not in known:
            history['changes'].append({'sku':item['sku'],'ean':catalogue[item['sku']]['ean'],
                                      'field':item['field'],'previous_difference':copy.deepcopy(item),
                                      'resolution':copy.deepcopy(result)})
            known.add(key)
        added+=1
    for name,data in [('retail-resolutions.json',resolutions),('source-review-history30.json',history)]:
        (p/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return {'new_supported_mounting_resolutions':added,'history_rows':len(history['changes']),
            'customer_values_changed':0,'import_allowed':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('root',nargs='?',type=Path,default=Path('.'))
    print(json.dumps(build(parser.parse_args().root)))
