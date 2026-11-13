import fs from 'node:fs';
import assert from 'node:assert/strict';
import {Window} from 'happy-dom';
import {Liquid} from 'liquidjs';

const theme=new URL('../../../../shopify/current/',import.meta.url);
const source=fs.readFileSync(new URL('assets/bc-external-filters.js',theme),'utf8');
const money=fs.readFileSync(new URL('assets/bc-money.js',theme),'utf8');
const results=[];
const tick=async()=>{for(let i=0;i<18;i++)await new Promise(r=>setImmediate(r));};
const record=test=>results.push({test,result:'PASS'});
const base={id:123,shopify_product_id:123,handle:'testtegel',title:'Testtegel',vendor:'Cottoceramix',price_cents:6907,price_varies:false,image_url:''};
const tile={...base,variant_id:789,available:true,can_add:true,specs:[],switcher_html:'',tile_price:{box_area:1.08,unit_price_cents:6395,price_varies:false}};
const section=data=>({'bc-card-data':'<script type="application/json" data-bc-card-data>'+JSON.stringify(data)+'</script>'});

async function setup({search=false,lang='nl',mode='success',data=tile,products=[base],configured=true}={}) {
 const w=new Window({url:'https://test.invalid/'+(search?'search?q=tegel':'collections/demo'),width:390,height:844});
 Object.defineProperty(w.document,'readyState',{configurable:true,value:'complete'});
 w.ResizeObserver=class{observe(){}disconnect(){}};w.IntersectionObserver=class{observe(){}disconnect(){}};
 w.Shopify={routes:{root:'/'}};w.document.documentElement.lang=lang;
 w.document.body.innerHTML=`<main id="MainContent"><section class="${search?'template-search':'bc-collection'}"><div id="BcExternalFilters" data-api-base="https://filters.invalid" data-collection="${search?'__all__':'demo'}" data-search-mode="${search}" data-products-count="${products.length}" ${configured?'data-card-data-section="bc-card-data"':''} data-label-price-loading="${lang==='en'?'Loading price…':'Prijs laden…'}" data-label-price-unavailable="${lang==='en'?'View price':'Bekijk prijs'}"></div><div class="facets-vertical page-width"><aside id="main-collection-filters"></aside><div id="ProductGridContainer"><ul id="product-grid" class="grid product-grid"><li id="native-card">Native €63,95 per m²</li></ul></div></div></section></main>`;
 let release;
 const pending=new Promise(r=>{release=r;});
 if(mode==='timeout') {const original=w.setTimeout.bind(w);w.setTimeout=(fn,ms,...args)=>original(fn,ms===5000?1:ms,...args);}
 w.fetch=async(input,options)=>{
  if(String(input).startsWith('https://filters.invalid/')){
   if(mode==='api-failure')throw new Error('Index down');
   return {ok:true,json:async()=>({products,facets:[],found:products.length,collection:{handle:search?'__all__':'demo',profile_products:products.length}})};
  }
  if(mode==='delayed')await pending;
  if(mode==='reject')throw new Error('Offline');
  if(mode==='timeout')return new Promise((_,reject)=>options.signal.addEventListener('abort',()=>reject(new Error('Abort')),{once:true}));
  return {ok:mode!=='http-error',json:async()=>{
   if(mode==='json-error')throw new Error('Invalid JSON');
   if(mode==='null-section')return {'bc-card-data':null};
   if(mode==='broken-payload')return {'bc-card-data':'<script type="application/json" data-bc-card-data>{broken}</script>'};
   return section(data);
  }};
 };
 w.eval(money);w.eval(source);await tick();
 return {w,release,price:()=>w.document.querySelector('.bc-filter-card__price'),cart:()=>w.document.querySelector('[data-bc-card-cart]'),close:async()=>{await w.happyDOM.abort();w.close();}};
}

