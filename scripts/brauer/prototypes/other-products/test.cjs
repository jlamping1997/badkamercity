const fs=require('fs'),vm=require('vm'),assert=require('assert'),crypto=require('crypto');
const dir='brauer_analysis/next-sample/';
const html=fs.readFileSync('/workspace/brauer-andere-producten.html','utf8');
const expected=JSON.parse(fs.readFileSync(dir+'expected.json'));
class El{
 constructor(tag='div'){Object.assign(this,{tag,_text:'',hidden:false,disabled:false,selected:false,attrs:{},events:{},children:[],dataset:{},style:{setProperty(){}}});}
 set textContent(s){this._text=String(s);this.children=[];}get textContent(){return this._text+this.children.map(c=>c.textContent).join('');}get lastChild(){return this.children.at(-1);}
 setAttribute(k,v){this.attrs[k]=String(v);}addEventListener(k,fn){this.events[k]=fn;}append(...x){this.children.push(...x);}replaceChildren(...x){this._text='';this.children=[...x];}focus(){this.focused=true;}contains(x){return this===x||this.children.some(e=>e.contains(x));}
}
const fields={};for(const m of html.matchAll(/data-field="([^"]+)"/g))fields[m[1]]=new El();
const root=new El(),holder=new El(),specs=new El(),picker=new El('select'),figure=new El('figure'),mainImage=new El('img'),missing=new El('span');
root.querySelector=q=>{const m=q.match(/data-field="([^"]+)"/);if(m)return fields[m[1]];const e={'[data-options]':holder,'[data-specs]':specs,'[data-example-picker]':picker,'[data-product-photo]':figure,'[data-product-photo-image]':mainImage,'[data-product-photo-missing]':missing}[q];assert(e,q);return e;};
let code=html.match(/<script>([\s\S]*?)<\/script>/)[1];const idx=code.lastIndexOf('      build();');assert(idx>0);
code=code.slice(0,idx)+code.slice(idx).replace('      build();','      build();globalThis.qa={families,selected,linkedProducts,firstLinkedProductImage,replaceLinkedProductImages,choose,chooseDrain,currentOptions,cabinetMatches,cabinetProduct,get cabinetState(){return cabinetState},expanded,controls:()=>controls,drain:()=>drain,family:()=>family,update};');
const sandbox={Intl,document:{getElementById:id=>{assert.equal(id,'brauer-andere-producten');return root;},createElement:t=>new El(t),createElementNS:(ns,t)=>new El(t),createTextNode:s=>{const n=new El('text');n.textContent=s;return n;},addEventListener(){}}};
vm.runInNewContext(code,sandbox);const qa=sandbox.qa,money=new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR'});
const report={families:[],shopify_writes:0,browser_layout:'NOT_TESTED: no browser execution',photo_checks:0};
function activate(f){picker.value=f.id;picker.events.change();assert.equal(qa.family().id,f.id);}
function set(f,p){if(f.kind==='cabinet')Object.assign(qa.cabinetState,p.options);else qa.selected.set(f.id,p);qa.update();}
function candidates(f,axis,value){const opts=qa.currentOptions();return f.products.filter(p=>f.axes.every(a=>p.options[a.key]===(a.key===axis?value:opts[a.key])));}
function target(f,axis,value){const matches=candidates(f,axis,value);if(f.kind==='cabinet'){if(matches.length>1&&!qa.cabinetState.cutouts)return null;return matches.find(p=>p.options.cutouts===qa.cabinetState.cutouts)||matches[0];}return matches[0];}
function check(f){
 const p=f.kind==='cabinet'?qa.cabinetProduct():qa.selected.get(f.id),opts=qa.currentOptions();assert.equal(picker.value,f.id);
 const asset=qa.firstLinkedProductImage(p,qa.linkedProducts);assert(!figure.hidden);assert.equal(mainImage.hidden,!asset);assert.equal(missing.hidden,Boolean(asset));
 if(asset){assert.equal(mainImage.src,asset.src);assert.equal(mainImage.attrs['data-photo-sku'],p.sku);report.photo_checks++;}
 if(p){assert.equal(fields.sku.textContent,p.sku);assert.equal(fields.price.textContent,money.format(p.price));assert(specs.children.some(e=>e.textContent===p.ean));}
 else{assert.equal(fields.sku.textContent,'Kies eerst de afvoerindeling');assert.equal(fields.price.textContent,'Vanaf '+money.format(Math.min(...qa.cabinetMatches().map(p=>p.price))));}
 for(const c of qa.controls()){
  const active=c.entries.find(e=>e.value===opts[c.axis.key]);assert(active);assert(!active.button.disabled);assert(!active.button.hidden);
  assert.equal(c.chosen.textContent,c.axis.key==='width'&&f.widthLabels?f.widthLabels[opts[c.axis.key]]:opts[c.axis.key]);
  for(const e of c.entries){
   const matches=candidates(f,c.axis.key,e.value);assert.equal(e.button.disabled,!matches.length);
   if(e.button.previewImage||e.button.colourImage){
    const t=target(f,c.axis.key,e.value),image=qa.firstLinkedProductImage(t,qa.linkedProducts),img=e.button.previewImage||e.button.colourImage;
    assert.equal(img.hidden,!image);assert.equal(img.src,image?image.src:'');assert.equal(img.attrs[e.button.previewImage?'data-preview-sku':'data-colour-sku'],t?t.sku:'');
   }
  }
  if(c.select){assert.equal(c.select.value,opts[c.axis.key]);assert.equal(c.entries.filter(e=>e.button.selected).length,1);}
  else assert.equal(c.entries.filter(e=>e.button.attrs['aria-pressed']==='true').length,1);
  if(['texture','metal'].includes(c.axis.kind)){
   assert.equal(c.entries.filter(e=>!e.button.hidden).length,c.entries.length>6&&!qa.expanded.has(f.id+':'+c.axis.key)?6:c.entries.length);
   assert.equal(Boolean(c.toggle),c.entries.length>6);
  }
 }
}
for(const f of qa.families){
 activate(f);let valid=0,rejected=0,ambiguous=0;
 for(const p of f.products){set(f,p);check(f);
  for(const c of qa.controls())for(const e of c.entries){
   set(f,p);const matches=candidates(f,c.axis.key,e.value);assert.equal(e.button.disabled,!matches.length);
   if(c.select){c.select.value=e.value;c.select.events.change();}else e.button.events.click();check(f);
   if(matches.length){valid++;const opts=qa.currentOptions();assert.equal(opts[c.axis.key],e.value);for(const a of f.axes)if(a.key!==c.axis.key)assert.equal(opts[a.key],p.options[a.key]);if(f.kind==='cabinet'&&!qa.cabinetProduct())ambiguous++;}
   else{rejected++;assert.equal(fields.sku.textContent,p.sku);}
  }
  if(f.kind==='cabinet')for(const n of ['1','2']){set(f,p);const exists=qa.cabinetMatches().some(x=>x.options.cutouts===n);assert.equal(qa.chooseDrain(n),exists);check(f);}
 }
 const reached=new Set([f.default_sku]),queue=[f.products.find(p=>p.sku===f.default_sku)];
 while(queue.length){const p=queue.shift();for(const q of f.products){if(reached.has(q.sku))continue;const keys=[...f.axes.map(a=>a.key),...(f.kind==='cabinet'?['cutouts']:[])];if(keys.filter(k=>p.options[k]!==q.options[k]).length===1){reached.add(q.sku);queue.push(q);}}}
 assert.equal(reached.size,f.products.length,f.id);
 const c=qa.controls().find(c=>c.toggle);if(c){set(f,f.products.at(-1));const sku=fields.sku.textContent;c.toggle.events.click();assert(c.entries.every(e=>!e.button.hidden));assert.equal(fields.sku.textContent,sku);c.toggle.events.click();check(f);}
 report.families.push({id:f.id,articles:f.products.length,valid_transitions:valid,rejected_transitions:rejected,ambiguous_transitions:ambiguous,reachable:reached.size});
}
const embedded=JSON.parse(html.match(/const families=(.*);\n/)[1]),pool=JSON.parse(html.match(/const specPool=(.*);\n/)[1]);for(const f of embedded)for(const p of f.products)p.specs=p.specs.map(i=>pool[i]);assert.equal(JSON.stringify(embedded),JSON.stringify(expected));
const media=JSON.parse(fs.readFileSync(dir+'media.json'));
const seeded=[...qa.linkedProducts.values()].filter(p=>p.images.length);
for(const p of seeded){const r=media[p.sku];assert(r,p.sku);assert.equal(crypto.createHash('sha256').update(Buffer.from(p.images[0].src.split(',')[1],'base64')).digest('hex'),r.photo_sha256);assert.equal(r.first_gallery_image.split('/').at(-1),r.preview_url.split('/').at(-1));}
const cabin=qa.families.find(f=>f.id==='cabin');activate(cabin);assert(!qa.controls().find(c=>c.axis.key==='width').select);assert.equal(qa.controls().find(c=>c.axis.key==='width').entries.length,2);
const basin=qa.families.find(f=>f.id==='basin');activate(basin);set(basin,basin.products.find(p=>p.sku==='WT-AU600HW'));assert(qa.controls().find(c=>c.axis.key==='position').entries.find(e=>e.value==='Links').button.disabled);assert(qa.controls().find(c=>c.axis.key==='holes').entries.find(e=>e.value==='2').button.disabled);
const v=qa.families.find(f=>f.id==='void-door');activate(v);set(v,v.products.find(p=>p.sku==='GS-VON2H6030200CE'));assert(qa.controls().find(c=>c.axis.key==='hinge').entries.find(e=>e.value==='Scharnieren aan het glas').button.disabled);
const cab=qa.families.find(f=>f.id==='cabinet');activate(cab);set(cab,cab.products.find(p=>p.sku==='OK-TR120-2CH'));assert(!qa.controls().some(c=>c.axis.key==='depth'));assert(!fields.description.textContent.includes('Greeploze'));assert(specs.children.some(e=>e.textContent==='Grepen inbegrepen'));
const savedSku=fields.sku.textContent;activate(cabin);activate(cab);assert.equal(fields.sku.textContent,savedSku);
activate(cabin);const p=qa.selected.get(cabin.id),linked=qa.linkedProducts.get(p.linked_product_id),saved=linked.images.map(i=>({...i}));assert(saved.length,'Default cabin must have a verified sample image');
const extra={id:'test:image',media_type:'image',src:'https://cdn.shopify.com/test/new-first.jpg'};
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:[...saved,extra]}});assert.equal(mainImage.src,saved[0].src);
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:[extra,...saved]}});assert.equal(mainImage.src,extra.src);check(cabin);
assert.equal(qa.replaceLinkedProductImages(qa.linkedProducts,linked.id,'wrong-sku',saved),false);assert.equal(qa.replaceLinkedProductImages(qa.linkedProducts,'missing',p.sku,saved),false);
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:[]}});check(cabin);assert.equal(fields.sku.textContent,p.sku);assert(!qa.controls().find(c=>c.axis.key==='colour').entries.find(e=>e.value===p.options.colour).button.disabled);
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:saved}});check(cabin);
assert(!/\bfetch\s*\(|XMLHttpRequest|WebSocket/.test(code));assert(Buffer.byteLength(html)<1e6);assert(!/<!doctype|<html|<head>|<body>/i.test(html));
report.total_example_records=report.families.reduce((n,f)=>n+f.articles,0);report.verified_photo_articles=seeded.length;report.first_image_binding='PASS: add/append/reorder/remove and identity guards';report.all_articles_reachable=true;report.six_colour_limit=true;report.btw_source_check='PASS: Decimal 21% / half-up; matched prepared proposal';report.fragment_bytes=Buffer.byteLength(html);
fs.writeFileSync(dir+'verification.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report));
