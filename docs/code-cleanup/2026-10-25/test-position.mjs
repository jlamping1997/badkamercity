import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const source=fs.readFileSync(new URL('theme/assets/bc-product-switcher.js',import.meta.url),'utf8');
const engine=fs.readFileSync(new URL('theme/assets/bc-choice-position.js',import.meta.url),'utf8');
const fn=source.slice(source.indexOf('  function createSwitcherPositionKeeper('),source.indexOf('  const switcherPosition = '));
const key='bc:product-switcher:position:v1';
const group={id:'g',menus:[{key:'kleur'}],products:[{handle:'a',url:'/products/a'},{handle:'b',url:'/products/b'}]};
function rig({sticky=false,blocked=false,quota=false}={}) {
  let time=10000,next=0,flow=800;
  const jobs=new Map(),listeners=new Map(),storage=new Map(),props=new Map();
  const style={getPropertyValue:k=>props.get(k)?.[0]||'',getPropertyPriority:k=>props.get(k)?.[1]||'',setProperty:(k,v,p='')=>props.set(k,[v,p]),removeProperty:k=>props.delete(k)};
  style.setProperty('scroll-behavior','smooth','important');
  const document={documentElement:{style},fonts:{status:'loaded'}};
  const calls=[];
  const window={innerWidth:390,scrollY:650,scrollX:0,location:{origin:'https://badkamercity.nl',href:'https://badkamercity.nl/products/a'},history:{scrollRestoration:'auto'},
    sessionStorage:{getItem:k=>{if(blocked)throw Error('blocked');return storage.get(k)||null;},setItem:(k,v)=>{if(blocked||(quota&&JSON.parse(v).handoff))throw Error('quota');storage.set(k,v);},removeItem:k=>storage.delete(k)},
    requestAnimationFrame:cb=>{const id=++next;jobs.set(id,{at:time+16,cb});return id;},cancelAnimationFrame:id=>jobs.delete(id),
    setTimeout:(cb,delay)=>{const id=++next;jobs.set(id,{at:time+delay,cb});return id;},clearTimeout:id=>jobs.delete(id),
    addEventListener:(type,cb)=>{if(!listeners.has(type))listeners.set(type,new Set());listeners.get(type).add(cb);},removeEventListener:(type,cb)=>listeners.get(type)?.delete(cb),
    scrollTo:(value,y)=>{const top=typeof value==='object'?value.top:y;calls.push({at:time,top});window.scrollY=top;}};
  const root={dataset:{bcPreservePosition:'true',switchGroup:'g',productHandle:'a',switcherDataUrl:'/data?v=1'},style:{minHeight:'12px'},isConnected:true,
    getBoundingClientRect:()=>({top:sticky?150:flow-window.scrollY,height:300})};
  vm.runInNewContext(engine,{window,document,Date:{now:()=>time}});
  const keeper=vm.runInNewContext('('+fn+')',{Date:{now:()=>time},URL})(window,document);
  function advance(ms) {
    const end=time+ms;
    for(;;){const candidates=[...jobs].filter(([,j])=>j.at<=end).sort((a,b)=>a[1].at-b[1].at);if(!candidates.length)break;const[id,j]=candidates[0];jobs.delete(id);time=j.at;j.cb();}
    time=end;
  }
  function nextPage(){window.location.href='https://badkamercity.nl/products/b';window.scrollY=0;root.dataset.productHandle='b';flow=900;}
  function emit(type){for(const cb of [...listeners.get(type)||[]])cb({type});}
  return {window,document,root,keeper,storage,calls,jobs,listeners,advance,nextPage,emit,setFlow:v=>flow=v,now:()=>time};
}
const checks=[];
let x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();let r=x.keeper.prepare(x.root);
assert.equal(r.dataGroup.id,'g');assert.equal(x.root.style.minHeight,'300px');r.activate();assert.equal(x.root.style.minHeight,'12px');
x.advance(64);assert.equal(x.calls.length,0);x.advance(48);assert.equal(x.calls.length,1);assert.equal(x.calls[0].top,750);assert.equal(x.jobs.size,0);
assert.equal(x.window.history.scrollRestoration,'auto');assert.equal(x.document.documentElement.style.getPropertyValue('scroll-behavior'),'smooth');assert.equal(x.document.documentElement.style.getPropertyPriority('scroll-behavior'),'important');
x.setFlow(940);x.emit('load');x.advance(16000);assert.equal(x.calls.length,1);checks.push('One correction, no later pulling; timers, styles and history restored');

