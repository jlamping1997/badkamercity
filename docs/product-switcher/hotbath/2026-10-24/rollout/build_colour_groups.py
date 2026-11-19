#!/usr/bin/env python3
"""Compile conservative Hotbath colour menus and title-verified configurations.

Read-only inputs. No Shopify, GitHub, prices, stock or product writes.
"""
from __future__ import annotations

import argparse
import collections
import copy
import hashlib
import importlib.util
import json
import re
import unicodedata
from pathlib import Path

SOURCE = Path('/workspace/scratch/6866aa3baeaf/hotbath-menu-20261024')
OUTPUT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('hotbath_catalogue_audit', SOURCE / 'analyze_catalog.py')
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)
EXCLUSIVE_IBS = {'IBS70','IBS7009','IBS20','IBS20A','IBS1','IBS1A','IBS12','IBS12A'}
SOURCE_CONFLICT_HOLDS = {'IBS20AGN357','IBS20BBP','IBS20BCP','SDS32BGP','IBS33BGP4'}
ADDITIVE_COLOUR_GROUPS = {
    'hotbath-archie-ar105ext-inbouw-wastafelmengkraan-rvs316': {'AR105EXT18','AR105EXT25'},
    'hotbath-archie-arhf-inbouwthermostaat-afbouwdeel': {'ARHF011','ARHF012','ARHF013','ARHF014','ARHF015'},
}
COLOUR_ORDER = ['CR','IX','GN','BB','AB','WH','AI','TB','PBP','MBP','BBP','BCP','BGP','BL','BK','NB','BC','RG','BNP','GBP']
CONFIG_FIELDS = [
    ('kleur','Kleur'),
    ('breedte_diameter_hoofddouche','Diameter hoofddouche'),
    ('type_bevestiging_hoofddouche','Bevestiging hoofddouche'),
    ('type_handdouche','Handdouche'),
    ('bevestiging_handdouche','Handdouchehouder'),
]

def load(path):
    return json.loads(path.read_text())

def sku_of(p):
    return audit.sku_of(p)

def exclusion(p):
    values = ' '.join([sku_of(p), p.get('title',''), p.get('handle','')])
    if 'SPOM' in values.upper():
        return 'SPOM_EXCLUDED_BY_USER'
    if sku_of(p).upper().startswith('TEST') or re.search(r'\btest(?:product)?\b|\bpilot\b', values, re.I):
        return 'TEST_EXCLUDED'
    if sku_of(p).upper() in SOURCE_CONFLICT_HOLDS:
        return 'SOURCE_CONFLICT_HELD_FOR_REVIEW'
    if p.get('status') != 'ACTIVE' or not p.get('publishedAt'):
        return 'NOT_ACTIVE_PUBLISHED'
    if p.get('variants',{}).get('pageInfo',{}).get('hasNextPage'):
        return 'MULTI_VARIANT_REVIEW'
    return None

def colour_sort(value):
    names = [audit.PALETTE[x][0] for x in COLOUR_ORDER]
    return (names.index(value) if value in names else 1000, value)

def new_record(p, options, order):
    return {'handle':p['handle'],'url':'/products/'+p['handle'],'title':p['title'],
            'sort_order':order,'options':dict(options)}

def menus_for(records, fields):
    menus = []
    for key, label in fields:
        values = sorted({r['options'][key] for r in records}, key=colour_sort if key=='kleur' else str)
        if len(values) < 2:
            continue
        menus.append({'key':key,'label':label,'order':len(menus)+1,
                      'display_type':'dropdown' if key=='kleur' or len(values)>5 else 'buttons',
                      'hide_if_single_value':True,'values':values})
    return menus

def assert_group(g):
    if not g.get('menus'):
        raise ValueError('No varying choices in '+g['id'])
    keys = [m['key'] for m in sorted(g['menus'],key=lambda m:m.get('order',0))]
    tuples = []
    for p in g['products']:
        if not p.get('handle') or p.get('url') != '/products/'+p['handle']:
            raise ValueError('Invalid product identity in '+g['id'])
        values = tuple(p.get('options',{}).get(k) for k in keys)
        if not all(v is not None and str(v).strip() for v in values):
            raise ValueError('Missing choice in '+g['id'])
        for menu in g['menus']:
            if p['options'][menu['key']] not in menu['values']:
                raise ValueError('Choice missing from values in '+g['id'])
        tuples.append(values)
    if len(tuples) != len(set(tuples)):
        raise ValueError('Duplicate choices in '+g['id'])
    if len({p['handle'] for p in g['products']}) != len(g['products']):
        raise ValueError('Duplicate handles in '+g['id'])

