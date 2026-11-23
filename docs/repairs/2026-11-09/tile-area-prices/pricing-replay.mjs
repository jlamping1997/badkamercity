import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {Window} from 'happy-dom';
import {Liquid} from 'liquidjs';

const theme = new URL('../../../../shopify/current/', import.meta.url);
const moneyJs = fs.readFileSync(new URL('assets/bc-money.js', theme), 'utf8');
const filterJs = fs.readFileSync(new URL('assets/bc-external-filters.js', theme), 'utf8');
const results = [];
const record = (name) => results.push({test: name, result: 'PASS'});
const normalize = value => value.replaceAll('\u00a0', ' ').replaceAll('\u202f', ' ').trim();
const sandbox = {window: {}, Intl};
vm.runInNewContext(moneyJs, sandbox);
const factory = sandbox.window.BCMoney.createFormatter;
for (const locale of ['nl-NL', 'en-GB', 'de-DE']) {
  for (const currency of ['EUR', 'GBP', 'USD', 'JPY']) {
    const regular = new Intl.NumberFormat(locale, {style: 'currency', currency});
    const integer = new Intl.NumberFormat(locale, {style: 'currency', currency, minimumFractionDigits: 0, maximumFractionDigits: 0});
    for (const value of [0, -149, 99, 99.49, 99.99, 100, 100.49, 100.50, 149, 149.49, 149.50, 1147, 9999.99, 10000]) {
      const expected = currency === 'EUR' && value >= 100 && Number.isInteger(value) ? integer : regular;
      assert.equal(factory(locale, currency).format(value), expected.format(value));
    }
    record(`real-js-formatter-${locale}-${currency}-14-boundaries`);
  }
}

const liquid = new Liquid({root: new URL('snippets/', theme).pathname, extname: '.liquid', strictFilters: true,
  globals: {shop: {currency: 'EUR'}, cart: {currency: {iso_code: 'EUR'}}, settings: {currency_code_enabled: false}}
});
liquid.registerFilter('money', cents => new Intl.NumberFormat('nl-NL', {style: 'currency', currency: 'EUR'}).format(Number(cents) / 100));
liquid.registerFilter('money_with_currency', cents => new Intl.NumberFormat('nl-NL', {style: 'currency', currency: 'EUR'}).format(Number(cents) / 100) + ' EUR');
liquid.registerFilter('money_without_trailing_zeros', cents => new Intl.NumberFormat('nl-NL', {style: 'currency', currency: 'EUR', minimumFractionDigits: 0, maximumFractionDigits: 2}).format(Number(cents) / 100));
liquid.registerFilter('t', (key, ...args) => {
  if (key === 'products.product.price.from_price_html') return 'Vanaf ' + args.find(x => x[0] === 'price')[1];
  if (key === 'products.product.volume_pricing.price_range') return args.map(x => x[1]).join(' – ');
  return key;
});
liquid.registerTag('doc',{parse(token,remaining){while(remaining.length && remaining.shift().getText()!=='{% enddoc %}'){}},render(){return '';}});
const moneyLiquid = fs.readFileSync(new URL('snippets/bc-money.liquid', theme), 'utf8');
const priceLiquid = fs.readFileSync(new URL('snippets/price.liquid', theme), 'utf8');
const baseContext = {shop: {currency: 'EUR'}, cart: {currency: {iso_code: 'EUR'}}, settings: {currency_code_enabled: false}};
for (const [amount, expected] of [[9900, '€ 99,00'], [9999, '€ 99,99'], [10000, '€ 100'], [10049, '€ 100,49'], [14900, '€ 149'], [14949, '€ 149,49'], [114700, '€ 1.147']]) {
  assert.equal(normalize(await liquid.parseAndRender(moneyLiquid, {...baseContext, amount})), expected);
  assert.equal(normalize(await liquid.parseAndRender(moneyLiquid, {...baseContext, amount, with_currency: true})), expected + ' EUR');
  record(`real-liquid-helper-${amount}-with-and-without-currency`);
}
assert.match(await liquid.parseAndRender(moneyLiquid, {...baseContext, cart: {currency: {iso_code: 'USD'}}, amount: 14900}), /149,00/);
record('non-eur-liquid-uses-original-money-filter');

