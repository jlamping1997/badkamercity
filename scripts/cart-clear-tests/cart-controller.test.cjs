const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM, VirtualConsole } = require('jsdom');
const themePath = path.resolve(process.argv[2] || process.env.BC_CART_THEME_PATH || path.join(__dirname, '../..'));
const assetRoot = process.env.BC_CART_ASSETS || path.join(themePath, 'assets');
const source = fs.readFileSync(path.join(assetRoot, 'bc-cart-page.js'), 'utf8');
const nativeSource = fs.readFileSync(path.join(assetRoot, 'cart.js'), 'utf8');
const flush = async () => { for (let i = 0; i < 5; i++) await new Promise(resolve => setImmediate(resolve)); };
const defer = () => { let resolve, reject; const promise = new Promise((a, b) => { resolve = a; reject = b; }); return { promise, resolve, reject }; };
const codeDiscount = title => ({ title, type: 'discount_code', target_type: 'line_item', total_allocated_amount: 1000 });
const cartData = ({ codes = [], monetary = [], quantity = 1, total = 2900, sections, errors } = {}) => ({
  item_count: quantity, items: quantity ? [{ quantity, line_level_discount_allocations: monetary.map(title => ({ amount: 1000, discount_application: codeDiscount(title) })) }] : [],
  total_price: total, discount_codes: codes.map(c => typeof c === 'string' ? { code: c, applicable: true } : c), cart_level_discount_applications: [], ...(sections ? { sections } : {}), ...(errors ? { errors } : {}),
});
const component = () => `<bc-cart-discount hidden data-cart-url="/nl/cart" data-update-url="/nl/cart/update.js" data-message-empty="Empty" data-message-error="Error" data-message-invalid="Invalid" data-message-loading="Loading" data-message-success="Applied" data-message-shipping="Shipping pending" data-message-pending="Code pending" data-message-removed="Removed" data-message-remove="Remove [code]">
  <form data-bc-discount-form><input id="BC-Cart-Discount" name="discount"><button type="submit">Apply</button></form><ul data-bc-discount-codes hidden></ul><p id="BC-Cart-Discount-Status" data-bc-discount-status role="status" hidden></p></bc-cart-discount>`;
