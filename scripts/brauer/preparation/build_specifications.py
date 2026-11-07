"""Offline customer specifications. No network, Shopify writes or inferred dimensions.

Every displayed fact carries evidence; unknown is not false. Run after
prepare_catalog.py and restore_verified_details.py, before preflight.
"""
import json, re, hashlib, unicodedata
from pathlib import Path
from collections import Counter, defaultdict

GROUPS = ['Algemeen', 'Afmetingen', 'Uitvoering', 'Meegeleverd']
PARTS = {'Ladefronten','Deurfronten','Binnenlades','Spiegeldeuren','Lichtlijsten voor spiegelkasten',
 'Bodemplaten','Meubelonderdelen','Toiletonderdelen','Losse glasdelen','Setgebonden glasdelen',
 'Glasbeslag','Glasbeslagpakketten','Spiegeldeurgrepen','Meubelgrepen','Topbladbeugels'}
GLASS = {'Inloopdouches','Nisdeuren','Douchecabines','Badwanden','Losse glasdelen','Setgebonden glasdelen'}
CABINETS = {'Onderkasten','Fonteinkasten','Halfhoge kasten','Hoge kasten','Bijkasten','Spiegelkasten'}
BASINS = {'Meubelwastafels','Waskommen','Fonteinen','Vrijhangende wastafels'}
TAPS = {'Opbouwwastafelkranen','Inbouwwastafelkranen','Opbouwfonteinkranen','Inbouwfonteinkranen',
 'Opbouwbadkranen','Inbouwbadkranen','Vrijstaande badkranen','Opbouwdouchekranen','Inbouwdouchesets','Losse inbouwthermostaten','Douchepanelen'}

def key(label):
 return re.sub(r'[^a-z0-9]+','_',unicodedata.normalize('NFKD',label).encode('ascii','ignore').decode().lower()).strip('_')

ALIASES = {'Aantal laden':'Aantal lades','Afwerking wand':'Wandafwerking','Diepte uitloop':'Lengte uitloop',
 'Model':'Hoogtemodel','Montagewijze':'Montage','Glassoort':'Glas','Met inbouwdeel':'Inbouwdeel inbegrepen',
 'Met plug':'Afvoerplug inbegrepen','Met sifon':'Sifon inbegrepen','Met wastafel/blad':'Wastafel of blad inbegrepen',
 'Met koude start':'Koudestartfunctie','Brauer ColdStart':'Koudestartfunctie','Met softclose':'Softclose',
 'Aantal waskommen':'Aantal spoelbakken','Uitvoering handgrepen':'Greepuitvoering','Antikalkbehandeling':'Glascoating','Met verlichting':'Verlichting','Warm/koud aansluiting':'Watertoevoer',
 'Maat aansluiting aanvoer':'Aansluitmaat watertoevoer','Met douchegarnituur':'Douchegarnituur inbegrepen',
 'Met handdoekhouder':'Handdoekhouder inbegrepen','Met stabilisatiestang':'Stabilisatiestang inbegrepen',
 'Met zijwand(en)':'Zijwand inbegrepen','Met uitloop':'Uitloop inbegrepen'}
SKIP_AUDIT = {'Artikelnummer','Fabrikantnummer','EAN','Merk','Serie','Kleur','Kleurgroep','Kleur profiel/bevestiging',
 'Kleur kast','Kleur corpus','Glansgraad','Materiaal','Materiaal kraan','Materiaal onderkast','Vormgeving / stijlgroep',
 'Type hendel','Vorm uitloop','Breedtemaat','Dieptemaat','Belgaqua keurmerk','Materiaal afbouwdeel'}
DIMENSIONS = {'Breedte','Diepte','Hoogte','Hoogte kraan','Hoogte uitloop','Lengte uitloop','Inbouwdiepte',
 'Glasdikte','Lengte stabilisatiestang','Breedte zijwand','Verstelbaarheid breedte','Diameter','Lengte', 'Lengte douchearm','Diameter hoofddouche','Maat hoofddouche','Lengte doucheslang'}
