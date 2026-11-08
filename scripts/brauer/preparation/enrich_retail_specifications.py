"""Apply reviewed public retailer facts offline. Never copy identities, prices or media.

Primary evidence needs exact manufacturer SKU AND EAN AND brand. SKU-only pages
may corroborate or raise differences but never introduce a customer value.
"""
import json,re,hashlib
from pathlib import Path
from collections import defaultdict,Counter
from urllib.parse import urlparse
from build_specifications import key,essentials,DIMENSIONS,GROUPS,INCLUDED,TAPS,GLASS,CABINETS,ALIASES

def normalized(label,value):
 v=value.strip().lower().replace('–','-').replace('&','en')
 # Compare measurements as millimetres without discarding a range.
 m=re.fullmatch(r'(\d+(?:[.,]\d+)?)(?:\s*-\s*(\d+(?:[.,]\d+)?))?\s*(cm|mm)',v)
 if m:
  unit=10 if m[3]=='cm' else 1
  return tuple(round(float(x.replace(',','.'))*unit,6) for x in [m[1],m[2]] if x is not None)
 v=re.sub(r'\s+',' ',v)
 if label=='Montage':
  if v in {'wand','hangend','wandmontage'}:return 'wand'
  if v in {'links/rechts','links of rechts te monteren'}:return 'links/rechts'
 if label=='Draairichting deur' and v in {'links of rechts','links of rechts te monteren','links/rechts'}:return 'links/rechts'
 if label=='Aantal grepen':return {'eengreeps':'1','tweegreeps':'2'}.get(v,v)
 if label=='Type handdouche':return {'staaf handdouche':'staafmodel','staafhanddouche':'staafmodel'}.get(v,v)
 if label=='Uitvoering uitloop':return {'vast':'vast','vaste uitloop':'vast','niet draaibaar':'vast','draaibare uitloop':'draaibaar'}.get(v,v)
 if label=='Vorm':return {'rechthoek':'rechthoekig'}.get(v,v)
 if label=='Wandafwerking':return {'met achterplaat':'afdekplaat','met afdekplaat':'afdekplaat','met rozetten':'rozetten'}.get(v,v)
 if label=='Glas':return {'helder':'helder glas','brons':'brons glas','brons rook':'brons glas'}.get(v,v)
 if label=='Materiaal':return v.replace('roestvaststaal (rvs)','rvs').replace(' / ',' ').replace(',',' ')
 if label=='Deursysteem':return {'1 schuifdeur':'schuifdeur','1 draaideur':'draaideur'}.get(v,v)
 if label=='Verlichting' and ('verlichting' in v or 'led' in v):return 'ja'
 return v