const itemContents = quantity => quantity ? `<div class="cart-item" id="CartItem-1"><a href="/product">Product</a><button type="button" name="plus">+</button><input id="Quantity-1" name="updates[]" value="${quantity}" data-index="1" data-min="0" min="0" step="1" data-quantity-variant-id="123"><cart-remove-button data-index="1"><a href="/cart/change">Remove</a></cart-remove-button><span class="loading__spinner hidden"></span><p id="Line-item-error-1"><span class="cart-item__error-text"></span></p></div>` : '';
const footerContents = (total = '€29,00', empty = false) => `<div data-bc-cart-summary data-bc-product-total="${total}" data-bc-total-label="Products" data-bc-shipping-pending-label="At checkout"><span data-bc-shipping-price>€6,95</span><span data-bc-order-total>${total}+shipping</span><span data-bc-total-label>Total</span><p data-bc-shipping-promise>Shipping threshold</p>${component()}<button id="checkout" type="submit" name="checkout" form="cart"${empty ? ' disabled' : ''}>Checkout</button><div id="cart-errors"></div></div>`;
const sections = (quantity = 1, total = '€19,00') => ({
  items: `<section><div class="js-contents">${itemContents(quantity)}</div></section>`,
  footer: `<section><div class="js-contents">${footerContents(total, quantity === 0)}</div></section>`,
  'cart-icon-bubble': `<section class="shopify-section"><b>${quantity}</b></section>`,
  'cart-live-region-text': `<section class="shopify-section"><span>Updated ${quantity}</span></section>`,
});
function setup({ native = false, empty = false } = {}) {
  const dom = new JSDOM(`<body><cart-items><form id="cart" action="/nl/cart"><div id="main-cart-items" data-id="items"><div class="js-contents">${itemContents(empty ? 0 : 1)}</div></div></form><p id="shopping-cart-line-item-status"></p></cart-items><div id="main-cart-footer" data-id="footer"><div class="js-contents">${footerContents('€29,00', empty)}</div></div><div id="cart-icon-bubble"><b>1</b></div><div id="cart-live-region-text"></div></body>`, { url: 'https://example.test/nl/cart?preview_theme_id=123', runScripts: 'outside-only', virtualConsole: new VirtualConsole() });
  const w = dom.window, requests = [], events = [], subscribers = [];
  w.routes = { cart_url: '/nl/cart', cart_change_url: '/nl/cart/change.js', cart_update_url: '/nl/cart/update.js' };
  w.PUB_SUB_EVENTS = { cartUpdate: 'cart-update' };
  w.subscribe = (name, cb) => { subscribers.push(cb); return () => {}; };
  w.publish = (name, data) => { events.push({ name, data }); for (const cb of subscribers) cb(data); };
  w.CartPerformance = { createStartingMarker: () => 1, measure: (name, cb) => cb(), measureFromMarker: () => {}, measureFromEvent: () => {} };
  w.ON_CHANGE_DEBOUNCE_TIMER = 300;
  w.debounce = (cb, delay) => (...args) => w.setTimeout(() => cb(...args), delay);
  w.fetchConfig = () => ({ method: 'POST', headers: { 'Content-Type': 'application/json' } });
  w.cartStrings = { error: 'Native error', quantityError: 'Quantity [quantity]' };
  w.quickOrderListStrings = { min_error: 'Min [min]', max_error: 'Max [max]', step_error: 'Step [step]' };
  w.fetch = (url, options = {}) => { const d = defer(); requests.push({ url, options, ...d }); return d.promise; };
  if (native) w.eval(nativeSource);
  else w.document.querySelector('cart-items').getSectionsToRender = () => [{ id: 'main-cart-items', section: 'items', selector: '.js-contents' }, { id: 'cart-icon-bubble', section: 'cart-icon-bubble', selector: '.shopify-section' }, { id: 'cart-live-region-text', section: 'cart-live-region-text', selector: '.shopify-section' }, { id: 'main-cart-footer', section: 'footer', selector: '.js-contents' }];
  w.eval(source);
  const respond = (request, data, ok = true) => request.resolve({ ok, json: async () => data, text: async () => JSON.stringify(data) });
  const submit = code => { const input = w.document.querySelector('input[name="discount"]'); input.value = code; input.focus(); w.document.querySelector('[data-bc-discount-form]').dispatchEvent(new w.Event('submit', { bubbles: true, cancelable: true })); };
  const change = value => { const input = w.document.getElementById('Quantity-1'); input.focus(); input.value = value; input.dispatchEvent(new w.Event('change', { bubbles: true })); };
  const status = () => w.document.querySelector('[data-bc-discount-status]').textContent;
  const checkout = () => w.document.getElementById('checkout');
  const body = request => JSON.parse(request.options.body);
  return { dom, w, requests, events, respond, submit, change, status, checkout, body, close: () => w.close() };
}
(async () => {
  let checks = 0;
  {
    const t = setup(); assert.equal(t.requests.length, 1);
    assert.equal(t.requests[0].url, '/nl/cart.js');
    t.respond(t.requests[0], cartData({ codes: ['SHIP'], total: 2900 })); await flush();
    assert.equal(t.w.document.querySelector('[data-bc-discount-remove]').dataset.bcDiscountRemove, 'SHIP');
    assert.equal(t.w.document.querySelector('[data-bc-shipping-price]').textContent, 'At checkout');
    assert.equal(t.w.document.querySelector('[data-bc-order-total]').textContent, '€29,00');
    assert.equal(t.w.document.querySelector('span[data-bc-total-label]').textContent, 'Products');
    t.submit('SAVE'); await flush();
    assert.equal(t.checkout().disabled, true);
    assert.equal(t.body(t.requests[1]).discount, 'SHIP,SAVE', 'Keep shipping codes hidden by Liquid');
    assert.deepEqual(t.body(t.requests[1]).sections, ['items', 'cart-icon-bubble', 'cart-live-region-text', 'footer']);
    assert.equal(t.body(t.requests[1]).sections_url, '/nl/cart?preview_theme_id=123');
    t.respond(t.requests[1], cartData({ codes: ['SHIP', 'SAVE'], monetary: ['SAVE'], total: 1900, sections: sections() })); await flush();
    assert.equal(t.status(), 'Applied'); assert.equal(t.checkout().disabled, false);
    assert.equal(t.events.length, 1); assert.equal(t.events[0].data.source, 'cart-items');
    assert.equal(t.w.document.querySelector('[data-bc-order-total]').textContent, '€19,00');
    assert.equal(t.w.document.querySelectorAll('[data-bc-discount-remove]').length, 2);
    t.close(); checks++;
  }
  {
    const t = setup(); t.respond(t.requests[0], cartData()); await flush(); t.submit('BAD'); await flush();
    t.respond(t.requests[1], cartData({ codes: [{ code: 'BAD', applicable: false }], sections: sections() })); await flush();
    assert.equal(t.status(), 'Invalid', '200 is not a successful discount');
    assert.equal(t.w.document.querySelectorAll('[data-bc-discount-remove]').length, 0);
    assert.equal(t.w.document.querySelector('[data-bc-shipping-price]').textContent, '€6,95');
    assert.equal(t.checkout().disabled, false); t.close(); checks++;
  }
  {
    const t = setup(); t.respond(t.requests[0], cartData()); await flush(); t.submit('SAVE'); t.submit('SAVE'); await flush();
    assert.equal(t.requests.length, 2, 'Double submit sends one mutation');
    const partial = sections(2); partial.footer = null;
    t.respond(t.requests[1], cartData({ codes: ['SAVE'], monetary: ['SAVE'], quantity: 2, sections: partial })); await flush();
    assert.equal(t.requests.length, 3); assert.equal(t.requests[2].options.method, undefined);
    assert.equal(t.w.document.getElementById('cart-icon-bubble').textContent, '1', 'No partial section update before all validate');
    t.respond(t.requests[2], sections(2)); await flush();
    assert.equal(t.w.document.getElementById('cart-icon-bubble').textContent, '2');
    assert.equal(t.w.document.getElementById('cart-live-region-text').textContent, 'Updated 2');
    assert.equal(t.w.document.getElementById('Quantity-1').value, '2');
    assert.equal(t.requests.filter(r => r.options.method === 'POST').length, 1, 'Rendering fallback never repeats mutation');
    assert.equal(t.checkout().disabled, false); assert.equal(t.status(), 'Applied'); t.close(); checks++;
  }
  {
    const t = setup(); t.respond(t.requests[0], cartData()); await flush(); t.submit('SAVE'); await flush();
    t.requests[1].reject(new Error('Response lost after server wrote')); await flush();
    t.respond(t.requests[2], cartData({ codes: ['SAVE'], monetary: ['SAVE'], total: 1900 })); await flush();
    t.respond(t.requests[3], sections()); await flush();
    assert.equal(t.status(), 'Applied', 'Read confirms uncertain mutation outcome');
    assert.equal(t.requests.filter(r => r.options.method === 'POST').length, 1); assert.equal(t.checkout().disabled, false); t.close(); checks++;
  }
  {
    const t = setup(); t.respond(t.requests[0], cartData()); await flush(); t.submit('SAVE'); await flush();
    t.requests[1].reject(new Error('Network')); await flush(); t.requests[2].reject(new Error('Network')); await flush();
    assert.equal(t.status(), 'Error'); assert.equal(t.checkout().disabled, true); assert.equal(t.w.BCCartPage.mustReload, true);
    assert.equal(t.w.BCCartPage.stateKnown, false); assert.equal(t.requests.filter(r => r.options.method === 'POST').length, 1); t.close(); checks++;
  }
  {
    const t = setup({ native: true }); t.respond(t.requests[0], cartData()); await flush();
    t.change('2'); t.submit('SAVE'); await flush();
    assert.equal(t.requests.length, 2, 'Quantity reserves the mutation slot before coupon');
    assert.equal(t.requests[1].url, '/nl/cart/change.js'); assert.equal(t.body(t.requests[1]).quantity, 2);
    assert.equal(t.checkout().disabled, true);
    t.respond(t.requests[1], cartData({ quantity: 2, sections: sections(2) })); await flush();
    assert.equal(t.checkout().disabled, false); assert.equal(t.w.document.getElementById('Quantity-1').value, '2');
    await new Promise(resolve => setTimeout(resolve, 350)); assert.equal(t.requests.length, 2, 'No stale native debounce mutation');
    assert.equal(t.events.length, 1); t.close(); checks++;
  }
  {
    const t = setup({ native: true }); t.respond(t.requests[0], cartData()); await flush(); t.submit('SAVE'); await flush(); t.change('2'); await flush();
    assert.equal(t.requests.length, 2, 'Quantity cannot race an in-flight coupon');
    assert.equal(t.w.document.getElementById('Quantity-1').value, '1');
    const submit = new t.w.Event('submit', { bubbles: true, cancelable: true });
    t.w.document.getElementById('cart').dispatchEvent(submit); assert.equal(submit.defaultPrevented, true);
    t.respond(t.requests[1], cartData({ codes: ['SAVE'], monetary: ['SAVE'], sections: sections() })); await flush();
    assert.equal(t.checkout().disabled, false); t.close(); checks++;
  }
  {
    const t = setup(); t.respond(t.requests[0], cartData({ codes: ['SAVE', 'SHIP'], monetary: ['SAVE'] })); await flush();
    t.w.document.querySelector('[data-bc-discount-remove="SAVE"]').click(); await flush();
    assert.equal(t.body(t.requests[1]).discount, 'SHIP');
    t.respond(t.requests[1], cartData({ codes: ['SHIP'], sections: sections() })); await flush();
    assert.equal(t.status(), 'Removed'); assert.equal(t.w.document.querySelector('[data-bc-shipping-price]').textContent, 'At checkout');
    t.w.document.querySelector('[data-bc-discount-remove="SHIP"]').click(); await flush();
    assert.equal(t.body(t.requests[2]).discount, '');
    t.respond(t.requests[2], cartData({ sections: sections() })); await flush();
    assert.equal(t.w.document.querySelector('[data-bc-shipping-price]').textContent, '€6,95');
    assert.equal(t.w.document.querySelector('span[data-bc-total-label]').textContent, 'Total'); t.close(); checks++;
  }
  {
    const t = setup({ native: true }); t.change('2'); await flush(); assert.equal(t.requests.length, 1, 'Wait for initial state read');
    assert.equal(t.checkout().disabled, true);
    t.respond(t.requests[0], cartData({ codes: ['SHIP'] })); await flush();
    assert.equal(t.requests.length, 2); t.respond(t.requests[1], cartData({ quantity: 2, codes: ['SHIP'], sections: sections(2) })); await flush();
    assert.equal(t.w.BCCartPage.cart.item_count, 2); assert.equal(t.checkout().disabled, false); t.close(); checks++;
  }
  {
    const t = setup({ native: true }); t.respond(t.requests[0], cartData()); await flush(); t.change('2'); await flush();
    const broken = sections(2); broken.items = null;
    t.respond(t.requests[1], cartData({ quantity: 2, sections: broken })); await flush();
    assert.equal(t.requests.length, 3); t.respond(t.requests[2], cartData({ quantity: 2 })); await flush();
    t.respond(t.requests[3], sections(2)); await flush();
    assert.equal(t.requests.filter(r => r.options.method === 'POST').length, 1);
    assert.equal(t.w.document.getElementById('Quantity-1').value, '2'); assert.equal(t.checkout().disabled, false); t.close(); checks++;
  }
  {
    const t = setup(); const code = '<img src=x onerror=alert(1)>'; t.respond(t.requests[0], cartData({ codes: [code] })); await flush();
    const pill = t.w.document.querySelector('[data-bc-discount-remove]');
    assert.equal(pill.dataset.bcDiscountRemove, code); assert.equal(t.w.document.querySelector('bc-cart-discount img'), null);
    assert.equal(pill.getAttribute('aria-label'), `Remove ${code}`); t.close(); checks++;
  }
  {
    const t = setup({ empty: true }); t.respond(t.requests[0], cartData({ quantity: 0, total: 0 })); await flush(); t.submit('BAD'); await flush();
    t.respond(t.requests[1], cartData({ quantity: 0, total: 0, codes: [{ code: 'BAD', applicable: false }], sections: sections(0, '€0,00') })); await flush();
    assert.equal(t.checkout().disabled, true, 'Do not re-enable server-disabled empty checkout'); t.close(); checks++;
  }
  {
    const t = setup({ native: true }); t.respond(t.requests[0], cartData()); await flush(); t.change('2'); await flush();
    t.w.publish('cart-update', { source: 'recommendation' }); await flush(); assert.equal(t.requests.length, 2, 'External refresh waits for pending change');
    t.respond(t.requests[1], cartData({ quantity: 2, sections: sections(2) })); await flush();
    t.respond(t.requests[2], cartData({ quantity: 3 })); await flush(); t.respond(t.requests[3], sections(3)); await flush();
    assert.equal(t.w.document.getElementById('Quantity-1').value, '3'); assert.equal(t.checkout().disabled, false); t.close(); checks++;
  }
  {
    const t = setup({ native: true }); t.respond(t.requests[0], cartData({ codes: ['SHIP'] })); await flush(); t.change('2'); await flush();
    const noCodes = cartData({ quantity: 2, sections: sections(2) }); delete noCodes.discount_codes;
    t.respond(t.requests[1], noCodes); await flush(); assert.equal(t.checkout().disabled, true);
    assert.equal(t.requests[2].url, '/nl/cart.js', 'Read code metadata missing from native change response');
    t.respond(t.requests[2], cartData({ quantity: 2, codes: ['SHIP'] })); await flush();
    t.respond(t.requests[3], sections(2)); await flush();
    assert.equal(t.w.document.querySelector('[data-bc-discount-remove]').dataset.bcDiscountRemove, 'SHIP');
    assert.equal(t.w.document.querySelector('[data-bc-shipping-price]').textContent, 'At checkout');
    assert.equal(t.checkout().disabled, false); t.close(); checks++;
  }
  {
    const t = setup({ native: true }); t.respond(t.requests[0], cartData()); await flush();
    const focus = t.w.HTMLElement.prototype.focus;
    t.w.HTMLElement.prototype.focus = function(...args) { if (!this.closest('cart-items')?.inert) return focus.apply(this, args); };
    t.w.document.querySelector('button[name="plus"]').focus();
    const input = t.w.document.getElementById('Quantity-1'); input.value = '2'; input.dispatchEvent(new t.w.Event('change', { bubbles: true })); await flush();
    t.respond(t.requests[1], cartData({ quantity: 2, sections: sections(2) })); await flush();
    assert.equal(t.w.document.activeElement.id, 'Quantity-1', 'Restore keyboard focus after inert content unlocks'); t.close(); checks++;
  }
  {
    const t = setup(); t.respond(t.requests[0], cartData()); await flush(); t.submit('SHIP'); await flush();
    t.respond(t.requests[1], cartData({ codes: ['SHIP'], sections: sections() })); await flush();
    assert.equal(t.status(), 'Code pending', 'A non-monetary code is not assumed to be a shipping discount');
    assert.equal(t.w.document.querySelector('[data-bc-shipping-price]').textContent, 'At checkout'); t.close(); checks++;
  }
  console.log(JSON.stringify({ passed: checks, assets: assetRoot }));
})().catch(error => { console.error(error); process.exitCode = 1; });