def parse_title_configuration(p, parsed, required=None):
    """Only literal title words become choices; no numeric SKU decoding."""
    s = unicodedata.normalize('NFKC',p['title']).lower().replace('–','-').replace('—','-')
    opts = {'kleur':parsed['colour']}
    spans = []
    def choice(key, pattern, convert=lambda m:m[0]):
        matches = list(re.finditer(pattern,s,re.I))
        values = {convert(m) for m in matches}
        if len(values) == 1:
            opts[key] = values.pop()
            spans.extend(m.span() for m in matches)
        elif len(values) > 1:
            opts[key] = None
    cm = r'(\d+(?:[.,]\d+)?)\s*cm'
    choice('breedte_diameter_hoofddouche', cm+r'\s*(?:ronde?\s*|vierkante?\s*)?hoofddouche', lambda m:m[1].replace(',','.')+' cm')
    if 'breedte_diameter_hoofddouche' not in opts:
        choice('breedte_diameter_hoofddouche', r'hoofddouche\s*(?:van\s*)?'+cm, lambda m:m[1].replace(',','.')+' cm')
    choice('type_bevestiging_hoofddouche', cm+r'\s*plafondbuis', lambda m:'Plafondbuis '+m[1].replace(',','.')+' cm')
    if 'type_bevestiging_hoofddouche' not in opts:
        choice('type_bevestiging_hoofddouche', r'plafondbuis\s*(?:van\s*)?'+cm, lambda m:'Plafondbuis '+m[1].replace(',','.')+' cm')
    if 'type_bevestiging_hoofddouche' not in opts:
        choice('type_bevestiging_hoofddouche',r'wandarm',lambda m:'Wandarm')
    hand = list(re.finditer(r'(staaf|ronde?)(?:\s*(?:3[\s-]*standen|3s))?\s*handdouche(?:\s*(?:met\s*)?(?:3[\s-]*standen|3s))?',s))
    values = set()
    for m in hand:
        label = 'Staafmodel' if m[1]=='staaf' else 'Rond model'
        if re.search(r'3[\s-]*standen|3s',m[0]): label += ' - 3 standen'
        values.add(label);spans.append(m.span())
    if len(values)==1: opts['type_handdouche']=values.pop()
    elif len(values)>1: opts['type_handdouche']=None
    # A literal absence is a holder choice, never a positive glijstang match.
    no_rail = list(re.finditer(r'zonder\s+glijstang',s))
    rail = [m for m in re.finditer(r'(?:met\s+)?glijstang(?:\s+met\s+(?:wand)?uitlaat)?',s)
            if not any(a.start()<=m.start()<a.end() for a in no_rail)]
    holder = list(re.finditer(r'wandhouder|wandsteun(?:\s+met\s+(?:wand)?uitlaat)?',s))
    if rail and (holder or no_rail): opts['bevestiging_handdouche']=None
    elif rail: opts['bevestiging_handdouche']='Glijstang'
    elif holder or no_rail: opts['bevestiging_handdouche']='Wandhouder'
    spans.extend(m.span() for m in no_rail+rail+holder)
    # Strip exactly the captured choices, model/SKU and finish from the residual.
    chars = list(s)
    for a,b in spans:
        chars[a:b] = ' '*(b-a)
    residual=''.join(chars)
    residual=residual.replace(sku_of(p).lower(),' ')
    model=parsed['model']
    model_pattern=re.escape(model)
    model_pattern=re.sub(r'(?<=S)(?=\d)',r'\\s*',model_pattern) if model.startswith('IBS') else model_pattern
    residual=re.sub(model_pattern,' ',residual,flags=re.I)
    for alias in sorted({a for label,aliases in audit.PALETTE.values() for a in aliases},key=len,reverse=True):
        residual=re.sub(r'(?<!\w)'+re.escape(alias)+r'(?!\w)',' ',residual)
    residual=re.sub(r'\b(?:met|zonder|en)\b',' ',residual)
    residual=re.sub(r'[^a-z0-9]+',' ',residual).strip()
    fields = required or [k for k,_ in CONFIG_FIELDS]
    missing=[k for k in fields if not opts.get(k)]
    return opts,residual,missing

