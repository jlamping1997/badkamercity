'use strict';
/**
 * Behavioral contracts for Sunshower quick-shop. Requires jsdom on NODE_PATH.
 * Set BC_THEME_PATH to a theme export with the production patch applied.
 * Browser/Shopify network, real photos and checkout need independent QA.
 */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM, VirtualConsole } = require('jsdom');
const themePath = process.env.BC_THEME_PATH || path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(themePath, 'assets/bc-sunshower-shop.js'), 'utf8');
const flush = () => new Promise(resolve => setImmediate(resolve));
const deferred = () => { let resolve, reject; const promise = new Promise((a, b) => { resolve = a; reject = b; }); return { promise, resolve, reject }; };
const simulateNativeBlur = w => { w.document.body.tabIndex = -1; w.document.body.focus(); w.document.body.removeAttribute('tabindex'); };
function fixture(prefix) {
  const choices = ['white', 'black', 'grey', 'sand'].map((key, index) => ({ key, id: `${prefix}${index + 1}`, available: key !== 'grey', url: `/products/${prefix}-${key}`, title: `Sunseat ${key}`, label: key, price: `€${index + 320},00`, image: { src: `https://example.test/${key}.jpg`, srcset: `https://example.test/${key}.jpg 500w`, sizes: '300px', width: 500, height: 500, alt: `${key} seat`, mode: 'lifestyle' } }));
  return `<article data-bcsse-shop-card data-bcsse-add-label="Add" data-bcsse-loading-label="Adding" data-bcsse-loading-image-label="Loading image" data-bcsse-added-label="Added __product__" data-bcsse-error-label="Check cart before trying again" data-bcsse-image-error-label="Image failed" data-bcsse-sold-out-label="Sold out">
  <script type="application/json" data-bcsse-shop-data>${JSON.stringify({ initial: 'white', choices })}</script>
  <a href="/products/${prefix}-white" data-bcsse-shop-link><img data-bcsse-shop-image src="/white.jpg"></a>
  <span data-bcsse-shop-color>white</span><p data-bcsse-shop-price>€320,00</p>
  ${choices.map(c => `<a href="${c.url}" data-bcsse-shop-choice="${c.key}"${c.key === 'white' ? ' class="bcsse-swatch--selected" aria-current="true"' : ''}>${c.label}</a>`).join('')}
  <form data-bcsse-shop-form action="/nl/cart/add"><input name="id" value="${prefix}1"><button type="submit" data-bcsse-shop-submit><span data-bcsse-shop-button-label>Add</span></button></form>
  <p data-bcsse-shop-status role="status" hidden></p><a data-bcsse-shop-cart-link href="/nl/cart" hidden>Cart</a></article>`;
}
function setup({ count = 1, cart = true, cartType = 'notification', throwRender = false, route = '/nl/cart/add' } = {}) {
  const tag = cartType === 'drawer' ? 'cart-drawer' : 'cart-notification';
  const dom = new JSDOM(`<body><a id="cart-icon-bubble" href="/nl/cart"><span data-cart-count>0</span></a>${cart ? `<${tag}></${tag}>` : ''}${Array.from({ length: count }, (_, i) => fixture(i + 1)).join('')}</body>`, { url: 'https://example.test/nl/pages/sunshower', runScripts: 'outside-only', virtualConsole: new VirtualConsole() });
  const w = dom.window;
  const probes = [], requests = [], renders = [], events = [];
  w.routes = { cart_add_url: route, cart_url: '/nl/cart' };
  w.PUB_SUB_EVENTS = { cartUpdate: 'cart-update' };
  w.publish = async (name, data) => { events.push({ name, data }); };
  w.Image = class {
    constructor() { this.naturalWidth = 0; this.complete = false; probes.push(this); }
    set src(value) { this._src = value; }
    get src() { return this._src; }
  };
  w.fetch = (url, options) => { const d = deferred(); requests.push({ url, options, ...d }); return d.promise; };
  Object.defineProperty(w, 'scrollY', { value: 735, writable: true });
  const notification = w.document.querySelector(tag);
  if (notification) {
    notification.getSectionsToRender = () => [{ id: cartType === 'drawer' ? 'cart-drawer' : 'cart-notification-product' }, { id: 'cart-icon-bubble' }];
    notification.setActiveElement = element => { notification.trigger = element; };
    notification.renderContents = data => { renders.push(data); if (cartType === 'notification') w.scrollY = 0; if (throwRender) throw new Error('render'); };
  }
  w.eval(source);
  w.BCSunshowerShop.init(w.document);
  const cards = [...w.document.querySelectorAll('[data-bcsse-shop-card]')];
  const get = (card, name) => card.querySelector(`[data-bcsse-shop-${name}]`);
  const choice = (card, key, options = {}) => { const e = new w.MouseEvent('click', { bubbles: true, cancelable: true, button: 0, ...options }); card.querySelector(`[data-bcsse-shop-choice="${key}"]`).dispatchEvent(e); return e; };
  const submit = card => { const e = new w.Event('submit', { bubbles: true, cancelable: true }); get(card, 'form').dispatchEvent(e); return e; };
  const succeedImage = probe => { probe.naturalWidth = 500; probe.complete = true; if (probe.onload) probe.onload(); };
  const result = (id = 11, sections = true) => ({ id, key: `${id}:key`, ...(sections ? { sections: { 'cart-notification-product': '<div>Product</div>', 'cart-drawer': '<div class="shopify-section"><div id="CartDrawer">Drawer</div></div>', 'cart-icon-bubble': '<div class="shopify-section"><span data-cart-count>1</span></div>' } } : {}) });
  const respond = (request, data = result(), ok = true) => request.resolve({ ok, json: async () => data });
  return { dom, w, cards, probes, requests, renders, events, notification, get, choice, submit, succeedImage, result, respond };
}

