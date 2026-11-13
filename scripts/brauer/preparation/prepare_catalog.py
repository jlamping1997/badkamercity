"""Prepare the complete BRAUER catalogue offline. This module contains no store writes."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict, Counter
import json,re,hashlib,unicodedata,csv,html,argparse
import openpyxl

VERSION='brauer-preparation-19'
PRICE='Adviesverkoopprijs ex. Btw'
CRITICAL={'EAN',PRICE,'Merk','Materiaal','Afwerking','Productomschrijving'}
METALS={'Chroom':'Chroom','Goud':'Geborsteld goud PVD','Koper':'Geborsteld koper PVD','Gunmetal':'Geborsteld gunmetal PVD','RVS-kleurig':'Geborsteld RVS-kleurig PVD','Zwart':'Mat zwart','Coffee':'Geborsteld coffee PVD'}
def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def clean(value):
 if value is None:return ''
 if isinstance(value,float) and value.is_integer():return str(int(value))
 return re.sub(r'\s+',' ',str(value)).strip()
def slug(value):return re.sub('[^a-z0-9]+','-',unicodedata.normalize('NFKD',value).encode('ascii','ignore').decode().lower()).strip('-')
def money(value):return Decimal(str(value)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
def gtin_valid(value):
 return value.isdigit() and len(value) in [8,12,13,14] and (10-sum(int(n)*(3 if i%2==0 else 1) for i,n in enumerate(value[-2::-1]))%10)%10==int(value[-1])
def colourless(title,colour):
 text=title.lower()
 # Supplier colour often contains two distinct values for metal and glass.
 c=colour.split(',')[0].strip().lower()
 patterns={
  'chroom':r'chroom','goud':r'(?:pvd\s+)?goud(?:\s+geborsteld)?','koper':r'(?:pvd\s+)?koper(?:\s+geborsteld)?',
  'gunmetal':r'(?:pvd\s+)?gunmetal(?:\s+geborsteld)?','rvs-kleurig':r'(?:pvd\s+)?rvs-kleurig(?:\s+geborsteld)?',
  'zwart':r'(?:mat\s+)?zwart','coffee':r'(?:pvd\s+)?coffee(?:\s+geborsteld)?'}
 if c in patterns:text=re.sub(r'\b'+patterns[c]+r'\b',' ',text)
 elif c:text=re.sub(r'\b'+re.escape(c)+r'\b',' ',text)
 return text
def prepare_fields(row,old):
 f=row['fields'];title=f['Productomschrijving'];low=title.lower();g=f['Productgroep'];typ=old.get('Producttypevoorstel',g);role='Product'
 if 'onderdeel' in low or g in ['Ladefronten','Deurfronten','Spiegeldeuren','Bodemplaten voor onderkasten','Los beslag','Beslagpakket','Deur 2-delig','Zijwand','Deur'] or g.startswith('Wand ') or (g.startswith('Deur ') and 'Nisdeur' not in g):role='Onderdeel'
 if low.startswith('lichtlijst'):typ='Lichtlijsten voor spiegelkasten';role='Onderdeel'
 if 'topbladbeugel' in low:typ='Topbladbeugels';role='Onderdeel'
 if 'handdoekbeugel' in low and row['sku']=='5-S-221':typ='Handdoekhouders'
 opts={'colour':f['Kleur'].split(',')[0].strip()};spec={k:v for k,v in [('Serie','Standaard' if f['Serie']=='Edition' else f['Serie']),('Materiaal',f['Materiaal']),('Kleur',opts['colour']),('Afwerking',f['Afwerking'])] if v}
 spec['Artikelrol']=role;sig=colourless(title,f['Kleur']);family_partitions={};axes={}
 if opts['colour']:axes['colour']={'label':'Kleur / decor','kind':'decor_sample' if 'Spiegelkasten' in g else 'product_first_image'}
 if role=='Product' and 'ondiep' in low:family_partitions['depth']='Ondiep'
 elif role=='Product' and ('onderkast' in low or 'topblad' in low):family_partitions['depth']='Standaard'
 if re.search(r'\b(?:carving|stripe|edition)\b',low) and 'kranen' in f['Hoofdcategorie'].lower():
  finish='Carving' if 'carving' in low else 'Stripe' if 'stripe' in low else 'Standaard'
  opts['finish']=finish;axes['finish']={'label':'Afwerking greep','kind':'finish_detail_photo','labels':{'Standaard':'Standaard · glad','Carving':'Carving · gekarteld','Stripe':'Stripe · gestreept'}}
  spec['Afwerking greep']={'Standaard':'Glad','Carving':'Gekarteld','Stripe':'Gestreept'}[finish]
  sig=re.sub(r'\b(?:edition|carving|stripe)\b',' ',sig)
  set_number=re.search(r'\bset\s+\d+\b',sig)
  # The rest of the complete supplier description defines set identity.
  if set_number:sig=sig[:set_number.start()]+sig[set_number.end():]
 cabinet=bool(re.search(r'\bonderkast\b',low)) and role=='Product'
 mirror='Spiegelkasten' in g and not low.startswith('lichtlijst')
 high='Hoge kasten' in g
 basin=g.startswith('Wastafels ') and role=='Product'
 furniture=cabinet or mirror or high or basin or 'topblad' in low or 'fonteinkast' in low or low.startswith('planchet')
 if furniture:
  m=re.search(r'\b(onderkast|spiegelkast|hoge kast|wastafel|topblad|fonteinkast|planchet)(?:\s+(?:ondiep|asymmetrisch|vrijhangend))?\s+(\d+)(?!\d)',sig)
  if m:
   n=m[2];key='height' if high else 'width';spec['Hoogtemaat bron' if high else 'Breedtemaat bron']=n
   if high:
    family_partitions['height']=n;typ='Halfhoge kasten' if n=='120' else 'Hoge kasten'
   else:
    opts[key]=n;axes[key]={'label':'Breedte','kind':'size'}
    end=m.end(2)
    if basin:
     suffix=re.match(r'-(\d+)\b',sig[end:]);bowls=re.search(r'(\d+)\s+spoelbak',sig)
     if suffix and bowls and suffix[1]==bowls[1]:end+=len(suffix[0])
    sig=sig[:m.start(2)]+' '+sig[end:]
  if cabinet:
   for pat,key,label in [(r'(\d+)\s+softclose\s+lades','drawers','Aantal lades'),(r'(\d+)\s+sifon\s*uitsparing(?:en)?','cutouts','Afvoerindeling')]:
    m=re.search(pat,sig)
    if m:opts[key]=m[1];spec[label]=m[1];axes[key]={'label':label,'kind':'conditional_if_multiple' if key=='cutouts' else 'buttons'};sig=sig[:m.start()]+' '+sig[m.end():]
  if mirror:
   m=re.search(r'(\d+)\s+(?:(links|rechts)draaiende\s+)?dubbelzijdige\s+spiegeldeur(?:en)?',sig)
   if m:
    spec['Aantal deuren']=m[1];spec['Dubbelzijdige spiegeldeuren']='Ja';opts['door']=m[2].capitalize() if m[2] else None
    axes['door']={'label':'Draairichting deur','kind':'buttons','show_only_if_multiple':True,'depends_on':['width','colour']};sig=sig[:m.start()]+' '+sig[m.end():]
  if high or 'fonteinkast' in low:
   if 'links- of rechtsdraaiend' in sig:spec['Draairichting deur']='Omkeerbaar';sig=sig.replace('links- of rechtsdraaiend',' ')
   else:
    m=re.search(r'\b(links|rechts)draaiend\b',sig)
    if m:opts['door']=m[1].capitalize();axes['door']={'label':'Draairichting deur','kind':'buttons'};spec['Draairichting deur']=opts['door'];sig=sig[:m.start()]+' '+sig[m.end():]
  if basin:
   m=re.search(r'(\d+)\s+kraangat(?:en)?',sig)
   if m:opts['tap_holes']=m[1];axes['tap_holes']={'label':'Aantal kraangaten','kind':'buttons'};spec['Aantal kraangaten']=m[1];sig=sig[:m.start()]+' '+sig[m.end():]
   m=re.search(r'(\d+)\s+spoelbak(?:ken)?(?:\s+(links|rechts))?',sig)
   if m:
    opts['bowls']=m[1];opts['bowl_position']=m[2].capitalize() if m[2] else ('Midden' if f['Serie']=='Aurora' else 'Standaard')
    axes['bowls']={'label':'Aantal spoelbakken','kind':'buttons'};axes['bowl_position']={'label':'Positie spoelbak','kind':'product_first_image'}
    spec['Aantal spoelbakken']=m[1];spec['Positie spoelbak']=opts['bowl_position'];sig=sig[:m.start()]+' '+sig[m.end():];sig=sig.replace('asymmetrisch',' ')
   if g=='Wastafels opbouw':spec['Montage']='Op een wastafelonderkast'
 if f['Hoofdcategorie'].lower().startswith('glas') or row['sku'].startswith(('GS-','GL-','GP-','GB-')):
  m=re.search(r'\b(\d+)x(\d+)(?:x(\d+))?\b',sig)
  if m:
   opts['width']=m[1];axes['width']={'label':'Breedtemaat','kind':'size'}
   if m[3]:opts['depth']=m[2];axes['depth']={'label':'Dieptemaat','kind':'size'};family_partitions['height']=m[3]
   else:family_partitions['height']=m[2]
   sig=sig[:m.start()]+' '+sig[m.end():]
  m=re.search(r'\b(helder ribbelglas|helder glas|brons glas)\b',sig)
  if m:opts['glazing']=m[1].capitalize();spec['Glas']=opts['glazing'];axes['glazing']={'label':'Glas','kind':'buttons'};sig=sig[:m.start()]+' '+sig[m.end():]
  m=re.search(r'met\s+(?:zijwand\s+(\d+)|(\d+)\s+zijwand)',sig)
  if m:opts['side']=(m[1] or m[2]);axes['side']={'label':'Zijwand','kind':'product_first_image'};spec['Zijwandmaat bron']=opts['side'];sig=sig[:m.start()]+' '+sig[m.end():]
  elif 'inloopdouche' in sig:opts['side']='Zonder zijwand';axes['side']={'label':'Opstelling','kind':'product_first_image'}
  m=re.search(r'met\s+draaideur\s+(\d+)\s+aan\s+(muur|glas)',sig)
  if m:spec['Deurbreedtemaat bron']=m[1];opts['hinge']='Scharnieren aan de '+('muur' if m[2]=='muur' else 'glaswand');axes['hinge']={'label':'Bevestiging deur','kind':'product_first_image'};sig=sig[:m.start()]+' '+sig[m.end():]
  if 'omkeerbaar' in low:spec['Montage']='Omkeerbaar: links of rechts';sig=sig.replace('omkeerbaar',' ')
 if 'wastafelkranen' in g.lower():
  if g=='Opbouw wastafelkranen':
   m=re.search(r'\b(lage|verhoogde|hoge)\b',sig)
   if m:opts['height_model']={'lage':'Laag','verhoogde':'Verhoogd','hoge':'Hoog'}[m[1]];axes['height_model']={'label':'Hoogtemodel','kind':'product_first_image'};spec['Hoogtemodel leverancier']=opts['height_model'];sig=sig[:m.start()]+' '+sig[m.end():]
   m=re.search(r'met\s+draaibare\s+(ronde|platte)\s+uitloop',sig)
   opts['outlet_shape']=m[1].capitalize() if m else None
   axes['outlet_shape']={'label':'Vorm uitloop','kind':'product_first_image','show_only_if_multiple':True,'depends_on':['height_model','colour','finish','handle']}
   if m:spec['Uitloop']='Draaibaar, '+m[1];sig=sig[:m.start()]+' '+sig[m.end():]
  m=re.search(r'\bmodel\s+([a-e](?:[12])?)\b',sig)
  if m:
   code=m[1].upper();opts['handle']=code;axes['handle']={'label':'Hendel' if len(code)==1 else 'Uitvoering','kind':'dedicated_handle_photo' if len(code)==1 and 'lage' in low else 'product_first_image'};spec['Model leverancier']=code;sig=sig[:m.start()]+' '+sig[m.end():]
   if g=='Opbouw wastafelkranen':axes['handle']={'label':'Hendel','kind':'handle_photo','dedicated_image_scope':{'height_model':'Laag'},'other_scope_image':'product_first_image'}
  for pat,key,label in [(r'(rechte|gebogen)\s+uitloop','spout','Uitloop'),(r'(rozetten|afdekplaat)','wall_finish','Wandafwerking')]:
   m=re.search(pat,sig)
   if m:opts[key]=m[1].capitalize();axes[key]={'label':label,'kind':'product_first_image'};sig=sig[:m.start()]+' '+sig[m.end():]
 if g in ['Opbouw fonteinkranen']:
  opts['spout']='Gebogen uitloop' if 'met gebogen uitloop' in sig else 'Standaard uitloop';axes['spout']={'label':'Uitloop','kind':'product_first_image'};sig=sig.replace('met gebogen uitloop',' ')
 if 'douchekranen' in g.lower() or 'badkranen' in g.lower():
  for pat,key,label in [(r'(\d+)\s*cm\s+douchekop','head_size','Hoofddouche'),(r'(rechte muurarm|gebogen muurarm|plafondarm)','arm','Bevestiging hoofddouche'),(r'(staaf\s*handdouche|3-standen handdouche)','handshower','Handdouche')]:
   m=re.search(pat,sig)
   if m:opts[key]=clean(m[1]);axes[key]={'label':label,'kind':'size' if key=='head_size' else 'product_first_image'};sig=sig[:m.start()]+' '+sig[m.end():]
  # Do not equate a hose-only set with a holder or slide-rail set.
 for phrase,label in [('excl. opbouwgrepen','Grepen'),('excl. opbouwgreep','Greep'),('excl. opleggrepen','Grepen'),('excl. opleggreep','Greep'),('excl. bodemplaat','Bodemplaat')]:
  if phrase in low:spec[label+' inbegrepen']='Nee'
 title_out='BRAUER '+re.sub(r'\bEdition\b','Standaard',title,flags=re.I)
 if high and family_partitions.get('height')=='120':title_out=re.sub(r'\bhoge kast\b','halfhoge kast',title_out,flags=re.I)
 sig=clean(sig)
 key={'type':typ,'supplier_group':g,'series':f['Serie'] if f['Serie']!='Edition' else 'BRAUER kranen','material':f['Materiaal'],'role':role,'fixed':family_partitions,'technical_remainder':sig}
 return typ,role,title_out,opts,spec,key,axes

def main(source_dir,out_dir):
 source_dir=Path(source_dir);out=Path(out_dir);out.mkdir(parents=True,exist_ok=True)
 observations=defaultdict(list);manifest=[]
 for path in sorted(source_dir.glob('Prijslijst BRAUER*.xlsx')):
  sheet=openpyxl.load_workbook(path,read_only=True,data_only=True).active;rows=sheet.iter_rows(values_only=True);headers=next(rows);count=0
  for n,row in enumerate(rows,2):
   if not row[0]:continue
   fields={k:clean(v) for k,v in zip(headers,row)}
   fields[PRICE]=str(money(fields[PRICE]));observations[fields['Artikelcode']].append({'source':path.name,'sheet':sheet.title,'row':n,'fields':fields});count+=1
  manifest.append({'name':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'rows':count})
 assert len(manifest)==3
 base_path=next(source_dir.glob('Brauer-productbasis*.xlsx'));sheet=openpyxl.load_workbook(base_path,read_only=True,data_only=True)['Productbasis'];rows=sheet.iter_rows(values_only=True);headers=next(rows);old={clean(row[0]):dict(zip(headers,row)) for row in rows if row[0]}
 assert set(old)==set(observations),'Input catalogue changed: investigate identity differences'
 products=[];families=defaultdict(list);conflicts=[]
 for sku,obs in sorted(observations.items()):
  obs.sort(key=lambda x:0 if 'kranenprogramma' in x['source'] else 1 if 'meubelprogramma' in x['source'] else 2)
  fields={};diffs={}
  for key in obs[0]['fields']:
   values=list(dict.fromkeys(o['fields'][key] for o in obs if o['fields'][key]))
   fields[key]=values[0] if values else ''
   if len(values)>1:diffs[key]=values
  critical={k:v for k,v in diffs.items() if k in CRITICAL}
  r={'sku':sku,'fields':fields};typ,role,title,options,spec,fkey,axes=prepare_fields(r,old[sku])
  issues=[]
  if critical:issues.append('BRONCONFLICT')
  if not gtin_valid(fields['EAN']):issues.append('EAN_CONTROLE')
  price=money(Decimal(fields[PRICE])*Decimal('1.21'))
  if money(old[sku]['Prijsbasis incl btw'])!=price:issues.append('PRIJS_VERSCHIL_VORIGE_BASIS')
  future='2027-02-01' if '2027' in fields['Levertijd'] and ('februari' in fields['Levertijd'].lower() or re.search(r'0?1[-./]0?2[-./]2027',fields['Levertijd'])) else None
  if '2027' in fields['Levertijd'] and not future:issues.append('LEVERDATUM_CONTROLEREN')
  p={'sku':sku,'ean':fields['EAN'],'vendor':'BRAUER','product_type':typ,'role':role,'title':title,'handle_proposal':slug(title+'-'+sku),'price_incl_vat':str(price),'advice_ex_vat':fields[PRICE],'vat_rate':'0.21','description':title.removeprefix('BRAUER ')+'.'+(' Dit is een los onderdeel.' if role=='Onderdeel' else ''),'specifications':spec,'options':options,'family_key':fkey,'axis_definitions':axes,'family_id':'BRAUER-'+digest(fkey)[:16].upper(),'data_issues':issues,'source_conflicts':critical,'source_category_differences':{k:v for k,v in diffs.items() if k not in CRITICAL},'source':fields,'source_refs':[{'file':o['source'],'sheet':o['sheet'],'row':o['row']} for o in obs],'future_available_date':future,'media':{'images':[],'pdfs':[],'status':'AWAITING_OFFICIAL_PACKAGE'},'user_additions':{k:old[sku].get(k) for k in ['Jouw aanvulling omschrijving','Jouw aanvulling techniek','Jouw afbeeldingen','Jouw PDF-documenten']},'import_allowed':False,'publications':[]}
  # Preserve manual work and the previous full source in the bundle.
  products.append(p);families[p['family_id']].append(p)
  for field,values in critical.items():conflicts.append({'sku':sku,'field':field,'values':values,'source_refs':p['source_refs']})
 # A selector must reach every article without silently changing a second choice.
 # Split disconnected option graphs into separate families rather than inventing combinations.
 graph_splits=[];connected={}
 for base,ps in families.items():
  defs={k:v for p in ps for k,v in p['axis_definitions'].items()}
  keys=[k for k,v in defs.items() if not v.get('show_only_if_multiple') and k!='cutouts']
  parent=list(range(len(ps)))
  def find(i):
   while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
   return i
  for omitted in keys or [None]:
   buckets={}
   for i,p in enumerate(ps):
    state=tuple((k,p['options'].get(k)) for k in keys if k!=omitted)
    if state in buckets:parent[find(i)]=find(buckets[state])
    else:buckets[state]=i
  parts=defaultdict(list)
  for i,p in enumerate(ps):parts[find(i)].append(p)
  if len(parts)>1:graph_splits.append({'original_family':base,'articles':len(ps),'separate_groups':len(parts)})
  for part in parts.values():
   id=base if len(parts)==1 else base+'-'+digest(sorted(p['sku'] for p in part))[:6].upper()
   for p in part:p['family_id']=id
   connected[id]=part
 families=connected
 groups=[];unresolved=[]
 for id,ps in sorted(families.items()):
  all_axes={k:v for p in ps for k,v in p['axis_definitions'].items()};group_axes=[]
  for key,definition in all_axes.items():
   values=sorted({p['options'].get(key) for p in ps if p['options'].get(key) is not None},key=lambda x:(len(str(x)),str(x)))
   if len(values)<2:continue
   d={'key':key,**definition,'values':values}
   if key=='colour':d['visible_limit']=6;d['expand_label']='Bekijk meer kleuren'
   if d['kind']=='size':d['kind']='buttons' if len(values)<=3 else 'select'
   if key=='cutouts':d['depends_on']=['width','drawers','colour'];d['show_only_if_multiple']=True;d['reset_on_change']=['width','drawers']
   group_axes.append(d)
  group_axes.sort(key=lambda a:a['key']!='colour')
  seen=defaultdict(list)
  for p in ps:seen[tuple((a['key'],p['options'].get(a['key'])) for a in group_axes)].append(p)
  ambiguous=[v for v in seen.values() if len(v)>1]
  if ambiguous:
   for same in ambiguous:
    unresolved.append({'family_id':id,'skus':[p['sku'] for p in same],'reason':'Identieke keuzewaarden voor verschillende artikelnummers. Geen willekeurige koppeling.'})
    for p in same:p['data_issues'].append('KEUZECOMBINATIE_NIET_UNIEK')
  status='CONTROLEREN' if ambiguous or any(p['source_conflicts'] for p in ps) else 'VOORBEREID'
  label='BRAUER '+('Standaard' if ps[0]['source']['Serie']=='Edition' else ps[0]['source']['Serie'])+' '+ps[0]['product_type']+' '+ps[0]['source']['Materiaal']
  group={'id':id,'name':clean(label),'technical_source_signature':ps[0]['family_key']['technical_remainder'],'product_type':ps[0]['product_type'],'role':ps[0]['role'],'fixed_partitions':ps[0]['family_key']['fixed'],'material':ps[0]['source']['Materiaal'],'axes':group_axes,'sku_count':len(ps),'skus':[p['sku'] for p in ps],'status':status,'combination_rule':'EXACT_CANDIDATE_ONLY_NO_SILENT_OTHER_CHANGES','missing_combination':'VISIBLE_DISABLED','image_rule':'FIRST_IMAGE_EXACT_LINKED_PRODUCT','same_as_compatibility':False}
  for p in ps:p['group_status']=status;p.pop('axis_definitions');p.pop('family_key')
  groups.append(group)
 identities=Counter(p['ean'] for p in products)
 duplicates=[{'ean':ean,'skus':[p['sku'] for p in products if p['ean']==ean]} for ean,n in identities.items() if n>1]
 for d in duplicates:
  for p in products:
   if p['sku'] in d['skus']:p['data_issues'].append('EAN_GEDEELD_DOOR_VERSCHILLENDE_SKUS')
 handles=Counter(p['handle_proposal'] for p in products);assert max(handles.values())==1
 summary={'version':VERSION,'source_files':manifest,'source_rows':sum(s['rows'] for s in manifest),'unique_skus':len(products),'families':len(groups),'families_prepared':sum(g['status']=='VOORBEREID' for g in groups),'families_to_review':sum(g['status']!='VOORBEREID' for g in groups),'critical_conflict_skus':len({x['sku'] for x in conflicts}),'critical_conflicts':len(conflicts),'future_skus':sum(bool(p['future_available_date']) for p in products),'data_issue_counts':dict(Counter(i for p in products for i in p['data_issues'])),'duplicate_eans':duplicates,'disconnected_families_split':graph_splits,'all_import_blocked':True,'importable_skus':0,'official_media_package_received':False,'existing_source_workbook':base_path.name,'source_workbook_sha256':hashlib.sha256(base_path.read_bytes()).hexdigest()}
 def write(name,value):(out/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
 write('catalog.json',products);write('families.json',groups);write('source-conflicts.json',conflicts);write('ambiguous-choices.json',unresolved);write('summary.json',summary)
 write('release-gate.json',{'version':VERSION,'official_package_received':False,'media_inventory_reviewed':False,'source_conflicts_resolved':False,'shopify_identity_and_handle_check_passed':False,'field_and_collection_mapping_rechecked':False,'unpublished_theme_integration_verified':False,'pilot_review_passed':False,'merchant_import_release':False,'catalog_sha256':hashlib.sha256((out/'catalog.json').read_bytes()).hexdigest(),'import_allowed':False})
 cols=['Artikelnummer','EAN','Producttype','Titel','Prijs incl btw','Keuzegroep','Keuzes','Groepstatus','Datapunten te controleren','Toekomstige datum','Afbeeldingen','PDFs','Import toegestaan','Jouw aanvulling omschrijving','Jouw aanvulling techniek','Jouw afbeeldingen','Jouw PDF-documenten']
 values=[[p['sku'],p['ean'],p['product_type'],p['title'],float(p['price_incl_vat']),p['family_id'],'; '.join({'colour':'Kleur','width':'Breedtemaat','drawers':'Lades','cutouts':'Afvoeruitsparingen','door':'Deurrichting','finish':'Greepafwerking','tap_holes':'Kraangaten','bowl_position':'Bakpositie','bowls':'Spoelbakken','glazing':'Glas','side':'Zijwand','hinge':'Scharnieren','handle':'Hendel','head_size':'Hoofddouche','arm':'Douchearm','handshower':'Handdouche','wall_finish':'Wandafwerking','spout':'Uitloop'}.get(k,k)+': '+v for k,v in p['options'].items() if v is not None),p['group_status'],', '.join(p['data_issues']),p['future_available_date'] or '',0,0,'NEE'] for p in products]
 for row,p in zip(values,products):row.extend(p['user_additions'].get(k) for k in cols[13:])
 with (out/'productvoorbereiding.csv').open('w',newline='',encoding='utf-8-sig') as file:w=csv.writer(file);w.writerow(cols);w.writerows(values)
 write('sheet-data.json',{'product_headers':cols,'product_rows':values,'family_headers':['Keuzegroep','Producttype','Naam','Artikelen','Status','Keuzemenu','Vaste eigenschappen'],'family_rows':[[g['id'],g['product_type'],g['name'],g['sku_count'],g['status'],'; '.join(a['label']+': '+', '.join(a['values']) for a in g['axes']),json.dumps(g['fixed_partitions'],ensure_ascii=False)] for g in groups],'issue_headers':['Artikelnummer','Probleem','Bronwaarden'],'issue_rows':[[x['sku'],x['field'],' / '.join(x['values'])] for x in conflicts]+[[sku,x['reason'],x['family_id']] for x in unresolved for sku in x['skus']]})
 print(json.dumps({k:v for k,v in summary.items() if k not in ['source_files','duplicate_eans']},ensure_ascii=False))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--source-dir',required=True);parser.add_argument('--output-dir',required=True);args=parser.parse_args();main(args.source_dir,args.output_dir)
