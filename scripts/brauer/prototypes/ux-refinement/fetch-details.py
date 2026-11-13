from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,json,hashlib

root=Path(__file__).parent
# URLs observed in the existing BadkamerXXL article's Afwerking greep explanation.
def download(name):
 url='https://cdn.projectxxl.nl/attributes/afwerking_greep/'+name+'.jpg'
 content=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read()
 path=root/(name+'.jpg');path.write_bytes(content)
 return dict(name=name,url=url,path=str(path),sha256=hashlib.sha256(content).hexdigest(),bytes=len(content))
with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(download,['glad','gekarteld','gestreept']))
(root/'details.json').write_text(json.dumps(records,indent=2))
