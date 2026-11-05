'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { Liquid } = require('liquidjs');
const base = path.resolve(__dirname, '../shopify/current');
const adapt = source => source.replaceAll(String.raw`'\u003c'`, String.raw`'\\u003c'`)
  .replace(/{%-?\s*doc\s*-?%}[\s\S]*?{%-?\s*enddoc\s*-?%}/g, '')
  .replace(/{%-?\s*schema\s*-?%}[\s\S]*?{%-?\s*endschema\s*-?%}/g, '');
function engine(locale = 'nl') {
  const strings = JSON.parse(fs.readFileSync(path.join(base, 'locales', locale === 'nl' ? 'nl.json' : 'en.default.json'), 'utf8').replace(/^\s*\/\*[\s\S]*?\*\/\s*/, ''));
  const files = new Map([
    ['/snippets/bc-card-tile-price.liquid', adapt(fs.readFileSync(path.join(base, 'snippets/bc-card-tile-price.liquid'), 'utf8'))],
    ['/snippets/bc-hotbath-menu-route.liquid', '']
  ]);
  const read = file => { assert(files.has(file), 'known snippet: ' + file); return files.get(file); };
  const liquid = new Liquid({ root: '/snippets', extname: '.liquid', strictFilters: true,
    fs: { sep: '/', resolve: (dir, file, ext) => path.posix.resolve(dir, file.endsWith(ext) ? file : file + ext), dirname: path.posix.dirname,
      exists: async file => files.has(file), existsSync: file => files.has(file), readFile: async file => read(file), readFileSync: read }
  });
  liquid.registerFilter('json', value => JSON.stringify(value ?? null));
  liquid.registerFilter('t', (key, ...pairs) => {
    let value = String(key).split('.').reduce((a, k) => a?.[k], strings);
    assert.equal(typeof value, 'string', 'known translation: ' + key);
    for (const [key, replacement] of pairs) value = value.replaceAll('{{ ' + key + ' }}', replacement).replaceAll('{{' + key + '}}', replacement);
    return value;
  });
  liquid.registerFilter('money', cents => new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' }).format(Number(cents) / 100));
  liquid.registerFilter('image_url', value => value?.src || '');
  liquid.registerFilter('asset_url', value => '/assets/' + value);
  liquid.registerFilter('stylesheet_tag', value => '<link href="' + value + '">');
  return liquid;
}
function product(overrides = {}) {
  const selected = { id: 456, sku: 'TEST-EXPENSIVE', price: 20000, available: true, quantity_rule: { min: 1, increment: 1 } };
  return { id: 123, title: 'Test product', handle: 'test-product', vendor: 'Test',
    metafields: { custom: {}, bc_filters: {}, specs: {} }, images: [], featured_image: null,
    selected_or_first_available_variant: selected, variants: [selected, { id: 457, sku: 'TEST-CHEAP', price: 7800 }],
    price_min: 7800, price_varies: true, requires_selling_plan: false, ...overrides };
}
async function data(p) {
  const source = adapt(fs.readFileSync(path.join(base, 'sections/bc-card-data.liquid'), 'utf8'));
  const html = await engine().parseAndRender(source, { product: p });
  const match = html.match(/<script\b[^>]*data-bc-card-data[^>]*>([\s\S]*?)<\/script>/);
  assert(match, 'one card JSON payload');
  return { value: JSON.parse(match[1]), raw: match[1] };
}
test('Card JSON exposes Shopify minimum price independently of selected variant', async () => {
  const { value } = await data(product());
  assert.equal(value.price_cents, 7800);
  assert.equal(value.price_varies, true);
  assert.equal(value.variant_id, 456);
  assert.equal(value.can_add, false);
});
test('Single-variant and equal-price products keep their exact price without a varying-price flag', async () => {
  const p = product({ price_min: 20000, price_varies: false });
  for (const count of [1, 2]) {
    p.variants = Array.from({ length: count }, (_, i) => ({ ...p.selected_or_first_available_variant, id: 456 + i }));
    const { value } = await data(p);
    assert.equal(value.price_cents, 20000);
    assert.equal(value.price_varies, false);
    assert.equal(value.variant_id, 456);
    assert.equal(value.can_add, count === 1);
  }
});
test('A known zero minimum price survives the data contract', async () => {
  const { value } = await data(product({ price_min: 0 }));
  assert.equal(value.price_cents, 0);
  assert.equal(value.price_varies, true);
});
test('Card title JSON still escapes closing script markup', async () => {
  const title = 'Test </script><script>alert(1)</script>';
  const result = await data(product({ title }));
  assert.equal(result.value.title, title);
  assert(!result.raw.includes('<'));
});
test('Single-price tile box and m² amounts remain unchanged', async () => {
  const p = product({ price_min: 9929, price_varies: false });
  p.selected_or_first_available_variant = { ...p.selected_or_first_available_variant, price: 9929, unit_price: 6895 };
  p.variants = [p.selected_or_first_available_variant];
  p.metafields.custom.bron_toelichtingen_json = { value: { tiles: { m2_per_box: 1.44, price_per_m2: { amount: 68.95 } } } };
  const { value } = await data(p);
  assert.equal(value.price_cents, 9929);
  assert.deepEqual(value.tile_price, { box_area: 1.44, unit_price_cents: 6895 });
});
for (const [locale, expected] of [['nl', 'Vanaf __BC_PRICE__'], ['en', 'From __BC_PRICE__']]) {
  test(`External card minimum-price template uses the existing ${locale} translation`, async () => {
    const source = adapt(fs.readFileSync(path.join(base, 'snippets/bc-external-filters.liquid'), 'utf8'));
    const html = await engine(locale).parseAndRender(source, { shop: { name: 'Test', taxes_included: true }, search: { terms: 'test' }, collection: { all_products_count: 1 }, collection_handle: 'test', section_id: 'fixture' });
    assert.equal(html.match(/data-label-price-from="([^"]*)"/)[1], expected);
  });
}
