const fs=require('node:fs'),assert=require('node:assert/strict'),{Liquid}=require('liquidjs');
const s=fs.readFileSync('sections/header.liquid','utf8').split('-%}')[0]+'-%}{{ quote_header_visible }}|{{ quote_header_url }}';
(async()=>{const e=new Liquid();const cases=[
 [{quote_cta_preview:true},'main',{},'false|'],
 [{quote_cta_preview:true},'unpublished',{},'true|/pages/contact?view=offerte-vergelijken'],
 [{quote_cta_enabled:true},'main',{},'false|'],
 [{quote_cta_enabled:true},'main',{'offerte-vergelijken':{url:'/pages/offerte-vergelijken'}},'true|/pages/offerte-vergelijken'],
 [{},'unpublished',{},'false|']
];for(const [settings,role,pages,out] of cases)assert.equal((await e.parseAndRender(s,{section:{settings},theme:{role},pages})).trim(),out);console.log('5 header visibility/routing cases passed')})().catch(e=>{console.error(e);process.exit(1)});
