import fs from 'node:fs';
import assert from 'node:assert/strict';
import {Window} from 'happy-dom';
const shared=fs.readFileSync(new URL('theme/assets/bc-choice-position.js',import.meta.url),'utf8');
const script=fs.readFileSync(new URL('theme/assets/bc-sunshower-page.js',import.meta.url),'utf8');
const html=fs.readFileSync(new URL('fixtures/sunshower.html',import.meta.url),'utf8').replace(/<script\b[\s\S]*?<\/script>/gi,'').replace(/<link\b[^>]*>/gi,'');
const url='https://badkamercity.nl/products/sunshower-round-one-medium-inbouw-white#sunshower-configurator';
const results=[];
const wait=ms=>new Promise(r=>setTimeout(r,ms));
async function setup({token,input}={}) {
 const w=new Window({url,width:390,height:844});
 w.document.write(html);w.document.fonts={status:'loaded',ready:Promise.resolve()};
 w.ResizeObserver=class{observe(){} disconnect(){}};w.IntersectionObserver=class{observe(){} disconnect(){}};
 let calls=[],prepared=[];w.scrollTo=o=>calls.push(o);
 if(token)w.sessionStorage.setItem('bc-sunshower-choice-scroll',JSON.stringify(token));
 w.eval(shared);const prepare=w.BCChoicePosition.prepare;w.BCChoicePosition.prepare=(root,saved)=>{prepared.push({field:root.dataset.ssField,top:saved.top});return prepare(root,saved);};
 w.eval(script);if(input)w.dispatchEvent(new w.Event(input));
 await wait(150);return{w,calls,prepared};
}
const route=new URL(url).pathname;
for(const [name,token,expected] of [
 ['valid',{target:route,field:'kleur',top:-120,y:500,width:390,time:Date.now()},1],
 ['expired',{target:route,field:'kleur',top:-120,y:500,width:390,time:Date.now()-40000},0],
 ['different route',{target:'/products/else',field:'kleur',top:-120,y:500,width:390,time:Date.now()},0],
 ['no token',undefined,0]
]){
 const a=await setup({token});
 const field=a.w.document.querySelector('[data-ss-field]')?.dataset.ssField;
 if(name==='valid'&&!a.prepared.length){await a.w.happyDOM.abort();a.w.close();throw Error('Fixture field mismatch; first field '+field);}
 assert.equal(a.prepared.length,expected,name);assert(a.calls.length<=1,name);
 a.w.dispatchEvent(new a.w.Event('load'));await wait(120);assert(a.calls.length<=1,name+' no second correction');
 assert.equal(a.w.document.querySelector('[data-ss-total]').textContent.includes('2.725'),true);
 results.push(name);await a.w.happyDOM.abort();a.w.close();
}
for(const input of ['wheel','pointerdown','touchstart','keydown']){
 const a=await setup({token:{target:route,field:'kleur',top:-120,y:500,width:390,time:Date.now()},input});
 assert.equal(a.calls.length,0,input);results.push(input+' cancels');await a.w.happyDOM.abort();a.w.close();
}
for(const blocked of [false,true]){
 const a=await setup();const page=a.w.document.querySelector('[data-ss-page]');
 const selection=Object.fromEntries([...page.querySelectorAll('[data-ss-field]')].map(field=>[field.dataset.ssField,field.querySelector('[aria-pressed="true"]').dataset.ssOption]));
 selection.kleur='Black';
 a.w.fetch=async()=>({ok:true,json:async()=>({products:[{url:'/products/sunshower-round-one-medium-inbouw-black',selection}]})});
 if(blocked)Object.defineProperty(a.w,'sessionStorage',{get(){throw Error('blocked');}});
 page.querySelector('[data-ss-option="Black"]').click();await wait(60);
 assert.equal(a.w.location.pathname,'/products/sunshower-round-one-medium-inbouw-black');
 assert.equal(a.w.location.hash,blocked?'#sunshower-configurator':'');
 results.push(blocked?'Blocked storage retains anchor fallback':'Remembered position avoids competing native hash scroll');
 await a.w.happyDOM.abort();a.w.close();
}
fs.writeFileSync(new URL('sunshower-test-results.json',import.meta.url),JSON.stringify({status:'PASS',checks:results},null,2));console.log({status:'PASS',checks:results});
