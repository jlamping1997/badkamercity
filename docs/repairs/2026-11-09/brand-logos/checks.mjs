import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
const require=createRequire(process.env.BC_TEST_DEPENDENCIES||new URL('package.json',import.meta.url));
const {Liquid}=require('liquidjs'),{Window}=require('happy-dom');
const theme=new URL('../../../../shopify/current/',import.meta.url);
const source=fs.readFileSync(new URL('snippets/bc-brand-items.liquid',theme),'utf8');
const manifest=JSON.parse(fs.readFileSync(new URL('logo-sources.json',import.meta.url),'utf8'));
const results=[],record=test=>results.push({test,result:'PASS'});
const vendors=['Cottoceramix','Hotbath','JEE-O','Lagoo','Porcelanosa','Sunshower','THE MOSAIC FACTORY','Verlavio','Wiesbaden','BadkamerCity Test'];
for(const logo of manifest.logos){
 const bytes=fs.readFileSync(new URL(logo.asset,theme));
 assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),logo.sha256);
 assert.equal(crypto.createHash('md5').update(bytes).digest('hex'),logo.md5);
 if(logo.asset.endsWith('.svg'))assert(bytes.toString().includes('<svg'));
 else assert.equal(bytes.subarray(0,8).toString('hex'),'89504e470d0a1a0a');
 assert(new URL(logo.source_page).protocol==='https:');
 record(logo.brand+'-verified-local-logo-matches-source-record');
}
const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;');
async function render(settings={},list=vendors,mode='directory'){
 const globals={shop:{vendors:list},settings,collections:{cottoceramix:{url:'/collections/cottoceramix'}},routes:{collections_url:'/collections'}};
 const e=new Liquid({globals});
 e.registerTag('doc',{parse(t,tokens){while(tokens.length&&tokens.shift().getText()!=='{% enddoc %}'){}},render(){return ''}});
 e.registerFilter('handleize',s=>String(s).toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''));
 e.registerFilter('asset_url',s=>'/assets/'+s);
 e.registerFilter('image_url',s=>s.src);
 e.registerFilter('image_tag',(src,...args)=>{const options=Object.fromEntries(args.filter(Array.isArray));return '<img src="'+escape(src)+'" alt="'+escape(options.alt||'')+'">';});
 const html=await e.parseAndRender(source,{mode}),w=new Window();w.document.body.innerHTML=html;
 return {w,html};
}
for(const mode of ['directory','slider']){
 const {w}=await render({},vendors,mode);
 assert.equal(w.document.querySelectorAll('li').length,9);
 const images=[...w.document.querySelectorAll('img')];assert.equal(images.length,8);
 for(const logo of manifest.logos){
  const key=logo.brand.toLowerCase(),card=w.document.querySelector('[data-bc-brand="'+key+'"]');
  assert(card);const image=card.querySelector('img');assert(image);
  assert.equal(image.getAttribute('src'),'/'+logo.asset);
  assert.equal(image.getAttribute('alt'),logo.brand);
  assert.equal(image.getAttribute('width'),'180');assert.equal(image.getAttribute('height'),'48');
  assert.equal(image.getAttribute('loading'),'lazy');
  assert(card.querySelector('a').getAttribute('href'));
 }
 assert(!w.document.querySelector('[data-bc-brand="verlavio"] img'));
 assert.equal(w.document.querySelector('[data-bc-brand="verlavio"] span').textContent,'Verlavio');
 assert(!w.document.querySelector('[data-bc-brand="badkamercity test"]'));
 record(mode+'-same-eight-self-hosted-logos-nine-valid-brand-links');w.close();
}
const custom=await render({bc_brand_logo_hotbath:{src:'/files/my-logo.png'},bc_brand_link_hotbath:'/collections/hotbath'});
assert.equal(custom.w.document.querySelector('[data-bc-brand="hotbath"] img').getAttribute('src'),'/files/my-logo.png');
assert.equal(custom.w.document.querySelector('[data-bc-brand="hotbath"] a').getAttribute('href'),'/collections/hotbath');
record('merchant-logo-and-brand-link-override-bundled-default');custom.w.close();
const future=await render({},['Nieuw merk']);assert.equal(future.w.document.querySelectorAll('img').length,0);assert.equal(future.w.document.querySelector('span').textContent,'Nieuw merk');record('unknown-future-brand-stays-readable-without-broken-image');future.w.close();
const parse=s=>JSON.parse(s.replace(/^\/\*[\s\S]*?\*\//,''));
const before=parse(fs.readFileSync(new URL('rollback/config/settings_schema.json',import.meta.url),'utf8')),after=parse(fs.readFileSync(new URL('config/settings_schema.json',theme),'utf8'));
const group=after.find(s=>s.name==='Merken'),oldGroup=before.find(s=>s.name==='Merken');
group.settings[0].content=oldGroup.settings[0].content;
assert.deepEqual(after,before);record('only-brand-help-text-changes-no-existing-settings-redefined');
fs.writeFileSync(new URL('checks.json',import.meta.url),JSON.stringify({status:'PASS',checks:results.length,results,scope:'Original asset signatures/hashes and actual shared Liquid; browser rendering and live asset responses checked separately.'},null,2)+'\n');
console.log(results.length+' brand logo checks PASS');

