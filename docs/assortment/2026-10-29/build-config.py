from pathlib import Path
import json, re

root = Path(__file__).resolve().parents[3]
baseline = Path(__file__).parent / 'baseline'
nl = {
    'breadcrumb':'Kruimelpad','home':'Home','assortment':'Assortiment',
    'search_label':'Zoek een categorie','search_placeholder':'Zoek een categorie, bijvoorbeeld wastafelkraan',
    'clear':'Wis categoriezoekopdracht','view_all':'Bekijk alle {{ category }}',
    'complete':'Maak het compleet','more_categories':'Meer categorieën',
    'no_results':'Geen categorieën gevonden.','results':'{count} categorieën gevonden.',
    'no_results_help':'Probeer een andere naam, of bekijk alle categorieën.','show_all':'Toon alle categorieën',
    'ask_advice':'Vraag advies','seo_title':'Badkamerassortiment: sanitair, tegels en meubels','seo_description':'Ontdek sanitair, badkamermeubels, kranen, tegels en accessoires bij Badkamercity. Bekijk alle categorieën en vind wat past bij jouw badkamer.'
}
en = {
    'breadcrumb':'Breadcrumb','home':'Home','assortment':'Our range',
    'search_label':'Find a category','search_placeholder':'Find a category, for example basin tap',
    'clear':'Clear category search','view_all':'View all {{ category }}',
    'complete':'Complete your space','more_categories':'More categories',
    'no_results':'No categories found.','results':'{count} categories found.',
    'no_results_help':'Try a different name, or browse all categories.','show_all':'Show all categories',
    'ask_advice':'Ask for advice','seo_title':'Bathroom range: sanitaryware, tiles and furniture','seo_description':'Explore sanitaryware, bathroom furniture, taps, tiles and accessories at Badkamercity. Browse categories and find the right products for your bathroom.'
}
for name, values in [('nl.json',nl),('en.default.json',en)]:
    data=json.loads(re.sub(r'/\*[\s\S]*?\*/', '', (baseline/'locales'/name).read_text()))
    data['bc_assortment']=values
    (root/'locales'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

categories = [
    ('kranen','Kranen','bch-kranen.webp',''),
    ('douches','Douche','bch-douches.webp','douchekranen|douche-accessoires'),
    ('badkamermeubels','Badkamermeubels','bch-badkamermeubels.webp','badkamerspiegels|wastafel-toebehoren'),
    ('wastafels','Wastafels','bch-wastafels.webp','wastafelkranen|wastafel-toebehoren'),
    ('toiletten','Toiletten & fonteinen','bch-toiletten.webp','toilet-accessoires'),
    ('baden','Baden','bch-baden.webp','badkranen|badafvoeren-vulsystemen|bad-accessoires'),
    ('tegels','Tegels','bch-tegels.webp',''),
    ('spiegels-en-verlichting','Spiegels & verlichting','bch-spiegels.webp',''),
    ('accessoires','Accessoires','bch-accessoires.webp',''),
    ('verwarming-en-ventilatie','Verwarming & ventilatie','bca-verwarming.webp','radiatortoebehoren')
]
blocks = {}
for i,(handle,title,asset,supplement) in enumerate(categories):
    blocks[f'category_{i}']={'type':'category','settings':{'collection':handle,'title':title,'asset':asset,'supplement':supplement}}
for i,title in enumerate(['Kranen','Douche','Badmeubels','Wastafels','Toiletten','Baden','Tegels','Spiegels','Accessoires','Verwarming']):
    blocks[f'category_{i}']['settings']['mobile_title']=title
blocks['sunshower']={'type':'promotion','settings':{
    'brand':'Sunshower','heading':'Warmte onder de douche','label':'Ontdek Sunshower','link':'/pages/sunshower',
    'image':'shopify://shop_images/bc-sunshower-beleving-infrarood-v2.png','dark':True
}}
blocks['porcelanosa']={'type':'promotion','settings':{
    'brand':'Porcelanosa','heading':'Tegels met karakter','label':'Ontdek Porcelanosa','link':'/collections/vendors?q=Porcelanosa',
    'asset':'bca-porcelanosa.webp','dark':False
}}
settings = {'menu':'main-menu','heading':'Ontdek ons assortiment','intro':'Alles voor jouw badkamer, overzichtelijk bij elkaar.',
    'categories_heading':'Waar ben je naar op zoek?','promotions_heading':'Uitgelicht voor jouw badkamer',
    'directory_heading':'Alle categorieën, per afdeling','seo_heading':'Vind wat past bij jouw badkamer',
    'seo_text':'<p>Van wastafelkranen en badkamermeubels tot tegels, spiegels en accessoires: bekijk ons assortiment per afdeling. Gebruik de categoriezoeker als je al weet wat je nodig hebt, of ontdek de mogelijkheden via de categorieën hierboven.</p><p>Maak je keuze compleet met bijpassende onderdelen en lees bij ieder product de specificaties. Twijfel je over de combinatie of uitvoering? Neem contact op voor persoonlijk advies.</p>',
    'advice_heading':'Hulp bij het kiezen?','advice_text':'We denken graag met je mee.','advice_link':'/pages/contact'}
data={'sections':{'main':{'type':'bc-assortment','blocks':blocks,'block_order':list(blocks),'settings':settings}},'order':['main']}
(root/'templates/list-collections.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Wrote template, category overrides, two brand links and additive translations')
