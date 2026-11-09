import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
const require=createRequire(process.env.BC_TEST_DEPENDENCIES||new URL('package.json',import.meta.url));
const {Window}=require('happy-dom');
const source=fs.readFileSync(new URL('../../../../shopify/current/assets/bc-brand-slider.js',import.meta.url),'utf8');
const results=[],record=test=>results.push({test,result:'PASS'});
async function setup({width=1348,reduced=false,rtl=false,count=9,visible=true}={}){
 const w=new Window({url:'https://example.invalid',width,height:914});
 let viewport=width,prefersReduced=reduced,hidden=false,scroll=0,clock=0,id=0,intersection;
 const frames=new Map(),media=[];
 w.requestAnimationFrame=fn=>{frames.set(++id,fn);return id;};w.cancelAnimationFrame=id=>frames.delete(id);
 Object.defineProperty(w.document,'hidden',{get:()=>hidden,configurable:true});
 w.matchMedia=query=>{const m=new w.EventTarget();Object.defineProperty(m,'matches',{get:()=>query.includes('min-width')?viewport>=990:prefersReduced});media.push(m);return m;};
 w.ResizeObserver=class{observe(){}disconnect(){}};
 w.IntersectionObserver=class{constructor(cb){intersection=cb;}observe(){intersection([{isIntersecting:visible}]);}disconnect(){}};
 w.document.body.innerHTML='<bc-brand-slider data-brand-autoplay><div data-brand-controls hidden><button data-brand-toggle data-label-play="Afspelen" data-label-pause="Pauzeren"><span></span></button><button data-brand-previous></button><button data-brand-next></button></div><ul data-brand-track tabindex="0" style="column-gap:48px;direction:'+(rtl?'rtl':'ltr')+'">'+Array.from({length:count},(_,n)=>'<li data-bc-brand="brand-'+n+'"><a id="brand-'+n+'" href="/brand/'+n+'">Brand '+n+'</a></li>').join('')+'</ul></bc-brand-slider>';
 const root=w.document.querySelector('bc-brand-slider'),track=root.querySelector('ul'),calls=[];
 Object.defineProperties(track,{clientWidth:{get:()=>viewport},scrollWidth:{get:()=>Math.max(0,track.children.length*248-48)},scrollLeft:{get:()=>scroll,set:value=>{const max=Math.max(0,track.scrollWidth-viewport);scroll=(rtl?-1:1)*Math.min(max,Math.max(0,Math.round(Math.abs(value))));track.dispatchEvent(new w.Event('scroll'));}}});
 for(const el of track.children)el.getBoundingClientRect=()=>({width:200});
 track.scrollBy=({left,behavior})=>{calls.push({left,behavior});track.scrollLeft=scroll+left;};
 track.scrollTo=({left,behavior})=>{calls.push({left,behavior});track.scrollLeft=left;};
 const advance=(duration=16)=>{clock+=duration;const batch=[...frames.values()];frames.clear();for(const fn of batch)fn(clock);};
 const advanceFrames=(count=60,duration=1000/60)=>{for(let i=0;i<count;i++)advance(duration);};
 w.eval(source);advance(0);
 return {w,root,track,calls,advance,advanceFrames,frames,
  resize:value=>{viewport=value;w.dispatchEvent(new w.Event('resize'));advance(0);},
  reduce:value=>{prefersReduced=value;for(const m of media)m.dispatchEvent(new w.Event('change'));advance(0);},
  visible:value=>{intersection([{isIntersecting:value}]);},
  hidden:value=>{hidden=value;w.document.dispatchEvent(new w.Event('visibilitychange'));},
  close:async()=>{root.remove();await w.happyDOM.abort();w.close();}};
}
let p=await setup();assert.equal(p.root.originals.length,9);assert.equal(p.track.querySelectorAll('[data-brand-clone]').length,18);assert(p.root.hasAttribute('data-brand-moving'));assert(p.track.scrollWidth>=p.root.loopWidth+p.track.clientWidth);record('desktop-continuous-full-width-coverage-with-nine-original-brands');
p.advanceFrames(6);const start=p.track.scrollLeft;p.advanceFrames(60);const moved=(start-p.track.scrollLeft+p.root.loopWidth)%p.root.loopWidth;assert(moved>=17&&moved<=19);record('rightward-motion-18px-per-second-with-fractional-frame-accumulation');
p.track.scrollLeft=1;p.resize(1348);p.advance(0);p.advance(100);assert(p.track.scrollLeft>p.root.loopWidth-3);record('cycle-wrap-retains-identical-logo-sequence-without-empty-gap');
p.root.dispatchEvent(new p.w.Event('mouseenter'));const hover=p.track.scrollLeft;p.advanceFrames(60);assert.equal(p.track.scrollLeft,hover);assert(!p.root.hasAttribute('data-brand-moving'));p.root.dispatchEvent(new p.w.Event('mouseleave'));p.advanceFrames(20);assert.notEqual(p.track.scrollLeft,hover);record('hover-pauses-and-leaving-resumes-without-catch-up-jump');
p.root.originals[0].querySelector('a').focus();const focused=p.track.scrollLeft;p.advanceFrames(60);assert.equal(p.track.scrollLeft,focused);p.root.originals[0].querySelector('a').blur();p.advanceFrames(20);assert.notEqual(p.track.scrollLeft,focused);record('keyboard-focus-pauses-and-blur-resumes');
p.root.toggle.click();assert.equal(p.root.toggle.getAttribute('aria-label'),'Afspelen');const paused=p.track.scrollLeft;p.advanceFrames(60);assert.equal(p.track.scrollLeft,paused);p.root.dispatchEvent(new p.w.Event('mouseleave'));p.advanceFrames(20);assert.equal(p.track.scrollLeft,paused);p.root.toggle.click();p.advanceFrames(20);assert.notEqual(p.track.scrollLeft,paused);assert.equal(p.root.toggle.getAttribute('aria-label'),'Pauzeren');record('explicit-pause-persists-until-play');
p.hidden(true);const hidden=p.track.scrollLeft;p.advanceFrames(60);assert.equal(p.track.scrollLeft,hidden);p.hidden(false);p.advanceFrames(20);assert.notEqual(p.track.scrollLeft,hidden);record('hidden-document-stops-animation');
p.visible(false);const offscreen=p.track.scrollLeft;p.advanceFrames(60);assert.equal(p.track.scrollLeft,offscreen);p.visible(true);p.advanceFrames(20);assert.notEqual(p.track.scrollLeft,offscreen);record('offscreen-rail-stops-animation');
const clones=[...p.track.querySelectorAll('[data-brand-clone]')];assert(clones.every(li=>li.getAttribute('aria-hidden')==='true'));assert(clones.every(li=>!li.querySelector('[id]')));assert(clones.every(li=>li.querySelector('a').tabIndex===-1));assert.equal(new Set([...p.track.querySelectorAll('[id]')].map(n=>n.id)).size,9);const down=new p.w.MouseEvent('mousedown',{bubbles:true,cancelable:true});clones[0].querySelector('a').dispatchEvent(down);assert(down.defaultPrevented);const click=new p.w.MouseEvent('click',{bubbles:true,cancelable:true});clones[0].querySelector('a').dispatchEvent(click);assert(!click.defaultPrevented);record('visual-copies-have-no-duplicate-ids-or-tab-stops-and-keep-native-links');
p.root.next.click();assert.equal(p.track.querySelectorAll('[data-brand-clone]').length,0);assert(p.root.userPaused);assert.equal(p.root.toggle.getAttribute('aria-label'),'Afspelen');const manual=p.track.scrollLeft;p.advanceFrames(60);assert.equal(p.track.scrollLeft,manual);record('manual-arrow-navigation-stops-autoplay-and-restores-original-nine');
p.root.toggle.click();p.advanceFrames(5);assert(p.root.loopWidth>0);p.reduce(true);assert.equal(p.track.querySelectorAll('[data-brand-clone]').length,0);assert(!p.root.hasAttribute('data-brand-moving'));assert(p.root.toggle.hidden);p.reduce(false);p.advanceFrames(20);assert(p.root.hasAttribute('data-brand-moving'));record('live-reduced-motion-preference-disables-and-restores-automatic-mode');await p.close();
for(const width of [320,390,750,989]){
 p=await setup({width});assert(!p.root.hasAttribute('data-brand-moving'));assert(p.root.toggle.hidden);assert.equal(p.track.children.length,9);p.track.scrollLeft=200;p.advanceFrames(60);assert.equal(p.track.scrollLeft,200);p.root.next.click();assert(p.calls.length);record('manual-swipe-and-buttons-no-automatic-motion-'+width+'px');await p.close();
}
p=await setup({reduced:true});assert.equal(p.track.children.length,9);assert(p.root.toggle.hidden);p.root.next.click();assert.equal(p.calls.at(-1).behavior,'auto');record('reduced-motion-starts-with-native-static-rail');await p.close();
p=await setup({width:4000});assert(p.track.scrollWidth>=p.root.loopWidth+p.track.clientWidth);p.advanceFrames(30);assert(p.track.scrollLeft>0);record('ultrawide-viewport-keeps-entire-rail-filled');await p.close();
for(const count of [0,1]){p=await setup({count});assert.equal(p.track.children.length,count);assert(!p.root.hasAttribute('data-brand-moving'));assert(p.root.controls.hidden);record('zero-or-one-brand-does-not-loop-'+count);await p.close();}
p=await setup({rtl:true});p.advanceFrames(60);assert(p.track.scrollLeft<0);assert(Math.abs(p.track.scrollLeft)>=17);record('rtl-scroll-sign-still-moves-logos-physically-right');await p.close();
p=await setup();p.track.dispatchEvent(new p.w.PointerEvent('pointerdown',{pointerType:'touch',bubbles:true}));assert.equal(p.track.children.length,9);assert(p.root.userPaused);assert(!p.root.hasAttribute('data-brand-moving'));record('touch-interaction-on-wide-screen-switches-to-manual');await p.close();
p=await setup();p.root.remove();assert.equal(p.track.children.length,9);assert.equal(p.frames.size,0);p.w.document.body.append(p.root);p.advance(0);assert.equal(p.root.originals.length,9);assert.equal(p.track.children.length,27);p.root.toggle.click();assert(p.root.userPaused);record('editor-reconnect-cleans-copies-and-does-not-duplicate-controls');await p.close();
fs.writeFileSync(new URL('checks.json',import.meta.url),JSON.stringify({status:'PASS',checks:results.length,results,scope:'Real marquee JavaScript with synthetic geometry, deterministic animation frames and viewport/media/visibility events. Browser visual motion checked separately.'},null,2)+'\n');console.log(results.length+' continuous brand rail checks PASS');

