const { Liquid } = require('liquidjs');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const code = fs.readFileSync(path.join(__dirname, '../snippets/bc-card-specs.liquid'), 'utf8')
  .replace(/\{% doc %\}[\s\S]*?\{% enddoc %\}/, '');
const engine = new Liquid();
engine.registerFilter('t', (key) => key);
function product(sku, manifestSku, values) {
  return { type: 'Opzetfontein', variants: [{ sku }], metafields: { bc_data: { filter_manifest: {
    value: { format: 'verified-product-filters-v1', sku: manifestSku, values }
  } } } };
}
(async () => {
  let html = await engine.parseAndRender(code, { product: product('A1', 'A1', { materiaal: 'Quartz', kleur: 'Zilver' }) });
  assert(html.includes('Quartz') && html.includes('Zilver'));
  assert.equal((html.match(/<dd>/g) || []).length, 2);
  html = await engine.parseAndRender(code, { product: product('A1', 'WRONG', { materiaal: 'Onjuiste waarde', kleur: 'Rood' }) });
  assert(!html.includes('Onjuiste waarde') && !html.includes('Rood'));
  assert(html.includes('Opzetfontein') && html.includes('A1'));
  html = await engine.parseAndRender(code, { product: product('A1', 'A1', { materiaal: '<script>unsafe</script>', kleur: 'Zwart' }) });
  assert(!html.includes('<script>'));
  assert(html.includes('&lt;script&gt;'));
  html = await engine.parseAndRender(code, { product: { type: '', variants: [{ sku: '' }], metafields: {} } });
  assert(!html.includes('<dl'));
  console.log('4 card attribute render checks passed.');
})().catch((error) => { console.error(error); process.exitCode = 1; });
