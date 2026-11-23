import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {Window} from 'happy-dom';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const read=name=>fs.readFileSync(path.join(root,'shopify/current',name),'utf8');
const colorMarkup=read('snippets/bc-porcelanosa-buybox.liquid').match(/<fieldset class="bc-tile__field" data-tile-field="color">[\s\S]*?<\/fieldset>/)[0];
const colors=['Blanc','Caramel','Cognac','Cuivre','Gris','Mix','Or','Perle','Petrol','Taupe','Vert'];
const windows=[];
const checks=[];
function fixture({selected='Perle',layout='expandable_grid',values=colors,saved}={}){
  const w=new Window({url:'https://fixture.invalid/products/tile'});windows.push(w);
  const products=values.map((color,i)=>({id:String(i+1),variant:String(i+101),sku:'SKU'+i,handle:'tile-'+i,title:'Tile '+color,type:'Vloertegel',color,finish:'Mat',size:'60 x 60 cm',thickness:10,area:3600,boxUnits:14400,priceCents:9929,unitPriceCents:6895,leadTime:'Op voorraad bij leverancier',orderType:'Voorraadartikel',image:'https://cdn.shopify.com/'+i+'.jpg'}));
  const current=products.find(p=>p.color===selected)||products[0];
  if(saved!==undefined)w.sessionStorage.setItem('bc-tile-colors:v1:fixture',saved);
  w.eval(read('assets/bc-porcelanosa-core.js'));w.eval(read('assets/bc-porcelanosa-buybox.js'));
  const page=w.document.createElement('product-info');page.innerHTML='<form id="fixture-form"><button type="submit">Bestellen</button></form>';
  const box=w.document.createElement('bc-porcelanosa-buybox');
  Object.assign(box.dataset,{form:'fixture-form',group:'fixture',productId:current.id,sku:current.sku,boxUnits:'14400',priceCents:'9929',unitPriceCents:'6895',currency:'EUR',colorLayout:layout,labelAllColors:'Bekijk alle __COUNT__ kleuren',labelLessColors:'Minder kleuren',areaError:'Ongeldige oppervlakte',boxError:'Ongeldig aantal'});
  const color=colorMarkup.replace(/{{[\s\S]*?}}/g,tag=>tag.includes('section.id')?'fixture':tag.includes('product.id')?current.id:tag.includes('bc_tiles.color')?'Kleur':current.color);
  box.innerHTML='<script type="application/json" data-tile-catalog>'+JSON.stringify({schema:1,group:'fixture',products})+'</script><div data-tile-choices>'+['type','color','finish','size','thickness'].map(field=>field==='color'?color:'<fieldset data-tile-field="'+field+'"><div data-tile-options></div></fieldset>').join('')+'</div><p data-tile-fixed-choices></p><p data-tile-choice-status></p><div data-tile-calculator hidden></div><div data-tile-manual></div><input data-tile-area value="1,44"><select data-tile-waste><option value="0">Geen</option><option value="10">10%</option></select><input data-tile-quantity value="1"><input data-tile-box-input value="1"><span data-tile-error></span><span data-tile-box-one>doos</span><span data-tile-box-many>dozen</span><span data-tile-boxes></span><span data-tile-boxes-label></span><span data-tile-required></span><span data-tile-supplied></span><span data-tile-total></span><span data-tile-unit-price></span><span data-tile-box-price></span><span data-tile-box-area></span><span data-tile-delivery-text></span><div data-tile-delivery></div><div data-tile-contact></div><input data-tile-property>';
  page.append(box);w.document.body.append(page);
  return {w,box,buttons:()=>[...box.querySelectorAll('.bc-tile__color')],visible:()=>[...box.querySelectorAll('.bc-tile__color')].filter(b=>!b.hidden),toggle:box.querySelector('[data-tile-colors-toggle]')};
}
async function check(name,run){await run();checks.push(name);}
await check('Collapsed grid shows exactly four square-image choices including a later selected color',()=>{
  const f=fixture();assert.deepEqual(f.visible().map(b=>b.dataset.choice),['Blanc','Caramel','Cognac','Perle']);assert.equal(f.toggle.getAttribute('aria-expanded'),'false');assert.equal(f.toggle.querySelector('[data-tile-colors-label]').textContent,'Bekijk alle 11 kleuren');assert.equal(f.toggle.querySelector('[data-tile-colors-count]').textContent,'+7');assert.equal(f.box.querySelector('.bc-tile__scroll-track'),null);assert(f.visible().every(b=>b.querySelector('img')));assert.equal(f.toggle.getAttribute('aria-controls'),f.box.querySelector('.bc-tile__colors').id);
});
await check('Expand exposes all eleven in source order and collapse restores four with selected color',()=>{
  const f=fixture();f.toggle.click();assert.equal(f.visible().length,11);assert.equal(f.toggle.getAttribute('aria-expanded'),'true');assert.equal(f.toggle.querySelector('[data-tile-colors-label]').textContent,'Minder kleuren');assert.equal(f.toggle.querySelector('[data-tile-colors-count]').hidden,true);f.toggle.click();assert.equal(f.visible().length,4);assert.equal(f.visible().at(-1).dataset.choice,'Perle');assert.equal(f.w.document.activeElement,f.toggle);
});
await check('Open state survives a product change within the same series and changes back when collapsed',()=>{
  const a=fixture();a.toggle.click();const stored=a.w.sessionStorage.getItem('bc-tile-colors:v1:fixture');const b=fixture({selected:'Vert',saved:stored});assert.equal(b.visible().length,11);b.toggle.click();assert.equal(b.visible().length,4);assert.equal(b.visible().at(-1).dataset.choice,'Vert');assert.equal(b.w.sessionStorage.getItem('bc-tile-colors:v1:fixture'),'false');
});
await check('Four or fewer colors have no disclosure button; one color stays a fixed choice',()=>{
  const f=fixture({values:colors.slice(0,4),selected:'Blanc'});assert.equal(f.visible().length,4);assert.equal(f.toggle.hidden,true);const one=fixture({values:['Blanc'],selected:'Blanc'});assert.equal(one.box.querySelector('[data-tile-field="color"]').hidden,true);
});
await check('Existing unconfigured tile groups keep their horizontal rail and full choices',()=>{
  const f=fixture({layout:'rail'});assert.equal(f.buttons().length,11);assert.equal(f.visible().length,11);assert(f.box.querySelector('.bc-tile__scroll-track'));assert.equal(f.toggle.hidden,true);
});
await check('Toggling colors does not change the box calculation or form quantity',()=>{
  const f=fixture();const input=f.box.querySelector('[data-tile-area]');input.value='10';input.dispatchEvent(new f.w.Event('input',{bubbles:true}));const waste=f.box.querySelector('[data-tile-waste]');waste.value='10';waste.dispatchEvent(new f.w.Event('change',{bubbles:true}));f.toggle.click();f.toggle.click();assert.equal(f.box.querySelector('[data-tile-quantity]').value,'8');assert.match(f.box.querySelector('[data-tile-total]').textContent,/794,32/);
});
for(const w of windows){await w.happyDOM.abort();w.close();}
console.log(JSON.stringify({status:'PASS',checks,scope:'Real color-field Liquid markup and buybox JS lifecycle in happy-dom; layout and real product navigation are browser checks.'},null,2));