INCLUDED = {'Inbouwdeel inbegrepen','Afvoerplug inbegrepen','Sifon inbegrepen','Wastafel of blad inbegrepen',
 'Douchegarnituur inbegrepen','Handdoekhouder inbegrepen','Stabilisatiestang inbegrepen','Zijwand inbegrepen',
 'Uitloop inbegrepen','Doucheslang inbegrepen','Handdouche inbegrepen','Wandaansluitbocht inbegrepen',
 'Glijstang inbegrepen','Grepen inbegrepen','Bodemplaat inbegrepen','Ophanging inbegrepen','Toiletzitting inbegrepen','Aansluitslang inbegrepen','Afbouwdeel inbegrepen'}

def essentials(typ):
 """Required for a useful listing, not a fabricated quality percentage."""
 if typ in CABINETS:
  return ['Breedte','Diepte','Hoogte','Materiaal'] + (['Aantal lades','Aantal sifonuitsparingen','Softclose'] if typ=='Onderkasten' else ['Aantal deuren','Verlichting'] if typ=='Spiegelkasten' else [])
 if typ in BASINS:return ['Breedte','Diepte','Hoogte','Materiaal','Aantal kraangaten']
 if typ in GLASS:return ['Breedte','Hoogte','Glasdikte','Glas'] + (['Deursysteem','Verstelbaarheid breedte'] if typ in {'Nisdeuren','Douchecabines'} else [])
 if typ in {'Inbouwwastafelkranen','Inbouwfonteinkranen'}:return ['Lengte uitloop','Inbouwdiepte','Inbouwdeel inbegrepen','Wandafwerking','Plaats bediening']
 if typ in {'Opbouwwastafelkranen','Opbouwfonteinkranen'}:return ['Hoogte kraan','Hoogte uitloop','Lengte uitloop','Watertoevoer','Aansluitmaat watertoevoer']
 if typ in TAPS:return ['Thermostatisch','Inbouwdeel inbegrepen','Aansluitmaat watertoevoer'] if typ.startswith('Inbouw') or typ=='Losse inbouwthermostaten' else ['Thermostatisch','Aansluitmaat watertoevoer']
 if typ in {'Spiegels','Topbladen','Douchebakken','Planchetten','Inbouwnissen','Opbouwnissen'}:return ['Breedte','Diepte','Hoogte'] if typ!='Spiegels' else ['Breedte','Hoogte','Verlichting']
 if typ=='Hoofddouches':return ['Diameter','Aansluitmaat watertoevoer']
 if typ in {'Doucheslangen','Douchearmen','Meubelgrepen','Spiegeldeurgrepen','Handdoekrekken','Handdoekradiatoren','Douchegoten'}:return ['Lengte','Aansluitmaat watertoevoer'] if typ in {'Doucheslangen','Douchearmen'} else ['Breedte','Hoogte']
 if typ in PARTS:return ['Geschikt voor']
 return ['Materiaal','Afmetingen']

