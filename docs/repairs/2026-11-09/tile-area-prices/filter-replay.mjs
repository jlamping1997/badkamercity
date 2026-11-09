import fs from 'node:fs';
import assert from 'node:assert/strict';
import {Window} from 'happy-dom';
import {Liquid} from 'liquidjs';

const theme = new URL('../../../../shopify/current/', import.meta.url);
const js = fs.readFileSync(new URL('assets/bc-external-filters.js', theme), 'utf8');
const oldSpecs = fs.readFileSync(new URL('../../2026-11-08/mobile-product-list/rollback/snippets/bc-card-specs.liquid', import.meta.url), 'utf8');
const newSpecs = fs.readFileSync(new URL('snippets/bc-card-specs.liquid', theme), 'utf8');
const labels = {'products.product.card_type':'Productsoort','products.product.card_sku':'Artikelnummer','products.product.card_mounting':'Montage','products.product.card_material':'Materiaal','products.product.card_colour':'Kleur'};
const liquid = new Liquid();
liquid.registerTag('doc', {parse(token, remaining) {while(remaining.length && remaining.shift().getText() !== '{% enddoc %}') {}}, render() {return '';}});
liquid.registerFilter('t', key => labels[key] || key);
liquid.registerFilter('json', value => JSON.stringify(value ?? null));
const results=[];
const products=[
  {vendor:'Wiesbaden',type:'Onderkast',variants:[{sku:'38.4054'}],metafields:{}},
  {vendor:'Demo',type:'Kraan',variants:[{sku:'ABC'}],metafields:{bc_data:{filter_manifest:{value:{format:'verified-product-filters-v1',sku:'ABC',values:{kraanmontage:'Wand',kleur:'Chroom'}}}}}},
  {vendor:'Demo',type:'Kraan',variants:[{sku:'ABC'}],metafields:{bc_data:{filter_manifest:{value:{format:'verified-product-filters-v1',sku:'WRONG',values:{materiaal:'Onjuist',kleur:'Onjuist'}}}}}},
  {vendor:'Demo',type:'',variants:[{sku:''}],metafields:{}},
  {vendor:'JEE-O',type:'Wastafel',variants:[{sku:'J1'}],metafields:{custom:{color_variants:{value:['A','B']},kleur:{value:'Zand'}}}},
  {vendor:'Demo',type:'</script><img src=x onerror=alert(1)>',variants:[{sku:'<svg onload=alert(1)>'}],metafields:{}}
];
for (let i=0;i<products.length;i++) {
  const product=products[i];
  const before=(await liquid.parseAndRender(oldSpecs,{product})).trim();
  const after=(await liquid.parseAndRender(newSpecs,{product})).trim();
  assert.equal(after,before,'Existing HTML contract changed');
  const data=await liquid.parseAndRender(newSpecs,{product,mode:'data'});
  const specs=JSON.parse(data);
  assert(specs.length<=2);
  assert(!data.includes('</script>'));
  if(i===1) assert.deepEqual(specs,[{label:'Montage',value:'Wand'},{label:'Kleur',value:'Chroom'}]);
  if(i===2) assert.deepEqual(specs,[{label:'Productsoort',value:'Kraan'},{label:'Artikelnummer',value:'ABC'}]);
  if(i===3) assert.deepEqual(specs,[]);
  if(i===4) assert.equal(specs[1].value,'Zand');
  results.push({test:'liquid-html-and-json-'+i,result:'PASS'});
}

