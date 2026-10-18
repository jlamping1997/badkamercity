'use strict';
/**
 * Liquid contracts for Sunshower quick-shop. Requires liquidjs on NODE_PATH.
 * Set BC_THEME_PATH to a downloaded theme. Shopify-owned form/image/money/t
 * helpers use deterministic adapters; native Shopify output still needs browser QA.
 */
const fs=require('node:fs'), path=require('node:path'), assert=require('node:assert/strict');
const {Liquid}=require('liquidjs');
const base=process.env.BC_THEME_PATH||path.resolve(__dirname,'..'), checks=[];
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const attrs=x=>Object.fromEntries([...x.matchAll(/([\w:-]+)="([^"]*)"/g)].map(m=>[m[1],m[2]]));
const image=name=>({src:'/images/'+name+'.jpg',width:2500,height:1800});
function product(name,id,cents,available=true){return {id,title:name,url:'/products/'+name,price:cents+9999,featured_image:image(name),selected_or_first_available_variant:{id:id*100+1,price:cents,available}};}
function fixture(){
 const cleaning=product('cleaning',10,4000);
 const colors=['white','black','grey','sand'];
 const seat=Object.fromEntries(colors.map((c,i)=>[c,product('seat-'+c,101+i,32501+i)]));
 const wiper=Object.fromEntries(colors.map((c,i)=>[c,product('wiper-'+c,201+i,2900+i)]));
 const block=(kind,id,ps)=>({id,settings:{kind,product:ps.sand,...Object.fromEntries(Object.entries(ps).map(([c,p])=>['product_'+c,p]))}});
 const sb=block('seat','sunseat',seat);sb.settings.image_override=image('seat-selected-override');
 return {cleaning,seat,wiper,blocks:[{id:'cleaning',settings:{kind:'cleaning',product:cleaning}},sb,block('wiper','sunswipe',wiper)]};
}
function adapter(source){
 // Only the Shopify product-form wrapper is substituted. Its actual hidden fields
 // and action are Shopify's responsibility and are verified in the real browser.
 // LiquidJS decodes unicode escapes in quoted literals; Shopify Liquid keeps
 // the backslash literal. Preserve Shopify's JSON script escaping in this adapter.
 return source.replaceAll(String.raw`'\u003c'`,String.raw`'\\u003c'`).replace(/{%-?\s*doc\s*-?%}[\s\S]*?{%-?\s*enddoc\s*-?%}/g,'')
  .replace(/{%-?\s*schema\s*-?%}[\s\S]*?{%-?\s*endschema\s*-?%}/g,'')
  .replace(/{%-?\s*form\s+'product',\s*accessory_product,\s*id:\s*shop_form_id,\s*class:\s*'bcsse-shop-form',\s*data-bcsse-shop-form:\s*''\s*-?%}/g,'<form method="post" action="{{ routes.cart_add_url }}" id="{{ shop_form_id }}" class="bcsse-shop-form" data-bcsse-shop-form=""><input type="hidden" name="form_type" value="product">')
  .replace(/{%-?\s*endform\s*-?%}/g,'</form>');
}
async function render(locale,f=fixture(),sectionId='fixture'){
 const strings=JSON.parse(fs.readFileSync(path.join(base,'locales',locale==='nl'?'nl.json':'en.default.json'),'utf8').replace(/^\s*\/\*[\s\S]*?\*\/\s*/,''));
 const money=cents=>new Intl.NumberFormat(locale==='nl'?'nl-NL':'en-IE',{style:'currency',currency:'EUR'}).format(Number(cents)/100);
 const files=new Map([['/snippets/bc-sunshower-shop-card.liquid',adapter(fs.readFileSync(path.join(base,'snippets/bc-sunshower-shop-card.liquid'),'utf8'))]]);
 const read=file=>{assert(files.has(file),'known snippet '+file);return files.get(file);};
 const engine=new Liquid({root:'/snippets',extname:'.liquid',strictFilters:true,globals:{routes:{cart_url:'/cart',cart_add_url:'/cart/add'}},fs:{sep:'/',resolve:(dir,file,ext)=>path.posix.resolve(dir,file.endsWith(ext)?file:file+ext),dirname:path.posix.dirname,exists:async file=>files.has(file),existsSync:file=>files.has(file),readFile:async file=>read(file),readFileSync:read}});
 engine.registerFilter('t',(key,...pairs)=>{let v=String(key).split('.').reduce((a,k)=>a?.[k],strings);assert.equal(typeof v,'string','translation '+locale+' '+key);for(const [k,val] of pairs)v=v.replaceAll('{{ '+k+' }}',val).replaceAll('{{'+k+'}}',val);assert(!v.includes('{{'),'resolved translation '+key);return v;});
 engine.registerFilter('json',v=>JSON.stringify(v??null));
 engine.registerFilter('asset_url',v=>'/assets/'+v);
 engine.registerFilter('stylesheet_tag',v=>'<link rel="stylesheet" href="'+esc(v)+'">');
 engine.registerFilter('image_url',(v,...pairs)=>v?.src+'?width='+Object.fromEntries(pairs).width);
 engine.registerFilter('image_tag',(src,...pairs)=>'<img src="'+esc(src)+'" '+pairs.filter(([k])=>k!=='widths').map(([k,v])=>k+'="'+esc(v)+'"').join(' ')+'>');
 engine.registerFilter('money',money);
 const section={id:sectionId,settings:{one_product:product('one',1,200000),plus_product:product('plus',2,300000),hero_image:image('hero'),one_image:image('infrared'),plus_image:image('uv')},blocks:f.blocks};
 const html=await engine.parseAndRender(adapter(fs.readFileSync(path.join(base,'sections/bc-sunshower-landing.liquid'),'utf8')),{section,pages:{contact:{url:'/pages/contact'}},routes:{cart_url:'/cart',cart_add_url:'/cart/add'}});
 return {html,money,strings};
}
function cards(html){return [...html.matchAll(/<article\b[^>]*data-bcsse-shop-card[\s\S]*?<\/article>/g)].map(m=>{
 const content=m[0],scripts=[...content.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)],forms=[...content.matchAll(/<form\b[^>]*>[\s\S]*?<\/form>/g)];
 assert.equal(scripts.length,1,'one data script per card');assert.equal(attrs(scripts[0][1]).type,'application/json');assert(scripts[0][1].includes('data-bcsse-shop-data'));
 assert.equal(forms.length,1,'one product form per card');const form=forms[0][0],submit=content.match(/<button\b[^>]*type="submit"[^>]*>/)?.[0];assert(submit,'submit button');
 return {content,data:JSON.parse(scripts[0][2]),rawData:scripts[0][2],form,formAttrs:attrs(form.match(/^<form[^>]*>/)[0]),input:[...form.matchAll(/<input\b[^>]*>/g)].map(m=>attrs(m[0])),submit};
});}
async function main(){
 for(const locale of ['nl','en']){
  const f=fixture(),{html,money,strings}=await render(locale,f),cs=cards(html);
  const js=fs.readFileSync(path.join(base,'assets/bc-sunshower-shop.js'),'utf8');
  for(const match of js.matchAll(/root\.querySelector(?:All)?\('\[([^\]]+)\]'\)/g))assert(html.includes(match[1]),'JS selector exists in rendered markup: '+match[1]);
  for(const match of js.matchAll(/label\('([^']+)'\)/g)){const attribute='data-'+match[1].replace(/[A-Z]/g,c=>'-'+c.toLowerCase());for(const c of cs)assert(attrs(c.content.match(/^<article[^>]*>/)[0])[attribute],'translated JS dataset label: '+attribute);}
  assert.equal(cs.length,3);assert.equal((html.match(/data-bcsse-shop-choice=/g)||[]).length,8);
  assert.deepEqual(cs.map(c=>c.data.choices.length),[1,4,4]);assert.deepEqual(cs.map(c=>c.data.initial),['default','sand','sand']);
  const expected=[[f.cleaning],Object.values(f.seat),Object.values(f.wiper)];
  cs.forEach((c,i)=>{
   assert.equal(c.formAttrs.action,'/cart/add');assert.equal(c.formAttrs.method,'post');assert.equal(c.formAttrs.class,'bcsse-shop-form');assert(c.form.includes('data-bcsse-shop-form'));
   assert(c.input.some(a=>a.name==='quantity'&&a.value==='1'));
   c.data.choices.forEach((choice,j)=>{const p=expected[i][j];assert.equal(choice.id,String(p.selected_or_first_available_variant.id));assert.equal(choice.price,money(p.selected_or_first_available_variant.price),'use variant price');assert.equal(choice.available,true);assert.equal(choice.url,p.url);assert.equal(choice.title,p.title);assert.equal(choice.image.alt,p.title);assert(choice.image.srcset.includes('w'));assert.equal(choice.label,i===0?'':strings.ss_experience.colors[['white','black','grey','sand'][j]]);});
   const selected=c.data.choices.find(x=>x.key===c.data.initial);assert.equal(c.input.find(a=>a.name==='id').value,selected.id);
   assert(!/\sdisabled(?:[\s=>])/.test(c.submit));assert(c.content.includes('href="'+selected.url+'" data-bcsse-shop-link'));
   assert(c.content.includes('aria-describedby="'+c.formAttrs.id+'-status"'));assert(c.content.includes('id="'+c.formAttrs.id+'-status" role="status" aria-live="polite"'));
   assert(c.content.includes('href="/cart" data-bcsse-shop-cart-link hidden'));
  });
  assert.equal(cs[1].data.choices.find(c=>c.key==='sand').image.src,'/images/seat-selected-override.jpg?width=2000');
  for(const c of cs[1].data.choices.filter(c=>c.key!=='sand'))assert.equal(c.image.src,'/images/seat-'+c.key+'.jpg?width=2000','override only selected product');
  for(const color of ['white','black','grey','sand']){assert(cs[1].content.includes('href="/products/seat-'+color+'" data-bcsse-shop-choice="'+color+'"'));assert(cs[2].content.includes('href="/products/wiper-'+color+'" data-bcsse-shop-choice="'+color+'"'));}
  const formIds=[...cs,...cards((await render(locale,f,'second')).html)].map(c=>c.formAttrs.id);assert.equal(new Set(formIds).size,6);assert(formIds.every(id=>/^bcsse-shop-(fixture|second)-(cleaning|sunseat|sunswipe)$/.test(id)));
  checks.push(locale+': JS selectors and translated dataset labels match Liquid; 3 cards, 8 native colour links, 1+4+4 choices, variant IDs/prices/availability, selected override, six unique forms, accessible statuses and native form fallback');
  assert.equal((html.match(/<h1\b/g)||[]).length,1);
  for(const kind of ['infrared','uv']){assert(html.includes('id="bcsse-light-'+kind+'-fixture"'));assert(html.includes('href="#bcsse-light-'+kind+'-fixture"'));assert(html.includes('data-bcsse-light-panel="'+kind+'"'));}
  for(const p of ['one','plus'])assert(html.includes('href="/products/'+p+'#sunshower-configurator"'));
  assert(html.includes('data-bcsse-model-disclosure open'));assert(!/<section class="bcsse-light-detail[^>]*\bhidden\b/.test(html));assert(html.includes('data-bcsse-accessory-shelf'));
  for(const script of ['mobile','shop'])assert(html.includes('src="/assets/bc-sunshower-'+script+'.js"'));
  checks.push(locale+': IR/UV panels, model disclosure, configurator routes, shelf and readable no-JS details remain present');
  const bad=fixture();bad.cleaning.title='Set </script><script>alert("bad")</script> & "clean"';const badHtml=(await render(locale,bad)).html,badCard=cards(badHtml)[0];
  assert.equal(badCard.data.choices[0].title,bad.cleaning.title);assert.equal(badCard.data.choices[0].image.alt,bad.cleaning.title);assert(!badCard.rawData.includes('<'));assert(badCard.rawData.includes('\\u003c/script>'));assert(!badHtml.includes('<script>alert('));
  checks.push(locale+': malicious closing-script title stays escaped and JSON round trips');
  const unavailable=fixture();unavailable.seat.sand.selected_or_first_available_variant.available=false;const uc=cards((await render(locale,unavailable)).html)[1];
  assert(/\sdisabled(?:[\s=>])/.test(uc.submit));assert(uc.content.includes(strings.ss_quick_shop.unavailable));assert.equal(uc.data.choices.find(c=>c.key==='sand').available,false);assert.equal(uc.data.choices.find(c=>c.key==='white').available,true);
  const noImage=fixture();noImage.cleaning.featured_image=null;noImage.seat.white.featured_image=null;const nih=(await render(locale,noImage)).html,nic=cards(nih);
  assert(!nic[0].content.includes('data-bcsse-shop-image'));assert.equal(nic[0].data.choices[0].image.src,'');assert.equal(nic[0].data.choices[0].image.srcset,'');assert.equal(nic[1].data.choices.find(c=>c.key==='white').image.src,'');assert.equal(nic[1].data.choices.find(c=>c.key==='white').available,true);assert(!nih.includes('NaN'));assert(!nih.includes('undefined?width='));
  const empty=fixture();empty.blocks=[];const eh=(await render(locale,empty)).html;assert.equal(cards(eh).length,0);assert(!eh.includes('class="bcsse-accessories bcsse-section"'));assert.equal((eh.match(/<h1\b/g)||[]).length,1);
  const blank=fixture();blank.blocks=[{id:'missing',settings:{kind:'seat',product:null}}];assert.equal(cards((await render(locale,blank)).html).length,0);
  checks.push(locale+': unavailable current/available alternative, missing initial/alternative photo, empty/blank blocks render safely');
 }
 console.log(JSON.stringify({status:'passed',checks,limits:'LiquidJS adapters cover markup/data contracts. Shopify native form output, browser event handling, real colour photos, cart network/section rendering, responsive layout and persistence need independent JS/browser QA.'},null,2));
}
main().catch(error=>{console.error(error);process.exitCode=1;});
