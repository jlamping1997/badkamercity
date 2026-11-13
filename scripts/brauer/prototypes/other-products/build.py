from pathlib import Path
from html import escape
import json,re,base64,hashlib,copy
root=Path(__file__).parent
families=json.loads((root/'families.json').read_text())
media=json.loads((root/'media.json').read_text()) if (root/'media.json').exists() else {}
basin=next(f for f in families if f['id']=='basin')
basin['axes'][1]['values']=['Midden','Links','Rechts']
basin['widthLabels']={}
for p in basin['products']:
 src=media.get(p['sku'])
 if src:
  position=src['fields'].get('Uitvoering')
  assert position==('Midden' if p['options']['position']=='Standaard' else p['options']['position'])
  p['options']['position']=position
  width=src['fields'].get('Breedte/diameter');assert width
  basin['widthLabels'][p['options']['width']]=width
  p['specs']=[(k,position if k=='Positie spoelbak' else v) for k,v in p['specs']]
assert len(basin['widthLabels'])==4,'All Aurora widths need exact-SKU checks before using physical labels'
basin['help']='De breedtekeuze toont de gecontroleerde buitenmaat. Niet elke bakpositie of elk kraangat is in iedere breedte leverbaar.'
for f in families:
 for p in f['products']:
  opts=p['options'];spec=dict(p['specs']);src=media.get(p['sku'])
  # Only supplement the exact verified SKU/EAN; never inherit measurements across a series.
  if src:
   assert p['ean']==src['ean'];data=src['fields']
   for dest,keys in [('Breedte',['Breedte','Breedte/diameter']),('Diepte',['Diepte']),('Hoogte',['Hoogte','Hoogte (excl. verlichting)']),('Hoogte kraan',['Hoogte kraan']),('Hoogte uitloop',['Hoogte uitloop']),('Diepte uitloop',['Diepte uitloop']),('Glasdikte',['Glasdikte']),('Wateraansluiting',['Warm/koud aansluiting']),('Afwerking greep',['Afwerking greep'])]:
    for key in keys:
     value=data.get(key)
     if isinstance(value,str) and value and (dest not in ['Breedte','Diepte','Hoogte'] or spec.get(dest)=='Te bevestigen'):
      spec[dest]=value;break
   p['specs']=list(map(list,spec.items()))
  if f['id']=='cabin':p['title']='BRAUER Galactic douchecabine · '+opts['width']+' · '+opts['colour']
  elif f['id']=='void-door':p['title']='BRAUER Void nisdeur · '+opts['width']+' · '+opts['colour']
  elif f['id']=='basin':p['title']='BRAUER Aurora wastafel · '+f['widthLabels'][opts['width']]+' · '+opts['position'].lower()
  elif f['id']=='cabinet':p['title']='BRAUER Trust onderkast · '+opts['width']+' · '+opts['colour']
  elif f['id']=='tall':p['title']='BRAUER Adore hoge kast · '+opts['layout']+' · '+opts['colour']
  elif f['id']=='mirror':p['title']='BRAUER Impress Deluxe spiegelkast · '+opts['layout']+' · '+opts['colour']
  elif f['id']=='design-tap':p['title']='BRAUER '+opts['design']+' wastafelkraan · laag · '+opts['colour']
  elif f['id']=='fountain':p['title']='BRAUER '+opts['design']+' fonteinkraan · '+opts['spout'].lower()+' · '+opts['colour']
(root/'expected.json').write_text(json.dumps(families,ensure_ascii=False,indent=2))
s=(root/'preview-template.html').read_text()
s=s.replace('brauer-all-colour-images','brauer-andere-producten').replace('brauer-sample-picker','brauer-other-picker')
s=s.replace('Drie Brauer productvoorbeelden','Nieuwe Brauer productvoorbeelden')
pool=[];lookup={};compact=copy.deepcopy(families)
for f in compact:
 for p in f['products']:
  indices=[]
  for pair in p['specs']:
   t=tuple(pair)
   if t not in lookup:lookup[t]=len(pool);pool.append(pair)
   indices.append(lookup[t])
  p['specs']=indices