def build(p, audit):
 s=p['source']; text=s['Productomschrijving']; low=text.lower(); typ=p['product_type']; opt=p['options']; facts={}; evidence={}; internal=[]
 def add(label,value,field='Productomschrijving',fragment=None,kind='supplier',url=None,overwrite=False):
  if value is None or value=='':return
  if label in facts and not overwrite:return
  if isinstance(value,bool):value='Ja' if value else 'Nee'
  if isinstance(value,int):value=str(value)
  group='Afmetingen' if label in DIMENSIONS else 'Meegeleverd' if label in INCLUDED else 'Algemeen' if label in {'Merk','Artikelnummer','EAN','Serie','Kleur','Materiaal','Afwerking','Coating','Productuitvoering'} else 'Uitvoering'
  facts[label]={'key':'fabrikantnummer' if label=='Artikelnummer' else key(label),'label':label,'value':str(value),'group':group}
  evidence[label]={'kind':kind,'field':field,'fragment':str(fragment if fragment is not None else s.get(field,value)),'source_refs':p['source_refs'] if kind=='supplier' else [],'url':url}
 def match(pattern,label,value=None,flags=re.I):
  m=re.search(pattern,text,flags)
  if m:add(label,value if value is not None else m.group(1),fragment=m.group(0))
  return m
 add('Merk','BRAUER','Merk');add('Artikelnummer',p['sku'],'Artikelcode');add('EAN',p['ean'],'EAN')
 if s['Serie']:add('Serie','Standaard' if s['Serie']=='Edition' else s['Serie'],'Serie')
 if opt.get('colour'):add('Kleur',opt['colour'],'Kleur')
 if s['Materiaal'] and 'Materiaal' not in p['source_conflicts']:
  add('Materiaal',re.sub(r'RVS\s*(\d+)',r'RVS \1',s['Materiaal']).replace(',', ' / '),'Materiaal')
 if s['Afwerking'] and 'Afwerking' not in p['source_conflicts']:add('Afwerking',s['Afwerking'],'Afwerking')
 match(r'\bPVD\b','Coating','PVD')
 if typ in PARTS:add('Productuitvoering','Onderdeel',fragment=text)
 if typ=='Meubelwastafels':add('Toepassing','Wastafel voor onderkast',field='Productcategorie',fragment=s['Productcategorie'])
 if typ in TAPS:
  if re.search(r'\bcarving\b',low):add('Afwerking greep','Carving – gekarteld',fragment='Carving')
  elif re.search(r'\bstripe\b',low):add('Afwerking greep','Stripe – gestreept',fragment='Stripe')
  elif re.search(r'\bedition\b',low):add('Afwerking greep','Standaard – glad',fragment='Edition')
  match(r'\b(lage|verhoogde|middelhoge|hoge) opbouw','Hoogtemodel',opt.get('height_model'))
  if 'inbouw' in low:add('Montage','Inbouw',fragment='inbouw')
  elif 'opbouw' in low:add('Montage','Opbouw',fragment='opbouw')
  elif 'vrijstaande' in low:add('Montage','Vrijstaand',fragment='Vrijstaande')
  if 'thermosta' in low:add('Thermostatisch',True,fragment=re.search(r'thermosta\w+',text,re.I).group(0))
  if 'mengkraan' in low:add('Watertoevoer','Warm en koud water',fragment=re.search(r'\w*mengkraan',text,re.I).group(0))
  match(r'(gebogen|rechte?) uitloop','Uitloop', 'Gebogen' if 'gebogen uitloop' in low else 'Recht')
  match(r'\bdraaibare (?:ronde )?uitloop\b','Uitvoering uitloop','Draaibaar')
  match(r'\bronde uitloop\b','Vorm uitloop','Rond')
  match(r'\b(met )?rozetten\b','Wandafwerking','Rozetten')
  match(r'\bafdekplaat\b','Wandafwerking','Afdekplaat')
  match(r'\binkortbaar\b','Inkortbaar',True)
  match(r'\b(\d+)-weg\b','Aantal standen omstelling')
  match(r'\b(\d+) stopkranen\b','Aantal stopkranen')
  if re.search(r'\bmet in- en afbouwdelen|\binclusief in- en afbouwdelen',low):
   add('Inbouwdeel inbegrepen',True);add('Afbouwdeel inbegrepen',True)
  elif 'met inbouwdeel' in low:add('Inbouwdeel inbegrepen',True,fragment='met inbouwdeel')
  match(r'(\d+(?:[.,]\d+)?)\s*cm douchekop','Maat hoofddouche', None)
  if 'Maat hoofddouche' in facts:facts['Maat hoofddouche']['value']+=' cm'
  match(r'\b(rechte muurarm|gebogen muurarm|plafondarm)\b','Bevestiging hoofddouche')
  match(r'\b(\d+)-standen (?:wandmodel douchekop|inbouw plafond douche)','Aantal straalstanden hoofddouche')
 for pattern,label in [(r'\bstaaf handdouche\b','Type handdouche'),(r'\b[23]-standen handdouche\b','Type handdouche')]:
  m=re.search(pattern,text,re.I)
  if m:add(label,m.group(0).capitalize(),fragment=m.group(0))
 if typ in TAPS:
  for word,label in [('handdouche','Handdouche inbegrepen'),('doucheslang','Doucheslang inbegrepen'),('wandaansluitbocht','Wandaansluitbocht inbegrepen'),('glijstang','Glijstang inbegrepen')]:
   if re.search(r'\b'+word+r'\b',low):add(label,True,fragment=word)
 if typ in CABINETS or typ in {'Binnenlades','Meubelwastafels','Fonteinen','Vrijhangende wastafels','Waskommen'}:
  for pattern,label in [(r'\b(\d+) (?:softclose )?lades?\b','Aantal lades'),(r'\b(\d+) (?:dubbelzijdige |enkelzijdige |linksdraaiende |rechtsdraaiende )*(?:spiegel)?deur(?:en)?\b','Aantal deuren'),(r'\b(\d+) sifon\s*uitsparing(?:en)?\b','Aantal sifonuitsparingen'),(r'\b(\d+) spoelbak(?:ken)?\b','Aantal spoelbakken'),(r'\b(\d+) kraangat(?:en)?\b','Aantal kraangaten')]:match(pattern,label)
  match(r'\bsoftclose\b','Softclose',True)
  match(r'\bgreeploos\b','Greepuitvoering','Greeploos')
  if 'links- of rechtsdraaiend' in low:add('Draairichting deur','Links of rechts te monteren',fragment='links- of rechtsdraaiend')
  else:
   match(r'\blinksdraaiend','Draairichting deur','Links');match(r'\brechtsdraaiend','Draairichting deur','Rechts')
  match(r'\bdubbelzijdige spiegeldeur(?:en)?\b','Spiegeldeuren','Aan beide zijden een spiegel')
  match(r'\benkelzijdige spiegeldeur(?:en)?\b','Spiegeldeuren','Aan één zijde een spiegel')
  match(r'\bspoelbak (links|rechts)\b','Positie spoelbak')
  for pattern,label in [(r'\bexcl\. (?:opleg)?grepen\b','Grepen inbegrepen'),(r'\bexcl\. greep\b','Grepen inbegrepen'),(r'\bexcl\. bodemplaat\b','Bodemplaat inbegrepen')]:match(pattern,label,False)
 if typ in CABINETS|{'Spiegels'}:
  if 'zonder verlichting' in low:add('Verlichting',False,fragment='zonder verlichting')
  elif 'interne en externe verlichting' in low:add('Verlichting','Binnen- en buitenverlichting',fragment='interne en externe verlichting')
  elif 'indirecte' in low and 'verlichting' in low:add('Verlichting','Indirecte LED-verlichting',fragment=text)
  elif 'directe' in low and 'verlichting' in low:add('Verlichting','Directe verlichting'+(' (LED)' if 'led' in low else ''),fragment=text)
  elif 'verlichting' in low:add('Verlichting',True,fragment=text)
  match(r'\bdimfunctie\b','Dimbaar',True);match(r'\btouch-bediening\b','Bediening verlichting','Touchbediening')
 if typ in GLASS:
  match(r'\b(helder|brons|rook|mat) glas\b','Glas',opt.get('glazing') or None)
  match(r'\bincl\. glascoating\b','Glascoating',True)
  match(r'\bomkeerbaar\b','Montage','Links of rechts te monteren')
  if re.search(r'\bschuifdeur\b',low):add('Deursysteem','Schuifdeur',fragment='schuifdeur')
  elif re.search(r'\bdraaiend\b',low):add('Deursysteem','Draaideur',fragment='draaiend')
  match(r'\b(enkelzijdige|tweezijdige) uitsparingen\b','Uitsparingen in glas')
  match(r'\bzonder uitsparingen\b','Uitsparingen in glas','Geen')
  match(r'\bgeschikt voor tweepuntsgreep\b','Geschikt voor','Tweepuntsgreep')
  # No physical dimensions or tolerances from nominal, unitless model numbers.
 if typ not in PARTS:
  match(r'\bincl\. (?:blinde ophanging|verborgen ophangbeugels)\b','Ophanging inbegrepen',True)
  match(r'\bgeïntegreerde ophangbeugel\b','Ophanging inbegrepen',True)
 if typ in {'Topbladen','Vrijhangende wastafels','Fonteinen'}:match(r'\bvrijhangend\b','Montage','Vrijhangend aan de wand')
 if typ in BASINS|{'Spiegels'}:
  match(r'\b(rechthoekig|rond|ovaal)\b','Vorm')
 if typ in {'Douchebakken'}:
  match(r'\bantislip\b','Antislip',True);match(r'\bantibacterieel\b','Antibacterieel',True)
 if typ=='Afvoerpluggen':
  match(r'\bklikwaste\b','Bediening','Kliksluiting');match(r'\baltijd open waste\b','Bediening','Altijd open')
 if typ=='Handdouches en houders':
  match(r'\b(\d+)-Standen handdouche\b','Aantal straalstanden')
  match(r'\bstaaf handdouche\b','Type handdouche','Staafhanddouche')
 if typ=='Doucheslangen':
  match(r'\bglad\b','Slanguitvoering','Glad');match(r'\bgevlochten\b','Slanguitvoering','Gevlochten')
 if typ=='Douchearmen':
  match(r'\bmuurarm\b','Montage','Wand');match(r'\bplafondarm\b','Montage','Plafond')
 if typ=='Prullenbakken':
  match(r'\b(\d+)L\b','Inhoud');
  if 'Inhoud' in facts:facts['Inhoud']['value']+=' liter'
 if typ=='Onderhoudsmiddelen':
  match(r'\b(\d+) ml\b','Inhoud');
  if 'Inhoud' in facts:facts['Inhoud']['value']+=' ml'
 if typ=='Hangtoiletten':match(r'\bincl\. bril\b','Toiletzitting inbegrepen',True)
 if typ=='Hoekstopkranen':match(r'\bmet slang\b','Aansluitslang inbegrepen',True)
 if typ in PARTS|{'Bedieningsplaten','Afvoerroosters','Toiletzittingen','Douchebaksifons'}:
  m=re.search(r'\btbv\s+(.+?)(?:\s+PVD\b|\s+chroom\b|$)',text,re.I)
  if m:add('Geschikt voor',m.group(1),fragment=m.group(0))
  if typ=='Setgebonden glasdelen':add('Productuitvoering','Setgebonden glasdeel',fragment=text,overwrite=True)
 # Only lengths whose units are explicit in the supplier text.
 m=re.search(r'\b(\d+(?:[.,]\d+)?)\s*x\s*(\d+(?:[.,]\d+)?)\s*mm\b',text,re.I)
 if m:
  add('Breedte',m.group(1)+' mm',fragment=m.group(0));add('Hoogte',m.group(2)+' mm',fragment=m.group(0))
 elif typ in {'Doucheslangen','Douchearmen','Meubelgrepen','Spiegeldeurgrepen'}:
  match(r'\b(\d+(?:[.,]\d+)?)\s*mm\b','Lengte')
  if 'Lengte' in facts:facts['Lengte']['value']+=' mm'
 # Exact previous identity audit, never propagated to colour siblings.
 r=audit.get(p['sku'])
 if r:
  assert r['ean']==p['ean']
  for label,value in r['fields'].items():
   if label in SKIP_AUDIT or value is None or value=='':continue
   target=ALIASES.get(label,label)
   if label in p.get('measurement_hold',{}).get('fields',[]):continue
   if label in {'Uitvoering','Afwerking greep','Montagewijze','Antikalkbehandeling'} and target in facts:continue
   # Nominal dealer filters and physical measurements must remain distinct.
   if isinstance(value,str):
    value=re.sub(r'(?<=\d)(mm|cm)\b',r' \1',value)
    value={'Warm & koud water':'Warm en koud water','Met rozetten':'Rozetten','Met afdekplaat':'Afdekplaat'}.get(value,value)
   add(target,value,field=label,fragment=str(r['fields'][label]),kind='previous_exact_sku_audit',url=r.get('url'),overwrite=True)
 # Holds always override an older exact audit, including aliases.
 for label in p.get('measurement_hold',{}).get('fields',[]):
  target=ALIASES.get(label,label);facts.pop(target,None);evidence.pop(target,None)
 for field in p['source_conflicts']:
  facts.pop(field,None);evidence.pop(field,None)
 # Unproven numeric model classes remain internal and never become cm values.
 for field in ['width','depth','side','height_model']:
  if opt.get(field) and re.search(r'\d',str(opt[field])):internal.append({'field':field,'source_class':opt[field],'reason':'Nominale modelmaat; geen bewezen fysieke afmeting'})
 ordered=[{'group':group,'items':[{k:v for k,v in f.items() if k!='group'} for f in facts.values() if f['group']==group]} for group in GROUPS]
 ordered=[g for g in ordered if g['items']]
 missing=[f for f in essentials(typ) if f not in facts]
 return ordered,evidence,missing,internal

