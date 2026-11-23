import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {Liquid} from 'liquidjs';
import {Window} from 'happy-dom';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const theme=path.join(root,'shopify/current');
const checks=[];
function engine(language='nl'){
  const localeText=fs.readFileSync(path.join(theme,'locales',language==='nl'?'nl.json':'en.default.json'),'utf8');
  const locale=JSON.parse(localeText.slice(localeText.indexOf('{')));
  const liquid=new Liquid({root:path.join(theme,'snippets'),extname:'.liquid'});
  liquid.registerTag('doc',{parse(_token,tokens){while(tokens.length){if(tokens.shift().name==='enddoc')break;}},render(){return '';}});
  liquid.registerFilter('t',(key,...pairs)=>{
    const params=Object.fromEntries(pairs.filter(Array.isArray));
    let value=String(key).split('.').reduce((obj,part)=>obj?.[part],locale);
    if(value&&typeof value==='object')value=value[Number(params.count)===1?'one':'other'];
    return String(value??key).replace(/{{\s*(\w+)\s*}}/g,(_match,name)=>String(params[name]??''));
  });
  for(const filter of ['asset_url','stylesheet_tag','inline_asset_content'])liquid.registerFilter(filter,()=> '');
  return liquid;
}
function fixture({handle='cottoceramix',search=false,param='filter.v.availability',labels=['Op voorraad','Niet op voorraad'],values=['1','0'],bothActive=false}={}){
  const entries=values.map((value,index)=>({value,label:labels[index],count:index===0?3159:0,active:index===0||bothActive,param_name:param,url_to_remove:'/collections/cottoceramix?remove='+value}));
  const filter={type:'boolean',param_name:param,label:'Beschikbaarheid',values:entries,active_values:entries.filter(v=>v.active),operator:'OR',url_to_remove:'/collections/cottoceramix'};
  const results={handle:search?undefined:handle,filters:[filter],url:'/collections/cottoceramix',sort_options:[],products_count:3159,all_products_count:3159,terms:search?'tegel':undefined};
  return {collection:handle?{handle}:undefined,results,section:{id:'native-facet-test'},settings:{},enable_filtering:true,enable_sorting:false,filter_type:'vertical',paginate:{},routes:{search_url:'/search'}};
}
async function render(options={},type='vertical',language='nl',snippet='facets'){
  const context=fixture(options);context.filter_type=type;
  const html=await engine(language).renderFile(snippet,context);
  const window=new Window();window.document.body.innerHTML=html;
  return {html,document:window.document};
}
async function check(name,run){await run();checks.push(name);}
for(const type of ['vertical','horizontal','drawer'])await check('Cotto availability labels, screen-reader copy and active chips in '+type,async()=>{
  const {html,document}=await render({bothActive:true},type);
  assert.doesNotMatch(html,/Op voorraad|Niet op voorraad/);
  const labels=[...document.querySelectorAll('.facet-checkbox__text-label')].map(e=>e.textContent.trim());
  assert.deepEqual(labels,type==='drawer'?['Bestelbaar','Niet bestelbaar']:['Bestelbaar','Niet bestelbaar','Bestelbaar','Niet bestelbaar']);
  assert([...document.querySelectorAll('.visually-hidden')].some(e=>e.textContent.trim().startsWith('Bestelbaar (')));
  assert([...document.querySelectorAll('.visually-hidden')].some(e=>e.textContent.trim().startsWith('Niet bestelbaar (')));
  const chips=[...document.querySelectorAll('.active-facets__button-inner')].map(e=>e.textContent);
  assert(chips.some(text=>text.includes('Beschikbaarheid: Bestelbaar')));
  assert(chips.some(text=>text.includes('Beschikbaarheid: Niet bestelbaar')));
});
await check('Separate selected-filter chips use the same scoped labels',async()=>{
  const {html,document}=await render({bothActive:true},'vertical','nl','bc-collection-active-filters');
  assert.doesNotMatch(html,/Op voorraad/);
  assert.deepEqual([...document.querySelectorAll('.bc-selected-filters__pill')].map(e=>e.firstChild.textContent.trim()),['Beschikbaarheid: Bestelbaar','Beschikbaarheid: Niet bestelbaar']);
});
await check('Native values/counts/checked/disabled and remove URLs are unchanged',async()=>{
  const cotto=await render();const other=await render({handle:'other-brand'});
  const inputs=doc=>[...doc.querySelectorAll('input[type="checkbox"]')].map(e=>({name:e.name,value:e.value,checked:e.checked,disabled:e.disabled}));
  const urls=doc=>[...doc.querySelectorAll('facet-remove a')].map(e=>e.getAttribute('href'));
  assert.deepEqual(inputs(cotto.document),inputs(other.document));assert.deepEqual(urls(cotto.document),urls(other.document));
  assert(cotto.document.querySelector('input[value="0"]').disabled);
  assert(cotto.document.querySelector('input[value="1"]').checked);
  assert(cotto.document.querySelector('.facet-checkbox__text').textContent.includes('3159'));
});
await check('Other collections and search preserve original stock wording',async()=>{
  for(const options of [{handle:'other-brand'},{handle:'cottoceramix',search:true},{handle:null,search:true}]){
    const {html}=await render(options);assert.match(html,/Op voorraad/);assert.doesNotMatch(html,/>Bestelbaar</);
    const chip=await render(options,'vertical','nl','bc-collection-active-filters');assert.match(chip.html,/Op voorraad/);
  }
});
await check('Other filter parameters and unknown availability values preserve escaped source labels',async()=>{
  for(const options of [{param:'filter.v.option.color',labels:['Blauw & <bron>','Overig']},{values:['unexpected','0'],labels:['A & <bron>','Niet op voorraad']}]){
    const {html,document}=await render(options);assert.match(html,/&amp; &lt;bron&gt;/);assert.doesNotMatch(html,/&amp;amp;|&amp;lt;/);
    assert(document.querySelector('.facet-checkbox__text-label').textContent.includes('& <bron>'));
  }
});
await check('English and numeric native values retain availability semantics',async()=>{
  const {html}=await render({values:[1,0],bothActive:true},'vertical','en');
  assert.match(html,/Available to order/);assert.match(html,/Not available to order/);assert.doesNotMatch(html,/Op voorraad/);
});
console.log(JSON.stringify({status:'PASS',checks,scope:'Actual native facets and selected-chip Liquid render; desktop/mobile/accessible text and native filter controls. No browser, Shopify write or supplier-stock claim.'},null,2));
