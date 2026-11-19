import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {fileURLToPath,pathToFileURL} from 'node:url';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const require=createRequire(import.meta.url);
const core=require(path.join(root,'shopify/current/assets/bc-porcelanosa-core.js'));
const dependencyRequire=createRequire(path.join(root,'scripts/component-audit/package.json'));
const {Window}=await import(pathToFileURL(dependencyRequire.resolve('happy-dom')).href);
const file=process.argv[2];
if(!file)throw new Error('Usage: node scripts/cottoceramix/audit_unit_plan.mjs PRIVATE_PRODUCTS_JSON');
const rows=JSON.parse(fs.readFileSync(file,'utf8'));
const source=name=>fs.readFileSync(path.join(root,'shopify/current',name),'utf8');
const colorMarkup=source('snippets/bc-porcelanosa-buybox.liquid').match(/<fieldset class="bc-tile__field" data-tile-field="color">[\s\S]*?<\/fieldset>/)[0];
const entries=rows.map((row,index)=>{
  const mf=Object.fromEntries(row.input.metafields.map(m=>[m.namespace+'.'+m.key,m.value]));
  const tile=JSON.parse(mf['custom.bron_toelichtingen_json']).tiles;
  assert.equal(tile.order_mode,'unit');assert.equal(row.input.status,'DRAFT');
  assert.equal(row.publishable_after_readback,false);assert(row.requires_unit_renderer_publication);
  assert(!('unitPriceMeasurement'in row.input.variants[0]));assert.equal(row.input.variants[0].showUnitPrice,false);
  for(const field of ['m2_per_box','price_per_m2','price_per_box','pieces_per_box'])assert(!(field in tile));
  const product={id:String(index+1),variant:String(index+10001),sku:row.sku,handle:row.input.handle,title:row.input.title,
    type:mf['tiles.application']||row.input.productType,color:mf['tiles.color']||null,
    finish:(mf['tiles.execution']||'').split(' · ').filter(v=>!v.includes(' mm')).join(' · '),
    size:mf['tiles.size']||null,thickness:Number(mf['bc_filters.tegel_dikte_mm']||0),
    area:Number(mf['bc_filters.tegel_breedte_mm']||0)*Number(mf['bc_filters.tegel_lengte_mm']||0)/100,
    orderMode:'unit',saleUnit:tile.sale_unit,unitCount:tile.unit_count,
    priceCents:Math.round(Number(row.input.variants[0].price)*100),
    unitPriceCents:Math.round(Number(row.input.variants[0].price)*100),
    leadTime:tile.lead_time,orderType:tile.order_type,
    image:'https://cdn.shopify.com/fixture/'+encodeURIComponent(row.sku)+'.jpg'};
  const multiplier=tile.source.source_price_basis==='per_piece'?product.unitCount:1;
  assert.equal(product.priceCents,Math.round(Number(tile.source.source_price)*100)*multiplier,row.sku+': source price reconciles');
  return {row,mf,tile,product};
});
const groups=new Map();
for(const e of entries){if(!groups.has(e.row.group_key))groups.set(e.row.group_key,[]);groups.get(e.row.group_key).push(e.product);}
let choiceChecks=0;
for(const [key,products]of groups){
  assert(products.length<=50,key+': renderer limit');
  assert.equal(new Set(products.map(p=>p.saleUnit+':'+p.unitCount)).size,1,key+': native unit stays fixed');
  assert.equal(new Set(products.map(p=>JSON.stringify(core.fields.map(f=>p[f])))).size,products.length,key+': unique runtime vectors');
  for(const current of products)for(const field of core.fields)for(const option of core.choices(products,current,field)){
    const result=core.choose(products,current,field,option[field]);assert(products.includes(result));
    assert.equal(String(result[field]),String(option[field]));
    for(const other of core.fields.filter(f=>f!==field))assert.equal(String(result[other]),String(current[other]),key+': another choice changed');
    choiceChecks++;
  }
}
const calcWindow=new Window({url:'https://fixture.invalid/products/tile'});
calcWindow.eval(source('assets/bc-porcelanosa-core.js'));calcWindow.eval(source('assets/bc-porcelanosa-buybox.js'));
const unitResult=calcWindow.customElements.get('bc-porcelanosa-buybox').prototype.unitResult;
let calculationChecks=0,invalidQuantityChecks=0;
for(const {product}of entries){
  for(const quantity of [1,2,3]){
    const result=unitResult.call({current:product},quantity);
    assert(result);assert.equal(result.quantity,quantity);assert.equal(result.pieces,quantity*product.unitCount);assert.equal(result.total,quantity*product.priceCents);calculationChecks++;
  }
  for(const value of ['',0,-1,'1.5','2,5','2147483648']){assert.equal(unitResult.call({current:product},value),null);invalidQuantityChecks++;}
}
await calcWindow.happyDOM.abort();calcWindow.close();

