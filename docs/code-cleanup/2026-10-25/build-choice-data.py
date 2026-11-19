from pathlib import Path
import json,hashlib,re
R=Path(__file__).parent
T=R/'theme'
manifest=[]
revisions=json.loads((R/'source-revisions.json').read_text())
lookup=['{% doc %}','Resolves a product group to its generated, bounded data asset.','@param {string} source - Original source asset filename.','@param {string} group - Exact group identifier.','@param {string} revision - Current source asset revision.','{% enddoc %}','{%- liquid','  case source']
for p in sorted((R/'datasets').glob('*.json')):
 data=json.loads(p.read_text());groups=data.get('groups',[])
 assert isinstance(groups,list)
 ids=[g['id'] for g in groups];assert len(set(ids))==len(ids),p.name
 if len(groups)<2:continue
 lookup+=['    when '+json.dumps(p.name),'      if revision == '+json.dumps(revisions[p.name]),'      case group']
 for g in groups:
  assert re.fullmatch(r'[a-zA-Z0-9_ /-]+',g['id']),g['id']
  identity=p.name+'|'+g['id']
  name='bc-choice-data-'+hashlib.sha256(identity.encode()).hexdigest()[:16]+'.json'
  output=dict(data);output['groups']=[g]
  content=json.dumps(output,ensure_ascii=False,separators=(',',':'))+'\n'
  path=T/'assets'/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
  lookup+=['        when '+json.dumps(g['id']),'          echo '+json.dumps(name)]
  manifest.append({'source':p.name,'source_revision':revisions[p.name],'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'group':g['id'],'asset':name,'source_bytes':p.stat().st_size,'bytes':len(content.encode()),'products':len(g.get('products',[]))})
 lookup+=['      endcase','      endif']
lookup+=['  endcase','-%}','']
(T/'snippets/bc-choice-data-source.liquid').write_text('\n'.join(lookup))
(R/'choice-data-manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({'group_files':len(manifest),'lookup_bytes':(T/'snippets/bc-choice-data-source.liquid').stat().st_size,'example':next(x for x in manifest if x['group']=='hotbath-book-cb105ext-keuzes')},indent=2))
