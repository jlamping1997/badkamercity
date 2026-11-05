import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {Liquid} from 'liquidjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const theme=path.join(root,'shopify/current');
const text=fs.readFileSync(path.join(theme,'locales/nl.json'),'utf8');
const locale=JSON.parse(text.slice(text.indexOf('{')));
const engine=new Liquid({root:path.join(theme,'snippets'),extname:'.liquid'});
engine.registerTag('doc',{parse(_token,tokens){while(tokens.length){if(tokens.shift().name==='enddoc')break;}},render(){return '';}});
engine.registerTag('form',{parse(_token,tokens){while(tokens.length){if(tokens.shift().name==='endform')break;}},render(){return '';}});
engine.registerFilter('t',(key,...pairs)=>{
  let value=String(key).split('.').reduce((obj,part)=>obj?.[part],locale)||key;
  for(const pair of pairs)if(Array.isArray(pair))value=value.replace(new RegExp('{{\\s*'+pair[0]+'\\s*}}','g'),String(pair[1]));
  return value;
});
engine.registerFilter('money',cents=>'€'+(Number(cents)/100).toFixed(2).replace('.',','));
engine.registerFilter('money_with_currency',cents=>'€'+(Number(cents)/100).toFixed(2).replace('.',',')+' EUR');
engine.registerFilter('asset_url',value=>value);
engine.registerFilter('stylesheet_tag',()=> '');
engine.registerFilter('inline_asset_content',()=> '');
engine.registerFilter('placeholder_svg_tag',()=> '<svg></svg>');
engine.registerFilter('image_url',value=>value?.src||'https://cdn.shopify.com/fixture.jpg');
function product({vendor='Cottoceramix',lead,mode='m2'}={}){
  const tile=mode==='unit'?{order_mode:'unit',sale_unit:'pak',unit_count:10}:{m2_per_box:1.36};
  if(lead!==undefined)tile.lead_time=lead;
  tile.order_type=lead==='Op voorraad bij leverancier'?'Voorraadartikel':'Bestelartikel';
  const variant={id:45,sku:mode==='unit'?'WY1304':'AH6571',price:9950,available:true,quantity_rule:{min:1,increment:1}};
  return{id:123,vendor,title:'Cottoceramix Fixture',handle:'fixture',url:'/products/fixture',type:'Tegel',price:9950,price_min:9950,compare_at_price:0,price_varies:false,available:true,variants_count:1,variants:[variant],selected_or_first_available_variant:variant,media:[],metafields:{custom:{bron_toelichtingen_json:{value:{tiles:tile}}}}};
}
async function renderedCard(name,cardProduct){
  return engine.renderFile(name,{card_product:cardProduct,show_card_delivery:true,skip_styles:true,section_id:'fixture',settings:{card_style:'standard'},shop:{taxes_included:true}});
}
const delivery=html=>html.match(/<p class="bc-card-delivery">([\s\S]*?)<\/p>/)?.[1];
const checks=[];
async function check(name,run){await run();checks.push(name);}
await check('Known m2 supplier stock text reaches both real native card callers',async()=>{
  for(const name of ['card-product','bc-card-product-search'])assert.equal(delivery(await renderedCard(name,product({lead:'Op voorraad bij leverancier'}))),'Op voorraad bij leverancier');
});
await check('Unit pack source lead and neutral on-request text both reach native and search cards',async()=>{
  for(const name of ['card-product','bc-card-product-search'])for(const lead of ['Levertijd ongeveer 12 werkdag(en)','Levertijd op aanvraag'])assert.equal(delivery(await renderedCard(name,product({mode:'unit',lead}))),lead);
});
await check('Other brands and missing source values preserve the existing neutral text and class',async()=>{
  for(const prod of [product(),product({lead:'   '}),product({vendor:'Other',lead:'Op voorraad bij leverancier'})]){
    const html=(await engine.renderFile('bc-card-delivery',{product:prod})).trim();
    assert.equal(html,'<p class="bc-card-delivery">Levertijd op aanvraag</p>');
    for(const name of ['card-product','bc-card-product-search'])assert.equal(delivery(await renderedCard(name,prod)),'Levertijd op aanvraag');
  }
});
await check('Canonical lead is escaped and no stock style or fabricated delivery promise is added',async()=>{
  const html=await engine.renderFile('bc-card-delivery',{product:product({lead:'<b>Verwacht & bron</b>'})});
  assert.equal(delivery(html),'&lt;b&gt;Verwacht &amp; bron&lt;/b&gt;');assert.doesNotMatch(html,/bc-card-delivery--stock|8 - 9 weken/);
});
console.log(JSON.stringify({status:'PASS',checks,scope:'Actual shared helper plus complete native/search card snippet rendering. Product-form body omitted because quick-add is not enabled in these delivery fixtures; no browser/index claim.'},null,2));
