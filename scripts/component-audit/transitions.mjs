// Offline state-chain replay. Real supplied source; synthetic DOM and transport.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const argv=process.argv.slice(2),args=Object.fromEntries(argv.reduce((a,v,i)=>(i%2===0&&a.push([v.replace(/^--/,''),argv[i+1]]),a),[]));
if(!args.source||!args.manifest||!args.output)throw Error('Use --source THEME --manifest PROVENANCE --output RESULT [--dom-module MODULE]');
const {Window}=await import(args['dom-module']||'happy-dom');
const manifest=JSON.parse(fs.readFileSync(args.manifest,'utf8')),sources={},scripts={},results=[];
const required=['assets/bc-product-inbouw.js','assets/product-form.js','assets/bc-product-disclosure.js','sections/footer.liquid','sections/main-glossary.liquid','sections/main-glossary-page.liquid'];
for(const name of required){const raw=fs.readFileSync(path.join(args.source,name)),row=manifest.files.find(r=>r.path===name);if(!row||crypto.createHash('sha256').update(raw).digest('hex')!==row.sha256)throw Error('Unverified source '+name);sources[name]=raw.toString('utf8');}
for(const name of required.filter(n=>n.endsWith('.liquid'))){const pattern=name.includes('footer')?/{%\s*javascript\s*%}([\s\S]*?){%\s*endjavascript\s*%}/:/<script>([\s\S]*?)<\/script>/;const match=sources[name].match(pattern);if(!match||/{[{%]/.test(match[1]))throw Error('Unsafe/absent plain script '+name);scripts[name]=match[1];}
const tick=()=>new Promise(resolve=>setImmediate(resolve));
async function settle(){for(let i=0;i<5;i++)await tick();}
const record=(id,classification,observations)=>results.push({id,classification,observations});
function context(html,{pathname='/products/synthetic-a',stored}={}){
 const w=new Window({url:'https://audit.invalid'+pathname,width:1363,height:936}),moves=[],calls=[],timers=new Map();let timerId=0;
 Object.defineProperty(w,'location',{configurable:true,value:{origin:'https://audit.invalid',pathname,search:'',href:'https://audit.invalid'+pathname,assign:url=>moves.push(url)}});
 Object.defineProperty(w.document,'readyState',{configurable:true,value:'complete'});
 w.fetch=()=>{throw Error('No unstubbed network permitted');};w.console.error=()=>{};
 w.setTimeout=(fn,delay)=>{const id=++timerId;timers.set(id,{fn,delay});return id;};w.clearTimeout=id=>timers.delete(id);
 w.document.body.innerHTML=html;
 if(stored!==undefined)w.sessionStorage.setItem('bc-inbouw-choice-v1',typeof stored==='string'?stored:JSON.stringify(stored));
 return {w,moves,calls,timers,fireTimeouts:()=>{for(const [id,t]of [...timers]){timers.delete(id);t.fn();}}};
}
async function dispose(c){await c.w.happyDOM.abort();c.w.close();}
function inbouw({choice='',quantity='2',available=true,loadAddon=true,mobile=false,stored,pathname}={}){
 const c=context(`<product-info ${mobile?'data-hotbath-mobile-a="true"':''}><div data-bc-product-switcher-v2 data-switch-group="synthetic-group"></div><product-form><form>
 <input name="id" value="101"><input name="quantity" type="number" min="1" step="1" value="${quantity}"><input name="properties[Fixture]" value="Synthetic"><input name="selling_plan" value="321">
 <bc-inbouw-addon data-valid="true" data-parent-variant="101" data-body-variant="202" data-parent-sku="SYN-A" data-body-sku="SYN-B" data-body-available="${available}" data-body-price="500" data-quantity-per-trim="1" data-currency="EUR" data-add-url="/cart/add.js" data-cart-url="/cart" data-message-choice="choose" data-message-changed="changed" data-message-quantity="quantity" data-message-unavailable="unavailable" data-message-uncertain="uncertain" data-message-loading="loading">
 <fieldset data-inbouw-controls disabled hidden aria-describedby="synthetic-detail"><div class="bc-inbouw__radio-controls"><input type="radio" name="bc_inbouw_choice" value="yes" data-inbouw-choice ${choice==='yes'?'checked':''} disabled><input type="radio" name="bc_inbouw_choice" value="no" data-inbouw-choice ${choice==='no'?'checked':''} disabled></div><div class="bc-inbouw__toggle-row" hidden><input type="checkbox" data-inbouw-toggle disabled></div></fieldset><p data-inbouw-total></p><p data-inbouw-error tabindex="-1" hidden></p><a data-inbouw-cart-link hidden>Check synthetic cart</a></bc-inbouw-addon>
 <div class="product-form__error-message-wrapper" hidden><span class="product-form__error-message"></span></div><button type="submit"><span>Buy</span></button><span class="loading__spinner hidden"></span></form></product-form></product-info>`,{stored,pathname});
 const {w}=c;w.fetchConfig=()=>({method:'POST',headers:{'Content-Type':'application/json'}});w.routes={cart_add_url:'/cart/add.js',cart_url:'/cart'};w.PUB_SUB_EVENTS={cartError:'cartError',cartUpdate:'cartUpdate'};w.publish=()=>Promise.resolve();w.CartPerformance={createStartingMarker:()=>0,measureFromMarker(){},measureFromEvent(){},measure:(label,fn)=>fn()};
 if(loadAddon)w.eval(sources['assets/bc-product-inbouw.js']);w.eval(sources['assets/product-form.js']);
 c.addon=w.document.querySelector('bc-inbouw-addon');c.form=w.document.querySelector('form');c.productForm=w.document.querySelector('product-form');c.button=w.document.querySelector('[type=submit]');
 c.submit=()=>c.form.dispatchEvent(new w.Event('submit',{bubbles:true,cancelable:true}));
 c.choose=value=>{const radio=c.addon.querySelector(`[value="${value}"]`);radio.checked=true;radio.dispatchEvent(new w.Event('change',{bubbles:true}));};
 c.pending=()=>{let resolve,reject;c.w.fetch=(url,options)=>{c.calls.push({url,options});return new Promise((a,b)=>{resolve=a;reject=b;options.signal?.addEventListener('abort',()=>b(new Error('synthetic timeout')),{once:true});});};return {resolve:body=>resolve({ok:true,json:async()=>body}),response:response=>resolve(response),reject:()=>reject(new Error('synthetic network failure'))};};
 return c;
}
const confirmed=(quantity=2)=>({items:[{variant_id:101,sku:'SYN-A',quantity},{variant_id:202,sku:'SYN-B',quantity}]});
function assertUncertain(c){assert.equal(c.addon.uncertain,true);assert.equal(c.addon.busy,false);assert.equal(c.button.getAttribute('aria-disabled'),'true');assert.equal(c.button.hasAttribute('aria-busy'),false);assert.equal(c.addon.querySelector('[data-inbouw-cart-link]').hidden,false);const count=c.calls.length;c.submit();assert.equal(c.calls.length,count);assert.equal(c.moves.length,0);}
{
 const c=inbouw({loadAddon:false});c.submit();assert.equal(c.calls.length,0);assert.equal(c.w.document.querySelector('.product-form__error-message').textContent,'loading');record('IBX-01','CONTROL_PASSED',{unreadyAddonBlocksNativeSubmit:true});await dispose(c);
}
{
 const c=inbouw();c.submit();assert.equal(c.calls.length,0);assert.equal(c.addon.querySelector('[data-inbouw-error]').textContent,'choose');assert.equal(c.w.document.activeElement,c.addon.choices[0]);record('IBX-02','CONTROL_PASSED',{missingChoiceBlocksAndFocusesFirstChoice:true});await dispose(c);
}
{
 const c=inbouw({choice:'no'});c.w.fetch=async(url,options)=>{c.calls.push({url,options});return {json:async()=>({status:422,description:'synthetic rejection'})};};c.submit();await settle();assert.equal(c.calls.length,1);assert.equal(c.calls[0].options.body.get('id'),'101');assert.equal(c.calls[0].options.body.get('quantity'),'2');assert.equal(c.addon.busy,false);record('IBX-03','CONTROL_PASSED',{noChoiceDelegatesOnceToActualProductForm:true,requestType:'FormData',nativeErrorResponseStubbed:true});await dispose(c);
}
{
 const c=inbouw({choice:'yes'}),pending=c.pending();c.submit();assert.equal(c.calls.length,1);const body=JSON.parse(c.calls[0].options.body);assert.deepEqual(body,{items:[{id:'101',quantity:2,properties:{Fixture:'Synthetic'},selling_plan:'321'},{id:'202',quantity:2}]});assert.equal(c.addon.busy,true);assert.equal(c.addon.controls.disabled,true);c.submit();assert.equal(c.calls.length,1);
 c.form.elements.namedItem('quantity').value='3';c.form.dispatchEvent(new c.w.Event('change',{bubbles:true}));assert.equal(JSON.parse(c.calls[0].options.body).items[0].quantity,2);
 pending.resolve(confirmed());await c.addon.pendingAdd;assert.deepEqual(c.moves,['/cart']);assert.equal(c.timers.size,0);record('IBX-04','CONTROL_PASSED',{twoItemPayloadAndParentOnlyPropertiesPlan:true,pendingBlocksDuplicateSubmit:true,payloadIsSnapshot:true,confirmedPairNavigatesOnce:true,busyUntilNavigation:true});await dispose(c);
}
for(const [id,change,error] of [['IBX-05',c=>{c.form.elements.namedItem('id').value='999';},'changed'],['IBX-06',c=>{c.form.elements.namedItem('quantity').value='';},'Vul een geldig aantal in.']]){
 const c=inbouw({choice:'yes'});change(c);c.submit();assert.equal(c.calls.length,0);assert.equal(id==='IBX-05'?c.addon.querySelector('[data-inbouw-error]').textContent:c.w.document.querySelector('.product-form__error-message').textContent,error);record(id,'CONTROL_PASSED',{identityOrQuantityMismatchBlocksBeforeTransport:true,trigger:id==='IBX-05'?'identity':'empty quantity'});await dispose(c);
}
{
 const c=inbouw({available:false,choice:'yes'});c.submit();assert.equal(c.calls.length,0);assert.equal(c.addon.querySelector('[data-inbouw-error]').textContent,'unavailable');record('IBX-07','CONTROL_PASSED',{unavailableBodyBlocksExplicitYes:true});await dispose(c);
}
const invalidResponses=[
 ['IBX-08','HTTP 422',{ok:false,json:async()=>({status:422})}],
 ['IBX-09','invalid JSON',{ok:true,json:async()=>{throw Error('synthetic JSON failure');}}],
 ['IBX-10','missing body item',{ok:true,json:async()=>({items:[confirmed().items[0]]})}],
 ['IBX-11','wrong SKU',{ok:true,json:async()=>({items:[confirmed().items[0],{variant_id:202,sku:'WRONG',quantity:2}]})}],
 ['IBX-12','insufficient quantity',{ok:true,json:async()=>confirmed(1)}]
];
for(const [id,trigger,response] of invalidResponses){const c=inbouw({choice:'yes'}),pending=c.pending();c.submit();pending.response(response);await c.addon.pendingAdd;assertUncertain(c);assert.equal(c.timers.size,0);record(id,'CONTROL_PASSED',{trigger,uncertainLocksRetryAndShowsCartLink:true,HTTPRejectionAlsoConservativelyLocked:trigger==='HTTP 422'});await dispose(c);}
{
 const c=inbouw({choice:'yes'}),pending=c.pending();c.submit();pending.resolve(confirmed(4));await c.addon.pendingAdd;assert.deepEqual(c.moves,['/cart']);record('IBX-13','BOUNDARY_CONFIRMED',{responseQuantityGreaterThanRequestedAccepted:true,existingCartMergeNotSimulated:true});await dispose(c);
}
{
 const c=inbouw({choice:'yes'}),pending=c.pending();c.submit();pending.reject();await c.addon.pendingAdd;assertUncertain(c);record('IBX-14','CONTROL_PASSED',{networkFailureLocksRetry:true});await dispose(c);
}
{
 const c=inbouw({choice:'yes'});c.pending();c.submit();assert.deepEqual([...c.timers.values()].map(t=>t.delay),[30000]);c.fireTimeouts();await c.addon.pendingAdd;assertUncertain(c);assert.equal(c.calls[0].options.signal.aborted,true);record('IBX-15','CONTROL_PASSED',{timeoutMs:30000,abortSignalAndUncertainLock:true});await dispose(c);
}
{
 const c=inbouw({choice:'yes'}),pending=c.pending();c.submit();c.w.dispatchEvent(new c.w.Event('pagehide'));pending.resolve(confirmed());await c.addon.pendingAdd;assert.equal(c.moves.length,0);const show=new c.w.Event('pageshow');Object.defineProperty(show,'persisted',{value:true});c.w.dispatchEvent(show);assertUncertain(c);record('IBX-16','CONTROL_PASSED',{leavingPageSuppressesNavigation:true,persistedReturnConvertsBusyToUncertain:true});await dispose(c);
}
{
 const c=inbouw({choice:'yes'}),pending=c.pending();c.submit();c.addon.remove();assert.equal(c.calls[0].options.signal.aborted,false);pending.resolve(confirmed());await c.addon.pendingAdd;assert.equal(c.moves.length,0);record('IBX-17','BOUNDARY_CONFIRMED',{disconnectStopsListenersButNotAddRequest:true,detachedSuccessDoesNotNavigate:true,realServerOutcomeNotModeled:true});await dispose(c);
}
for(const [id,edit,restore] of [
 ['IBX-18',s=>s,true],['IBX-19',s=>({...s,group:'other'}),false],['IBX-20',s=>({...s,body:'999'}),false],['IBX-21',s=>({...s,from:'/products/synthetic-a'}),false],['IBX-22',s=>({...s,savedAt:Date.now()-31000}),false],['IBX-23',s=>({...s,savedAt:Date.now()+31000}),false],['IBX-24',()=>'{invalid',false]
]){
 const saved=edit({group:'synthetic-group',body:'202',choice:'yes',from:'/products/synthetic-previous',savedAt:Date.now()});const c=inbouw({stored:saved});assert.equal(c.addon.choice(),restore?'yes':'');assert.equal(c.w.sessionStorage.getItem('bc-inbouw-choice-v1'),id==='IBX-24'?'{invalid':null);record(id,id==='IBX-24'?'BOUNDARY_CONFIRMED':'CONTROL_PASSED',{handoffRestored:restore,savedValueConsumed:id!=='IBX-24',scenario:{'IBX-18':'valid','IBX-19':'wrong group','IBX-20':'wrong body','IBX-21':'same route','IBX-22':'expired','IBX-23':'future timestamp','IBX-24':'invalid JSON'}[id]});await dispose(c);
}
{
 const c=inbouw({mobile:true});assert.equal(c.addon.choice(),'no');assert.equal(c.addon.explicitChoice,false);c.w.document.querySelector('product-info').dataset.bcNavigating='true';c.addon.rememberForNavigation();assert.equal(c.w.sessionStorage.getItem('bc-inbouw-choice-v1'),null);c.choose('yes');c.addon.rememberForNavigation();assert.equal(JSON.parse(c.w.sessionStorage.getItem('bc-inbouw-choice-v1')).choice,'yes');record('IBX-25','CONTROL_PASSED',{implicitMobileNoNotPersisted:true,explicitChoiceCanBeHandedOff:true,mobileFlagIsSyntheticNotViewportEvidence:true});await dispose(c);
}

function footerContext(mobile){const c=context('<footer class="bcf-v3"><details class="bcf-nav" open><summary class="bcf-nav-summary">Synthetic column</summary><ul class="bcf-links"><li>Item</li></ul></details></footer>');c.medias=[];c.w.matchMedia=()=>{const listeners=new Set(),media={matches:mobile,addEventListener:(type,fn)=>listeners.add(fn),removeEventListener:(type,fn)=>listeners.delete(fn),listeners,set(value){this.matches=value;listeners.forEach(fn=>fn());}};c.medias.push(media);return media;};c.w.eval(scripts['sections/footer.liquid']);c.root=c.w.document.querySelector('footer');c.panel=c.root.querySelector('details');c.summary=c.root.querySelector('summary');c.editor=type=>c.root.dispatchEvent(new c.w.Event('shopify:section:'+type,{bubbles:true}));return c;}
{
 const c=footerContext(true);assert.equal(c.panel.open,false);assert.equal(c.summary.hasAttribute('aria-disabled'),false);c.panel.open=true;c.medias[0].set(false);assert.equal(c.panel.open,true);assert.equal(c.summary.getAttribute('tabindex'),'-1');const click=new c.w.Event('click',{bubbles:true,cancelable:true});c.summary.dispatchEvent(click);assert.equal(click.defaultPrevented,true);c.medias[0].set(true);assert.equal(c.panel.open,false);record('FT-01','CONTROL_PASSED',{mobileStartsClosed:true,desktopForcesOpenAndSuppressesToggle:true,returnToMobileResetsPanelState:true,matchMediaAndNativeDetailsAreStubs:true});await dispose(c);
}
{
 const c=footerContext(false);c.editor('load');c.editor('load');assert.equal(c.medias.length,1);assert.equal(c.medias[0].listeners.size,1);c.editor('unload');assert.equal(c.medias[0].listeners.size,0);assert.equal(c.root.bcfCleanup,undefined);c.editor('load');assert.equal(c.medias.length,2);assert.equal(c.medias[1].listeners.size,1);record('FT-02','CONTROL_PASSED',{repeatedSectionLoadDoesNotDuplicateListeners:true,unloadCleansMediaListener:true,reloadReinitializes:true});await dispose(c);
}

function glossaryContext(){const c=context('<section data-glossary-section><input data-glossary-search><nav><a data-glossary-az-link data-letter="A" href="#group-a">A</a><a data-glossary-az-link data-letter="R" href="#group-r">R</a></nav><p data-glossary-status></p><div data-glossary-group data-letter="A" id="group-a"><a data-glossary-term data-term="antraciet" data-keywords="grijs">A</a></div><div data-glossary-group data-letter="R" id="group-r"><a data-glossary-term data-term="rimless" data-keywords="randloos">R</a></div><div data-glossary-empty hidden>Empty</div></section><script></script>');Object.defineProperty(c.w.document,'currentScript',{configurable:true,get:()=>c.w.document.querySelector('script')});c.w.eval(scripts['sections/main-glossary.liquid']);c.search=value=>{const input=c.w.document.querySelector('input');input.value=value;input.dispatchEvent(new c.w.Event('input',{bubbles:true}));};return c;}
{
 const c=glossaryContext();c.search(' RANDLOOS ');assert.equal(c.w.document.querySelector('[data-glossary-status]').textContent,'1 begrip gevonden.');assert.equal(c.w.document.getElementById('group-a').hidden,true);assert.equal(c.w.document.getElementById('group-r').hidden,false);c.search('synthetic-missing');assert.equal(c.w.document.querySelector('[data-glossary-empty]').hidden,false);c.search('');assert.equal(c.w.document.querySelector('[data-glossary-status]').textContent,'2 begrippen beschikbaar.');assert.equal(c.w.document.getElementById('group-a').hidden,false);record('GL-01','CONTROL_PASSED',{trimCaseAndKeywordsMatch:true,emptyAndClearRestore:true});await dispose(c);
}
{
 const c=glossaryContext();c.search('rimless');const anchor=c.w.document.querySelector('[data-letter="A"]');assert.equal(anchor.getAttribute('aria-disabled'),'true');assert.equal(anchor.getAttribute('href'),'#group-a');const click=new c.w.Event('click',{bubbles:true,cancelable:true});anchor.dispatchEvent(click);assert.equal(click.defaultPrevented,false);record('GL-02','BOUNDARY_CONFIRMED',{ariaDisabledAZAnchorRetainsHrefAndIsNotPrevented:true,targetGroupHidden:true,realKeyboardOrScrollOutcomeNotTested:true});await dispose(c);
}
function tocContext(body){const c=context('<section data-glossary-page><div class="bc-glossary-page__content">'+body+'</div><nav data-glossary-page-toc hidden><ol data-glossary-page-toc-list></ol></nav></section><script></script>');Object.defineProperty(c.w.document,'currentScript',{configurable:true,get:()=>c.w.document.querySelector('script')});c.run=()=>c.w.eval(scripts['sections/main-glossary-page.liquid']);c.run();return c;}
for(const count of [0,1,2]){const c=tocContext('<p>Summary</p>'+Array.from({length:count},(_,i)=>`<h2>Section ${i}</h2><p>Text</p>`).join(''));assert.equal(c.w.document.querySelectorAll('.bc-glossary-page__content-card').length,count);assert.equal(c.w.document.querySelector('[data-glossary-page-toc]').hidden,count<=1);c.run();assert.equal(c.w.document.querySelectorAll('[data-glossary-page-toc-list] li').length,count);record('TOC-0'+count,'CONTROL_PASSED',{directH2Count:count,tocVisible:count>1,secondScriptRunDoesNotDuplicateExistingCards:true});await dispose(c);}
{
 const c=tocContext('<div><h2>Nested heading</h2><p>Text</p></div><h2 id="stable-id">Direct heading</h2><p>Text</p>');assert.equal(c.w.document.querySelectorAll('.bc-glossary-page__content-card').length,1);assert.equal(c.w.document.querySelector('a').getAttribute('href'),'#stable-id');record('TOC-03','BOUNDARY_CONFIRMED',{nestedH2NotAddedToTOC:true,existingDirectIdPreserved:true});await dispose(c);
}
{
 const c=tocContext('<h2 id="begrip-section-2">First</h2><p>A</p><h2>Second</h2><p>B</p>');assert.equal(c.w.document.querySelectorAll('[id="begrip-section-2"]').length,2);record('TOC-04','BOUNDARY_CONFIRMED',{existingIdCanCollideWithGeneratedId:true,duplicateTargetIdCount:2,syntheticContentOnly:true,notObservedInCurrentLiveBodies:true});await dispose(c);
}
function disclosureContext({reduced=false,specs=false,phone=true}={}){
 const rows=specs?Array.from({length:12},(_,i)=>`<div class="bc-product-specs__row" data-row="${i}">Row</div>`).join(''):'';
 const c=context(`<bc-product-disclosure ${specs?'data-disclosure-mode="specs"':''}><div data-disclosure-viewport><div data-disclosure-content><a href="#visible" data-position="above">Above</a><a href="#hidden" data-position="below" tabindex="2">Below</a>${rows}</div></div><button data-disclosure-toggle>More</button></bc-product-disclosure>`);
 const {w}=c;c.animations=[];c.scrolls=[];c.frames=new Map();let frameId=0;
 Object.defineProperty(w.document,'fonts',{configurable:true,value:{ready:Promise.resolve()}});
 w.ResizeObserver=class{constructor(fn){this.fn=fn;c.observer=this;}observe(){}disconnect(){this.disconnected=true;}};
 w.requestAnimationFrame=fn=>{const id=++frameId;c.frames.set(id,fn);return id;};w.cancelAnimationFrame=id=>c.frames.delete(id);
 w.getComputedStyle=()=>({lineHeight:'20px'});
 w.HTMLElement.prototype.getBoundingClientRect=function(){let top=0,height=20;if(this.matches('bc-product-disclosure'))top=50;if(this.hasAttribute('data-disclosure-content'))height=specs?120:200;if(this.hasAttribute('data-disclosure-viewport'))height=this.style.height==='auto'?(specs?120:200):(parseFloat(this.style.height)||80);if(this.dataset.position==='above'){top=20;height=20;}if(this.dataset.position==='below'){top=110;height=10;}if(this.dataset.row){top=Number(this.dataset.row)*10;height=10;}return {top,bottom:top+height,height,left:0,right:300,width:300};};
 w.HTMLElement.prototype.scrollIntoView=function(options){c.scrolls.push(options);};
 w.HTMLElement.prototype.animate=function(frames,options){let resolve;const animation={frames,options,finished:new Promise(a=>{resolve=a;}),cancel(){this.cancelled=true;},finish:()=>resolve()};c.animations.push(animation);return animation;};
 c.medias={};w.matchMedia=query=>{const listeners=new Set(),media={matches:query.includes('max-width')?phone:reduced,addEventListener:(type,fn,options)=>{listeners.add(fn);options?.signal?.addEventListener('abort',()=>listeners.delete(fn),{once:true});},set(value){this.matches=value;listeners.forEach(fn=>fn());}};c.medias[query.includes('max-width')?'phone':'reduce']=media;return media;};
 w.eval(sources['assets/bc-product-disclosure.js']);c.root=w.document.querySelector('bc-product-disclosure');c.viewport=c.root.querySelector('[data-disclosure-viewport]');c.button=c.root.querySelector('button');c.below=c.root.querySelector('[data-position=below]');return c;
}
{
 const c=disclosureContext();assert.equal(c.root.collapsedHeight,80);assert.equal(c.below.getAttribute('tabindex'),'-1');c.button.click();assert.equal(c.below.getAttribute('tabindex'),'2');assert.equal(c.animations[0].options.duration,320);c.animations[0].finish();await settle();assert.equal(c.viewport.style.height,'auto');c.button.click();c.animations[1].finish();await settle();assert.equal(c.viewport.style.height,'80px');assert.equal(c.below.getAttribute('tabindex'),'-1');assert.equal(c.scrolls[0].behavior,'smooth');record('DS-01','CONTROL_PASSED',{fourLineClampUsesMeasuredLineHeight:true,belowClampTabindexRestoredOnExpand:true,animationMs:320,closeRestoresClamp:true,geometryAndAnimationsStubbed:true});await dispose(c);
}
{
 const c=disclosureContext();c.button.click();const old=c.animations[0];c.button.click();assert.equal(old.cancelled,true);old.finish();await settle();assert.equal(c.root.expanded,false);assert.equal(c.viewport.style.height,'80px');c.animations[1].finish();await settle();assert.equal(c.button.getAttribute('aria-expanded'),'false');record('DS-02','CONTROL_PASSED',{rapidReversalCancelsOldAnimation:true,lateOldCompletionCannotRestoreExpandedHeight:true});await dispose(c);
}
{
 const c=disclosureContext({reduced:true});c.button.click();assert.equal(c.viewport.style.height,'auto');c.button.click();assert.equal(c.animations.length,0);assert.equal(c.scrolls[0].behavior,'instant');record('DS-03','CONTROL_PASSED',{reducedMotionBypassesAnimation:true,collapseScrollInstant:true});await dispose(c);
}
{
 const c=disclosureContext({specs:true,phone:false});assert.equal(c.button.hidden,true);assert.equal(c.below.getAttribute('tabindex'),'2');c.medias.phone.set(true);assert.equal(c.root.collapsedHeight,100);assert.equal(c.button.hidden,false);assert.equal(c.below.getAttribute('tabindex'),'-1');c.medias.phone.set(false);assert.equal(c.viewport.style.height,'auto');assert.equal(c.below.getAttribute('tabindex'),'2');record('DS-04','CONTROL_PASSED',{specsDesktopFullyOpen:true,syntheticPhoneClampsAfterTenRows:true,breakpointChangeRestoresTabindex:true,notRealMobileEvidence:true});await dispose(c);
}
{
 const c=disclosureContext();assert.equal(c.below.getAttribute('tabindex'),'-1');c.root.remove();await settle();assert.equal(c.below.getAttribute('tabindex'),'2');assert.equal(c.observer.disconnected,true);assert.equal(c.frames.size,0);record('DS-05','CONTROL_PASSED',{disconnectRestoresOriginalTabindexAndStopsObserverFrames:true});await dispose(c);
}
const report={schemaVersion:1,themeId:manifest.themeId,environment:{node:process.version,dom:'happy-dom 21.0.4'},safety:{realNetwork:false,realCartActions:false,productionWrites:false,syntheticFixturesOnly:true},scope:'Actual hash-checked source in DOM simulation. Native constraints, browser/CSS/touch, server cart outcomes and occurrence frequency are not certified.',results};
fs.mkdirSync(path.dirname(args.output),{recursive:true});fs.writeFileSync(args.output,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({cases:results.length,classifications:results.reduce((a,r)=>(a[r.classification]=(a[r.classification]||0)+1,a),{})}));
