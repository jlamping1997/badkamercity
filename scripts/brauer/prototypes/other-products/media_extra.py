from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from html import unescape
from html.parser import HTMLParser
import urllib.request,json,re,hashlib
root=Path(__file__).parent
(root/'pages').mkdir(exist_ok=True);(root/'photos').mkdir(exist_ok=True)
master={p['sku']:p for p in json.loads(Path('brauer_analysis/combined/master.json').read_text())}
families=json.loads((root/'families.json').read_text())
all_skus={p['sku'] for f in families for p in f['products']}
def download(url):
 r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35)
 return r.read(),r.url
def fields(s):
 out={};rows=list(re.finditer(r'<div class="row[^\"]*product-specs-row[^\"]*">',s))
 for i,m in enumerate(rows):
  seg=s[m.end():rows[i+1].start() if i+1<len(rows) else m.end()+3000];cols=re.split(r'<div class="col-6">',seg)
  if len(cols)<3:continue
  chunks=[unescape(c).strip() for c in re.findall(r'>([^<>]+)<','<div>'+cols[1]+'</div>') if c.strip()]
  if not chunks:continue
  key=chunks[0];raw=cols[2].split('</div>')[0];value=' '.join(unescape(re.sub('<[^>]+>',' ',raw)).split())
  if not value:
   if 'fa-check' in raw:value=True
   elif 'fa-times' in raw:value=False
  if key not in out:out[key]=value
 return out
class Images(HTMLParser):
 def __init__(self):super().__init__();self.first=None
 def handle_starttag(self,t,a):
  d=dict(a);src=d.get('src','')
  if t=='img' and self.first is None and 'product-carousel' in d.get('class','') and '/products/' in src:self.first=src
sources={'void-extra': 'https://www.badkamerxxl.nl/bewonen-sean-2-delige-nisopstelling-type-c-inloopwand-met-nisdeur-aaneengeschakeld-110-cm-50-60-antraciet', 'tall-extra': 'https://www.badkamerxxl.nl/bewonen-hoge-kast-nexxt-160-old-castle-7136'}
def config(pair):
 n,url=pair;path=root/(n+'.html')
 if not path.exists():path.write_bytes(download(url)[0])
 s=path.read_text();m=re.search(r'var CONFIGURATOR_META = (\{.*?\});',s)
 initial=fields(s);out=[{'id':None,'url':url}]
 if m:
  cid=json.loads(m[1])['configId'];p=root/(n+'-variants.json')
  if not p.exists():p.write_bytes(download('https://www.badkamerxxl.nl/configurator/'+str(cid)+'/variants')[0])
  lookup=json.loads(p.read_text())['data']['variant_lookup']
  for key,id in lookup.items():
   a=dict(x.split('=',1) for x in key.split('|'))
   # Keep this media request small: Chrome, or the default size in the first six colour/decor choices.
   chrome=a.get('basiskleur')=='Chroom' or any('chateau'==str(v).lower() for v in a.values())
   target=(n in ['cabin','basin','carving','stripe','fountain-low','fountain-high']) or chrome
   if not target:
    first_values=set(['Chateau','Damascus','Driftwood','Erosion','Forest Cacao','Forest Seashell'])
    default_sizes={'trust':'800','tall':'1200','mirror':'990'}
    target=(any(str(v) in first_values for v in a.values()) and any(str(v) in {default_sizes.get(n,''),'80' if n=='trust' else '100' if n=='mirror' else '120'} for k,v in a.items() if 'breed' in k or 'hoog' in k))
   if n=='void':target=chrome or a.get('breedtemaat') in ['110cm','110 cm']
   if n=='void-extra':target=a.get('kleur_profiel')=='Chroom' or a.get('verstelbaarheid_breedte')=='1074'
   if n=='tall-extra':target=any(str(v) in ['Chateau','Damascus','Driftwood','Erosion','Forest Cacao','Forest Seashell'] for v in a.values())
   if target:out.append({'id':id,'url':'https://www.badkamerxxl.nl/product/'+str(id)})
 print('Routes',n,len(out),flush=True);return out
def work(route):
 url=route['url'];name=str(route['id']) if route['id'] else hashlib.sha256(url.encode()).hexdigest()[:10];path=root/'pages'/(name+'.html')
 if path.exists():s=path.read_text();final=url
 else:
  b,final=download(url);path.write_bytes(b);s=b.decode()
 f=fields(s);sku=str(f.get('Fabrikantnummer','')).upper()
 if sku not in all_skus:return None
 assert f.get('EAN')==master[sku]['fields']['EAN'],(sku,f.get('EAN'))
 im=Images();im.feed(s);assert im.first,(sku,'no photo')
 thumb=im.first.replace('/480x480/','/200x200/')
 path=root/'photos'/(sku+'.img')
 if not path.exists():path.write_bytes(download(thumb)[0])
 photo=path.read_bytes();assert photo[:2]==b'\xff\xd8' or photo[:8]==b'\x89PNG\r\n\x1a\n',(sku,photo[:10])
 return dict(sku=sku,ean=f['EAN'],source_url=final,fields=f,first_gallery_image=im.first,preview_url=thumb,photo_path=str(path),photo_bytes=len(photo),photo_sha256=hashlib.sha256(photo).hexdigest(),source_sha256=hashlib.sha256(s.encode()).hexdigest())

routes=[]
for pair in sources.items():routes.extend(config(pair))
records={};errors=[]
with ThreadPoolExecutor(max_workers=8) as ex:
 jobs={ex.submit(work,r):r for r in routes}
 for fut in as_completed(jobs):
  try:
   r=fut.result()
   if r:records[r['sku']]=r
  except Exception as e:errors.append(str(e))
(root/'media-extra.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print(json.dumps(dict(photos=len(records),errors=errors)))
