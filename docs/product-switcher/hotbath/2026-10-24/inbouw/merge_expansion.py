import json,re,collections,hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def read(name): return json.loads((ROOT/name).read_text())
old=read('book_mapping_review.json')
old_models={x['trim_model'] for x in old['mappings']}
old_skus={p['sku'] for m in old['mappings'] for p in m['current_trim_products']}
live=read('expansion-live-products.json')['products']
by_sku=collections.defaultdict(list)
for p in live:
 assert p and not p['variants']['pageInfo']['hasNextPage']
 for v in p['variants']['nodes']: by_sku[v['sku']].append((p,v))
parts={c:read('expansion-'+c+'.json') for c in 'abc'}
catalog_path=ROOT.parent/'hotbath-menu-20261024/catalog_snapshot.json'
if catalog_path.exists():
 all_skus={v['sku'] for p in json.loads(catalog_path.read_text())['products'] for v in p['variants']['nodes']}
else:
 # Portable replay from the persisted live candidate read and source-derived candidate sets.
 all_skus=set(by_sku)
 for d in parts.values():
  for m in d['mappings']:
   all_skus.update(m.get('candidate_skus',m.get('matched_skus',[])))
groups=collections.defaultdict(list)
for c,d in parts.items():
 for m in d['mappings']:
  assert m['trim_model'] not in old_models
  groups[m['trim_model'],m['body_sku']].append((c,m))
records=[]
for (model,body),sources in sorted(groups.items()):
 colors=set()
 for _,m in sources:
  colors.update(m.get('book_colors',m.get('book_finishes',m.get('book_confirmed_finishes',[]))))
 # Only exact model + explicitly listed finish. Do not use wildcard-prefix grouping.
 candidates=sorted(s for s in all_skus if re.fullmatch(re.escape(model)+r'[A-Z]+',s))
 matched=sorted(s for s in candidates if s[len(model):] in colors)
 statuses={m['status'] for _,m in sources}
 special=('REVIEW' in statuses or any(m.get('selection_required') for _,m in sources))
 body_matches=by_sku.get(body,[])
 body_ok=len(body_matches)==1 and body_matches[0][0]['status']=='ACTIVE' and bool(body_matches[0][0]['publishedAt']) and body_matches[0][1]['availableForSale'] and float(body_matches[0][1]['price'])>0
 body_id=body_matches[0][1]['id'] if len(body_matches)==1 else None
 sku_reviews=[];ready=[]
 for sku in matched:
  rows=by_sku.get(sku,[]); reasons=[]
  if len(rows)!=1:reasons.append('EXACT_LIVE_SKU_NOT_UNIQUE_OR_NOT_READ')
  else:
   p,v=rows[0]
   if p['status']!='ACTIVE' or not p['publishedAt'] or not v['availableForSale'] or float(v['price'])<=0:reasons.append('TRIM_NOT_CURRENTLY_SELLABLE')
   if (p.get('included') or {}).get('value')=='true':reasons.append('SHOP_DATA_SAYS_BODY_INCLUDED')
   if re.search(r'inclusief\s+(?:het\s+)?inbouwdeel',p['title'],re.I):reasons.append('TITLE_SAYS_BODY_INCLUDED')
  if not body_ok:reasons.append('BODY_MISSING_OR_NOT_SELLABLE')
  if special:reasons.append('MODEL_REQUIRES_REVIEW_OR_EXTRA_CHOICE')
  if 'SPOM' in body or 'SPOM' in sku or sku.startswith('IBS'):reasons.append('OUTSIDE_NORMAL_ADDON_SCOPE')
  if not any(m['status']=='VERIFIED_BOOK' and m.get('visual_verified') for _,m in sources):reasons.append('NO_UNAMBIGUOUS_VISUALLY_VERIFIED_TABLE')
  if reasons:sku_reviews.append({'sku':sku,'reasons':reasons})
  else:
   p,v=rows[0]
   ready.append({'trim_sku':sku,'trim_product_id':p['id'],'trim_variant_id':v['id'],'trim_handle':p['handle'],'body_sku':body,'body_variant_id':body_id,'quantity_per_trim':1,'met_inbouwdeel':(p.get('included') or {}).get('value')})
 notes=[]
 for c,m in sources:
  n=m.get('notes',[]);notes.extend(n if isinstance(n,list) else [n])
 if model=='KHDS3EXT':notes.append('Cross-page resolution: AI is absent from p367 but explicitly listed in p176/304; accept AI using those pages. Omission on one page is not a contradiction of the positive same-model evidence elsewhere.')
 records.append({'trim_model':model,'body_sku':body,'quantity_per_trim':1,'printed_pages':sorted({p for _,m in sources for p in m['printed_pages']}),'source_segments':[c for c,_ in sources],'source_statuses':sorted(statuses),'book_finishes':sorted(colors),'candidate_skus':candidates,'exact_book_finish_skus':matched,'unlisted_finish_skus':sorted(set(candidates)-set(matched)) if colors else [],'current_body_variant_id':body_id,'body_currently_sellable':body_ok,'ready_skus':ready,'review_skus':sku_reviews,'requires_model_review':special,'notes':list(dict.fromkeys(notes)),'source_evidence':[{'segment':c,'evidence':m['evidence']} for c,m in sources],'visual_verified':all(m.get('visual_verified',False) for _,m in sources)})
