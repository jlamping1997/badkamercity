const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync('/workspace/brauer-kleur-eerst-bestaand.html','utf8');
const expected=JSON.parse(fs.readFileSync('brauer_analysis/ux-refinement/earlier-expected.json','utf8'));
class El{
 constructor(tag='div'){this.tag=tag;this._text='';this.hidden=false;this.disabled=false;this.selected=false;this.attrs={};this.events={};this.children=[];this.dataset={};this.style={setProperty(){}};}
 set textContent(s){this._text=String(s);this.children=[];}get textContent(){return this._text+this.children.map(c=>c.textContent).join('');}get lastChild(){return this.children.at(-1);}
 setAttribute(k,v){this.attrs[k]=String(v);}addEventListener(k,fn){this.events[k]=fn;}append(...x){this.children.push(...x);}replaceChildren(...x){this._text='';this.children=[...x];}focus(){this.focused=true;}contains(x){return this===x||this.children.some(e=>e.contains(x));}
}
const fields={};for(const m of html.matchAll(/data-field="([^"]+)"/g))fields[m[1]]=new El();
const root=new El(),holder=new El(),specs=new El(),picker=new El('select'),figure=new El('figure'),mainImage=new El('img'),missing=new El('span');
root.querySelector=q=>{const m=q.match(/data-field="([^"]+)"/);if(m)return fields[m[1]];const e={'[data-options]':holder,'[data-specs]':specs,'[data-example-picker]':picker,'[data-product-photo]':figure,'[data-product-photo-image]':mainImage,'[data-product-photo-missing]':missing}[q];assert(e,q);return e;};
let code=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const idx=code.lastIndexOf('      build();');assert(idx>0);
code=code.slice(0,idx)+code.slice(idx).replace('      build();','      build();globalThis.qa={families,selected,linkedProducts,firstLinkedProductImage,replaceLinkedProductImages,handleImages,choose,chooseDrain,currentOptions,cabinetMatches,cabinetProduct,get cabinetState(){return cabinetState},expanded,controls:()=>controls,drain:()=>drain,family:()=>family,update};');
const sandbox={Intl,document:{getElementById:id=>{assert.equal(id,'brauer-kleur-eerst-bestaand');return root;},createElement:t=>new El(t),createElementNS:(ns,t)=>new El(t),createTextNode:s=>{const n=new El('text');n.textContent=s;return n;},addEventListener(){}}};
vm.runInNewContext(code,sandbox);const qa=sandbox.qa,money=new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR'});
const report={families:[],shopify_writes:0,browser_layout:'NOT_TESTED - no browser executable'};
function activate(f){picker.value=f.id;picker.events.change();assert.equal(qa.family().id,f.id);}
function set(f,p){if(f.kind==='cabinet')Object.assign(qa.cabinetState,p.options);else qa.selected.set(f.id,p);qa.update();}
function check(f){
 const p=f.kind==='cabinet'?qa.cabinetProduct():qa.selected.get(f.id),opts=qa.currentOptions();assert.equal(picker.value,f.id);
 const image=qa.firstLinkedProductImage(p,qa.linkedProducts);assert.equal(figure.hidden,!f.photoBacked&&!image);
 if(image){assert(p);assert.equal(mainImage.src,image.src);assert.equal(mainImage.attrs['data-photo-sku'],p.sku);}

 if(p){assert.equal(fields.sku.textContent,p.sku);assert.equal(fields.price.textContent,money.format(p.price));assert(specs.children.some(e=>e.textContent===p.ean));}
 else{assert.equal(fields.sku.textContent,'Kies eerst de afvoerindeling');assert.equal(fields.price.textContent,'Vanaf '+money.format(Math.min(...qa.cabinetMatches().map(p=>p.price))));}
 if(f.kind!=='cabinet'){assert.equal(fields.title.textContent,p.title);assert.equal(fields.description.textContent,p.description);assert.equal(Boolean(fields.future.textContent),Boolean(p.future));}
 for(const c of qa.controls()){
  if(c.axis.key==='colour')for(const entry of c.entries){
   const b=entry.button;assert(b.colourImage);
   const target=f.products.find(q=>f.axes.every(a=>q.options[a.key]===(a.key==='colour'?entry.value:opts[a.key])));
   const linked=qa.firstLinkedProductImage(target,qa.linkedProducts);
   assert.equal(b.colourImage.hidden,!linked);assert.equal(b.colourFallback.hidden,Boolean(linked));
   assert.equal(b.colourMissing.hidden,Boolean(linked));assert.equal(b.colourImage.attrs['data-colour-sku'],target?target.sku:'');
   if(linked)assert.equal(b.colourImage.src,linked.src);
  }
  const active=c.entries.find(e=>e.value===opts[c.axis.key]);assert(active);assert(!active.button.disabled);assert(!active.button.hidden);
  assert.equal(c.chosen.textContent,c.axis.key==='height'?opts[c.axis.key]+' · '+dict(p.specs)['Hoogte kraan']:f.kind==='cabinet'&&c.axis.key==='width'?f.widthLabels[opts[c.axis.key]]:opts[c.axis.key]);
  for(const entry of c.entries)if(entry.button.previewImage){
   const target=f.products.find(q=>f.axes.every(a=>q.options[a.key]===(a.key===c.axis.key?entry.value:opts[a.key])));
   assert(target);assert.equal(entry.button.previewImage.attrs['data-preview-sku'],target.sku);assert.equal(entry.button.previewImage.src,qa.firstLinkedProductImage(target,qa.linkedProducts).src);
  }
  if(c.select){assert.equal(c.select.value,opts[c.axis.key]);assert.equal(c.entries.filter(e=>e.button.selected).length,1);}
  else assert.equal(c.entries.filter(e=>e.button.attrs['aria-pressed']==='true').length,1);
  if(c.axis.kind==='texture'||c.axis.kind==='metal'){
   const open=qa.expanded.has(f.id+':'+c.axis.key);
   assert.equal(c.entries.filter(e=>!e.button.hidden).length,c.entries.length>6&&!open?6:c.entries.length);
   assert.equal(Boolean(c.toggle),c.entries.length>6);
   if(c.toggle&&!open)assert.equal(c.toggleLabel.textContent,'Bekijk meer kleuren');
  }
 }
 if(f.kind==='cabinet')assert(!qa.controls().some(c=>c.axis.key==='depth'));
}
for(const f of qa.families){
 activate(f);let valid=0,rejected=0,ambiguous=0;
 for(const p of f.products){
  set(f,p);check(f);
  for(const c of qa.controls())for(const e of c.entries){
   set(f,p);
   const candidates=f.products.filter(x=>f.axes.every(a=>x.options[a.key]===(a.key===c.axis.key?e.value:p.options[a.key])));
   assert.equal(e.button.disabled,candidates.length===0);
   if(c.select){c.select.value=e.value;c.select.events.change();}else e.button.events.click();
   check(f);
   if(candidates.length){valid++;const opts=qa.currentOptions();assert.equal(opts[c.axis.key],e.value);for(const a of f.axes)if(a.key!==c.axis.key)assert.equal(opts[a.key],p.options[a.key]);if(f.kind==='cabinet'&&!qa.cabinetProduct())ambiguous++;}
   else{rejected++;assert.equal(fields.sku.textContent,p.sku);if(c.select)assert.equal(c.select.value,p.options[c.axis.key]);}
  }
  if(f.kind==='cabinet')for(const n of ['1','2']){set(f,p);const exists=qa.cabinetMatches().some(x=>x.options.cutouts===n);assert.equal(qa.chooseDrain(n),exists);check(f);}
 }
 // Every source article remains reachable using one changed axis or explicit drain selection.
 const reached=new Set([f.default_sku]),queue=[f.products.find(p=>p.sku===f.default_sku)];
 while(queue.length){const p=queue.shift();for(const q of f.products){if(reached.has(q.sku))continue;const keys=[...f.axes.map(a=>a.key),...(f.kind==='cabinet'?['cutouts']:[])];if(keys.filter(k=>p.options[k]!==q.options[k]).length===1){reached.add(q.sku);queue.push(q);}}}
 assert.equal(reached.size,f.products.length,f.id);
 const c=qa.controls().find(c=>c.toggle);
 if(c){const p=f.products.at(-1);set(f,p);const sku=fields.sku.textContent;c.toggle.events.click();assert(c.entries.every(e=>!e.button.hidden));assert.equal(fields.sku.textContent,sku);c.toggle.events.click();check(f);}
 report.families.push({id:f.id,articles:f.products.length,valid_transitions:valid,rejected_transitions:rejected,ambiguous_transitions:ambiguous,reachable_articles:reached.size});
}
// Concrete new glass combination: bronze + 40 cm return is absent and must stay disabled.
const ob=qa.families.find(f=>f.id==='glass-oblivion');activate(ob);set(ob,ob.products.find(p=>p.options.width==='90 cm'&&p.options.glazing==='Brons glas'&&p.options.side==='30 cm zijwand'&&p.options.colour==='Chroom'));
assert(qa.controls().find(c=>c.axis.key==='side').entries.find(e=>e.value==='40 cm zijwand').button.disabled);
// The four families with existing numeric dimensions use native dropdowns.
for(const f of qa.families){activate(f);for(const c of qa.controls())if(['width','head'].includes(c.axis.key))assert.equal(Boolean(c.select),c.axis.values.length>3,f.id+':'+c.axis.key);}
// Existing exact-SKU-only enrichment must not leak to other handle models or colours.
const low=qa.families.find(f=>f.id==='tap-low');activate(low);set(low,low.products.find(p=>p.sku==='5-CE-001-HD1'));assert(specs.children.some(e=>e.textContent==='16,5 cm'));set(low,low.products.find(p=>p.sku==='5-CE-001'));assert(!specs.children.some(e=>e.textContent==='16,5 cm'));
// Independent selection persists across the expanded sample list.
const before=fields.sku.textContent;activate(ob);activate(low);assert.equal(fields.sku.textContent,before);
const embedded=JSON.parse(html.match(/const families=(.*);\n/)[1]),pool=JSON.parse(html.match(/const specPool=(.*);\n/)[1]);
for(const f of embedded)for(const p of f.products)p.specs=p.specs.map(i=>pool[i]);
assert(JSON.stringify(embedded)===JSON.stringify(expected),'Specification reconstruction must preserve audited values');
assert(!/\bfetch\s*\(|XMLHttpRequest|WebSocket/.test(code));assert(Buffer.byteLength(html)<1e6);

const crypto=require('crypto'),sources=JSON.parse(fs.readFileSync('brauer_analysis/visual-config/verified-with-previews.json','utf8'));
const seeded=[...qa.linkedProducts.values()].filter(p=>p.images.length);assert.equal(seeded.length,58);
for(const product of seeded){const sku=product.sku,uri=product.images[0].src;
 const actual=crypto.createHash('sha256').update(Buffer.from(uri.split(',')[1],'base64')).digest('hex');assert.equal(actual,sources[sku].preview_sha256);
 assert.equal(sources[sku].first_gallery_image.split('/').at(-1),sources[sku].preview_url.split('/').at(-1));
}
const wall=qa.families.find(f=>f.id==='tap-wall');assert.equal(wall.products.length,40);assert.equal(wall.axes.find(a=>a.key==='colour').values.length,1);
for(const p of wall.products){const src=sources[p.sku];assert.equal(p.ean,src.ean);assert.equal(p.options.position,src.specs['Plaats bediening']);assert.equal(p.options.position==='Rechts',dict(p.specs)['Fabrikantmodel'].endsWith('1'));}
const heights=qa.families.find(f=>f.id==='tap-height');assert.equal(heights.products.length,18);
const corrected=JSON.parse(fs.readFileSync('brauer_analysis/media-link/applied-specs.json','utf8'));for(const p of heights.products)assert.equal(dict(p.specs)['Hoogte kraan'],(corrected[p.sku]||[]).find(x=>x[0]==='Hoogte kraan')?.[1]||sources[p.sku].specs['Hoogte kraan']);
assert(!heights.axes.find(a=>a.key==='height').values.some(x=>/middel/i.test(x)));
const g=qa.families.find(f=>f.id==='glass-galactic');activate(g);assert(!qa.controls().find(c=>c.axis.key==='width').select);
function dict(pairs){return Object.fromEntries(pairs);}
report.photos_byte_exact=58;report.photo_candidate_matches_verified=true;report.inset_position_mapping_verified=40;report.distinct_source_skus=new Set(qa.families.flatMap(f=>f.products.map(p=>p.sku))).size;


// Restore the five approved dedicated handle images in the inset menu.
activate(wall);set(wall,wall.products.find(p=>p.sku==='5-CE-004'));
const handles=qa.controls().find(c=>c.axis.key==='handle');assert.equal(handles.axis.kind,'handlephotos');
for(const entry of handles.entries){assert(!entry.button.previewImage);const img=entry.button.children.find(e=>e.tag==='img');assert.equal(img.src,qa.handleImages[entry.value]);}
// Media mutations are read from the linked product, without changing any product choice.
const p=qa.selected.get(wall.id),linked=qa.linkedProducts.get(p.linked_product_id),saved=linked.images.map(x=>({...x}));
const replacement={id:'test:second',media_type:'image',src:'https://cdn.shopify.com/test/second-image.jpg'};
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:[...saved,replacement]}});assert.equal(mainImage.src,saved[0].src);
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:[replacement,...saved]}});assert.equal(mainImage.src,replacement.src);assert.equal(fields.sku.textContent,p.sku);
for(const c of qa.controls())for(const entry of c.entries)if(entry.button.previewImage&&entry.value===p.options[c.axis.key])assert.equal(entry.button.previewImage.src,replacement.src);
assert.equal(qa.replaceLinkedProductImages(qa.linkedProducts,linked.id,'wrong-sku',saved),false);assert.equal(qa.replaceLinkedProductImages(qa.linkedProducts,'missing',p.sku,saved),false);
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:[]}});assert(!figure.hidden);assert(mainImage.hidden);assert(!missing.hidden);assert.equal(fields.sku.textContent,p.sku);
for(const c of qa.controls())for(const entry of c.entries)if(entry.button.previewImage&&entry.value===p.options[c.axis.key]){assert(entry.button.previewImage.hidden);assert(!entry.button.previewMissing.hidden);assert(!entry.button.disabled);}
root.events['brauer:product-images']({detail:{productId:linked.id,sku:p.sku,images:saved}});assert.equal(mainImage.src,saved[0].src);
// An image added to a previously imageless glass product appears without a hardcoded photo table.
activate(g);const gp=qa.selected.get(g.id),glink=qa.linkedProducts.get(gp.linked_product_id);assert(figure.hidden);
root.events['brauer:product-images']({detail:{productId:glink.id,sku:gp.sku,images:[replacement]}});assert(!figure.hidden);assert.equal(mainImage.src,replacement.src);const colourButton=qa.controls().find(c=>c.axis.key==='colour').entries.find(e=>e.value===gp.options.colour).button;assert.equal(colourButton.colourImage.src,replacement.src);assert(!colourButton.colourImage.hidden);
root.events['brauer:product-images']({detail:{productId:glink.id,sku:gp.sku,images:[]}});assert(figure.hidden);
assert(!html.includes('productPhotos'));
report.all_colour_choices_use_exact_linked_first_image=true;report.handle_images_restored=true;report.media_add_append_reorder_remove_verified=true;report.product_identity_guards_verified=true;report.automatic_first_image_binding=true;

for(const f of qa.families){if(f.axes.some(a=>a.key==='colour'))assert.equal(f.axes[0].key,'colour');}report.colour_first_all_families=true;report.total_example_records=report.families.reduce((n,f)=>n+f.articles,0);report.small_dimension_groups_use_buttons=true;report.six_colour_limit=true;report.all_articles_reachable=true;report.exact_only_enrichment=true;
fs.writeFileSync('brauer_analysis/ux-refinement/earlier-verification.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report));
