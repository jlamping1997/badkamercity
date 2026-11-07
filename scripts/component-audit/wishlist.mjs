// Offline replay of hash-verified wishlist code. Every request is synthetic.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const argv=process.argv.slice(2),args={};
for(let i=0;i<argv.length;i+=2)args[argv[i].replace(/^--/,'')]=argv[i+1];
if(!args.source||!args.manifest||!args.output)throw Error('Use --source THEME --manifest PROVENANCE --output RESULT [--dom-module MODULE]');
const {Window}=await import(args['dom-module']||'happy-dom');
const manifest=JSON.parse(fs.readFileSync(args.manifest,'utf8')),source={},results=[];
for(const name of ['assets/bc-wishlist.js','assets/bc-sunshower-shop.js']){
 const bytes=fs.readFileSync(path.join(args.source,name));
 if(crypto.createHash('sha256').update(bytes).digest('hex')!==manifest.files.find(f=>f.path===name)?.sha256)throw Error('Unverified source '+name);
 source[name]=bytes.toString('utf8');
}
const KEY='bc_wishlist_v1';
const tick=()=>new Promise(r=>setImmediate(r));
async function settle(){for(let i=0;i<8;i++)await tick();}
const record=(id,classification,observations)=>results.push({id,classification,observations});
const entry=(handle='fixture-a',variantId='10001',source='detail')=>({handle,variantId,title:'Synthetic '+handle,image:'',source,savedAt:1700000000000});
const product=(patch={})=>({handle:'fixture-a',title:'Current synthetic title',featured_image:'',images:[],variants:[{id:10001,title:'Default Title',price:12345,available:true}],...patch});
const response=data=>({ok:true,json:async()=>data});
function deferred(){let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return {promise,resolve:data=>resolve(response(data)),reject};}
function button(handle='fixture-a',variant='10001',extra=''){
 return `<button type="button" data-bc-wishlist-toggle data-bc-wishlist-handle="${handle}" data-bc-wishlist-variant="${variant}" data-bc-wishlist-title="Synthetic title" data-bc-wishlist-source="detail" ${extra}>Heart</button>`;
}
const page='<section data-bc-wishlist-page><p data-bc-wishlist-page-count></p><p data-bc-wishlist-loading></p><div data-bc-wishlist-empty hidden></div><div data-bc-wishlist-grid role="list" hidden></div></section>';
async function fixture({initial=[],raw,html='',withPage=false,shared,denyRead=false,denyWrite=false,handler,boot=true,observer=false}={}){
 const w=new Window({url:'https://audit.invalid/pages/verlanglijst'}),store=shared||new Map(),c={w,store,calls:[],moves:[],events:[],frames:new Map(),timers:new Map(),unexpected:[],probes:[],denyRead,denyWrite};let serial=0;
 if(!shared)store.set(KEY,raw===undefined?JSON.stringify(initial):raw);
 Object.defineProperty(w.document,'readyState',{configurable:true,value:'complete'});
 Object.defineProperty(w,'localStorage',{configurable:true,value:{getItem(key){if(c.denyRead)throw Error('Synthetic read denied');return store.get(key)??null;},setItem(key,value){if(c.denyWrite)throw Error('Synthetic quota denied');store.set(key,String(value));},removeItem:key=>store.delete(key)}});
 w.setTimeout=(fn,delay)=>{const id=++serial;c.timers.set(id,{fn,delay});return id;};w.clearTimeout=id=>c.timers.delete(id);
 w.requestAnimationFrame=fn=>{const id=++serial;c.frames.set(id,fn);return id;};w.cancelAnimationFrame=id=>c.frames.delete(id);
 if(!observer)w.MutationObserver=class{observe(){}disconnect(){}};
 w.location.assign=url=>c.moves.push(String(url));
 // No image transport: the Sunshower preload is resolved explicitly by a case.
 w.Image=class {constructor(){c.probes.push(this);this.complete=false;this.naturalWidth=0;}set src(value){this._src=value;}get src(){return this._src;}success(){this.naturalWidth=480;this.complete=true;this.onload?.();}failure(){this.onerror?.();}};
 w.routes={cart_add_url:'/cart/add',cart_url:'/cart'};
 w.fetch=(url,options={})=>{
  const value=String(url),isProduct=/^\/products\/[a-z0-9-]+\.js$/.test(value)&&!options.method,isAdd=value==='/cart/add.js'&&options.method==='POST';
  if(!isProduct&&!isAdd){c.unexpected.push(value);return Promise.reject(Error('Unstubbed request denied'));}
  const call={url:value,method:options.method||'GET',credentials:options.credentials,body:options.body?JSON.parse(options.body):undefined};c.calls.push(call);
  return handler?handler(call,c):Promise.resolve(response(isAdd?{id:10001}:product()));
 };
 w.document.body.innerHTML=`<main id="MainContent"><a class="bc-header__utility-link--wishlist"><span data-bc-wishlist-count hidden>0</span></a>${html}${withPage?page:''}</main>`;
 w.document.addEventListener('bc:wishlist-changed',e=>c.events.push(e.detail.count));
 c.boot=()=>w.eval(source['assets/bc-wishlist.js']);
 c.click=node=>node.dispatchEvent(new w.MouseEvent('click',{bubbles:true,cancelable:true,button:0}));
 c.toggle=()=>w.document.querySelector('[data-bc-wishlist-toggle]');
 c.frame=()=>{for(const [id,fn]of [...c.frames]){c.frames.delete(id);fn();}};
 c.fire=delay=>{for(const [id,t]of [...c.timers])if(t.delay===delay){c.timers.delete(id);t.fn();}};
 c.storage=key=>w.dispatchEvent(new w.StorageEvent('storage',{key}));
 c.list=()=>JSON.parse(JSON.stringify(w.BCWishlist.list()));c.count=()=>w.document.querySelector('[data-bc-wishlist-count]');
 c.message=()=>w.document.getElementById('BCWishlistStatus')?.textContent||'';
 if(boot){c.boot();await settle();}return c;
}
async function dispose(c){assert.deepEqual(c.unexpected,[]);await c.w.happyDOM.abort();c.w.close();}
{
 const c=await fixture({withPage:true});assert.deepEqual(c.list(),[]);assert.equal(c.count().hidden,true);assert.equal(c.w.document.querySelector('[data-bc-wishlist-empty]').hidden,false);assert.equal(c.w.document.querySelector('[data-bc-wishlist-grid]').hidden,true);record('WL-01','CONTROL_PASSED',{emptyState:true,noRequests:c.calls.length===0});await dispose(c);
}
{
 const item={...entry('  FIXTURE-A  ',' 10001 '),title:'T'.repeat(200),image:'I'.repeat(900),source:'unknown'};const c=await fixture({initial:[null,{},entry('bad/handle'),entry('fixture-a','1234'),item]});assert.equal(c.list().length,1);const x=c.list()[0];assert.equal(x.handle,'fixture-a');assert.equal(x.variantId,'10001');assert.equal(x.title.length,180);assert.equal(x.image.length,800);assert.equal(x.source,'card');record('WL-02','CONTROL_PASSED',{invalidEntriesDropped:true,stringsNormalisedAndBounded:true,unknownSourceBecomesCard:true});await dispose(c);
}
for(const [id,raw]of [['WL-03','{broken'],['WL-04','{"version":1,"items":[]}']]){
 const c=await fixture({raw});assert.equal(c.list().length,0);assert.equal(c.store.get(KEY),raw);record(id,'BOUNDARY_CONFIRMED',{badOrDifferentSchemaReadsEmpty:true,originalBytesRetained:true,noMigrationOrRepair:true});await dispose(c);
}
{
 const c=await fixture({denyRead:true});assert.equal(c.list().length,0);assert.equal(c.message(),'');record('WL-05','BOUNDARY_CONFIRMED',{readDeniedLooksEmpty:true,noReadErrorToast:true});await dispose(c);
}
{
 const c=await fixture({initial:Array.from({length:105},(_,i)=>entry('fixture-'+i,String(10000+i)))});assert.equal(c.list().length,100);assert.equal(JSON.parse(c.store.get(KEY)).length,105);record('WL-06','CONTROL_PASSED',{memoryLimit:100,loadDoesNotRewriteStorage:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry(),entry()]});assert.equal(c.list().length,2);assert.equal(c.count().textContent,'2');record('WL-07','BOUNDARY_CONFIRMED',{duplicateStoredIdentitiesRemain:true,badgeCountsEntries:true,noClaimNormalToggleCreatesDuplicates:true});await dispose(c);
}
{
 const old={...entry(),savedAt:1};const c=await fixture({initial:[old]});assert.equal(c.list()[0].savedAt,1);const list=c.w.BCWishlist.list();list[0].title='mutated copy';list.push(entry('other'));assert.equal(c.list().length,1);assert.notEqual(c.list()[0].title,'mutated copy');record('WL-08','CONTROL_PASSED',{listReturnsCopies:true,noExpiryForOldTimestamp:true,hasUsesExactStrings:c.w.BCWishlist.has('FIXTURE-A','10001')===false});await dispose(c);
}
{
 const c=await fixture({html:button()});c.click(c.toggle());await settle();assert.equal(c.list().length,1);assert.equal(c.toggle().getAttribute('aria-pressed'),'true');assert.deepEqual(c.events,[1]);assert.equal(c.count().textContent,'1');c.click(c.toggle());await settle();assert.equal(c.list().length,0);assert.deepEqual(c.events,[1,0]);assert.equal(c.calls.length,0);record('WL-09','CONTROL_PASSED',{knownVariantTogglesWithoutProductRequest:true,eventAfterCommitAndCountSync:true});await dispose(c);
}
{
 const c=await fixture({html:button(),denyWrite:true});const before=c.store.get(KEY);c.click(c.toggle());await settle();assert.equal(c.store.get(KEY),before);assert.equal(c.list().length,0);assert.equal(c.toggle().getAttribute('aria-pressed'),'false');assert.deepEqual(c.events,[]);assert.match(c.message(),/geblokkeerd/);assert.equal(c.toggle().dataset.bcWishlistBusy,undefined);record('WL-10','CONTROL_PASSED',{failedWritePreservesMemoryAndStorage:true,noSuccessEvent:true,busyReleased:true});await dispose(c);
}
{
 const initial=Array.from({length:100},(_,i)=>entry('fixture-'+i,String(10000+i)));const c=await fixture({initial,html:button('new-item','99999')});c.click(c.toggle());await settle();assert.equal(c.list().length,100);assert.match(c.message(),/maximaal 100/);c.toggle().dataset.bcWishlistHandle='fixture-0';c.toggle().dataset.bcWishlistVariant='10000';c.click(c.toggle());await settle();assert.equal(c.list().length,99);record('WL-11','CONTROL_PASSED',{fullListBlocksAdditionButAllowsRemoval:true});await dispose(c);
}
{
 const c=await fixture({html:`<product-info><product-form><form><input name="id" value="20002">${button()}</form></product-form></product-info>`});c.click(c.toggle());await settle();assert.equal(c.list()[0].variantId,'20002');record('WL-12','CONTROL_PASSED',{nearestFormVariantOverridesStaleButtonDataset:true});await dispose(c);
}
{
 const c=await fixture({html:`<section data-ss-page data-variant="30003"><form class="ss-product-form"><input name="id" value="20002">${button()}</form></section>`});c.click(c.toggle());await settle();assert.equal(c.list()[0].variantId,'30003');record('WL-13','CONTROL_PASSED',{sunshowerPageVariantOverridesForm:true});await dispose(c);
}
{
 const c=await fixture({html:button('fixture-a','')});c.click(c.toggle());await settle();assert.equal(c.list()[0].variantId,'10001');assert.equal(c.calls.length,1);assert.equal(c.calls[0].credentials,'same-origin');record('WL-14','CONTROL_PASSED',{unknownVariantUsesProductRead:true});await dispose(c);
}
{
 const p=product({variants:[{id:10001,available:false},{id:20002,available:true}]});const c=await fixture({html:button('fixture-a',''),handler:()=>Promise.resolve(response(p))});c.click(c.toggle());await settle();assert.equal(c.list()[0].variantId,'20002');record('WL-15','CONTROL_PASSED',{fallbackSelectsFirstAvailableVariant:true});await dispose(c);
}
{
 const c=await fixture({html:button('fixture-a',''),handler:()=>Promise.resolve(response(product({variants:[{id:10001,available:false}]})))});c.click(c.toggle());await settle();assert.equal(c.list()[0].variantId,'10001');record('WL-16','BOUNDARY_CONFIRMED',{savingUnavailableFavouriteAllowed:true,saveIsNotPurchaseEligibility:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry()],html:button('fixture-a','')});c.click(c.toggle());await settle();assert.equal(c.list().length,0);assert.equal(c.calls.length,0);record('WL-17','CONTROL_PASSED',{oneExistingVariantRemovedWithoutRead:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry(),entry('fixture-a','20002')],html:button('fixture-a','')});c.click(c.toggle());await settle();assert.equal(c.list().length,2);assert.match(c.message(),/productpagina/);assert.equal(c.calls.length,0);record('WL-18','CONTROL_PASSED',{ambiguousVariantsRequireProductPage:true});await dispose(c);
}
{
 const d=deferred();const c=await fixture({html:button('fixture-a',''),handler:()=>d.promise});c.click(c.toggle());c.click(c.toggle());assert.equal(c.calls.length,1);d.resolve(product());await settle();assert.equal(c.list().length,1);assert.deepEqual(c.events,[1]);record('WL-19','CONTROL_PASSED',{sameButtonPendingClickIgnored:true});await dispose(c);
}
{
 let attempt=0;const c=await fixture({html:button('fixture-a',''),handler:()=>++attempt===1?Promise.reject(Error('Synthetic failure')):Promise.resolve(response(product()))});c.click(c.toggle());await settle();assert.equal(c.list().length,0);c.click(c.toggle());await settle();assert.equal(c.calls.length,2);assert.equal(c.list().length,1);record('WL-20','CONTROL_PASSED',{failedProductCacheEvictedAndRetryWorks:true});await dispose(c);
}
{
 const c=await fixture({html:button()});c.store.set(KEY,JSON.stringify([entry()]));c.storage('unrelated');assert.equal(c.list().length,0);c.storage(KEY);assert.equal(c.list().length,1);assert.equal(c.toggle().getAttribute('aria-pressed'),'true');c.store.delete(KEY);c.storage(null);assert.equal(c.list().length,0);assert.deepEqual(c.events,[1,0]);record('WL-21','CONTROL_PASSED',{keyAndClearStorageEventsReloadAndNotify:true,unrelatedKeyIgnored:true});await dispose(c);
}
{
 const shared=new Map([[KEY,'[]']]),a=await fixture({shared,html:button('fixture-a','10001')}),b=await fixture({shared,html:button('fixture-b','20002')});a.click(a.toggle());await settle();b.storage(KEY);b.click(b.toggle());await settle();a.storage(KEY);assert.equal(a.list().length,2);assert.equal(b.list().length,2);record('WL-22','CONTROL_PASSED',{sequentialTabsKeepBothWhenStorageEventDeliveredBeforeSecondEdit:true});await dispose(a);await dispose(b);
}
{
 const shared=new Map([[KEY,'[]']]),a=await fixture({shared,html:button('fixture-a','10001')}),b=await fixture({shared,html:button('fixture-b','20002')});a.click(a.toggle());await settle();assert.equal(a.list().length,1);b.click(b.toggle());await settle();assert.equal(JSON.parse(shared.get(KEY)).length,1);assert.equal(JSON.parse(shared.get(KEY))[0].handle,'fixture-b');a.storage(KEY);b.storage(KEY);assert.equal(a.list().some(x=>x.handle==='fixture-a'),false);record('WL-23','DEFECT_REPRODUCED',{finding:'WISH-F01',secondTabWritesFromStaleMemory:true,firstFavouriteLost:true,storageEventsExplicitlyDelayed:true,noNativeMultiTabSchedulingClaim:true});await dispose(a);await dispose(b);
}
{
 const c=await fixture({initial:[entry()],withPage:true});assert.match(c.w.document.querySelector('.bc-wishlist-item__price').textContent,/123/);assert.equal(c.w.document.querySelector('[data-bc-wishlist-add]').dataset.bcWishlistAdd,'fixture-a:10001');assert.equal(c.w.document.querySelector('.bc-wishlist-item__title').textContent,'Current synthetic title');record('WL-24','CONTROL_PASSED',{pageUsesProductPriceAndExactVariant:true,eligibleDetailVariantGetsAddButton:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry('fixture-a','99999')],withPage:true});assert.equal(c.w.document.querySelector('[data-bc-wishlist-add]'),null);assert.match(c.w.document.querySelector('.bc-wishlist-item__delivery').textContent,/niet meer beschikbaar/);c.click(c.w.document.querySelector('[data-bc-wishlist-remove]'));await settle();assert.equal(c.list().length,0);assert.equal(c.w.document.querySelector('[data-bc-wishlist-empty]').hidden,false);record('WL-25','CONTROL_PASSED',{missingVariantHasNoPurchaseButtonAndCanBeRemoved:true});await dispose(c);
}
for(const [id,item,p] of [
 ['WL-26',entry('fixture-a','10001','sunshower'),product()],
 ['WL-27',entry('fixture-a','10001','card'),product({variants:[{id:10001,price:12345,available:true},{id:20002,price:222,available:true}]})],
 ['WL-28',entry(),product({requires_selling_plan:true})],
 ['WL-29',entry(),product({variants:[{id:10001,price:12345,available:true,quantity_rule:{min:2,increment:1}}]})],
 ['WL-30',entry(),product({variants:[{id:10001,price:12345,available:true,quantity_rule:{min:1,increment:2}}]})],
 ['WL-31',entry(),product({variants:[{id:10001,price:12345,available:false}]})]
]){
 const c=await fixture({initial:[item],withPage:true,handler:()=>Promise.resolve(response(p))});assert.equal(c.w.document.querySelector('[data-bc-wishlist-add]'),null);const primary=c.w.document.querySelector('.bc-wishlist-item__primary');assert.equal(primary.tagName,'A');assert.match(primary.href,/variant=10001/);assert.equal(c.calls.some(x=>x.method==='POST'),false);record(id,'CONTROL_PASSED',{complexOrUnavailableVariantKeepsProductLink:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry()],withPage:true,handler:()=>Promise.resolve({ok:false})});assert.equal(c.w.document.querySelector('[data-bc-wishlist-add]'),null);assert.match(c.w.document.querySelector('.bc-wishlist-item__price').textContent,/niet beschikbaar/);assert.equal(c.list().length,1);record('WL-32','CONTROL_PASSED',{productHTTPErrorKeepsFavouriteAndRemoval:true});await dispose(c);
}
{
 const d=deferred();const c=await fixture({initial:[entry()],withPage:true,handler:()=>d.promise});c.click(c.w.document.querySelector('[data-bc-wishlist-remove]'));await settle();d.resolve(product());await settle();assert.equal(c.w.document.querySelectorAll('[data-bc-wishlist-card]').length,0);assert.equal(c.list().length,0);record('WL-33','CONTROL_PASSED',{lateProductResponseCannotReviveRemovedCard:true});await dispose(c);
}
{
 const pending=[];const initial=Array.from({length:6},(_,i)=>entry('fixture-'+i,String(10000+i)));const c=await fixture({initial,withPage:true,handler:()=>{const d=deferred();pending.push(d);return d.promise;}});assert.equal(c.calls.length,4);pending[0].resolve(product());await settle();assert.equal(c.calls.length,5);record('WL-34','CONTROL_PASSED',{productWorkerLimitPerRender:4,nextItemStartsAfterCompletion:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry()],withPage:true});const add=c.w.document.querySelector('[data-bc-wishlist-add]');c.click(add);c.click(add);await settle();assert.equal(c.calls.filter(x=>x.method==='POST').length,1);assert.deepEqual(c.calls.find(x=>x.method==='POST').body,{id:10001,quantity:1});assert.deepEqual(c.moves,['/cart']);assert.equal(c.list().length,1);record('WL-35','CONTROL_PASSED',{syntheticAddPostsExactVariantOnce:true,successNavigatesToCartAndRetainsFavourite:true,noRealCartRequest:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry()],withPage:true,handler:call=>Promise.resolve(call.method==='POST'?{ok:false}:response(product()))});const add=c.w.document.querySelector('[data-bc-wishlist-add]');c.click(add);await settle();assert.equal(add.disabled,false);assert.equal(add.textContent,'In winkelwagen');assert.equal(c.moves.length,0);assert.match(c.message(),/niet aan de winkelwagen/);record('WL-36','CONTROL_PASSED',{syntheticAddErrorRestoresButton:true,noNavigationOnError:true});await dispose(c);
}
{
 let current=product();const c=await fixture({initial:[entry()],withPage:true,handler:call=>Promise.resolve(response(call.method==='POST'?{}:current))});current=product({variants:[{id:10001,available:false,price:99999}]});c.store.set(KEY,JSON.stringify([entry()]));c.storage(KEY);await settle();c.click(c.w.document.querySelector('[data-bc-wishlist-add]'));await settle();assert.equal(c.calls.filter(x=>x.method==='GET').length,1);assert.equal(c.calls.filter(x=>x.method==='POST').length,1);record('WL-37','BOUNDARY_CONFIRMED',{successCacheHasNoTTL:true,rerenderAndAddReuseCachedEligibility:true,serverRemainsCartAuthority:true,noPriceOrStockFreezeClaim:true});await dispose(c);
}
{
 const c=await fixture({initial:[entry()],withPage:true,handler:()=>new Promise(()=>{})});assert.equal(c.w.document.querySelector('.bc-wishlist-item__price').textContent,'Prijs ophalen…');assert.equal(c.timers.size,0);assert.equal(c.w.document.querySelector('[data-bc-wishlist-loading]').hidden,true);assert.ok(c.w.document.querySelector('[data-bc-wishlist-remove]'));record('WL-38','BOUNDARY_CONFIRMED',{noProductRequestTimeout:true,perCardLoadingCanRemainIndefinitely:true,removalStillPresent:true});await dispose(c);
}
{
 const malicious='<img src=x onerror="throw 1">';const c=await fixture({initial:[{...entry(),title:malicious,image:'javascript:alert(1)'}],withPage:true,handler:()=>Promise.resolve(response(product({title:malicious})))});assert.equal(c.w.document.querySelector('.bc-wishlist-item__title').textContent,malicious);assert.equal(c.w.document.querySelector('.bc-wishlist-item__title img'),null);assert.equal(c.w.document.querySelector('.bc-wishlist-item__media img').hidden,true);record('WL-39','CONTROL_PASSED',{titlesUseTextContent:true,javascriptImageRejected:true,notGeneralSecurityAudit:true});await dispose(c);
}
{
 const c=await fixture({html:'<article class="bc-filter-card"><h2 class="bc-filter-card__title"><a href="/products/fixture-a">Fixture A</a></h2></article>',observer:true});assert.ok(c.toggle());assert.equal(c.toggle().getAttribute('aria-pressed'),'false');c.toggle().dataset.bcWishlistVariant='10001';c.click(c.toggle());await settle();const card=c.w.document.querySelector('.bc-filter-card');card.insertAdjacentHTML('afterend','<article class="bc-standard-card">'+button('fixture-a','10001')+'</article>');await settle();c.frame();assert.equal(c.w.document.querySelector('.bc-standard-card button').getAttribute('aria-pressed'),'true');record('WL-40','CONTROL_PASSED',{externalCardsDecorated:true,actualDOMLibraryMutationObserverSchedulesNewCardSync:true});await dispose(c);
}
{
 const c=await fixture({html:button()});c.boot();c.click(c.toggle());await settle();assert.equal(c.list().length,1);assert.deepEqual(c.events,[1]);c.w.BCWishlist.refresh();c.w.BCWishlist.refresh();assert.equal(c.frames.size,1);c.frame();c.fire(2900);assert.equal(c.w.document.getElementById('BCWishlistStatus').hidden,true);record('WL-41','CONTROL_PASSED',{duplicateScriptBootGuard:true,refreshCoalescesOneFrame:true,toastHidesAfter2900msModel:true});await dispose(c);
}
{
 const c=await fixture({html:`<product-info><product-form><form><input name="id" value="10001">${button()}</form></product-form></product-info>`,initial:[entry()]});const field=c.w.document.querySelector('input');field.value='20002';field.dispatchEvent(new c.w.Event('change',{bubbles:true}));c.frame();assert.equal(c.toggle().getAttribute('aria-pressed'),'false');record('WL-42','CONTROL_PASSED',{variantChangeEventRefreshesPressedState:true});await dispose(c);
}
{
 const choices=['a','b'].map((key,i)=>({key,id:String(10001+i),available:true,url:'/products/fixture-'+key,title:'Synthetic '+key,image:{src:'https://images.audit.invalid/'+key+'.jpg'},price:'Synthetic price'}));
 const html=`<article data-bcsse-shop-card><script type="application/json" data-bcsse-shop-data>${JSON.stringify({initial:'a',choices})}</script><img data-bcsse-shop-image><a data-bcsse-shop-link href="/products/fixture-a">Product</a><h2 class="bcsse-accessory__title">Synthetic title</h2><span data-bcsse-shop-price></span><form data-bcsse-shop-form><input name="id" value="10001"><button data-bcsse-shop-submit><span data-bcsse-shop-button-label>Add</span></button></form><p data-bcsse-shop-status></p><a data-bcsse-shop-choice="b" href="/products/fixture-b">B</a>${button().replace('data-bc-wishlist-source="detail"','data-bc-wishlist-source="card"')}</article>`;
 const c=await fixture({html,initial:[entry()],boot:false,observer:true});c.w.eval(source['assets/bc-sunshower-shop.js']);c.boot();await settle();assert.equal(c.toggle().getAttribute('aria-pressed'),'true');c.click(c.w.document.querySelector('[data-bcsse-shop-choice="b"]'));assert.equal(c.probes.length,1);c.probes[0].success();await settle();c.frame();assert.equal(c.w.document.querySelector('input').value,'10002');assert.match(c.w.document.querySelector('[data-bcsse-shop-link]').href,/fixture-b/);assert.equal(c.w.BCWishlist.has('fixture-b','10002'),false);assert.equal(c.toggle().getAttribute('aria-pressed'),'true');assert.equal(c.toggle().classList.contains('is-saved'),true);c.click(c.toggle());await settle();assert.equal(c.w.BCWishlist.has('fixture-b','10002'),true);record('WL-43','DEFECT_REPRODUCED',{finding:'WISH-F02',realSunshowerControllerCommitsNewHandleAndVariant:true,heartPressedAndClassRetainPreviousSavedState:true,nextHeartClickUsesCorrectNewIdentity:true,imagePreloadExplicitlySimulated:true});await dispose(c);
}
const counts=Object.fromEntries(['CONTROL_PASSED','DEFECT_REPRODUCED','BOUNDARY_CONFIRMED'].map(k=>[k,results.filter(r=>r.classification===k).length]));
const report={task:'DOC-03D',sourceTheme:manifest.themeId,node:process.version,dom:'happy-dom 21.0.4',executedSources:Object.keys(source),sourceSha256:manifest.files.filter(f=>source[f.path]).map(f=>({path:f.path,sha256:f.sha256})),caseCount:results.length,classifications:counts,limitations:['Synthetic storage only; storage event delivery is manual, not native cross-tab scheduling.','All product and cart responses are synthetic; zero actual cart or storefront requests.','Timers, navigation, image preloads and request transport are stubs; no CSS, layout, focus, screen reader, touch or native browser proof.','MutationObserver is disabled except WL-40 and WL-43, which use the DOM library observer.','No account sync, checkout, real customer storage, cart restore or current business product data inspected.'],results};
fs.writeFileSync(args.output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({cases:results.length,...counts}));
