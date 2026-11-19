import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
pages = json.loads((ROOT / 'hotbath-menu-20261024/book_pages.json').read_text())
catalog = json.loads((ROOT / 'hotbath-menu-20261024/catalog_snapshot.json').read_text())
old = json.loads((OUT / 'book_mapping_review.json').read_text())
old_models = {x['trim_model'] for x in old['mappings']}
sku_index = {}
for product in catalog['products']:
    for variant in product['variants']['nodes']:
        sku_index.setdefault(variant['sku'], []).append(product)
colors = {'CR','GN','BB','AB','WH','AI','PBP','MBP','BBP','BCP','BGP','TB','IX','BL','NI','RG','PB','BZ','CB','CH'}

def product_skus(model):
    return sorted(s for s in sku_index if s.startswith(model) and s[len(model):] in colors)

def build(model, body, page, finishes=None, status=None, notes='', book_model=None, known=False):
    matches = product_skus(model)
    bodies = [body] if body in sku_index else []
    book_model = book_model or model
    evidence = f'Inbouwdeel {body}; Afbouwdeel {book_model}..; Totaal'
    assert (body, book_model) in re.findall(r'Inbouwdeel\s+([A-Z0-9-]+)\s+Afbouwdeel\s+([A-Z0-9-]+)', pages[page+1]['text'])
    qualified = [s for s in matches if finishes is not None and s[len(model):] in finishes]
    review = [s for s in matches if finishes is not None and s[len(model):] not in finishes]
    if status is None:
        status = 'VERIFIED_BOOK' if bodies else 'MISSING_BODY'
    return {
        'trim_model': model, 'book_trim_model': book_model, 'body_sku': body,
        'qty': 1, 'printed_pages': [page], 'pdf_pages': [page+2],
        'evidence': evidence, 'match_type': 'DIRECT' if model == book_model else 'ALIAS_REVIEW',
        'matched_skus': matches, 'book_confirmed_finishes': sorted(finishes) if finishes is not None else [],
        'approved_finish_skus': qualified if status == 'VERIFIED_BOOK' else [],
        'finish_review_skus': review,
        'body_catalog_skus': bodies, 'body_product_count': len(sku_index.get(body, [])),
        'body_active_published': all(p['status'] == 'ACTIVE' and p.get('publishedAt') for p in sku_index.get(body, [])) if bodies else False,
        'status': status, 'notes': notes, 'visual_verified': True,
        'already_known_as_exception': known,
        'paid_addon_eligible': status == 'VERIFIED_BOOK',
    }

mappings = []
for n in (1,2,3):
    mappings.append(build(f'ARHF01{n}', f'MHF00{n}', 360, {'IX','BGP','BBP','BCP'}, notes='The manufacturer trim model itself has no EXT. Exact SKU plus explicitly listed finish matches.'))
mappings.append(build('KHDS3EXT','HBKHDS3',367,{'CR','GN','BB','AB','WH','PBP','MBP','BBP','BCP'}, notes='KHDS3EXTAI exists in the shop snapshot but AI is absent from this book table; that finish stays in review.'))
mappings.append(build('KHDS4EXT','HBKHDS4',367,{'CR','GN','PBP','MBP','BBP','BCP'}, notes='Manufacturer relation is explicit, but exact body HBKHDS4 is absent from the supplied shop snapshot. Do not substitute HBKHDS3.'))
mappings.append(build('KHDS5EXT','HBKHDS4',367,{'IX','BBP','BCP','BGP'}, notes='This relation was already documented as a missing-body exception, not one of the previous31 model mappings. Not a newly discovered relation.', known=True))

rails = []
for page in list(range(462,473)) + [474,476,477,478]:
    for body, model in re.findall(r'Inbouwdeel\s+([A-Z0-9-]+)\s+Afbouwdeel\s+([A-Z0-9-]+)', pages[page+1]['text']):
        rails.append(build(model,body,page,status='REVIEW',notes='INCLUDED_PRICE_SEPARATE_ORDER: book explicitly says the body is included in the set price but must be ordered separately. Physical compatibility is verified. Do not automatically add a paid extra until shop price and fulfilment treatment are checked.',known=model=='RARH50-1'))
