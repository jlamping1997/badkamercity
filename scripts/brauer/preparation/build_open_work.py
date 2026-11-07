"""Make the remaining offline work explicit without granting import permission."""
import json
from pathlib import Path
from collections import Counter

def main():
 root=Path('prepared');catalog=json.loads((root/'catalog.json').read_text());retail=json.loads((root/'retail-enrichment-report.json').read_text());by={p['sku']:p for p in catalog};questions=[]
 def add(p,field,status,values,question,urls):
  questions.append({'sku':p['sku'],'ean':p['ean'],'type':p['product_type'],'field':field,'status':status,'values':values,'question':question,'urls':urls})
 for p in catalog:
  if 'BRONCONFLICT' in p['data_issues']:
   vals='; '.join(k+': '+' / '.join(v) for k,v in p['source_conflicts'].items())
   add(p,', '.join(p['source_conflicts']),'LEVERANCIERSLIJSTEN_VERSCHILLEN',vals,'Bevestig per conflicterend veld de juiste waarde voor dit artikelnummer en EAN. De drie prijslijsten spreken elkaar tegen. Graag actuele artikelgegevens.',[])
  if 'KEUZECOMBINATIE_NIET_UNIEK' in p['data_issues']:
   peers=[x['sku'] for x in catalog if x['family_id']==p['family_id'] and x['sku']!=p['sku'] and 'KEUZECOMBINATIE_NIET_UNIEK' in x['data_issues']]
   add(p,'Verschil tussen uitvoeringen','UITVOERING_BEVESTIGEN',', '.join(peers),'Welke technische of zichtbare eigenschap onderscheidt dit artikel van de andere artikelen in deze keuzegroep? Bevestig ook of een artikel een vervanger is. Niet samenvoegen zonder bevestiging.',[])
  if 'MAATBRONCONFLICT' in p['data_issues']:
   fields=', '.join(p['measurement_hold']['fields']);url=p.get('previous_exact_sku_verification',{}).get('url')
   add(p,fields,'ACTUELE_MAATTEKENING_NODIG',p['measurement_hold']['reason'],'Bevestig de fysieke maten en eventuele stelbereiken met een actuele tekening voor dit exacte artikelnummer/EAN. Vermeld de revisie; nominale prijslijstmaat is onvoldoende.',[url] if url else [])
 for d in retail['differences']:
  if d['status']!='OPEN':continue
  p=by[d['sku']];values=([d['existing']] if d['existing'] else [])+[x['value'] for x in d['candidates']]
  question=f"Bevestig {d['field'].lower()} voor dit exacte artikel. Graag technische tekening of artikelblad met artikelnummer/EAN en revisie. Bij maten aangeven of dit nominale maat, fysieke maat of stelbereik is."
  if d['field']=='Materiaal':question='Bevestig het basismateriaal van dit exacte artikelnummer/EAN: RVS of messing? Graag materiaal apart van kleur/coating vermelden en een actueel artikelblad meesturen.'
  elif d['field']=='Aansluitmaat watertoevoer':question='Bevestig de draadaansluiting van de warm-/koudwatertoevoer voor dit exacte artikelnummer/EAN. Bronnen noemen 1/2 en 3/8 inch. Graag actuele aansluittekening; doucheslangaansluiting apart houden.'
  add(p,d['field'],'BRONVERSCHIL', ' / '.join(dict.fromkeys(values)),question,sorted({x['url'] for x in d['candidates']}))
 for d in retail['scope_rejections']:
  if not d['reason'].startswith('Afwijkende'):continue
  add(by[d['sku']],d['label'],'AFWIJKENDE_SLANGLENGTE',d['source_value'],'Welke lengte heeft de daadwerkelijk meegeleverde doucheslang? De winkeltabel noemt 15 cm. Graag bevestigen met dit setartikelnummer en het artikelnummer van de meegeleverde slang. Geen automatische omzetting naar 150 cm.',[d['url']])
 observed={r['url'] for r in json.loads((root/'retail-observations.json').read_text())}
 queue=json.loads((root/'retail-next-batch-queue.json').read_text());queue['items']=[x for x in queue['items'] if x['url'] not in observed]
 (root/'retail-next-batch-queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
 out={'checked_on':'2026-11-07','questions':questions,'question_rows':len(questions),'question_articles':len({q['sku'] for q in questions}),'question_status_counts':dict(Counter(q['status'] for q in questions)),
 'remaining_url_candidates':len(queue['items']),'articles_missing_chosen_essential_fields':sum(bool(p['specification_review']['missing_essential_fields']) for p in catalog),
 'articles_by_missing_field':dict(Counter(f for p in catalog for f in p['specification_review']['missing_essential_fields'])),
 'media_status':'Wachten op volledige officiële afbeeldingen- en PDF-aanlevering; gevonden winkelbijlagen zijn alleen onderzoeksbronnen.',
 'after_media':['Inventariseren en exact op artikelnummer koppelen; ontbrekende en dubbele bestanden melden.','Eerste gekoppelde productfoto toepassen bij gekozen configuratie; spiegelkastkleuren als stalen; grepen behouden.','Representatieve volledige productpagina’s en keuzepaden beoordelen, inclusief onmogelijke keuzes en afbeelding/specs/prijs bij wisselen.','Pas na akkoord een gecontroleerde import voorbereiden.'],
 'shopify_writes':0,'import_allowed':False,'counts_overlap':True,'all_catalogue_scraped':False,'background_job_running':False}
 (root/'open-work.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in {'questions','articles_by_missing_field','after_media'}},ensure_ascii=False))

if __name__=='__main__':main()