async function replay(specs,{search=false,wrongId=false,tile=false,failedHydration=false}={}) {
  const w=new Window({url:'https://test.invalid/'+(search?'search?q=demo':'collections/demo'),width:390,height:844});
  Object.defineProperty(w.document,'readyState',{configurable:true,value:'complete'});
  w.ResizeObserver=class {observe(){} disconnect(){}};
  w.IntersectionObserver=class {observe(){} disconnect(){}};
  const errors=[];w.console.error=(...a)=>errors.push(a.map(String).join(' '));
  w.Shopify={routes:{root:'/'}};
  w.document.documentElement.lang='nl';
  w.document.body.innerHTML=`<main id="MainContent"><section class="${search?'template-search':'bc-collection'}"><div id="BcExternalFilters" data-api-base="https://filters.invalid" data-collection="${search?'__all__':'demo'}" data-search-mode="${search}" data-products-count="1" data-card-data-section="bc-card-data" data-card-delivery="Op voorraad" data-temporary-in-stock="true" data-tax-included="true"></div><div class="facets-vertical page-width"><aside id="main-collection-filters"></aside><div id="ProductGridContainer"><ul id="product-grid" class="grid product-grid"><li>Native fallback</li></ul></div></div></section></main>`;
  const base={id:123,shopify_product_id:123,handle:'demo',title:'Wiesbaden Onderkast',vendor:'Wiesbaden',price_cents:82000,price_varies:false,image_url:''};
  const card={...base,id:wrongId?999:123,variant_id:789,available:true,can_add:true,color:'Mat zwart',delivery_text:'Leverancierlabel',delivery_in_stock:false,switcher_html:'',specs};
  if(tile)card.tile_price={box_area:1.2,unit_price_cents:68333};
  w.fetch=async input=>{
    const url=String(input);
    if(url.startsWith('https://filters.invalid/'))return {ok:true,json:async()=>({products:[base],facets:[],found:1,collection:{handle:search?'__all__':'demo',profile_products:1}})};
    if(url.includes('/products/demo?sections=bc-card-data'))return {ok:!failedHydration,json:async()=>({'bc-card-data':`<script type="application/json" data-bc-card-data>${JSON.stringify(card).replaceAll('<','\\u003c')}</script>`})};
    throw new Error('Unstubbed fetch '+url);
  };
  w.eval(js);
  for(let i=0;i<18;i++)await new Promise(resolve=>setImmediate(resolve));
  assert.deepEqual(errors,[]);
  const cardEl=w.document.querySelector('.bc-filter-card');assert(cardEl,'Card failed to render');
  const list=cardEl.querySelector('[data-bc-card-specs]');assert(list);
  assert.equal(list.classList.contains('bc-card-specs--mobile'),true);
  if(wrongId||failedHydration){assert(list.hidden);assert(cardEl.querySelector('[data-bc-card-cart]').disabled);}
  else {
    assert.equal(list.querySelectorAll('img,svg,script').length,0);
    assert.equal(cardEl.querySelector('[data-bc-card-cart]').disabled,false);
    assert.equal(cardEl.querySelector('.bc-card-delivery').textContent,'Op voorraad');
    assert(cardEl.querySelector('.bc-card-delivery').classList.contains('bc-card-delivery--stock'));
    assert.equal(cardEl.querySelector('.bc-filter-card__title a').href,'https://test.invalid/products/demo');
    assert.match(cardEl.querySelector('.bc-filter-card__price').textContent,tile ? /683,33.*per m²/ : /820,00/);
    assert.equal(list.childElementCount,Array.isArray(specs)?specs.slice(0,2).filter(s=>typeof s?.label==='string'&&typeof s.value==='string'&&s.value.trim()).length:0);
    assert.equal(list.hidden,!list.childElementCount);
    if(tile){assert.equal(cardEl.querySelectorAll('.bc-card-unit').length,0);assert(!cardEl.querySelector('.bc-filter-card__price').textContent.includes('820,00'));}
  }
  await w.happyDOM.abort();w.close();
}
const cases=[
  {specs:[{label:'Materiaal',value:'Eiken'},{label:'Kleur',value:'Mat zwart'}]},
  {specs:[]},
  {specs:undefined},
  {specs:null},
  {specs:[{label:'A',value:''},{label:'B',value:{bad:true}}]},
  {specs:[{label:'<script>',value:'<img src=x onerror=alert(1)>'}]},
  {specs:[{label:'A',value:'1'},{label:'B',value:'2'},{label:'C',value:'3'}]},
  {specs:[{label:'A',value:'1'}],options:{wrongId:true}},
  {specs:[{label:'A',value:'1'}],options:{failedHydration:true}},
  {specs:[{label:'Doos',value:'1,2 m²'}],options:{tile:true}}
];
for(let i=0;i<cases.length;i++)for(const search of [false,true]) {
  await replay(cases[i].specs,{...cases[i].options,search});
  results.push({test:'real-filter-js-'+i+'-'+(search?'search':'collection'),result:'PASS'});
}
fs.writeFileSync(new URL('./filter-contract-results.json',import.meta.url),JSON.stringify({status:'PASS',tests:results.length,results,scope:'Offline real Liquid and full filter JS with synthetic data. Not browser layout, live network, real SKU/color switching or purchase proof.'},null,2)+'\n');
console.log(results.length+' contract checks PASS');
