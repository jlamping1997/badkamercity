#!/usr/bin/env python3
"""Exact Edition18 Rails set families; read-only V2 supplemental groups."""
import json,re,collections
from pathlib import Path
from build_config_groups import eligible
BASE=Path(__file__).parent
SOURCE=BASE.parent/'hotbath-menu-20261024'
COLORS={k:v['label'] for k,v in json.loads((SOURCE/'book_rules.json').read_text())['finish_dictionary'].items()}
FINISH=('IX','CR','GN','WH','TB','BBP','BCP','BGP','MBP','PBP')
SHAPES={'RAS':'Square','RASS':'Soft Square','RARH':'Round','RARV':'Round','RASV':'Square'}
# Exact manufacturer model blocks, with heading/text evidence from PDF pages.
PAGES={'RAS':[466,467,468,469],'RASS':[470,471,472,473],'RARH':[464,465],'RARV':[478,479,480],'RASV':[476,477],'RAS8050':[474],'RASS8050':[474]}

def norm(t):return re.sub(r'\s+',' ',t.casefold().replace('–','-').replace('—','-')).strip()

def parse(sku,title):
 m=re.fullmatch(r'(RASS|RAS)(50|80)-([1-4])('+ '|'.join(FINISH)+')',sku)
 if m:family,length,count,color=m.groups()
 else:
  m=re.fullmatch(r'(RARH)(50)-([1-4])('+ '|'.join(FINISH)+')',sku) or re.fullmatch(r'(RARV|RASV)(135)-([1-3])('+ '|'.join(FINISH)+')',sku)
  if m:family,length,count,color=m.groups()
  else:
   m=re.fullmatch(r'(RASS8050|RAS8050)('+ '|'.join(FINISH)+')',sku)
   if not m:raise ValueError('UNKNOWN_EXACT_RAILS_MODEL')
   family,color=m.groups();length='80 + 50';count='2'
 if color=='PBP' and (family=='RASV' or (family=='RARV' and count in ('1','2'))):
  raise ValueError('FINISH_NOT_CONFIRMED_FOR_EXACT_BOOK_SET')
 shape=SHAPES.get(family, 'Soft Square' if family=='RASS8050' else 'Square')
 if family.endswith('8050'):
  # These historical titles truncate after the first length. Exact 8050 model is
  # explicitly confirmed by PDF474, so no digit-based inference is involved.
  text=f'Hotbath set van 2 rails {family[:-4]}80 {shape.upper()} 80 en'+(' RAS50' if family=='RAS8050' else '')+f' - {sku}'
  if norm(title)!=norm(text):raise ValueError('TITLE_TEMPLATE_OR_FIXED_FEATURE_CONFLICT')
 else:
  model=family+length
  nword='stang' if count=='1' else 'stangen'
  pretty=f'Hotbath &More Rails {model} {shape} handdoekwarmerset {length}cm - {count} {nword} - {COLORS[color]} - {sku}'
  old=f'Hotbath set van {count} rails {model if family!="RARH" else "RARH 50"} {shape.upper()}{"" if family in ("RARV","RASV") else " "}{length} cm met separate schakelaar excl inbouwelement - {sku}'
  # RARV/RASV legacy titles omit the space before 135 but retain cm.
  if norm(title) not in {norm(pretty),norm(old)}:raise ValueError('TITLE_TEMPLATE_OR_FIXED_FEATURE_CONFLICT')
 return family,{'kleur':COLORS[color],**({'lengte':length+' cm'} if family in ('RAS','RASS') else {}),**({'aantal_stangen':count+' '+('stang' if count=='1' else 'stangen')} if not family.endswith('8050') else {})}

