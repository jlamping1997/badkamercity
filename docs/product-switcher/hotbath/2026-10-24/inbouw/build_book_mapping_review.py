import json,re,collections
from pathlib import Path
ROOT=Path('/workspace/scratch/6866aa3baeaf/hotbath-inbouw-20261024')
SRC=ROOT.parent/'hotbath-menu-20261024'
book=json.loads((SRC/'book_pages.json').read_text())
snap=json.loads((SRC/'catalog_snapshot.json').read_text())
products=snap['products']
rows=[]
for p in products:
 for v in p['variants']['nodes']:
  rows.append({'sku':v['sku'],'title':p['title'],'product_id':p['id'],'handle':p['handle'],'status':p['status'],'published':bool(p.get('publishedAt')),'price':v['price']})
by_sku=collections.defaultdict(list)
for r in rows:by_sku[r['sku']].append(r)
def sources(pp):return [{'printed_page':p,'pdf_page':p+2} for p in pp]
def matching(root):return [r for r in rows if re.fullmatch(re.escape(root)+r'[A-Z]+',r['sku'])]
# Every row below is taken from an explicit Inbouwdeel/Afbouwdeel price table, not from prefix guessing.
specs=[
 ('CB105EXT18','HBCB105',[170],'DIRECT'),('CB105EXT25','HBCB105',[170],'DIRECT'),
 ('CB105TEXT18','HBCB105T',[171],'DIRECT'),('CB105TEXT25','HBCB105T',[171],'DIRECT'),
 ('CB106EXT18','HBCB105',[172],'DIRECT'),('CB106EXT25','HBCB105',[172],'DIRECT'),
 ('CB006TEXT18','HBCB005T',[173],'DIRECT'),('CB006TEXT25','HBCB005T',[173],'DIRECT'),
 ('AR105EXT18','HBCB105',[67],'DIRECT'),('AR105EXT25','HBCB105',[67],'DIRECT'),('AR125EXT','HBCB105',[68],'DIRECT'),
 ('AR009EXT','MB009',[77],'DIRECT'),
 ('CB009EXT','HB009',[194,282],'DIRECT'),('CB007EXT','HB007',[194,282],'DIRECT'),
 ('CB7009EXT','HBCB7009',[187],'DIRECT'),('CB7067EXT','HBCB7067',[187],'DIRECT'),
 ('AR7009EXT','HBCB7009',[81],'DIRECT'),('AR7067EXT','HBCB7067',[81],'DIRECT'),
 ('MHF011','MHF001',[356],'EXPLICIT_CURRENT_SKU_ALIAS'),('MHF012','MHF002',[356],'EXPLICIT_CURRENT_SKU_ALIAS'),('MHF013','MHF003',[356],'EXPLICIT_CURRENT_SKU_ALIAS'),
 ('MHF014','MHF004',[357],'EXPLICIT_CURRENT_SKU_ALIAS'),('MHF015','MHF005',[357],'EXPLICIT_CURRENT_SKU_ALIAS'),
 ('GLF011EXT','MHF001',[358],'DIRECT'),('GLF012EXT','MHF002',[358],'DIRECT'),('GLF013EXT','MHF003',[358],'DIRECT'),
 ('GLF014EXT','MHF004',[359],'DIRECT'),('GLF015EXT','MHF005',[256],'DIRECT'),
 ('AC009EXT','HBAC009',[308],'DIRECT'),('AC039EXT','HBAC039',[308],'DIRECT'),
 ('AC177EXT','HBCB177',[311],'DIRECT')]