def main():
 root=Path('prepared');catalog=json.loads((root/'catalog.json').read_text());old=json.loads(Path('recovered/previous-verified-audit.json').read_text())
 audit={sku:{'ean':r['ean'],'url':r['source_url'],'fields':r['specs']} for sku,r in old['visual']['source_records'].items()};audit.update(old['audit']['exact_source_records'])
 provenance={}; rows=[]; report=defaultdict(lambda:{'articles':0,'facts':0,'missing':Counter(),'complete_essential_articles':0});examples=[]
 chosen=['5-CE-001','5-CE-083-S2-65','5-GG-024','OK-JY120-4CH','SK-IM60LCH','WT-AU1000LHW','GS-GTC1H12090200CE','GS-OBI2B9030200CE','HK-AD120LCH','SP-GA100RH','5-CE-012','5-GG-264']
 for p in catalog:
  groups,evidence,missing,internal=build(p,audit);flat={i['label']:i['value'] for g in groups for i in g['items']}
  p['specifications']=flat;p['customer_specifications']=groups
  p['specification_review']={'missing_essential_fields':missing,'internal_nominal_values':internal,'status':'AANVULLEN' if missing else 'BASIS_AANWEZIG','exact_sku_audit_retained':p['sku'] in audit}
  provenance[p['sku']]={'ean':p['ean'],'facts':evidence}
  typ=p['product_type'];r=report[typ];r['articles']+=1;r['facts']+=len(flat);r['missing'].update(missing);r['complete_essential_articles']+=not missing
  customer='\n'.join(f"{i['label']}: {i['value']}" for g in groups for i in g['items'] if i['label'] not in {'Merk','Artikelnummer','EAN'})
  rows.append([p['sku'],p['ean'],typ,p['title'],len(flat),flat.get('Breedte',''),flat.get('Diepte',''),flat.get('Hoogte',''),flat.get('Hoogte kraan',''),flat.get('Lengte uitloop',''),customer,'; '.join(missing),'; '.join(p['data_issues']),p['source_refs'][0]['file'],p['previous_exact_sku_verification']['url'] if p.get('previous_exact_sku_verification') else ''])
  if p['sku'] in chosen:examples.append({'sku':p['sku'],'title':p['title'],'type':typ,'groups':groups,'missing':missing})
 bytype=[{'type':typ,**r,'missing':dict(r['missing'])} for typ,r in sorted(report.items())]
 summary={'articles':len(catalog),'product_types':len(report),'facts':sum(r['facts'] for r in report.values()),'articles_needing_essential_details':sum(bool(p['specification_review']['missing_essential_fields']) for p in catalog),'previous_exact_sku_audits':len(audit),'physical_dimensions_never_inferred_from_nominal':True,'shopify_writes':0,'import_allowed':False,'types':bytype}
 for name,obj in [('catalog.json',catalog),('specification-evidence.json',provenance),('specification-summary.json',summary),('specification-examples.json',examples),('specification-sheet-data.json',{'rows':rows})]:
  (root/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 gate=json.loads((root/'release-gate.json').read_text());gate['catalog_sha256']=hashlib.sha256((root/'catalog.json').read_bytes()).hexdigest();(root/'release-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
 print(json.dumps({k:v for k,v in summary.items() if k!='types'},ensure_ascii=False))

if __name__=='__main__':main()
