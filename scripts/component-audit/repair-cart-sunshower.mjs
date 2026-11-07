// Offline contract replay against explicitly supplied, hash-checked theme sources.
// All fetches, navigation, dialog timing and observers are local test doubles.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const args=Object.fromEntries(process.argv.slice(2).reduce((pairs,value,index,all)=>{
  if(index%2===0)pairs.push([value.replace(/^--/,''),all[index+1]]);return pairs;
},[]));
if(!args.source || !args.manifest || !args.output)throw Error('Use --source THEME --manifest SOURCE_PROVENANCE --output RESULT_JSON [--dom-module MODULE]');
const {Window}=await import(args['dom-module'] || 'happy-dom');
const manifest=JSON.parse(fs.readFileSync(args.manifest,'utf8'));
const source={};
for(const name of ['assets/cart-notification.js','assets/bc-product-switcher.js','assets/bc-sunshower-page.js','assets/bc-product-inbouw.js']){
  const raw=fs.readFileSync(path.join(args.source,name));
  const expected=manifest.files.find(row=>row.path===name);
  if(!expected || crypto.createHash('sha256').update(raw).digest('hex')!==expected.sha256)throw Error('Unverified source '+name);
  source[name]=raw.toString('utf8');
}
const results=[];
const tick=()=>new Promise(resolve=>setImmediate(resolve));
async function settle(){await tick();await tick();}
function context(html){
  const w=new Window({url:'https://audit.invalid/products/base',width:390,height:844});
  const moves=[];
  Object.defineProperty(w,'location',{configurable:true,value:{origin:'https://audit.invalid',pathname:'/products/base',search:'',href:'https://audit.invalid/products/base',assign:url=>moves.push(String(url)),reload:()=>moves.push('reload')}});
  Object.defineProperty(w.document,'readyState',{configurable:true,value:'complete'});
  w.fetch=()=>{throw Error('No unstubbed network allowed');};
  w.ResizeObserver=class {observe(){} disconnect(){}};
  w.IntersectionObserver=class {observe(){} disconnect(){}};
  w.document.body.innerHTML=html;
  return {w,moves};
}
async function dispose(w){await w.happyDOM.abort();w.close();}
function record(id,classification,observations){results.push({id,classification,observations});}

// CartNotification: real DOMParser, controlled native-dialog methods/timers.
function cartContext(reduced=false){
  const {w}=context('<button id="opener">Open</button><cart-notification><dialog id="cart-notification"><button data-cart-close>Close</button><div id="cart-notification-product"></div><div id="cart-notification-button"></div></dialog></cart-notification><div id="cart-icon-bubble"></div>');
  const dialog=w.document.querySelector('dialog');
  dialog.showModal=()=>{dialog.open=true;};
  dialog.close=()=>{dialog.open=false;dialog.dispatchEvent(new w.Event('close'));};
  dialog.getBoundingClientRect=()=>({left:10,right:100,top:10,bottom:100});
  let id=0;const timers=new Map(),frames=new Map();
  w.setTimeout=(fn,delay)=>{const key=++id;timers.set(key,{fn,delay});return key;};
  w.clearTimeout=key=>timers.delete(key);
  w.requestAnimationFrame=fn=>{const key=++id;frames.set(key,fn);return key;};
  w.cancelAnimationFrame=key=>frames.delete(key);
  w.matchMedia=()=>({matches:reduced});
  w.eval(source['assets/cart-notification.js']);
  const component=w.document.querySelector('cart-notification');
  const flush=()=>{for(const [key,timer] of [...timers]){timers.delete(key);timer.fn();}};
  const frame=()=>{for(const [key,fn] of [...frames]){frames.delete(key);fn();}};
  return {w,dialog,component,timers,flush,frame};
}
function payload(key,label){return {key,sections:{'cart-notification-product':`<div id="cart-notification-product-${key}">${label}</div>`,'cart-notification-button':'<div class="shopify-section">Cart</div>','cart-icon-bubble':'<div class="shopify-section">Badge</div>'}};}
{
  const c=cartContext();c.component.renderContents(payload('a','Synthetic article A'));c.frame();
  assert.equal(c.w.document.getElementById('cart-notification-product').textContent,'Synthetic article A');
  c.component.renderContents(payload('b','Synthetic article B'));
  assert.equal(c.w.document.getElementById('cart-notification-product').textContent,'Synthetic article B');
  record('CN-01','CONTROL_PASSED',{completeResponseReplacesProduct:true});await dispose(c.w);
}
for(const value of [undefined,null]){
  const c=cartContext();c.component.renderContents(payload('a','Synthetic article A'));
  c.component.renderContents({key:'b',sections:value===undefined?{}:{'cart-notification-product':null}});
  const actual=c.w.document.getElementById('cart-notification-product').textContent;
  assert.equal(actual,'');assert.equal(c.dialog.open,true);
  record(value===undefined?'CN-02':'CN-03','REGRESSION_PASSED',{input:value===undefined?'missing product section':'null product section',stalePriorProductCleared:true,dialogOpen:true});await dispose(c.w);
}
{
  const c=cartContext();c.component.renderContents(payload('a','Synthetic article A'));
  c.component.renderContents({key:'b',sections:{'cart-notification-product':'<div class="shopify-section">No matching product key</div>'}});
  assert.equal(c.w.document.getElementById('cart-notification-product').textContent,'');
  record('CN-04','CONTROL_PASSED',{stringSectionWithMissingKeyClearsProduct:true});await dispose(c.w);
}
{
  const c=cartContext();const style=c.w.document.documentElement.style;style.overflow='scroll';style.scrollbarGutter='auto';
  const opener=c.w.document.getElementById('opener');c.component.setActiveElement(opener);
  c.component.open();c.frame();c.component.close();c.component.open();c.flush();
  assert.equal(c.dialog.open,true);assert.equal(style.overflow,'hidden');
  c.component.close();c.flush();assert.equal(c.dialog.open,false);assert.equal(style.overflow,'scroll');assert.equal(style.scrollbarGutter,'auto');assert.equal(c.w.document.activeElement,opener);
  record('CN-05','CONTROL_PASSED',{reopenCancelsPendingClose:true,stylesAndOpenerFocusRestoredInStub:true});await dispose(c.w);
}
for(const reduce of [false,true]){
  const c=cartContext(reduce);c.component.open();c.dialog.dispatchEvent(new c.w.Event('cancel',{cancelable:true}));
  assert.equal([...c.timers.values()][0].delay,reduce?0:230);c.flush();assert.equal(c.dialog.open,false);
  record(reduce?'CN-07':'CN-06','CONTROL_PASSED',{cancelSchedulesCloseDelayMs:reduce?0:230,nativeBrowserBehaviorNotModeled:true});await dispose(c.w);
}