mappings=[]
for trim,body,pp,kind in specs:
 booktrim=trim+'EXT' if kind=='EXPLICIT_CURRENT_SKU_ALIAS' else trim
 texts=[book[p+1]['text'] for p in pp]
 evidence=[]
 for p,t in zip(pp,texts):
  pattern=r'Inbouwdeel\s+'+re.escape(body)+r'\s+Afbouwdeel\s+'+re.escape(booktrim)+r'\.*\s+Totaal'
  m=re.search(pattern,t)
  evidence.append({'printed_page':p,'pdf_page':p+2,'table_pair_present':bool(m),'table_evidence':' '.join(m.group(0).split()) if m else None})
 found=matching(trim);bodies=by_sku.get(body,[])
 body_ready=len(bodies)==1 and bodies[0]['status']=='ACTIVE' and bodies[0]['published']
 conflicting=[r for r in found if re.search(r'inclusief.*inbouw|compleet|complete',r['title'],re.I)]
 mappings.append({'trim_model':trim,'book_trim_table_model':booktrim,'body_sku':body,'body_quantity_per_trim_unit':1,
 'source_type':'EXPLICIT_MANUFACTURER_PARTS_PRICE_TABLE','sources':sources(pp),'evidence':evidence,
 'current_trim_sku_match':kind,'current_trim_products':found,'current_trim_count':len(found),
 'body_matches':bodies,'body_unique_active_published':body_ready,
 'assembly_requirement':'ONE_BODY_PER_ONE_TRIM_UNIT',
 'current_sale_content':'TRIM_ONLY_SUPPORTED_BY_EXACT_MODEL_AND_TABLE' if kind=='DIRECT' else 'TRIM_SUPPORTED_BY_BOOK_HEADING_AND_TABLE_PLUS_CURRENT_SKU_ALIAS',
 'included_in_trim_price':'NO_ACCORDING_TO_SEPARATE_BOOK_INBOUWDEEL_A FBOUWDEEL_COLUMNS'.replace('A F','AF'),
 'title_inclusion_conflicts':conflicting,
 'automatic_addon_eligibility':'CANDIDATE_FOR_CONTROLLED_PILOT' if body_ready and found and not conflicting and kind=='DIRECT' else 'REVIEW_ALIAS_OR_MISSING_TARGET',
 'notes':['This is a proposed compatibility record, not a claim that a cart addon is installed or tested.','Live variant IDs, price/tax, product availability and exact sale-content readback remain mandatory before implementation.']+(['Current Shopify trim SKUs omit EXT; the catalog heading names '+trim+' while the table uses '+booktrim+'. Approve this alias once explicitly; do not globally insert EXT.'] if kind!='DIRECT' else [])})
# Prefer the bounded fresh Admin readback when provided by root.
fresh_path=ROOT/'shopify-cb105-family.json'
fresh_info=None
if fresh_path.exists():
 fresh=json.loads(fresh_path.read_text())
 fresh_rows=[]
 for p in fresh['nodes']:
  for v in p['variants']['nodes']:
   fresh_rows.append({'sku':v['sku'],'title':p['title'],'product_id':p['id'],'handle':p['handle'],'status':p['status'],'published':bool(p.get('publishedAt')),'price':v['price'],'variant_id':v['id'],'available_for_sale':v.get('availableForSale'),'met_inbouwdeel':p.get('included'),'components':p.get('components')})
 for m in mappings:
  if m['trim_model'] in ['CB105EXT18','CB105EXT25','CB105TEXT18','CB105TEXT25']:
   m['current_trim_products']=[r for r in fresh_rows if re.fullmatch(re.escape(m['trim_model'])+r'[A-Z]+',r['sku'])]
   m['current_trim_count']=len(m['current_trim_products'])
   m['body_matches']=[r for r in fresh_rows if r['sku']==m['body_sku']]
   m['live_readback_source']=str(fresh_path)
   m['sale_content_readback']='met_inbouwdeel=false on every matched trim SKU'
 fresh_info={'source':str(fresh_path),'records':len(fresh['nodes']),'trim_records':sum(m['current_trim_count'] for m in mappings if m.get('live_readback_source')),'all_trims_met_inbouwdeel_false':all(r.get('met_inbouwdeel',{}).get('value')=='false' for m in mappings if m.get('live_readback_source') for r in m['current_trim_products'])}
