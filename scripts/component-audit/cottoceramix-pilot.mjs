import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
import assert from 'node:assert/strict';
import {Liquid} from 'liquidjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const theme=path.join(root,'shopify/current');
const products=JSON.parse(fs.readFileSync(path.join(root,'docs/cottoceramix/2026-11-05/rebel/products.json'),'utf8'));
const core=createRequire(import.meta.url)(path.join(theme,'assets/bc-porcelanosa-core.js'));
const locale=JSON.parse(fs.readFileSync(path.join(theme,'locales/nl.json'),'utf8').replace(/^\s*\/\*[\s\S]*?\*\//,''));
const engine=new Liquid({root:path.join(theme,'snippets'),extname:'.liquid'});
engine.registerTag('doc',{parse(_token,tokens){while(tokens.length){if(tokens.shift().name==='enddoc')break;}},render(){return '';}});
engine.registerFilter('t',key=>String(key).split('.').reduce((o,k)=>o?.[k],locale)||key);
engine.registerFilter('money',cents=>'€'+(Number(cents)/100).toFixed(2).replace('.',','));
engine.registerFilter('asset_url',value=>value);
engine.registerFilter('stylesheet_tag',()=> '');
engine.registerFilter('inline_asset_content',()=> '');
engine.registerFilter('image_url',value=>value?.src||'fixture.jpg');
const checks=[];
async function check(name,run){await run();checks.push(name);}
function product(tiles,vendor='Revoir Paris',stock=false){return {vendor,title:'Testproduct',has_only_default_variant:true,metafields:{custom:{bron_toelichtingen_json:{value:{tiles}},leverancier_voorraad:{value:stock}}}};}
function line(prod,quantity=3){return {product:prod,quantity,key:'fixture-'+prod.vendor,index:0,properties:{},options_with_values:[],discounts:[],line_level_discount_allocations:[],original_price:9929,final_price:9929,original_line_price:29787,final_line_price:29787,variant:{sku:'FIXTURE',available:true,quantity_rule:{increment:1,min:1}},url:'/products/fixture'};}
const tile={m2_per_box:1.44,lead_time:'Op voorraad bij leverancier',order_type:'Voorraadartikel'};
const tileLine=line(product(tile));
const normalLine=line(product(undefined,'Hotbath'));
const read=name=>fs.readFileSync(path.join(theme,name),'utf8');
await check('22 unique SKU/product/variant identities and complete 11 x 2 choice matrix',()=>{
  assert.equal(products.length,22);
  for(const key of ['sku','product_id','variant_id','handle'])assert.equal(new Set(products.map(p=>p[key])).size,22);
  assert.equal(new Set(products.map(p=>p.color)).size,11);
  for(const color of new Set(products.map(p=>p.color)))assert.deepEqual(products.filter(p=>p.color===color).map(p=>p.size).sort(),['100 x 100 cm','60 x 60 cm']);
});
const choices=products.map(p=>({sku:p.sku,color:p.color,size:p.size,type:'Vloertegel',finish:'Mat',thickness:10,area:p.size.startsWith('100')?10000:3600,boxUnits:Math.round(p.m2_per_box*10000),priceCents:Math.round(Number(p.box_price)*100)}));
await check('Every color switch preserves the current size; size switches preserve color',()=>{
  for(const current of choices){
    for(const color of new Set(choices.map(p=>p.color))){const next=core.choose(choices,current,'color',color);assert.equal(next.size,current.size);assert.equal(next.color,color);}
    for(const size of ['60 x 60 cm','100 x 100 cm']){const next=core.choose(choices,current,'size',size);assert.equal(next.color,current.color);assert.equal(next.size,size);}
  }
});
await check('10 m2 plus 10 percent gives 8 x 1.44 or 6 x 2 m2 at exact box prices',()=>{
  for(const p of choices){const result=core.calculate('10',10,p.boxUnits,p.priceCents);assert.equal(result.boxes,p.boxUnits===14400?8:6);assert.equal(result.supplied,p.boxUnits===14400?115200:120000);assert.equal(result.total,p.boxUnits===14400?79432:95940);}
});
await check('Cart unit label is per box for tiles and per item for normal and missing metadata',async()=>{
  for(const tiles of [tile,{m2_per_box:2}])assert.equal((await engine.renderFile('bc-cart-unit-label',{product:product(tiles)})).trim(),'per doos');
  for(const tiles of [undefined,{m2_per_box:0}])assert.equal((await engine.renderFile('bc-cart-unit-label',{product:product(tiles)})).trim(),'per stuk');
});
await check('Real notification section renders box label and preserves normal item label',async()=>{
  const markup=read('sections/cart-notification-product.liquid');
  assert.match(await engine.parseAndRender(markup,{cart:{items:[tileLine]},settings:{}}),/€99,29<small>per doos<\/small>/);
  assert.match(await engine.parseAndRender(markup,{cart:{items:[normalLine]},settings:{}}),/€99,29<small>per stuk<\/small>/);
});
await check('Real cart section renders box units with normal and discounted prices',async()=>{
  const markup=read('sections/main-cart-items.liquid').replace(/{%-?\s*style\s*-?%}[\s\S]*?{%-?\s*endstyle\s*-?%}/g,'').replace(/{%-?\s*schema\s*-?%}[\s\S]*?{%-?\s*endschema\s*-?%}/g,'');
  const context={cart:{items:[tileLine],item_count:3,total_price:29787},section:{id:'test',settings:{}},settings:{},routes:{}};
  for(const discounted of [false,true]){tileLine.original_price=discounted?10929:9929;const rendered=await engine.parseAndRender(markup,context);assert.match(rendered,/bc-cart-unit-label">per doos/);assert.doesNotMatch(rendered,/bc-cart-unit-label">per stuk/);}
  const normal=await engine.parseAndRender(markup,{...context,cart:{...context.cart,items:[normalLine]}});assert.match(normal,/bc-cart-unit-label">per stuk/);
});
await check('Cart uses confirmed tile lead times, escapes text and keeps neutral fallback',async()=>{
  const render=tiles=>engine.renderFile('bc-cart-delivery',{product:product(tiles)});
  assert.match(await render(tile),/Voorraadartikel.*Op voorraad bij leverancier/);
  assert.match(await render({...tile,order_type:'Bestelartikel',lead_time:'Ongeveer 12 werkdagen'}),/Bestelartikel.*Ongeveer 12 werkdagen/);
  assert.match(await render({...tile,lead_time:'<b>bron<\/b>'}),/&lt;b&gt;bron&lt;\/b&gt;/);
  assert.match(await render({m2_per_box:1.44}),/Levertijd op aanvraag/);
  assert.match(await engine.renderFile('bc-cart-delivery',{product:product(undefined,'Wiesbaden',true)}),/Op voorraad bij leverancier/);
});
console.log(JSON.stringify({status:'PASS',checks,scope:'Liquid rendering and real selection/calculation code with explicit fixtures; no browser, checkout, shipment or payment claim'},null,2));
