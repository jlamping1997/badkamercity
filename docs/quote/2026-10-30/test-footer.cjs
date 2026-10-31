const fs=require('node:fs'),assert=require('node:assert/strict'),{Liquid}=require('liquidjs');
const src=fs.readFileSync('snippets/bc-footer-quote.liquid','utf8').replace(/{% doc %}[\s\S]*?{% enddoc %}/,'');
const e=new Liquid();e.registerFilter('t',k=>({'bc_quote.eyebrow':'Laagsteprijsgarantie','bc_quote.header_button':'Offerte uploaden'}[k]));
(async()=>{const cases=[
 [{quote_link_preview:true},'main',{},false,null],
 [{quote_link_preview:true},'unpublished',{},true,'/pages/contact?view=offerte-vergelijken'],
 [{quote_link_enabled:true},'main',{},false,null],
 [{quote_link_enabled:true},'main',{'offerte-vergelijken':{url:'/pages/offerte-vergelijken'}},true,'/pages/offerte-vergelijken'],
 [{},'unpublished',{},false,null]
];for(const [settings,role,pages,visible,url] of cases){const html=await e.parseAndRender(src,{section:{settings},theme:{role},pages});assert.equal(html.includes('data-bc-footer-quote'),visible);if(visible){assert.ok(html.includes(url));assert.ok(html.includes('Laagsteprijsgarantie – Offerte uploaden'));}}console.log('5 footer activation/routing cases passed')})().catch(e=>{console.error(e);process.exit(1)});
