import fs from 'node:fs';
import assert from 'node:assert/strict';
import { Window } from 'happy-dom';

const source = fs.readFileSync(new URL('theme/assets/bc-product-switcher.js', import.meta.url), 'utf8')
  .replace('function init(root = document)', 'window.TestSwitcher = BCProductSwitcherV2; function init(root = document)');
const data = JSON.parse(fs.readFileSync(new URL('fixture.json', import.meta.url)));
const group = data.groups.find(g => g.id === 'hotbath-book-cb105ext-keuzes');
const codes = ['cr','gn','bb','ab','wh','ai','bbp','bcp','pbp','mbp','bgp','tb','ix'];
const storageKey = 'bc:product-switcher:expanded-colors:v1';
const results = [];

function setup({ groupData=group, color='Verouderd messing', mobile=true, hotbath=true, token, blockedStorage=false }={}) {
  const product = groupData.products.find(p => p.options.kleur === color) || groupData.products[0];
  const window = new Window({ url: 'https://badkamercity.nl'+product.url });
  window.console.info = () => {};
  const media = {matches:mobile,addEventListener(){},removeEventListener(){}};
  window.matchMedia = () => media;
  if(token) window.sessionStorage.setItem(storageKey,JSON.stringify(token));
  if(blockedStorage) Object.defineProperty(window,'sessionStorage',{get(){throw new Error('blocked');}});
  window.eval(source);
  const root = window.document.createElement('div');
  Object.assign(root.dataset, {
    bcProductSwitcherV2:'', hotbathMobileA:String(hotbath), switchGroup:groupData.id,
    productHandle:product.handle, productUrl:product.url, sectionId:'round-test',
    labelAllColors:'Bekijk alle __COUNT__ kleuren', labelLessColors:'Minder kleuren',
    hotbathSwatchUrls:JSON.stringify(Object.fromEntries(codes.map(c=>[c,`https://badkamercity.nl/swatch-${c}.jpg`])))
  });
  window.document.body.append(root);
  const instance = new window.TestSwitcher(root,{groups:[groupData]});
  return {window,root,instance,media,product};
}
const visible = root => [...root.querySelectorAll('.bc-hotbath-swatch')].filter(b=>!b.hidden);
const toggle = root => root.querySelector('.bc-hotbath-colors__toggle');
const label = root => root.querySelector('.bc-hotbath-colors__toggle-label')?.textContent;

