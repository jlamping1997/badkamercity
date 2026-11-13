const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const {JSDOM} = require('jsdom');
const key = 'bc-sunshower-choice-scroll';
const source = fs.readFileSync(process.argv[2], 'utf8');
const controller = source.slice(0, source.indexOf('      const gallery =')) + '\n    });\n  };\n  initialize(document);\n})();';
const tick = () => new Promise(resolve => setImmediate(resolve));
function fixture({url='https://badkamercity.nl/products/black',saved,blocked=false,ready='loading'}={}) {
  const dom = new JSDOM('<div data-ss-page data-catalog="/catalog.json" data-loading="Loading" data-choice-error="Error"><fieldset data-ss-field="kleur"><button data-ss-option="Black" aria-pressed="true">Black</button><button data-ss-option="White" aria-pressed="false">White</button></fieldset><p data-ss-choice-status></p><button type="submit">Buy</button></div>');
  const document = dom.window.document;
  Object.defineProperty(document,'readyState',{value:ready,configurable:true});
  const state={y:0,absolute:1300,now:1000,scrolls:[],assigned:[],storage:new Map(),fetches:0};
  if(saved!==undefined) state.storage.set(key,typeof saved==='string'?saved:JSON.stringify(saved));
  const field=document.querySelector('[data-ss-field]');
  field.getBoundingClientRect=()=>({top:state.absolute-state.y});
  const storage={getItem:k=>{if(blocked)throw Error('blocked');return state.storage.get(k)??null;},setItem:(k,v)=>{if(blocked)throw Error('blocked');state.storage.set(k,v);},removeItem:k=>{if(blocked)throw Error('blocked');state.storage.delete(k);}};
  const location=new URL(url); location.assign=v=>state.assigned.push(v);
  const frames=new Map(),timers=new Map(); let id=0;
  const history={scrollRestoration:'auto'};
  const window={Shopify:{},get scrollY(){return state.y;},scrollX:0,scrollTo:({top})=>{state.y=top;state.scrolls.push(top);},addEventListener:(...args)=>dom.window.addEventListener(...args),removeEventListener:(...args)=>dom.window.removeEventListener(...args)};
  let fetchResolve,resize;
  const context={document,window,location,history,sessionStorage:storage,URL,URLSearchParams,Date:{now:()=>state.now},requestAnimationFrame:fn=>{frames.set(++id,fn);return id;},cancelAnimationFrame:i=>frames.delete(i),setTimeout:(fn,ms)=>{timers.set(++id,{fn,at:state.now+ms});return id;},clearTimeout:i=>timers.delete(i),ResizeObserver:class {constructor(fn){resize=fn;}observe(){}disconnect(){resize=null;}},fetch:()=>{state.fetches++;return new Promise(resolve=>{fetchResolve=resolve;});}};
  vm.runInNewContext(controller,context);
  const flush=()=>{for(const [i,fn] of [...frames]){frames.delete(i);fn();}};
  return {state,field,history,document,click:()=>document.querySelector('[data-ss-option="White"]').click(),finish:async(ok=true)=>{fetchResolve({ok,json:async()=>({products:[{url:'/products/white',selection:{kleur:'White'}}]})});await tick();},flush,resize:()=>{resize?.();flush();},event:name=>{dom.window.dispatchEvent(new dom.window.Event(name));flush();},advance:ms=>{state.now+=ms;for(const [i,t] of [...timers])if(t.at<=state.now){timers.delete(i);t.fn();}flush();}};
}
const record=extra=>({target:'/products/black',field:'kleur',top:250,y:1050,time:1000,...extra});
const tests=[];
const test=async(name,fn)=>{try{await fn();tests.push({name,result:'PASS'});}catch(error){tests.push({name,result:'FAIL',error:error.message});}};
(async()=>{
await test('Cold first click captures position before async catalog and layout changes',async()=>{
 const f=fixture();f.state.y=1050;f.click();f.state.y=0;f.state.absolute=1400;await f.finish();
 const stored=JSON.parse(f.state.storage.get(key));assert.equal(stored.y,1050);assert.equal(stored.top,250);assert.match(f.state.assigned[0],/#sunshower-configurator$/);
});
await test('Restore still corrects load and image shifts after the original two-second cutoff',()=>{
 const f=fixture({saved:record()});assert.equal(f.state.y,1050);f.advance(3000);f.state.y=0;f.state.absolute=1450;f.event('load');assert.equal(f.field.getBoundingClientRect().top,250);assert.equal(f.history.scrollRestoration,'manual');f.advance(2000);assert.equal(f.history.scrollRestoration,'auto');
});
await test('First preview navigation survives Shopify removing preview_theme_id',()=>{
 const f=fixture({saved:record({target:'/products/black?preview_theme_id=123'}),url:'https://badkamercity.nl/products/black'});assert.equal(f.state.y,1050);
});
await test('Semantic query remains required and query order is stable',()=>{
 const f=fixture({saved:record({target:'/products/black?view=sunshower&bc_sunshower=42&preview_theme_id=123'}),url:'https://badkamercity.nl/products/black?bc_sunshower=42&view=sunshower'});assert.equal(f.state.y,1050);
 const other=fixture({saved:record({target:'/products/black?view=sunshower'})});assert.equal(other.state.y,0);
});
for(const name of ['pointerdown','touchstart','wheel','keydown','pagehide']) await test(`User ${name} cancels corrections immediately`,()=>{
 const f=fixture({saved:record()});f.event(name);f.state.y=300;f.state.absolute=1600;f.resize();f.event('load');assert.equal(f.state.y,300);assert.equal(f.history.scrollRestoration,'auto');
});
await test('No record leaves ordinary product visits and native scroll restoration unchanged',()=>{
 const f=fixture();f.resize();f.event('load');assert.equal(f.state.scrolls.length,0);assert.equal(f.history.scrollRestoration,'auto');
});
await test('Stored position is consumed only once',()=>{
 const f=fixture({saved:record()});assert.equal(f.state.storage.has(key),false);
});
await test('Bad route, TTL, future values, malformed records do not restore or crash',()=>{
 for(const saved of [record({target:'/products/other'}),record({target:'http://['}),record({time:-31000}),record({time:2000}),record({y:'1050'}),record({top:null}),'not-json',{}]){const f=fixture({saved});assert.equal(f.state.scrolls.length,0);assert.equal(f.history.scrollRestoration,'auto');}
});
await test('Blocked storage preserves navigation with native configurator anchor fallback',async()=>{
 const f=fixture({blocked:true});f.click();await f.finish();assert.equal(f.state.assigned[0],'https://badkamercity.nl/products/white#sunshower-configurator');
});
await test('Failed catalog restores controls and does not store a position',async()=>{
 const f=fixture();f.click();await f.finish(false);assert.equal(f.state.assigned.length,0);assert.equal(f.state.storage.has(key),false);assert.equal(f.document.querySelector('[data-ss-option="White"]').disabled,false);
});
await test('Loaded page stops correction after settling and late layout does not pull visitor',()=>{
 const f=fixture({saved:record(),ready:'complete'});f.advance(2000);f.state.y=300;f.state.absolute=1500;f.resize();assert.equal(f.state.y,300);assert.equal(f.history.scrollRestoration,'auto');
});
await test('Absolute max timeout restores browser setting when load never arrives',()=>{
 const f=fixture({saved:record()});f.advance(15000);assert.equal(f.history.scrollRestoration,'auto');f.state.y=300;f.resize();assert.equal(f.state.y,300);
});
console.log(JSON.stringify({file:process.argv[2],passed:tests.filter(t=>t.result==='PASS').length,total:tests.length,tests},null,2));
if(tests.some(t=>t.result==='FAIL'))process.exitCode=1;
})();
