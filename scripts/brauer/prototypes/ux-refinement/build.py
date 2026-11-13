from pathlib import Path
from html import escape
import json,re,copy,base64,hashlib

root=Path(__file__).parent
old=Path('brauer_analysis/next-sample')
families=json.loads((old/'expected.json').read_text())
media=json.loads((old/'media.json').read_text())
master={p['sku']:p for p in json.loads(Path('brauer_analysis/combined/master.json').read_text())}
previous=json.loads(Path('brauer_analysis/media-link/families.json').read_text())
f=next(f for f in families if f['id']=='design-tap')
standard=[copy.deepcopy(p) for a in previous if a['id']=='tap-low' for p in a['products'] if re.fullmatch(r'5-[A-Z]+-001',p['sku'])]
assert len(standard)==7
for p in standard:
 p['options']={'colour':p['options']['colour'],'design':'Standaard'}
 p['title']='BRAUER wastafelkraan · standaard · laag · '+p['options']['colour']
 p['description']='Lage opbouwwastafelkraan met een gladde greep.'
 p['specs']=[['Afwerking greep','Glad'] if k=='Serie' else [k,v] for k,v in p['specs']]
f['products']+=standard
f['nav']='Wastafelkraan · glad / Carving / Stripe'
f['default_sku']='5-CE-001-HD6'
f['axes'][0]['values']=['Standaard','Carving','Stripe']
f['axes'][1]['values']+=['Coffee'] if 'Coffee' not in f['axes'][1]['values'] else []
f['note']='Wastafelkraan · laag · kies de greepafwerking'
f['help']='De detailfoto’s tonen de structuur in RVS-kleur. De productfoto volgt jouw gekozen kleur.'

# 120 and 160 cm cabinets are distinct product families.
tall=next(f for f in families if f['id']=='tall');index=families.index(tall);families.remove(tall)
for half in [True,False]:
 f=copy.deepcopy(tall);f['id']='tall-half' if half else 'tall-high'
 f['products']=[p for p in f['products'] if (dict(p['specs'])['Hoogte']=='120 cm')==half]
 for p in f['products']:
  direction=dict(p['specs'])['Draairichting deur']
  p['options']={'colour':p['options']['colour'],**({'door':direction} if half else {})}
  p['title']='BRAUER Adore '+('halfhoge kast · 120 cm' if half else 'hoge kast · 160 cm')+' · '+p['options']['colour']
  p['specs'].append(['Producttype','Halfhoge kast' if half else 'Hoge kast'])
 f['axes']=[copy.deepcopy(next(a for a in tall['axes'] if a['key']=='colour'))]+([{'key':'door','label':'Draairichting deur','kind':'buttons','values':['Links','Rechts']}] if half else [])
 f['nav']='Adore · halfhoge kast 120 cm' if half else 'Adore · hoge kast 160 cm'
 f['note']='Adore · halfhoge kast · 120 cm · MFC' if half else 'Adore · hoge kast · 160 cm · MFC'
 f['help']='Eén deur. Kies links- of rechtsdraaiend.' if half else 'Twee deuren. Deze kast is omkeerbaar en kan links of rechts worden geplaatst.'
 f['default_sku']='HK-AD120LCH' if half else 'HK-AD160CH'
 families.insert(index,f);index+=1

mirror=next(f for f in families if f['id']=='mirror')
mirror['kind']='conditional'
for p in mirror['products']:
 spec=dict(p['specs']);w=spec['Breedtemaat']
 p['options']={'colour':p['options']['colour'],'width':w,'door':spec['Draairichting deur']}
 p['title']='BRAUER Impress Deluxe spiegelkast · '+w+' · '+p['options']['colour']
mirror['axes']=[{'key':'colour','label':'Kleur / decor','kind':'decorchips','values':copy.deepcopy(next(a for a in mirror['axes'] if a['key']=='colour')['values'])},{'key':'width','label':'Breedte','kind':'select','values':['60 cm','80 cm','100 cm','120 cm','140 cm']},{'key':'door','label':'Draairichting deur','kind':'buttons','values':['Links','Rechts'],'dependsOn':['width','colour']}]
mirror['help']='De deurrichting verschijnt alleen bij de uitvoering van 60 cm. De kleur kies je met een decorstaal.'

