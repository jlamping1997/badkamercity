"""Index received supplier files; exact article codes only, no fuzzy or prefix joins."""
from pathlib import Path
import json,hashlib,argparse,re
IMAGE_EXT={'.jpg','.jpeg','.png','.webp','.avif'}
def article_for_name(stem,skus):
 matches=[s for s in skus if stem.casefold()==s.casefold() or any(stem.casefold().startswith(s.casefold()+sep) for sep in ['_',' ','('])]
 return max(matches,key=len) if matches else None
def inventory(catalog,folder):
 skus={p['sku'] for p in catalog};result={sku:{'images':[],'pdfs':[],'issues':[]} for sku in skus};unknown=[]
 for path in sorted(Path(folder).rglob('*')):
  if not path.is_file() or path.suffix.lower() not in IMAGE_EXT|{'.pdf'}:continue
  sku=article_for_name(path.stem,skus)
  if not sku:unknown.append(str(path));continue
  slot='pdfs' if path.suffix.lower()=='.pdf' else 'images'
  seq=re.search(r'(?:_|\s)(\d+)$',path.stem);order=int(seq[1]) if seq else None
  result[sku][slot].append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'order':order})
 for sku,item in result.items():
  images=item['images']
  if len(images)>1 and (any(i['order'] is None for i in images) or len({i['order'] for i in images})!=len(images)):item['issues'].append('EERSTE_AFBEELDING_KIEZEN')
  images.sort(key=lambda i:(i['order'] is None,i['order'] or 0,i['path']))
 return {'articles':result,'unmatched_files':unknown,'official_package_received':False,'inventory_reviewed':False,'import_allowed':False}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--catalog',required=True);parser.add_argument('--media-dir',required=True);parser.add_argument('--output',required=True);args=parser.parse_args();Path(args.output).write_text(json.dumps(inventory(json.loads(Path(args.catalog).read_text()),args.media_dir),ensure_ascii=False,indent=2))
