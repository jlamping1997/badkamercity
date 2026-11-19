const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const {JSDOM} = require('jsdom');
const source = fs.readFileSync(process.env.BC_CARD_SOURCE || require('node:path').join(__dirname,'../shopify/current/assets/bc-external-filters.js'),'utf8');
const flush = async () => { for(let i=0;i<8;i++) await new Promise(setImmediate); };
const product = (id,handle) => ({id,shopify_product_id:`gid://shopify/Product/${id}`,handle,title:`Lagoo ${handle}`,vendor:'Lagoo',price_cents:51000,image_url:''});
const readyData = p => ({...p,short_title:p.title,color:'Zilver',variant_id:100+Number(p.id),available:true,can_add:true,specs:[],hover_image_url:'',switcher_html:''});
async function fixture(options={}) {
  const search = options.search === true;
  const products = options.products || [product('1','good'),product('2','missing')];
  const count = options.found ?? products.length;
  const sectionClass = search ? 'template-search' : 'bc-collection';
  const dom = new JSDOM(`<div class="${sectionClass}"><div id="BcExternalFilters" data-api-base="https://shop.test/verified" data-collection="${search?'__all__':'kranen'}" data-products-count="${search?'':count}" data-card-data-section="bc-card-data" data-search-mode="${search}" data-search-query="lagoo" data-search-title="Lagoo (__BC_COUNT__)" data-label-page-count-suffix="op deze pagina" data-label-catalog-updated="De resultaten zijn bijgewerkt."></div><div class="facets-vertical"><aside id="${search?'main-search-filters':'main-collection-filters'}">Native filters</aside><facet-filters-form class="${search?'template-search__toolbar':'facets-vertical-sort'}"></facet-filters-form><div id="ProductGridContainer"><ul id="product-grid"><li id="native-product" class="bc-search-card">Native product</li></ul><div class="pagination-wrapper">Native pages</div></div></div></div>`,{url:`https://shop.test${search?'/search?q=lagoo':'/collections/kranen'}`,runScripts:'outside-only',pretendToBeVisual:true});
  const w=dom.window;
  w.matchMedia=()=>({matches:false,addEventListener(){},removeEventListener(){}});
  w.HTMLElement.prototype.scrollIntoView=function(){};
  w.console.error=()=>{};
  const calls=[];
  const modes={good:'ready',missing:'empty404',...(options.modes||{})};
  const pages=options.pages||{1:products};
  const deferred={};
  let apiFails=false;
  const response=(status,json)=>({status,ok:status>=200&&status<300,json:async()=>json});
  w.fetch=async(url,init={})=>{
    const u=new URL(url,w.location.origin);
    calls.push({url:u.href,init});
    if(init.body){
      if(apiFails)throw Error('offline');
      const req=JSON.parse(init.body);
      return response(200,{found:count,collection:{handle:search?'__all__':'kranen',profile_products:count},products:pages[req.page]||[],facets:[{field:'f_kleur',label:'Kleur',type:'string',values:[{value:'Zilver',count}]}]});
    }
    const handle=decodeURIComponent(u.pathname.split('/').pop().replace(/\.js$/,''));
    const p=products.find(p=>p.handle===handle)||Object.values(pages).flat().find(p=>p.handle===handle)||product('9',handle);
    const mode=modes[handle]||'ready';
    if(u.pathname.endsWith('.js')){
      if(mode==='empty404')return response(404,{});
      if(mode==='empty410')return response(410,{});
      if(mode==='empty503')return response(503,{});
      if(mode==='emptyNetwork')throw Error('offline');
      return response(200,{id:p.id,handle:p.handle});
    }
    if(mode==='deferred')return new Promise(resolve=>{deferred[handle]=resolve;});
    if(mode==='network')throw Error('offline');
    if(mode==='abort')throw new w.DOMException('aborted','AbortError');
    if(mode==='404')return response(404,{});
    if(mode==='410')return response(410,{});
    if(mode==='503')return response(503,{});
    if(mode==='invalidJson')return {ok:true,status:200,json:async()=>{throw Error('bad JSON');}};
    if(mode==='null')return response(200,{'bc-card-data':null});
    if(mode.startsWith('empty'))return response(200,{'bc-card-data':'<div class="shopify-section"></div>'});
    let data=readyData(p);
    if(mode==='mismatch')data.id='999';
    if(mode==='soldout')data.available=false;
    if(options.switcher&&handle==='good')data.switcher_html=`<div data-bc-product-switcher-v2 data-switch-group="qa"><script data-bc-switcher-inline type="application/json">${JSON.stringify({groups:[{id:'qa',menus:[{key:'kleur'}],products:[{handle:'good',options:{kleur:'Zilver'}},{handle:'missing',options:{kleur:'Zwart'}}]}]})}</script></div>`;
    return response(200,{'bc-card-data':`<script data-bc-card-data type="application/json">${JSON.stringify(data).replaceAll('<','\\u003c')}</script>`});
  };
  w.eval(source);
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  await flush();
  const f={dom,w,calls,modes,deferred,pages,apiFail:()=>{apiFails=true;},cards:()=>[...w.document.querySelectorAll('.bc-filter-card')],count:()=>w.document.querySelector('[data-bc-count]').textContent,refresh:async()=>{w.document.querySelector('#BcFilterSort').dispatchEvent(new w.Event('change',{bubbles:true}));await flush();}};
  return f;
}
for(const search of [false,true]) {
  test(`${search?'search':'collection'}: blank section + actual 404 removes only stale card`,async()=>{
    const f=await fixture({search});try{
      assert.deepEqual(f.cards().map(x=>x.dataset.bcCardHandle),['good']);
      assert.equal(f.count(),'1 product op deze pagina');
      assert.equal(f.w.document.querySelectorAll('a[href="/products/missing"]').length,0);
      assert.equal(f.w.document.querySelector('.bc-filter-error').hidden,false);
      if(search)assert.match(f.w.document.title,/1 op deze pagina/);
      assert.ok(f.calls.some(x=>x.url.endsWith('/products/missing.js')));
    }finally{f.dom.window.close();}
  });
}
for(const mode of ['404','410','empty410']) test(`${mode} is confirmed unavailable`,async()=>{
  const f=await fixture({modes:{missing:mode}});try{assert.equal(f.cards().length,1);}finally{f.dom.window.close();}
});
for(const mode of ['network','abort','503','invalidJson','null','empty200','empty503','emptyNetwork','mismatch']) test(`${mode} keeps uncertain product and original count`,async()=>{
  const f=await fixture({modes:{missing:mode}});try{
    assert.equal(f.cards().length,2);
    assert.equal(f.count(),'2 producten');
    assert.equal(f.cards()[1].querySelector('[data-bc-price-state]').dataset.bcPriceState,'unavailable');
    assert.equal(f.cards()[1].hasAttribute('inert'),false);
  }finally{f.dom.window.close();}
});
test('sold-out is still a published product and stays visible',async()=>{
  const f=await fixture({modes:{missing:'soldout'}});try{assert.equal(f.cards().length,2);assert.equal(f.cards()[1].querySelector('[data-bc-card-cart]').disabled,true);}finally{f.dom.window.close();}
});
test('all-stale page is explicit and does not resurrect native cards',async()=>{
  const f=await fixture({products:[product('2','missing')]});try{
    assert.equal(f.cards().length,0);assert.equal(f.count(),'0 producten op deze pagina');
    assert.match(f.w.document.querySelector('.bc-filter-empty').textContent,/Op deze pagina/);
    assert.equal(f.w.document.querySelector('#native-product'),null);
  }finally{f.dom.window.close();}
});
test('later raw pages remain reachable after removing stale hits',async()=>{
  const p1=[product('1','good'),product('2','missing')],p2=[product('3','next')];
  const f=await fixture({products:[...p1,...p2],found:25,pages:{1:p1,2:p2}});try{
    assert.equal(f.w.document.querySelector('[data-page="2"]').disabled,false);
    assert.equal(f.w.document.querySelector('.bc-filter-pagination__status').textContent,'Pagina 1');
    f.w.document.querySelector('[data-page="2"]').click();await flush();
    assert.deepEqual(f.cards().map(x=>x.dataset.bcCardHandle),['next']);
    assert.equal(f.count(),'1 product op deze pagina');
    assert.equal(new URL(f.w.location.href).searchParams.get('bcpage'),'2');
  }finally{f.dom.window.close();}
});
test('an empty stale page still has a working next page',async()=>{
  const f=await fixture({products:[product('2','missing'),product('3','next')],found:25,pages:{1:[product('2','missing')],2:[product('3','next')]}});try{
    assert.equal(f.cards().length,0);f.w.document.querySelector('[data-page="2"]').click();await flush();
    assert.equal(f.cards()[0].dataset.bcCardHandle,'next');
  }finally{f.dom.window.close();}
});
test('cache is revalidated on a fresh listing request',async()=>{
  const f=await fixture({modes:{missing:'ready'}});try{
    assert.equal(f.cards().length,2);f.modes.missing='empty404';await f.refresh();assert.equal(f.cards().length,1);
    assert.ok(f.calls.filter(x=>x.url.includes('/products/good?sections')).length>=2);
  }finally{f.dom.window.close();}
});
test('republished product can return on the next request',async()=>{
  const f=await fixture();try{f.modes.missing='ready';await f.refresh();assert.equal(f.cards().length,2);}finally{f.dom.window.close();}
});
test('old async 404 does not remove a newer grid',async()=>{
  const f=await fixture({modes:{missing:'deferred'}});try{
    const old=f.deferred.missing;f.modes.missing='ready';await f.refresh();
    old({status:404,ok:false});await flush();assert.equal(f.cards().length,2);assert.equal(f.count(),'2 producten');
  }finally{f.dom.window.close();}
});
test('pending product links are inert until verification finishes',async()=>{
  const f=await fixture({modes:{missing:'deferred'}});try{assert.equal(f.cards()[1].hasAttribute('inert'),true);f.deferred.missing({status:404,ok:false});await flush();assert.equal(f.cards().length,1);}finally{f.dom.window.close();}
});
test('missing color keeps the last valid card, with correct link and price',async()=>{
  const f=await fixture({products:[product('1','good')],switcher:true});try{
    f.w.document.querySelector('[data-bc-card-color="missing"]').click();await flush();
    assert.equal(f.cards().length,1);assert.equal(f.cards()[0].dataset.bcCardHandle,'good');
    assert.equal(f.cards()[0].querySelector('.bc-card-view').getAttribute('href'),'/products/good');
    assert.equal(f.w.document.querySelector('[data-bc-card-color="missing"]'),null);
    assert.match(f.cards()[0].querySelector('.bc-filter-card__price').textContent,/510/);
  }finally{f.dom.window.close();}
});
test('cached browser back restores a fresh listing',async()=>{
  const f=await fixture({modes:{missing:'ready'}});try{f.modes.missing='404';f.w.dispatchEvent(new f.w.PageTransitionEvent('pageshow',{persisted:true}));await flush();assert.equal(f.cards().length,1);}finally{f.dom.window.close();}
});
test('API error still restores the native listing and filters',async()=>{
  const f=await fixture();try{f.apiFail();await f.refresh();assert.ok(f.w.document.querySelector('#native-product'));assert.equal(f.w.document.documentElement.classList.contains('bc-external-filters-active'),false);}finally{f.dom.window.close();}
});
test('returning to a tab after 30 seconds revalidates the products',async()=>{
  const f=await fixture({modes:{missing:'ready'}});try{
    let time=1000,hidden=true;f.w.Date.now=()=>time;
    Object.defineProperty(f.w.document,'hidden',{configurable:true,get:()=>hidden});
    f.w.document.dispatchEvent(new f.w.Event('visibilitychange'));
    time+=30001;hidden=false;f.modes.missing='empty404';
    f.w.document.dispatchEvent(new f.w.Event('visibilitychange'));await flush();assert.equal(f.cards().length,1);
  }finally{f.dom.window.close();}
});
test('a short tab switch does not add product requests',async()=>{
  const f=await fixture();try{
    const count=f.calls.length;let time=1000,hidden=true;f.w.Date.now=()=>time;
    Object.defineProperty(f.w.document,'hidden',{configurable:true,get:()=>hidden});
    f.w.document.dispatchEvent(new f.w.Event('visibilitychange'));time+=1000;hidden=false;
    f.w.document.dispatchEvent(new f.w.Event('visibilitychange'));await flush();assert.equal(f.calls.length,count);
  }finally{f.dom.window.close();}
});
test('tab refresh does not replace a card while an add is pending',async()=>{
  const f=await fixture();try{
    const count=f.calls.length;let time=1000,hidden=true;f.w.Date.now=()=>time;
    Object.defineProperty(f.w.document,'hidden',{configurable:true,get:()=>hidden});
    f.cards()[0].querySelector('[data-bc-card-cart]').setAttribute('aria-busy','true');
    f.w.document.dispatchEvent(new f.w.Event('visibilitychange'));time+=30001;hidden=false;
    f.w.document.dispatchEvent(new f.w.Event('visibilitychange'));await flush();assert.equal(f.calls.length,count);
  }finally{f.dom.window.close();}
});
test('changing the filter scope restores exact totals if no stale cards are found',async()=>{
  const f=await fixture();try{
    f.modes.missing='ready';f.w.document.querySelector('[data-filter-field="f_kleur"]').click();await flush();assert.equal(f.count(),'2 producten');
  }finally{f.dom.window.close();}
});
test('filter and price sorting requests keep their intended values',async()=>{
  const f=await fixture();try{
    f.w.document.querySelector('[data-filter-field="f_kleur"]').click();await flush();
    let req=JSON.parse(f.calls.filter(x=>x.init.body).at(-1).init.body);assert.deepEqual(req.filters.f_kleur,['Zilver']);
    f.w.document.querySelector('#BcFilterSort').value='price_asc';await f.refresh();
    req=JSON.parse(f.calls.filter(x=>x.init.body).at(-1).init.body);assert.equal(req.sort,'price_asc');assert.equal(req.page,1);
  }finally{f.dom.window.close();}
});
