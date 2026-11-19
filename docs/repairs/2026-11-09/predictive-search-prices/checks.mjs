import fs from 'node:fs';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';

const require = createRequire(process.env.BC_TEST_DEPENDENCIES || new URL('package.json', import.meta.url));
const {Liquid} = require('liquidjs');
const theme = new URL('../../../../shopify/current/', import.meta.url);
const current = fs.readFileSync(new URL('sections/predictive-search.liquid', theme), 'utf8');
const original = fs.readFileSync(new URL('rollback/sections/predictive-search.liquid', import.meta.url), 'utf8');
const results = [];
const plain = value => value.replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();
const withoutPrice = html => html.replace(/(<div class="predictive-search__product-price"[^>]*>)[\s\S]*?(<\/div>)/g, '$1__PRICE__$2');

function engine(locale, currency) {
  const lang = locale === 'en' ? 'en.default' : 'nl';
  const dictionary = JSON.parse(fs.readFileSync(new URL('locales/' + lang + '.json', theme), 'utf8').replace(/^\s*\/\*[\s\S]*?\*\/\s*/, ''));
  const liquid = new Liquid({root: new URL('snippets/', theme).pathname, extname: '.liquid', strictFilters: true,
    globals: {shop: {currency}, cart: {currency: {iso_code: currency}}}});
  const format = cents => new Intl.NumberFormat(locale === 'nl' ? 'nl-NL' : 'en-GB', {style: 'currency', currency}).format(Number(cents) / 100);
  liquid.registerFilter('money', format);
  liquid.registerFilter('money_with_currency', cents => format(cents) + ' ' + currency);
  liquid.registerFilter('money_without_trailing_zeros', cents => new Intl.NumberFormat(locale === 'nl' ? 'nl-NL' : 'en-GB', {style: 'currency', currency, minimumFractionDigits: 0, maximumFractionDigits: 2}).format(Number(cents) / 100));
  liquid.registerFilter('inline_asset_content', filename => fs.readFileSync(new URL('assets/' + filename, theme), 'utf8'));
  liquid.registerFilter('image_url', (image, args) => image.src + '?width=' + args[1]);
  liquid.registerFilter('t', (key, ...pairs) => {
    const args = Object.fromEntries(pairs);
    let value = key.split('.').reduce((a, k) => a?.[k], dictionary);
    if (value && typeof value === 'object') value = args.count === 1 ? value.one : value.other;
    assert.equal(typeof value, 'string', 'Known translation: ' + key);
    for (const [name, replacement] of pairs) value = value.replaceAll('{{ ' + name + ' }}', replacement).replaceAll('{{' + name + '}}', replacement);
    return value;
  });
  return liquid;
}

function product({minimum = 14900, selected = minimum, varies = false, title = 'Test product', image = false} = {}) {
  return {price: minimum, price_min: minimum, price_varies: varies,
    selected_or_first_available_variant: {price: selected}, title, vendor: 'Test', url: '/products/test-product',
    featured_media: image ? {src: 'https://example.invalid/product.jpg', alt: 'Test image'} : null};
}
function input(products, withCurrency = false, performed = true) {
  return {predictive_search: {performed, terms: 'test', resources: {products}}, settings: {currency_code_enabled: withCurrency, predictive_search_show_vendor: true}};
}
const priceText = html => plain(html.match(/<div class="predictive-search__product-price"[^>]*>([\s\S]*?)<\/div>/)[1]);

for (const [locale, currency, minimum, selected, varies, withCurrency, expected] of [
  ['nl', 'EUR', 14900, 14900, false, false, '€ 149'],
  ['nl', 'EUR', 14900, 14900, false, true, '€ 149 EUR'],
  ['nl', 'EUR', 9900, 9900, false, false, '€ 99,00'],
  ['nl', 'EUR', 9999, 9999, false, false, '€ 99,99'],
  ['nl', 'EUR', 10000, 10000, false, false, '€ 100'],
  ['nl', 'EUR', 14949, 14949, false, false, '€ 149,49'],
  ['nl', 'EUR', 0, 0, false, false, '€ 0,00'],
  ['nl', 'EUR', 14900, 24999, true, false, 'Vanaf € 149'],
  ['nl', 'EUR', 7800, 17500, true, true, 'Vanaf € 78,00 EUR'],
  ['nl', 'EUR', 14900, 14900, false, false, '€ 149'],
  ['en', 'EUR', 14900, 24999, true, false, 'From €149'],
  ['en', 'GBP', 14900, 14900, false, false, '£149.00'],
  ['nl', 'USD', 14900, 14900, false, false, 'US$ 149,00']
]) {
  const liquid = engine(locale, currency);
  const context = input([product({minimum, selected, varies, image: true})], withCurrency);
  const html = await liquid.parseAndRender(current, context);
  const before = await liquid.parseAndRender(original, context);
  assert.equal(priceText(html), expected);
  assert.equal(withoutPrice(html), withoutPrice(before), 'Only the price text changes; URLs, image, listbox, count and keyboard hooks stay byte-identical');
  if (minimum === 14900 && selected === 24999 && locale === 'nl') assert.equal(priceText(before), '€ 249,99');
  results.push({test: `${locale}-${currency}-${minimum}-${selected}-${varies}-${withCurrency}`, result: 'PASS'});
}

const liquid = engine('nl', 'EUR');
assert.equal((await liquid.parseAndRender(current, input([], false, false))).trim(), '');
results.push({test: 'unperformed-search-emits-no-results', result: 'PASS'});
const empty = await liquid.parseAndRender(current, input([]));
assert(!empty.includes('role="option"'));
assert.equal(empty, await liquid.parseAndRender(original, input([])));
assert(!empty.includes('NaN'));
results.push({test: 'empty-search-keeps-announcement-without-price', result: 'PASS'});
const unsafe = await liquid.parseAndRender(current, input([product({title: '<img src=x onerror=alert(1)> & test'})]));
assert(!unsafe.includes('<img src=x onerror='));
assert(unsafe.includes('&lt;img'));
results.push({test: 'product-title-remains-html-escaped', result: 'PASS'});
const multi = await liquid.parseAndRender(current, input([product({minimum: 14900}), product({minimum: 9900}), product({minimum: 7800, selected: 17500, varies: true})]));
assert.equal((multi.match(/role="option"/g) || []).length, 3);
assert.equal(new Set([...multi.matchAll(/id="(predictive-search-option-product-\d+)"/g)].map(x => x[1])).size, 3);
results.push({test: 'multiple-results-retain-unique-keyboard-option-ids', result: 'PASS'});

const oldDoc = fs.readFileSync(new URL('rollback/snippets/bc-jeeo-colors.liquid', import.meta.url), 'utf8');
const newDoc = fs.readFileSync(new URL('snippets/bc-jeeo-colors.liquid', theme), 'utf8');
assert.equal(oldDoc.split('{% enddoc %}')[1], newDoc.split('{% enddoc %}')[1]);
fs.writeFileSync(new URL('checks.json', import.meta.url), JSON.stringify({status: 'PASS', tests: results.length, results,
  jeeoRuntimeBytesUnchanged: true, scope: 'Actual predictive section and shared money snippet execute in LiquidJS; Shopify money filters are stubbed with Intl. Browser/Shopify preview evidence is separate.'}, null, 2) + '\n');
console.log(results.length + ' predictive price checks PASS; JEE-O runtime unchanged');
