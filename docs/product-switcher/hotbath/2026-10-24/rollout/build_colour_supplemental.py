#!/usr/bin/env python3
"""Small scoped supplement: exact letter-only accessory models and SDS32."""
import collections
import json
import re
from pathlib import Path

import build_colour_groups as core

HERE=Path(__file__).resolve().parent
LETTER_MODELS={
    'RAAR':('Hotbath ronde haak voor RARV135/RARVM135 rails',480),
    'RAAS':('Hotbath rechthoekige haak voor RASV135 rails',477),
    'SWIROU':('Hotbath ronde temperatuur/timer-schakelaar voor rails',466),
}
SDS_REPLACE=['hotbath-colour-sds32-config-4','hotbath-colour-sds32-config-5','hotbath-colour-sds32-config-6']

def decode_letters(sku):
    for model in LETTER_MODELS:
        if sku.startswith(model) and sku[len(model):] in core.audit.PALETTE:
            code=sku[len(model):]
            return model,code,core.audit.PALETTE[code][0]
    return None

def strip_literal_identity(title,sku):
    return re.sub(r'\W+',' ',title.lower().replace(sku.lower(),'')).strip()

def parse_sds_literal(p):
    sku=core.sku_of(p)
    parsed=core.audit.split_sku(sku)
    if not parsed or parsed['model']!='SDS32':return None
    m=re.search(r'(\d+)\s*cm\s*hoofd?douche\s*\((\d+)\s*mm\)',p['title'],re.I)
    if not m:return None
    if parsed['configuration_suffix'] not in {'','4','5','6'}:return None
    # These are the literal normal set titles. Differently described round-hand
    # sets remain review, rather than inheriting an assumed standard component.
    residual=p['title'].lower().replace(sku.lower(),'')
    residual=re.sub(r'(\d+)\s*cm\s*hoofd?douche\s*\((\d+)\s*mm\)',' ',residual)
    for alias in sorted({a for label,aliases in core.audit.PALETTE.values() for a in aliases},key=len,reverse=True):
        residual=re.sub(r'(?<!\w)'+re.escape(alias)+r'(?!\w)',' ',residual)
    residual=re.sub(r'\W+',' ',residual).strip()
    seen=core.audit.title_colours(p['title'])
    if parsed['colour_code'] not in seen or any(c not in {parsed['colour_code'],'IX'} for c in seen):
        raise ValueError('SDS32 title finish conflict '+sku)
    return {'kleur':parsed['colour'],'diameter_hoofddouche':m[1]+' cm','dikte_hoofddouche':m[2]+' mm'},residual

