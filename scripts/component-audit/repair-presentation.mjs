import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {Liquid} from 'liquidjs';
import {Window} from 'happy-dom';

const args=Object.fromEntries(process.argv.slice(2).reduce((out,value,i,all)=>{if(i%2===0)out.push([value.slice(2),all[i+1]]);return out},[]));
if(!args.source||!args.manifest||!args.output)throw Error('Use --source, --manifest and --output');
const manifest=JSON.parse(fs.readFileSync(args.manifest,'utf8'));
const read=name=>{const bytes=fs.readFileSync(path.join(args.source,name));assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),manifest.files.find(f=>f.path===name)?.sha256,'Source '+name);return bytes.toString('utf8')};
const locale=JSON.parse(read('locales/nl.json').replace(/^\s*\/\*[\s\S]*?\*\//,''));
const engine=new Liquid();
engine.registerFilter('json',value=>JSON.stringify(value));
engine.registerFilter('money',value=>new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR'}).format(Number(value)/100));
engine.registerFilter('t',(key,...values)=>{let value=key.split('.').reduce((o,k)=>o?.[k],locale)||key;for(const [k,v]of values.filter(Array.isArray))value=value.replaceAll('{{ '+k+' }}',String(v));return value});
const clean=source=>source.replace(/{% doc %}[\s\S]*?{% enddoc %}/g,'');
const checks=[];
async function check(name,fn){await fn();checks.push(name)}
const snippet=clean(read('snippets/bc-card-tile-price.liquid'));
const tile=(patch={})=>({price_varies:false,selected_or_first_available_variant:{price:29489,unit_price:10995},metafields:{custom:{bron_toelichtingen_json:{value:{tiles:{m2_per_box:2.682,price_per_m2:{amount:109.95}}}}}},...patch});

await check('Tile JSON matches box area and actual selected unit price',async()=>{
 const result=JSON.parse(await engine.parseAndRender(snippet,{product:tile(),mode:'data'}));assert.deepEqual(result,{box_area:2.682,unit_price_cents:10995});
});
await check('Native tile label separates box and m² prices',async()=>{
 const text=await engine.parseAndRender(snippet,{product:tile()});assert.match(text,/per doos/);assert.match(text,/2,682 m²/);assert.match(text,/109,95/);assert.match(text,/per m²/);
});
await check('Native unit measurement is not duplicated by the tile label',async()=>{const p=tile();p.selected_or_first_available_variant.unit_price_measurement={reference_unit:'m²'};const text=await engine.parseAndRender(snippet,{product:p,mode:'native'});assert.match(text,/per doos/);assert.doesNotMatch(text,/109,95/)});
await check('No invented tile unit for non-tile or zero area',async()=>{
 for(const product of [{metafields:{}},tile({metafields:{custom:{bron_toelichtingen_json:{value:{tiles:{m2_per_box:0}}}}}})]){assert.equal((await engine.parseAndRender(snippet,{product})).trim(),'');assert.equal((await engine.parseAndRender(snippet,{product,mode:'data'})).trim(),'null')}
});
await check('Missing supplier price derives from box price and real box area',async()=>{
 const p=tile({selected_or_first_available_variant:{price:29489}});delete p.metafields.custom.bron_toelichtingen_json.value.tiles.price_per_m2;assert.equal(JSON.parse(await engine.parseAndRender(snippet,{product:p,mode:'data'})).unit_price_cents,10995);
});
await check('Variable product price avoids presenting a single native m² price',async()=>{const text=await engine.parseAndRender(snippet,{product:tile({price_varies:true})});assert.match(text,/per doos/);assert.doesNotMatch(text,/109,95/)});

const layout=read('layout/theme.liquid');
const seo=layout.slice(layout.indexOf("    {%- if request.page_type == 'collection' and page_description == blank -%}"),layout.indexOf("    {% render 'meta-tags'"));
await check('Empty collection SEO has escaped title-specific description',async()=>{
 const value=await engine.parseAndRender(seo,{request:{page_type:'collection'},page_description:'',collection:{title:'Kranen & onderdelen',description:'<style>private-selector{display:none}</style>'},shop:{name:'Badkamercity'}});assert.match(value,/name="description"/);assert.match(value,/Kranen &amp; onderdelen/);assert.doesNotMatch(value,/private-selector/);
});
await check('Existing SEO stays intact; non-collection gets no invented fallback',async()=>{
 const existing=await engine.parseAndRender(seo,{request:{page_type:'collection'},page_description:'Eigen omschrijving'});assert.match(existing,/Eigen omschrijving/);assert.doesNotMatch(await engine.parseAndRender(seo,{request:{page_type:'product'},page_description:''}),/meta name=/);
});
await check('Description is limited and passed explicitly to isolated meta snippet',async()=>{
 const text=await engine.parseAndRender(seo,{request:{page_type:'collection'},page_description:'',collection:{title:'Lang '.repeat(100)},shop:{name:'Badkamercity'}});const w=new Window();w.document.head.innerHTML=text;assert(w.document.querySelector('meta').content.length<=160);w.close();assert(layout.includes("render 'meta-tags', page_title: page_title, page_description: page_description"));
});
await check('Search USP has no 75-euro or same-day shipping promise',async()=>{
 const source=read('snippets/bc-search-usp-strip.liquid').replace(/{{-[\s\S]*?inline_asset_content\s*-}}/g,'');const text=await engine.parseAndRender(source);assert.match(text,/boven €100/);assert.match(text,/Levertijd per artikel/);assert.doesNotMatch(text,/€75|22:00|vandaag verzonden/);
});

const w=new Window({url:'https://fixture.invalid/products/tile'});w.eval(read('assets/bc-porcelanosa-core.js'));w.eval(read('assets/bc-porcelanosa-buybox.js'));
const box=w.document.createElement('bc-porcelanosa-buybox');
box.innerHTML='<input data-tile-area><select data-tile-waste><option value="0">Geen</option><option value="10" selected>10%</option></select><input data-tile-quantity type="number" value="1" min="1"><span data-tile-error></span><span data-tile-boxes></span><span data-tile-boxes-label></span><span data-tile-box-one>doos</span><span data-tile-box-many>dozen</span><span data-tile-required></span><span data-tile-supplied></span><span data-tile-total></span><span data-tile-unit-price></span><span data-tile-box-price></span><span data-tile-box-area></span><span data-tile-delivery-text></span><div data-tile-delivery></div><div data-tile-contact></div><input data-tile-property>';
box.area=box.querySelector('[data-tile-area]');box.waste=box.querySelector('[data-tile-waste]');box.quantity=box.querySelector('[data-tile-quantity]');box.submit=w.document.createElement('button');box.initialDisabled=false;box.core=w.BCPorcelanosa;box.number=new Intl.NumberFormat('nl-NL',{maximumFractionDigits:4});box.inputNumber=new Intl.NumberFormat('nl-NL',{useGrouping:false,maximumFractionDigits:4});box.money=new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR'});box.current={boxUnits:26820,priceCents:29489,unitPriceCents:10995};box.dataset.areaError='Vul een oppervlakte in';box.explicitArea=false;box.waste.value='10';
await check('Untouched empty area has neutral totals and disabled purchase',()=>{box.calculate();assert.equal(box.submit.disabled,true);assert.equal(box.querySelector('[data-tile-error]').hidden,true);assert.equal(box.area.getAttribute('aria-invalid'),'false');assert.equal(box.querySelector('[data-tile-total]').textContent,'—')});
await check('Entered surface uses real core, 10% waste and whole boxes',()=>{box.area.value='10';box.explicitArea=true;box.calculate();assert.equal(box.quantity.value,'5');assert.equal(box.submit.disabled,false);assert.equal(box.querySelector('[data-tile-supplied]').textContent,'13,41 m²');assert.equal(box.querySelector('[data-tile-required]').textContent,'11 m²')});
await check('Invalid edited area shows feedback and prevents buying',()=>{box.area.value='0';box.calculate();assert.equal(box.submit.disabled,true);assert.equal(box.querySelector('[data-tile-error]').hidden,false)});
await check('Default waste remains 10% and initial field is not a box-sized order',async()=>{const markup=read('snippets/bc-porcelanosa-buybox.liquid');assert.match(markup,/value="" placeholder="10" data-tile-area/);const select=markup.match(/<select[^>]*data-tile-waste[^>]*>[\s\S]*?<\/select>/)[0];const temp=new Window();temp.document.body.innerHTML=await engine.parseAndRender(select);assert.equal(temp.document.querySelector('option[selected]').value,'10');temp.close()});
await check('Manual whole boxes still work and do not add waste twice',()=>{box.boxInput=w.document.createElement('input');box.boxInput.value='3';box.boxMode=true;box.calculate();assert.equal(box.quantity.value,'3');assert.equal(box.waste.value,'0');assert.equal(box.area.value,'8,046');assert.equal(box.submit.disabled,false)});
await check('Invalid manual box quantity cannot preserve a stale total',()=>{box.boxInput.value='0';box.calculate();assert.equal(box.submit.disabled,true);assert.equal(box.querySelector('[data-tile-total]').textContent,'—');assert.equal(box.boxInput.getAttribute('aria-invalid'),'true')});
await w.happyDOM.abort();w.close();

await check('Footer only exposes real link destinations outside Theme Editor',async()=>{
 let source=read('sections/footer.liquid');const start=source.indexOf('                {% assign footer_link_url');source=source.slice(start,source.indexOf('\n              {% endif %}',start));source=source.replace("{% render 'bc-returns-url' %}",'{{ resolved_return_url }}');
 const blank=await engine.parseAndRender(source,{block:{settings:{label:'Showroom',url:''}},request:{design_mode:false}});assert.doesNotMatch(blank,/<li|Showroom/);
 const live=await engine.parseAndRender(source,{block:{settings:{label:'Retour aanmelden',url:'/pages/retour-aanmelden'}},request:{design_mode:false},resolved_return_url:'/pages/retour-aanmelden'});assert.match(live,/href="\/pages\/retour-aanmelden"/);
 const editor=await engine.parseAndRender(source,{block:{settings:{label:'Voorbeeld',url:''}},request:{design_mode:true},section:{settings:{example_label:'Vul bestemming in'}}});assert.match(editor,/Voorbeeld/);
});
await check('Footer brand directory configured; removed address remains empty',()=>{
 const data=JSON.parse(read('sections/footer-group.json').replace(/^\s*\/\*[\s\S]*?\*\//,''));const footer=Object.values(data.sections)[0];assert.equal(footer.settings.contact_address,'');assert.equal(Object.values(footer.blocks).find(b=>b.settings.label==='Onze merken').settings.url,'/collections?view=merken');
});
const result={status:'PASS',method:'Offline LiquidJS with explicit translation/money fixtures; real tile core and buybox method in happy-dom. No browser/server/cart/email claim.',checks,sourceManifest:path.basename(args.manifest)};fs.writeFileSync(args.output,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.status,checks:checks.length}));