// V2 private helpers are exposed only in this instrumented sandbox copy.
{
  const {w}=context('');const text=source['assets/bc-product-switcher.js'];const end=text.lastIndexOf('})();');assert(end>=0);
  w.eval(text.slice(0,end)+'window.__audit={findExactMatch,hasPartialMatch,getDisplayType};\n'+text.slice(end));
  const api=w.__audit,menus=[{key:'kleur'}],a={handle:'a',options:{kleur:'White'}},b={handle:'b',options:{kleur:'White'}};
  assert.equal(api.findExactMatch([a],menus,{kleur:'White'}),a);
  assert.equal(api.findExactMatch([a,b],menus,{kleur:'White'}),undefined);
  assert.equal(api.findExactMatch([a],menus,{kleur:'Black'}),undefined);
  assert.equal(api.getDisplayType({},['1','2','3','4','5']),'buttons');
  assert.equal(api.getDisplayType({},['1','2','3','4','5','6']),'dropdown');
  record('V2-01','CONTROL_PASSED',{uniqueMatchAccepted:true,ambiguousAndMissingMatchRejected:true,noncompactFiveSixThreshold:true});await dispose(w);
}
{
  const {w}=context('<div data-bc-product-switcher-v2 data-switch-group="g" data-product-handle="a" data-product-url="/products/a" data-switcher-data-url="/primary.json" data-switcher-fallback-url="/fallback.json"></div>');
  const calls=[];w.fetch=async url=>{calls.push(url);return {ok:true,json:async()=>({groups:[]})};};
  w.eval(source['assets/bc-product-switcher.js']);await settle();
  assert.deepEqual(calls,['/primary.json']);assert.equal(w.document.querySelector('[data-bc-product-switcher-v2]').hidden,true);
  record('V2-02','BOUNDARY_CONFIRMED',{validJsonMissingGroupHidesControl:true,networkFallbackNotRequested:true,notEvidenceOfBrokenLiveDataset:true});await dispose(w);
}

