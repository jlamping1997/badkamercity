import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {fileURLToPath, pathToFileURL} from 'node:url';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const require=createRequire(import.meta.url);
const core=require(path.join(root,'shopify/current/assets/bc-porcelanosa-core.js'));
const dependencyRequire=createRequire(path.join(root,'scripts/component-audit/package.json'));
const {Window}=await import(pathToFileURL(dependencyRequire.resolve('happy-dom')).href);
const input=process.argv[2];
if(!input)throw new Error('Usage: node scripts/cottoceramix/audit_optional_m2.mjs PRIVATE_PRODUCTS_JSON');
const rows=JSON.parse(fs.readFileSync(input,'utf8'));
const source=name=>fs.readFileSync(path.join(root,'shopify/current',name),'utf8');
const colorMarkup=source('snippets/bc-porcelanosa-buybox.liquid').match(/<fieldset class="bc-tile__field" data-tile-field="color">[\s\S]*?<\/fieldset>/)[0];
const serialized=rows.map((row,index)=>{
  const mf=Object.fromEntries(row.input.metafields.map(m=>[m.namespace+'.'+m.key,m.value]));
  const tile=JSON.parse(mf['custom.bron_toelichtingen_json']).tiles;
  const product={id:String(index+1),variant:String(index+10001),sku:row.sku,handle:row.input.handle,title:row.input.title,
    type:mf['tiles.application']||row.input.productType,color:mf['tiles.color']||null,
    finish:(mf['tiles.execution']||'').split(' · ').filter(value=>!value.includes(' mm')).join(' · '),
    size:mf['tiles.size']||null,thickness:Number(mf['bc_filters.tegel_dikte_mm']||0),
    area:Number(mf['bc_filters.tegel_breedte_mm']||0)*Number(mf['bc_filters.tegel_lengte_mm']||0)/100,
    boxUnits:Math.round(tile.m2_per_box*10000),priceCents:Math.round(Number(row.input.variants[0].price)*100),
    unitPriceCents:Math.round(Number(tile.price_per_m2.amount)*100),leadTime:tile.lead_time,
    // Liquid serializes imported Shopify media, not originalSource supplier URLs.
    // This fixture URL tests host validation only; media readiness is an Admin gate.
    orderType:tile.order_type,image:'https://cdn.shopify.com/fixture/'+encodeURIComponent(row.sku)+'.jpg'};
  return {row,mf,tile,product};
});
let choiceChecks=0,calculationChecks=0;
for(const {row,product}of serialized){
  assert.equal(row.group_key,'optional-singleton|'+row.sku);
  for(const field of core.fields){
    const options=core.choices([product],product,field);
    assert.equal(options.length,1,row.sku+': singleton choices');
    assert.equal(core.choose([product],product,field,options[0][field]),product,row.sku+': exact singleton destination');
    choiceChecks++;
  }
  const result=core.calculate('2.1',10,product.boxUnits,product.priceCents);
  assert(result,row.sku+': calculator result');
  assert.equal(result.boxes,Math.ceil(21000*110/(product.boxUnits*100)));
  assert.equal(result.total,result.boxes*product.priceCents);
  calculationChecks++;
}

