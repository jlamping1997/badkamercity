import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {Window} from 'happy-dom';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../..');
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const source = read('snippets/bc-porcelanosa-buybox.liquid');
const locale = JSON.parse(read('locales/nl.json').replace(/^\s*\/\*[\s\S]*?\*\//, ''));
const input = source.match(/<input[^>]*data-tile-area[^>]*>/)[0];
const waste = source.match(/<select[^>]*data-tile-waste[^>]*>[\s\S]*?<\/select>/)[0];
const dialog = source.match(/<dialog[\s\S]*?<\/dialog>/)[0];
const coreName = 'scripts/component-audit/fixtures/fix01-baseline/assets/bc-porcelanosa-core.js';
const core = read(coreName);
assert.equal(crypto.createHash('md5').update(core).digest('hex'), '6d80b1b7c69ba340312d2b563bed9d96');
const windows = [];
const checks = [];
const markup = text => text.replace(/{{\s*'([^']+)'\s*\|\s*t(?:\s*\|\s*escape)?\s*}}/g, (_, key) => key.split('.').reduce((o, k) => o?.[k], locale) || key).replace(/{{\s*section.id\s*}}/g, 'fixture');

function fixture(saved, unavailable = false) {
  const w = new Window({url: 'https://fixture.invalid/products/tile'});
  windows.push(w);
  w.eval(core);
  w.eval(read('assets/bc-porcelanosa-buybox.js'));
  if (saved) w.sessionStorage.setItem('bc-tile-area:fixture', JSON.stringify(saved));
  const product = w.document.createElement('product-info');
  product.innerHTML = '<form id="fixture-form"><button type="submit">Bestellen</button></form>';
  product.querySelector('button').disabled = unavailable;
  const box = w.document.createElement('bc-porcelanosa-buybox');
  Object.assign(box.dataset, {form: 'fixture-form', group: 'fixture', currency: 'EUR', boxUnits: '14300', priceCents: '14293', unitPriceCents: '9995', areaError: 'Vul een oppervlakte in', boxError: 'Vul een heel aantal dozen in'});
  box.innerHTML = markup(input + waste + dialog) + '<div data-tile-choices></div><div data-tile-calculator hidden></div><div data-tile-manual></div><button type="button" data-tile-application-help aria-expanded="false">i</button><input data-tile-quantity value="1"><input data-tile-box-input value=""><button data-tile-box-step="-1"></button><button data-tile-box-step="1"></button><span data-tile-error></span><span data-tile-boxes></span><span data-tile-boxes-label></span><span data-tile-box-one>doos</span><span data-tile-box-many>dozen</span><span data-tile-required></span><span data-tile-supplied></span><span data-tile-total></span><span data-tile-unit-price></span><span data-tile-box-price></span><span data-tile-box-area></span><span data-tile-delivery-text></span><div data-tile-delivery></div><div data-tile-contact></div><input data-tile-property>';
  product.append(box);
  w.document.body.append(product);
  return {w, box, change(selector, value) {const el = box.querySelector(selector); el.value = value; el.dispatchEvent(new w.Event('input', {bubbles: true}));}};
}

async function check(name, run) {await run(); checks.push(name);}
await check('Fresh product starts at 1 m², 10% waste and correct whole-box total', () => {
  const {box} = fixture();
  assert.equal(box.area.value, '1');
  assert.equal(box.waste.value, '10');
  assert.equal(box.quantity.value, '1');
  assert.equal(box.querySelector('[data-tile-required]').textContent, '1,1 m²');
  assert.equal(box.querySelector('[data-tile-supplied]').textContent, '1,43 m²');
  assert.match(box.querySelector('[data-tile-total]').textContent, /142,93/);
  assert.equal(box.submit.disabled, false);
});
await check('Zero edited area clears the previous total and blocks ordering', () => {
  const f = fixture(); f.change('[data-tile-area]', '0');
  assert.equal(f.box.submit.disabled, true);
  assert.equal(f.box.querySelector('[data-tile-total]').textContent, '—');
  assert.equal(f.box.querySelector('[data-tile-error]').hidden, false);
});
await check('Clearing the default is an invalid explicit edit', () => {
  const f = fixture(); f.change('[data-tile-area]', '');
  assert.equal(f.box.submit.disabled, true);
  assert.equal(f.box.area.getAttribute('aria-invalid'), 'true');
});
await check('Ten square metres still rounds 11 required m² to eight boxes', () => {
  const f = fixture(); f.change('[data-tile-area]', '10');
  assert.equal(f.box.quantity.value, '8');
  assert.equal(f.box.querySelector('[data-tile-supplied]').textContent, '11,44 m²');
});
await check('Manual whole boxes preserve their quantity without double waste', () => {
  const f = fixture(); f.change('[data-tile-box-input]', '3');
  assert.equal(f.box.quantity.value, '3'); assert.equal(f.box.waste.value, '0');
  assert.equal(f.box.area.value, '4,29');
});
await check('A saved explicit area and waste take precedence over the fresh default', () => {
  const {box} = fixture({area: '3', waste: 5, mode: 'area'});
  assert.equal(box.area.value, '3'); assert.equal(box.waste.value, '5');
});
await check('A saved manual box quantity is restored', () => {
  const {box} = fixture({area: '2,86', waste: 0, mode: 'boxes', boxes: 2});
  assert.equal(box.quantity.value, '2'); assert.equal(box.waste.value, '0');
});
await check('Invalid saved zero area falls back to the fresh 1 m² default', () => {
  assert.equal(fixture({area: '0', waste: 0}).box.area.value, '1');
});
await check('A product that cannot be ordered remains disabled at the valid default', () => {
  assert.equal(fixture(undefined, true).box.submit.disabled, true);
});
await check('Info button opens the dialog, sets expanded and restores body scrolling', async () => {
  const {w, box} = fixture(); w.document.body.style.overflow = 'scroll';
  box.applicationHelp.click();
  assert.equal(box.applicationDialog.open, true);
  assert.equal(box.applicationHelp.getAttribute('aria-expanded'), 'true');
  assert.equal(w.document.body.style.overflow, 'hidden');
  box.querySelector('[data-tile-application-close]').click();
  await w.happyDOM.waitUntilComplete();
  assert.equal(box.applicationDialog.open, false);
  assert.equal(box.applicationHelp.getAttribute('aria-expanded'), 'false');
  assert.equal(w.document.body.style.overflow, 'scroll');
});
for (const w of windows) {await w.happyDOM.abort(); w.close();}
const files = ['assets/bc-porcelanosa-buybox.js', 'snippets/bc-porcelanosa-buybox.liquid', 'locales/nl.json', coreName];
const result = {status: 'PASS', method: 'Real buybox lifecycle and calculation core in happy-dom; synthetic product, session storage and markup fragments. No layout, native Escape/focus, server, cart or form claim.', checks, sources: files.map(name => ({path: name, sha256: crypto.createHash('sha256').update(read(name)).digest('hex')}))};
const output = process.argv[2];
if (output) {fs.mkdirSync(path.dirname(output), {recursive: true}); fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');}
console.log(JSON.stringify({status: result.status, checks: checks.length}));
