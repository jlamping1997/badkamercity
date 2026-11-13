#!/usr/bin/env python3
"""Exact remaining Gent members plus independently reviewed Rails groups."""
import argparse
import json
import re
from pathlib import Path

from build_config_groups import eligible

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'hotbath-menu-20261024'
GENT={'GT003': {'GT003IX':'Laag','GT003MIX':'Medium','GT003HIX':'Hoog'},'GT023':{'GT023IX':'Laag','GT023HIX':'Hoog'}}
HELD={'IBS20AGN357','IBS20BBP','IBS20BCP','IBS33BGP4'}


def gent_groups(remaining,book):
    rules={r['id']:r for r in book['families'] if r['id'] in GENT}
    groups,review,records=[],[],[]
    for family,members in GENT.items():
        rule=rules[family]
        if set(members)!={member+'IX' for member in rule['members']}:
            raise ValueError('Gent exact member rule changed')
        rows=[]
        for p in remaining['products']:
            variants=p.get('variants',{}).get('nodes',[])
            sku=(variants[0].get('sku') or '') if variants else ''
            if sku not in members:continue
            okay,reason=eligible(p)
            if not okay or sku in HELD:
                review.append({'sku':sku,'reason':reason or 'GLOBAL_HOLD'});continue
            if p.get('group'):
                review.append({'sku':sku,'reason':'EXISTING_GROUP_NOT_OVERRIDDEN'});continue
            height=members[sku]
            title=p['title'].casefold()
            explicit=re.findall(r'\b(laag|middel|medium|hoog)\b',title)
            explicit=['Medium' if v in {'middel','medium'} else v.title() for v in explicit]
            expected_gaps='2 gats' if family=='GT023' else None
            if (explicit and set(explicit)!={height}) or (expected_gaps and expected_gaps not in title):
                review.append({'sku':sku,'reason':'GENT_TITLE_CONTRADICTS_EXACT_BOOK_MEMBER'});continue
            if any(term in title for term in ['inbouwdeel','afbouwdeel','3 gats']):
                review.append({'sku':sku,'reason':'GENT_PRODUCT_FUNCTION_CONFLICT'});continue
            fixed=re.sub(r'(?<!\w)'+re.escape(sku.casefold())+r'(?!\w)',' ',title)
            fixed=re.sub(r'\b(?:laag|middel|medium|hoog)\b',' ',fixed)
            fixed=re.sub(r'\s+',' ',re.sub(r'[-–—,]',' ',fixed)).strip()
            expected_fixed='hotbath wastafelmengkraan' if family=='GT003' else 'hotbath wastafelmengkraan 2 gats met draaibare uitloop'
            if fixed!=expected_fixed:
                review.append({'sku':sku,'reason':'GENT_UNMODELED_FIXED_TITLE_DIFFERENCE','fixed_title':fixed});continue
            rows.append({'p':p,'sku':sku,'options':{'kleur':'RVS 316','hoogte':height}})
        tuples=[tuple(row['options'].values()) for row in rows]
        if len(rows)<2 or len(tuples)!=len(set(tuples)):
            review.append({'family':family,'reason':'DUPLICATE_OR_TOO_FEW_MEMBERS'});continue
        rows.sort(key=lambda row:['Laag','Medium','Hoog'].index(row['options']['hoogte']))
        gid=f'hotbath-gent-{family.lower()}-wastafelmengkraan'
        groups.append({'id':gid,'label':f'Hotbath Gent {family} wastafelmengkraan','menus':[
            {'key':'kleur','label':'Kleur','order':1,'display_type':'dropdown','hide_if_single_value':True,'values':['RVS 316']},
            {'key':'hoogte','label':'Hoogte','order':2,'display_type':'buttons','hide_if_single_value':True,'values':[v for v in ['Laag','Medium','Hoog'] if any(r['options']['hoogte']==v for r in rows)]},
        ],'products':[{'handle':r['p']['handle'],'url':'/products/'+r['p']['handle'],'title':r['p']['title'],'sort_order':i,'options':r['options']} for i,r in enumerate(rows)]})
        records.extend({'sku':r['sku'],'handle':r['p']['handle'],'id':r['p']['id'],'group_id':gid,'sources':rule['sources'],'evidence':'EXACT_BOOK_MEMBER_HEIGHT; IX_FINISH_ONLY'} for r in rows)
    return groups,review,records


def combine(remaining,book,rails=None):
    groups,review,records=gent_groups(remaining,book)
    if rails:groups.extend(rails['groups'])
    allowed={p['handle']:p for p in remaining['products']}
    handles=[]
    for group in groups:
        keys=[m['key'] for m in group['menus']]
        choices=[]
        for row in group['products']:
            p=allowed[row['handle']]
            sku=p['variants']['nodes'][0]['sku']
            okay,reason=eligible(p)
            if not okay or sku in HELD:raise ValueError('Ineligible supplemental row: '+sku+' '+str(reason))
            if p.get('group'):raise ValueError('Existing membership: '+sku)
            handles.append(row['handle']);choices.append(tuple(row['options'][key] for key in keys))
        if len(choices)!=len(set(choices)):raise ValueError('Duplicate choices in '+group['id'])
    if len(handles)!=len(set(handles)):raise ValueError('Supplemental handle overlap')
    return {'version':'hotbath-supplemental-20261024','groups':groups},{'schema':'hotbath-supplemental-review-v1','gent_records':records,'gent_review':review,'rails_included':bool(rails),'group_count':len(groups),'product_count':len(handles),'limits':['Exact book-confirmed Gent member heights only.','Rails export is independent; horizontal/vertical shapes and integrated/separate controls remain separate.','IBS33 has no confirmed family suffix grammar in source; no configuration group generated.']}


def main():
    p=argparse.ArgumentParser();p.add_argument('--dir',type=Path,default=HERE);args=p.parse_args()
    remaining=json.loads((args.dir/'coverage_remaining.json').read_text());book=json.loads((BASE/'book_rules.json').read_text())
    rails_path=args.dir/'rails_supplemental.json';rails=json.loads(rails_path.read_text()) if rails_path.exists() else None
    groups,review=combine(remaining,book,rails)
    for name,data in [('supplemental_groups.json',groups),('supplemental_review.json',review)]:
        (args.dir/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'groups':review['group_count'],'products':review['product_count'],'rails_included':review['rails_included']}))


if __name__=='__main__':main()
