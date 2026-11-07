const { JSDOM } = require('jsdom');
const fs = require('fs');
const assert = require('node:assert/strict');
const code = fs.readFileSync(require('node:path').resolve(__dirname, '../../../assets/bc-mobile-header.js'), 'utf8');
let checks = [];
function scenario(name, test) {
  const dom = new JSDOM('<!doctype html><html style="--header-height:200px"><body><section class="section-header"><div class="bc-header"><div class="bc-header__search"><predictive-search><input></predictive-search></div><div class="bc-mobile-drawer"><button>Menu</button></div></div></section><dialog></dialog></body></html>', {runScripts:'outside-only', pretendToBeVisual:true});
  const w=dom.window, d=w.document, root=d.querySelector('section'), search=d.querySelector('.bc-header__search');
  let queue=new Map(), id=0, y=0, mobile=true, change;
  w.requestAnimationFrame=fn=>{queue.set(++id,fn);return id;};
  w.cancelAnimationFrame=id=>queue.delete(id);
  w.matchMedia=()=>({get matches(){return mobile;},addEventListener:(_,fn)=>change=fn,removeEventListener:()=>{change=null;}});
  w.ResizeObserver=class {observe(){} disconnect(){}};
  Object.defineProperty(w,'scrollY',{get:()=>y});
  Object.defineProperty(w,'innerHeight',{value:800});
  Object.defineProperty(d.documentElement,'scrollHeight',{value:3000});
  Object.defineProperty(root,'offsetHeight',{value:138});
  d.querySelector('.bc-header').getBoundingClientRect=()=>({height:root.dataset.bcScrollState==='compact'?84:138,bottom:root.dataset.bcScrollState==='compact'?84:138});
  function flush(){for(let n=0;queue.size&&n<10;n++){let tasks=[...queue.values()];queue.clear();tasks.forEach(fn=>fn());}}
  w.eval(code);d.dispatchEvent(new w.Event('DOMContentLoaded'));flush();
  const scroll=value=>{y=value;w.dispatchEvent(new w.Event('scroll'));flush();};
  const ctx={w,d,root,search,scroll,flush,compact:()=>root.dataset.bcScrollState==='compact',media:value=>{mobile=value;change?.({matches:value});flush();}};
  try{test(ctx);checks.push({name,result:'PASS'});}finally{dom.window.close();}
}
scenario('Initial search visible and focusable',c=>{assert(!c.compact());assert.equal(c.search.inert,false);assert(!c.search.hasAttribute('aria-hidden'));});
scenario('Downward scroll retains header and hides only search',c=>{c.scroll(300);assert(c.compact());assert(c.search.inert);assert.equal(c.search.getAttribute('aria-hidden'),'true');assert.equal(c.d.documentElement.style.getPropertyValue('--header-height'),'84px');});
scenario('Small reversal does not flash search',c=>{c.scroll(300);c.scroll(288);assert(c.compact());c.scroll(294);assert(c.compact());});
scenario('Deliberate upward scroll reveals search',c=>{c.scroll(300);c.scroll(268);assert(!c.compact());assert(!c.search.inert);});
scenario('Returning near top always reveals',c=>{c.scroll(300);c.scroll(20);assert(!c.compact());});
scenario('Slow 1px downward scroll still collapses',c=>{for(let y=1;y<=220;y++)c.scroll(y);assert(c.compact());});
scenario('Slow upward scroll accumulates intent',c=>{c.scroll(300);for(let y=299;y>=268;y--)c.scroll(y);assert(!c.compact());});
scenario('No collapse near top',c=>{c.scroll(100);assert(!c.compact());});
scenario('Search typing keeps search visible',c=>{c.d.querySelector('input').focus();c.scroll(300);assert(!c.compact());});
scenario('Open predictive results preserve search',c=>{c.d.querySelector('predictive-search').setAttribute('open','');c.scroll(300);assert(!c.compact());});
scenario('Open menu freezes compact state',c=>{c.scroll(300);c.d.querySelector('.bc-mobile-drawer').classList.add('is-open');c.scroll(180);assert(c.compact());});
scenario('Open dialog freezes current header state',c=>{c.d.querySelector('dialog').setAttribute('open','');c.scroll(300);assert(!c.compact());});
scenario('Bottom rubber band does not reveal accidentally',c=>{c.scroll(2200);c.scroll(2270);c.scroll(2200);assert(c.compact());});
scenario('Top rubber band stays expanded',c=>{c.scroll(-60);c.scroll(0);assert(!c.compact());});
scenario('Desktop does not compact',c=>{c.media(false);c.scroll(300);assert(!c.compact());assert.equal(c.d.documentElement.style.getPropertyValue('--header-height'),'200px');});
scenario('Crossing breakpoint resets mobile safely',c=>{c.scroll(300);c.media(false);assert(!c.search.inert);c.media(true);assert(!c.compact());c.scroll(350);assert(c.compact());});
scenario('Pointer and keyboard modality switch independently',c=>{c.d.dispatchEvent(new c.w.KeyboardEvent('keydown',{key:'Tab'}));assert.equal(c.root.dataset.bcInput,'keyboard');c.d.dispatchEvent(new c.w.Event('pointerdown'));assert.equal(c.root.dataset.bcInput,'pointer');});
scenario('Repeated initialization does not replace controller',c=>{const first=c.root.bcMobileHeader;c.w.eval(code);assert.equal(c.root.bcMobileHeader,first);});
scenario('Section unload restores attributes and metrics',c=>{c.scroll(300);c.root.dispatchEvent(new c.w.Event('shopify:section:unload',{bubbles:true}));assert(!c.root.bcMobileHeader);assert(!c.search.inert);assert(!c.root.hasAttribute('data-bc-scroll-state'));assert.equal(c.d.documentElement.style.getPropertyValue('--header-height'),'200px');c.scroll(400);assert(!c.root.hasAttribute('data-bc-scroll-state'));});
scenario('Section reload makes exactly one working controller',c=>{c.root.dispatchEvent(new c.w.Event('shopify:section:unload',{bubbles:true}));c.root.dispatchEvent(new c.w.Event('shopify:section:load',{bubbles:true}));c.flush();assert(c.root.bcMobileHeader);c.scroll(300);assert(c.compact());});
scenario('History return to top restores search',c=>{c.scroll(300);c.scroll(0);c.w.dispatchEvent(new c.w.Event('pageshow'));c.flush();assert(!c.compact());});
fs.writeFileSync(__dirname+'/behavior-checks.json',JSON.stringify({suite:'Isolated JavaScript behavior; synthetic geometry, no visual/phone claim',count:checks.length,checks},null,2)+'\n');
console.log(`${checks.length} behavior scenarios passed`);
