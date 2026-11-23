"""Prepare private format decisions for the parent's published-ID-filtered input."""

from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

from nominal_formats import (TileContext, classify_pair, pair, format_key,
                             format_label, SHAPE_REVIEW_HINT, MOSAIC_SHEET_HINT)


NONRECTANGULAR = SHAPE_REVIEW_HINT
MOSAIC_SHEET = MOSAIC_SHEET_HINT


def field(row, key):
    value=row.get(key)
    return value.get('value') if isinstance(value,dict) else value


def prepare(document, *, expected_count=3496):
    rows=document.get('rows')
    if not isinstance(rows,list) or len(rows)!=expected_count:
        raise ValueError('Input must contain exactly the expected published-ID-filtered rows')
    ids=[r.get('id') for r in rows]
    if any(not x for x in ids) or len(set(ids))!=len(ids):
        raise ValueError('Missing or duplicate product IDs')
    if document.get('public_index_count')!=expected_count:
        raise ValueError('Published-index scope count is missing or mismatched')
    decisions=[]
    for row in rows:
        title=row.get('title') or ''
        product_type=row.get('productType') or ''
        text=' '.join((title,product_type))
        if MOSAIC_SHEET.search(text):
            shape,basis='unknown','sheet_or_mosaic'
        elif NONRECTANGULAR.search(text):
            shape,basis='shape_review_by_name','piece'
        else:
            # A working assumption for generating review candidates only.
            # Neither value is asserted as a fact about the source catalogue.
            shape,basis='rectangular','piece'
        ctx=TileContext(shape=shape,measure_basis=basis,vendor=row.get('vendor') or '',
                        series=field(row,'series') or '',title=title,product_type=product_type)
        decision=classify_pair(field(row,'width'),field(row,'length'),context=ctx).to_dict()
        engine_eligible=decision['eligible_for_plan']
        decision['engine_status']=decision['status']
        if decision['status']=='BLOCKED_UNKNOWN' and decision['raw_pair_mm']:
            # A valid existing unusual format is not missing data. Preserve it
            # as an exact display term rather than dropping the product or
            # inventing a more familiar nominal format.
            exact=pair(*decision['raw_pair_mm'])
            decision.update(nominal_pair_mm=decision['raw_pair_mm'],format_key=format_key(exact),
                            label=format_label(exact),status='EXACT_RETAINED',delta_mm=['0','0'],
                            reason='No reviewed nominal target; existing exact size retained unchanged for the offline format list')
        decision.update({
            'eligible_for_plan':False,
            'context_verified':False,
            'production_eligible':False,
            'engine_eligible_under_assumed_context':engine_eligible,
            'context_assumption':{'shape':shape,'measure_basis':basis,
                                  'note':'Shape and piece/sheet basis are not fields in the source snapshot. Candidate exploration only.'},
            'id':row['id'],'handle':row.get('handle'),'title':title,'vendor':row.get('vendor'),
            'series':field(row,'series'),'declared_size_cm':field(row,'size'),
            'source_width_mm':field(row,'width'),'source_length_mm':field(row,'length'),
        })
        decisions.append(decision)
    statuses=Counter(d['status'] for d in decisions)
    formats=Counter(d['format_key'] for d in decisions if d['format_key'])
    raw_pairs={tuple(d['raw_pair_mm']) for d in decisions if d['raw_pair_mm']}
    covered_pairs={tuple(d['raw_pair_mm']) for d in decisions if d['format_key']}
    changed=[d for d in decisions if d['nominal_pair_mm'] and d['raw_pair_mm']!=d['nominal_pair_mm']]
    grouped=defaultdict(list)
    for d in decisions:
        k=(tuple(d['raw_pair_mm']) if d['raw_pair_mm'] else None,d['format_key'],d['status'],d['reason'])
        grouped[k].append(d)
    pairs=[]
    for (raw,key,status,reason),items in grouped.items():
        first=items[0]
        pairs.append({'raw_pair_mm':raw,'nominal_pair_mm':first['nominal_pair_mm'],
                      'format_key':key,'label':first['label'],'status':status,'reason':reason,
                      'count':len(items),'context_verified':False,'production_eligible':False,
                      'examples':[{'id':d['id'],'title':d['title'],'handle':d['handle']} for d in items[:3]],
                      'source_declared_sizes_cm':sorted({str(d['declared_size_cm']) for d in items if d['declared_size_cm']})})
    pairs.sort(key=lambda x:(-x['count'],str(x['raw_pair_mm']),str(x['format_key'])))
    summary={'scope':'OFFLINE_CANDIDATE_PREPARATION_NOT_APPLIED',
             'public_index_count':document['public_index_count'],'input_rows':len(rows),
             'admin_collection_count':document.get('admin_collection_count'),
             'excluded_admin_rows':document.get('excluded_admin_rows'),
             'generation':document.get('generation'),'source_scope_note':document.get('scope_note') or document.get('eligibility') or document.get('source'),
             'unique_valid_source_pairs':len(raw_pairs),'candidate_nominal_format_count':len(formats),
             'candidate_label_scope_products':sum(d['format_key'] is not None for d in decisions),
             'candidate_label_scope_source_pairs':len(covered_pairs),
             'same_scope_distinct_pair_reduction':len(covered_pairs)-len(formats),
             'decision_status_counts':dict(statuses),'changed_candidate_products':len(changed),
             'changed_candidate_source_pairs':len({tuple(d['raw_pair_mm']) for d in changed}),
             'unresolved_products':sum(d['format_key'] is None for d in decisions),
             'context_verified_products':0,'production_eligible_products':0,
             'usage_restriction':'FILTER_LABEL_AND_SEARCH_GROUP_ONLY; never use these nominal dimensions for area, box quantities, price or order calculations',
             'candidate_format_counts':dict(sorted(formats.items(),key=lambda x:(-x[1],x[0]))),
             'policy':'max8mm AND3percent per side, curated pair targets; changed596to600 ownerexample, other changes proposed',
             'context_note':'All shape/basis context is assumed or excluded by text hints; no row has product-level shape/basis verification.'}
    return {'summary':summary,'pair_decisions':pairs,'rows':decisions}


def output_paths(input_path, requested_output=None):
    """Keep private output beside its input and reject source-path collisions."""
    source=Path(input_path).resolve()
    output=(Path(requested_output) if requested_output is not None else source.with_name('format-decision-table.json')).resolve()
    stats=output.with_name('format-summary.json')
    if source in {output,stats}:
        raise ValueError('Output or summary path would overwrite the source snapshot')
    return output,stats


def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--expected-count',type=int,default=3496)
    args=ap.parse_args()
    output,stats=output_paths(args.input,args.output)
    before=args.input.read_bytes()
    result=prepare(json.loads(before),expected_count=args.expected_count)
    result['summary']['input_sha256']=hashlib.sha256(before).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2))
    assert args.input.read_bytes()==before,'Source snapshot unexpectedly changed'
    stats.write_text(json.dumps(result['summary'],ensure_ascii=False,indent=2))
    print(json.dumps(result['summary'],ensure_ascii=False))


if __name__=='__main__':main()