def build():
    catalog=json.loads((core.SOURCE/'catalog_snapshot.json').read_text())['products']
    book={p['pdf_page']:p['text'] for p in json.loads((core.SOURCE/'book_pages.json').read_text())}
    stable=json.loads((HERE/'groups-input.json').read_text())['groups']
    groups=[];proof={};reviews=[];identities=collections.defaultdict(list)
    for p in catalog:
        if core.exclusion(p):continue
        decoded=decode_letters(core.sku_of(p))
        if decoded:identities[decoded[0]].append((p,decoded))
    for model,(label,page) in LETTER_MODELS.items():
        rows=identities[model]
        signatures={strip_literal_identity(p['title'],core.sku_of(p)) for p,d in rows}
        if len(signatures)!=1:raise ValueError('Different exact identity titles for '+model)
        if not re.search(r'\b'+model+r'\b',book[page]):raise ValueError('Missing explicit book model '+model)
        records=[core.new_record(p,{'kleur':d[2]},(i+1)*10) for i,(p,d) in enumerate(rows)]
        group={'id':'hotbath-colour-'+model.lower(),'label':label,
               'menus':core.menus_for(records,[('kleur','Kleur')]),'products':records}
        core.assert_group(group);groups.append(group)
        proof[group['id']]={'basis':'EXACT_LETTER_MODEL_CATALOGUE_TITLE_AND_BOOK_COMPONENT_IDENTITY',
            'model':model,'literal_identity_signature':next(iter(signatures)),
            'book_source':{'printed_page':page-2,'pdf_page':page},
            'finish_mapping_source':{'printed_page':7,'pdf_page':9,'basis':'Exact SKU finish suffix to official finish-code palette; current catalogue variants only.'},
            'component_scope':'Accessory/component only; never grouped with complete rails or mirrored product.',
            'notes':['RAAR heading identifies round hook; its book price-table row says RAAS, recorded as book typo, not used to rename SKU.'] if model=='RAAR' else []}
    sds=[];signatures=set()
    for p in catalog:
        sku=core.sku_of(p)
        if not sku.startswith('SDS32'):continue
        if core.exclusion(p):
            reviews.append({'sku':sku,'reason':core.exclusion(p)});continue
        parsed=parse_sds_literal(p)
        if not parsed:
            reviews.append({'sku':sku,'reason':'Round-handshower title/component difference or missing literal diameter/thickness. No inference from numeric suffix.'});continue
        options,signature=parsed;sds.append(core.new_record(p,options,10*(len(sds)+1)));signatures.add(signature)
    if len(signatures)!=1:raise ValueError('SDS32 unexplained residual title difference')
    group={'id':'hotbath-archie-sds32-opbouw-doucheset-keuzes','label':'Hotbath Archie SDS32 opbouwdoucheset',
           'menus':core.menus_for(sds,[('kleur','Kleur'),('diameter_hoofddouche','Diameter hoofddouche'),('dikte_hoofddouche','Dikte hoofddouche')]),
           'products':sds}
    for menu in group['menus']:
        if menu['key']!='kleur':menu['values'].sort(key=lambda value:int(value.split()[0]))
    core.assert_group(group);groups.append(group)
    proof[group['id']]={'basis':'CATALOG_LITERAL_DIAMETER_THICKNESS_AND_COLOUR_WITH_BOOK_MODEL',
        'model':'SDS32','book_source':{'printed_page':74,'pdf_page':76},
        'literal_identity_signature':next(iter(signatures)),
        'literal_fields':['diameter_hoofddouche','dikte_hoofddouche','kleur'],
        'replaces_group_ids':SDS_REPLACE,
        'fixed_component_scope':'Same residual catalogue title for normal set; three different round-handshower titles are excluded. No unknown handshower model inferred.'}
    ids={g['id'] for g in stable}
    if not set(SDS_REPLACE)<=ids:raise ValueError('Unexpected stable input: replacement IDs missing')
    old_handles={p['handle'] for g in stable if g['id'] not in SDS_REPLACE for p in g['products']}
    handles=[p['handle'] for g in groups for p in g['products']]
    if len(handles)!=len(set(handles)) or set(handles)&old_handles:raise ValueError('Supplemental ownership conflict')
    replaced={p['handle'] for g in stable if g['id'] in SDS_REPLACE for p in g['products']}
    if not replaced<=set(handles):raise ValueError('Replacement loses old generated group members')
    metadata={'schema':'hotbath-colour-supplemental-v1','groups':len(groups),'records':len(handles),
        'new_connections_vs_stable_input':len(set(handles)-replaced),'replaces_group_ids':SDS_REPLACE,
        'pure_letter_model_counts':{m:len(identities[m]) for m in LETTER_MODELS},
        'sds32_records':len(sds),'review':reviews,'limits':['No Shopify/Git changes.','No manufacturer stock claim.','SDS32BGP remains hard HOLD.']}
    return {'groups':groups},proof,metadata

if __name__=='__main__':
    data,proof,metadata=build()
    for filename,value in [('colour_supplemental.json',data),('colour_supplemental_provenance.json',proof),('colour_supplemental_review.json',metadata)]:
        (HERE/filename).write_text(json.dumps(value,ensure_ascii=False,indent=2))
    print(json.dumps(metadata,ensure_ascii=False,indent=2))
