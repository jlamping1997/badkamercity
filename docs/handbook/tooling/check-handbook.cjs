// Offline DOM verification. No browser layout, phone, storefront, email or cart claim.
const fs=require('fs');
const assert=require('assert/strict');
const crypto=require('crypto');
const {JSDOM,VirtualConsole}=require(process.env.HANDBOOK_JSDOM_MODULE||'jsdom');
if(!process.argv[2]||!process.argv[3])throw new Error('Usage: check-handbook.cjs INPUT.html OUTPUT.json');
const source=fs.readFileSync(process.argv[2],'utf8');
const errors=[],network=[],checks=[];
const vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e.message));
const dom=new JSDOM(source,{runScripts:'dangerously',url:'https://documentation.invalid/',virtualConsole:vc,pretendToBeVisual:true,beforeParse(w){w.fetch=()=>{network.push('fetch');throw new Error('Network forbidden')};w.XMLHttpRequest=class{open(){network.push('xhr');throw new Error('Network forbidden')}}}});
const w=dom.window,d=w.document,$=s=>d.querySelector(s),$$=s=>[...d.querySelectorAll(s)];
const input=(id,value,type='input')=>{const el=$(id);el.value=value;el.dispatchEvent(new w.Event(type,{bubbles:true}))};
const wait=()=>new Promise(resolve=>setTimeout(resolve,300));
const check=(name,fn)=>{fn();checks.push(name)};
(async()=>{
 check('80 sequential chapter headings; one H1; 81 contents links',()=>{
  assert.equal($$('#document h2').length,80);assert.equal($$('h1').length,1);assert.equal($$('#toc a').length,81);
  assert.deepEqual($$('#document h2').map(el=>Number(el.textContent.match(/^\d+/)[0])),Array.from({length:80},(_,i)=>i+1));
 });
 check('Version 2.0, date and live/concept/mail boundaries',()=>{
  assert(d.title.includes('31 oktober 2026'));assert($('.top').textContent.includes('versie 2.0'));
  const text=$('#document').textContent;
  assert(text.includes('MAIN 195948839178'));assert(text.includes('195947036938'));assert(text.includes('NAV-02 is concept'));
  assert(text.includes('mailboxbewijs blijft open'));assert(text.includes('407/409'));
  assert(text.includes('Snapshot 30 oktober 2026'));assert(text.includes('niet volledig opnieuw geëxporteerd'));
 });
 check('50 embedded task definitions and first 12 cards',()=>{
  assert.equal(JSON.parse($('#task-data').textContent).length,50);assert.equal($$('.task-card').length,12);
  assert($('#task-status').textContent.includes('50 van 50'));
 });
 check('Task term, role and state filters combine',()=>{
  input('#task-search','retour');assert($$('.task-card').length>0);assert($$('.task-card').every(x=>/retour/i.test(x.textContent)));
  input('#task-owner','Eigenaar','change');input('#task-state','OPEN','change');
  assert.equal($$('.task-card').length,1);assert($('.task-card').textContent.includes('Retourmailontvangst'));
  input('#task-search','documentatie-geen-taak');assert.equal($$('.task-card').length,0);assert($('#task-results').textContent.includes('Geen passende taak'));
  input('#task-search','');input('#task-owner','','change');input('#task-state','CONCEPT','change');
  assert.equal($$('.task-card').length,1);assert($('.task-card').textContent.includes('zonder schuiven'));
  input('#task-state','','change');input('#task-search','doosinhoud');assert($$('.task-card').length>=2);
  input('#task-search','');
 });
 check('All task targets resolve; catalog snapshot contains 11679 records',()=>{
  for(const t of JSON.parse($('#task-data').textContent))assert(d.getElementById(t.target));
  assert.equal(JSON.parse($('#catalog-data').textContent).length,11679);assert.equal($$('#catalog-body tr').length,30);
 });
 check('Catalog vendor 337 Porcelanosa; three Verona Cubik; empty result',()=>{
  input('#catalog-vendor','Porcelanosa','change');assert($('#catalog-status').textContent.includes('337'));
  assert($$('#catalog-body tr').every(el=>el.cells[0].textContent==='Porcelanosa'&&el.cells[2].textContent==='tegels'));
  input('#catalog-search','Verona Cubik');assert.equal($$('#catalog-body tr').length,3);
  input('#catalog-search','documentatie-geen-product');assert.equal($$('#catalog-body tr').length,0);assert($('#catalog-prev').disabled&&$('#catalog-next').disabled);assert($('#catalog-page').textContent.includes('0 van 0'));
 });
 check('Catalog pagination and return preserve first page',()=>{
  input('#catalog-search','');input('#catalog-vendor','','change');const first=$('#catalog-body a').href;
  $('#catalog-next').click();assert($('#catalog-page').textContent.includes('Pagina 2'));assert.notEqual($('#catalog-body a').href,first);
  $('#catalog-prev').click();assert.equal($('#catalog-body a').href,first);assert($('#catalog-prev').disabled);
 });
 input('#doc-search','snijverlies');await wait();
 check('Text search returns chapter links',()=>{assert($$('#doc-results a').length>0);assert($('#search-status').textContent.includes('tekstplaatsen'))});
 input('#doc-search','retourlabel');await wait();
 check('New practical text searchable',()=>{assert($$('#doc-results a').length>0);assert($$('#doc-results a').some(el=>/retour/i.test(el.textContent)))});
 input('#doc-search','documentatie-geen-inhoud-xyz');await wait();
 check('No-result search and Escape reset',()=>{
  assert.equal($$('#doc-results a').length,0);$('#doc-search').dispatchEvent(new w.KeyboardEvent('keydown',{key:'Escape',bubbles:true}));assert.equal($('#doc-search').value,'');
 });
 check('Contents toggle and chapter click update aria state',()=>{
  $('#menu-toggle').click();assert.equal($('#menu-toggle').getAttribute('aria-expanded'),'true');
  $('#toc a').dispatchEvent(new w.MouseEvent('click',{bubbles:true,cancelable:true}));assert.equal($('#menu-toggle').getAttribute('aria-expanded'),'false');
 });
 check('Unique IDs, valid internal anchors and standalone external links',()=>{
  const ids=$$('[id]').map(el=>el.id);assert.equal(ids.length,new Set(ids).size);
  for(const a of $$('a[href^="#"]'))assert(d.getElementById(a.hash.slice(1)),'Missing anchor '+a.hash);
  for(const a of $$('a[href]'))assert(/^(#|https?:|mailto:|tel:)/.test(a.getAttribute('href')),'Relative/unsafe URL '+a.getAttribute('href'));
 });
 check('No external scripts, styles, execution errors or network requests',()=>{
  assert.equal($$('script[src],link[rel="stylesheet"]').length,0);assert.deepEqual(errors,[]);assert.deepEqual(network,[]);
 });
 // Static parsing verifies the content remains available with scripts disabled.
 const plain=new JSDOM(source);
 check('No-script document retains chapters and complete task table',()=>{
  assert.equal(plain.window.document.querySelectorAll('#document h2').length,80);
  assert(plain.window.document.querySelector('#document').textContent.includes('T50'));
  assert(plain.window.document.querySelector('#document').textContent.includes('A50'));
  assert(plain.window.document.querySelector('#document').textContent.includes('D40'));
 });plain.window.close();
 const result={status:'PASS',date:new Date().toISOString(),artifact:process.argv[2].split('/').pop(),sha256:crypto.createHash('sha256').update(source).digest('hex'),bytes:Buffer.byteLength(source),counts:{chapters:80,tasks:50,diagnoses:40,acceptanceCases:50,products:11679},method:'Offline jsdom DOM execution and static parsing only',limits:['No visual browser or physical phone/laptop claim','No Windows workspace check','No storefront JavaScript/mail/cart/checkout execution','Product identity catalog is the 30 October snapshot'],checks,errors,network};
 fs.writeFileSync(process.argv[3],JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));dom.window.close();
})().catch(error=>{console.error(error);process.exitCode=1;dom.window.close()});
