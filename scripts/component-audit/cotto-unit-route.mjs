import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {Liquid} from 'liquidjs';
import {Window} from 'happy-dom';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const theme = path.join(root, 'shopify/current');
const read = name => fs.readFileSync(path.join(theme, name), 'utf8');
const localeText = read('locales/nl.json');
const locale = JSON.parse(localeText.slice(localeText.indexOf('{')));
const engine = new Liquid({root:path.join(theme, 'snippets'), extname:'.liquid'});
engine.registerTag('doc', {parse(_token,tokens){while(tokens.length){if(tokens.shift().name==='enddoc')break;}}, render(){return '';}});
engine.registerFilter('t', (key,...args) => {
  let value = String(key).split('.').reduce((obj, part) => obj?.[part], locale) || key;
  for (const arg of args) if (Array.isArray(arg)) value = value.replace(new RegExp('{{\\s*'+arg[0]+'\\s*}}', 'g'), String(arg[1]));
  return value;
});
engine.registerFilter('money', cents => '€'+(Number(cents)/100).toFixed(2).replace('.', ','));
engine.registerFilter('asset_url', value => value);
engine.registerFilter('stylesheet_tag', () => '');
engine.registerFilter('image_url', value => value?.src || 'https://cdn.shopify.com/fixture.jpg');
const windows = [];
const checks = [];
async function check(name, run) { await run(); checks.push(name); }
function product({id=1,color='Blue',price=345,saleUnit='stuk',count=1,size='1,1x15',vendor='Cottoceramix',mode='unit',published=true}={}) {
  const variant = {id:100+id,sku:'UNIT'+id,price,available:true};
  return {id,vendor,title:'Cottoceramix Edge '+color,handle:'edge-'+id,published_at:published?'2026-11-05':null,product_type:'Sierstrip',featured_image:{src:'https://cdn.shopify.com/edge-'+id+'.jpg'},selected_or_first_available_variant:variant,
    metafields:{custom:{bron_toelichtingen_json:{value:{tiles:{order_mode:mode,sale_unit:saleUnit,unit_count:count,lead_time:'Verwacht eind oktober',order_type:'Bestelartikel',color_picker_layout:'expandable_grid'}}}},tiles:{group_id:{value:'UNIT-FIXTURE'},group_products:{value:[]},color:{value:color},size:{value:size},application:{value:'Sierstrip'},execution:{value:'Mat'}},bc_filters:{tegel_lengte_mm:{value:150},tegel_breedte_mm:{value:11}}}};
}
function context(prod) { return {product:prod,section:{id:'unit-fixture'},product_form_id:'unit-form',actions_markup:'',routes:{root_url:'/'},shop:{currency:'EUR'},localization:{country:{currency:{iso_code:'EUR'}}}}; }
async function markup(prod) { return engine.renderFile('bc-porcelanosa-buybox', context(prod)); }
async function fixture({prod=product(),related=[],saved,preview=true}={}) {
  prod.metafields.tiles.group_products.value = related;
  const w = new Window({url:'https://fixture.invalid/products/'+prod.handle}); windows.push(w);
  if (saved) for (const [key,value] of Object.entries(saved)) w.sessionStorage.setItem(key,value);
  w.eval(read('assets/bc-porcelanosa-core.js')); w.eval(read('assets/bc-porcelanosa-buybox.js')); w.eval(read('assets/bc-product-sticky.js'));
  const page = w.document.createElement('product-info');
  page.innerHTML = '<div class="product__info-container"><h1 class="bc-product__title">'+prod.title+'</h1><p class="bc-product__sku">Artikelnummer: '+prod.selected_or_first_available_variant.sku+'</p><div class="bc-buybox__section--actions"><form id="unit-form"><input name="id" value="'+prod.selected_or_first_available_variant.id+'"><button class="product-form__submit" type="submit">Bestellen</button></form></div></div><bc-product-sticky><span data-sticky-price></span><div class="bc-product-sticky__quantity"><button data-sticky-minus>−</button><input data-sticky-quantity><button data-sticky-plus>+</button></div><button data-sticky-submit><span data-sticky-label>Bestellen</span></button><p data-sticky-error hidden></p></bc-product-sticky>';
  const template = w.document.createElement('template'); template.innerHTML = await markup(prod);
  const box = template.content.querySelector('bc-porcelanosa-buybox');
  box.dataset.preview = String(preview);
  page.querySelector('.product__info-container').append(box); w.document.body.append(page);
  return {w,page,box,quantity:box.querySelector('[data-unit-quantity]'),submit:page.querySelector('[type="submit"]')};
}
function set(f,value) {f.quantity.value=value; f.quantity.dispatchEvent(new f.w.Event('input',{bubbles:true}));}
await check('Explicit Cotto opt-in uses unit renderer; other brands and ordinary products retain their gate', async()=>{
  const prefix = read('sections/main-product.liquid').split('<product-info')[0];
  const render = prod => engine.parseAndRender(prefix+'{{ bc_tiles_enabled }}', {product:prod});
  assert.equal((await render(product())).trim(),'true');
  assert.equal((await render(product({vendor:'Other'}))).trim(),'false');
  assert.equal((await render(product({mode:'m2'}))).trim(),'false');
  const old = product({vendor:'Porcelanosa',mode:'m2'}); old.metafields.custom.bron_toelichtingen_json.value.tiles.m2_per_box=1.44;
  assert.equal((await render(old)).trim(),'true');
});
await check('Real piece Liquid has native integer quantity, source delivery and no m2 inputs or cart property', async()=>{
  const text = await markup(product());
  assert.match(text,/per stuk/); assert.match(text,/Verwacht eind oktober/);
  assert.match(text,/name="quantity"[^>]+step="1"/); assert.match(text,/data-order-mode="unit"/);
  assert.doesNotMatch(text,/data-tile-area|data-tile-waste|_bc_m2_per_box|data-tile-calculator|8 - 9 weken|\/ m²/);
});
await check('Catalog excludes m2 products, other vendors, different packs and unpublished siblings',async()=>{
  const prod=product({saleUnit:'pak',count:10});
  const related=[product({id:2,color:'Green',saleUnit:'pak',count:10}),product({id:3,color:'Grey',saleUnit:'pak',count:20}),product({id:4,mode:'m2'}),product({id:5,vendor:'Other',saleUnit:'pak',count:10}),product({id:6,saleUnit:'pak',count:10,published:false})];
  prod.metafields.tiles.group_products.value=related;
  const text=await markup(prod);const catalog=JSON.parse(text.match(/data-tile-catalog>([\s\S]*?)<\/script>/)[1]);
  assert.deepEqual(catalog.products.map(p=>p.sku),['UNIT1','UNIT2']);
  assert(catalog.products.every(p=>p.orderMode==='unit'&&p.saleUnit==='pak'&&p.unitCount===10));
});
await check('Two pieces calculate6.90; invalid quantities block normal and sticky purchase',async()=>{
  const f=await fixture(); set(f,'2');
  assert.match(f.box.querySelector('[data-tile-total]').textContent,/6,90/);assert.equal(f.box.querySelector('[data-unit-received]').textContent,'2 stuks');assert.equal(f.submit.disabled,false);
  for(const value of ['0','-1','1.5','','2147483648']) {set(f,value);assert.equal(f.submit.disabled,true,value);assert.equal(f.page.querySelector('[data-sticky-submit]').disabled,true);assert.equal(f.quantity.getAttribute('aria-invalid'),'true');}
  set(f,'3');assert.equal(f.submit.disabled,false);assert.match(f.box.querySelector('[data-tile-total]').textContent,/10,35/);
});
await check('Pack count means whole native packs, with correct total and received piece count',async()=>{
  const f=await fixture({prod:product({saleUnit:'pak',count:10,price:9950})});set(f,'3');
  assert.match(f.box.querySelector('[data-tile-total]').textContent,/298,50/);assert.equal(f.box.querySelector('[data-unit-received]').textContent,'30 stuks');
  assert.equal(f.quantity.name,'quantity');assert.equal(f.quantity.value,'3');assert.equal(f.box.querySelector('[name="properties[_bc_m2_per_box]"]'),null);
  assert.match(f.box.textContent,/per pak/);assert.match(f.box.textContent,/Aantal pakken/);
});
await check('Actual sticky plus/minus mirrors whole pack quantity and native pack total',async()=>{
  const f=await fixture({prod:product({saleUnit:'pak',count:10,price:9950})});
  const sticky=f.page.querySelector('bc-product-sticky');sticky.sync();
  assert.equal(sticky.querySelector('[data-sticky-plus]').disabled,false);
  sticky.querySelector('[data-sticky-plus]').click();sticky.sync();
  assert.equal(f.quantity.value,'2');assert.equal(sticky.querySelector('[data-sticky-quantity]').value,'2');
  assert.match(f.box.querySelector('[data-tile-total]').textContent,/199,00/);assert.match(sticky.querySelector('[data-sticky-price]').textContent,/199,00/);
  sticky.querySelector('[data-sticky-minus]').click();sticky.sync();assert.equal(f.quantity.value,'1');assert.equal(sticky.querySelector('[data-sticky-minus]').disabled,true);
});
await check('Existing generic quantity-input controls keep their sticky button forwarding',()=>{
  const w=new Window({url:'https://fixture.invalid/products/ordinary'});windows.push(w);w.eval(read('assets/bc-product-sticky.js'));
  const page=w.document.createElement('product-info');
  page.innerHTML='<div class="product__info-container"><span class="bc-buybox__price-current">€3,45</span><quantity-input><button name="minus">−</button><input name="quantity" value="1" min="1" step="1"><button name="plus">+</button></quantity-input><div class="bc-buybox__section--actions"><button class="product-form__submit">Bestellen</button></div></div><bc-product-sticky><span data-sticky-price></span><div class="bc-product-sticky__quantity"><button data-sticky-minus>−</button><input data-sticky-quantity><button data-sticky-plus>+</button></div><button data-sticky-submit><span data-sticky-label>Bestellen</span></button><p data-sticky-error hidden></p></bc-product-sticky>';
  const original=page.querySelector('input[name="quantity"]');const plus=page.querySelector('button[name="plus"]');
  plus.addEventListener('click',()=>{original.value=String(Number(original.value)+1);original.dispatchEvent(new w.Event('change',{bubbles:true}));});
  w.document.body.append(page);const sticky=page.querySelector('bc-product-sticky');sticky.sync();
  assert.equal(sticky.querySelector('[data-sticky-plus]').disabled,false);sticky.querySelector('[data-sticky-plus]').click();sticky.sync();assert.equal(original.value,'2');assert.equal(sticky.querySelector('[data-sticky-quantity]').value,'2');
});
await check('Unit color switch keeps count, updates SKU and prices, and retains last selected photo when collapsed',async()=>{
  const prod=product();const related=['Amber','Green','Ivory','Red','White'].map((color,i)=>product({id:i+2,color,price:495}));
  const f=await fixture({prod,related});set(f,'2');
  f.box.querySelector('[data-tile-colors-toggle]').click();
  f.box.querySelector('[data-tile-field="color"] button[data-choice="White"]').click();
  assert.equal(f.quantity.value,'2');assert.match(f.box.querySelector('[data-tile-total]').textContent,/9,90/);assert.equal(f.page.querySelector('.bc-product__sku').textContent,'Artikelnummer: UNIT6');
  assert.equal(f.page.querySelector('input[name="id"]').value,'106');
  f.box.querySelector('[data-tile-colors-toggle]').click();
  const visible=[...f.box.querySelectorAll('[data-tile-field="color"] button[data-choice]')].filter(b=>!b.hidden);
  assert.equal(visible.length,4);assert(visible.some(b=>b.dataset.choice==='White'&&b.getAttribute('aria-pressed')==='true'));
  const saved=Object.fromEntries(Array.from({length:f.w.sessionStorage.length},(_,i)=>{const key=f.w.sessionStorage.key(i);return[key,f.w.sessionStorage.getItem(key)];}));
  const next=await fixture({prod:product({id:9,color:'White',price:495}),saved});
  assert.equal(next.quantity.value,'2');assert.match(next.box.querySelector('[data-tile-total]').textContent,/9,90/);
});
await check('Unit orders never inherit m2 cache or a differently sized pack cache',async()=>{
  const saved={'bc-tile-order:v2:UNIT-FIXTURE':JSON.stringify({mode:'area',area:'40',waste:10}),'bc-tile-unit-order:v1:UNIT-FIXTURE:pak:20':JSON.stringify({quantity:'12'})};
  const f=await fixture({prod:product({saleUnit:'pak',count:10,price:9950}),saved});assert.equal(f.quantity.value,'1');assert.match(f.box.querySelector('[data-tile-total]').textContent,/99,50/);
});
await check('Invalid unit metadata fails closed and never renders a fabricated m2 or generic delivery',async()=>{
  for(const prod of [product({count:0}),product({count:1.5}),product({count:10}),product({saleUnit:'unknown'}),product({price:0})]) {
    const f=await fixture({prod});assert.equal(f.submit.disabled,true);assert.match(f.box.querySelector('[data-tile-error]').textContent,/hele besteleenheden/);assert.doesNotMatch(f.box.textContent,/8 - 9 weken|m²/);
  }
});
await check('Cart and cards use truthful units and escaped source delivery; other brands retain defaults',async()=>{
  for(const [saleUnit,label] of [['stuk','per stuk'],['pak','per pak'],['set','per set']]) {
    const prod=product({saleUnit,count:saleUnit==='stuk'?1:10});
    assert.equal((await engine.renderFile('bc-cart-unit-label',{product:prod})).trim(),label);
    const card=await engine.renderFile('bc-card-tile-price',{product:prod});assert(card.includes(label));assert(!card.includes('m²'));
    assert.equal((await engine.renderFile('bc-card-tile-price',{product:prod,mode:'data'})).trim(),'null');
  }
  const prod=product();prod.metafields.custom.bron_toelichtingen_json.value.tiles.lead_time='<b>bron</b>';
  assert.match(await engine.renderFile('bc-cart-delivery',{product:prod}),/&lt;b&gt;bron&lt;\/b&gt;/);
  const other=product({vendor:'Other',saleUnit:'pak',count:10});assert.equal((await engine.renderFile('bc-cart-unit-label',{product:other})).trim(),'per stuk');
  assert.match(await engine.renderFile('bc-cart-delivery',{product:other}),/Levertijd op aanvraag/);
});
await check('Cotto exact sizes preserve59.5 versus60 while non-opt-in nominal behavior remains',async()=>{
  const prod=product({size:'59,5x59,5'});const f=await fixture({prod,related:[product({id:2,size:'60x60'})]});
  const sizes=[...f.box.querySelectorAll('[data-tile-field="size"] button')].map(b=>b.textContent);
  assert.equal(sizes.length,2);assert(sizes.includes('60 x 60 cm'));assert(sizes.includes('59,5 x 59,5 cm'));
  assert.equal(f.box.nominalSize('29,4x59,5'),'29,4 x 59,5 cm');
  f.box.dataset.exactSize='false';assert.equal(f.box.nominalSize('29,4x59,5'),'30 x 60 cm');
});
for(const w of windows){await w.happyDOM.abort();w.close();}
console.log(JSON.stringify({status:'PASS',checks,scope:'Actual Liquid+buybox JS lifecycle and source-aware cart/card snippets; no live browser, cart, shipment or checkout claim.'},null,2));
