"""Read optional notes by exact SKU/EAN, without applying them to store data."""
from pathlib import Path
import argparse,json
import openpyxl
KEYS=['Jouw aanvulling omschrijving','Jouw aanvulling techniek','Jouw afbeeldingen','Jouw PDF-documenten']
def read_notes(workbook,catalog):
 expected={p['sku']:p['ean'] for p in catalog};sheet=openpyxl.load_workbook(workbook,read_only=True,data_only=True)['Producten'];rows=sheet.iter_rows(values_only=True);headers=next(rows);notes={}
 for row in rows:
  values=dict(zip(headers,row));sku=values.get('Artikelnummer')
  if not sku:continue
  if sku not in expected or str(values.get('EAN'))!=expected[sku] or sku in notes:raise ValueError('Artikel/EAN gewijzigd of dubbel: '+str(sku))
  notes[sku]={key:values.get(key) for key in KEYS}
 if set(notes)!=set(expected):raise ValueError('Artikeldekking in aanvulbestand verschilt')
 return notes
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--workbook',required=True);p.add_argument('--catalog',required=True);p.add_argument('--output',required=True);a=p.parse_args();result=read_notes(a.workbook,json.loads(Path(a.catalog).read_text()));Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