def book_options(family, parsed):
    member=family['member_options'][parsed['model']]
    out={'kleur':parsed['colour']}
    fields=[('kleur','Kleur')]
    mapping={
        'height':('hoogte','Hoogte','height',str),
        'spout':('uitloopvorm','Uitloopvorm','spout',str),
        'spout_length':('uitlooplengte','Uitlooplengte','spout_length_cm',lambda v:f'{v} cm'),
        'diameter':('diameter','Diameter','diameter_cm',lambda v:f'{v} cm'),
        'width':('breedte','Breedte','width_cm',lambda v:f'{v} cm'),
        'size':('afmeting','Afmeting','size_cm' if 'size_cm' in member else 'outer_dimensions_cm',lambda v:str(v)+' cm'),
        'cutouts':('uitsparingen','Aantal uitsparingen','cutouts',str),
        'led':('verlichting','Verlichting','led',lambda v:'Met verlichting' if v else 'Zonder verlichting'),
        'frame':('rand','Rand','frame',lambda v:'Met rand' if v else 'Zonder rand'),
    }
    for choice in family['choices']:
        if choice=='color':continue
        if choice=='mount':
            out['bevestiging']=member['mount']+' '+str(member['length_cm']).replace('.',',')+' cm';fields.append(('bevestiging','Bevestiging'));continue
        if choice not in mapping:return None,None
        key,label,source,fmt=mapping[choice]
        if source not in member:return None,None
        out[key]=fmt(member[source]);fields.append((key,label))
    return out,fields

