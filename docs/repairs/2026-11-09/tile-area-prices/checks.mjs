import fs from 'node:fs';
import assert from 'node:assert/strict';
import {Liquid} from 'liquidjs';
import {Window} from 'happy-dom';

const theme = new URL('../../../../shopify/current/', import.meta.url);
const results = [];
const record = test => results.push({test, result:'PASS'});
const plain = s => s.replace(/<[^>]*>/g,' ').replace(/\s+/g,' ').trim();
const liquid = new Liquid({root:new URL('snippets/',theme).pathname, extname:'.liquid'});
liquid.registerTag('doc',{parse(token,remaining){while(remaining.length && remaining.shift().getText()!=='{% enddoc %}'){}},render(){return '';}});
const dict=JSON.parse(fs.readFileSync(new URL('locales/nl.json',theme),'utf8').replace(/^\/\*[\s\S]*?\*\//,''));
liquid.registerFilter('t',(key,...args)=>{
  let value=key.split('.').reduce((v,k)=>v?.[k],dict)||key;
  for(const [key,val] of args) value=value.replaceAll('{{ '+key+' }}',String(val));
  return value;
});
liquid.registerFilter('money',cents=>new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR'}).format(Number(cents)/100));
liquid.registerFilter('money_with_currency',cents=>new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR'}).format(Number(cents)/100)+' EUR');
liquid.registerFilter('money_without_trailing_zeros',cents=>new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR',maximumFractionDigits:0}).format(Number(cents)/100));
liquid.registerFilter('json',x=>JSON.stringify(x??null));
liquid.registerFilter('asset_url',x=>'/assets/'+x);
liquid.registerFilter('stylesheet_tag',x=>'<link rel="stylesheet" href="'+x+'">');
liquid.registerFilter('image_url',x=>x?.src||'');
const context={shop:{currency:'EUR',taxes_included:true},cart:{currency:{iso_code:'EUR'}},settings:{currency_code_enabled:true},localization:{country:{currency:{iso_code:'EUR'}}},routes:{root_url:'/'}};
function product({box=.5,price=2500,unit=5000,mode='',vendor='Cottoceramix',variants=null}={}) {
  const variant={id:12,sku:'T1',price,unit_price:unit,available:true};
  return {id:1,handle:'demo',title:'Demo tile',vendor,price,price_min:price,price_max:price,price_varies:Boolean(variants),available:true,published_at:'2026-11-09',selected_or_first_available_variant:variant,variants:variants||[variant],metafields:{custom:{bron_toelichtingen_json:{value:{tiles:{m2_per_box:box,order_mode:mode,sale_unit:mode?'stuk':'m2',unit_count:1,price_per_m2:{amount:50}}}}}}};
}
async function render(name,product,extra={}) {return liquid.renderFile(name,{...context,product,card_product:product,...extra});}
for(const name of ['price','bc-card-product-search']){
  const html=await render(name,product());
  const prices=[...html.matchAll(/class="price-item[^\"]*">([\s\S]*?)<\/span>/g)].map(x=>plain(x[1]));
  assert.equal(prices.length,1);assert.match(prices[0],/50,00.*m²/);assert(!prices[0].includes('25,00'));
  assert(!html.includes('per doos'));record(name+'-one-area-price');
}
const data=JSON.parse(await render('bc-card-tile-price',product(),{mode:'data'}));
assert.deepEqual(data,{box_area:.5,unit_price_cents:5000,price_varies:false});record('hydration-data-verified-area-price');
for(const name of ['price','bc-card-product-search']){
  for(const p of [product({box:0,unit:0,vendor:'Hotbath',price:14900}),product({box:.5,mode:'unit',price:2995})]) {
    const text=plain(await render(name,p));assert(!text.includes('per m²'));assert(text.includes(p.price===14900?'149':'29,95'));
    record(name+'-normal-or-unit-'+p.price);
  }
}
assert.equal((await render('bc-card-tile-price',product({mode:'unit'}),{mode:'data'})).trim(),'null');record('unit-mode-with-stale-box-area-not-m2');
const derived=product({box:1.08,price:6907,unit:0});derived.metafields.custom.bron_toelichtingen_json.value.tiles.price_per_m2=null;
assert.match(plain(await render('price',derived)),/63,95.*m²/);record('area-price-derived-from-real-box-price');
const sale=product();sale.compare_at_price=10000;sale.selected_or_first_available_variant.compare_at_price=10000;
const saleHtml=await render('price',sale);assert(!/<s[ >]/.test(saleHtml));assert.match(plain(saleHtml),/50,00.*m²/);record('no-box-compare-at-mixed-with-area-price');
const range=product({variants:[{price:3500,unit_price:7000},{price:2500,unit_price:5000}]});
assert.match(plain(await render('price',range)),/Vanaf.*50,00.*m²/);record('variant-family-minimum-area-price');
assert.match(plain(await render('price',range,{use_variant:true})),/50,00.*m²/);record('selected-variant-price');

const buybox=await render('bc-porcelanosa-buybox',product(),{section:{id:'test'},product_form_id:'test-form',actions_markup:''});
assert(!buybox.includes('data-tile-box-price'));assert(buybox.indexOf('data-tile-total')>buybox.indexOf('data-tile-calculator'));record('pdp-area-only-above-calculator-total-below');
const w=new Window({url:'https://test.invalid/products/demo'});w.document.documentElement.lang='nl-NL';
w.document.body.innerHTML='<product-info><form id="test-form"><button type="submit">Add</button></form>'+buybox+'<span class="bc-product-sticky__price"></span></product-info>';
w.eval(fs.readFileSync(new URL('assets/bc-porcelanosa-core.js',theme),'utf8'));
w.eval(fs.readFileSync(new URL('assets/bc-porcelanosa-buybox.js',theme),'utf8'));
const box=w.document.querySelector('bc-porcelanosa-buybox');
const boxes=box.querySelector('[data-tile-box-input]');boxes.value='3';boxes.dispatchEvent(new w.Event('input',{bubbles:true}));
assert.match(box.querySelector('[data-tile-total]').textContent,/75,00/);assert.match(box.querySelector('[data-tile-unit-price]').textContent,/50,00/);
assert.equal(box.querySelector('[data-tile-quantity]').value,'3');assert.match(box.querySelector('[data-tile-supplied]').textContent,/1,5/);record('real-controller-3-half-m2-boxes-equals-75-euros');
box.area.value='1,01';box.area.dispatchEvent(new w.Event('input',{bubbles:true}));assert.equal(box.quantity.value,'3');assert.match(box.querySelector('[data-tile-total]').textContent,/75,00/);record('area-rounds-up-to-whole-boxes-and-real-cart-quantity');
box.current={...box.current,boxUnits:10800,priceCents:6907,unitPriceCents:6395};box.boxMode=true;box.boxInput.value='3';box.calculate();
assert.match(box.querySelector('[data-tile-total]').textContent,/207,21/);assert.match(box.querySelector('[data-tile-unit-price]').textContent,/63,95/);record('real-cent-rounding-3-times-6907-not-rounded-area-total');
await w.happyDOM.abort();w.close();

let replay=fs.readFileSync(new URL('../../2026-11-08/mobile-product-list/contract-checks.mjs',import.meta.url),'utf8');
replay=replay.replace("assert.match(cardEl.querySelector('.bc-filter-card__price').textContent,/820,00/);","assert.match(cardEl.querySelector('.bc-filter-card__price').textContent,tile ? /683,33.*per m²/ : /820,00/);");
replay=replay.replace("if(tile){assert.equal(cardEl.querySelectorAll('.bc-card-unit').length,2);assert.match(cardEl.querySelector('.bc-filter-card__price').textContent,/1,2 m²/);}","if(tile){assert.equal(cardEl.querySelectorAll('.bc-card-unit').length,0);assert(!cardEl.querySelector('.bc-filter-card__price').textContent.includes('820,00'));}");
replay=replay.replace("'./rollback/snippets/bc-card-specs.liquid'","'../../2026-11-08/mobile-product-list/rollback/snippets/bc-card-specs.liquid'");
replay=replay.replace("'./contract-results.json'","'./filter-contract-results.json'");
fs.writeFileSync(new URL('filter-replay.mjs',import.meta.url),replay);
await import('./filter-replay.mjs');
record('full-external-filter-26-regressions-with-new-area-contract');
let pricing=fs.readFileSync(new URL('../../2026-11-08/whole-euro-prices/checks.mjs',import.meta.url),'utf8');
pricing=pricing.replace("const moneyLiquid =","liquid.registerTag('doc',{parse(token,remaining){while(remaining.length && remaining.shift().getText()!=='{% enddoc %}'){}},render(){return '';}});\nconst moneyLiquid =");
pricing=pricing.replace("assert.match(tile, /128,45/);","assert(!tile.includes('128,45'));").replace("assert.match(tile, /1,2 m²/);","assert.match(tile, /per m²/);").replace("tile-box-and-area-amounts-remain-exact","tile-area-only-amount-remains-exact").replace("new URL('checks.json', import.meta.url)","new URL('pricing-contract-results.json', import.meta.url)");
fs.writeFileSync(new URL('pricing-replay.mjs',import.meta.url),pricing);
await import('./pricing-replay.mjs');
record('31-price-format-regressions-with-new-area-contract');
fs.writeFileSync(new URL('checks.json',import.meta.url),JSON.stringify({status:'PASS',tests:results.length,results,scope:'Liquid rendering and actual JS controllers in Happy DOM; no browser geometry or completed order.'},null,2)+'\n');
console.log(results.length+' tile area checks PASS');
