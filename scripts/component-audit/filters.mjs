// Offline whole-closure replay; real source bytes, synthetic responses and DOM.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const argv=process.argv.slice(2),args=Object.fromEntries(argv.reduce((a,v,i)=>(i%2===0&&a.push([v.replace(/^--/,''),argv[i+1]]),a),[]));
if(!args.source||!args.manifest||!args.output)throw Error('Use --source THEME --manifest PROVENANCE --output RESULT [--dom-module MODULE]');
const {Window}=await import(args['dom-module']||'happy-dom');
const manifest=JSON.parse(fs.readFileSync(args.manifest,'utf8')),source={},results=[];
for(const name of ['assets/bc-external-filters.js','assets/bc-mobile-listing.js','assets/facets.js']){const raw=fs.readFileSync(path.join(args.source,name));if(crypto.createHash('sha256').update(raw).digest('hex')!==manifest.files.find(r=>r.path===name)?.sha256)throw Error('Unverified source '+name);source[name]=raw.toString('utf8');}
const tick=()=>new Promise(resolve=>setImmediate(resolve));async function settle(){for(let i=0;i<6;i++)await tick();}
const record=(id,classification,observations)=>results.push({id,classification,observations});
const response=data=>({ok:true,json:async()=>data});
const product=(handle='fixture-a',id='101')=>({id,shopify_product_id:'gid://shopify/Product/'+id,handle,title:'Synthetic '+handle,vendor:'Fixture',price_cents:10000});
function facets(visible=6){return [
 {field:'price_cents',label:'Prijs',type:'number_decimal',data_type:'int64',min:0,max:50000,ui:{display_divisor:100,display_unit:'€'}},
 {field:'vendor',label:'Merk',type:'string',values:'ABCDEFGH'.split('').map(value=>({value,count:1})),ui:{visible_values:visible,searchable:true}},
 {field:'f_bool',label:'Eigenschap',type:'string',data_type:'bool',values:[{value:'true',count:1},{value:'false',count:1}]},
 {field:'f_count',label:'Aantal',type:'number_integer',data_type:'int32',min:1,max:4},
 {field:'f_exact',label:'Lengte',type:'number_integer',data_type:'int32',values:[{value:1000,count:1},{value:2000,count:1}],ui:{control:'single_select',display_divisor:1000,display_unit:'m'}},
 {field:'f_finish',label:'Afwerking',type:'string',values:[{value:'Brass',count:1},{value:'Gold',count:2}],ui:{option_groups:[{label:'Warm',exact_values:['Brass','Gold']}]}},
 {field:'f_serie',label:'Serie',type:'string',values:[{value:'Series',count:1}],ui:{section:'more'}},
 {field:'f_other',label:'Overig',type:'string',values:[{value:'Other',count:1}],ui:{section:'more'}}
];}
const valid=(patch={})=>({found:48,collection:{handle:'sample',profile_products:48},products:[product()],facets:facets(),...patch});
function deferred(){let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return {promise,resolve:data=>resolve(response(data)),reject};}
function cardData(handle='fixture-a',id='101',patch={}){return {id,handle,title:'Hydrated '+handle,short_title:'',vendor:'Fixture',color:'White',price_cents:12500,variant_id:'501',available:true,can_add:true,image_url:'',delivery_text:'Synthetic delivery',switcher_html:'',...patch};}
function sectionResponse(data){return response({'bc-card-data':`<script type="application/json" data-bc-card-data>${JSON.stringify(data).replaceAll('<','\\u003c')}</script>`});}
async function fixture({url='https://audit.invalid/collections/sample',search=false,drawer=false,hydrate=false,searchHandler,cardHandler,visible=6,emptyRoot=false}={}){
 const w=new Window({url,width:1363,height:936}),c={w,calls:[],cardCalls:[],moves:[],scrolls:[],timers:new Map(),frames:new Map(),medias:[],nativeEvents:0,unexpected:[]};let next=0;
 Object.defineProperty(w.document,'readyState',{configurable:true,value:'complete'});w.console.error=()=>{};
 w.setTimeout=(fn,delay)=>{const id=++next;c.timers.set(id,{fn,delay});return id;};w.clearTimeout=id=>c.timers.delete(id);
 w.requestAnimationFrame=fn=>{const id=++next;c.frames.set(id,fn);return id;};w.cancelAnimationFrame=id=>c.frames.delete(id);
 w.HTMLElement.prototype.scrollIntoView=function(options){c.scrolls.push(options);};
 const originalValidity=w.HTMLInputElement.prototype.checkValidity;
 // happy-dom 21.0.4 rejects exact decimal multiples via floating-point remainder.
 // Model numeric constraints explicitly; this is not native browser validation proof.
 w.HTMLInputElement.prototype.checkValidity=function(){
  if(this.type!=='number')return originalValidity.call(this);
  if(!this.value.trim())return !this.required;
  const n=Number(this.value);if(!Number.isFinite(n))return false;
  if(this.hasAttribute('min')&&n<Number(this.min))return false;
  if(this.hasAttribute('max')&&n>Number(this.max))return false;
  if(this.step==='any')return true;
  const step=Number(this.step)||1,base=this.hasAttribute('min')?Number(this.min):0,ratio=(n-base)/step;
  return Math.abs(ratio-Math.round(ratio))<1e-7;
 };
 w.HTMLInputElement.prototype.reportValidity=function(){return this.checkValidity();};
 w.HTMLElement.prototype.getClientRects=function(){return this.hidden||this.closest('[hidden]')?[]:[{top:0,bottom:40}];};
 w.location.assign=url=>c.moves.push(String(url));
 w.matchMedia=query=>{const callbacks=new Set(),media={query,matches:query.includes('989')?drawer:false,addEventListener:(name,fn)=>callbacks.add(fn),removeEventListener:(name,fn)=>callbacks.delete(fn),change(value){this.matches=value;callbacks.forEach(fn=>fn());}};c.medias.push(media);return media;};
 w.document.body.innerHTML=`<section class="${search?'template-search':'bc-collection'}">${emptyRoot?'':`<div id="BcExternalFilters" data-api-base="https://api.audit.invalid/verified" data-collection="${search?'__all__':'sample'}" data-products-count="${search?'':'48'}" data-search-mode="${search}" ${hydrate?'data-card-data-section="bc-card-data"':''} data-empty-label="Synthetic zero"></div>`}<div class="facets-vertical page-width"><aside id="${search?'main-search-filters':'main-collection-filters'}" style="display:grid">Native filters</aside><facet-filters-form class="${search?'template-search__toolbar':'facets-vertical-sort'}" style="display:flex"><form>Native sort</form></facet-filters-form><p data-bc-native-search-status>Native count</p><div id="ProductGridContainer"><ul id="product-grid"><li id="native-product">Native product</li></ul><div class="pagination-wrapper" style="display:block">Native pages</div></div></div></section>`;
 c.native=w.document.getElementById('native-product');c.nativeAside=w.document.querySelector('aside');
 w.addEventListener('popstate',()=>c.nativeEvents++);
 c.searchHandler=searchHandler||(()=>Promise.resolve(response(valid({facets:facets(visible),...(search?{collection:{handle:'__all__',profile_products:48}}:{})}))));
 c.cardHandler=cardHandler||((url)=>Promise.resolve(sectionResponse(cardData(decodeURIComponent(new URL(url).pathname.split('/').pop())))));
 w.fetch=(url,options={})=>{
  const href=String(url);
  if(href==='https://api.audit.invalid/verified/api/v1/search'&&options.body){const call={payload:JSON.parse(options.body),signal:options.signal,mode:options.mode,credentials:options.credentials};c.calls.push(call);return c.searchHandler(call);}
  if(href.startsWith('https://audit.invalid/products/')&&new URL(href).searchParams.get('sections')==='bc-card-data'){const call={url:href,signal:options.signal,credentials:options.credentials};c.cardCalls.push(call);return c.cardHandler(href,call);}
  c.unexpected.push(href);throw Error('Unstubbed request denied');
 };
 c.fire=delay=>{for(const [id,t]of [...c.timers])if(t.delay===delay){c.timers.delete(id);t.fn();}};
 c.frame=()=>{for(const [id,fn]of [...c.frames]){c.frames.delete(id);fn();}};
 c.sort=value=>{const node=w.document.getElementById('BcFilterSort');node.value=value;node.dispatchEvent(new w.Event('change',{bubbles:true}));};
 c.input=(field,kind,value,event='change')=>{const node=w.document.querySelector(`[data-range-field="${field}"][data-range-kind="${kind}"]`);node.value=value;node.dispatchEvent(new w.Event(event,{bubbles:true}));return node;};
 c.check=(field,value,checked=true)=>{const node=w.document.querySelector(`[data-filter-field="${field}"][value="${value}"]`);node.checked=checked;node.dispatchEvent(new w.Event('change',{bubbles:true}));};
 c.active=()=>w.document.documentElement.classList.contains('bc-external-filters-active');c.latest=()=>c.calls.at(-1).payload;
 w.eval(source['assets/bc-external-filters.js']);await settle();return c;
}
async function dispose(c){assert.deepEqual(c.unexpected,[]);await c.w.happyDOM.abort();c.w.close();}
function assertFallback(c){assert.equal(c.active(),false);assert.equal(c.w.document.getElementById('native-product'),c.native);assert.equal(c.nativeAside.style.display,'grid');assert.equal(c.w.document.querySelector('facet-filters-form').style.display,'flex');assert.equal(c.w.document.querySelector('.pagination-wrapper').style.display,'block');assert.equal(c.w.document.querySelector('.bc-filter-error').hidden,false);assert.equal(c.w.document.getElementById('ProductGridContainer').classList.contains('bc-filter-loading'),false);}
{
 const c=await fixture();assert.equal(c.calls.length,1);assert.equal(c.calls[0].credentials,'omit');assert.equal(c.calls[0].mode,'cors');assert.equal(c.latest().per_page,24);assert.equal(c.active(),true);record('FX-01','CONTROL_PASSED',{automaticActivationWithoutOptIn:true,searchReadCredentialsOmitted:true,perPage:24});await dispose(c);
}
{
 const c=await fixture({url:'https://audit.invalid/collections/sample?bcf_vendor=A&bcf_vendor=B&bcr_price_cents_min=1000&bcsort=price_desc&bcpage=3&utm_source=fixture#grid'});assert.deepEqual(c.latest().filters,{vendor:['A','B']});assert.deepEqual(c.latest().ranges,{price_cents:{min:1000}});assert.equal(c.latest().page,3);c.sort('price_asc');await settle();const u=new URL(c.w.location.href);assert.equal(u.searchParams.get('utm_source'),'fixture');assert.equal(u.hash,'#grid');assert.equal(u.searchParams.has('bcpage'),false);record('FX-02','CONTROL_PASSED',{customURLStateParsed:true,sortResetsPage:true,unrelatedQueryAndHashPreserved:true});await dispose(c);
}
{
 const c=await fixture({url:'https://audit.invalid/search?q=fixture&type=product,article&options%5Bprefix%5D=last',search:true});assert.equal(c.latest().collection,'__all__');assert.equal(c.latest().q,'fixture');c.check('vendor','A');await settle();assert.equal(c.latest().q,'fixture');assert.equal(new URL(c.w.location.href).searchParams.get('type'),'product,article');record('FX-03','CONTROL_PASSED',{productSearchUsesGlobalProfile:true,qAndSearchContextRetained:true});await dispose(c);
}
{
 const c=await fixture({url:'https://audit.invalid/search?q=fixture&type=article',search:true});assert.equal(c.calls.length,0);assert.equal(c.w.document.querySelector('.bc-filter-toolbar'),null);record('FX-04','CONTROL_PASSED',{nonProductSearchSkipped:true});await dispose(c);
}
{
 const c=await fixture();const before=c.calls.length;c.input('price_cents','min','100','input');c.input('price_cents','max','200','input');assert.equal(c.calls.length,before);c.fire(300);await settle();assert.equal(c.calls.length,before+1);assert.deepEqual(c.latest().ranges.price_cents,{min:10000,max:20000});record('FX-05','CONTROL_PASSED',{dualBoundDraftSurvivesDebounce:true,debounceMs:300,eurosConvertedToIntegerCents:true});await dispose(c);
}
{
 const c=await fixture();const before=c.calls.length;const n=c.input('f_count','max','1.5');assert.equal(n.checkValidity(),false);assert.equal(c.calls.length,before);record('FX-06','CONTROL_PASSED',{fractionalIntegerControlRejectedBeforeAPI:true});await dispose(c);
}
{
 const c=await fixture();c.input('price_cents','min','10');await settle();c.input('price_cents','max','20');await settle();c.input('price_cents','min','');await settle();assert.deepEqual(c.latest().ranges.price_cents,{max:2000});c.w.document.querySelector('[data-chip-range="price_cents"]').click();await settle();assert.deepEqual(c.latest().ranges,{});record('FX-07','CONTROL_PASSED',{oneBoundCanBeCleared:true,rangeChipRemovesWholeRange:true});await dispose(c);
}
{
 const c=await fixture();c.check('f_bool','true');await settle();assert.deepEqual(c.latest().filters.f_bool,['true']);assert.match(c.w.document.querySelector('.bc-filter-active').textContent,/Ja/);c.check('f_finish','Warm');await settle();assert.deepEqual(c.latest().filters.f_finish,['Brass','Gold']);record('FX-08','CONTROL_PASSED',{booleanLabelDoesNotChangeAPIBooleanString:true,groupedOptionSendsExactMemberValues:true});await dispose(c);
}
{
 const c=await fixture();const n=c.w.document.querySelector('[data-exact-field="f_exact"][value="2000"]');n.checked=true;n.dispatchEvent(new c.w.Event('change',{bubbles:true}));await settle();assert.deepEqual(c.latest().ranges.f_exact,{min:2000,max:2000});assert.match(c.w.document.querySelector('[data-chip-range="f_exact"]').textContent,/2 m/);record('FX-09','CONTROL_PASSED',{singleSelectUsesRawExactRange:true,displayDivisorAffectsLabelOnly:true});await dispose(c);
}
{
 const c=await fixture({url:'https://audit.invalid/collections/sample?bcf_vendor=A&bcr_price_cents_min=1000&bcsort=price_desc&bcpage=2&utm_source=fixture'});c.w.document.querySelector('[data-bc-clear-all]').click();await settle();assert.deepEqual(c.latest().filters,{});assert.deepEqual(c.latest().ranges,{});assert.equal(c.latest().page,1);assert.equal(c.latest().sort,'price_desc');assert.equal(new URL(c.w.location.href).searchParams.get('utm_source'),'fixture');record('FX-10','CONTROL_PASSED',{clearAllResetsFiltersRangesPageButRetainsSort:true});await dispose(c);
}
{
 const c=await fixture();c.w.document.querySelector('[data-page="2"]').click();await settle();assert.equal(c.latest().page,2);assert.equal(c.scrolls[0].behavior,'smooth');c.check('vendor','A');await settle();assert.equal(c.latest().page,1);record('FX-11','CONTROL_PASSED',{paginationWritesStateAndScrolls:true,newFilterReturnsToPageOne:true,scrollBehavior:'smooth without local reduced-motion check'});await dispose(c);
}
{
 const c=await fixture({searchHandler:()=>Promise.resolve(response(valid({found:0,products:[]})))});assert.equal(c.active(),true);assert.equal(c.w.document.querySelector('[data-bc-count]').textContent,'0 producten');assert.equal(c.w.document.querySelector('.bc-filter-empty').textContent,'Synthetic zero');record('FX-12','CONTROL_PASSED',{validZeroResultsRemainExternal:true});await dispose(c);
}
for(const [id,trigger,handler]of [
 ['FX-13','network',()=>Promise.reject(Error('synthetic failure'))],
 ['FX-14','HTTP',()=>Promise.resolve({ok:false,status:503})],
 ['FX-15','profile count mismatch',()=>Promise.resolve(response(valid({collection:{handle:'sample',profile_products:49}})))],
 ['FX-16','shape',()=>Promise.resolve(response(valid({found:-1})))],
 ['FX-17','global handle',()=>Promise.resolve(response(valid({collection:{handle:'wrong',profile_products:48}})))]
]){const c=await fixture({search:id==='FX-17',url:id==='FX-17'?'https://audit.invalid/search?q=fixture&type=product':undefined});c.searchHandler=handler;c.sort('price_asc');await settle();assertFallback(c);record(id,'CONTROL_PASSED',{trigger,originalNodesAndInlineDisplaysRestored:true});await dispose(c);}
{
 const c=await fixture();const a=deferred(),b=deferred();let i=0;c.searchHandler=()=>[a,b][i++].promise;c.sort('price_asc');c.sort('price_desc');assert.equal(c.calls.at(-2).signal.aborted,true);b.resolve(valid({products:[product('newest')]}));await settle();a.resolve(valid({products:[product('stale')]}));await settle();assert.match(c.w.document.querySelector('.bc-filter-card__title').textContent,/newest/);record('FX-18','CONTROL_PASSED',{newestRequestWinsEvenWhenOldTransportIgnoresAbort:true});await dispose(c);
}
{
 const c=await fixture();const a=deferred(),b=deferred();let i=0;c.searchHandler=()=>[a,b][i++].promise;c.sort('price_asc');c.sort('price_desc');b.resolve(valid());await settle();a.reject(Error('late old failure'));await settle();assert.equal(c.active(),true);assert.equal(c.w.document.querySelector('.bc-filter-error').hidden,true);record('FX-19','CONTROL_PASSED',{lateOldErrorCannotTriggerFallbackAfterNewSuccess:true});await dispose(c);
}
{
 const c=await fixture();c.searchHandler=call=>new Promise((a,b)=>call.signal.addEventListener('abort',()=>b(Error('synthetic timeout')),{once:true}));c.sort('price_asc');c.fire(12000);await settle();assertFallback(c);record('FX-20','CONTROL_PASSED',{timeoutMs:12000,nativeFallbackAfterAbort:true});await dispose(c);
}
{
 const c=await fixture();c.w.history.replaceState({},'','?bcf_vendor=B&bcpage=2');c.w.dispatchEvent(new c.w.PopStateEvent('popstate'));await settle();assert.equal(c.nativeEvents,0);assert.deepEqual(c.latest().filters,{vendor:['B']});assert.equal(c.latest().page,2);c.searchHandler=()=>Promise.reject(Error('synthetic'));c.sort('price_asc');await settle();c.w.dispatchEvent(new c.w.PopStateEvent('popstate'));await settle();assert.equal(c.nativeEvents,1);record('FX-21','CONTROL_PASSED',{externalPopstateOwnsEventWhileActive:true,nativeListenerReceivesEventAfterFallback:true,nativeListenerIsStubNotFacetsExecution:true});await dispose(c);
}
{
 const c=await fixture({visible:2});const visible=()=>[...c.w.document.querySelectorAll('[data-filter-group="vendor"] [data-option-label]')].filter(n=>!n.hidden).length;assert.equal(visible(),2);const button=c.w.document.querySelector('[data-filter-group="vendor"] [data-bc-show-values]');button.click();assert.equal(visible(),8);button.click();assert.equal(visible(),6);record('FX-22','DEFECT_REPRODUCED',{configuredVisibleValues:2,initialVisible:2,afterExpandCollapseVisible:6,conditionalSyntheticConfiguration:true,liveProfilesNotClaimedAffected:true});await dispose(c);
}
{
 const c=await fixture({searchHandler:()=>Promise.resolve(response(valid({collection:{handle:'other-collection',profile_products:48}})))});assert.equal(c.active(),true);record('FX-23','BOUNDARY_CONFIRMED',{sameCountWrongCollectionHandleAccepted:true,serverOccurrenceNotEstablished:true});await dispose(c);
}
{
 const c=await fixture({url:'https://audit.invalid/collections/sample?filter.p.vendor=A&sort_by=price-descending&page=2'});assert.deepEqual(c.latest().filters,{});assert.equal(c.latest().sort,'relevance');assert.equal(c.latest().page,1);c.check('vendor','B');await settle();const u=new URL(c.w.location.href);assert.equal(u.searchParams.get('filter.p.vendor'),'A');assert.equal(u.searchParams.get('bcf_vendor'),'B');record('FX-24','BOUNDARY_CONFIRMED',{nativeFilterSortPageNotTranslated:true,nativeAndExternalURLDialectsCoexist:true,initialServerFilteringNotSimulated:true});await dispose(c);
}
{
 const c=await fixture();c.input('price_cents','min','200');await settle();c.input('price_cents','max','100');await settle();assert.deepEqual(c.latest().ranges.price_cents,{min:20000,max:10000});record('FX-25','BOUNDARY_CONFIRMED',{invertedFiniteRangeReachesAPI:true,backendHandlingNotTested:true});await dispose(c);
}
{
 const c=await fixture({hydrate:true});assert.match(c.w.document.querySelector('.bc-filter-card__title').textContent,/Hydrated/);assert.equal(c.w.document.querySelector('[data-bc-card-cart]').disabled,false);assert.equal(c.cardCalls[0].credentials,'same-origin');record('FX-26','CONTROL_PASSED',{matchingShopifyIdHydratesCardAndAvailability:true});await dispose(c);
}
{
 const c=await fixture({hydrate:true,cardHandler:()=>Promise.resolve(sectionResponse(cardData('fixture-a','999')))});assert.match(c.w.document.querySelector('.bc-filter-card__title').textContent,/Synthetic/);assert.equal(c.w.document.querySelector('[data-bc-card-cart]').disabled,true);record('FX-27','CONTROL_PASSED',{mismatchedHydrationProductIdRejected:true,addRemainsDisabled:true});await dispose(c);
}
{
 let count=0;const c=await fixture({hydrate:true,cardHandler:()=>Promise.resolve(++count===1?{ok:false}:sectionResponse(cardData()))});assert.equal(c.w.document.querySelector('[data-bc-card-cart]').disabled,true);c.sort('price_asc');await settle();assert.equal(c.cardCalls.length,2);assert.equal(c.w.document.querySelector('[data-bc-card-cart]').disabled,false);record('FX-28','CONTROL_PASSED',{failedCardCacheEntryEvictedForRetry:true});await dispose(c);
}
{
 const c=await fixture({hydrate:true});const old=deferred(),fresh=deferred();c.cardHandler=url=>new URL(url).pathname.endsWith('/old')?old.promise:fresh.promise;let n=0;c.searchHandler=()=>Promise.resolve(response(valid({products:[product(++n===1?'old':'fresh',n===1?'111':'222')]})));c.sort('price_asc');await settle();c.sort('price_desc');await settle();fresh.resolve({'bc-card-data':`<script data-bc-card-data>${JSON.stringify(cardData('fresh','222'))}</script>`});await settle();old.resolve({'bc-card-data':`<script data-bc-card-data>${JSON.stringify(cardData('old','111'))}</script>`});await settle();assert.match(c.w.document.querySelector('.bc-filter-card__title').textContent,/fresh/);record('FX-29','CONTROL_PASSED',{staleHydrationCannotOverwriteNewGrid:true});await dispose(c);
}
{
 const c=await fixture({drawer:true});const sidebar=c.w.document.getElementById('BcFilterDrawer'),open=c.w.document.querySelector('[data-bc-open-filters]');assert.equal(sidebar.inert,true);open.focus();open.click();assert.equal(sidebar.inert,false);assert.equal(open.getAttribute('aria-expanded'),'true');const e=new c.w.KeyboardEvent('keydown',{key:'Escape',bubbles:true,cancelable:true});c.w.document.dispatchEvent(e);assert.equal(open.getAttribute('aria-expanded'),'false');assert.equal(c.w.document.activeElement,open);assert.equal(sidebar.inert,true);record('FX-30','CONTROL_PASSED',{syntheticDrawerEscapeRestoresOpenerAndInert:true,notRealMobileOrFocusTrapEvidence:true});await dispose(c);
}
{
 const c=await fixture({drawer:true});c.w.document.querySelector('[data-bc-open-filters]').click();c.medias.find(m=>m.query.includes('989')).change(false);const sidebar=c.w.document.getElementById('BcFilterDrawer');assert.equal(sidebar.hasAttribute('role'),false);assert.equal(sidebar.inert,false);assert.equal(c.w.document.documentElement.classList.contains('bc-filter-drawer-open'),false);record('FX-31','CONTROL_PASSED',{desktopQueryClosesDrawerAndRemovesDialogRole:true});await dispose(c);
}
{
 const c=await fixture();assert.equal(c.w.document.querySelector('[data-filter-group="vendor"] input[type="search"]'),null);assert.equal(c.w.document.querySelector('[data-filter-group="f_serie"]').closest('[data-bc-more-filters]'),null);record('FX-32','BOUNDARY_CONFIRMED',{searchableFlagDoesNotCreateOptionSearch:true,seriesForcedPrimaryDespiteMoreSection:true});await dispose(c);
}
{
 const c=await fixture();c.input('price_cents','max','200','input');const n=c.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]');n.focus();c.sort('price_asc');await settle();assert.equal(c.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]').value,'200');c.fire(300);await settle();assert.equal(c.latest().ranges.price_cents.max,20000);record('FX-33','CONTROL_PASSED',{rangeDraftSurvivesFilterDOMReplacementBeforeDebounce:true});await dispose(c);
}
{
 const html='<div data-bc-product-switcher-v2 data-switch-group="fixture-colors"><script type="application/json" data-bc-switcher-inline>'+JSON.stringify({groups:[{id:'fixture-colors',menus:[{key:'kleur'}],products:[{handle:'fixture-a',options:{kleur:'White'}},{handle:'fixture-b',options:{kleur:'Black'}},{handle:'fixture-c',options:{kleur:'Gold'}}]}]})+'</script></div>';
 const b=deferred(),d=deferred();const c=await fixture({hydrate:true,cardHandler:url=>{const h=new URL(url).pathname.split('/').pop();return h==='fixture-a'?Promise.resolve(sectionResponse(cardData('fixture-a','101',{switcher_html:html}))):h==='fixture-b'?b.promise:d.promise;}});
 c.w.document.querySelector('[data-bc-card-color="fixture-b"]').click();c.w.document.querySelector('[data-bc-card-color="fixture-c"]').click();d.resolve({'bc-card-data':`<script data-bc-card-data>${JSON.stringify(cardData('fixture-c','303',{color:'Gold'}))}</script>`});await settle();b.resolve({'bc-card-data':`<script data-bc-card-data>${JSON.stringify(cardData('fixture-b','202',{color:'Black'}))}</script>`});await settle();assert.equal(c.w.document.querySelector('.bc-filter-card').dataset.bcCardHandle,'fixture-c');assert.equal(c.w.document.querySelector('.bc-card-color').textContent,'Gold');assert.match(c.w.document.querySelector('.bc-card-view').href,/fixture-c/);record('FX-34','CONTROL_PASSED',{latestColorIntentWinsOverOutOfOrderSectionReads:true,handleColorAndLinkStayAligned:true});await dispose(c);
}
{
 const c=await fixture({hydrate:true,cardHandler:(url,call)=>new Promise((a,b)=>call.signal.addEventListener('abort',()=>b(Error('synthetic card timeout')),{once:true}))});c.fire(5000);await settle();assert.equal(c.active(),true);assert.equal(c.w.document.querySelector('[data-bc-card-cart]').disabled,true);assert.match(c.w.document.querySelector('.bc-filter-card__title').textContent,/Synthetic/);record('FX-35','CONTROL_PASSED',{cardTimeoutMs:5000,failedHydrationKeepsAddDisabledWithoutReplacingWholeList:true});await dispose(c);
}
{
 const c=await fixture({searchHandler:()=>Promise.reject(Error('first load failure'))});assertFallback(c);record('FX-36','CONTROL_PASSED',{initialFailureKeepsOriginalNativeNodes:true});await dispose(c);
}
{
 const c=await fixture();c.searchHandler=()=>Promise.reject(Error('force native fallback'));c.sort('price_asc');await settle();assertFallback(c);
 c.w.debounce=fn=>fn;c.w.eval(source['assets/facets.js']+'\nwindow.__nativeAudit=FacetFiltersForm;');
 const native=c.w.__nativeAudit;let nativeRenders=0;native.renderPage=()=>{nativeRenders++;native.renderProductGridContainer('<div id="ProductGridContainer"><ul id="product-grid"><li id="native-new">Native replacement</li></ul><div class="pagination-wrapper">New native pages</div></div>');};
 const pending=deferred();c.searchHandler=()=>pending.promise;c.w.history.replaceState({searchParams:'native=1'},'','?bcf_vendor=B');c.w.dispatchEvent(new c.w.PopStateEvent('popstate',{state:c.w.history.state}));assert.equal(nativeRenders,1);assert.ok(c.w.document.getElementById('native-new'));pending.resolve(valid({products:[product('recovered-external')]}));await settle();assert.equal(c.active(),true);assert.ok(c.w.document.getElementById('native-new'));assert.equal(c.w.document.querySelectorAll('#product-grid .bc-filter-card').length,0);assert.equal(c.w.document.querySelector('.bc-filter-toolbar'),null);record('FX-37','DEFECT_REPRODUCED',{afterFallbackPopstateRunsBothControllers:true,actualNativeGridReplacementDetachesExternalClosureReferences:true,laterExternalSuccessMarksActiveButLiveGridRemainsNative:true,nativeTransportIsStubbed:true,liveOccurrenceNotEstablished:true});await dispose(c);
}
async function floatingContext(){
 const c=await fixture();c.mobile=true;c.nativeOpen=0;c.externalOpen=0;c.w.document.querySelector('section').insertAdjacentHTML('beforeend','<details class="mobile-facets__disclosure"><summary class="mobile-facets__open-wrapper">Native filters</summary></details><button data-bc-floating-filter hidden>Floating filters</button>');
 const section=c.w.document.querySelector('section'),native=section.querySelector('.mobile-facets__open-wrapper'),external=section.querySelector('[data-bc-open-filters]');native.addEventListener('click',()=>c.nativeOpen++);external.addEventListener('click',()=>c.externalOpen++);
 c.w.matchMedia=query=>({get matches(){return c.mobile;},addEventListener(){}});c.w.MutationObserver=class{constructor(fn){this.fn=fn;}observe(){}disconnect(){}};
 c.w.HTMLElement.prototype.getBoundingClientRect=function(){return this.id==='product-grid'?{top:0,bottom:800}:this.matches('.mobile-facets__open-wrapper,[data-bc-open-filters]')?{top:-80,bottom:-40}:{top:0,bottom:40};};
 c.w.eval(source['assets/bc-mobile-listing.js']);c.floating=c.w.document.querySelector('[data-bc-floating-filter]');c.refresh=()=>{c.w.dispatchEvent(new c.w.Event('scroll'));c.frame();};return c;
}
{
 const c=await floatingContext();assert.equal(c.floating.parentElement,c.w.document.body);assert.equal(c.floating.hidden,false);assert.equal(c.floating.dataset.initialized,'true');c.w.eval(source['assets/bc-mobile-listing.js']);assert.equal(c.w.document.querySelectorAll('[data-bc-floating-filter]').length,1);record('FL-01','CONTROL_PASSED',{floatingButtonMovedToBody:true,eligibleSyntheticGeometryShowsShortcut:true,secondInitDoesNotCreateAnotherButton:true});await dispose(c);
}
{
 const c=await floatingContext();c.w.document.body.insertAdjacentHTML('beforeend','<dialog open>Another overlay</dialog>');c.refresh();assert.equal(c.floating.hidden,true);record('FL-02','CONTROL_PASSED',{anotherOpenDialogSuppressesFloatingShortcut:true});await dispose(c);
}
{
 const c=await floatingContext();c.floating.click();assert.equal(c.externalOpen,1);c.w.document.documentElement.classList.remove('bc-external-filters-active');c.floating.click();assert.equal(c.nativeOpen,1);record('FL-03','CONTROL_PASSED',{shortcutChoosesExternalOrNativeOpenerFromActiveClass:true,openerHandlersAndGeometrySynthetic:true});await dispose(c);
}
{
 const c=await floatingContext();c.mobile=false;c.refresh();assert.equal(c.floating.hidden,true);record('FL-04','CONTROL_PASSED',{nonMobileMediaQueryHidesShortcut:true,notDeviceOrCSSProof:true});await dispose(c);
}
const report={schemaVersion:1,themeId:manifest.themeId,environment:{node:process.version,dom:'happy-dom 21.0.4'},safety:{realNetwork:false,realCartActions:false,productionWrites:false,syntheticProductsOnly:true},scope:'Actual filter and listing closures with synthetic API/section responses; FX-37 includes actual native facets popstate/grid method with stubbed native request orchestration. Numeric validity uses an explicit tolerance shim. CSS, geometry, full history traversal and mobile device behavior are not certified.',results};fs.mkdirSync(path.dirname(args.output),{recursive:true});fs.writeFileSync(args.output,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({cases:results.length,classifications:results.reduce((a,r)=>(a[r.classification]=(a[r.classification]||0)+1,a),{})}));