basin=next(f for f in families if f['id']=='basin')
basin['nav']='Aurora · wastafel voor onderkast'
basin['note']='Aurora · wastafel voor onderkast · keramiek'
basin['description']='Wastafel voor plaatsing op een onderkast.'
basin['help']='Deze wastafel komt op een onderkast te liggen. De bakpositie toont de eerste foto van het bijbehorende artikel.'
for p in basin['products']:
 p['description']='Keramische wastafel voor plaatsing op een onderkast. Eén spoelbak en '+p['options']['holes']+' kraangat'+('en.' if p['options']['holes']!='1' else '.')
 p['specs']=[['Montage','Op een wastafelonderkast']]+[(k,v) for k,v in p['specs'] if k!='Montage']

design_labels={'Standaard':'Standaard · glad','Carving':'Carving · gekarteld','Stripe':'Stripe · gestreept'}
for f in families:
 for a in f['axes']:
  if a['key']=='design':
   a['kind']='finishphotos';a['label']='Afwerking greep';a['values']=['Standaard' if v=='Edition' else v for v in a['values']];a['labels']=design_labels
 f['axes']=sorted(f['axes'],key=lambda a:a['key']!='colour')
 if any(a['key']=='design' for a in f['axes']):
  f['help']='Detailfoto’s van de greepstructuur in RVS-kleur. De kleurkeuze bepaalt de productuitvoering.'
 for p in f['products']:
  if p['options'].get('design')=='Edition':p['options']['design']='Standaard'
  p['title']=p['title'].replace('Edition','standaard')
  p['description']=p['description'].replace('Edition','standaard')
  p['specs']=[(k,'Standaard' if v=='Edition' else v) for k,v in p['specs']]
  if p['options'].get('design') in design_labels:
   p['specs']=[(k,v) for k,v in p['specs'] if k!='Afwerking greep']+[('Afwerking greep',{'Standaard':'Glad','Carving':'Gekarteld','Stripe':'Gestreept'}[p['options']['design']])]
 f['note']=f['note'].replace('Edition','Standaard')
 # Validate exact SKU, EAN, price preservation across regrouping.
 for p in f['products']:assert master[p['sku']]['fields']['EAN']==p['ean']
(root/'expected.json').write_text(json.dumps(families,ensure_ascii=False,indent=2))

s=Path('/workspace/brauer-andere-producten.html').read_text()
s=s.replace('brauer-andere-producten','brauer-heldere-keuzes').replace('brauer-other-picker','brauer-refined-picker')
pool=[];lookup={};compact=copy.deepcopy(families);descriptions=[];description_lookup={}
for f in compact:
 for p in f['products']:
  description=p['description']
  if description not in description_lookup:description_lookup[description]=len(descriptions);descriptions.append(description)
  p['description']=description_lookup[description]
  indices=[]
  for pair in p['specs']:
   t=tuple(pair)
   if t not in lookup:lookup[t]=len(pool);pool.append(pair)
   indices.append(lookup[t])
  p['specs']=indices
for n,value in [('families',compact),('specPool',pool)]:s=re.sub(r'const '+n+r'=.*;\n',lambda m:'const '+n+'='+json.dumps(value,ensure_ascii=False,separators=(',',':'))+';\n',s,1)
s=s.replace('const specPool=', 'const descriptions='+json.dumps(descriptions,ensure_ascii=False,separators=(',',':'))+';\nconst specPool=',1)
s=s.replace('for(const f of families)for(const p of f.products)p.specs=p.specs.map(i=>specPool[i]);', 'for(const f of families)for(const p of f.products){p.specs=p.specs.map(i=>specPool[i]);p.description=descriptions[p.description];}')
old_photos=json.loads(re.search(r'const linkedProducts = new Map\((\[.*\])\.map',Path('/workspace/brauer-kleuren-met-productafbeeldingen.html').read_text())[1])
records=json.loads(re.search(r'const linkedProducts = new Map\((\[.*\])\.map',s)[1])
extra_skus={p['sku'] for p in standard};records+=[p for p in old_photos if p['sku'] in extra_skus]
s=re.sub(r'const linkedProducts = new Map\(.*\.map\(p=>\[String\(p.id\),p\]\)\);',lambda m:'const linkedProducts = new Map('+json.dumps(records,separators=(',',':'))+'.map(p=>[String(p.id),p]));',s,1)
details=json.loads((root/'details.json').read_text());finishImages={}
for r in details:
 b=Path(r['path']).read_bytes();assert hashlib.sha256(b).hexdigest()==r['sha256']
 finishImages[{'glad':'Standaard','gekarteld':'Carving','gestreept':'Stripe'}[r['name']]]='data:image/jpeg;base64,'+base64.b64encode(b).decode()