x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();r=x.keeper.prepare(x.root);r.activate();x.document.fonts.status='loading';
x.advance(48);x.setFlow(960);x.advance(80);x.setFlow(980);x.advance(80);assert.equal(x.calls.length,0);x.document.fonts.status='loaded';x.advance(112);
assert.equal(x.calls.length,1);assert.equal(x.calls[0].top,830);checks.push('Moving layout and loading fonts settle before the single correction');

for(const input of ['pointerdown','touchstart','wheel','keydown']){
 x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();r=x.keeper.prepare(x.root);r.activate();x.advance(32);x.emit(input);x.advance(2000);assert.equal(x.calls.length,0);assert.equal(x.jobs.size,0);
}
checks.push('Touch, wheel, pointer and keyboard cancel restoration immediately');
x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();r=x.keeper.prepare(x.root);r.activate();x.document.fonts.status='loading';x.advance(1200);assert.equal(x.calls.length,1);assert.equal(x.jobs.size,0);checks.push('Never waits indefinitely for fonts or window load');

x=rig({sticky:true});x.keeper.remember(x.root,'/products/b',group);let token=JSON.parse(x.storage.get(key));token.top=-40;x.storage.set(key,JSON.stringify(token));x.nextPage();r=x.keeper.prepare(x.root);r.activate();x.advance(15000);assert.equal(x.calls.length,1);checks.push('Sticky or unreachable target cannot create a correction loop');

for(const change of [t=>t.savedAt-=31000,t=>t.savedAt+=1000,t=>t.target='/products/other',t=>t.group='other']){
 x=rig();x.keeper.remember(x.root,'/products/b',group);token=JSON.parse(x.storage.get(key));change(token);x.storage.set(key,JSON.stringify(token));x.nextPage();assert.equal(x.keeper.prepare(x.root),null);
}
checks.push('Expired, future, wrong-target and wrong-group tokens rejected');

x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();x.root.dataset.switcherDataUrl='/data?v=2';r=x.keeper.prepare(x.root);assert.equal(r.dataGroup,null);r.cancel();
x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();x.root.dataset.productHandle='wrong';r=x.keeper.prepare(x.root);assert.equal(r.dataGroup,null);r.cancel();checks.push('Menu handoff requires exact source revision and destination product');

x=rig({quota:true});assert(x.keeper.remember(x.root,'/products/b',group));assert(!JSON.parse(x.storage.get(key)).handoff);x.nextPage();r=x.keeper.prepare(x.root);assert.equal(r.dataGroup,null);r.activate();x.advance(200);assert.equal(x.calls.length,1);
x=rig({blocked:true});assert.equal(x.keeper.remember(x.root,'/products/b',group),null);assert.equal(x.keeper.prepare(x.root),null);checks.push('Storage quota falls back to position-only; blocked storage does not throw');

x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();r=x.keeper.prepare(x.root);x.advance(15001);assert.equal(x.jobs.size,0);assert.equal(x.root.style.minHeight,'12px');r.activate();x.advance(200);assert.equal(x.calls.length,0);
x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();r=x.keeper.prepare(x.root);r.activate();x.emit('pagehide');x.advance(200);assert.equal(x.calls.length,0);checks.push('Failed initialization and pagehide clean up without late jumps');

x=rig();x.keeper.remember(x.root,'/products/b',group);x.nextPage();x.window.innerWidth=800;r=x.keeper.prepare(x.root);r.activate();x.advance(200);assert.equal(x.calls.length,0);checks.push('Changed screen orientation skips outdated coordinates');
const result={status:'PASS',checks};fs.writeFileSync(new URL('position-test-results.json',import.meta.url),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
