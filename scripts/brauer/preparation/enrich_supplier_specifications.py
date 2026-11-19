"""Extract additional literal supplier facts; never infer sizes or sibling facts."""
import json,re
from pathlib import Path
from collections import Counter
from build_specifications import TAPS,CABINETS,BASINS,GLASS,ALIASES
from enrich_retail_specifications import normalized

DOOR_GROUPS={
 'Nisdeur 2-delig met draaideur profielloos':'Draaideur',
 'Nisdeur met draaideur profielloos':'Draaideur',
 'Douchecabine met draaideur met profiel':'Draaideur',
 'Douchecabine met draaideur profielloos':'Draaideur',
 'Pendeldeuren profielloos':'Pendeldeur',
 'Nisdeur 2-delig met schuifdeur met profiel':'Schuifdeur',
 'Douchecabine met schuifdeur met profiel':'Schuifdeur',
 'Douchecabine met draai-schuifdeur met profiel':'Draai-schuifdeur',
 'Nisdeur 2-delig met draai-schuifdeur met profiel':'Draai-schuifdeur',
 'Nisdeur met draai-schuifdeur met profiel':'Draai-schuifdeur',
}

def candidates(p):
 s=p['source'];text=s['Productomschrijving'];typ=p['product_type'];out=[]
 exact=(p.get('vendor')=='BRAUER' and s.get('Merk')=='BRAUER'
        and s.get('Artikelcode')==p.get('sku') and s.get('EAN')==p.get('ean')
        and bool(p.get('ean')) and bool(p.get('source_refs')))
 def add(label,value,fragment,rule,field='Productomschrijving'):
  out.append({'label':label,'value':value,'fragment':fragment,'rule':rule,'field':field})
 def match(pattern,label,value,rule):
  m=re.search(pattern,text,re.I)
  if m:add(label,value(m) if callable(value) else value,m.group(0),rule)
 # Keep manufacturer model names literal. They do not prove thickness or texture.
 if s['Uitvoering'] and typ not in TAPS:
  add('Uitvoering',s['Uitvoering'],s['Uitvoering'],'literal_manufacturer_execution','Uitvoering')
 if typ in CABINETS:
  match(r'\bexcl\.\s*(?:opbouw|opleg)?(?:grepen|greep)\b','Grepen inbegrepen','Nee','explicit_excluded_handles')
 if typ in BASINS:
  match(r'\b(\d+) wasbak(?:ken)?\b','Aantal spoelbakken',lambda m:m[1],'explicit_basin_count')
  match(r'\blinks/rechts te plaatsen\b','Links/rechts te plaatsen','Ja','explicit_reversible_basin')
 if typ in TAPS:
  match(r'\bdraaibare (?:ronde |platte )?uitloop\b','Uitvoering uitloop','Draaibaar','explicit_swivel_outlet')
  match(r'\bvaste uitloop\b','Uitvoering uitloop','Vast','explicit_fixed_outlet')
  match(r'\bplatte uitloop\b','Doorsnede uitloop','Plat','explicit_flat_outlet_section')
  match(r'\b(\d+)-standen handdouche\b','Aantal straalstanden handdouche',lambda m:m[1],'explicit_handshower_spray_count')
 if (typ=='Inbouwdouchesets' and exact
     and not re.search(r'\b(?:zonder|exclusief|excl\.)\s+(?:\d+(?:[.,]\d+)?\s*cm\s+)?(?:douchekop|hoofddouche)\b',text,re.I)):
  match(r'\ben\s+(?:\d+(?:[.,]\d+)?\s*cm\s+douchekop|[2-6]-standen\s+(?:(?:cilindervormige|wandmodel)\s+douchekop|inbouw\s+plafond\s+douche))\b',
        'Hoofddouche inbegrepen','Ja','explicit_set_component_headshower')
 if typ in {'Nisdeuren','Douchecabines'} and exact and s.get('Productgroep') in DOOR_GROUPS:
  add('Deursysteem',DOOR_GROUPS[s['Productgroep']],s['Productgroep'],
      'explicit_supplier_door_system','Productgroep')
 if typ in CABINETS|{'Spiegels'}:
  match(r'\bmet klok\b','Klok','Ja','explicit_clock')
  match(r'\bdim- en kleurfunctie\b','Dimbaar','Ja','explicit_combined_dimming')
  match(r'\bdim- en kleurfunctie\b','Lichtkleur instelbaar','Ja','explicit_light_colour_control')
  match(r'\bafstandsbediening\b','Bediening verlichting','Afstandsbediening','explicit_remote_control')
 if typ=='Opbouwnissen':match(r'\bverborgen opbergruimte\b','Verborgen opbergruimte','Ja','explicit_hidden_storage')
 if 'badafvoer' in text.lower():match(r'\bzonder vulfunctie\b','Vulfunctie','Nee','explicit_no_filling_function')
 if typ in GLASS:match(r'\bmet afgeronde hoek\b','Hoekafwerking','Afgeronde hoek','explicit_rounded_glass_corner')
 return out

def main():
 root=Path('prepared');catalog=json.loads((root/'catalog.json').read_text());evidence=json.loads((root/'specification-evidence.json').read_text());added=[];differences=[]
 for p in catalog:
  held=set(p['source_conflicts'])|{ALIASES.get(x,x) for x in p.get('measurement_hold',{}).get('fields',[])}|set(p.get('retail_review',{}).get('open_fields',[]))
  for f in candidates(p):
   label=f['label'];value=f['value'];current=p['specifications'].get(label)
   if label in held:continue
   if current is not None:
    if normalized(label,current)!=normalized(label,value):differences.append({'sku':p['sku'],'ean':p['ean'],'field':label,'existing':current,'supplier_candidate':value,'fragment':f['fragment'],'rule':f['rule'],'action':'Bestaande waarde behouden; verschil beoordelen'})
    continue
   p['specifications'][label]=value
   evidence[p['sku']]['facts'][label]={'kind':'supplier','field':f['field'],'fragment':f['fragment'],'source_refs':p['source_refs'],'url':None,'supplier_extension_rule':f['rule'],'identity':{'sku':p['sku'],'ean':p['ean'],'brand':'BRAUER'}}
   added.append({'sku':p['sku'],'field':label,'new':value})
 # Build the reusable ledger from evidence, so reapplying never erases history.
 cumulative=[]
 for p in catalog:
  for label,e in evidence[p['sku']]['facts'].items():
   if e.get('supplier_extension_rule'):
    cumulative.append({'sku':p['sku'],'ean':p['ean'],'field':label,'new':p['specifications'][label],'source_field':e['field'],'fragment':e['fragment'],'source_refs':e['source_refs'],'rule':e['supplier_extension_rule']})
 report={'checked_on':'2026-11-07','articles_scanned':len(catalog),'fields_added_this_run':len(added),'new_fields':len(cumulative),'articles_with_additions':len({x['sku'] for x in cumulative}),'fields':dict(Counter(x['field'] for x in cumulative)),'additions':cumulative,'differences':differences,'import_allowed':False}
 for name,data in [('catalog.json',catalog),('specification-evidence.json',evidence),('supplier-enrichment-report.json',report)]: (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k not in {'additions','differences'}},ensure_ascii=False));print('Supplier differences:',len(differences))

if __name__=='__main__':main()