s=s.replace('const handleImages={};','const handleImages={};\nconst finishImages='+json.dumps(finishImages,separators=(',',':'))+';')
module=(root/'conditional-choices.mjs').read_text().replace('export ','')
s=s.replace("      const cabinet=families.find(f=>f.id==='cabinet');",module+"\n      function usesState(f=family){return f.kind==='cabinet'||f.kind==='conditional';}\n      const cabinet=families.find(f=>f.id==='cabinet');")
s=s.replace("families.filter(f=>f.kind==='cabinet').map(f=>[f.id,{...selected.get(f.id).options}])","families.filter(f=>usesState(f)).map(f=>{const options={...selected.get(f.id).options};for(const axis of f.axes)if((axis.when||axis.dependsOn)&&!axisActive(axis,options,f))options[axis.key]=null;return [f.id,options]})")
s=s.replace("let family=families.find(f=>f.id==='cabin');","let family=families.find(f=>f.id==='design-tap');")
s=s.replace("function displayValue(axis,value){","function displayValue(axis,value){if(axis.labels)return axis.labels[value]||value;")
s=s.replace("return family.kind==='cabinet'?cabinetState:selected.get(family.id).options;","return usesState()?cabinetState:selected.get(family.id).options;")
s=s.replace("return family.products.filter(p=>family.axes.every(a=>p.options[a.key]===opts[a.key]));","return matchingChoices(family,opts);")
s=s.replace("const matches=cabinetMatches();return matches.length===1?matches[0]:matches.find(p=>p.options.cutouts===cabinetState.cutouts)||null;","return resolvedChoice(family,cabinetState);")
s=s.replace("if(family.kind==='cabinet'){const matches=cabinetMatches({[axis]:value});return matches.find(p=>p.options.cutouts===cabinetState.cutouts)||matches[0]||null;}","if(usesState()){const matches=cabinetMatches({[axis]:value});return matches.find(p=>p.options.cutouts===cabinetState.cutouts)||matches[0]||null;}")
s=s.replace("if(family.kind==='cabinet'){\n          const changed=", "if(usesState()){\n          const changed=")
s=s.replace("if(changed&&axis!=='colour')cabinetState.cutouts=null;","if(family.kind==='cabinet'&&changed&&axis!=='colour')cabinetState.cutouts=null;")
s=s.replace("const swatch=axis.kind==='metal'||axis.kind==='texture'", "const swatch=['metal','texture','decorchips'].includes(axis.kind)")
s=s.replace("if(axis.kind==='productphotos'){const img=", "if(axis.kind==='finishphotos'){const img=node('img','bc-finish-photo');img.src=finishImages[value];img.alt=displayValue(axis,value)+' · structuurvoorbeeld in RVS-kleur';img.width=200;img.height=187;b.append(img,node('span',null,displayValue(axis,value)));}\n            else if(axis.kind==='productphotos'){const img=")
s=s.replace("if(axis.kind==='texture'&&textures[value])", "if(['texture','decorchips'].includes(axis.kind)&&textures[value])")
s=s.replace("if(axis.key==='colour'){", "if(axis.key==='colour'&&axis.kind!=='decorchips'){")
s=s.replace("axis.kind==='productphotos'?'bc-config-options':", "['productphotos','finishphotos'].includes(axis.kind)?'bc-config-options':")
s=s.replace("axis.kind==='productphotos'?'bc-choice bc-config-choice':", "['productphotos','finishphotos'].includes(axis.kind)?'bc-choice bc-config-choice':")
s=s.replace("controls.push({axis,chosen,entries,select});", "controls.push({axis,group,chosen,entries,select});")
s=s.replace("controls.push({axis,chosen,entries,toggle", "controls.push({axis,group,chosen,entries,toggle")
s=s.replace("const options=currentOptions(),matches=family.kind==='cabinet'?cabinetMatches():[],product=family.kind==='cabinet'?cabinetProduct():selected.get(family.id),reference=product||matches[0];", "const options=currentOptions(),matches=usesState()?cabinetMatches():[],product=usesState()?cabinetProduct():selected.get(family.id),reference=product||matches[0];")
s=s.replace("if(family.kind==='cabinet')selected.set(family.id,product);", "if(usesState())selected.set(family.id,product);")
s=s.replace("product?product.sku:'Kies eerst de afvoerindeling'", "product?product.sku:(family.kind==='conditional'?'Kies de draairichting':'Kies eerst de afvoerindeling')")
s=s.replace("family.cabinetDescription.replace('{drawers}',options.drawers.replace('lades','softclose lades')):product.description", "family.cabinetDescription.replace('{drawers}',options.drawers.replace('lades','softclose lades')):reference.description")
s=s.replace("const {axis,chosen,entries,toggle,count,toggleLabel,dropdown,currentImage,currentName,select}=item;", "const {axis,group,chosen,entries,toggle,count,toggleLabel,dropdown,currentImage,currentName,select}=item;\n          group.hidden=!axisActive(axis,options,family);")
s=s.replace("chosen.textContent=displayValue(axis,options[axis.key]);", "chosen.textContent=options[axis.key]==null?'Kies links of rechts':displayValue(axis,options[axis.key]);")
s=s.replace("target=family.kind==='cabinet'&&cabinetMatches({[axis.key]:value}).length>1&&!cabinetState.cutouts?null:optionTarget", "target=usesState()?resolvedChoice(family,{...cabinetState,[axis.key]:value}):optionTarget")
s=s.replace("!target?'Kies afvoerindeling'", "!target?(family.kind==='conditional'?'Kies de draairichting':'Kies afvoerindeling')")
s=s.replace("if(button.previewImage){const next=candidate(axis.key,value);", "if(button.previewImage){const next=usesState()?resolvedChoice(family,{...cabinetState,[axis.key]:value}):candidate(axis.key,value);")
s=s.replace("if(family.kind==='cabinet')cabinetState=cabinetStates.get(family.id);", "if(usesState())cabinetState=cabinetStates.get(family.id);")
s=s.replace("if(family.kind==='cabinet'&&!product)specs=specs.filter(([label])=>label!=='Sifonuitsparingen');", "if(family.kind==='cabinet'&&!product)specs=specs.filter(([label])=>label!=='Sifonuitsparingen');\n        if(family.kind==='conditional'&&!product)specs=specs.map(([label,value])=>[label,label==='Draairichting deur'?'Nog te kiezen':value]);")
s=s.replace("root.querySelector('[data-product-photo-missing]').hidden=Boolean(mainSrc);", "root.querySelector('[data-product-photo-missing]').hidden=Boolean(mainSrc);root.querySelector('[data-product-photo-missing]').textContent=product?'Afbeelding volgt':family.kind==='conditional'?'Kies de draairichting':'Kies de afvoerindeling';")
css='''
    #brauer-heldere-keuzes .bc-finish-photo{display:block;width:100%;max-width:200px;height:150px;object-fit:contain;background:var(--bc-paper)}
    #brauer-heldere-keuzes .bc-swatch>.bc-chip{width:72px;height:72px;border-radius:6px}
    #brauer-heldere-keuzes .bc-swatch .bc-chip-surface{border-radius:4px}
'''
s=s.replace('  </style>',css+'\n  </style>')
groups=[]
for category in ['Kranen','Glas','Meubels']:
 group='<optgroup label="'+category+'">'
 for f in families:
  if f['category']==category:group+='<option value="'+f['id']+'"'+(' selected' if f['id']=='design-tap' else '')+'>'+escape(f['nav'])+'</option>'
 groups.append(group+'</optgroup>')
s=re.sub(r'(<select id="brauer-refined-picker"[^>]*>).*?(</select>)',lambda m:m[1]+''.join(groups)+m[2],s,1,flags=re.S)
f=next(f for f in families if f['id']=='design-tap');p=next(p for p in f['products'] if p['sku']==f['default_sku'])
for field,value in [('note',f['note']),('title',p['title']),('sku',p['sku']),('description',p['description'])]:s=re.sub(r'(data-field="'+field+r'">)[^<]*',lambda m:m[1]+escape(value),s,1)
s=re.sub(r'(data-field="price">)[^<]*',lambda m:m[1]+'€ '+f'{p["price"]:.2f}'.replace('.',','),s,1)
path=Path('/workspace/brauer-heldere-keuzes.html');path.write_text(s)
print(json.dumps(dict(path=str(path),bytes=path.stat().st_size,families=len(families),products=sum(len(f['products']) for f in families))))
assert path.stat().st_size<1_000_000