const picked=['VV0906','CB1801','FGB323M','WY1305'].map(sku=>entries.find(e=>e.product.sku===sku)).filter(Boolean);
const unknown=entries.find(e=>!e.product.color);if(unknown&&!picked.includes(unknown))picked.push(unknown);
const runtimeChecks=[];
for(const {row,mf,product}of picked){
  const w=new Window({url:'https://fixture.invalid/products/tile'});w.document.documentElement.lang='nl-NL';
  w.eval(source('assets/bc-porcelanosa-core.js'));w.eval(source('assets/bc-porcelanosa-buybox.js'));
  const page=w.document.createElement('product-info');page.innerHTML='<form id="fixture-form"><button type="submit">Bestellen</button></form>';
  const box=w.document.createElement('bc-porcelanosa-buybox');
  Object.assign(box.dataset,{form:'fixture-form',group:'fixture',productId:product.id,sku:product.sku,
    orderMode:'unit',saleUnit:product.saleUnit,unitCount:String(product.unitCount),priceCents:String(product.priceCents),
    currency:'EUR',colorLayout:'expandable_grid',leadTime:product.leadTime,orderType:product.orderType,
    labelAllColors:'Bekijk alle __COUNT__ kleuren',labelLessColors:'Minder kleuren',
    piecesOne:'__COUNT__ stuk',piecesMany:'__COUNT__ stuks',unitError:'Ongeldig aantal',choiceError:'Keuze kon niet worden geladen'});
  const color=colorMarkup.replace(/{{[\s\S]*?}}/g,tag=>tag.includes('section.id')?'fixture':tag.includes('product.id')?product.id:tag.includes('bc_tiles.color')?'Kleur':product.color||'');
  const catalog=groups.get(row.group_key);
  box.innerHTML='<script type="application/json" data-tile-catalog>'+JSON.stringify({schema:1,group:'fixture',products:catalog})+'</script><div data-tile-choices>'+core.fields.map(field=>field==='color'?color:'<fieldset data-tile-field="'+field+'"><div data-tile-options></div></fieldset>').join('')+'</div><p data-tile-fixed-choices></p><p data-tile-choice-status hidden></p><input type="number" name="quantity" form="fixture-form" value="1" data-unit-quantity><button type="button" data-unit-step="-1">−</button><button type="button" data-unit-step="1">+</button><span data-tile-error hidden></span><span data-unit-received></span><span data-tile-total></span><span data-tile-unit-price></span><span data-tile-delivery-text></span><div data-tile-delivery></div>';
  box.querySelector('[data-tile-fixed-choices]').textContent=[mf['tiles.application'],mf['tiles.color'],mf['tiles.execution'],mf['tiles.size']].filter(Boolean).join(' · ');
  page.append(box);w.document.body.append(page);
  assert.equal(box.querySelector('[data-tile-choice-status]').hidden,true,product.sku+': choices loaded');
  assert.equal(box.querySelector('[data-tile-area]'),null);assert.equal(box.querySelector('[data-tile-property]'),null);
  const quantity=box.querySelector('[data-unit-quantity]');quantity.value='2';quantity.dispatchEvent(new w.Event('input',{bubbles:true}));
  assert.equal(quantity.value,'2');assert.equal(box.unitResult(quantity.value).total,2*product.priceCents);
  assert.equal(box.querySelector('[data-unit-received]').textContent,String(2*product.unitCount)+' stuks');
  assert.equal(page.querySelector('[type=submit]').disabled,false);
  const count=catalog.length;
  if(count>4){const toggle=box.querySelector('[data-tile-colors-toggle]');toggle.click();assert.equal([...box.querySelectorAll('[data-tile-field="color"] button[data-choice]')].filter(b=>!b.hidden).length,count);toggle.click();}
  const expectedLead=[product.orderType,product.leadTime].filter(Boolean).join(' · ');
  assert.equal(box.querySelector('[data-tile-delivery-text]').textContent,expectedLead);
  runtimeChecks.push({sku:product.sku,saleUnit:product.saleUnit,unitCount:product.unitCount,
    quantity:2,receivedPieces:2*product.unitCount,totalCents:2*product.priceCents,colors:count,delivery:expectedLead});
  await w.happyDOM.abort();w.close();
}
console.log(JSON.stringify({status:'PASS',products:entries.length,groups:groups.size,choiceChecks,
  calculationChecks,invalidQuantityChecks,runtimeChecks,
  scope:'Actual local select core and unitResult across every planned unit article, plus full happy-dom component fixtures. CDN fixture URLs test host handling only. No real browser, media-ready, cart, shipping or checkout claim.'},null,2));
