import fs from 'node:fs';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
const require=createRequire(process.env.BC_TEST_DEPENDENCIES||new URL('package.json',import.meta.url));
const { Window }=require('happy-dom');
const source=fs.readFileSync(new URL('../../../../shopify/current/assets/bc-brand-slider.js',import.meta.url),'utf8');
const results=[],record=test=>results.push({test,result:'PASS'});
async function setup({width=1348,reduced=false,rtl=false,count=9,visible=true,autoplay=true,controls=true}={}){
 const w=new Window({url:'https://example.invalid',width,height:936});
 let viewport=width,prefersReduced=reduced,hidden=false,scroll=0,clock=0,id=0,intersection;
 const frames=new Map(),media=[],captures=new Set(),calls=[];
 w.requestAnimationFrame=fn=>{frames.set(++id,fn);return id;};w.cancelAnimationFrame=id=>frames.delete(id);
 Object.defineProperty(w.document,'hidden',{get:()=>hidden,configurable:true});
 w.matchMedia=()=>{const m=new w.EventTarget();Object.defineProperty(m,'matches',{get:()=>prefersReduced});media.push(m);return m;};
 w.ResizeObserver=class{observe(){}disconnect(){}};
 w.IntersectionObserver=class{constructor(cb){intersection=cb;}observe(){intersection([{isIntersecting:visible}]);}disconnect(){}};
 w.document.body.innerHTML='<bc-brand-slider '+(autoplay?'data-brand-autoplay':'')+'>'+(controls?'<div data-brand-controls hidden><button data-brand-previous></button><button data-brand-next></button></div>':'')+'<ul data-brand-track tabindex="0" style="column-gap:'+(width>=990?48:24)+'px;direction:'+(rtl?'rtl':'ltr')+'">'+Array.from({length:count},(_,n)=>'<li><a id="brand-'+n+'" href="/brand/'+n+'"><img alt="Brand '+n+'"></a></li>').join('')+'</ul></bc-brand-slider>';
 const root=w.document.querySelector('bc-brand-slider'),track=root.querySelector('ul');
 const cell=()=>viewport>=990?200:150,gap=()=>parseFloat(track.style.columnGap),cycle=()=>count*(cell()+gap());
 Object.defineProperties(track,{clientWidth:{get:()=>viewport},scrollWidth:{get:()=>Math.max(0,track.children.length*(cell()+gap())-gap())},scrollLeft:{get:()=>scroll,set:value=>{const max=Math.max(0,track.scrollWidth-viewport);scroll=(rtl?-1:1)*Math.min(max,Math.max(0,Math.round(Math.abs(value))));track.dispatchEvent(new w.Event('scroll'));}}});
 for(const el of track.children)el.getBoundingClientRect=()=>({width:cell()});
 track.setPointerCapture=id=>captures.add(id);track.hasPointerCapture=id=>captures.has(id);track.releasePointerCapture=id=>captures.delete(id);
 track.scrollBy=({left,behavior})=>{calls.push({left,behavior});track.scrollLeft=scroll+left;};track.scrollTo=({left,behavior})=>{calls.push({left,behavior});track.scrollLeft=left;};
 const advance=(duration=16)=>{clock+=duration;const batch=[...frames.values()];frames.clear();for(const fn of batch)fn(clock);};
 const run=(seconds=1,fps=60)=>{for(let i=0;i<Math.round(seconds*fps);i++)advance(1000/fps);};
 const pointer=(type,{x=100,y=10,kind='mouse',pid=1,button=0,primary=true,target=track}={})=>{const e=new w.PointerEvent(type,{bubbles:true,cancelable:true,pointerId:pid,pointerType:kind,clientX:x,clientY:y,button,isPrimary:primary});Object.defineProperty(e,'timeStamp',{value:clock});target.dispatchEvent(e);return e;};
 const rightward=(a,b)=>((a-b)%cycle()+cycle())%cycle();
 w.eval(source);advance(0);
 return {w,root,track,frames,captures,calls,cycle,advance,run,pointer,rightward,
  resize:v=>{viewport=v;track.style.columnGap=(v>=990?48:24)+'px';w.dispatchEvent(new w.Event('resize'));advance(0);},
  reduce:v=>{prefersReduced=v;for(const m of media)m.dispatchEvent(new w.Event('change'));advance(0);},
  visible:v=>intersection([{isIntersecting:v}]),hidden:v=>{hidden=v;w.document.dispatchEvent(new w.Event('visibilitychange'));},
  close:async()=>{root.remove();await w.happyDOM.abort();w.close();}};
}
let p;
for(const width of [320,390,750,989,1348,4000]){
 p=await setup({width,controls:false});assert(p.root.hasAttribute('data-brand-moving'));assert.equal(p.track.querySelectorAll(':scope > li:not([data-brand-clone])').length,9);assert(p.track.scrollWidth>=p.cycle()+width);const a=p.track.scrollLeft;p.run();assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);record('full-filled-infinite-autoplay-without-controls-22px-per-second-'+width+'px');await p.close();
}
p=await setup();p.root.dispatchEvent(new p.w.Event('mouseenter'));let a=p.track.scrollLeft;p.run();assert(p.root.hasAttribute('data-brand-moving'));assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);record('hover-keeps-autoplay-running');
p.pointer('pointerdown');a=p.track.scrollLeft;p.run(1);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);p.pointer('pointerup');record('holding-mouse-down-keeps-autoplay-running');
p.pointer('pointerdown',{kind:'touch'});a=p.track.scrollLeft;p.run(1);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);p.pointer('pointerup',{kind:'touch'});record('holding-finger-keeps-autoplay-running');
p.pointer('pointerdown',{x:100});p.advance(16);a=p.track.scrollLeft;p.pointer('pointermove',{x:260});assert(Math.abs(p.rightward(a,p.track.scrollLeft)-160)<=1);assert(p.captures.has(1));assert(p.root.hasAttribute('data-brand-moving'));p.pointer('pointerup',{x:260});assert(!p.captures.has(1));a=p.track.scrollLeft;p.run(0.2);assert(p.rightward(a,p.track.scrollLeft)>80);record('mouse-drag-follows-pointer-and-releases-with-momentum');
p.run(3);a=p.track.scrollLeft;p.run(1);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);record('momentum-decays-back-to-base-speed-without-permanent-pause');
let click=new p.w.MouseEvent('click',{bubbles:true,cancelable:true,detail:1});p.track.querySelector('a').dispatchEvent(click);assert(click.defaultPrevented);p.pointer('pointerdown');p.pointer('pointerup');click=new p.w.MouseEvent('click',{bubbles:true,cancelable:true,detail:1});p.track.querySelector('a').dispatchEvent(click);assert(!click.defaultPrevented);record('drag-blocks-accidental-link-click-but-next-intentional-click-works');
p.pointer('pointerdown',{kind:'touch',x:100});p.advance(16);a=p.track.scrollLeft;p.pointer('pointermove',{kind:'touch',x:-60});assert(Math.abs(p.rightward(p.track.scrollLeft,a)-160)<=1);p.pointer('pointerup',{kind:'touch',x:-60});p.run(3);a=p.track.scrollLeft;p.run(1);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);assert(p.root.hasAttribute('data-brand-moving'));record('touch-swipe-in-opposite-direction-returns-to-rightward-autoplay');
p.pointer('pointerdown',{kind:'touch',x:100,y:10});const vertical=p.pointer('pointermove',{kind:'touch',x:102,y:80});assert(!vertical.defaultPrevented);assert(!p.captures.has(1));assert(!p.root.hasAttribute('data-brand-dragging'));a=p.track.scrollLeft;p.run(1);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);record('vertical-touch-remains-page-scroll-and-does-not-pause-rail');
p.pointer('pointerdown',{x:100});p.advance(16);p.pointer('pointermove',{x:180});p.pointer('pointercancel',{x:180});a=p.track.scrollLeft;p.run(1);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);assert(!p.root.hasAttribute('data-brand-dragging'));record('cancelled-drag-cleans-up-and-continues-at-base-speed');
p.pointer('pointerdown',{x:100});p.advance(16);p.pointer('pointermove',{x:180});p.run(0.3);p.pointer('pointerup',{x:180});a=p.track.scrollLeft;p.run(1);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);record('held-drag-release-does-not-reuse-stale-throw-velocity');
p.pointer('pointerdown',{x:100});p.pointer('pointerdown',{x:900,pid:2,primary:false});p.advance(16);a=p.track.scrollLeft;p.pointer('pointermove',{x:200});assert(Math.abs(p.rightward(a,p.track.scrollLeft)-100)<=1);p.pointer('pointerup',{x:200});record('second-finger-does-not-replace-active-drag');
p.run(3);a=p.track.scrollLeft;p.run(p.cycle()*3/22+1);assert(p.track.scrollLeft>=0&&p.track.scrollLeft<p.cycle());assert(p.root.hasAttribute('data-brand-moving'));assert(p.track.scrollWidth>=p.cycle()+p.track.clientWidth);record('multiple-complete-cycles-retain-filled-loop-and-autoplay');
p.resize(1280);const resized=p.track.scrollLeft;p.resize(1348);assert.equal(p.track.scrollLeft,resized);record('desktop-resize-preserves-cycle-position');
p.hidden(true);a=p.track.scrollLeft;p.run();assert.equal(p.track.scrollLeft,a);p.hidden(false);p.advance(0);p.run();assert(p.root.hasAttribute('data-brand-moving'));p.visible(false);a=p.track.scrollLeft;p.run();assert.equal(p.track.scrollLeft,a);p.visible(true);p.advance(0);p.run();assert(p.root.hasAttribute('data-brand-moving'));record('offscreen-and-hidden-work-is-suspended-and-resumes');
const clones=[...p.track.querySelectorAll('[data-brand-clone]')];assert(clones.every(li=>li.getAttribute('aria-hidden')==='true'&&!li.querySelector('[id]')&&li.querySelector('a').tabIndex===-1));record('copies-have-no-duplicate-ids-or-screen-reader-tab-stops');
p.root.querySelector('[data-brand-next]').click();p.run(0.5);assert(p.root.hasAttribute('data-brand-moving'));assert(p.track.querySelectorAll('[data-brand-clone]').length>0);p.run(3);a=p.track.scrollLeft;p.run();assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);record('arrow-button-keeps-loop-and-returns-to-base-speed');
p.reduce(true);assert.equal(p.track.children.length,9);assert(!p.root.hasAttribute('data-brand-moving'));p.root.querySelector(p.root.querySelector('[data-brand-next]').disabled?'[data-brand-previous]':'[data-brand-next]').click();assert.equal(p.calls.at(-1).behavior,'auto');p.reduce(false);assert(p.root.hasAttribute('data-brand-moving'));record('reduced-motion-preference-retains-static-native-scroll-fallback');
const anchor=p.track.querySelector('a');anchor.matches=selector=>selector===':focus-visible';anchor.dispatchEvent(new p.w.FocusEvent('focusin',{bubbles:true}));a=p.track.scrollLeft;p.run();assert.equal(p.track.scrollLeft,a);anchor.dispatchEvent(new p.w.FocusEvent('focusout',{bubbles:true,relatedTarget:p.w.document.body}));p.advance(0);p.run();assert(p.root.hasAttribute('data-brand-moving'));record('keyboard-focus-remains-operable-and-blur-resumes');
anchor.matches=()=>false;anchor.dispatchEvent(new p.w.FocusEvent('focusin',{bubbles:true}));a=p.track.scrollLeft;p.run();assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);record('pointer-focus-does-not-pause-autoplay');
p.root.remove();assert.equal(p.frames.size,0);assert.equal(p.track.children.length,9);p.w.document.body.append(p.root);p.advance(0);assert.equal(p.track.children.length,27);record('editor-reconnect-cleans-and-recreates-only-needed-copies');await p.close();
p=await setup({rtl:true});a=p.track.scrollLeft;p.run();assert(p.track.scrollLeft<0);assert(Math.abs(p.rightward(a,p.track.scrollLeft)-22)<=1);p.pointer('pointerdown',{x:100});p.advance(16);a=p.track.scrollLeft;p.pointer('pointermove',{x:260});assert(Math.abs(p.rightward(a,p.track.scrollLeft)-160)<=1);p.pointer('pointerup',{x:260});record('rtl-autoplay-and-drag-move-physically-with-pointer');await p.close();
for(const count of [0,1]){p=await setup({count});assert(!p.root.hasAttribute('data-brand-moving'));assert.equal(p.track.children.length,count);assert(p.root.querySelector('[data-brand-controls]').hidden);record('zero-or-one-brand-does-not-animate-'+count);await p.close();}
p=await setup({autoplay:false});assert.equal(p.track.children.length,9);p.root.querySelector('[data-brand-next]').click();assert(p.calls.length>0);assert(!p.root.hasAttribute('data-brand-moving'));record('existing-manual-component-still-works-without-autoplay');await p.close();
const markup=fs.readFileSync(new URL('../../../../shopify/current/sections/bc-homepage.liquid',import.meta.url),'utf8');assert(!markup.includes('data-brand-toggle'));assert(markup.includes('data-brand-autoplay'));const css=fs.readFileSync(new URL('../../../../shopify/current/assets/bc-brands.css',import.meta.url),'utf8');assert(css.includes('touch-action:pan-y pinch-zoom'));record('no-pause-control-and-vertical-pan-and-pinch-remain-available');
fs.writeFileSync(new URL('checks.json',import.meta.url),JSON.stringify({status:'PASS',checks:results.length,results,scope:'Actual component JS with synthetic geometry, pointer capture/events, deterministic frames and media events; real desktop drag checked separately.'},null,2)+'\n');console.log(results.length+' infinite drag rail checks PASS');
