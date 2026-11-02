import assert from 'node:assert/strict';
import fs from 'node:fs';
import ts from 'typescript';
import {createRequire} from 'node:module';
import React from 'react';
import {renderToStaticMarkup} from 'react-dom/server';
const require=createRequire(import.meta.url),module={exports:{}};
const source=fs.readFileSync('components/lagoo-fast-review.tsx','utf8');
const compiled=ts.transpileModule(source,{compilerOptions:{jsx:ts.JsxEmit.ReactJSX,module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
new Function('require','module','exports',compiled)(require,module,module.exports);
const Component=module.exports.default;
const products=JSON.parse(fs.readFileSync('data/lagoo-catalogue.json')).products;
let passed=0;
function test(name,fn){fn();console.log('PASS',name);passed++}
const product=products.find(p=>p.quality.colour==='Chroom'&&p.images.length>1);
const noop=()=>{};
const props={product,image:product.images[0],candidates:product.images,detailsReady:true,position:0,total:1745,reviewed:0,available:1745,loading:false,ready:true,busy:false,blocked:false,imageReady:true,imageError:false,error:'',message:'',theme:'light',canUndo:false,done:false,...Object.fromEntries(['Judge','Choose','ImageLoad','ImageError','Zoom','Theme','Advanced','Undo','Skip','Continue','Retry','Connect'].map(x=>['on'+x,noop]))};
const render=overrides=>renderToStaticMarkup(React.createElement(Component,{...props,...overrides}));
function enabledYes(html){return !html.match(/<button class="decision yes"([^>]*)>/)[1].includes('disabled')}
test('Exact source colour in title is visible as the primary heading for all photographed Lagoo variants with a colour',()=>{for(const p of products.filter(p=>p.images.length&&p.quality.colour)){assert(p.title.includes(p.quality.colour));const html=render({product:p,image:p.images[0],candidates:p.images});assert(html.includes('<h1>'+p.quality.colour+'</h1>'))}});
test('Focused view has one large picture and direct decisions, without full QC menus or PDF data',()=>{const html=render();assert(html.includes('Kleur volgens titel'));assert(html.includes('Andere foto'));assert(html.includes('Uitgebreid'));assert(enabledYes(html));assert(!html.includes('Specificaties uit de bron'));assert(!html.includes('<select'));assert(!html.includes('Te controleren:'));assert(!html.includes('Alle merken'))});
test('Correct cannot be submitted before photo and candidate mapping load, during save, without login or after a failure',()=>{for(const state of [{imageReady:false},{detailsReady:false},{imageError:true},{busy:true},{blocked:true},{ready:false}])assert(!enabledYes(render(state)))});
test('Different candidate is the actually displayed full-size image',()=>{const im=product.images[1];const html=render({image:im});assert(html.includes('src="'+im.url.replaceAll('&','&amp;')+'"'));assert(html.includes('Foto 2 van '+product.images.length))});
test('Missing colour stays explicit, never substituted with SKU or another colour',()=>{const p={...product,quality:{...product.quality,colour:''}};assert(render({product:p}).includes('<h1>Geen kleur opgegeven</h1>'))});
test('Connection failure shows sign-in and retry, and pending saves keep decisions locked',()=>{const html=render({ready:false,error:'Meld je aan',blocked:true});assert(html.includes('Aanmelden'));assert(html.includes('Opnieuw proberen'));assert(!enabledYes(html))});
console.log(JSON.stringify({passed,failed:0}));