def build(remaining,existing,holds=None):
 holds=holds or {};owners=collections.defaultdict(set)
 for g in existing['groups']:
  for p in g['products']:owners[p['handle']].add(g['id'])
 rows=collections.defaultdict(list);review=[];excluded=[];selected=0
 for p in remaining['products']:
  vs=p.get('variants',{}).get('nodes',[]);sku=str((vs[0] if vs else {}).get('sku') or '')
  if not re.match(r'^(RASS|RASV|RARVM|RARV|RARH|RAS)\d',sku):continue
  selected+=1
  ok,reason=eligible(p)
  if not ok or p['handle'] in holds:
   excluded.append({'sku':sku,'handle':p['handle'],'reason':reason or holds[p['handle']]});continue
  if (p.get('group') or {}).get('value') or owners[p['handle']]:
   excluded.append({'sku':sku,'handle':p['handle'],'reason':'EXISTING_GROUP_RECONCILIATION_REQUIRED'});continue
  try:f,opts=parse(sku,p['title'])
  except ValueError as e:
   review.append({'sku':sku,'handle':p['handle'],'reason':str(e),'title':p['title']});continue
  rows[f].append((p,sku,opts))
 groups=[];families=[]
 for f,items in sorted(rows.items()):
  keys=list(items[0][2]);tuples=[tuple(o[k] for k in keys) for p,s,o in items]
  if len(set(tuples))!=len(tuples):
   review.append({'family':f,'reason':'DUPLICATE_CHOICE_TUPLES'});continue
  menus=[]
  for k in keys:
   vals=sorted(set(o[k] for p,s,o in items),key=lambda x:(0,int(x.split()[0])) if x[0].isdigit() else (1,x))
   if len(vals)<2:continue
   menus.append({'key':k,'label':{'kleur':'Kleur','lengte':'Lengte','aantal_stangen':'Aantal stangen'}[k],'order':len(menus)+1,'display_type':'dropdown' if k=='kleur' else 'buttons','hide_if_single_value':True,'values':vals})
  if len(items)<2 or not menus:
   review.append({'family':f,'reason':'NO_MULTIPLE_CHOICES'});continue
  items.sort(key=lambda x:tuple(x[2][k] for k in keys))
  group={'id':'hotbath-rails-'+f.lower()+'-sets','label':'Hotbath Rails '+f+' '+('80 + 50 cm combinatieset' if f.endswith('8050') else SHAPES[f]+' handdoekwarmerset'),'menus':menus,'products':[{'handle':p['handle'],'url':'/products/'+p['handle'],'title':p['title'],'sort_order':i,'options':o} for i,(p,s,o) in enumerate(items)]}
  groups.append(group);families.append({'family':f,'articles':len(items),'pdf_pages':PAGES[f],'printed_pages':[n-2 for n in PAGES[f]],'choices':[x['key'] for x in menus],'membership_basis':'EXACT_BOOK_MODEL_AND_EXACT_CURRENT_TITLE_TEMPLATE','installation_note':'Only same afbouw/set article class; MBASES installation parts and single spare rails never included. Book says inbouwdeel must be ordered separately.'})
 return {'schema':'hotbath-rails-supplemental-v1','groups':groups,'families':families,'review':review,'excluded':excluded,'metrics':{'selected':selected,'ready_groups':len(groups),'ready_products':sum(len(g['products']) for g in groups),'review':len(review),'excluded':len(excluded)},'book_limitations':['Book family rules were absent in book_rules.json; exact model evidence read directly from local Edition18 PDF.','PDF477 table has apparent RASS80-3 typo; RASV135-3 is separately confirmed by heading and complete set description.','Group membership does not assert that a separate inbouwdeel is supplied; existing prices and titles are preserved.','RARVM integrated-switch model is separate from RARV separate-switch models and excluded here.']}

if __name__=='__main__':
 remaining=json.loads((BASE/'coverage_remaining.json').read_text());existing=json.loads((BASE/'groups-input.json').read_text());holds=json.loads((BASE/'colour_review.json').read_text())['excluded_products']
 result=build(remaining,existing,holds)
 (BASE/'rails_supplemental.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 (BASE/'rails_review.json').write_text(json.dumps({k:result[k] for k in ('metrics','families','review','excluded','book_limitations')},ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result['metrics']))
