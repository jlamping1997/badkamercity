import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
const require=createRequire(process.env.BC_TEST_DEPENDENCIES || new URL('../../../../../testdeps/package.json',import.meta.url));
const {Liquid}=require('liquidjs'), {Window}=require('happy-dom');
const theme=new URL('../../../../shopify/current/',import.meta.url),read=p=>fs.readFileSync(new URL(p,theme),'utf8');
const json=s=>JSON.parse(s.replace(/^\s*\/\*[\s\S]*?\*\/\s*/,''));
const results=[],record=test=>results.push({test,result:'PASS'});
async function render({handle='bad-accessoires',description='',extra='',locale='nl.json',faucets=false,contact=true,suffix=''}={}) {
 const e=new Liquid(),translations=json(read('locales/'+locale));
 e.registerTag('schema',{parse(token,tokens){while(tokens.length&&tokens.shift().getText()!=='{% endschema %}'){}},render(){return '';}});
 e.registerFilter('asset_url',s=>'/assets/'+s);e.registerFilter('stylesheet_tag',s=>'<link rel="stylesheet" href="'+s+'">');
 e.registerFilter('inline_asset_content',()=>'<svg></svg>');
 e.registerFilter('t',(key,...args)=>{const options=Object.fromEntries(args.filter(Array.isArray));return String(key.split('.').reduce((v,k)=>v?.[k],translations)||key).replace(/\{\{\s*(\w+)\s*\}\}/g,(_,k)=>options[k]??'');});
 const collection={id:1,handle,title:'Bad accessoires',description,template_suffix:suffix};
 const menu={links:faucets?[{object:{handle:'kranen',id:1},links:[]}]:[]};
 const html=await e.parseAndRender(read('sections/bc-collection-advice.liquid'),{collection,request:{page_type:'collection'},routes:{collections_url:'/collections'},pages:{contact:contact?{url:'/pages/contact'}:null},linklists:{'main-menu':menu},section:{id:'test',settings:{navigation_menu:menu,extra_content:extra,show_contact:true,show_faq:true}}});
 const w=new Window();w.document.body.innerHTML=html;return {w,html};
}
for(const marker of ['[SPLIT]','<p>[SPLIT]</p>','[split]','<p>[split]</p>']){
 const r=await render({description:'<p>Unique introduction</p>'+marker+'<h2>Specific category advice</h2><p>Actual useful text <a href="/collections/badgrepen">grab rails</a></p>'});
 assert(!r.html.includes('Unique introduction'));assert.equal(r.w.document.querySelectorAll('h2').length,1);assert(r.html.includes('Actual useful text'));assert(!r.html.includes('[SPLIT]'));assert(!r.html.includes('Badaccessoires kiezen'));assert.equal(r.w.document.querySelector('.rte a').getAttribute('href'),'/collections/badgrepen');r.w.close();
}
record('all-four-existing-split-markers-show-only-bottom-content-with-links');
let hub=await render({handle:'kranen',suffix:'category-landing',description:'<p>Intro</p>[SPLIT]<h2>Already rendered by category hub</h2><p>Preserve in its original section.</p>'});assert(!hub.html.includes('Already rendered by category hub'));hub.w.close();record('category-hub-keeps-its-own-seo-renderer-without-duplicating-its-copy');
let r=await render({description:'<p>Intro</p>[SPLIT]<h2>Existing content</h2><p>Preserve this.</p>',extra:'<h3>Merchant content</h3><p>Keep this too.</p>'});assert(r.html.includes('Preserve this.'));assert(r.html.includes('Keep this too.'));assert(!r.html.includes('Badaccessoires kiezen'));r.w.close();record('split-and-section-content-preserved-without-fallback-duplication');
r=await render({extra:'<h2>Merchant advice</h2><p>Specific advice</p>'});assert(r.html.includes('Merchant advice'));assert(!r.html.includes('Badaccessoires kiezen'));r.w.close();record('merchant-copy-takes-precedence-over-authored-fallback');
r=await render();assert(r.html.includes('Badaccessoires kiezen'));assert.equal(r.w.document.querySelectorAll('.bc-advice-card,.bc-advice-grid,.bc-category-help').length,0);assert.equal(r.w.document.querySelectorAll('.rte a').length,2);assert.equal(r.w.document.querySelector('.bc-category-editorial__contact a').getAttribute('href'),'/pages/contact');r.w.close();record('bad-accessoires-readable-copy-real-links-and-compact-contact');
r=await render({handle:'badgrepen'});assert(r.html.includes('hartmaat'));assert(!r.html.includes('Badaccessoires kiezen'));r.w.close();record('grab-rails-get-relevant-installation-copy');
r=await render({handle:'unfilled-category',description:'<p>Already shown above products</p>',contact:false});assert(!r.html.includes('Already shown above products'));assert(!r.html.includes('Meet je ruimte'));assert.equal(r.w.document.querySelectorAll('.rte,.bc-category-faq,.bc-category-editorial__contact').length,0);r.w.close();record('unwritten-categories-do-not-get-repeated-generic-filler');
r=await render({faucets:true});assert.equal(r.w.document.querySelectorAll('.bc-category-faq details').length,3);r.w.close();r=await render();assert.equal(r.w.document.querySelectorAll('.bc-category-faq').length,0);r.w.close();record('existing-faucet-faq-keeps-exact-scope');
r=await render({locale:'en.default.json'});assert(r.html.includes('Choosing bath accessories'));assert(!r.html.includes('translation missing'));r.w.close();record('english-copy-and-links-render');
for(const locale of ['nl.json','en.default.json']){const current=json(read('locales/'+locale));delete current.bc_collection.editorial;const before=json(fs.readFileSync(new URL('rollback/locales/'+locale,import.meta.url),'utf8'));assert.deepEqual(current,before);}record('all-existing-translations-including-tile-prices-and-brands-preserved');
const js=read('assets/bc-external-filters.js'),code=js.slice(js.indexOf('    function swatch('),js.indexOf('    function renderFilters('));const swatch=new Function('location',code+';return swatch;')({origin:'https://badkamercity.nl'});
for(const v of ['Gunmetal','Gun metal','Gun-metal','Geborsteld gunmetal PVD','Gunmetal black'])assert.equal(swatch(v),'linear-gradient(120deg,#343e45,#7a8790,#455159)');assert.notEqual(swatch('Grijs'),swatch('Gunmetal'));assert.notEqual(swatch('Verouderd ijzer'),swatch('Gunmetal'));record('gunmetal-finishes-have-distinct-metallic-swatch-without-relabeling-gray-or-aged-iron');
const external=read('assets/bc-external-filters.css'),native=read('assets/component-card.css'),search=read('sections/main-search.liquid'),cards=read('assets/bc-product-cards.css');
assert(!external.includes('.bc-filter-card:hover .bc-card-media--hover-ready'));assert(external.includes('.bc-card-media--hover-ready:hover [data-bc-card-hover]'));assert(!/\.card-wrapper:hover \.media\.media--hover-effect/.test(native));assert(native.includes('.card__inner:hover .media.media--hover-effect'));assert(search.includes('.bc-search-card__media:hover .bc-search-card__image--secondary'));assert(!search.includes('.bc-search-card__link:hover .bc-search-card__image--secondary'));assert(cards.includes('.bc-standard-card .card__inner, .bc-filter-card .bc-filter-card__media { position: relative; z-index: 3; }'));record('all-three-renderers-limit-image-hover-and-raise-image-hit-area-over-overlay');
assert(native.includes('(hover: hover) and (pointer: fine)'));assert(external.includes('@media(hover:hover) and (pointer:fine)'));assert(search.includes('(hover: hover) and (pointer: fine)'));record('coarse-pointers-do-not-get-sticky-image-swap');
const footer=json(read('sections/footer-group.json')),beforeFooter=json(fs.readFileSync(new URL('rollback/sections/footer-group.json',import.meta.url),'utf8'));assert.equal(footer.sections.footer.settings.contact_address,'Retouradres\nBadkamercity\nZichtenburglaan 150\n2544 EB Den Haag');footer.sections.footer.settings.contact_address=beforeFooter.sections.footer.settings.contact_address;assert.deepEqual(footer,beforeFooter);record('only-return-address-setting-changes-without-harry-suiker-or-appointment-condition');
fs.writeFileSync(new URL('checks.json',import.meta.url),JSON.stringify({passed:true,results},null,2)+'\n');console.log(results.length+' checks PASS');