def compile_groups(source=SOURCE, output=OUTPUT):
    snapshot=load(source/'catalog_snapshot.json')
    if not snapshot.get('complete'):raise ValueError('Partial catalog export')
    products=snapshot['products'];by_handle={p['handle']:p for p in products}
    if len(by_handle)!=len(products):raise ValueError('Duplicate current handles')
    proposals=load(source/'family_proposals.json')['proposals']
    original=load(source/'baseline/product-switcher-data.json')
    book=load(source/'book_rules.json')
    exclusions={p['handle']:exclusion(p) for p in products if exclusion(p)}
    eligible=[p for p in products if p['handle'] not in exclusions]
    parsed_by_handle={p['handle']:audit.split_sku(sku_of(p)) for p in eligible}
    by_model=collections.defaultdict(list)
    for p in eligible:
        parsed=parsed_by_handle[p['handle']]
        if parsed:by_model[parsed['model']].append(p)
    base=copy.deepcopy(original['groups'])
    removed=[]
    for g in base:
        kept=[]
        for r in g['products']:
            if r['handle'] in exclusions:removed.append({'group_id':g['id'],'handle':r['handle'],'reason':exclusions[r['handle']]})
            else:kept.append(r)
        g['products']=kept
    base=[g for g in base if len(g['products'])>1]
    # Preserve three colour pilots already implemented by the parent.
    pilot_path=source/'preview-theme/assets'
    index={g['id']:g for g in base}
    for asset in ['bc-hotbath-baa03-switcher-data.json','bc-hotbath-baa09-switcher-data.json','bc-hotbath-baa10-switcher-data.json']:
        for g in load(pilot_path/asset)['groups']:
            index[g['id']]=copy.deepcopy(g)
    # Two explicitly authorized old groups have size/stop valves but no colour.
    # IX is corroborated by the actual SKU, current RVS title, and the Archie
    # finish table (printed61/PDF63). Only the colour option is additive here.
    # ARHF014/015 are retained historical products: their model availability is
    # not claimed to be verified by the current book's model table.
    option_additions=[]
    for gid,models in ADDITIVE_COLOUR_GROUPS.items():
        g=index[gid]
        if any(m['key']=='kleur' for m in g['menus']):
            raise ValueError('Unexpected existing colour menu in authorized group '+gid)
        for r in g['products']:
            p=by_handle[r['handle']];parsed=parsed_by_handle[p['handle']]
            if (parsed['model'] not in models or parsed['colour_code']!='IX'
                    or 'IX' not in audit.title_colours(p['title'])
                    or 'archie' not in p['title'].lower()
                    or 'kleur' in r['options']):
                raise ValueError('Unverified additive colour on '+r['handle'])
            r['options']['kleur']=parsed['colour']
            option_additions.append({'group_id':gid,'handle':r['handle'],'sku':sku_of(p),
                'key':'kleur','field':'options.kleur','value':parsed['colour'],'colour_code':'IX',
                'sources':{'catalogue_title':p['title'],'catalogue_sku':sku_of(p),
                           'book_finish':{'printed_page':61,'pdf_page':63,'manufacturer_label':'RVS 316','finish_code':'IX'},
                           'book_model':({'printed_page':67,'pdf_page':69} if parsed['model'].startswith('AR105') else
                                         {'printed_page':86,'pdf_page':88} if parsed['model'] in {'ARHF011','ARHF012','ARHF013'} else None)},
                'note':'Application canonical label Geborsteld RVS denotes IX; book labels that finish RVS 316. Historical ARHF014/015 stay existing products; no current model/stock claim.'})
        g['menus'].append({'key':'kleur','label':'Kleur','order':max(m.get('order',0) for m in g['menus'])+1,
                          'display_type':'dropdown','hide_if_single_value':True,
                          'values':sorted({r['options']['kleur'] for r in g['products']},key=colour_sort)})
    baseline_handles={r['handle'] for g in original['groups'] for r in g['products']}
    current_owner={r['handle']:g['id'] for g in index.values() for r in g['products']}
    review=[];provenance={};new_groups=[];handled=set();changes=collections.defaultdict(list)
    decision_path=output/'colour_exception_decisions.json'
    decisions=load(decision_path) if decision_path.exists() else {}
    if 'decisions' in decisions:decisions=decisions['decisions']
    if isinstance(decisions,list):decisions={r['proposal_id']:r for r in decisions}
    approved=[]
    for r in proposals:
        if r['model'] in EXCLUSIVE_IBS:continue
        if r['model'].startswith('IBS'):continue
        decision=decisions.get(r['proposal_id'],{})
        promoted=decision.get('decision') in {'APPROVE','PROMOTE','READY'} or decision.get('approved') is True or decision.get('approve_for_colour_group') is True
        if r['confidence']=='HIGH' or promoted:approved.append((r,decision if promoted else None))
        else:review.append({'type':'COLOUR_PROPOSAL_REVIEW','proposal_id':r['proposal_id'],'model':r['model'],'reason_flags':r.get('reason_flags',[])})
    # Existing group IDs and every pre-existing record remain authoritative.
    for r,decision in approved:
        if r['action']!='AUGMENT_EXISTING_GROUP':continue
        ids=r.get('existing_group_ids',[])
        if len(ids)!=1 or ids[0] not in index:
            review.append({'type':'AMBIGUOUS_EXISTING_GROUP','proposal_id':r['proposal_id']});continue
        g=index[ids[0]];candidates=r.get('new_products',[])
        additions=[]
        for row in candidates:
            p=by_handle.get(row['handle'])
            if not p or exclusion(p):continue
            if row['handle'] in current_owner:continue
            opts=row.get('options',{})
            if set(opts)!={m['key'] for m in g['menus']}:
                review.append({'type':'EXISTING_OPTION_SCHEMA_MISMATCH','proposal_id':r['proposal_id'],'sku':row['sku']});continue
            additions.append(new_record(p,opts,max([v.get('sort_order',0) for v in g['products']]+[0])+10*(len(additions)+1)))
        candidate=copy.deepcopy(g);candidate['products']+=additions
        for m in candidate['menus']:
            m['values']=list(dict.fromkeys(m['values']+[x['options'][m['key']] for x in additions]))
        try:assert_group(candidate)
        except ValueError as e:
            review.append({'type':'AUGMENTATION_REJECTED','proposal_id':r['proposal_id'],'reason':str(e)});continue
        index[g['id']]=candidate
        for row in additions:current_owner[row['handle']]=g['id'];changes[g['id']].append(row['handle'])
        handled.add(r['proposal_id'])
        provenance.setdefault(g['id'],{'basis':'EXISTING_GROUP_PRESERVED_PLUS_CATALOGUE_COLOUR_SIBLINGS','proposals':[]})['proposals'].append(r['proposal_id'])
    # Roll up explicit book-defined sizes/heights only if no existing group is touched.
    safe_new={r['proposal_id']:(r,d) for r,d in approved if r['action']=='PROPOSE_NEW_COLOUR_GROUP'}
    for family in book['families']:
        members=family.get('members',[])
        if len(members)<2 or not family.get('member_options'):continue
        selected=[(r,d) for r,d in safe_new.values() if r['model'] in members]
        if not selected or len({r['model'] for r,d in selected})<2:continue
        if any(current_owner.get(p['handle']) for member in members for p in by_model[member]):continue
        all_family_rows=[p for member in members for p in by_model[member]]
        selected_handles={p['handle'] for r,d in selected for p in r['products']}
        if {p['handle'] for p in all_family_rows}!=selected_handles:continue
        records=[];fields=None;invalid=False
        for p in all_family_rows:
            opts,fl=book_options(family,parsed_by_handle[p['handle']])
            if opts is None:invalid=True;break
            records.append(new_record(p,opts,10*(len(records)+1)));fields=fl
        if invalid:continue
        gid='hotbath-book-'+family['id'].lower()+'-keuzes'
        g={'id':gid,'label':'Hotbath '+family['id'],'menus':menus_for(records,fields),'products':records}
        try:assert_group(g)
        except ValueError as e:review.append({'type':'BOOK_MEMBER_GROUP_REJECTED','family':family['id'],'reason':str(e)});continue
        new_groups.append(g)
        for r,d in selected:handled.add(r['proposal_id'])
        provenance[gid]={'basis':'BOOK_EXPLICIT_MODEL_MEMBERS_AND_CURRENT_SKU_COLOURS','book_sources':family['sources'],'model_members':members,'proposals':[r['proposal_id'] for r,d in selected]}
        for p in records:current_owner[p['handle']]=gid
    # One plain model/configuration gets one colour choice, never invented dimensions.
    for r,decision in approved:
        if r['proposal_id'] in handled or r['action']!='PROPOSE_NEW_COLOUR_GROUP':continue
        if r['model']=='M538':continue
        rows=[by_handle[p['handle']] for p in r['products'] if p['handle'] in by_handle and not exclusion(by_handle[p['handle']])]
        if any(p['handle'] in current_owner for p in rows):
            # The pre-existing pilot is already complete and keeps its ID.
            if all(p['handle'] in current_owner for p in rows):handled.add(r['proposal_id']);continue
            review.append({'type':'PARTIAL_EXISTING_OWNER','proposal_id':r['proposal_id']});continue
        if len(rows)<2:continue
        records=[new_record(p,{'kleur':parsed_by_handle[p['handle']]['colour']},10*(i+1)) for i,p in enumerate(rows)]
        suffix=r.get('configuration_suffix','')
        gid='hotbath-colour-'+r['model'].lower()+('-config-'+suffix if suffix else '')
        g={'id':gid,'label':'Hotbath '+r['model'],'menus':menus_for(records,[('kleur','Kleur')]),'products':records}
        try:assert_group(g)
        except ValueError as e:review.append({'type':'COLOUR_GROUP_REJECTED','proposal_id':r['proposal_id'],'reason':str(e)});continue
        new_groups.append(g);handled.add(r['proposal_id'])
        provenance[gid]={'basis':'CATALOGUE_MODEL_SKU_TITLE_VERIFIED','proposal':r['proposal_id'],'book_sources':r.get('book_model_sources',[]),'exception_decision':decision}
        for p in records:current_owner[p['handle']]=gid
    # Remaining complete IBS titles can be consolidated without interpreting SKU digits.
    title_groups=[]
    for model,rows in sorted(by_model.items()):
        if not (model.startswith('IBS') and model not in EXCLUSIVE_IBS or model=='M538'):continue
        if all(p['handle'] in current_owner for p in rows):continue
        if any(p['handle'] in current_owner for p in rows):
            review.append({'type':'CONFIG_EXISTING_OWNER','model':model,'product_count':len(rows)});continue
        required=['kleur','breedte_diameter_hoofddouche','type_handdouche'] if model=='M538' else [k for k,l in CONFIG_FIELDS]
        parsed_rows=[];problems=[]
        for p in rows:
            parsed=parsed_by_handle[p['handle']]
            opts,residual,missing=parse_title_configuration(p,parsed,required)
            seen=audit.title_colours(p['title'])
            # RVS316 in an Archie title denotes material, not a second finish.
            wrong=[c for c in seen if c!=parsed['colour_code'] and c!='IX']
            if parsed['colour_code'] not in seen:problems.append({'sku':sku_of(p),'issue':'COLOUR_NOT_CORROBORATED'})
            if wrong:problems.append({'sku':sku_of(p),'issue':'CONFLICTING_COLOUR','colours':wrong})
            if missing:problems.append({'sku':sku_of(p),'issue':'MISSING_LITERAL_CHOICES','fields':missing})
            parsed_rows.append((p,opts,residual))
        signatures=collections.Counter(res for p,opts,res in parsed_rows)
        if len(signatures)>1:problems.append({'issue':'UNEXPLAINED_RESIDUAL_TITLE_DIFFERENCES','signatures':dict(signatures)})
        if problems:
            review.append({'type':'TITLE_CONFIG_FAMILY_REVIEW','model':model,'product_count':len(rows),'problems':problems});continue
        records=[new_record(p,{k:opts[k] for k in required},10*(i+1)) for i,(p,opts,res) in enumerate(parsed_rows)]
        fields=[x for x in CONFIG_FIELDS if x[0] in required]
        gid='hotbath-title-'+model.lower()+'-doucheset'
        g={'id':gid,'label':'Hotbath '+model+' doucheset','menus':menus_for(records,fields),'products':records}
        try:assert_group(g)
        except ValueError as e:review.append({'type':'TITLE_CONFIG_GROUP_REJECTED','model':model,'reason':str(e)});continue
        title_groups.append(g)
        provenance[gid]={'basis':'CATALOG_TITLE_VERIFIED_NOT_BOOK_OPTION_DECODE','model':model,'literal_fields':required,'residual_signature':list(signatures)[0]}
        for p in records:current_owner[p['handle']]=gid
    # Incomplete configuration titles can still support a useful colour choice
    # within one exact model + unchanged configuration suffix. Never invent the
    # unknown diameter/mount/handshower values or present that as a full config.
    fallback_groups=[]
    fallback_models=set()
    for r in proposals:
        model=r['model']
        if not model.startswith('IBS') or model in EXCLUSIVE_IBS:
            continue
        decision=decisions.get(r['proposal_id'],{})
        if r['confidence']!='HIGH' and not decision.get('approve_for_colour_group'):
            continue
        rows=[by_handle[p['handle']] for p in r['products'] if p['handle'] in by_handle and not exclusion(by_handle[p['handle']])]
        if any(p['handle'] in current_owner for p in rows):
            continue
        if len(rows)<2:
            continue
        if r.get('existing_group_ids'):
            review.append({'type':'FALLBACK_TOUCHES_EXISTING_GROUP','proposal_id':r['proposal_id']})
            continue
        records=[new_record(p,{'kleur':parsed_by_handle[p['handle']]['colour']},10*(i+1)) for i,p in enumerate(rows)]
        suffix=r.get('configuration_suffix','')
        gid='hotbath-colour-'+model.lower()+'-fixed-config-'+(suffix or 'standaard')
        g={'id':gid,'label':'Hotbath '+model+' - vaste samenstelling','menus':menus_for(records,[('kleur','Kleur')]),'products':records}
        try:
            assert_group(g)
        except ValueError as e:
            review.append({'type':'COLOUR_ONLY_FIXED_CONFIG_REJECTED','proposal_id':r['proposal_id'],'reason':str(e)})
            continue
        fallback_groups.append(g);fallback_models.add(model)
        provenance[gid]={'basis':'COLOUR_ONLY_CONFIG_FIXED','model':model,'configuration_suffix':suffix,
                         'proposal':r['proposal_id'],'reason':'Exact model and fixed configuration; only finish varies. No unknown configuration choices inferred.',
                         'exception_decision':decision or None}
        for p in records:
            current_owner[p['handle']]=gid
    for item in review:
        if item['type']=='TITLE_CONFIG_FAMILY_REVIEW' and item['model'] in fallback_models:
            item['configuration_review_status']='COLOUR_ONLY_FALLBACK_CREATED; FULL_CONFIGURATION_CHOICES_NOT_VERIFIED'
    groups=list(index.values())+new_groups+title_groups+fallback_groups
    all_handles=[]
    for g in groups:
        assert_group(g)
        for p in g['products']:
            if p['handle'] not in by_handle or exclusion(by_handle[p['handle']]):raise ValueError('Excluded/missing product in output '+p['handle'])
            all_handles.append(p['handle'])
    if len(all_handles)!=len(set(all_handles)):raise ValueError('Handle appears in multiple output groups')
    # For every original record outside explicitly excluded scope, equality is required.
    final_records={r['handle']:r for g in groups for r in g['products']}
    preserved=0
    for g in original['groups']:
        for r in g['products']:
            if r['handle'] in exclusions:continue
            final=copy.deepcopy(final_records.get(r['handle']))
            allowed=next((a for a in option_additions if a['group_id']==g['id'] and a['handle']==r['handle']),None)
            if allowed:
                if final['options'].pop('kleur',None)!=allowed['value']:raise ValueError('Authorized colour differs '+r['handle'])
            if final!=r:raise ValueError('Original record changed '+r['handle'])
            preserved+=1
    metadata={'schema':'hotbath-colour-groups-v1','basis_snapshot':'2026-10-24','contains_existing_groups':True,
              'exclusive_config_models':sorted(EXCLUSIVE_IBS),'spom_excluded':True,
              'counts':{'baseline_groups':len(original['groups']),'original_records_preserved':preserved,
                        'base_groups_after_pilot_overlay':len(index),'new_colour_or_book_groups':len(new_groups),
                        'new_title_config_groups':len(title_groups),'total_output_groups':len(groups),
                        'fixed_config_colour_only_groups':len(fallback_groups),
                        'fixed_config_colour_only_models':len(fallback_models),
                        'fixed_config_colour_only_records':sum(len(g['products']) for g in fallback_groups),
                        'total_output_records':len(all_handles),'new_records_vs_original':len(set(all_handles)-baseline_handles),
                        'augmented_existing_groups':sum(bool(v) for v in changes.values()),
                        'appended_records_vs_pilot':sum(len(v) for v in changes.values()),
                        'excluded_spom_catalogue':sum(v=='SPOM_EXCLUDED_BY_USER' for v in exclusions.values()),
                        'old_records_with_additive_colour_option':len(option_additions),
                        'excluded_existing_records':len(removed),'review_entries':len(review)},
              'title_config_models':[g['label'] for g in title_groups],
              'fixed_config_colour_only_models':sorted(fallback_models),
              'limits':['No manufacturer inventory claim.','Unresolved family/title contradictions remain excluded from new groups.','Only literal title fields or explicit book member mappings create dimensions.']}
    output.mkdir(parents=True,exist_ok=True)
    (output/'colour_groups.json').write_text(json.dumps({'groups':groups},ensure_ascii=False,indent=2))
    (output/'colour_provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2))
    (output/'colour_review.json').write_text(json.dumps({'metadata':metadata,'excluded_products':exclusions,'removed_existing':removed,'reviews':review},ensure_ascii=False,indent=2))
    (output/'colour_metrics.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2))
    (output/'colour_option_additions.json').write_text(json.dumps({'schema':'hotbath-authorized-additive-options-v1','scope':'Only the two named existing groups and the listed seven records permit options.kleur addition. All other existing fields/options remain identical.','additions':option_additions},ensure_ascii=False,indent=2))
    return metadata

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,default=SOURCE);parser.add_argument('--output',type=Path,default=OUTPUT)
    args=parser.parse_args();print(json.dumps(compile_groups(args.source,args.output),ensure_ascii=False,indent=2))