assert len(rails) == 27
assert len({m['trim_model'] for m in rails}) == 27

exceptions = [
    {
        'type':'BOOK_MODEL_CONTRADICTION', 'trim_model':'RASV135-3','body_sku':'MBASES4',
        'printed_pages':[475], 'pdf_pages':[477], 'matched_skus':product_skus('RASV135-3'),
        'evidence':'Page title RASV135-3 and parts list contain RASV135T, RASV135, SWIROU, MBASES4; the table trim label says RASS80-3.. instead.',
        'status':'REVIEW','paid_addon_eligible':False,'visual_verified':True,
        'notes':'Do not copy the table label to infer RASV135-3 automatically. Also subject to included-price separate-order handling.'
    },
    {
        'type':'NO_TABLE_IN_SEGMENT','trim_models':['ARHF014','ARHF015'],
        'matched_skus':product_skus('ARHF014')+product_skus('ARHF015'),
        'status':'REVIEW','notes':'Both exist as trim-only shop products; pages330–502 provide no exact manufacturer table for them. Do not extrapolate MHF004/MHF005 from neighboring model numbers.'
    },
    {
        'type':'BOOK_MODEL_CONTRADICTION','trim_model':'GLF015EXT','printed_pages':[359], 'pdf_pages':[361],
        'status':'REVIEW','notes':'Page title GLF015 but table says MHF015EXT. Prior mapping has independent correct table evidence on printed256; do not use printed359 table as standalone GLF015EXT proof.'
    },
    {'type':'NON_EXT_DISCOVERY','models':['ARHF011','ARHF012','ARHF013'],'notes':'Three confirmed trim models without EXT demonstrate why EXT-only matching would miss valid additions.'},
    {'type':'GHOST_TEXT','printed_pages':[332,384],'notes':'Extracted unrelated AC105/AC111 text is present outside actual displayed product tables. Mappings use visible explicit body/trim tables only.'}
]

assert not (old_models & {m['trim_model'] for m in mappings})
all_matched = [s for m in mappings+rails for s in m['matched_skus']]
assert len(all_matched)==len(set(all_matched))
assert not any('SPOM' in s or s.startswith('IBS') for s in all_matched)
verified = [m for m in mappings if m['status']=='VERIFIED_BOOK']
result={
    'schema':'hotbath-inbouw-expansion-segment-v1','segment':'c','read_only':True,
    'source_pdf':'upload/Hotbath%20Catalogus%20Editie%2018.pdf',
    'source_snapshot':'hotbath-menu-20261024/catalog_snapshot.json',
    'snapshot_captured_at':catalog.get('captured_at'),
    'coverage':{'printed_pages':[330,502],'pdf_pages':[332,504],
        'method':'Full segment keyword scan for inbouwdeel/afbouwdeel/afdekset/inbouwelement and explicit parts-price tables; table pairs crosschecked visually on printed360,367 and all Rails table pages462–478. Body/trim candidates matched by exact known color suffix only.',
        'visually_reviewed_pages':[360,367]+list(range(462,473))+list(range(474,479)),
        'limits':'Shop data is a prior same-day snapshot, not a fresh API read. No deployment, product changes or cart behavior implemented. MHF and GLF previous31 models excluded.'},
    'summary':{'new_verified_normal_models':len(verified),'new_verified_normal_skus':sum(len(m['approved_finish_skus']) for m in verified),
        'normal_candidate_skus':sum(len(m['matched_skus']) for m in mappings),
        'new_missing_body_models':1,'previously_known_missing_body_models':1,
        'rails_verified_physical_relations_requiring_commercial_review':len(rails),
        'rails_candidate_skus':sum(len(m['matched_skus']) for m in rails),
        'additional_rails_book_contradiction_models':1},
    'mappings':mappings+rails,'exceptions':exceptions
}
(OUT/'expansion-c.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['summary'],indent=2))
