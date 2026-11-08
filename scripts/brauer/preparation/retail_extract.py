"""Parse public specification-table excerpts, not SEO text or missing boolean icons."""
import json,re,hashlib
from pathlib import Path

LENGTHS={'Breedte':'Breedte','Breedte/diameter':'Breedte','Diepte':'Diepte','Hoogte':'Hoogte','Hoogte (excl. verlichting)':'Hoogte',
 'Hartafstand':'Hartafstand','Diameter plug':'Diameter plug',
 'Hoogte kraan':'Hoogte kraan','Hoogte uitloop':'Hoogte uitloop','Diepte uitloop':'Lengte uitloop','Voorsprong uitloop':'Lengte uitloop',
 'Inbouwdiepte':'Inbouwdiepte','Glasdikte':'Glasdikte','Dikte glas':'Glasdikte','Lengte':'Lengte','Dikte':'Dikte',
 'Lengte douchearm':'Lengte douchearm','Lengte doucheslang':'Lengte doucheslang','Diameter':'Diameter','Diameter hoofddouche':'Diameter hoofddouche',
 'Verstelbaarheid breedte':'Verstelbaarheid breedte','Lengte stabilisatiestang':'Lengte stabilisatiestang','Breedte/diameter douchekop':'Diameter',
 'Breedte/diameter hoofddouche':'Diameter hoofddouche','Lengte glijstang':'Lengte glijstang'}
COUNTS={'Aantal laden':'Aantal lades','Aantal lades':'Aantal lades','Aantal deuren':'Aantal deuren','Aantal deuren (totaal)':'Aantal deuren',
 'Aantal rozetten':'Aantal rozetten',
 'Aantal sifonuitsparingen':'Aantal sifonuitsparingen','Aantal kraangaten':'Aantal kraangaten','Aantal waskommen':'Aantal spoelbakken',
 'Aantal grepen':'Aantal grepen','Aantal delen':'Aantal delen','Aantal stopfuncties':'Aantal stopfuncties',
 'Aantal straalsoorten hoofddouche':'Aantal straalstanden hoofddouche','Aantal straalsoorten handdouche':'Aantal straalstanden handdouche'}
ENUMS={'Montagewijze':'Montage','Montage':'Montage','Type deur':'Deursysteem','Type douchedeur':'Deursysteem','Glassoort':'Glas','Glas decor':'Glas',
 'Plaats bediening':'Plaats bediening','Afwerking wand':'Wandafwerking','Vorm rozet':'Vorm rozet','Bediening voor aan/uit':'Bediening aan/uit','Aansluitmaat sifon':'Aansluitmaat sifon',
 'Uitvoering handgrepen':'Greepuitvoering','Uitvoering uitloop':'Uitvoering uitloop','Kraanuitloop':'Uitvoering uitloop',
 'Warm/koud aansluiting':'Watertoevoer','Draairichting deur':'Draairichting deur','Materiaal onderkast':'Materiaal',
 'Materiaal kraan':'Materiaal','Materiaal':'Materiaal','Materiaal slang':'Materiaal slang','Materiaal glas':'Materiaal glas',
 'Materiaal profiel/bevestiging':'Materiaal profiel/bevestiging','Afwerking front':'Afwerking front','Vorm':'Vorm',
 'Type handdouche':'Type handdouche','Maat aansluiting aanvoer':'Aansluitmaat watertoevoer','Maat draadaansluiting (inch)':'Aansluitmaat watertoevoer',
 'Maat draadaansluiting doucheslang':'Aansluitmaat doucheslang','Type bevestiging stabilisatiestang':'Bevestiging stabilisatiestang',
 'Lichtkleur':'Kleurtemperatuur','Afzetplateau':'Plaats afzetplateau','Leverwijze':'Leverwijze'}
