import fs from 'node:fs';
import assert from 'node:assert/strict';
import {Window} from 'happy-dom';
const before=['component-card.css','bc-product-cards.css','bc-collection.css','bc-external-filters.css','bc-wishlist.css'].map(name=>fs.readFileSync(new URL('./fixtures/assets/'+name,import.meta.url),'utf8')).join('\n');
const after=fs.readFileSync(new URL('../../../../shopify/current/assets/bc-mobile-product-list.css',import.meta.url),'utf8');
const info='<h3 class="bc-filter-card__title">Een volledige lange producttitel die niet wordt afgekapt</h3><dl class="bc-card-specs"><div><dt>Materiaal:</dt><dd>Eiken</dd></div></dl><div class="bc-card-buy"><div class="bc-filter-card__price">€ 820,00</div><p class="bc-card-delivery">Op voorraad</p><div class="bc-card-actions"><a class="bc-card-view" href="/products/demo">Bekijk product</a></div></div>';
function context(width,kind,css) {
 const w=new Window({url:'https://test.invalid/',width,height:844});
 const external=kind.startsWith('external');const search=kind.endsWith('search');
 w.document.documentElement.className=external?'bc-external-filters-active':'';
 w.document.documentElement.style.fontSize='10px';
 let card;
 if(external)card='<article class="bc-filter-card"><button class="bc-wishlist-button"></button><a class="bc-filter-card__media"><img src=""></a><div class="bc-filter-card__info">'+info+'</div></article>';
 else if(search)card='<article class="bc-search-card"><button class="bc-wishlist-button"></button><a class="bc-search-card__link"><div class="bc-search-card__media-wrapper"><div class="bc-search-card__media"><img class="bc-search-card__image" src=""></div></div><div class="bc-search-card__content">'+info.replaceAll('bc-filter-card__title','bc-search-card__title').replace('class="bc-card-buy"','class="native-price-wrap"')+'</div></a></article>';
 else card='<div class="bc-standard-card card-wrapper"><button class="bc-wishlist-button"></button><div class="card"><div class="card__inner"><div class="card__media"><div class="media"><img src=""></div></div></div><div class="card__content"><div class="card__information">'+info.replaceAll('bc-filter-card__title','card__heading').replace('class="bc-card-buy"','class="card-information"')+'</div></div></div></div>';
 const grid=search&&external?'<div id="product-grid"><ul class="product-grid grid"><li class="grid__item">'+card+'</li></ul></div>':'<ul id="product-grid" class="product-grid grid"><li class="grid__item">'+card+'</li></ul>';
 w.document.head.innerHTML='<style>'+css+'</style>';
 w.document.body.innerHTML='<main id="MainContent"><section class="'+(search?'template-search':'bc-collection')+'"><div id="ProductGridContainer">'+grid+'</div></section></main>';
 return w;
}
const results=[];
for(const kind of ['native-collection','external-collection','native-search','external-search'])for(const width of [320,390,430,750,1348]) {
 const w=context(width,kind,after+'\n'+before);
 const d=w.document;const external=kind.startsWith('external');const search=kind.endsWith('search');
 const card=d.querySelector(external?'.bc-filter-card':search?'.bc-search-card__link':'.bc-standard-card > .card');
 const row=d.querySelector(external?'.bc-filter-card':search?'.bc-search-card__link':'.bc-standard-card');
 const title=d.querySelector('h3');
 if(width<750) {
  assert.equal(w.getComputedStyle(card).display,'grid',kind);
  assert.equal(w.getComputedStyle(card).gridTemplateColumns,'minmax(0, 36%) minmax(0, 1fr)',kind);
  assert.equal(w.getComputedStyle(row).borderRadius,'0px',kind);
  assert.equal(w.getComputedStyle(row).boxShadow,'none',kind);
  assert.equal(w.getComputedStyle(d.querySelector('.bc-card-view')).display,'none',kind);
  assert.equal(w.getComputedStyle(d.querySelector('.bc-card-specs')).display,'block',kind);
  assert.equal(w.getComputedStyle(title).fontSize,'16px',kind);
  assert.equal(w.getComputedStyle(title).overflow,'visible',kind);
  if(external)assert.equal(w.getComputedStyle(d.querySelector('.bc-card-delivery')).order,'-1');
  else assert.notEqual(w.getComputedStyle(d.querySelector('.bc-card-delivery')).order,'-1');
 } else {
  const base=context(width,kind,before);
  for(const selector of ['h3','.bc-card-view','.bc-card-delivery','.bc-filter-card__price','.bc-card-specs']) {
   const a=d.querySelector(selector),b=base.document.querySelector(selector);if(!a||!b)continue;
   for(const property of ['display','font-size','padding','margin','border','overflow','order'])assert.equal(w.getComputedStyle(a).getPropertyValue(property),base.getComputedStyle(b).getPropertyValue(property),kind+' '+width+' '+selector+' '+property);
  }
  await base.happyDOM.abort();base.close();
 }
 results.push({kind,width,result:'PASS'});await w.happyDOM.abort();w.close();
}
fs.writeFileSync(new URL('./css-results.json',import.meta.url),JSON.stringify({status:'PASS',tests:results.length,results,scope:'Offline DOM CSS-cascade checks with old styles deliberately loaded last. No real browser geometry, screenshot, overflow, touch or purchase proof.'},null,2)+'\n');
console.log(results.length+' CSS cascade and desktop regression cases PASS');
