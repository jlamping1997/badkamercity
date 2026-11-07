import fs from 'node:fs';
import assert from 'node:assert/strict';
import { Liquid } from 'liquidjs';

const fixture = JSON.parse(fs.readFileSync(new URL('breadcrumb-fixture.json', import.meta.url)));
const source = fs.readFileSync(new URL('after/snippets/bc-product-breadcrumbs.liquid', import.meta.url), 'utf8')
  .replace(/{% doc %}[\s\S]*?{% enddoc %}/, '')
  .replace("{%- render 'bc-wiesbaden-reviewed-scope', product: product -%}", '{{ test_reviewed_scope }}');
const engine = new Liquid();
engine.registerFilter('t', key => ({'ss.home':'Home','ss.breadcrumb':'Kruimelpad','bc_pilot_category.kranen':'Kranen','bc_pilot_category.wastafelkranen':'Wastafelkranen','bc_pilot_category.opbouw':'Opbouw wastafelkranen'})[key] || key);
const collections = {};
function menuLinks(items) {
  return items.map(item => {
    const handle = item.url.split('/collections/')[1];
    const object = {handle,title:item.title,url:item.url};
    collections[handle] = object;
    return {type:'collection_link',object,links:menuLinks(item.items || [])};
  });
}
const menu = menuLinks(fixture.menu);
for (const item of fixture.product.collections.nodes) collections[item.handle] = {...item,url:'/collections/'+item.handle};
const product = {title:fixture.product.title,collections:fixture.product.collections.nodes};
const root = {product,collections,linklists:{'main-menu':{links:menu}},routes:{root_url:'/',collections_url:'/collections'},test_reviewed_scope:''};
const paths = html => [...html.matchAll(/<a href="([^"]+)"/g)].map(m=>m[1]);
const cases=[];
async function check(name, data, expected) {
  const html=await engine.parseAndRender(source,data);
  assert.deepEqual(paths(html),expected,name);
  assert.equal((html.match(/aria-current="page"/g)||[]).length,1);
  assert(html.includes('class="visually-hidden"'));
  cases.push(name);
}
await check('Actual CB105EXT25AB collection memberships and main navigation',root,['/','/collections/kranen','/collections/toebehoren','/collections/afbouwdelen-voor-kranen']);
await check('Shared generic category avoids a misleading parent',{...root,product:{...product,collections:[collections.toebehoren]}},['/','/collections/toebehoren']);
await check('Product outside navigation falls back to its actual collection',{...root,product:{...product,collections:[collections['kraan-toebehoren']]}},['/','/collections/kraan-toebehoren']);
await check('Uncategorised product has a safe home route',{...root,product:{...product,collections:[]}},['/']);
await check('Existing Wiesbaden pilot path preserved',{...root,test_reviewed_scope:'pilot'},['/','/collections/kranen','/collections/wastafelkranen','/collections/opbouw-wastafelkranen']);
await check('Reviewed path still checks actual membership',{...root,test_reviewed_scope:'reviewed',product:{...product,metafields:{bc_data:{content_review:{value:{category_handles:['toebehoren','unknown','afbouwdelen-voor-kranen']}}}}}},['/','/collections/toebehoren','/collections/afbouwdelen-voor-kranen']);
const result={status:'PASS',cases,renderer:'LiquidJS',scope:'Breadcrumb snippet rendering; the existing Wiesbaden scope dependency is stubbed'};
fs.writeFileSync(new URL('breadcrumb-test-results.json',import.meta.url),JSON.stringify(result,null,2));
console.log(JSON.stringify(result,null,2));
