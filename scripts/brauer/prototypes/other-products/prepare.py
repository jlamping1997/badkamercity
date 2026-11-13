from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import json,re

root=Path(__file__).parent
master=json.loads(Path('brauer_analysis/combined/master.json').read_text())
proposal={p['sku']:p for p in json.loads(Path('brauer_analysis/prepared/catalog-proposal.json').read_text())}
families=[]
def axis(key,label,kind,values):return dict(key=key,label=label,kind=kind,values=values)
def product(p,options,specs,description=None,title=None):
 f=p['fields'];assert not p['conflict_fields'],p['sku']
 price=(Decimal(f['Adviesverkoopprijs ex. Btw'])*Decimal('1.21')).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
 assert price==Decimal(proposal[p['sku']]['prepared_consumer_price'])
 return dict(sku=p['sku'],ean=f['EAN'],price=float(price),title=title or 'BRAUER '+f['Productomschrijving'],description=description or f['Productomschrijving'],options=options,specs=specs,future=proposal[p['sku']]['future_available_date'])
def add(id,nav,category,default,products,axes,note,help='',**kw):
 assert any(p['sku']==default for p in products)
 keys=[a['key'] for a in axes]+(['cutouts'] if kw.get('kind')=='cabinet' else [])
 seen=set()
 for p in products:
  key=tuple(p['options'][k] for k in keys);assert key not in seen,(id,p['sku'],key);seen.add(key)
  for a in axes:assert p['options'][a['key']] in a['values'],(id,a,p)
 families.append(dict(id=id,nav=nav,name=nav,category=category,default_sku=default,products=products,axes=axes,note=note,help=help,photoBacked=True,**kw))
colours=['Chroom','Goud','Koper','Gunmetal','Zwart','RVS-kleurig','Coffee']
def metal(f):
 c=f['Kleur'].split(',')[0]
 return next((v for v in colours if c.lower()==v.lower()),c)
decors=['Chateau','Damascus','Driftwood','Erosion','Forest Cacao','Forest Seashell','Forest Tan','Forest Wheat','Grove','Honey','Sunlit','Timber Anthracite','Timber Black','Timber Greige','Timber Grey']
def vals(ps,k,order=None):
 unique={p['options'][k] for p in ps}
 return [x for x in order if x in unique] if order else sorted(unique)
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if f['Serie']=='Galactic' and f['Productgroep']=='Douchecabine met schuifdeur met profiel':
  w,d,h=re.search(r'(\d+)x(\d+)x(\d+)',t).groups();c=metal(f)
  ps.append(product(p,dict(colour=c,width=w+' x '+d+' cm'),[['Serie','Galactic'],['Breedtemaat',w+' cm'],['Dieptemaat',d+' cm'],['Hoogte',h+' cm'],['Deur','Schuifdeur'],['Montage','Omkeerbaar: links of rechts'],['Glas','Helder glas'],['Glascoating','Ja'],['Profiel','Met profiel'],['Kleur',c]],'Douchecabine met schuifdeur, helder glas en glascoating. Omkeerbaar voor plaatsing links of rechts.'))
add('cabin','Galactic · douchecabine','Glas','GS-GTC1H12090200CE',ps,[axis('width','Afmeting','buttons',vals(ps,'width')),axis('colour','Kleur profiel','metal',vals(ps,'colour',colours))],'Galactic · schuifdeur · omkeerbaar','Catalogusmaten. Controleer de exacte plaatsingsmaten op de artikeltekening.')
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if f['Serie']=='Void' and f['Productgroep']=='Nisdeur 2-delig met draaideur profielloos' and not 'Carving' in t:
  w,h=re.search(r'(\d+)x(\d+)',t).groups();door,hinge=re.search(r'draaideur (\d+) aan (muur|glas)',t).groups();c=metal(f)
  op='Scharnieren aan de muur' if hinge=='muur' else 'Scharnieren aan het glas'
  ps.append(product(p,dict(colour=c,width=w+' cm',hinge=op),[['Serie','Void'],['Breedtemaat',w+' cm'],['Hoogte',h+' cm'],['Deurbreedtemaat',door+' cm'],['Deurbevestiging',op],['Montage','Omkeerbaar: links of rechts'],['Glas','Helder glas'],['Glascoating','Ja'],['Profiel','Profielloos'],['Kleur',c]],'Tweedelige nisopstelling met een vaste wand en draaideur. '+op+'. Omkeerbaar voor plaatsing links of rechts.'))
