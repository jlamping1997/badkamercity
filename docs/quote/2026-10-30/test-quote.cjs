const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {Liquid}=require('liquidjs'),{JSDOM}=require('jsdom');
const root=path.resolve(__dirname,'../../..'),locale=JSON.parse(fs.readFileSync(path.join(root,'locales/nl.json')));
const source=fs.readFileSync(path.join(root,'sections/bc-quote.liquid'),'utf8').replace(/{% schema %}[\s\S]*?{% endschema %}/,'');
const engine=new Liquid({strictFilters:false});
engine.registerFilter('asset_url',x=>'https://example.invalid/'+x);engine.registerFilter('stylesheet_tag',x=>'<link rel="stylesheet" href="'+x+'">');engine.registerFilter('t',key=>key.split('.').reduce((v,k)=>v?.[k],locale)||key);
const tests=[];const record=(name,fn)=>{fn();tests.push(name)};
(async()=>{
 const render=async settings=>new JSDOM(await engine.parseAndRender(source,{section:{id:'quote-fixture',settings},pages:{contact:{url:'/pages/contact'}},routes:{root_url:'/'}}));
 let dom=await render({show_preview:true,integration_enabled:false,form_id:''}),d=dom.window.document;
 record('Single H1 and three native FAQs',()=>{assert.equal(d.querySelectorAll('h1').length,1);assert.equal(d.querySelectorAll('details').length,3)});
 record('Preview cannot collect or send',()=>{assert.ok(d.querySelector('fieldset').disabled);assert.equal(d.querySelectorAll('form').length,0);assert.equal(d.querySelectorAll('iframe').length,0);assert.equal(d.querySelector('button').type,'button')});
 record('All input and textarea labels are present',()=>{for(const x of d.querySelectorAll('input:not([type=radio]),textarea'))assert.ok(d.querySelector('label[for="'+x.id+'"]'))});
 record('IDs are unique',()=>{const ids=[...d.querySelectorAll('[id]')].map(x=>x.id);assert.equal(ids.length,new Set(ids).size)});
 dom=await render({show_preview:false,integration_enabled:false,form_id:'123456789012345'});d=dom.window.document;
 record('Disabled integration never loads provider',()=>{assert.equal(d.querySelectorAll('iframe').length,0);assert.equal(d.querySelectorAll('input').length,0);assert.equal(d.querySelector('.bcq-unavailable + a').getAttribute('href'),'/pages/contact')});
 for(const id of ['', '1234','1234567890/../other','1234567890" onload="alert(1)','123456789012345678901']){
  d=(await render({show_preview:false,integration_enabled:true,form_id:id})).window.document;
  record('Invalid provider id blocked '+JSON.stringify(id),()=>assert.equal(d.querySelectorAll('iframe').length,0));
 }
 d=(await render({show_preview:false,integration_enabled:true,form_id:'123456789012345'})).window.document;
 record('Numeric ID loads only expected HTTPS provider',()=>{assert.equal(d.querySelector('iframe').src,'https://form.jotform.com/123456789012345');assert.ok(d.querySelector('iframe').title);assert.equal(d.querySelectorAll('fieldset').length,0)});
 const index=JSON.parse(fs.readFileSync(path.join(root,'templates/index.json'))),template=JSON.parse(fs.readFileSync(path.join(root,'templates/page.offerte-vergelijken.json')));
 record('No live CTA or upload enabled by default',()=>{assert.equal(index.sections.bc_quote_teaser.disabled,true);assert.equal(template.sections.main.settings.integration_enabled,false)});
 for(const file of ['nl.json','en.default.json']){
  const previous=JSON.parse(fs.readFileSync(path.join(__dirname,'baseline/locales',file),'utf8').replace(/^\s*\/\*[\s\S]*?\*\//,''));const current=JSON.parse(fs.readFileSync(path.join(root,'locales',file)));delete current.bc_quote;
  record('Preserve all existing translations '+file,()=>assert.deepEqual(current,previous));
 }
 fs.writeFileSync(path.join(__dirname,'tests.json'),JSON.stringify({scope:'Local LiquidJS/DOM fixture; no remote upload, delivery or private access test',passed:tests.length,tests},null,2));console.log(tests.length+' quote render cases passed');
})().catch(e=>{console.error(e);process.exit(1)});