flat=[r for m in records for r in m['ready_skus']]
counts=collections.Counter(r['trim_sku'] for r in flat)
assert all(c==1 for c in counts.values()),'Duplicate ready trim mapping'
assert not (set(counts)&old_skus),'New count includes previous articles'
assert all(r['body_sku']!=r['trim_sku'] for r in flat)
assert all(r['quantity_per_trim']==1 and r['body_variant_id'] for r in flat)
ready_models={m['trim_model'] for m in records if m['ready_skus']}
rails=[m for m in records if m['trim_model'].startswith('RA')]
summary={'previous_investigated_models':len(old_models),'previous_investigated_articles':len(old_skus),'new_simple_ready_models':len(ready_models),'new_simple_ready_articles':len(flat),'new_unique_model_records_including_holds':len({m['trim_model'] for m in records}),'new_relation_records_including_holds':len(records),'rails_models_commercial_review':len(rails),'rails_candidate_articles':len({s for m in rails for s in m['candidate_skus']}),'fresh_products_read':len(live),'missing_body_codes_with_live_exact_search':['HBCB001','HBKHDS4','HBCB7069','HBGL7071','HBGL7072'],'installed':False}
out={'schema':'hotbath-inbouw-expansion-consolidated-v1','date':'2026-10-24','status':'SOURCE_AND_ADMIN_VERIFIED_CANDIDATES_NOT_INSTALLED','summary':summary,'sources':{c:hashlib.sha256((ROOT/f'expansion-{c}.json').read_bytes()).hexdigest() for c in 'abc'},'limits':['No Ja/Nee feature, cart action, theme or product mutation performed.','This is an expansion beyond previous31; previous five MHF aliases retain review.','All book pages scanned for body/trim candidate signals; not a claim of all possible historical Hotbath compatibility.','Live reads refresh exact candidates from earlier full catalog; newly created product discovery was not a full fresh catalog rescan.','Prices and availability must be fetched again at actual implementation/runtime.','Rails remain excluded from paid addons because body price is already included.','SPOM targets held as a scope exception, not a compatibility failure.'],'records':records}
(ROOT/'expansion-consolidated.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(ROOT/'expansion-ready-variants.json').write_text(json.dumps({'schema':'hotbath-inbouw-additional-variant-mappings-v1','installed':False,'source':'expansion-consolidated.json','mappings':flat},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('Ready examples:',[(m['trim_model'],m['body_sku'],len(m['ready_skus'])) for m in records if m['ready_skus']][:20])
