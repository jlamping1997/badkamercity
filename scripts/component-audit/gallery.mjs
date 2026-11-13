import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import path from 'node:path';
const options={};for(let i=2;i<process.argv.length;i+=2)options[process.argv[i].replace(/^--/,'')]=process.argv[i+1];
if(!options.source||!options.candidate||!options.manifest||!options.output)throw Error('Use --source THEME --candidate IMPLEMENTATION --manifest PROVENANCE --output RESULT [--dom-module MODULE]');
const {Window}=await import(options['dom-module']||'happy-dom');
const provenance=JSON.parse(fs.readFileSync(options.manifest,'utf8'));
const globalBytes=fs.readFileSync(path.join(options.source,'assets/global.js'));
assert.equal(crypto.createHash('sha256').update(globalBytes).digest('hex'),provenance.files.find(f=>f.path==='assets/global.js').sha256);
const code=fs.readFileSync(path.join(options.candidate,'media-gallery.js'),'utf8'),markup=fs.readFileSync(path.join(options.candidate,'product-media-gallery.liquid'),'utf8');
const controls=markup.slice(markup.indexOf('    <div class="bc-gallery-navigation"'),markup.indexOf('    <div class="slider-buttons quick-add-hidden')).replaceAll('{{ section.id }}','fixture').replaceAll(/\{\{[^}]+\}\}/g,'Translated label');
assert.match(controls,/aria-live="polite"/);assert.equal((controls.match(/<button /g)||[]).length,2);
const results=[];const record=(id,observations)=>results.push({id,classification:'CONTROL_PASSED',observations});
const tick=()=>new Promise(r=>setImmediate(r));async function settle(){for(let i=0;i<4;i++)await tick();}
function html(n,thumbs=true){return `<media-gallery data-desktop-layout="thumbnail_slider"><div id="GalleryStatus-fixture"></div><slider-component id="GalleryViewer-fixture"><ul id="Slider-Gallery-fixture">${Array.from({length:n},(_,i)=>`<li class="product__media-item slider__slide ${i===0?'is-active':''}" id="Slide-fixture-${i}" data-media-id="fixture-${i}" data-index="${i}"><div class="product__modal-opener--image"><img src=""></div></li>`).join('')}</ul>${controls}<div class="slider-buttons"><button name="previous"></button><span class="slider-counter--current">1</span><span class="slider-counter--total">${n}</span><button name="next"></button></div></slider-component>${thumbs&&n>0?`<slider-component id="GalleryThumbnails-fixture"><button class="slider-button" name="previous"></button><ul id="Slider-Thumbnails-fixture">${Array.from({length:n},(_,i)=>`<li id="Slide-Thumbnail-${i}" data-index="${i}" data-target="fixture-${i}" data-media-position="${i+1}"><button ${i===0?'aria-current="true"':''}>${i+1}</button></li>`).join('')}</ul><button class="slider-button" name="next"></button></slider-component>`:''}</media-gallery>`;}
async function fixture({n=3,thumbs=true,mobile=false,reduced=false}={}){
 const w=new Window({url:'https://audit.invalid/products/fixture'}),c={w,animations:[],scrolls:[],timers:[],requests:[]};
 Object.defineProperty(w.document,'readyState',{configurable:true,value:'complete'});
 w.matchMedia=q=>({matches:q.includes('reduced-motion')?reduced:!mobile,addEventListener(){},removeEventListener(){}});
 w.ResizeObserver=class{observe(){}disconnect(){}};
 w.setTimeout=(fn,delay)=>{c.timers.push(fn);return c.timers.length;};w.clearTimeout=()=>{};
 w.fetch=(url)=>{c.requests.push(String(url));throw Error('Network denied');};
 w.pauseAllMedia=()=>{};w.accessibilityStrings={imageAvailable:'Image [index]'};
 Object.defineProperty(w.HTMLElement.prototype,'clientWidth',{configurable:true,get(){return this.hidden?0:this.id.includes('Thumbnail')?100:600;}});
 Object.defineProperty(w.HTMLElement.prototype,'offsetLeft',{configurable:true,get(){return Number(this.dataset.index||0)*(this.id.includes('Thumbnail')?100:600);}});
 Object.defineProperty(w.HTMLElement.prototype,'offsetWidth',{configurable:true,get(){return this.clientWidth;}});
 w.HTMLElement.prototype.getBoundingClientRect=function(){return {top:10,left:0,right:600,bottom:500,width:600,height:490};};
 w.HTMLElement.prototype.scrollTo=function(opts){c.scrolls.push(opts);this.scrollLeft=opts.left||0;this.dispatchEvent(new w.Event('scroll'));};w.scrollTo=()=>{};
 w.HTMLElement.prototype.animate=function(frames,options){const a={cancelled:false,frames,options,cancel(){this.cancelled=true;}};c.animations.push(a);return a;};
 w.document.body.innerHTML=html(n,thumbs);w.eval(globalBytes.toString());w.eval(code);await settle();
 c.gallery=w.document.querySelector('media-gallery');c.viewer=c.gallery.querySelector('[id^="GalleryViewer"]');c.nav=c.gallery.querySelector('[data-bc-gallery-navigation]');c.prev=c.nav.querySelector('[data-bc-gallery-step="-1"]');c.next=c.nav.querySelector('[data-bc-gallery-step="1"]');c.count=()=>c.nav.querySelector('[data-bc-gallery-count]').textContent;c.active=()=>c.viewer.querySelector('.is-active')?.dataset.mediaId;c.click=node=>node.click();c.flush=()=>{for(const fn of c.timers.splice(0))fn();};return c;
}
async function end(c){assert.deepEqual(c.requests,[]);await c.w.happyDOM.abort();c.w.close();}
for(const n of [0,1]){const c=await fixture({n});assert.equal(c.nav.hidden,true);assert.equal(c.gallery.hasAttribute('data-bc-gallery-ready'),false);record('GA-0'+(n+1),{renderedMedia:n,controlsHidden:true});await end(c);}
{
 const c=await fixture();assert.equal(c.count(),'1 / 3');assert.equal(c.prev.disabled,true);assert.equal(c.next.disabled,false);record('GA-03',{initialBoundaries:true,count:'1 / 3'});await end(c);
}
{
 const c=await fixture();c.click(c.next);assert.equal(c.active(),'fixture-1');assert.equal(c.count(),'2 / 3');assert.equal(c.gallery.querySelector('[data-target="fixture-1"] button').getAttribute('aria-current'),'true');record('GA-04',{nextSelectsSameMediaAndThumbnail:true});await end(c);
}
{
 const c=await fixture();c.click(c.next);c.click(c.next);c.click(c.next);assert.equal(c.active(),'fixture-2');assert.equal(c.next.disabled,true);assert.equal(c.count(),'3 / 3');record('GA-05',{endStopsWithoutWrapping:true});await end(c);
}
{
 const c=await fixture();c.click(c.next);c.click(c.prev);c.click(c.prev);assert.equal(c.active(),'fixture-0');assert.equal(c.prev.disabled,true);record('GA-06',{startStopsWithoutWrapping:true});await end(c);
}
{
 const c=await fixture();c.click(c.gallery.querySelector('[data-target="fixture-2"] button'));assert.equal(c.active(),'fixture-2');assert.equal(c.count(),'3 / 3');assert.equal(c.next.disabled,true);record('GA-07',{directThumbnailKeepsOverlayInSync:true});await end(c);
}
{
 const c=await fixture();c.gallery.setActiveMedia('fixture-2',true);assert.equal(c.active(),'fixture-2');assert.equal(c.count(),'1 / 3');assert.equal(c.prev.disabled,true);record('GA-08',{variantPrependRecomputesOrderAndControls:true});await end(c);
}
{
 const c=await fixture();c.viewer.querySelector('[data-media-id="fixture-1"]').hidden=true;c.gallery.syncGalleryNavigation();assert.equal(c.count(),'1 / 2');c.click(c.next);assert.equal(c.active(),'fixture-2');assert.equal(c.count(),'2 / 2');record('GA-09',{hiddenMediaExcluded:true});await end(c);
}
{
 const c=await fixture({thumbs:false,mobile:true});c.click(c.next);c.flush();assert.equal(c.active(),'fixture-1');assert.equal(c.count(),'2 / 3');assert.equal(c.animations.length,0);record('GA-10',{mobileModelWithoutThumbnailsWorks:true,noDesktopFade:true});await end(c);
}
{
 const c=await fixture({thumbs:false,mobile:true});c.viewer.querySelector('ul').scrollTo({left:1200});assert.equal(c.active(),'fixture-2');assert.equal(c.count(),'3 / 3');assert.equal(c.next.disabled,true);record('GA-11',{realSliderScrollEventUpdatesOverlayInMobileModel:true});await end(c);
}
{
 const c=await fixture();c.click(c.next);c.click(c.next);assert.equal(c.animations.length,2);assert.equal(c.animations[0].cancelled,true);assert.equal(c.animations[1].options.duration,180);assert.equal(c.active(),'fixture-2');record('GA-12',{rapidClicksCancelPreviousFade:true,newestSelectionWins:true,durationMs:180});await end(c);
}
{
 const c=await fixture({reduced:true});c.click(c.next);assert.equal(c.animations.length,0);record('GA-13',{reducedMotionSkipsFade:true});await end(c);
}
{
 const c=await fixture();c.click(c.next);c.gallery.remove();assert.equal(c.animations[0].cancelled,true);record('GA-14',{disconnectCancelsFade:true});await end(c);
}
{
 const c=await fixture();c.viewer.querySelectorAll('.product__media-item').forEach((node,i)=>{if(i)node.remove();});c.gallery.setActiveMedia('fixture-0',false);assert.equal(c.nav.hidden,true);assert.equal(c.gallery.hasAttribute('data-bc-gallery-ready'),false);record('GA-15',{singleMediaAfterVariantUpdateHidesControls:true});await end(c);
}
const report={task:'UI-01',environment:{node:process.version,dom:'happy-dom 21.0.4'},caseCount:results.length,executedSources:['whole existing global.js','whole candidate media-gallery.js'],candidateSha256:crypto.createHash('sha256').update(code).digest('hex'),limitations:['Synthetic markup and geometry/mediaqueries; real SliderComponent and MediaGallery classes.','No actual browser mobile viewport, keyboard default activation, zoom media playback, touch or cart actions.','No network; scroll, timers and animations are controlled models.'],results};fs.writeFileSync(options.output,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({cases:results.length,passed:results.length}));
