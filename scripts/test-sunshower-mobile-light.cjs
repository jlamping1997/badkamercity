'use strict';
const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
const {Liquid} = require('liquidjs');
const path = require('path');
const base = process.env.BC_THEME_PATH || path.resolve(__dirname, '..');
const section = fs.readFileSync(base + '/sections/bc-sunshower-landing.liquid','utf8');
const source = fs.readFileSync(base + '/assets/bc-sunshower-mobile.js','utf8');
const extra = {nl:{},en:{}};
const checks = [];
function pass(s) { checks.push(s); }
const esc = x => String(x ?? '').replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function image(name) {return {src:'/images/'+name+'.jpg',width:2048,height:1200};}
function product(name,price,id) {return {id:id||name,title:name,url:'/products/'+name,price,featured_image:image(name)};}
const one=product('one',210000),plus=product('plus',300000);
const blocks=['cleaning','seat','wiper'].map((kind,i)=>({settings:{kind,product:product(kind,[4000,32501,2900][i]),...Object.fromEntries((kind==='cleaning'?[]:['white','black','grey','sand']).map(color=>['product_'+color,product(kind+'-'+color,10)]))}}));
async function render(locale,empty=false) {
 const strings={...JSON.parse(fs.readFileSync(base+'/locales/'+(locale==='nl'?'nl.json':'en.default.json'),'utf8').replace(/^\s*\/\*[\s\S]*?\*\/\s*/,'')),...extra[locale]};
 const engine=new Liquid({strictFilters:true});
 engine.registerFilter('t',(key,...args)=>{let v=String(key).split('.').reduce((a,k)=>a?.[k],strings);assert.equal(typeof v,'string','translation '+key);for(const [k,val] of args) v=v.replaceAll('{{ '+k+' }}',val).replaceAll('{{'+k+'}}',val);return v;});
 engine.registerFilter('asset_url',x=>'/assets/'+x);
 engine.registerFilter('stylesheet_tag',x=>'<link rel="stylesheet" href="'+esc(x)+'">');
 engine.registerFilter('image_url',(x,...args)=>x?.src+'?width='+Object.fromEntries(args).width);
 engine.registerFilter('image_tag',(src,...args)=>'<img src="'+esc(src)+'" '+args.filter(([k])=>k!=='widths').map(([k,v])=>k+'="'+esc(v)+'"').join(' ')+'>');
 engine.registerFilter('money',x=>'€'+(x/100).toFixed(2));
 return engine.parseAndRender(section.replace(/{% schema %}[\s\S]*?{% endschema %}/,''),{section:{id:'fixture',settings:empty?{}:{one_product:one,plus_product:plus,hero_image:image('hero'),one_image:image('red'),plus_image:image('blue')},blocks:empty?[]:blocks},pages:{contact:{url:'/pages/contact'}}});
}
class Events {
 constructor(){this.events=new Map();}
 addEventListener(k,fn){if(!this.events.has(k))this.events.set(k,new Set());this.events.get(k).add(fn);}
 removeEventListener(k,fn){this.events.get(k)?.delete(fn);}
 emit(k,event={}){for(const fn of this.events.get(k)||[])fn(event);}
}
class El extends Events {
 constructor(dataset={},attrs={}){super();this.dataset=dataset;this.attrs=attrs;this.hidden=false;this.parent=null;this.open=true;}
 setAttribute(k,v){this.attrs[k]=v;} removeAttribute(k){delete this.attrs[k];} getAttribute(k){return this.attrs[k]??null;}
 closest(q){return q==='a'&&this.attrs.href?this:this.parent?.closest(q);}
 contains(el){for(let p=el;p;p=p.parent)if(p===this)return true;return false;}
 focus(){doc.activeElement=this;} scrollIntoView(){this.scrolled=true;}
 matches(q){return q==='[data-bcsse-mobile-light]'&&Boolean(this.dataset.bcsseSectionId);}
}
let doc;
function fixture(id){
 const root=new El({bcsseSectionId:id,bcsseConfiguratorUrl:'/products/one#sunshower-configurator',bcsseUvUrl:'/products/plus#sunshower-configurator'});
 const heroCopy=new El(),modelSummary=new El(),overview=new El(),infrared=new El({bcsseLightPanel:'infrared'}),uv=new El({bcsseLightPanel:'uv'}),cta=new El(),models=new El(),shelf=new El(),title=new El();
 const headings={infrared:new El(),uv:new El()};headings.infrared.parent=infrared;headings.uv.parent=uv;
 const links=['infrared','uv','overview','infrared','uv'].map(mode=>new El({bcsseLightLink:mode},{href:mode==='overview'?'#bcsse-lights-'+id:'#bcsse-light-'+mode+'-'+id}));
 const modelLink=new El({},{href:'#bcsse-models-'+id});
 for(const e of [overview,infrared,uv,cta,models,shelf,title,...links,modelLink])e.parent=root;
 title.parent=heroCopy;heroCopy.parent=root;modelSummary.parent=models;models.querySelector=s=>s==='summary'?modelSummary:null;
 root.querySelector=s=>({'.bcsse-hero__copy':heroCopy,'[data-bcsse-light-overview]':overview,'.bcsse-mobile-light':root,'[data-bcsse-mobile-configurator]':cta,'[data-bcsse-model-disclosure]':models,'[data-bcsse-accessory-shelf]':shelf}[s]);
 root.querySelectorAll=s=>s==='[data-bcsse-light-panel]'?[infrared,uv]:s==='[data-bcsse-light-link]'?links:[];
 root.nodes={heroCopy,modelSummary,overview,infrared,uv,cta,models,shelf,title,headings,links,modelLink};return root;
}
async function main(){
 for(const locale of ['nl','en']){
  const html=await render(locale);
  assert.equal((html.match(/<h1\b/g)||[]).length,1);
  assert.equal((html.match(/<article class="bcsse-accessory /g)||[]).length,3);
  assert.equal((html.match(/class="bcsse-swatch(?: bcsse-swatch--selected)?"/g)||[]).length,8);
  for(const amount of ['€40.00','€325.01','€29.00'])assert(html.includes(amount));
  for(const id of ['bcsse-light-infrared-fixture','bcsse-light-uv-fixture']){
   assert(html.includes('href="#'+id+'"'));assert(html.includes('id="'+id+'"'));
  }
  assert(!/<section class="bcsse-light-detail[^>]*\bhidden\b/.test(html),'no-script details readable');
  assert(html.includes('href="/products/plus#sunshower-configurator"'));
  assert(html.includes('<source media="(max-width: 749px)" srcset="data:image/svg+xml,'));
  assert(html.includes('id="bcsse-models-fixture"'));assert(html.includes('data-bcsse-model-disclosure open'));
  const empty=await render(locale,true);assert.equal((empty.match(/<h1\b/g)||[]).length,1);assert(!empty.includes('NaN'));
  pass(locale+' Liquid rendering: single H1, catalog prices, 8 color links, no-JS details and URL fallbacks');
 }
 const roots=[fixture('alpha'),fixture('beta')];
 doc=new Events();doc.readyState='complete';doc.activeElement=null;doc.querySelectorAll=()=>roots;
 doc.getElementById=id=>{for(const r of roots){let n=r.nodes,k=r.dataset.bcsseSectionId;if(id==='bcsse-title-'+k)return n.title;if(id==='bcsse-light-heading-infrared-'+k)return n.headings.infrared;if(id==='bcsse-light-heading-uv-'+k)return n.headings.uv;}return null;};
 const win=new Events();win.location={hash:''};const mqs=[];win.matchMedia=()=>{let m=new Events();m.matches=true;mqs.push(m);return m;};win.history={pushState:(data,title,hash)=>{win.location.hash=hash;}};
 const context={window:win,document:doc,Map,Array};vm.runInNewContext(source,context);
 const a=roots[0],n=a.nodes;assert(n.models.open===false);assert(n.overview.hidden===false&&n.uv.hidden&&n.infrared.hidden);assert.equal(n.cta.href,a.dataset.bcsseConfiguratorUrl);
 function click(root,link,extra={}) {let e={target:link,button:0,defaultPrevented:false,preventDefault(){this.defaultPrevented=true;},...extra};root.emit('click',e);return e;}
 let e=click(a,n.links[1]);assert(e.defaultPrevented);assert.equal(win.location.hash,'#bcsse-light-uv-alpha');assert.equal(n.cta.href,a.dataset.bcsseUvUrl);assert(n.overview.hidden&&!n.uv.hidden&&n.infrared.hidden);assert.equal(doc.activeElement,n.headings.uv);assert.equal(n.links[1].attrs['aria-current'],'true');
 win.location.hash='#bcsse-accessories-alpha';win.emit('hashchange');assert.equal(n.cta.href,a.dataset.bcsseUvUrl);assert(!n.uv.hidden);pass('UV selection retains PLUS configurator while visiting accessories');
 click(a,n.modelLink);assert(n.models.open);win.location.hash='#bcsse-models-alpha';win.emit('hashchange');assert.equal(n.cta.href,a.dataset.bcsseUvUrl);pass('Model anchor opens native disclosure without losing UV route');
 click(a,n.links[0]);assert.equal(n.cta.href,a.dataset.bcsseConfiguratorUrl);assert(!n.infrared.hidden&&n.uv.hidden);
 click(a,n.links[2]);assert(!n.overview.hidden&&n.infrared.hidden&&n.uv.hidden);assert.equal(doc.activeElement,n.title);assert.equal(n.cta.href,a.dataset.bcsseConfiguratorUrl);
 click(a,n.links[1]);win.location.hash='';win.emit('popstate');assert(!n.overview.hidden);assert.equal(doc.activeElement,n.title);assert.equal(n.cta.href,a.dataset.bcsseConfiguratorUrl);pass('IR/UV/overview and browser Back restore panels, route, selection and focus');
 click(a,n.links[1]);mqs[0].matches=false;mqs[0].emit('change');assert(n.models.open);assert.equal(n.cta.href,a.dataset.bcsseConfiguratorUrl);assert(n.uv.hidden&&n.infrared.hidden);assert.equal(doc.activeElement,n.title);assert.equal(n.shelf.tabIndex,-1);
 n.title.focus();mqs[0].matches=true;mqs[0].emit('change');assert.equal(doc.activeElement,n.headings.uv);assert(!n.uv.hidden);assert.equal(n.cta.href,a.dataset.bcsseUvUrl);assert.equal(n.shelf.tabIndex,0);pass('Desktop resize restores original CTA/open models; phone resize restores hash view');
 doc.activeElement=n.links[0];mqs[0].matches=false;mqs[0].emit('change');assert.equal(doc.activeElement,n.title);mqs[0].matches=true;mqs[0].emit('change');doc.activeElement=n.modelSummary;mqs[0].matches=false;mqs[0].emit('change');assert.equal(doc.activeElement,n.title);mqs[0].matches=true;mqs[0].emit('change');pass('Leaving phone layout restores focus from overview card and model summary');
 assert(!click(a,n.links[0],{ctrlKey:true}).defaultPrevented);pass('Modified native links remain available');
 win.BCSunshowerMobileLight.init(doc);assert.equal(a.events.get('click').size,1);assert.equal(roots[1].events.get('click').size,1);
 click(roots[1],roots[1].nodes.links[0]);assert.equal(roots[1].nodes.cta.href,roots[1].dataset.bcsseConfiguratorUrl);win.emit('hashchange');assert(!n.overview.hidden);pass('Multiple section roots and repeated initialization remain isolated');
 doc.emit('shopify:section:unload',{target:a});assert.equal(a.events.get('click').size,0);assert.equal(a.dataset.bcsseMobileReady,undefined);assert(!n.uv.hidden&&!n.infrared.hidden);doc.emit('shopify:section:load',{target:a});assert.equal(a.events.get('click').size,1);pass('Theme-editor unload restores fallback and reload installs one controller');
 console.log(JSON.stringify({status:'passed',checks,limits:'Logic uses a small DOM test double; CSS layout and browser viewport behavior require root browser QA.'},null,2));
}
main().catch(err=>{console.error(err);process.exitCode=1;});