(async function run() {
  let checks = 0;
  {
    const t = setup(); const c = t.cards[0];
    assert.equal(c.dataset.bcsseShopReady, 'true');
    t.w.BCSunshowerShop.init(t.w.document); t.w.eval(source);
    t.choice(c, 'black');
    assert.equal(t.get(c, 'form').elements.id.value, '11');
    assert.equal(t.get(c, 'color').textContent, 'white');
    assert.equal(t.get(c, 'submit').disabled, true);
    assert.equal(c.querySelectorAll('.bcsse-swatch--selected').length, 1);
    assert.equal(c.querySelector('.bcsse-swatch--selected').dataset.bcsseShopChoice, 'white');
    t.submit(c); await flush(); assert.equal(t.requests.length, 0);
    t.succeedImage(t.probes[0]); await flush();
    assert.equal(t.get(c, 'form').elements.id.value, '12');
    assert.equal(t.get(c, 'color').textContent, 'black');
    assert.equal(t.get(c, 'price').textContent, '€321,00');
    assert.equal(t.get(c, 'image').getAttribute('src'), 'https://example.test/black.jpg');
    assert.equal(t.get(c, 'image').getAttribute('srcset'), 'https://example.test/black.jpg 500w');
    assert.equal(t.get(c, 'image').alt, 'black seat');
    assert.equal(t.get(c, 'link').getAttribute('href'), '/products/1-black');
    assert.equal(c.querySelector('[data-bcsse-shop-choice="black"]').getAttribute('aria-pressed'), 'true');
    assert.equal(c.querySelectorAll('.bcsse-swatch--selected').length, 1);
    assert.equal(c.querySelector('.bcsse-swatch--selected').dataset.bcsseShopChoice, 'black');
    assert.equal(c.querySelectorAll('[data-bcsse-shop-choice][aria-current]').length, 0);
    assert.equal(c.dataset.bcsseImageMode, 'lifestyle');
    const originalBadge = t.w.document.getElementById('cart-icon-bubble');
    t.get(c, 'submit').focus();
    t.submit(c); t.submit(c); await flush();
    simulateNativeBlur(t.w);
    assert.equal(t.w.document.activeElement, t.w.document.body, 'Simulate native disabled-button focus loss');
    assert.equal(t.requests.length, 1, 'Repeated init and fast taps produce only one POST');
    const request = t.requests[0], payload = JSON.parse(request.options.body);
    assert.equal(request.url, '/nl/cart/add.js');
    assert.equal(payload.id, '12'); assert.equal(payload.quantity, 1); assert.equal(payload.items, undefined);
    assert.deepEqual(payload.sections, ['cart-icon-bubble']);
    assert.equal(payload.sections_url, '/nl/pages/sunshower');
    t.choice(c, 'sand'); assert.equal(t.probes.length, 1, 'Swatches locked during POST');
    t.respond(request, t.result(12)); await flush();
    assert.equal(t.get(c, 'status').textContent, 'Added Sunseat black');
    assert.equal(t.get(c, 'cart-link').hidden, false);
    assert.equal(t.get(c, 'submit').disabled, false);
    assert.equal(t.notification.trigger, undefined);
    assert.equal(t.renders.length, 0, 'Native notification must not open or reveal sticky header');
    assert.equal(t.w.document.getElementById('cart-icon-bubble'), originalBadge, 'Badge target node preserved');
    assert.equal(originalBadge.querySelector('[data-cart-count]').textContent, '1');
    assert.equal(t.w.document.activeElement, t.get(c, 'submit'), 'Focus stays on inline add button');
    assert.equal(t.w.scrollY, 735, 'Accessory browsing scroll position is preserved');
    assert.equal(t.events.length, 1);
    t.dom.window.close(); checks++;
  }
  {
    const t = setup(); const c = t.cards[0];
    t.choice(c, 'black'); t.choice(c, 'sand');
    t.succeedImage(t.probes[0]); await flush(); assert.equal(t.get(c, 'color').textContent, 'white');
    t.succeedImage(t.probes[1]); await flush(); assert.equal(t.get(c, 'color').textContent, 'sand');
    t.choice(c, 'black'); t.probes[2].onerror(); await flush();
    assert.equal(t.get(c, 'color').textContent, 'sand'); assert.equal(t.get(c, 'form').elements.id.value, '14');
    assert.equal(t.get(c, 'status').textContent, 'Image failed'); assert.equal(t.get(c, 'submit').disabled, false);
    assert.equal(c.querySelectorAll('.bcsse-swatch--selected').length, 1);
    assert.equal(c.querySelector('.bcsse-swatch--selected').dataset.bcsseShopChoice, 'sand');
    t.choice(c, 'black'); t.choice(c, 'sand'); await flush();
    t.succeedImage(t.probes[3]); await flush(); assert.equal(t.get(c, 'color').textContent, 'sand');
    assert.equal(t.get(c, 'submit').disabled, false);
    assert.equal(t.choice(c, 'white', { ctrlKey: true }).defaultPrevented, false);
    assert.equal(t.probes.length, 4);
    const grey = c.querySelector('[data-bcsse-shop-choice="grey"]');
    const key = new t.w.KeyboardEvent('keydown', { key: ' ', code: 'Space', bubbles: true, cancelable: true });
    grey.dispatchEvent(key); assert.equal(key.defaultPrevented, true); t.succeedImage(t.probes[4]); await flush();
    assert.equal(t.get(c, 'color').textContent, 'grey'); assert.equal(t.get(c, 'button-label').textContent, 'Sold out');
    t.submit(c); await flush(); assert.equal(t.requests.length, 0);
    t.dom.window.close(); checks++;
  }
  {
    const t = setup({ count: 2, route: '/nl/cart/add.js' });
    t.submit(t.cards[0]); t.submit(t.cards[1]); await flush();
    assert.equal(t.requests.length, 1); assert.equal(t.get(t.cards[1], 'submit').disabled, true);
    t.respond(t.requests[0]); await flush(); assert.equal(t.requests.length, 2);
    assert.equal(t.requests[1].url, '/nl/cart/add.js');
    assert.equal(JSON.parse(t.requests[1].options.body).id, '21');
    t.respond(t.requests[1], t.result(21)); await flush(); assert.equal(t.renders.length, 0); assert.equal(t.events.length, 2);
    t.dom.window.close(); checks++;
  }
  {
    for (const mode of ['render-throw', 'null-section', 'malformed-section', 'network', 'server', 'missing-confirmation', 'no-cart-ui']) {
      const t = setup({ throwRender: mode === 'render-throw', cart: mode !== 'no-cart-ui' }); const c = t.cards[0];
      t.submit(c); await flush();
      if (mode === 'network') t.requests[0].reject(new Error('lost response'));
      else if (mode === 'server') t.respond(t.requests[0], { status: 422, description: '<b>No stock</b>' }, false);
      else if (mode === 'missing-confirmation') t.respond(t.requests[0], {});
      else if (mode === 'null-section') { const result = t.result(); result.sections['cart-icon-bubble'] = null; t.respond(t.requests[0], result); }
      else if (mode === 'malformed-section') { const result = t.result(); result.sections['cart-icon-bubble'] = '<p>Wrong wrapper</p>'; t.respond(t.requests[0], result); }
      else t.respond(t.requests[0]);
      await flush();
      assert.equal(t.requests.length, 1, `${mode}: no automatic retry`);
      assert.equal(t.get(c, 'submit').disabled, false);
      assert.equal(t.get(c, 'cart-link').hidden, false);
      const status = t.get(c, 'status');
      assert.equal(status.textContent, mode === 'server' ? '<b>No stock</b>' : ['network', 'missing-confirmation'].includes(mode) ? 'Check cart before trying again' : 'Added Sunseat white');
      assert.equal(status.querySelector('b'), null, 'Server errors render as text');
      assert.equal(t.renders.length, 0);
      assert.equal(t.w.scrollY, 735);
      if (['null-section', 'malformed-section'].includes(mode)) assert.equal(t.w.document.querySelector('[data-cart-count]').textContent, '0');
      t.dom.window.close(); checks++;
    }
  }
  {
    const t = setup(); const c = t.cards[0];
    t.get(c, 'submit').focus();
    t.submit(c); await flush();
    simulateNativeBlur(t.w);
    const other = t.w.document.getElementById('cart-icon-bubble');
    other.focus();
    t.respond(t.requests[0]); await flush();
    assert.equal(t.w.document.activeElement, other, 'Do not steal focus when the user focused elsewhere during the request');
    assert.equal(t.w.scrollY, 735);
    t.dom.window.close(); checks++;
  }
  {
    const t = setup(); const c = t.cards[0];
    assert.equal(t.w.document.activeElement, t.w.document.body);
    t.submit(c); await flush(); t.respond(t.requests[0]); await flush();
    assert.equal(t.w.document.activeElement, t.w.document.body, 'Do not move focus when the add button was not focused at submission');
    t.dom.window.close(); checks++;
  }
  {
    for (const throwRender of [false, true]) {
      const t = setup({ cartType: 'drawer', throwRender }); const c = t.cards[0];
      t.submit(c); await flush();
      assert.deepEqual(JSON.parse(t.requests[0].options.body).sections, ['cart-drawer', 'cart-icon-bubble']);
      t.respond(t.requests[0]); await flush();
      assert.equal(t.renders.length, 1);
      assert.equal(t.notification.trigger, t.get(c, 'submit'));
      assert.equal(t.get(c, 'status').textContent, 'Added Sunseat white');
      assert.equal(t.get(c, 'cart-link').hidden, false);
      assert.equal(t.requests.length, 1);
      assert.equal(t.w.scrollY, 735);
      t.dom.window.close(); checks++;
    }
  }
  {
    const t = setup(); const c = t.cards[0];
    await flush();
    t.choice(c, 'black');
    c.dispatchEvent(new t.w.Event('shopify:section:unload', { bubbles: true }));
    t.succeedImage(t.probes[0]); await flush();
    assert.equal(c.dataset.bcsseShopReady, undefined);
    assert.equal(c.querySelector('[data-bcsse-shop-choice]').hasAttribute('role'), false);
    assert.equal(t.get(c, 'submit').disabled, false);
    assert.equal(t.submit(c).defaultPrevented, false, 'Unloaded controller restores native form submit');
    c.dispatchEvent(new t.w.Event('shopify:section:load', { bubbles: true }));
    assert.equal(c.dataset.bcsseShopReady, 'true');
    t.submit(c); await flush(); assert.equal(t.requests.length, 1);
    t.respond(t.requests[0]); await flush();
    t.dom.window.close(); checks++;
  }
  console.log(`PASS: ${checks} scenario groups (atomic image/variant changes, races, errors, keyboard, availability, duplicate locks, queue ordering, cart response contracts, render fallbacks, lifecycle).`);
})().catch(error => { console.error(error); process.exitCode = 1; });