def applicable(p,f):
 typ=p['product_type'];label=f['label'];s=p['source']['Productomschrijving'].lower()
 if label=='Hartafstand' and typ not in TAPS|{'Meubelgrepen','Spiegeldeurgrepen'}:return False,'Hartafstand niet zonder passende aansluit-/bevestigingscontext gebruiken'
 if label=='Diameter plug' and typ!='Afvoerpluggen':return False,'Plugdiameter hoort bij een afzonderlijke afvoerplug'
 if label=='Aansluitmaat sifon' and typ not in {'Afvoerpluggen','Sifons','Fonteinen','Meubelwastafels','Waskommen','Vrijhangende wastafels'}:return False,'Sifonaansluiting niet als wateraanvoer gebruiken'
 if label in {'Plaats bediening','Wandafwerking','Vorm rozet','Aantal rozetten','Bediening aan/uit'} and typ not in TAPS|{'Hoekstopkranen'}:return False,'Kraanbediening/-afwerking hoort niet bij dit producttype'
 if label in {'Vorm rozet','Aantal rozetten'} and normalized('Wandafwerking',p['specifications'].get('Wandafwerking',''))=='afdekplaat':return False,'Rozettenkenmerk niet als afdekplaatkenmerk gebruiken'
 if label in {'Handdouche inbegrepen','Doucheslang inbegrepen','Glijstang inbegrepen','Hoofddouche inbegrepen','Uitloop inbegrepen'} and typ not in TAPS|{'Handdouches en houders'}:return False,'Meegeleverd onderdeel niet bewezen als onderdeel van deze productsoort'
 if label in {'Breedte','Diepte','Hoogte','Dikte'} and typ in {'Inbouwdouchesets','Inbouwbadkranen','Opbouwbadkranen','Opbouwdouchekranen','Douchepanelen','Losse inbouwthermostaten'}:
  return False,'Afmeting kan een setonderdeel betreffen; niet als totale setmaat gebruiken'
 if label in {'Hoogte','Breedte','Diepte','Dikte'} and typ=='Inbouwwastafelkranen':return False,'Rozet/afdekplaat/onderdeelmaat niet als totale kraanmaat gebruiken'
 if label=='Thermostatisch' and typ not in TAPS:return False,'Niet relevant voor dit losse onderdeel'
 if label in {'Koudestartfunctie','Uittrekbare uitloop','Draaibare uitloop'} and typ not in {'Opbouwwastafelkranen','Inbouwwastafelkranen','Opbouwfonteinkranen','Inbouwfonteinkranen'}:return False,'Kenmerk hoort niet bij dit producttype'
 if label in {'Verlichting','Spiegelverwarming','Lichtschakelaar','Stopcontact'} and typ not in CABINETS|{'Spiegels'}:return False,'Niet relevant voor dit producttype'
 if label=='Aantal kraangaten' and typ not in {'Meubelwastafels','Waskommen','Fonteinen','Vrijhangende wastafels','Opbouwwastafelkranen','Inbouwwastafelkranen','Opbouwfonteinkranen','Inbouwfonteinkranen'}:return False,'Geen wastafel-/kraanopstelling'
 if label=='Aantal spoelbakken' and typ in CABINETS:return False,'Geen spoelbakkenaantal voor een losse kast'
 if label=='Aansluitmaat watertoevoer' and typ not in TAPS|{'Hoofddouches','Handdouches en houders','Douchearmen','Doucheslangen','Uitlopen','Hoekstopkranen'}:return False,'Aansluitsoort niet als wateraanvoer bewezen'
 if label=='Aansluitmaat doucheslang' and not (typ in {'Doucheslangen','Handdouches en houders','Opbouwbadkranen','Inbouwbadkranen','Opbouwdouchekranen','Inbouwdouchesets','Vrijstaande badkranen'}):return False,'Doucheslangaansluiting niet relevant'
 if label=='Diameter hoofddouche' and typ=='Hoofddouches':return False,'Zelfde maat staat al als Diameter'
 if label=='Diameter' and typ in TAPS:return False,'Diameter van een setonderdeel moet expliciet benoemd zijn'
 if label=='Lengte doucheslang':
  v=normalized(label,f['value'])
  if isinstance(v,tuple) and v and (v[0]<600 or v[0]>3000):return False,'Afwijkende doucheslanglengte; bevestigen met artikeltekening, niet automatisch corrigeren'
 if label=='Deursysteem' and typ not in GLASS:return False,'Deuren staan al als aantal en draairichting'
 if label=='Glascoating' and typ not in GLASS:return False,'Glascoating is geen kenmerk van keramiek/natuursteen'
 if label=='Dikte' and typ in {'Spiegels','Hoofddouches'}:return True,None
 return True,None

def collect(catalog,records,resolutions):
 by={p['sku']:p for p in catalog};candidates=defaultdict(lambda:defaultdict(list));rejected=[];scope=[]
 for r in records:
  host=urlparse(r['url']).hostname
  p=by.get(r['sku']);reason=None
  if host not in {'www.badkamerxxl.nl','www.sanitairwinkel.nl'}:reason='Bron buiten toegestane sites'
  elif not p:reason='Artikelnummer niet in catalogus'
  elif r.get('requested_sku') and r['requested_sku']!=r['sku']:reason='Opgevraagd artikelnummer wijkt af van aangetroffen artikelnummer'
  elif str(r.get('brand','')).lower()!='brauer':reason='Merk niet exact bevestigd'
  elif r.get('ean') and r['ean']!=p['ean']:reason='EAN wijkt af'
  if reason:rejected.append({'sku':r['sku'],'url':r['url'],'reason':reason});continue
  strong=r.get('ean')==p['ean']
  if not strong:rejected.append({'sku':r['sku'],'url':r['url'],'reason':'EAN ontbreekt; alleen aanvullende vergelijking, geen zelfstandige aanvulling'})
  for original in r['fields']:
   f=dict(original);ok,why=applicable(p,f)
   if not ok:scope.append({'sku':p['sku'],'label':f['label'],'source_value':f['value'],'reason':why,'url':r['url']});continue
   if f['label']=='Hoogte' and p['product_type'] in {'Opbouwwastafelkranen','Opbouwfonteinkranen'}:f['label']='Hoogte kraan'
   if f['label']=='Montage' and p['product_type'] in TAPS and f['value'].lower() in {'wand','op wand'}:f['label']='Bevestiging';f['value']='Wand'
   if f['label']=='Montage' and p['product_type'] in GLASS and f['value'].lower()=='muurprofiel':f['label']='Bevestiging glas'
   if f['label']=='Type handdouche' and f['value'].lower()=='rond model':f['label']='Vorm handdouche';f['value']='Rond'
   if f['label']=='Montage' and p['product_type'] in {'Waskommen','Meubelwastafels','Fonteinen','Vrijhangende wastafels'} and f['value'].lower()=='opbouw':f['label']='Montagetype'
   if p['product_type'] in GLASS and host=='www.sanitairwinkel.nl' and f['label'] in {'Breedte','Lengte'}:
    scope.append({'sku':p['sku'],'label':f['label'],'source_value':f['value'],'reason':'Mogelijk nominale glasmaat; niet als precieze glas-/stelmaat invullen zonder tekening','url':r['url']});continue
   f.update({'url':r['url'],'ref':r['ref'],'identity':'SKU_EAN_MERK' if strong else 'SKU_MERK_ONLY','ean':r.get('ean'),'checked_on':r['checked_on']})
   candidates[p['sku']][f['label']].append(f)
 return candidates,rejected,scope