BOOLS={'Met verlichting':'Verlichting','Met lichtschakelaar':'Lichtschakelaar','Met schakelaar':'Lichtschakelaar','Met stopcontact':'Stopcontact','Wandcontactdoos':'Stopcontact',
 'Met handdouche':'Handdouche inbegrepen','Met doucheslang':'Doucheslang inbegrepen','Met glijstang':'Glijstang inbegrepen','Met hoofddouche':'Hoofddouche inbegrepen','Met uitloop':'Uitloop inbegrepen','Inkortbaar':'Inkortbaar',
 'Met softclose':'Softclose','Softclose':'Softclose','Met inbouwdeel':'Inbouwdeel inbegrepen','Met afvoerplug':'Afvoerplug inbegrepen',
 'Met plug':'Afvoerplug inbegrepen','Met sifon':'Sifon inbegrepen','Met wastafel/blad':'Wastafel of blad inbegrepen','Overloop':'Overloop',
 'Inclusief douchebak':'Douchebak inbegrepen','Met bevestigingsmateriaal':'Bevestigingsmateriaal inbegrepen',
 'Met koude start':'Koudestartfunctie','ColdStart':'Koudestartfunctie','Thermostatisch':'Thermostatisch','Thermostaatkraan':'Thermostatisch',
 'Draaibare uitloop':'Draaibare uitloop','Uittrekbare uitloop':'Uittrekbare uitloop','Spiegelverwarming':'Spiegelverwarming','Antikalkbehandeling':'Glascoating'}
