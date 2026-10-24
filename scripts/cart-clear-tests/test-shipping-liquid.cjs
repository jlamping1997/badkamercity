const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { Liquid } = require(process.env.BC_LIQUIDJS_MODULE || 'liquidjs');

const themePath = path.resolve(process.argv[2] || process.env.BC_CART_THEME_PATH || path.join(__dirname, '../..'));
const footer = fs.readFileSync(path.join(themePath, 'sections/main-cart-footer.liquid'), 'utf8');
const items = fs.readFileSync(path.join(themePath, 'sections/main-cart-items.liquid'), 'utf8');
const cartTemplateSource = fs.readFileSync(path.join(themePath, 'templates/cart.json'), 'utf8');
const cartTemplate = JSON.parse(cartTemplateSource.replace(/^\s*\/\*[\s\S]*?\*\//, ''));
const policy = footer.match(/{%-?\s*liquid\b[\s\S]*?-?%}/)?.[0];
assert.ok(policy, 'Shipping policy must come from the actual footer Liquid block');

const engine = new Liquid({ strictFilters: true });
engine.registerFilter('money', (cents) => `EUR ${(Number(cents) / 100).toFixed(2)}`);
engine.registerFilter('json', (value) => JSON.stringify(value));
engine.registerFilter('asset_url', (value) => `/assets/${value}`);
engine.registerFilter('stylesheet_tag', (value) => `<link rel="stylesheet" href="${value}">`);
engine.registerFilter('inline_asset_content', () => '<svg aria-hidden="true"></svg>');
engine.registerFilter('payment_type_svg_tag', () => '<svg aria-hidden="true"></svg>');
engine.registerFilter('t', (key) => key);

const cases = [
  { name: 'below threshold', price: 9999, known: true, shipping: 695, total: 10694 },
  { name: 'exactly EUR 100 remains paid', price: 10000, known: true, shipping: 695, total: 10695 },
  { name: 'EUR 100.01 is free', price: 10001, known: true, shipping: 0, total: 10001 },
  { name: 'multiple products above threshold', price: 11600, count: 4, known: true, shipping: 0, total: 11600 },
  { name: 'discount moves total below threshold', price: 9000, original: 12000, discount: 3000, known: true, shipping: 695, total: 9695 },
  { name: 'discount ends exactly at threshold', price: 10000, original: 12000, discount: 2000, known: true, shipping: 695, total: 10695 },
  { name: 'discount remains one cent above threshold', price: 10001, original: 12000, discount: 1999, known: true, shipping: 0, total: 10001 },
  { name: 'zero-price physical cart remains paid', price: 0, original: 2900, discount: 2900, known: true, shipping: 695, total: 695 },
  { name: 'empty cart has no delivery charge', price: 0, count: 0, physical: false, known: false, shipping: 0, total: 0 },
  { name: 'non-shipping products have no delivery charge', price: 5250, physical: false, known: false, shipping: 0, total: 5250 },
  { name: 'foreign destination does not receive Dutch estimate', price: 2900, country: 'DE', known: false, shipping: 0, total: 2900 },
  { name: 'foreign destination above threshold is not promised free', price: 11600, country: 'BE', known: false, shipping: 0, total: 11600 },
  { name: 'non-EUR currency has no euro estimate', price: 2900, currency: 'USD', known: false, shipping: 0, total: 2900 },
];

const body = footer.replace(/{%[-]?\s*schema\s*[-]?%}[\s\S]*?{%[-]?\s*endschema\s*[-]?%}/g, '');
const contextFor = (entry) => ({
  cart: {
    total_price: entry.price,
    original_total_price: entry.original ?? entry.price,
    total_discount: entry.discount ?? 0,
    item_count: entry.count ?? 1,
    requires_shipping: entry.physical ?? true,
    currency: { iso_code: entry.currency ?? 'EUR' },
    taxes_included: true,
    duties_included: false,
    cart_level_discount_applications: [],
  },
  localization: { country: { iso_code: entry.country ?? 'NL' } },
  shop: { enabled_payment_types: [] },
  settings: { show_cart_note: false },
  routes: { cart_url: '/cart', cart_update_url: '/cart/update.js' },
  section: {
    id: 'cart-footer',
    settings: { color_scheme: 'scheme-1' },
    blocks: [{ type: 'subtotal' }, { type: 'buttons' }],
  },
});

async function main() {
  for (const entry of cases) {
    const context = contextFor(entry);
    const result = JSON.parse(await engine.parseAndRender(
      `${policy}{"known":{{ bc_shipping_known | json }},"shipping":{{ bc_shipping_price | json }},"total":{{ bc_cart_total | json }}}`,
      context,
    ));
    assert.deepEqual(result, { known: entry.known, shipping: entry.shipping, total: entry.total }, entry.name);

    const html = await engine.parseAndRender(body, context);
    const shippingText = html.match(/<dd\b[^>]*data-bc-shipping-price[^>]*>([\s\S]*?)<\/dd>/)?.[1].trim();
    const totalText = html.match(/<p\b[^>]*data-bc-order-total[^>]*>([\s\S]*?)<\/p>/)?.[1].trim();
    const expectedShipping = entry.physical === false
      ? 'bc_cart_page.no_shipping'
      : !entry.known
        ? 'bc_cart_page.calculated_at_checkout'
        : entry.shipping === 0
          ? 'bc_cart_page.free'
          : 'EUR 6.95';
    assert.equal(shippingText, expectedShipping, `${entry.name}: rendered shipping`);
    assert.equal(totalText, `EUR ${(entry.total / 100).toFixed(2)}`, `${entry.name}: rendered total`);
    assert.equal(html.includes('bc_cart_page.free_shipping_rule'), entry.known, `${entry.name}: Dutch free-shipping promise`);
    if (entry.discount) {
      assert.match(html, /bc_cart_page\.products_after_discounts/, `${entry.name}: discounted product subtotal is shown`);
      assert.match(html, new RegExp(`−EUR ${(entry.discount / 100).toFixed(2).replace('.', '\\.')}`), `${entry.name}: real discount is shown`);
    }
    console.log(`PASS ${entry.name}`);
  }

  const html = await engine.parseAndRender(body, contextFor(cases[0]));
  assert.match(html, /<button\b(?=[^>]*\bid="checkout")(?=[^>]*\bname="checkout")(?=[^>]*\bform="cart")[\s\S]*?>/);
  assert.match(items, /<form\b(?=[^>]*\bid="cart")(?=[^>]*\bmethod="post")(?=[^>]*\baction="{{ routes\.cart_url }}")[\s\S]*?>/);
  assert.ok(!html.includes('cart__dynamic-checkout-buttons'), 'Only the primary cart continuation should be shown');
  assert.match(html, /<bc-cart-discount\s+hidden\b/, 'Coupon control stays hidden until its controller is ready');
  assert.match(html, /<noscript>[\s\S]*bc_cart_page\.discount_no_js[\s\S]*<\/noscript>/);
  assert.match(html, /<form\s+data-bc-discount-form>/, 'Coupon form remains separate from native cart form');
  const itemSection = cartTemplate.order.findIndex((id) => cartTemplate.sections[id].type === 'main-cart-items');
  const footerSection = cartTemplate.order.findIndex((id) => cartTemplate.sections[id].type === 'main-cart-footer');
  assert.ok(itemSection >= 0 && footerSection > itemSection, 'Cost summary follows the products');
  console.log('PASS native checkout, progressive enhancement and section-order contracts');
  console.log(JSON.stringify({ policyCases: cases.length, renderedCases: cases.length, contracts: 'passed' }));
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