for (const [amount, expected] of [[9900, /99,00/], [14900, /149(?!,00)/], [14949, /149,49/]]) {
  const product = {price: amount, price_min: amount, price_max: amount, compare_at_price: 19995, available: true, price_varies: false, selected_or_first_available_variant: {}};
  const html = await liquid.parseAndRender(priceLiquid, {...baseContext, product});
  const content = html.match(/class="price-item price-item--sale price-item--last">([\s\S]*?)<\/span>/)[1];
  assert.match(content, expected);
  assert.match(html, /199,95/);
  record(`real-native-price-snippet-${amount}-preserves-compare-at`);
}
const rangeProduct = {price: 14900, price_min: 14900, price_max: 19900, available: true, price_varies: true, selected_or_first_available_variant: {}};
assert.match(await liquid.parseAndRender(priceLiquid, {...baseContext, product: rangeProduct}), /Vanaf €\s*149(?!,00)/);
record('native-price-varies-keeps-from-label');

async function filterReplay({search = false, cents = 14900, hydratedCents = cents, tile = null, helper = true}) {
  const w = new Window({url: 'https://test.invalid/' + (search ? 'search?q=demo' : 'collections/demo'), width: 390, height: 844});
  Object.defineProperty(w.document, 'readyState', {configurable: true, value: 'complete'});
  w.ResizeObserver = class {observe() {} disconnect() {}};
  w.IntersectionObserver = class {observe() {} disconnect() {}};
  w.Shopify = {routes: {root: '/'}};
  const errors = [];
  w.console.error = (...a) => errors.push(a.map(String).join(' '));
  w.document.documentElement.lang = 'nl';
  w.document.body.innerHTML = `<main id="MainContent"><section class="${search ? 'template-search' : 'bc-collection'}"><div id="BcExternalFilters" data-api-base="https://filters.invalid" data-collection="${search ? '__all__' : 'demo'}" data-search-mode="${search}" data-products-count="1" data-card-data-section="bc-card-data" data-temporary-in-stock="true"></div><div class="facets-vertical page-width"><aside id="main-collection-filters"></aside><div id="ProductGridContainer"><ul id="product-grid" class="grid product-grid"><li>Native fallback</li></ul></div></div></section></main>`;
  const product = {id: 123, shopify_product_id: 123, handle: 'demo', title: 'Testproduct', vendor: 'Demo', price_cents: cents, price_varies: false, image_url: ''};
  const card = {...product, price_cents: hydratedCents, variant_id: 789, available: true, can_add: true, specs: [], switcher_html: '', ...(tile ? {tile_price: tile} : {})};
  w.fetch = async input => {
    const url = String(input);
    if (url.startsWith('https://filters.invalid/')) return {ok: true, json: async () => ({products: [product], facets: [], found: 1, collection: {handle: search ? '__all__' : 'demo', profile_products: 1}})};
    if (url.includes('/products/demo?sections=bc-card-data')) return {ok: true, json: async () => ({'bc-card-data': `<script type="application/json" data-bc-card-data>${JSON.stringify(card)}</script>`})};
    throw new Error('Unstubbed request: ' + url);
  };
  if (helper) w.eval(moneyJs);
  w.eval(filterJs);
  for (let i = 0; i < 18; i++) await new Promise(resolve => setImmediate(resolve));
  assert.deepEqual(errors, []);
  const el = w.document.querySelector('.bc-filter-card__price');
  assert(el, 'actual external card rendered');
  const text = normalize(el.textContent);
  assert.equal(w.document.querySelector('[data-bc-card-cart]').disabled, false);
  await w.happyDOM.abort();
  w.close();
  return text;
}
for (const search of [false, true]) {
  const text = await filterReplay({search});
  assert.match(text, /149/);
  assert(!text.includes('149,00'));
  record(`full-external-js-whole-price-${search ? 'search' : 'collection'}`);
}
assert.match(await filterReplay({cents: 14949}), /149,49/);
record('fractional-selling-price-is-never-hidden');
assert.match(await filterReplay({cents: 9900}), /99,00/);
record('under100-retains-two-decimals');
const hydrated = await filterReplay({cents: 14949, hydratedCents: 14900});
assert(!hydrated.includes('149,49') && !hydrated.includes('149,00'));
record('fresh-shopify-hydration-replaces-older-index-price');
assert.match(await filterReplay({helper: false}), /149,00/);
record('missing-optional-helper-keeps-safe-existing-format');
const tile = await filterReplay({cents: 12845, tile: {box_area: 1.2, unit_price_cents: 10704}});
assert(!tile.includes('128,45'));
assert.match(tile, /107,04/);
assert.match(tile, /per m²/);
record('tile-area-only-amount-remains-exact');

const report = {status: 'PASS', tests: results.length, results, scope: 'Offline actual Liquid and full external-filter JS. Shopify money filters are stubbed with Intl; live preview is separate. No checkout, order, physical phone or real network claim.'};
fs.writeFileSync(new URL('pricing-contract-results.json', import.meta.url), JSON.stringify(report, null, 2) + '\n');
console.log(results.length + ' price presentation checks PASS');