LABELS=set(LENGTHS)|set(COUNTS)|set(ENUMS)|set(BOOLS)|{'EAN','EAN-code','EAN code','Fabrikantnummer','Leveranciernummer','Artikelnummer','Serie','Merk','Afmeting','Breedtemaat','Dieptemaat','Basiskleur','Kleur','Kleur kast','Kleur corpus','Kleurgroep','Glansgraad','Model','Type hendel'}
def clean(t):return re.sub(r'\s+(?:Uitleg|×)$','',re.sub(r'【\d+†([^†]+?)(?:†[^】]+)?】',r'\1',t)).strip()
def parse(page):
 rows=page['lines'];found=[];section=None
 for i,row in enumerate(rows):
  text=clean(row['text']);parts=[x.strip() for x in text.split('|') if x.strip()]
  if text in {'Hoofddouche','Handdouche','Doucheslang','Glijstang','Thermostaat'}:section=text
  if text in {'Bijlagen','Technische documenten','Over Brauer','Bijpassende onderdelen','Ervaringen met dit product','Ervaringen met onze klantenservice'}:break
  inline=len(parts)==2
  if inline:label,value=parts
  else:
   label=text;value=None
   if label not in LABELS and 'sanitairwinkel.nl' in page['url'] and page.get('retrieval')!='public_live_fetch_html':
    # Older Sanitairwinkel layout flattens table columns onto one line.
    for name in sorted(LABELS,key=len,reverse=True):
     if label.startswith(name+' '):
      value=label[len(name):].strip()
      if name=='Materiaal' and value.startswith(('corpus','slang','afbouwdeel','profiel')):continue
      if name=='Vorm' and value.startswith(('hoofddouche','uitloop')):continue
      label=name;inline=True;break
   if not inline and label in LABELS:
    for r in rows[i+1:i+16]:
     v=clean(r['text'])
     if not v or v.startswith('#') or v in {'×','Uitleg'}:continue
     if v in LABELS:break
     if len(v)>120:continue
     if label in LENGTHS and not re.fullmatch(r'\d+(?:[.,]\d+)?(?:\s*[-–]\s*\d+(?:[.,]\d+)?)?\s*(?:cm|mm)',v):continue
     if label in BOOLS and v.lower() not in {'ja','nee'}:break
     value=v;break
  if label not in LABELS or value is None:continue
  value=value.strip()
  if label in LENGTHS:
   if not re.fullmatch(r'\d+(?:[.,]\d+)?(?:\s*[-–]\s*\d+(?:[.,]\d+)?)?\s*(?:cm|mm)',value):continue
   if float(re.match(r'\d+(?:[.,]\d+)?',value).group().replace(',','.'))<=0:continue
   norm=re.sub(r'(?<=\d)(cm|mm)\b',r' \1',value).replace('.',',');target=LENGTHS[label]
  elif label in COUNTS:
   if not re.match(r'^\d+(?:\s*[- ]\s*\w+)?$',value):
    if value=='Eengreeps':norm='1'
    elif value=='Tweegreeps':norm='2'
    else:continue
   else:norm=re.match(r'\d+',value).group()
   target=COUNTS[label]
  elif label in BOOLS:
   if value.lower() not in {'ja','nee'}:continue
   norm=value.capitalize();target=BOOLS[label]
  elif label in ENUMS:
   if len(value)>90 or value.startswith(('Image:','*','##')):continue
   target=ENUMS[label];norm=value
   allowed={'Plaats bediening':{'Links','Rechts','Links en rechts'},'Wandafwerking':{'Met rozetten','Met achterplaat'},'Vorm rozet':{'Rond','Vierkant','Rechthoekig','Ovaal'},'Bediening aan/uit':{'Draaigreep','Drukknop','Sensor'}}
   if target in allowed and value not in allowed[target]:continue
   if target=='Wandafwerking':norm={'Met rozetten':'Rozetten','Met achterplaat':'Afdekplaat'}[value]
   if target.startswith('Aansluitmaat'):
    if not re.fullmatch(r'(?:\d+[. ]?)?\d+[/]\d+\s*(?:inch|\"|″)?',value):continue
    norm=re.match(r'(?:\d+[. ]?)?\d+[/]\d+',value).group().replace('.',' ')+'"'
  else:target=label;norm=value
  if target=='Diameter' and section=='Handdouche':target='Diameter handdouche'
  found.append({'label':target,'value':norm,'source_label':label,'source_value':value,'source_section':section,'line':row['line']})
 sku=next((v['value'] for v in found if v['source_label'] in {'Fabrikantnummer','Leveranciernummer'}),None)
 ean=next((v['value'] for v in found if v['source_label'] in {'EAN','EAN-code','EAN code'}),None)
 if re.search(r'\binclusief inbouwdeel\b',page['title'],re.I):
  found.append({'label':'Inbouwdeel inbegrepen','value':'Ja','source_label':'Met inbouwdeel','source_value':'inclusief inbouwdeel (producttitel)','line':None})
 brand=next((v['value'] for v in found if v['source_label']=='Merk'),None)
 return {'sku':sku,'ean':ean,'brand':brand,'title':page['title'],'requested_sku':page.get('requested_sku'),'requested_url':page.get('requested_url',page['url']),'url':page['url'],'ref':page['ref'],'checked_on':page.get('checked_on','2026-11-07'),'source_snapshot_note':page.get('source_snapshot_note','Search-service snapshot; source revision not guaranteed'),'retrieval':page.get('retrieval','public_web_page_excerpt'),'linked_documents':page.get('linked_documents',[]),'fields':[v for v in found if v['source_label'] in LENGTHS or v['source_label'] in COUNTS or v['source_label'] in ENUMS or v['source_label'] in BOOLS]}
if __name__=='__main__':
 pages=[p for file in sorted(Path('research/brauer-retail').glob('table-excerpts*.json')) for p in json.loads(file.read_text())]
 if not pages:raise SystemExit('Geen ruwe technische tabellen; bestaand retail-observations.json blijft behouden. Gebruik de getypeerde overdrachtsrecords.')
 unique={}
 for p in pages:
  if p['url'] not in unique or p.get('retrieval')=='public_live_fetch_html':unique[p['url']]=p
 fresh=[parse(p) for p in unique.values()]
 target=Path('prepared/retail-observations.json')
 previous=json.loads(target.read_text()) if target.exists() else []
 merged={r['url']:r for r in previous};merged.update({r['url']:r for r in fresh})
 records=list(merged.values())
 Path('prepared/retail-observations.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'retained_or_refreshed_source_pages':len(records),'raw_source_pages':len(fresh)}))
