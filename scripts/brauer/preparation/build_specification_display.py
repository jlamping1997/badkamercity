"""Audit the display-only projection; no catalogue, evidence or store writes."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from specification_display import POLICY, RULES, project


def build(root):
    prepared = root / 'prepared'
    catalog = json.loads((prepared/'catalog.json').read_text())
    evidence = json.loads((prepared/'specification-evidence.json').read_text())
    changes, different, ambiguous = [], [], []
    before = after = 0
    by_rule = Counter()
    for p in catalog:
        original = [i for g in p['customer_specifications'] for i in g['items']]
        if {i['label']: i['value'] for i in original} != p['specifications']:
            raise ValueError('Canonical customer groups differ from source facts')
        groups, removed = project(p)
        visible = [i for g in groups for i in g['items']]
        before += len(original)
        after += len(visible)
        if evidence[p['sku']]['ean'] != p['ean']:
            raise ValueError('Evidence identity differs')
        for entry in removed:
            labels = [entry[k]['label'] for k in ['removed', 'retained']]
            proof = {label: evidence[p['sku']]['facts'][label] for label in labels}
            changes.append({'sku': p['sku'], 'ean': p['ean'], 'type': p['product_type'],
                            **entry, 'source_evidence': proof})
            by_rule[entry['rule']] += 1
        for _, alias, canonical, types in RULES:
            if p['product_type'] in types and all(k in p['specifications'] for k in [alias, canonical]):
                if p['specifications'][alias] != p['specifications'][canonical]:
                    different.append({'sku': p['sku'], 'ean': p['ean'],
                                      'values': {k:p['specifications'][k] for k in [alias, canonical]},
                                      'action':'BOTH_RETAINED_SOURCE_REVIEW_REQUIRED'})
        if p['product_type'] == 'Douchecabines' and all(k in p['specifications'] for k in ['Dikte','Glasdikte']):
            ambiguous.append({'sku':p['sku'],'ean':p['ean'],
                              'values':{k:p['specifications'][k] for k in ['Dikte','Glasdikte']},
                              'action':'RETAINED_GENERIC_THICKNESS_HAS_NO_EXPLICIT_COMPONENT'})
    summary = {
        'policy': POLICY, 'articles':len(catalog), 'canonical_source_facts':before,
        'display_rows':after, 'duplicate_rows_removed':before-after,
        'articles_changed':len({x['sku'] for x in changes}), 'by_rule':dict(by_rule),
        'different_alias_value_pairs_retained':len(different),
        'ambiguous_thickness_pairs_retained':len(ambiguous),
        'catalogue_and_source_evidence_changed':False, 'description_changes':0,
        'shopify_writes':0, 'import_allowed':False,
        'source_sha256':{n:hashlib.sha256((prepared/n).read_bytes()).hexdigest()
                         for n in ['catalog.json','specification-evidence.json']}}
    for name, data in [('specification-display-summary31.json',summary),
                       ('specification-display-history31.json',{'policy':POLICY,'changes':changes}),
                       ('specification-display-review31.json',{'different_alias_values':different,
                                                               'ambiguous_thickness':ambiguous})]:
        (prepared/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return summary


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',nargs='?',type=Path,default=Path('.'))
    print(json.dumps(build(parser.parse_args().root),ensure_ascii=False))