def main():
 root=Path('prepared');catalog=json.loads((root/'catalog.json').read_text());evidence=json.loads((root/'specification-evidence.json').read_text());records=json.loads((root/'retail-observations.json').read_text());resolutions=json.loads((root/'retail-resolutions.json').read_text())
 previous_path=root/'retail-enrichment-report.json';previous=json.loads(previous_path.read_text()) if previous_path.exists() else {}
 previous_open={(x['sku'],x['field']):x for x in previous.get('differences',[]) if x['status']=='OPEN'}
 candidates,rejected,scope=collect(catalog,records,resolutions);changes=[];conflicts=[];unchanged=0
 for p in catalog:
  sku=p['sku'];flat=p['specifications'];held={ALIASES.get(x,x) for x in p.get('measurement_hold',{}).get('fields',[])}|set(p['source_conflicts']);review=[]
  # Retain previous run's additions on a repeated application; no duplicate rows.
  for label,values in candidates.get(sku,{}).items():
   primary=[v for v in values if v['identity']=='SKU_EAN_MERK']
   variants=defaultdict(list)
   for v in values:variants[str(normalized(label,v['value']))].append(v)
   base=flat.get(label);base_ev=evidence[sku]['facts'].get(label);base_key=str(normalized(label,base)) if base is not None else None
   primary_variants={str(normalized(label,v['value'])) for v in primary}
   resolution=resolutions.get(sku,{}).get(label)
   # SKU-only pages cannot introduce a fact, but counterevidence must still be reviewed.
   comparison=set(variants)
   if base is not None:comparison.add(base_key)
   historic=previous_open.get((sku,label),{}).get('existing')
   if historic is not None:comparison.add(str(normalized(label,historic)))
   if not primary:
    if len(variants)>1 or base is not None and any(k!=base_key for k in variants):
     conflicts.append({'sku':sku,'field':label,'status':'SECONDARY_SOURCE_DIFFERENCE','existing':base,'candidates':values,'action':'Geen zelfstandige wijziging zonder EAN'})
    continue
   chosen=primary[0];status='EXACT_ARTICLE_ONE_RETAILER'
   conflict=len(comparison)>1
   if label in held:
    conflicts.append({'sku':sku,'field':label,'status':'EXISTING_HOLD_RETAINED','existing':base,'candidates':values,'action':'Actuele leveranciersbevestiging nodig'});continue
   if resolution:
    target=normalized(label,resolution['value']);selected=[v for v in primary if normalized(label,v['value'])==target]
    assert selected,(sku,label,'Resolution must select an observed primary fact')
    chosen=selected[0];conflict=False
    if resolution.get('basis')=='SUPPLIER_AND_EXACT_RETAILER':
     assert base_ev and base_ev['kind']=='supplier' and base_key==str(target),(sku,label,'Supplier resolution requires the unchanged supplier fact')
     assert resolution.get('supplier_source_refs')==base_ev['source_refs'],(sku,label,'Supplier references must match')
     assert chosen['url']==resolution['corroborating_url'],(sku,label,'Corroboration must be exact SKU/EAN evidence')
     status='SUPPLIER_CORROBORATED';resolved='RESOLVED_SUPPLIER_CORROBORATED'
     action='Leveranciersgegeven behouden; exact artikel bij tweede winkel bevestigt dezelfde waarde; afwijkende winkelwaarde verworpen'
    else:
     status='LINKED_DRAWING_CHECKED';resolved='RESOLVED_LINKED_DRAWING'
     action='Gekozen tabelwaarde ondersteund door gekoppelde artikeltekening'
    conflicts.append({'sku':sku,'field':label,'status':resolved,'existing':base,'candidates':values,'resolution':resolution,'action':action})
   elif conflict:
    # More general material wording is not an alternative physical composition.
    if label=='Materiaal' and base:
     b=normalized(label,base).replace('-kunststof','').replace(',',' ').split()
     if all(set(normalized(label,v['value']).replace('-kunststof','').replace(',',' ').split()).issubset(set(b)) or set(b).issubset(set(normalized(label,v['value']).replace('-kunststof','').replace(',',' ').split())) for v in primary):unchanged+=1;continue
    item={'sku':sku,'field':label,'status':'OPEN','existing':base if base is not None else historic,'candidates':values,'action':'Betwiste externe waarde niet invullen; reeds externe waarde inhouden bij tegenspraak'}
    conflicts.append(item);review.append(label)
    if base_ev and base_ev['kind']!='supplier':
     flat.pop(label,None);evidence[sku]['facts'].pop(label,None);changes.append({'sku':sku,'field':label,'old':base,'new':'','action':'INGEHOUDEN_BIJ_BRONVERSCHIL','url':chosen['url'],'ref':chosen['ref']})
    continue
   if base is not None:
    unchanged+=1;continue
   flat[label]=chosen['value']
   evidence[sku]['facts'][label]={'kind':'retailer_exact_sku_ean','field':chosen['source_label'],'fragment':chosen['source_value'],'source_refs':[],
    'url':chosen['url'],'ref':chosen['ref'],'source_line':chosen.get('line'),'source_section':chosen.get('source_section'),'identity':{'sku':sku,'ean':p['ean'],'brand':'BRAUER'},
    'checked_on':chosen['checked_on'],'verification':status,'corroborating_urls':sorted({v['url'] for v in primary if normalized(label,v['value'])==normalized(label,chosen['value'])}),
    'drawing_resolution':resolution}
   changes.append({'sku':sku,'field':label,'old':'','new':chosen['value'],'action':'AANGEVULD','url':chosen['url'],'ref':chosen['ref']})
  if sku in candidates:p['retail_review']={'checked_on':max(v['checked_on'] for values in candidates[sku].values() for v in values),'open_fields':sorted(set(review)),'source_urls':sorted({v['url'] for values in candidates[sku].values() for v in values})}
  groups=[]
  for group in GROUPS:
   items=[]
   for label,value in flat.items():
    g='Algemeen' if label in {'Merk','Artikelnummer','EAN','Serie','Kleur','Materiaal','Afwerking','Coating','Productuitvoering'} else 'Afmetingen' if label in DIMENSIONS|{'Dikte','Diameter handdouche','Lengte glijstang'} else 'Meegeleverd' if label in INCLUDED|{'Douchebak inbegrepen','Bevestigingsmateriaal inbegrepen'} else 'Uitvoering'
    if g==group:items.append({'key':'fabrikantnummer' if label=='Artikelnummer' else key(label),'label':label,'value':value})
   if items:groups.append({'group':group,'items':items})
  p['customer_specifications']=groups
  missing=[x for x in essentials(p['product_type']) if x not in flat]
  p['specification_review']['missing_essential_fields']=missing;p['specification_review']['status']='AANVULLEN' if missing else 'BASIS_AANWEZIG'
 report=defaultdict(lambda:{'articles':0,'facts':0,'missing':Counter(),'complete_essential_articles':0})
 for p in catalog:
  r=report[p['product_type']];r['articles']+=1;r['facts']+=len(p['specifications']);r['missing'].update(p['specification_review']['missing_essential_fields']);r['complete_essential_articles']+=not p['specification_review']['missing_essential_fields']
 summary=json.loads((root/'specification-summary.json').read_text());summary['facts']=sum(len(p['specifications']) for p in catalog);summary['articles_needing_essential_details']=sum(bool(p['specification_review']['missing_essential_fields']) for p in catalog);summary['types']=[{'type':t,**r,'missing':dict(r['missing'])} for t,r in sorted(report.items())]
 selected={x['sku'] for x in json.loads((root/'specification-examples.json').read_text())};examples=[{'sku':p['sku'],'title':p['title'],'type':p['product_type'],'groups':p['customer_specifications'],'missing':p['specification_review']['missing_essential_fields']} for p in catalog if p['sku'] in selected]
 added_this_run=sum(x['action']=='AANGEVULD' for x in changes)
 withheld={(x['sku'],x['field'],x['action']):x for x in previous.get('changes',[]) if x['action']!='AANGEVULD'}
 withheld.update({(x['sku'],x['field'],x['action']):x for x in changes if x['action']!='AANGEVULD'})
 current_by={p['sku']:p for p in catalog}
 withheld={k:x for k,x in withheld.items() if x['field'] not in current_by[x['sku']]['specifications']}
 # Current evidence owns the cumulative ledger; repeat runs must not erase it.
 cumulative=[]
 for p in catalog:
  for label,e in evidence[p['sku']]['facts'].items():
   if e['kind']=='retailer_exact_sku_ean':cumulative.append({'sku':p['sku'],'field':label,'old':'','new':p['specifications'][label],'action':'AANGEVULD','url':e['url'],'ref':e['ref']})
 changes=cumulative+list(withheld.values())
 audit={'checked_on':max(r['checked_on'] for r in records),'fields_added_this_run':added_this_run,'source_pages':len(records),'unique_source_skus':len({r['sku'] for r in records}),'exact_sku_ean_pages':sum(r.get('ean')==next((p['ean'] for p in catalog if p['sku']==r['sku']),None) and r.get('ean') is not None for r in records),
 'articles_with_additions':len({x['sku'] for x in changes if x['action']=='AANGEVULD'}),'new_fields':sum(x['action']=='AANGEVULD' for x in changes),'withheld_previous_external_fields':sum(x['action']!='AANGEVULD' for x in changes),
 'open_field_conflicts':sum(x['status']=='OPEN' for x in conflicts),'open_conflict_articles':len({x['sku'] for x in conflicts if x['status']=='OPEN'}),'changes':changes,'differences':conflicts,'identity_notes':rejected,'scope_rejections':scope,'import_allowed':False,'all_catalogue_scraped':False,'direct_http':'Not attempted in this resumption; approved anonymous public content fetches used. Prior 403 note retained in historical reports; no bypass.'}
 audit['live_public_pages']=sum(r.get('retrieval')=='public_live_fetch_html' for r in records)
 audit['unusual_hose_values_withheld']=sum(x['reason'].startswith('Afwijkende') for x in scope)
 inventory_path=root/'retail-product-url-inventory.json'
 if inventory_path.exists():
  inv=json.loads(inventory_path.read_text());audit['listing_pages']=inv['listing_pages'];audit['candidate_urls']=len(inv['product_urls']);audit['code_suffix_candidates']=len(inv['exact_code_suffix_candidates'])
 rows=[]
 for p in catalog:
  flat=p['specifications'];customer='\n'.join(f"{i['label']}: {i['value']}" for g in p['customer_specifications'] for i in g['items'] if i['label'] not in {'Merk','Artikelnummer','EAN'})
  rows.append([p['sku'],p['ean'],p['product_type'],p['title'],len(flat),flat.get('Breedte',''),flat.get('Diepte',''),flat.get('Hoogte',''),flat.get('Hoogte kraan',''),flat.get('Lengte uitloop',''),customer,'; '.join(p['specification_review']['missing_essential_fields']),'; '.join(p['data_issues']),p['source_refs'][0]['file'],p.get('previous_exact_sku_verification',{}).get('url','')])
 (root/'specification-sheet-data.json').write_text(json.dumps({'rows':rows},ensure_ascii=False,indent=2)+'\n')
 for name,obj in [('catalog.json',catalog),('specification-evidence.json',evidence),('specification-summary.json',summary),('specification-examples.json',examples),('retail-enrichment-report.json',audit)]: (root/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 gate=json.loads((root/'release-gate.json').read_text());gate['catalog_sha256']=hashlib.sha256((root/'catalog.json').read_bytes()).hexdigest();gate['retail_specifications_reviewed']=False;(root/'release-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
 print(json.dumps({k:v for k,v in audit.items() if k not in {'changes','differences','identity_notes','scope_rejections'}},ensure_ascii=False))
if __name__=='__main__':main()