# Complete sets explicitly list the body as already part of the standard assembly.
sets=[('IBS7009','HBCB7009',199),('IBS70','HBCB7067',200),('IBS20','HB007',202),('IBS20A','HB009',203),('IBS1','HB007',286),('IBS1A','HB009',287),('IBS12','HB007',288),('IBS12A','HB009',289)]
finishes=['BBP','BCP','MBP','PBP','BGP','NBP','CR','GN','BB','AB','WH','AI','TB','BL','BK','NB','RG','IX']
complete=[]
for model,body,p in sets:
 matches=[r for r in rows if re.fullmatch(re.escape(model)+r'(?:'+'|'.join(finishes)+r')\d*',r['sku'])]
 t=book[p+1]['text'];cut=t.find('Deze standaardset bestaat uit:');excerpt=t[cut:cut+500] if cut>=0 else ''
 complete.append({'model':model,'body_sku_already_in_set':body,'body_qty_in_set':1,'sources':sources([p]),'parts_list_evidence':excerpt,'current_products_count':len(matches),'current_skus':sorted(r['sku'] for r in matches),'addon_rule':'DO_NOT_OFFER_OR_ADD_BODY_AGAIN','sale_content':'COMPLETE_SET_INCLUDES_BODY'})
ext=[r for r in rows if 'EXT' in r['sku']]
missing_trim_word=[r for r in ext if not re.search(r'afbouw|afdek',r['title'],re.I)]
neutral=[r for r in rows if 'EXT'not in r['sku'] and re.search(r'afbouw|afdekset',r['title'],re.I)]
rails=[r for r in rows if r['sku'].startswith('RARH50-1')]
exceptions=[
 {'type':'NO_EXT_FALSE_NEGATIVE','example_skus':['MHF011CR','MHF012GN','MHF013BBP','MHF014BCP','MHF015MBP'],'proof':'Current titles identify Afdekset or same exact book heading model; table uses MHF011EXT.. to MHF015EXT...','sources':sources([356,357]),'action':'Explicit mapping/alias, not EXT requirement.'},
 {'type':'BODY_PREFIX_GUESS_FAILURE','examples':[{'trim':'AR009EXTIX','body':'MB009','printed_page':77},{'trim':'CB009EXTCR','body':'HB009','printed_page':194},{'trim':'CB006TEXT18CR','body':'HBCB005T','printed_page':173},{'trim':'GLF011EXTCR','body':'MHF001','printed_page':358}],'action':'Store exact source-confirmed body SKU; never prepend HB mechanically.'},
 {'type':'COMPLETE_SET_DUPLICATION','example':'IBS70CR -> body HBCB7067 is already included in the standard set.','sources':sources([200]),'action':'No extra body Yes/No; at most a non-chargeable included-item explanation.'},
 {'type':'INCLUDED_PRICE_BUT_SEPARATE_ORDER','model':'RARH50-1','body':'MBASES2','sources':sources([462]),'evidence':'Let op: het inbouwdeel is inbegrepen in de setprijs, maar moet wel apart worden besteld.','current_products':rails,'body_matches':by_sku.get('MBASES2',[]),'action':'Commercial/fulfilment review. Adding separately with full body price may double-charge. Do not use the ordinary paid addon rule.'},
 {'type':'MISSING_CATALOG_TARGET','model':'KHDS5EXT','body':'HBKHDS4','sources':sources([367]),'evidence':'The table explicitly pairs KHDS5EXT.. with HBKHDS4, not HBKHDS5.','current_trim_products':matching('KHDS5EXT'),'body_matches':by_sku.get('HBKHDS4',[]),'action':'No addon while exact target is absent. Never substitute a guessed body.'},
 {'type':'EXT_FALSE_POSITIVE_NOT_ESTABLISHED','proof':'No source-verified current SKU containing EXT but proven not a trim was established within this bounded review. 27 EXT titles omit the explicit trim label; that is ambiguity, not proof of a false positive.','action':'Keep unknown semantics in review; do not invent counterexamples.'}
]
method=[
 'Classify sale content first: TRIM_ONLY, COMPLETE_SET_INCLUDES_BODY, BODY_ONLY, INCLUDED_PRICE_SEPARATE_ORDER, UNKNOWN.',
 'Discover candidates through EXT/TEXT plus title Afbouwdeel/Afdekset and exact catalog models; neither signal is decisive alone.',
 'Read the exact manufacturer table row or component list. Record exact body SKU, quantity, edition, printed/PDF page and evidence.',
 'Expand a verified trim model across color or length only where the exact model family is supported. Keep explicitly verified aliases as exceptions.',
 'Resolve the body by exact SKU to exactly one active published product; never derive or substitute a target. Retrieve live sellable variant ID before any cart work.',
 'If the body is already included in the set or price, block the normal paid addon and handle inclusion/fulfilment separately.',
 'For a confirmed trim-only item, Yes selects the exact body with quantity equal to trim quantity; No means the customer already has it. Default and copy require a clear customer choice.',
 'Test color/length switches, body deduplication, quantity changes, remove/add, cart matching and checkout totals before deployment.'
]
summary={'mapped_trim_models':len(mappings),'current_trim_products_matched':sum(m['current_trim_count'] for m in mappings),'direct_model_mappings':sum(m['current_trim_sku_match']=='DIRECT'for m in mappings),'explicit_alias_mappings':sum(m['current_trim_sku_match']!='DIRECT'for m in mappings),'all_mapped_body_targets_unique_active_published':all(m['body_unique_active_published'] for m in mappings),'all_table_pairs_found':all(all(e['table_pair_present'] for e in m['evidence']) for m in mappings),'ext_skus':len(ext),'ext_skus_without_explicit_trim_word_in_title':len(missing_trim_word),'trim_word_skus_without_ext':len(neutral),'complete_set_exclusion_models':len(complete)}
result={'schema':'hotbath-inbouw-book-mapping-review-v1','date':'2026-10-24','read_only':True,'source_pdf':'/workspace/scratch/6866aa3baeaf/upload/Hotbath%20Catalogus%20Editie%2018.pdf','source_snapshot':str(SRC/'catalog_snapshot.json'),'snapshot_captured_at':snap['captured_at'],'scope':'Bounded source-backed representative mappings; not a complete Hotbath compatibility catalog, no API/product/theme mutations.','summary':summary,'fresh_cb105_readback':fresh_info,'method':method,'mappings':mappings,'complete_set_exclusions':complete,'exceptions':exceptions,'ext_missing_trim_title_examples':missing_trim_word,'trim_without_ext_examples':neutral,'validation_limits':['The baseline snapshot does not include sellable variant IDs. Fresh CB105 readback, when attached, supplies them for that bounded 40-SKU pilot only.','Manufacturer compatibility is not inferred from the listed price. Discount and price differences cannot prove pack contents.','The baseline snapshot lacks description/metafields/included-components. The separate fresh CB105 readback confirms met_inbouwdeel=false for all40pilottrims; other families still require sale-content checks.','Finish codes absent from this edition are not automatically invalid; mechanical mapping needs exact model confirmation.']}
(ROOT/'book_mapping_review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
md=['# Hotbath afbouwdeel naar inbouwdeel - broncontrole','','24 oktober 2026. Alleen analyse van catalogus editie18 en de bestaande Shopify-snapshot. Geen wijzigingen aan webshop of producten.','','## Uitkomst','','Een betrouwbare koppeling kan via een expliciete compatibiliteitstabel. EXT helpt artikelen vinden, maar bepaalt niet zelfstandig het passende inbouwdeel of wat al bij de prijs hoort.','',f'{summary["mapped_trim_models"]} afbouwmodellen onderzocht; {summary["current_trim_products_matched"]} huidige kleur-/maatartikelen gevonden. Alle doel-inbouwdelen in deze mapping komen uniek, actief en gepubliceerd voor in de snapshot. Vijf MHF-modellen vereisen een expliciete alias omdat hun Shopify-SKU geen EXT bevat.','','## Methodiek','']
md += [f'{i+1}. {x}' for i,x in enumerate(method)]
md += ['','## Bronvaste representatieve koppelingen','','| Afbouwmodel in Shopify | Exact inbouwdeel | Aantal | Gedrukt / PDF | Huidige SKU-aantallen |','|---|---|---:|---|---:|']
for m in mappings:md.append(f'| {m["trim_model"]} | {m["body_sku"]} | 1 | '+', '.join(f'{r["printed_page"]}/{r["pdf_page"]}' for r in m['sources'])+f' | {m["current_trim_count"]} |')
md += ['','Elke directe koppeling staat in een tabel met afzonderlijke kolommen Inbouwdeel, Afbouwdeel en Totaal. Een combinatieprijs in die tabel betekent niet dat een Shopify-SKU met alleen het afbouwmodel ook het inbouwdeel bevat. De exacte SKU en leveringsinhoud moeten vóór gebruik overeenkomen.','','## Compleetsets: geen tweede inbouwdeel toevoegen','','| Complete set | Inbegrepen inbouwdeel | Gedrukt / PDF |','|---|---|---|']
for x in complete:md.append(f'| {x["model"]} | {x["body_sku_already_in_set"]} | {x["sources"][0]["printed_page"]}/{x["sources"][0]["pdf_page"]} |')
md += ['','De onderdelenlijsten noemen de body al in de standaardset. Een apart betaald Ja/Nee-inbouwdeel bij deze sets kan dubbel leveren en dubbel berekenen.','','## Belangrijke uitzonderingen','',
 '- **CB009EXT → HB009**, niet HBCB009. **AR009EXT → MB009**, niet HBAR009. **CB006TEXT → HBCB005T**, niet HBCB006T. **GLF011EXT → MHF001**. Een HB-prefixregel is dus onbetrouwbaar.',
 '- **MHF011..015 zonder EXT** zijn toch afdek-/afbouwmodellen. Het boek gebruikt in de tabel MHF011EXT.. tot MHF015EXT..; de kop en actuele Shopify-SKU ondersteunen de expliciete alias. Die alias moet eenmalig als uitzondering worden goedgekeurd.',
 '- **Rails RARH50-1 / MBASES2**: p462/PDF464 vermeldt dat het inbouwdeel al in de setprijs zit maar apart moet worden besteld. Dit vraagt een andere prijs-/afhandelregel dan een gewone betaalde aanvulling.',
 '- **KHDS5EXT → HBKHDS4**: p367/PDF369. Het exacte doelartikel is niet in de snapshot gevonden. Geen vervangend of afgeleid artikel koppelen.',
 f'- **EXT-statistiek:** {len(ext)} SKU’s bevatten EXT; {len(missing_trim_word)} titels daarvan zeggen niet expliciet afbouw/afdek. Omgekeerd hebben {len(neutral)} SKU’s zonder EXT wel een afbouw-/afdeksetlabel. Er is binnen deze beperkte controle geen bewezen EXT-foutpositief gevonden.',
 '- **Afbeelding of prijs is onvoldoende bewijs.** Een technische tekening kan beide delen tonen en het boek kan een totaalprijs noemen, terwijl de gekozen afbouw-SKU los verkocht wordt.',
 '','## Wat nog nodig is vóór bouwen','','Leest de live productvariant-ID van elk exact doelartikel uit, controleer de omschrijving/leveringsinhoud, leg de keuze en hoeveelheid vast en test de winkelwagen. Eerst CB105EXT18/25 als pilot, daarna de overige bevestigde families. Onbekende koppelingen krijgen geen optie.','',
 'Bestanden: book_mapping_review.json bevat alle huidige gematchte SKU’s, product-ID’s, handles, bronfragmenten en uitzonderingen. book_mapping_qa.png is een interne visuele broncontrole.']
if fresh_info:
 md+=['','## Actuele CB105-controle beschikbaar','','De aparte Admin-readback bevat42records:40afbouwartikelen en2inbouwdelen. Alle40afbouwartikelen hebben met_inbouwdeel=false. CB105EXT18/25 koppelt aan HBCB105, variant53187364356362 (€174,00); CB105TEXT18/25 koppelt aan HBCB105T, variant53187899162890 (€279,99). Beide doelvarianten zijn beschikbaar voor verkoop. Deze gegevens ondersteunen een exacte40artikelpilotallowlist; ze bewijzen nog geen gebouwde of geteste winkelwagenfunctie.','']
(ROOT/'book_mapping_review.md').write_text('\n'.join(md))
print(json.dumps(summary))
if not summary['all_table_pairs_found']:print('MISSING_TABLES',[(m['trim_model'],m['evidence']) for m in mappings if not all(e['table_pair_present']for e in m['evidence'])])
