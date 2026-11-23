from pathlib import Path
import json,re

root=Path(__file__).parent
source=Path('/workspace/brauer-kleuren-met-productafbeeldingen.html')
text=source.read_text().replace('brauer-all-colour-images','brauer-kleur-eerst-bestaand')
families=json.loads(re.search(r'const families=(.*);\n',text)[1])
pool=json.loads(re.search(r'const specPool=(.*);\n',text)[1])
for family in families:
 family['axes'].sort(key=lambda axis:axis['key']!='colour')
 for field in ['name','nav','note','help']:
  if field in family:family[field]=family[field].replace('Edition','Standaard')
 for product in family['products']:
  for field in ['title','description']:product[field]=product[field].replace('Edition','standaard')
for pair in pool:
 if pair[1]=='Edition':pair[1]='Standaard'
text=re.sub(r'const families=.*;\n',lambda match:'const families='+json.dumps(families,ensure_ascii=False,separators=(',',':'))+';\n',text,1)
text=re.sub(r'const specPool=.*;\n',lambda match:'const specPool='+json.dumps(pool,ensure_ascii=False,separators=(',',':'))+';\n',text,1)
text=text.replace('Edition','Standaard')
Path('/workspace/brauer-kleur-eerst-bestaand.html').write_text(text)
for family in families:
 for product in family['products']:product['specs']=[pool[index] for index in product['specs']]
(root/'earlier-expected.json').write_text(json.dumps(families,ensure_ascii=False,indent=2))
