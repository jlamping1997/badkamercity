import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
const require=createRequire(process.env.BC_TEST_DEPENDENCIES || new URL('package.json',import.meta.url));
const {Liquid}=require('liquidjs');
const {Window}=require('happy-dom');
const theme=new URL('../../../../shopify/current/',import.meta.url);
const file=path=>fs.readFileSync(new URL(path,theme),'utf8');
const results=[];
const record=name=>results.push({test:name,result:'PASS'});
const json=s=>JSON.parse(s.replace(/^\/\*[\s\S]*?\*\//,''));
const vendors=['Wiesbaden','THE MOSAIC FACTORY','Sunshower','Verlavio','Porcelanosa','Lagoo','JEE-O','Hotbath','Cottoceramix','BadkamerCity Test'];
const translations=json(file('locales/nl.json'));
const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;').replaceAll('>','&gt;');
async function render({mode='directory',settings={},list=vendors,collections={cottoceramix:{url:'/collections/cottoceramix'}},locale='/collections',source='helper'}={}) {
 const globals={shop:{vendors:list},settings,collections,routes:{collections_url:locale}};
 const e=new Liquid({root:new URL('snippets/',theme).pathname,extname:'.liquid',globals});
 e.registerTag('doc',{parse(token,tokens){while(tokens.length&&tokens.shift().getText()!=='{% enddoc %}'){}},render(){return '';}});
 e.registerTag('schema',{parse(token,tokens){while(tokens.length&&tokens.shift().getText()!=='{% endschema %}'){}},render(){return '';}});
 e.registerFilter('handleize',s=>String(s).toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''));
 e.registerFilter('asset_url',s=>'/assets/'+s);e.registerFilter('stylesheet_tag',s=>'<link rel="stylesheet" href="'+s+'">');
 e.registerFilter('t',key=>key.split('.').reduce((v,k)=>v?.[k],translations)||key);
 e.registerFilter('image_url',(image,...args)=>image.src+'?width=360');
 e.registerFilter('image_tag',(src,...args)=>{
  const opts=Object.fromEntries(args.filter(Array.isArray));
  return '<img src="'+escape(src)+'" alt="'+escape(opts.alt||'')+'" class="'+escape(opts.class||'')+'">';
 });
 let sourceText=file('snippets/bc-brand-items.liquid'),context={mode};
 if(source==='directory'){sourceText=file('sections/bc-brand-directory.liquid');context={section:{settings:{heading:'Onze merken'}}};}
 if(source==='home'){sourceText=file('sections/bc-homepage.liquid').match(/<section class="[^"]*\bbch-brands\b[^"]*"[\s\S]*?<\/section>/)[0];context={section:{id:'test',settings:{brands_heading:'Jouw favoriete merken',brands_label:'Alle merken',brands_link:'/collections?view=merken'}}};}
 const html=await e.parseAndRender(sourceText,context),w=new Window();w.document.body.innerHTML=html;
 const items=[...w.document.querySelectorAll('[data-bc-brand]')];
 const data=items.map(li=>({key:li.dataset.bcBrand,name:li.textContent.trim(),href:li.querySelector('a').getAttribute('href')}));
 return {html,w,data};
}
let r=await render();assert.equal(r.data.length,9);assert.equal(r.data[0].key,'cottoceramix');assert.equal(r.data.at(-1).key,'wiesbaden');assert(!r.html.toLowerCase().includes('badkamercity test'));assert.equal(r.data.find(i=>i.key==='cottoceramix').href,'/collections/cottoceramix');record('all-nine-real-brands-alphabetical-test-brand-excluded');r.w.close();
r=await render({mode:'slider'});assert.deepEqual(r.data.slice(0,4).map(i=>i.key),['hotbath','wiesbaden','jee-o','sunshower']);assert.equal(r.data.length,9);record('homepage-keeps-four-priority-brands-and-adds-rest');r.w.close();
r=await render({mode:'slider',settings:{bc_brand_home_order:' Verlavio, HOTBATH, Verlavio, ontbreekt, BadkamerCity Test '},list:[...vendors,'hotbath']});assert.deepEqual(r.data.slice(0,2).map(i=>i.key),['verlavio','hotbath']);assert.equal(r.data.length,9);record('priority-whitespace-case-duplicates-and-unknown-names');r.w.close();
r=await render({list:[...vendors,'Nieuw Merk']});assert.equal(r.data.length,10);assert(r.data.some(i=>i.key==='nieuw merk'));record('future-real-brand-appears-with-text-fallback');r.w.close();
r=await render({list:[]});assert.equal(r.data.length,0);record('empty-assortment-no-empty-links');r.w.close();
r=await render({list:['Merk & Co "Nieuw"'],locale:'/en/collections'});assert.equal(new URL(r.data[0].href,'https://example.invalid').searchParams.get('q'),'Merk & Co "Nieuw"');assert(r.data[0].href.startsWith('/en/collections/vendors?'));assert(r.html.includes('&amp;'));record('locale-aware-encoded-vendor-and-escaped-label');r.w.close();
r=await render({collections:{}});assert(r.data.find(i=>i.key==='cottoceramix').href.startsWith('/collections/vendors?q='));record('missing-cotto-collection-keeps-vendor-destination');r.w.close();
r=await render({settings:{bc_brand_link_hotbath:'/collections/hotbath',bc_brand_logo_hotbath:{src:'/files/hotbath.png'}}});assert.equal(r.data.find(i=>i.key==='hotbath').href,'/collections/hotbath');assert(r.w.document.querySelector('[data-bc-brand="hotbath"] img'));assert.equal(r.w.document.querySelector('[data-bc-brand="hotbath"] a').getAttribute('aria-label'),'Hotbath');record('shared-custom-logo-and-brand-landing-override');r.w.close();
for(const source of ['home','directory']){r=await render({source});assert.equal(r.data.length,9);if(source==='home'){assert(!r.w.document.querySelector('[data-brand-controls]'));assert(r.w.document.querySelector('[data-brand-track]'));assert(r.w.document.querySelector('a.bc-brand-slider__all'));}record('actual-'+source+'-uses-shared-list');r.w.close();}
const baseline=Object.fromEntries(['templates/index.json','config/settings_schema.json','locales/nl.json','locales/en.default.json'].map(path=>[path,fs.readFileSync(new URL('rollback/'+path,import.meta.url),'utf8')]));
const index=json(file('templates/index.json')),oldIndex=json(baseline['templates/index.json']);
for(const key of Object.keys(oldIndex.sections))if(key!=='bc_homepage')assert.deepEqual(index.sections[key],oldIndex.sections[key]);
const oldHome=structuredClone(oldIndex.sections.bc_homepage);
for(const [key,block]of Object.entries(oldHome.blocks))if(block.type==='brand')delete oldHome.blocks[key];
oldHome.block_order=oldHome.block_order.filter(k=>oldHome.blocks[k]);
assert.deepEqual(index.sections.bc_homepage,oldHome);record('homepage-campaigns-categories-settings-and-disabled-sections-preserved');
const global=json(file('config/settings_schema.json')),oldGlobal=json(baseline['config/settings_schema.json']);assert.deepEqual(global.slice(0,-1),oldGlobal);
const newSettings=global.at(-1).settings;assert.equal(newSettings.filter(s=>s.type==='image_picker').length,9);assert.equal(newSettings.filter(s=>s.type==='url').length,9);assert.equal(new Set(newSettings.filter(s=>s.id).map(s=>s.id)).size,newSettings.filter(s=>s.id).length);record('one-global-logo-and-link-setting-per-known-brand-existing-settings-preserved');
for(const lang of ['nl','en.default']){const current=json(file('locales/'+lang+'.json'));const original=json(baseline['locales/'+lang+'.json']);assert(current.bc_brands.previous&&current.bc_brands.next);delete current.bc_brands;delete current.bc_home.support;assert.deepEqual(current,original);}record('nl-en-labels-with-all-existing-price-translations-preserved');

const script=file('assets/bc-brand-slider.js');
const tick=()=>new Promise(resolve=>setTimeout(resolve,25));
async function slider({rtl=false,reduced=false,count=9,width=300}={}){
 const w=new Window({url:'https://example.invalid'});w.ResizeObserver=class{observe(){}disconnect(){}};w.matchMedia=()=>({matches:reduced});
 w.document.body.innerHTML='<bc-brand-slider><div data-brand-controls hidden><button data-brand-previous></button><button data-brand-next></button></div><ul data-brand-track tabindex="0" style="column-gap:10px;direction:'+(rtl?'rtl':'ltr')+'">'+Array.from({length:count},(_,i)=>'<li><a href="/brand/'+i+'">Brand '+i+'</a></li>').join('')+'</ul></bc-brand-slider>';
 const element=w.document.querySelector('bc-brand-slider'),track=w.document.querySelector('ul');let client=width,left=0,calls=[];
 const total=count?count*110-10:0;
 Object.defineProperties(track,{clientWidth:{get:()=>client},scrollWidth:{get:()=>total},scrollLeft:{get:()=>left,set:v=>{left=v;}}});
 if(track.firstElementChild)track.firstElementChild.getBoundingClientRect=()=>({width:100});
 const scroll=(value,behavior)=>{left=(rtl?-1:1)*Math.min(Math.max(0,Math.abs(value)),Math.max(0,total-client));calls.push({left,behavior});track.dispatchEvent(new w.Event('scroll'));};
 track.scrollBy=({left:amount,behavior})=>scroll(left+amount,behavior);track.scrollTo=({left:value,behavior})=>scroll(value,behavior);
 w.eval(script);await tick();
 return {w,element,track,calls,resize:async value=>{client=value;w.dispatchEvent(new w.Event('resize'));await tick();},close:async()=>{await w.happyDOM.abort();w.close();}};
}
let p=await slider();assert(p.element.previous.disabled);assert(!p.element.next.disabled);assert(!p.element.controls.hidden);p.element.next.click();await tick();assert(p.track.scrollLeft>0);assert(!p.element.previous.disabled);p.track.dispatchEvent(new p.w.KeyboardEvent('keydown',{key:'End',bubbles:true}));await tick();assert(p.element.next.disabled);p.element.previous.click();await tick();assert(!p.element.next.disabled);p.track.dispatchEvent(new p.w.KeyboardEvent('keydown',{key:'Home',bubbles:true}));await tick();assert(p.element.previous.disabled);record('real-slider-js-buttons-keyboard-and-boundaries');await p.close();
p=await slider();await p.resize(1200);assert(p.element.controls.hidden);await p.resize(300);assert(!p.element.controls.hidden);record('resize-hides-unneeded-controls-and-restores-them');await p.close();
for(const count of [0,1]){p=await slider({count});assert(p.element.controls.hidden);record('no-overflow-controls-hidden-'+count+'-brands');await p.close();}
p=await slider({reduced:true});p.element.next.click();await tick();assert.equal(p.calls.at(-1).behavior,'auto');record('reduced-motion-uses-instant-scroll');await p.close();
p=await slider({rtl:true});p.element.next.click();await tick();assert(p.track.scrollLeft<0);assert(!p.element.previous.disabled);record('rtl-direction-and-boundary-state');await p.close();
p=await slider();const saved=p.element;p.element.remove();p.w.document.body.append(saved);await tick();saved.next.click();await tick();assert.equal(p.calls.length,1);record('theme-editor-reconnect-does-not-duplicate-handlers');await p.close();
fs.writeFileSync(new URL('checks.json',import.meta.url),JSON.stringify({status:'PASS',checks:results.length,results,scope:'Actual shared Liquid renderer and slider JavaScript with synthetic data/layout. Real preview checked separately; no physical touch-device test.'},null,2)+'\n');
console.log(results.length+' brand renderer and slider checks PASS');