const representatives=new Map();
for(const entry of serialized){
  for(const field of ['color','finish','size'])if(!entry.product[field]&&!representatives.has(field))representatives.set(field,entry);
  if(!entry.product.thickness&&!representatives.has('thickness'))representatives.set('thickness',entry);
  if(!entry.mf['custom.serie']&&!representatives.has('series'))representatives.set('series',entry);
}
const runtimeChecks=[];
for(const [missing,{mf,product}]of representatives){
  const w=new Window({url:'https://fixture.invalid/products/tile'});
  w.document.documentElement.lang='nl-NL';
  w.eval(source('assets/bc-porcelanosa-core.js'));w.eval(source('assets/bc-porcelanosa-buybox.js'));
  const page=w.document.createElement('product-info');
  page.innerHTML='<form id="fixture-form"><button type="submit">Bestellen</button></form>';
  const box=w.document.createElement('bc-porcelanosa-buybox');
  Object.assign(box.dataset,{form:'fixture-form',group:'fixture',productId:product.id,sku:product.sku,
    boxUnits:String(product.boxUnits),priceCents:String(product.priceCents),unitPriceCents:String(product.unitPriceCents),
    currency:'EUR',colorLayout:'expandable_grid',leadTime:product.leadTime,orderType:product.orderType,
    labelAllColors:'Bekijk alle __COUNT__ kleuren',labelLessColors:'Minder kleuren',
    areaError:'Ongeldige oppervlakte',boxError:'Ongeldig aantal',choiceError:'Keuze kon niet worden geladen'});
  const color=colorMarkup.replace(/{{[\s\S]*?}}/g,tag=>tag.includes('section.id')?'fixture':tag.includes('product.id')?product.id:tag.includes('bc_tiles.color')?'Kleur':product.color||'');
  box.innerHTML='<script type="application/json" data-tile-catalog>'+JSON.stringify({schema:1,group:'fixture',products:[product]})+'</script><div data-tile-choices>'+core.fields.map(field=>field==='color'?color:'<fieldset data-tile-field="'+field+'"><div data-tile-options></div></fieldset>').join('')+'</div><p data-tile-fixed-choices></p><p data-tile-choice-status hidden></p><div data-tile-calculator hidden></div><div data-tile-manual></div><input data-tile-area value="1"><select data-tile-waste><option value="0">Geen</option><option value="10">10%</option></select><input data-tile-quantity value="1"><input data-tile-box-input value="1"><span data-tile-error></span><span data-tile-box-one>doos</span><span data-tile-box-many>dozen</span><span data-tile-boxes></span><span data-tile-boxes-label></span><span data-tile-required></span><span data-tile-supplied></span><span data-tile-total></span><span data-tile-unit-price></span><span data-tile-box-price></span><span data-tile-box-area></span><span data-tile-delivery-text></span><div data-tile-delivery></div><div data-tile-contact></div><input data-tile-property>';
  const fixed=[mf['tiles.application'],mf['tiles.color'],mf['tiles.execution'],mf['tiles.size']].filter(Boolean).join(' · ');
  box.querySelector('[data-tile-fixed-choices]').textContent=fixed;
  page.append(box);w.document.body.append(page);
  assert.equal(box.querySelector('[data-tile-choice-status]').hidden,true,missing+': no load error');
  assert.equal(box.querySelector('[data-tile-choices]').hidden,true,missing+': no synthetic choice menu');
  assert.equal(box.querySelector('[data-tile-fixed-choices]').hidden,false,missing+': factual fixed summary visible');
  assert(!/null|undefined|None/.test(box.querySelector('[data-tile-fixed-choices]').textContent),missing+': no unknown labels');
  const area=box.querySelector('[data-tile-area]');area.value='2,1';area.dispatchEvent(new w.Event('input',{bubbles:true}));
  const waste=box.querySelector('[data-tile-waste]');waste.value='10';waste.dispatchEvent(new w.Event('change',{bubbles:true}));
  const expected=core.calculate('2.1',10,product.boxUnits,product.priceCents);
  assert.equal(box.querySelector('[data-tile-quantity]').value,String(expected.boxes));
  assert.equal(box.querySelector('[data-tile-calculator]').hidden,false);
  assert.equal(page.querySelector('button[type=submit]').disabled,false);
  runtimeChecks.push({missing,sku:product.sku,fixedSummary:fixed,boxes:expected.boxes});
  await w.happyDOM.abort();w.close();
}
console.log(JSON.stringify({status:'PASS',products:rows.length,choiceChecks,calculationChecks,runtimeChecks,
  scope:'Actual local selection core and buybox lifecycle in happy-dom with source-shaped singleton payloads. No browser, media-ready, shipping or checkout claim.'},null,2));