add('void-door','Void · tweedelige nisdeur','Glas','GS-VON2H6050200CE',ps,[axis('width','Breedtemaat','select',sorted(vals(ps,'width'),key=lambda x:int(x.split()[0]))),axis('hinge','Bevestiging van de deur','productphotos',['Scharnieren aan de muur','Scharnieren aan het glas']),axis('colour','Kleur beslag','metal',vals(ps,'colour',colours))],'Void · draaideur · helder glas','Catalogusbreedte. De deurbreedte volgt de gekozen opstelling en staat in de specificaties.')
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if f['Serie']=='Aurora':
  w=re.search(r'wastafel (?:asymmetrisch )?(\d+)',t)[1];holes=re.search(r'en (\d+) kraangat',t)[1]
  pos='Links' if 'spoelbak links' in t else 'Rechts' if 'spoelbak rechts' in t else 'Standaard'
  ps.append(product(p,dict(width=w+' cm',position=pos,holes=holes),[['Serie','Aurora'],['Breedtemaat',w+' cm'],['Breedte','Te bevestigen'],['Diepte','Te bevestigen'],['Hoogte','Te bevestigen'],['Materiaal','Keramiek'],['Kleur','Hoogglans wit'],['Aantal spoelbakken','1'],['Positie spoelbak',pos],['Aantal kraangaten',holes]],'Keramische meubelwastafel in hoogglans wit met één spoelbak. '+('Zonder kraangat.' if holes=='0' else holes+' kraangat'+('en.' if holes!='1' else '.'))))
add('basin','Aurora · meubelwastafel','Meubels','WT-AU1000HW',ps,[axis('width','Breedte','select',sorted(vals(ps,'width'),key=lambda x:int(x.split()[0]))),axis('position','Positie spoelbak','productphotos',['Standaard','Links','Rechts']),axis('holes','Aantal kraangaten','buttons',['0','1','2'])],'Aurora · keramiek · hoogglans wit','De getoonde breedte is de maatklasse. De exacte buitenmaat staat bij de gecontroleerde artikelen in de specificaties.')
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if f['Serie']=='Trust' and f['Productgroep']=='Onderkasten met opbouwgreep' and f['Materiaal']=='MFC' and 'ondiep' not in t:
  w=re.search(r'onderkast (\d+)',t)[1];drawers,cutouts=re.search(r'met (\d+) softclose lades en (\d+) sifon',t).groups();c=f['Kleur']
  ps.append(product(p,dict(colour=c,width=w+' cm',drawers=drawers+' lades',cutouts=cutouts),[['Serie','Trust'],['Materiaal','MFC'],['Breedtemaat',w+' cm'],['Breedte','Te bevestigen'],['Diepte','Te bevestigen'],['Hoogte','Te bevestigen'],['Aantal lades',drawers],['Sifonuitsparingen',cutouts],['Sluiting lades','Softclose'],['Greep','Voor opbouwgrepen'],['Grepen inbegrepen','Nee'],['Kleur / decor',c]],'Onderkast van MFC voor opbouwgrepen, met '+drawers+' softclose lades. Grepen apart kiezen.'))
add('cabinet','Trust · onderkast voor grepen','Meubels','OK-TR80CH',ps,[axis('colour','Kleur / decor','texture',decors),axis('width','Breedte','select',sorted(vals(ps,'width'),key=lambda x:int(x.split()[0]))),axis('drawers','Aantal lades','buttons',['2 lades','4 lades'])],'Trust · MFC · grepen apart','Onderkast zonder wastafel. Afvoerindeling en passende grepen stemmen we apart af.',kind='cabinet',widthLabels={x:x for x in vals(ps,'width')},cabinetDescription='Onderkast van MFC voor opbouwgrepen, met {drawers}. Grepen zijn niet inbegrepen.')
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if f['Serie']=='Adore' and f['Productgroep']=='Hoge kasten greeploos' and f['Materiaal']=='MFC' and 'Wavy' not in t:
  h=re.search(r'kast (\d+)',t)[1];c=f['Kleur'];direction='Omkeerbaar' if 'links- of rechtsdraaiend' in t else 'Links' if 'linksdraaiend' in t else 'Rechts' if 'rechtsdraaiend' in t else 'Omkeerbaar'
  layout=h+' cm · '+('deur links' if direction=='Links' else 'deur rechts' if direction=='Rechts' else '2 deuren, omkeerbaar')
  ps.append(product(p,dict(colour=c,layout=layout),[['Serie','Adore'],['Materiaal','MFC'],['Breedte','Te bevestigen'],['Diepte','Te bevestigen'],['Hoogte',h+' cm'],['Aantal deuren','2' if h=='160' else '1'],['Draairichting deur',direction],['Greep','Greeploos'],['Kleur / decor',c]],'Greeploze kast van MFC. '+('Twee deuren, links of rechts te monteren.' if direction=='Omkeerbaar' else 'Eén '+('links' if direction=='Links' else 'rechts')+'draaiende deur.')))