{
  const {w}=context('<div data-bc-product-switcher-v2 data-switch-group="g" data-product-handle="a" data-product-url="/products/a" data-switcher-data-url="/primary.json" data-switcher-fallback-url="/fallback.json"></div>');
  const calls=[];w.fetch=async url=>{calls.push(url);if(url==='/primary.json')throw Error('Synthetic primary fetch failure');return {ok:true,json:async()=>({groups:[{id:'g',menus:[{key:'kleur',label:'Color'}],products:[{handle:'a',url:'/products/a',options:{kleur:'White'}},{handle:'b',url:'/products/b',options:{kleur:'Black'}}]}]})};};
  w.eval(source['assets/bc-product-switcher.js']);await settle();
  assert.deepEqual(calls,['/primary.json','/fallback.json']);assert.equal(w.document.querySelector('[data-bc-product-switcher-v2]').hidden,false);
  record('V2-03','CONTROL_PASSED',{primaryFetchFailureRequestsFallback:true,validFallbackRendersChoice:true});await dispose(w);
}

const sunHtml=`<div data-ss-page data-source="synthetic" data-variant="101" data-price="10000" data-currency="EUR" data-catalog="/catalog.json" data-add-url="/cart/add.js" data-cart-url="/cart" data-loading="Loading" data-choice-error="Choice failed" data-cart-error="Cart unconfirmed" data-busy-label="Adding">
 <div data-ss-field="kleur"><button type="button" data-ss-option="White" aria-pressed="true">White</button><button type="button" data-ss-option="Black" aria-pressed="false">Black</button></div><p data-ss-choice-status></p>
 <section class="ss-description"><div data-ss-description><div data-ss-description-content>Description</div></div><button data-ss-description-toggle data-more="More" data-less="Less"><span data-ss-description-label></span></button></section>
 <div data-ss-buybox><form><input data-ss-quantity name="quantity" type="number" value="1" min="1" step="1"><button type="submit" id="main-submit">Buy</button></form></div>
 <div data-ss-extra-row data-variant="202" data-price="500"><input type="checkbox" data-ss-extra></div>
 <b data-ss-total></b><button type="button" data-ss-add-set>Add set</button><p data-ss-cart-status></p><a data-ss-cart-check hidden>Check cart</a><div data-ss-sticky hidden></div></div>`;
{
  const {w,moves}=context(sunHtml);const calls=[];let rejectCart;
  w.fetch=(url,options)=>{calls.push({url,method:options?.method||'GET',body:options?.body});
    if(url==='/cart/add.js')return new Promise((resolve,reject)=>{rejectCart=reject;});
    if(url==='/catalog.json')return Promise.resolve({ok:true,json:async()=>({products:[{url:'/products/black',selection:{kleur:'Black'}}]})});
    throw Error('Unstubbed request');};
  w.eval(source['assets/bc-sunshower-page.js']);const button=w.document.querySelector('[data-ss-add-set]');button.click();
  const mainEnabled=!w.document.getElementById('main-submit').disabled;
  const color=w.document.querySelector('[data-ss-option="Black"]');const colorEnabled=!color.disabled;
  button.click();assert.equal(calls.filter(x=>x.method==='POST').length,1);
  color.click();await settle();assert.equal(moves.length,0);assert.equal(calls.filter(x=>x.method==='POST').length,1);
  assert.equal(mainEnabled,false);assert.equal(colorEnabled,false);
  record('SS-01','REGRESSION_PASSED',{duringPendingSetRequest:{setButtonDisabled:true,mainSubmitDisabled:!mainEnabled,colorDisabled:!colorEnabled},secondSetClickSuppressed:true,noColorNavigationBeforeSetResponse:true,allRequestsStubbed:true});
  rejectCart(Error('synthetic abort'));await settle();await dispose(w);
}
{
  const {w}=context(sunHtml);const calls=[];w.fetch=async(url,options)=>{calls.push(JSON.parse(options.body));return {ok:false,json:async()=>({status:422})};};
  w.eval(source['assets/bc-sunshower-page.js']);const qty=w.document.querySelector('[data-ss-quantity]');qty.value='2';
  const extra=w.document.querySelector('[data-ss-extra]');extra.checked=true;extra.dispatchEvent(new w.Event('change'));
  w.document.querySelector('[data-ss-add-set]').click();await settle();
  assert.equal(calls[0].items[0].quantity,2);assert.equal(calls[0].items[1].quantity,1);
  assert.equal(w.document.querySelector('[data-ss-add-set]').disabled,true);assert.equal(w.document.querySelector('[data-ss-cart-check]').hidden,false);
  record('SS-02','REGRESSION_PASSED',{parentQuantity:2,selectedExtraQuantity:1,failureOffersCartCheck:true,retryBlockedUntilCartReview:true,notARealCartOrStockTest:true});await dispose(w);
}