for(const search of [false,true]) {
 const p=await setup({search,mode:'delayed'});
 assert.equal(p.price().textContent,'Prijs laden…');assert.equal(p.price().getAttribute('aria-busy'),'true');assert.equal(p.price().dataset.bcPriceState,'loading');assert(p.cart().disabled);
 assert(!p.w.document.querySelector('#product-grid').textContent.includes('69,07'));
 p.release();await tick();
 assert.match(p.price().textContent,/63,95 per m²/);assert(!p.price().textContent.includes('69,07'));assert.equal(p.price().dataset.bcPriceState,'ready');assert.equal(p.price().getAttribute('aria-busy'),'false');assert(!p.cart().disabled);
 record('delayed-request-never-flashes-box-price-'+(search?'search':'collection'));await p.close();
}
for(const mode of ['http-error','reject','timeout','json-error','null-section','broken-payload'])for(const search of [false,true]) {
 const p=await setup({mode,search});if(mode==='timeout')await new Promise(r=>setTimeout(r,10));await tick();
 assert.equal(p.price().textContent,'Bekijk prijs');assert.equal(p.price().getAttribute('aria-busy'),'false');assert.equal(p.price().dataset.bcPriceState,'unavailable');assert(p.cart().disabled);
 assert.equal(p.w.document.querySelector('.bc-card-view').getAttribute('href'),'/products/testtegel');assert(!p.price().textContent.match(/[0-9€]/));
 record(mode+'-safe-product-link-'+(search?'search':'collection'));await p.close();
}
for(const [label,data] of [
 ['wrong-identity',{...tile,id:999}],
 ['missing-price',{...tile,tile_price:null,price_cents:null}],
 ['invalid-unit-price',{...tile,tile_price:{box_area:1.08,unit_price_cents:null}}],
 ['invalid-box-area',{...tile,tile_price:{box_area:0,unit_price_cents:6395}}],
 ['negative-price',{...tile,tile_price:null,price_cents:-1}]
]) {
 const p=await setup({data});assert.equal(p.price().textContent,'Bekijk prijs');assert(p.cart().disabled);record(label+'-cannot-show-misleading-price');await p.close();
}
for(const [label,data,expected] of [
 ['normal-whole-euro',{...tile,vendor:'Hotbath',tile_price:null,price_cents:14900},/149(?!,00)/],
 ['normal-cents',{...tile,tile_price:null,price_cents:14949},/149,49/],
 ['unit-product',{...tile,tile_price:null,price_cents:2995},/29,95/],
 ['normal-range',{...tile,tile_price:null,price_cents:14900,price_varies:true},/Vanaf.*149/],
 ['tile-range',{...tile,tile_price:{...tile.tile_price,price_varies:true}},/Vanaf.*63,95.*per m²/],
 ['zero-price',{...tile,tile_price:null,price_cents:0},/0,00/]
]){
 const p=await setup({data});assert.match(p.price().textContent,expected);assert.equal(p.price().dataset.bcPriceState,'ready');assert(!p.cart().disabled);if(label!=='tile-range')assert(!p.price().textContent.includes('per m²'));record(label+'-retains-verified-price');await p.close();
}
const english=await setup({lang:'en',mode:'delayed'});assert.equal(english.price().textContent,'Loading price…');english.release();await tick();assert.equal(english.price().dataset.bcPriceState,'ready');record('english-loading-label');await english.close();
const englishFail=await setup({lang:'en',mode:'http-error'});assert.equal(englishFail.price().textContent,'View price');record('english-failure-label');await englishFail.close();
const missingConfig=await setup({configured:false});assert.equal(missingConfig.price().textContent,'Bekijk prijs');record('missing-section-config-does-not-load-forever');await missingConfig.close();
const native=await setup({mode:'api-failure'});assert(native.w.document.querySelector('#native-card'));assert.equal(native.w.document.querySelector('.bc-filter-card'),null);record('index-failure-keeps-native-unit-price');await native.close();

const engine=new Liquid();
engine.registerTag('doc',{parse(token,remaining){while(remaining.length&&remaining.shift().getText()!=='{% enddoc %}'){}},render(){return '';}});
engine.registerFilter('asset_url',s=>s);engine.registerFilter('stylesheet_tag',s=>'<link href="'+s+'">');
for(const lang of ['nl','en.default']){
 const json=JSON.parse(fs.readFileSync(new URL('locales/'+lang+'.json',theme),'utf8').replace(/^\/\*[\s\S]*?\*\//,''));
 engine.registerFilter('t',key=>key.split('.').reduce((v,k)=>v?.[k],json)||key);
 const html=await engine.parseAndRender(fs.readFileSync(new URL('snippets/bc-external-filters.liquid',theme),'utf8'),{collection_handle:'demo',section_id:'demo',shop:{name:'Badkamercity'},collection:{all_products_count:1},search:{terms:''},settings:{}});
 assert(html.includes('data-label-price-loading="'+json.bc_listing.price_loading+'"'));assert(html.includes('data-label-price-unavailable="'+json.bc_listing.price_unavailable+'"'));record('real-liquid-localized-label-contract-'+lang);
}
fs.writeFileSync(new URL('checks.json',import.meta.url),JSON.stringify({status:'PASS',tests:results.length,results,scope:'Actual filter JS in Happy DOM and Liquid label rendering, synthetic offline data, including errors/timeouts. No live network-fault injection or completed order.'},null,2)+'\n');
console.log(results.length+' price fallback checks PASS');