add('tall','Adore · hoge kast','Meubels','HK-AD120LCH',ps,[axis('layout','Hoogte en deuren','productphotos',['120 cm · deur links','120 cm · deur rechts','160 cm · 2 deuren, omkeerbaar']),axis('colour','Kleur / decor','texture',decors)],'Adore · MFC · greeploos','De uitvoering van 160 cm is omkeerbaar en heeft één artikelnummer per decor.')
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if f['Serie']=='Impress' and f['Productgroep']=='Spiegelkasten met verlichting' and f['Materiaal']=='MFC':
  w=re.search(r'spiegelkast (\d+)',t)[1];c=f['Kleur'];doors=re.search(r'(\d+) (?:linksdraaiende |rechtsdraaiende )?dubbelzijdige',t)[1]
  direction='Links' if 'linksdraaiende' in t else 'Rechts' if 'rechtsdraaiende' in t else 'Meerdere deuren'
  layout=w+' cm'+(' · deur '+direction.lower() if w=='60' else ' · '+doors+' deuren')
  ps.append(product(p,dict(colour=c,layout=layout),[['Serie','Impress Deluxe'],['Materiaal corpus','MFC'],['Breedtemaat',w+' cm'],['Breedte','Te bevestigen'],['Diepte','Te bevestigen'],['Hoogte','Te bevestigen'],['Aantal deuren',doors],['Draairichting deur',direction],['Dubbelzijdige spiegeldeuren','Ja'],['Verlichting','Intern en extern'],['Kleur / decor',c]],'Spiegelkast met interne en externe verlichting en dubbelzijdige spiegeldeuren.'))
add('mirror','Impress Deluxe · spiegelkast','Meubels','SK-IMD100CH',ps,[axis('layout','Breedte en deuren','select',['60 cm · deur links','60 cm · deur rechts','80 cm · 2 deuren','100 cm · 2 deuren','120 cm · 2 deuren','140 cm · 3 deuren']),axis('colour','Kleur / decor','texture',decors)],'Impress Deluxe · intern en extern verlicht','Breedtes zijn maatklassen. Deuren en draairichting volgen de gekozen uitvoering.')
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if re.fullmatch(r'5-[A-Z]+-001-HD[67]',p['sku']):
  design='Carving' if '-HD6' in p['sku'] else 'Stripe';c=metal(f)
  ps.append(product(p,dict(colour=c,design=design),[['Serie',design],['Model','Laag'],['Montage','Opbouw'],['Materiaal',f['Materiaal']],['Kleur',c],['Design',design]],'Lage opbouwwastafelkraan in '+design+'-uitvoering.'))
add('design-tap','Wastafelkraan · Carving / Stripe','Kranen','5-CE-001-HD6',ps,[axis('design','Design','productphotos',['Carving','Stripe']),axis('colour','Kleur','metal',vals(ps,'colour',colours))],'Wastafelkraan · laag · Carving of Stripe')
ps=[]
for p in master:
 f=p['fields'];t=f['Productomschrijving']
 if f['Productgroep']=='Opbouw fonteinkranen':
  design='Carving' if 'Carving' in t else 'Stripe' if 'Stripe' in t else 'Edition';c=metal(f);spout='Gebogen uitloop' if 'gebogen uitloop' in t else 'Standaard uitloop'
  ps.append(product(p,dict(colour=c,design=design,spout=spout),[['Serie',design],['Montage','Opbouw'],['Uitloop',spout],['Materiaal',f['Materiaal']],['Kleur',c]],'Opbouwfonteinkraan in '+design+'-uitvoering met '+spout.lower()+'.'))
add('fountain','Fonteinkraan · design en uitloop','Kranen','5-CE-006',ps,[axis('design','Design','productphotos',['Edition','Carving','Stripe']),axis('spout','Uitloop','productphotos',['Standaard uitloop','Gebogen uitloop']),axis('colour','Kleur','metal',vals(ps,'colour',colours))],'Fonteinkraan · opbouw')
(root/'families.json').write_text(json.dumps(families,ensure_ascii=False,indent=2))
print([(f['id'],len(f['products'])) for f in families])
