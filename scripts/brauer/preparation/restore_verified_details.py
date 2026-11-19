"""Carry forward the exact-SKU audit, including unresolved measurement conflicts."""
from pathlib import Path
import json,csv

root=Path('prepared');source=json.loads(Path('recovered/previous-verified-audit.json').read_text());catalog=json.loads((root/'catalog.json').read_text());products={p['sku']:p for p in catalog}
for p in catalog:
 p['specifications'].pop('Serie leverancier',None)
 if p['source']['Serie']:p['specifications']['Serie']='Standaard' if p['source']['Serie']=='Edition' else p['source']['Serie']
 if p['options'].get('colour'):p['specifications']['Kleur']=p['options']['colour']
 if p['options'].get('glazing'):p['specifications']['Glas']=p['options']['glazing']
records={sku:{'ean':r['ean'],'url':r['source_url'],'fields':r['specs']} for sku,r in source['visual']['source_records'].items()}
records.update(source['audit']['exact_source_records'])
deny={'Artikelnummer','Fabrikantnummer','EAN','Merk','Serie','Kleur','Kleurgroep','Kleur profiel/bevestiging','Kleur kast','Kleur corpus','Glansgraad','Materiaal','Materiaal kraan','Materiaal onderkast','Vormgeving / stijlgroep'}
for sku,r in records.items():
 p=products[sku];assert p['ean']==r['ean'],sku
 fields={k:v for k,v in r['fields'].items() if k not in deny and v not in [None,'']}
 p['specifications'].update(fields);p['previous_exact_sku_verification']={'ean':r['ean'],'url':r.get('url',r.get('source_url')),'fields':list(fields),'status':'Previously verified exact identity; no inheritance to other SKUs'}
holds={'5-CE-001':['Hoogte kraan','Hoogte uitloop','Diepte uitloop'],'5-GG-001':['Hoogte kraan'],'GS-OBI2B9030200CE':['Breedte','Breedte zijwand']}
for sku,fields in holds.items():
 p=products[sku]
 if 'MAATBRONCONFLICT' not in p['data_issues']:p['data_issues'].append('MAATBRONCONFLICT')
 for key in fields:p['specifications'][key]='Te bevestigen met actuele leveranciersdocumentatie'
 p['measurement_hold']={'fields':fields,'reason':'Eerder vastgesteld verschil tussen dealerdata en gekoppelde fabrikanttekening; huidige versie moet worden bevestigd.'}
families=json.loads((root/'families.json').read_text())
for g in families:
 for axis in g['axes']:
  if axis['key']=='cutouts':axis['reset_on_change']=['width','drawers']
 if any(products[sku]['data_issues'] for sku in g['skus']):g['status']='CONTROLEREN'
 for sku in g['skus']:products[sku]['group_status']=g['status']
summary=json.loads((root/'summary.json').read_text());summary.update({'previous_exact_sku_details_retained':len(records),'measurement_conflict_skus':len(holds),'families_prepared':sum(g['status']=='VOORBEREID' for g in families),'families_to_review':sum(g['status']!='VOORBEREID' for g in families),'measurement_conflict_articles':list(holds)})
summary['data_issue_counts']['MAATBRONCONFLICT']=3
data=json.loads((root/'sheet-data.json').read_text())
for row in data['product_rows']:
 p=products[row[0]];row[7]=p['group_status'];row[8]=', '.join(p['data_issues'])
for row in data['family_rows']:row[4]=next(g['status'] for g in families if g['id']==row[0])
data['issue_rows']=[r for r in data['issue_rows'] if not r[1].startswith('Maatbronconflict:')]+[[sku,'Maatbronconflict: '+', '.join(fields),'Actuele artikeltekening nodig'] for sku,fields in holds.items()]
for name,value in [('catalog.json',catalog),('families.json',families),('summary.json',summary),('sheet-data.json',data)]: (root/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
import hashlib
gate=json.loads((root/'release-gate.json').read_text());gate['catalog_sha256']=hashlib.sha256((root/'catalog.json').read_bytes()).hexdigest();(root/'release-gate.json').write_text(json.dumps(gate,indent=2)+'\n')
with (root/'productvoorbereiding.csv').open('w',encoding='utf-8-sig',newline='') as file:writer=csv.writer(file);writer.writerow(data['product_headers']);writer.writerows(data['product_rows'])
print(json.dumps({'exact_sku_audit_records_retained':len(records),'measurement_holds':len(holds),'groups_to_review':summary['families_to_review']}))