s=re.sub(r'const families=.*;\n',lambda m:'const families='+json.dumps(compact,ensure_ascii=False,separators=(',',':'))+';\n',s,1)
s=re.sub(r'const specPool=.*;\n',lambda m:'const specPool='+json.dumps(pool,ensure_ascii=False,separators=(',',':'))+';\n',s,1)
textures=json.loads((root/'texture-records.json').read_text()) if (root/'texture-records.json').exists() else {}
s=re.sub(r'const textures=.*;\n',lambda m:'const textures='+json.dumps(textures,separators=(',',':'))+';\n',s,1)
records=[]
for sku,r in media.items():
 b=Path(r['photo_path']).read_bytes();assert hashlib.sha256(b).hexdigest()==r['photo_sha256']
 mime='image/jpeg' if b[:2]==b'\xff\xd8' else 'image/png'
 records.append(dict(id='offline:'+sku,sku=sku,images=[dict(id='reference:'+sku,src='data:'+mime+';base64,'+base64.b64encode(b).decode(),media_type='image')]))
s=re.sub(r'const linkedProducts = new Map\(.*\.map\(p=>\[String\(p.id\),p\]\)\);',lambda m:'const linkedProducts = new Map('+json.dumps(records,separators=(',',':'))+'.map(p=>[String(p.id),p]));',s,1)
s=re.sub(r'const handleImages=.*;\n','const handleImages={};\n',s,1)
s=re.sub(r"      const glass=families.find.*?      const selected=",'      const selected=',s,1,flags=re.S)
s=s.replace("let family=families.find(f=>f.id==='tap-height');","let family=families.find(f=>f.id==='cabin');")
s=s.replace("if(family.kind==='cabinet'&&axis.key==='width')return family.widthLabels[value];","if(axis.key==='width'&&family.widthLabels)return family.widthLabels[value];")
s=s.replace("if(family.kind==='cabinet')return cabinetMatches({[axis]:value})[0]||null;","if(family.kind==='cabinet'){const matches=cabinetMatches({[axis]:value});return matches.find(p=>p.options.cutouts===cabinetState.cutouts)||matches[0]||null;}")
s=s.replace("family.kind==='cabinet'?'Greeploze onderkast van MFC met '+options.drawers.replace('lades','softclose lades')+'.':product.description","family.kind==='cabinet'?family.cabinetDescription.replace('{drawers}',options.drawers.replace('lades','softclose lades')):product.description")
s=s.replace("if(axis.kind==='texture'){const img=node('img');img.src=textures[value];", "if(axis.kind==='texture'&&textures[value]){const img=node('img');img.src=textures[value];")
# An unresolved drain layout has no exact image. A chosen two-cutout article must retain that layout in colour previews.
s=s.replace("const target=candidate(axis.key,value),image=firstLinkedProductImage(target,linkedProducts);","const optionTarget=candidate(axis.key,value),target=family.kind==='cabinet'&&cabinetMatches({[axis.key]:value}).length>1&&!cabinetState.cutouts?null:optionTarget,image=firstLinkedProductImage(target,linkedProducts);")
s=s.replace("button.colourMissing.textContent=target?'Productfoto volgt':'Niet combineerbaar';","button.colourMissing.textContent=!optionTarget?'Niet combineerbaar':!target?'Kies afvoerindeling':'Productfoto volgt';")
# The product picker is local review chrome; all product option menus retain the approved behavior.
groups=[]
for category in ['Glas','Meubels','Kranen']:
 group='<optgroup label="'+category+'">'
 for f in families:
  if f['category']==category:group+='<option value="'+f['id']+'"'+(' selected' if f['id']=='cabin' else '')+'>'+escape(f['nav'])+'</option>'
 groups.append(group+'</optgroup>')
s=re.sub(r'(<select id="brauer-other-picker"[^>]*>).*?(</select>)',lambda m:m[1]+''.join(groups)+m[2],s,1,flags=re.S)
first=families[0];p=next(p for p in first['products'] if p['sku']==first['default_sku'])
for field,value in [('note',first['note']),('title',p['title']),('sku',p['sku']),('description',p['description'])]:
 s=re.sub(r'(data-field="'+field+r'">)[^<]*',lambda m:m[1]+escape(value),s,1)
s=re.sub(r'(data-field="price">)[^<]*',lambda m:m[1]+'€ '+f'{p["price"]:.2f}'.replace('.',','),s,1)
s=s.replace(' Grijze opties zijn niet opgenomen bij de overige gekozen opties.',' Grijze opties zijn niet beschikbaar bij je andere keuzes.')
s=s.replace('Offline productvoorbeelden','Nieuwe productproef')
path=Path('/workspace/brauer-andere-producten.html');path.write_text(s)
assert path.stat().st_size<1_000_000,path.stat().st_size
print(json.dumps(dict(path=str(path),bytes=path.stat().st_size,products=sum(len(f['products']) for f in families),photos=len(records))))