let x=setup();
assert.equal(visible(x.root).length,4);
assert.equal(x.root.querySelectorAll('.bc-hotbath-swatch').length,10);
assert.equal(label(x.root),'Bekijk alle 10 kleuren');
assert.equal(x.root.querySelector('.bc-hotbath-colors__count').textContent,'+6');
assert.equal(x.root.querySelector('.is-active .bc-hotbath-swatch__label').textContent,'Verouderd messing');
assert.equal(x.root.querySelectorAll('.bc-hotbath-colors__expanded').length,0);
results.push('10 kleuren: vier zichtbaar, geselecteerd, namen, totaal en +6 correct');
toggle(x.root).click();
assert.equal(visible(x.root).length,10);
assert.equal(toggle(x.root).getAttribute('aria-expanded'),'true');
assert.equal(label(x.root),'Minder kleuren');
assert.equal(x.root.querySelector('.bc-hotbath-colors__count').hidden,true);
toggle(x.root).click();
assert.equal(visible(x.root).length,4);
results.push('Inline uit-/inklappen en toegankelijke knopstatus');
x=setup({color:'Gepolijst zwart PVD'});
assert.equal(visible(x.root).length,4);
assert(visible(x.root).some(b=>b.dataset.switchValue==='Gepolijst zwart PVD'));
results.push('Geselecteerde kleur buiten eerste vier blijft zichtbaar');
for(const count of [1,3,4,5,7,9]) {
  const smaller=structuredClone(group);
  smaller.id='fixture-'+count;
  const colorMenu=smaller.menus.find(m=>m.key==='kleur');
  colorMenu.values=colorMenu.values.slice(0,count);
  smaller.products=smaller.products.filter(p=>colorMenu.values.includes(p.options.kleur));
  const a=setup({groupData:smaller});
  assert.equal(visible(a.root).length,count===1&&colorMenu.hide_if_single_value?0:Math.min(count,4));
  assert.equal(Boolean(toggle(a.root)),count>4);
  if(count>4){toggle(a.root).click();assert.equal(visible(a.root).length,count);}
}
results.push('1, 3, 4, 5, 7 en 9 kleuren zonder lege knoppen of duplicaten');
x=setup();toggle(x.root).click();
const next=group.products.find(p=>p.options.kleur==='Geborsteld nikkel'&&p.options.uitlooplengte===x.product.options.uitlooplengte);
x.instance.updateSelection('kleur','Geborsteld nikkel');
const token=JSON.parse(x.window.sessionStorage.getItem(storageKey));
assert.equal(token.target,next.url);assert.deepEqual(token.keys,['kleur']);
const destination=setup({color:'Geborsteld nikkel',token});
assert.equal(visible(destination.root).length,10);
assert.equal(label(destination.root),'Minder kleuren');
assert.equal(destination.root.querySelector('.is-active').dataset.switchValue,'Geborsteld nikkel');
results.push('Kleurwissel navigeert naar exact product en herstelt uitgeklapte staat');
for(const badToken of [{...token,group:'other'}, {...token,savedAt:Date.now()-60000}, {...token,target:'/products/other'}]) {
  assert.equal(visible(setup({token:badToken}).root).length,4);
}
results.push('Verlopen of niet-passende bewaarde keuzes worden genegeerd');
for (const mobile of [true,false]) {
  const v=setup({mobile});
  assert.equal(visible(v.root).length,4);
  toggle(v.root).click();
  assert.equal(visible(v.root).length,10);
  assert.equal(v.root.querySelector('select'),null);
  v.media.matches=!mobile;
  v.window.dispatchEvent(new v.window.Event('resize'));
  assert.equal(visible(v.root).length,10);
  assert.equal(toggle(v.root).getAttribute('aria-expanded'),'true');
}
assert(setup({hotbath:false,mobile:false}).root.querySelector('select'));
results.push('Desktop en mobiel delen ronde kleuren en uitgeklapte staat; andere merken behouden dropdowns');
x=setup();
x.instance.products=x.instance.products.filter(p=>!(p.options.kleur==='Chroom'&&p.options.uitlooplengte===x.instance.state.uitlooplengte));
x.instance.syncControls();
assert(x.root.querySelector('[data-switch-value="Chroom"]').disabled);
results.push('Onmogelijke combinatie blijft uitgeschakeld');
x=setup({blockedStorage:true});toggle(x.root).click();assert.equal(visible(x.root).length,10);
results.push('Kleurkeuze blijft werken bij geblokkeerde sessieopslag');
x=setup();const image=x.root.querySelector('.bc-hotbath-swatch img');
image.dispatchEvent(new x.window.Event('error'));
assert(!image.isConnected);assert(x.root.querySelector('.bc-hotbath-swatch__label').textContent);
results.push('Afbeeldingsfout behoudt leesbare kleurkeuze');
x=setup();
x.root.dataset.bcPreservePosition='true';
x.root.dataset.switcherDataUrl='/hotbath-data?v=1';
toggle(x.root).click();
x.instance.updateSelection('kleur','Geborsteld nikkel');
const handoff=x.window.sessionStorage.getItem('bc:product-switcher:position:v1');
assert(JSON.parse(handoff).handoff.group.id===group.id);
const nextWindow=new Window({url:'https://badkamercity.nl'+next.url});
nextWindow.console.info=()=>{};
nextWindow.matchMedia=()=>({matches:true,addEventListener(){},removeEventListener(){}});
let fetches=0;
nextWindow.fetch=async()=>{fetches++;return {ok:true,json:async()=>({groups:[group]})};};
nextWindow.sessionStorage.setItem('bc:product-switcher:position:v1',handoff);
nextWindow.sessionStorage.setItem(storageKey,x.window.sessionStorage.getItem(storageKey));
const nextRoot=nextWindow.document.createElement('div');
Object.assign(nextRoot.dataset,x.root.dataset,{productHandle:next.handle,productUrl:next.url});
delete nextRoot.dataset.bcProductSwitcherV2Initialized;
nextRoot.setAttribute('data-bc-product-switcher-v2','');
nextWindow.document.body.append(nextRoot);
nextWindow.eval(source);
nextWindow.document.dispatchEvent(new nextWindow.Event('DOMContentLoaded'));
assert.equal(nextRoot.dataset.bcProductSwitcherV2Initialized,'true');
assert.equal(fetches,0);
assert.equal(visible(nextRoot).length,10);
assert.equal(nextRoot.querySelector('.is-active').dataset.switchValue,'Geborsteld nikkel');
assert.equal(label(nextRoot),'Minder kleuren');
results.push('Volledige init gebruikt handoff direct zonder fetch; juiste kleur en uitgeklapt paneel blijven behouden');
console.log(JSON.stringify({status:'PASS',checks:results},null,2));
fs.writeFileSync(new URL('switcher-test-results.json',import.meta.url),JSON.stringify({status:'PASS',checks:results},null,2));
process.exit(0);
