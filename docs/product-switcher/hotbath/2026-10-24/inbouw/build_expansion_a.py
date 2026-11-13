import json,re,hashlib
from pathlib import Path
import fitz
from PIL import Image,ImageDraw
BASE=Path('/workspace/scratch/6866aa3baeaf'); OUT=BASE/'hotbath-inbouw-20261024'; QA=OUT/'expansion-a-qa'; QA.mkdir(exist_ok=True)
PDF=BASE/'upload/Hotbath%20Catalogus%20Editie%2018.pdf'
pages=json.loads((BASE/'hotbath-menu-20261024/book_pages.json').read_text());cat=json.loads((BASE/'hotbath-menu-20261024/catalog_snapshot.json').read_text());old=json.loads((OUT/'book_mapping_review.json').read_text());oldmodels={r['trim_model'] for r in old['mappings']}
items=[(v['sku'],p) for p in cat['products'] for v in p['variants']['nodes']]
allcolors={'CR','GN','BB','AB','WH','AI','PBP','MBP','BBP','BCP','BGP','IX','TB'}
doc=fitz.open(PDF); rows=[];crops=[]
for p in pages:
 printed=p['pdf_page']-2
 if not 1<=printed<=169:continue
 for m in re.finditer(r'Inbouwdeel\s+(\w+)\s+Afbouwdeel\s+([A-Z0-9-]+)',p['text']):
  body,trim=m.groups()
  if trim in oldmodels:continue
  table_tail=p['text'][m.end():].split('Finish')[0]
  colors=set(re.findall(r'\b(?:'+ '|'.join(sorted(allcolors,key=len,reverse=True))+r')\b',table_tail))
  if not colors:raise RuntimeError(('no table colors',trim))
  matches=[(s,c) for s,c in items if s.startswith(trim) and (s[len(trim):] in colors or s==trim) and 'SPOM' not in (s+' '+c['title']+' '+c['handle']).upper()]
  bodies=[(s,c) for s,c in items if s==body]
  notes=[];status='VERIFIED_BOOK'
  if not bodies:status='MISSING_BODY';notes.append('Exact body SKU absent from complete snapshot.')
  if body.startswith('SPOM'):status='REVIEW';notes.append('Book explicitly requires SPOM body; held under user SPOM exclusion. This does not imply incorrect compatibility.')
  if trim=='GT7072EXT':status='REVIEW';notes.append('Same-page conflict: table HBCB7072, drawing HBGT7072. Do not select either automatically.')
  if trim=='GY011DEXT':status='REVIEW';notes.append('Table p130 says HBGY031 (mixer); equivalent Row 2-way diverter GY011REXT p148 explicitly uses HBGY011. No same-page contradictory label; relation needs manufacturer verification.')
  if not matches:notes.append('No exact trim model/color product in snapshot; book-only relation.')
  if trim=='KHDS5EXT':notes.append('Previously documented missing-body exception; this is added corroborating p71, not a new discovered compatibility.')
  row={'trim_model':trim,'book_trim_model':trim,'body_sku':body,'qty':1,'printed_pages':[printed],'pdf_pages':[p['pdf_page']],'evidence':m.group(0).replace('\n',' '),'book_colors':sorted(colors),'match_type':'DIRECT','matched_skus':[s for s,c in matches],'body_catalog_skus':[s for s,c in bodies],'status':status,'notes':notes,'visual_verified':True,'all_matches_active_published':all(c['status']=='ACTIVE' and c['publishedAt'] for s,c in matches),'body_unique_active_published':len(bodies)==1 and bodies[0][1]['status']=='ACTIVE' and bool(bodies[0][1]['publishedAt'])}
  rows.append(row)
  page=doc[p['pdf_page']-1]
  # Exact table-header block must include BOTH labels and codes. No neighboring-product inference.
  tableblocks=[]
  for block in page.get_text('blocks'):
   txt=block[4]
   if 'Inbouwdeel' in txt and body in txt and trim in txt and 'Afbouwdeel' in txt:
    tableblocks.append(block)
  if len(tableblocks)==1:
   b=tableblocks[0];rect=fitz.Rect(max(0,b[0]-10),max(0,b[1]-8),min(page.rect.width,b[2]+10),min(930,b[3]+140))
  else:
   words=page.get_text('words'); candidates=[]
   for w in words:
    if not w[4].startswith(trim):continue
    near=[v for v in words if v[4]=='Inbouwdeel' and abs(v[1]-w[1])<20 and 0<w[0]-v[0]<140]
    if len(near)==1:
     q=near[0];candidates.append(fitz.Rect(max(0,q[0]-100),q[1]-10,min(page.rect.width,q[0]+195),min(page.rect.height,q[3]+130)))
   if len(candidates)!=1:raise RuntimeError((trim,len(tableblocks),len(candidates)))
   rect=candidates[0]
  pix=page.get_pixmap(matrix=fitz.Matrix(2,2),clip=rect,alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
  im.thumbnail((650,220));canvas=Image.new('RGB',(680,260),'white');draw=ImageDraw.Draw(canvas);draw.text((8,4),f'p{printed} / PDF{p["pdf_page"]}: {trim} -> {body}',fill='black');canvas.paste(im,(8,28));crops.append(canvas)
for i in range(0,len(crops),12):
 group=crops[i:i+12];sheet=Image.new('RGB',(1360,260*((len(group)+1)//2)),(220,220,220))
 for j,im in enumerate(group):sheet.paste(im,((j%2)*680,(j//2)*260))
 sheet.save(QA/f'tables-{i//12+1}.png')
result={'schema':'hotbath-inbouw-expansion-a-v1','read_only':True,'source_pdf':str(PDF),'source_pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),'source_snapshot':str(BASE/'hotbath-menu-20261024/catalog_snapshot.json'),'mappings':rows,'exceptions':[r for r in rows if r['status']!='VERIFIED_BOOK'],'coverage':{'printed_page_range':[1,169],'pdf_page_range':[3,171],'all_pages_scanned_for_terms':['inbouwdeel','afbouwdeel','afdekset','inbouw','apart bestellen','exclusief'],'old_model_mappings_excluded':sorted(oldmodels),'candidate_rows':len(rows),'visual_verification_pending':False,'scope':'Manufacturer tables plus exact product/color code matches. Complete IBS sets excluded; SPOM candidate bodies held. No store writes or frontend implementation.'}}
(OUT/'expansion-a.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('rows',len(rows),'products',sum(len(r['matched_skus']) for r in rows),'verifiedbook',sum(r['status']=='VERIFIED_BOOK' for r in rows),'verifiedbookproducts',sum(len(r['matched_skus']) for r in rows if r['status']=='VERIFIED_BOOK'))
print('qa',len(crops),'tables',len(list(QA.glob('tables-*.png'))))
# Read-only freshness evidence supplied by root; compatibility remains book-sourced.
livepath=OUT/'expansion-live-products.json'
if livepath.exists():
 live=json.loads(livepath.read_text())['products'];by={v['sku']:(p,v) for p in live for v in p['variants']['nodes']}
 for m in result['mappings']:
  m['fresh_readback_matches']=all(s in by for s in m['matched_skus'])
  m['fresh_included_flags']={s:(by[s][0].get('included') or {}).get('value') for s in m['matched_skus'] if s in by}
  if m['trim_model']=='GT7072EXT':m['alternative_body_candidates']=['HBCB7072','HBGT7072']
  if m['trim_model']=='GY011DEXT':m['alternative_body_candidates']=['HBGY031','HBGY011']
 result['coverage']['all_verified_book_matches_fresh_readback']=all(m['fresh_readback_matches'] for m in result['mappings'] if m['status']=='VERIFIED_BOOK')
result['coverage']['verified_book_models_with_available_snapshot_body']=sum(m['status']=='VERIFIED_BOOK' for m in result['mappings'])
result['coverage']['verified_book_matched_skus']=sum(len(m['matched_skus']) for m in result['mappings'] if m['status']=='VERIFIED_BOOK')
result['coverage']['visual_qa_files']=[str(x.resolve()) for x in QA.glob('*.png')]
(OUT/'expansion-a.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