{
 const c=cartContext();const link=c.w.document.getElementById('cart-notification-button');c.component.cartButtonLabel='Bekijk winkelwagen';c.component.renderContents(payload('a','A'));c.component.renderContents({items:[{key:'b'}],sections:null});assert.equal(c.component.cartItemKey,'b');assert.equal(c.w.document.getElementById('cart-notification-product').textContent,'');assert.equal(link.textContent,'Bekijk winkelwagen');c.component.renderContents(payload('c','C'));assert.equal(c.w.document.getElementById('cart-notification-product').textContent,'C');record('CN-08','REGRESSION_PASSED',{multiItemKeySupported:true,nullSectionsClearIdentity:true,cartLinkGeneric:true,nextCompleteResponseRecovers:true});await dispose(c.w);
}
{
 const {w,moves}=context(sunHtml);let calls=0;w.fetch=()=>{calls++;return Promise.reject(Error('synthetic lost response'))};w.eval(source['assets/bc-sunshower-page.js']);const button=w.document.querySelector('[data-ss-add-set]');button.click();await settle();button.click();const event=new w.Event('pageshow');Object.defineProperty(event,'persisted',{value:true});w.dispatchEvent(event);button.click();assert.equal(calls,1);assert.equal(button.disabled,true);assert.equal(w.document.querySelector('[data-ss-cart-check]').hidden,false);assert.equal(moves.length,0);record('SS-03','REGRESSION_PASSED',{uncertainResponseNeverRetried:true,bfcacheCannotUnlockUnconfirmedPurchase:true});await dispose(w);
}
{
 const {w,moves}=context(sunHtml);let calls=0;w.fetch=async()=>{calls++;return {ok:true,json:async()=>({items:[{id:101}]})}};w.eval(source['assets/bc-sunshower-page.js']);w.document.querySelector('[data-ss-add-set]').click();await settle();assert.equal(calls,1);assert.deepEqual(moves,['/cart']);record('SS-04','CONTROL_PASSED',{confirmedSuccessNavigatesToCartOnce:true});await dispose(w);
}

{
  const {w}=context('<form><input name="id" value="101"><input name="quantity" type="number" min="1" step="1" value="2"></form>');
  w.eval(source['assets/bc-product-inbouw.js']);const proto=w.customElements.get('bc-inbouw-addon').prototype;
  const fake={form:w.document.querySelector('form'),dataset:{valid:'true',parentVariant:'101',bodyVariant:'202',parentSku:'SYNTHETIC-A',bodySku:'SYNTHETIC-B',quantityPerTrim:'1'}};
  assert.equal(proto.validIdentity.call(fake),true);fake.form.elements.namedItem('id').value='303';assert.equal(proto.validIdentity.call(fake),false);
  fake.form.elements.namedItem('id').value='101';fake.dataset.bodyVariant='101';assert.equal(proto.validIdentity.call(fake),false);
  record('IB-01','CONTROL_PASSED',{exactParentFormIdentityRequired:true,sameParentBodyVariantRejected:true});
  fake.dataset.bodyVariant='202';const qty=fake.form.elements.namedItem('quantity');
  assert.deepEqual(JSON.parse(JSON.stringify(proto.quantity.call(fake))),{quantity:2,bodyQuantity:2});
  for(const invalid of ['', '0', '2.5']){qty.value=invalid;assert.equal(proto.quantity.call(fake),null);}
  record('IB-02','CONTROL_PASSED',{twoParentsProduceTwoBodiesAtRatioOne:true,emptyZeroAndFractionRejected:true});
  const locked={ready:true,busy:false,uncertain:true,isConnected:true,pageLeaving:false,root:{dataset:{}}};
  assert.equal(proto.handleSubmit.call(locked,{}),true);
  record('IB-03','CONTROL_PASSED',{uncertainStateConsumesAndBlocksAnotherSubmit:true,noFetchReached:true});await dispose(w);
}

const report={schemaVersion:1,sourceThemeId:manifest.themeId,environment:{node:process.version,dom:'happy-dom 21.0.4'},safety:{realNetwork:false,realCartActions:false,productionCodeWrites:false,syntheticProductsOnly:true},scope:'Isolated replay of real source bytes; native browser focus, CSS, touch, server behavior and defect frequency are not certified.',results};
fs.mkdirSync(path.dirname(args.output),{recursive:true});fs.writeFileSync(args.output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({cases:results.length,classifications:results.reduce((all,row)=>(all[row.classification]=(all[row.classification]||0)+1,all),{})}));
