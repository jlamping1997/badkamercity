const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync(path.join(__dirname, 'theme/assets/bc-product-inbouw.js'), 'utf8');
const formSource = fs.readFileSync(path.join(__dirname, 'theme/assets/product-form.js'), 'utf8');
const tests = [];
const test = (name, fn) => tests.push({ name, fn });
const clean = value => JSON.parse(JSON.stringify(value));

class Element {
  constructor() {
    this.dataset = {};
    this.attrs = new Map();
    this.listeners = new Map();
    this.hidden = true;
    this.disabled = false;
    this.isConnected = true;
    this.textContent = '';
    const classes = new Set();
    this.classList = {
      add: x => classes.add(x), remove: x => classes.delete(x), contains: x => classes.has(x),
      toggle(x, on) { if (on === undefined) on = !classes.has(x); on ? classes.add(x) : classes.delete(x); }
    };
  }
  setAttribute(k, v) { this.attrs.set(k, String(v)); }
  getAttribute(k) { return this.attrs.get(k) ?? null; }
  removeAttribute(k) { this.attrs.delete(k); }
  toggleAttribute(k, on) { on ? this.attrs.set(k, '') : this.attrs.delete(k); }
  addEventListener(k, fn) { if (!this.listeners.has(k)) this.listeners.set(k, []); this.listeners.get(k).push(fn); }
  dispatch(k, event = {}) { this.listeners.get(k)?.forEach(fn => fn(event)); }
  focus() { this.focused = true; }
}

function fixture(options = {}) {
  const registered = new Map();
  const storage = new Map();
  const observers = [];
  const calls = [];
  const redirects = [];
  const window = new Element();
  window.location = { pathname: options.path || '/products/cb105-cr', assign: url => redirects.push(url) };
  window.routes = { cart_url: '/cart' };
  const sessionStorage = {
    getItem: k => { if (options.storageError) throw Error('blocked'); return storage.get(k) || null; },
    setItem: (k, v) => { if (options.storageError) throw Error('blocked'); storage.set(k, v); },
    removeItem: k => { if (options.storageError) throw Error('blocked'); storage.delete(k); }
  };
  if (options.saved) storage.set('bc-inbouw-choice-v1', JSON.stringify(options.saved));
  class FakeFormData {
    constructor(form) { this.map = new Map(form.entries); }
    get(k) { return this.map.get(k) || null; }
    append(k, v) { this.map.set(k, v); }
    entries() { return this.map.entries(); }
  }
  const context = vm.createContext({
    HTMLElement: Element, AbortController, Date, Intl, Number, Map, Set, Array, JSON,
    customElements: { get: k => registered.get(k), define: (k, v) => registered.set(k, v) },
    MutationObserver: class { constructor(fn) { this.fn = fn; observers.push(this); } observe() {} disconnect() {} },
    window, sessionStorage, document: { documentElement: { lang: 'nl-NL' }, querySelector: () => null },
    FormData: FakeFormData, setTimeout: options.setTimeout || setTimeout, clearTimeout: options.clearTimeout || clearTimeout,
    fetch: async (url, config) => {
      calls.push({ url, config });
      if (options.fetch) return options.fetch(url, config);
      return { ok: true, json: async () => ({ items: [
        { variant_id: 53187556999434, sku: 'CB105EXT18CR', quantity: 9 },
        { variant_id: 53187364356362, sku: 'HBCB105', quantity: 9 }
      ] }) };
    },
    routes: { cart_add_url: '/cart/add.js' }, fetchConfig: () => ({ headers: {} }),
    PUB_SUB_EVENTS: { cartUpdate: 'update', cartError: 'error' }, publish: () => Promise.resolve(),
    CartPerformance: { createStartingMarker() {}, measureFromMarker() {}, measureFromEvent() {}, measure(x, fn) { fn(); } },
    console
  });
  vm.runInContext(source, context);
  vm.runInContext(formSource, context);
  const addon = new (registered.get('bc-inbouw-addon'))();
  addon.dataset = {
    valid: 'true', parentVariant: '53187556999434', parentSku: 'CB105EXT18CR',
    bodyVariant: '53187364356362', bodySku: 'HBCB105', bodyAvailable: 'true',
    bodyPrice: '17400', quantityPerTrim: '1', currency: 'EUR', addUrl: '/cart/add.js', cartUrl: '/cart',
    messageChoice: 'choose', messageChanged: 'changed', messageQuantity: 'quantity',
    messageUnavailable: 'unavailable', messageUncertain: 'uncertain', messageLoading: 'loading',
    ...options.dataset
  };
  const controls = new Element(), error = new Element(), cartLink = new Element(), total = new Element();
  const radios = ['yes', 'no'].map(value => Object.assign(new Element(), { value, checked: false, disabled: true }));
  const button = new Element(), spinner = new Element();
  const root = new Element();
  const switcher = new Element();
  switcher.dataset.switchGroup = options.group === undefined ? 'cb105' : options.group;
  root.querySelector = selector => selector === '[data-bc-product-switcher-v2]' ? switcher : null;
  const quantity = Object.assign(new Element(), { value: options.quantity ?? '1', reportValidity() {} });
  quantity.checkValidity = () => !options.invalidQuantity && Number(quantity.value) > 0;
  const id = { get value() { return options.currentVariant || addon.dataset.parentVariant; } };
  const form = new Element();
  form.entries = [['id', id.value], ['quantity', quantity.value], ...(options.properties || [])];
  form.elements = { namedItem: name => ({ id, quantity })[name] || null };
  form.contains = () => !options.externalQuantity;
  form.querySelector = selector => selector === 'bc-inbouw-addon' ? addon : selector === '[type="submit"]' ? button : null;
  const parent = Object.create(registered.get('product-form').prototype);
  Object.assign(parent, { form, submitButton: button, submitButtonText: new Element(), cart: null, hideErrors: false });
  parent.errors = [];
  parent.handleErrorMessage = m => parent.errors.push(m);
  parent.querySelector = selector => selector === '.loading__spinner' ? spinner : null;
  parent.closest = selector => selector === 'product-info' ? root : null;
  addon.closest = selector => ({ 'product-info': root, form, 'product-form': parent })[selector] || null;
  addon.querySelector = selector => ({ '[data-inbouw-controls]': controls, '[data-inbouw-error]': error,
    '[data-inbouw-cart-link]': cartLink, '[data-inbouw-total]': total })[selector] || null;
  addon.querySelectorAll = () => radios;
  addon.connectedCallback();
  const choose = value => { radios.forEach(x => x.checked = x.value === value); addon.update(); };
  const submit = () => addon.handleSubmit(parent);
  return { addon, form, parent, controls, error, cartLink, total, radios, button, spinner, root,
    choose, submit, calls, redirects, storage, window, quantity, observers, context };
}

test('explicit choice required; no paid default', () => {
  const f = fixture(); assert.equal(f.submit(), true); assert.equal(f.error.textContent, 'choose');
  assert.equal(f.calls.length, 0); assert.equal(f.addon.choice(), ''); assert.equal(f.controls.disabled, false);
});
test('No leaves original single-product flow untouched', () => {
  const f = fixture(); f.choose('no'); assert.equal(f.submit(), false); assert.equal(f.calls.length, 0);
});
test('Yes adds exact two variants and multiplies both by quantity two', async () => {
  const f = fixture({ quantity: '2' }); f.choose('yes'); assert.equal(f.submit(), true); await f.addon.pendingAdd;
  assert.deepEqual(clean(JSON.parse(f.calls[0].config.body)), { items: [
    { id: '53187556999434', quantity: 2 }, { id: '53187364356362', quantity: 2 }
  ] }); assert.deepEqual(f.redirects, ['/cart']); assert.equal(f.calls.length, 1);
});
test('existing body cart quantity does not skip requested body', async () => {
  const f = fixture({ quantity: '3' }); f.choose('yes'); f.submit(); await f.addon.pendingAdd;
  assert.equal(JSON.parse(f.calls[0].config.body).items[1].quantity, 3); assert.equal(f.calls.length, 1);
  assert.deepEqual(f.redirects, ['/cart']);
});
test('trim properties and selling plan remain on trim only', async () => {
  const f = fixture({ properties: [['properties[Notitie]', 'Eigen keuze'], ['selling_plan', '123']] });
  f.choose('yes'); f.submit(); await f.addon.pendingAdd;
  const items = JSON.parse(f.calls[0].config.body).items;
  assert.deepEqual(items[0].properties, { Notitie: 'Eigen keuze' }); assert.equal(items[0].selling_plan, '123');
  assert.equal(items[1].properties, undefined);
});
test('changed trim identity blocks both Yes and No', () => {
  for (const choice of ['yes', 'no']) {
    const f = fixture({ currentVariant: '999' }); f.choose(choice); assert.equal(f.submit(), true);
    assert.equal(f.error.textContent, 'changed'); assert.equal(f.calls.length, 0);
  }
});
test('invalid, same-ID, missing-SKU, and nonnumeric mappings fail closed', () => {
  for (const dataset of [{ valid: 'false' }, { bodyVariant: '53187556999434' }, { bodySku: '' }, { bodyVariant: 'wrong' }]) {
    const f = fixture({ dataset }); f.choose('yes'); assert.equal(f.submit(), true); assert.equal(f.calls.length, 0);
    assert.equal(f.controls.disabled, true);
  }
});
test('unavailable body disables Yes but explicit No remains possible', () => {
  const f = fixture({ dataset: { bodyAvailable: 'false' } }); assert.equal(f.radios[0].disabled, true);
  assert.equal(f.radios[1].disabled, false); f.choose('yes'); assert.equal(f.submit(), true);
  assert.equal(f.error.textContent, 'unavailable'); f.choose('no'); assert.equal(f.submit(), false);
});
test('quantity validation rejects blank zero negative fraction nonnumber and overflow', () => {
  for (const quantity of ['', '0', '-1', '1.5', 'no', '9007199254740992']) {
    const f = fixture({ quantity }); f.choose('yes'); assert.equal(f.submit(), true); assert.equal(f.calls.length, 0);
    assert.equal(f.error.textContent, 'quantity');
  }
});
test('browser quantity-rule validity is respected', () => {
  const f = fixture({ quantity: '3', invalidQuantity: true }); f.choose('yes'); f.submit();
  assert.equal(f.calls.length, 0); assert.equal(f.error.textContent, 'quantity');
});
test('duplicate submits while awaiting response send one request', async () => {
  let resolve;
  const f = fixture({ fetch: () => new Promise(r => resolve = r) }); f.choose('yes'); f.submit(); f.submit();
  assert.equal(f.calls.length, 1); assert.equal(f.button.getAttribute('aria-busy'), 'true');
  resolve({ ok: false, json: async () => ({ status: 422 }) }); await f.addon.pendingAdd;
});
test('422 uncertainty locks repeats including after switching to No', async () => {
  const f = fixture({ fetch: async () => ({ ok: false, json: async () => ({ status: 422, description: 'sold out' }) }) });
  f.choose('yes'); f.submit(); await f.addon.pendingAdd;
  assert.equal(f.addon.uncertain, true); assert.equal(f.cartLink.hidden, false); assert.equal(f.error.textContent, 'uncertain');
  assert.equal(f.button.getAttribute('aria-disabled'), 'true'); f.choose('no'); f.submit(); assert.equal(f.calls.length, 1);
});
test('missing or wrong response line never reports successful pair', async () => {
  const badResults = [ {}, { items: [] }, { items: [{ variant_id: 53187556999434, sku: 'CB105EXT18CR', quantity: 1 }] },
    { items: [{ variant_id: 53187556999434, sku: 'wrong', quantity: 1 }, { variant_id: 53187364356362, sku: 'HBCB105', quantity: 1 }] } ];
  for (const result of badResults) {
    const f = fixture({ fetch: async () => ({ ok: true, json: async () => result }) }); f.choose('yes'); f.submit(); await f.addon.pendingAdd;
    assert.equal(f.addon.uncertain, true); assert.equal(f.redirects.length, 0);
  }
});
test('partial returned quantity locks without retry or rollback', async () => {
  const f = fixture({ quantity: '2', fetch: async () => ({ ok: true, json: async () => ({ items: [
    { id: 53187556999434, sku: 'CB105EXT18CR', quantity: 2 }, { id: 53187364356362, sku: 'HBCB105', quantity: 1 }
  ] }) }) }); f.choose('yes'); f.submit(); await f.addon.pendingAdd;
  assert.equal(f.calls.length, 1); assert.equal(f.addon.uncertain, true); assert.equal(f.redirects.length, 0);
});
test('network and malformed-JSON failures require checking cart', async () => {
  for (const fetch of [async () => { throw TypeError('network'); }, async () => ({ ok: true, json: async () => { throw SyntaxError('bad'); } })]) {
    const f = fixture({ fetch }); f.choose('yes'); f.submit(); await f.addon.pendingAdd;
    assert.equal(f.addon.uncertain, true); assert.equal(f.cartLink.hidden, false); assert.equal(f.calls.length, 1);
  }
});
test('stalled request times out once and requires cart check', async () => {
  let timeout;
  const f = fixture({ setTimeout: fn => { timeout = fn; return 1; }, clearTimeout() {},
    fetch: (url, config) => new Promise((resolve, reject) => config.signal.addEventListener('abort', () => reject(Error('aborted')))) });
  f.choose('yes'); f.submit(); timeout(); await f.addon.pendingAdd;
  assert.equal(f.calls.length, 1); assert.equal(f.addon.uncertain, true); assert.equal(f.cartLink.hidden, false);
});
test('navigation and disconnected product block new adds', () => {
  const f = fixture(); f.choose('yes'); f.root.dataset.bcNavigating = 'true'; f.submit(); assert.equal(f.calls.length, 0);
  delete f.root.dataset.bcNavigating; f.addon.isConnected = false; f.submit(); assert.equal(f.calls.length, 0);
});
test('same group and body restores explicit choice once across product pages', () => {
  const saved = { group: 'cb105', body: '53187364356362', choice: 'yes', from: '/products/cb105-ai', savedAt: Date.now() };
  const f = fixture({ saved }); assert.equal(f.addon.choice(), 'yes'); assert.equal(f.storage.size, 0);
});
test('different group/body/path or stale future malformed choice never restores', () => {
  const base = { group: 'cb105', body: '53187364356362', choice: 'yes', from: '/products/cb105-ai', savedAt: Date.now() };
  for (const delta of [{ group: 'other' }, { body: '999' }, { from: '/products/cb105-cr' },
    { savedAt: Date.now() - 60000 }, { savedAt: Date.now() + 60000 }, { choice: 'whatever' }]) {
    const f = fixture({ saved: { ...base, ...delta } }); assert.equal(f.addon.choice(), ''); assert.equal(f.storage.size, 0);
  }
});
test('restored Yes with unavailable body remains Yes and visibly blocked', () => {
  const f = fixture({ dataset: { bodyAvailable: 'false' }, saved: { group: 'cb105', body: '53187364356362', choice: 'yes', from: '/products/cb105-ai', savedAt: Date.now() } });
  assert.equal(f.addon.choice(), 'yes'); assert.equal(f.error.textContent, 'unavailable'); assert.equal(f.radios[0].disabled, true);
  f.submit(); assert.equal(f.calls.length, 0);
});
test('storage failure does not block initial explicit choice', () => {
  const f = fixture({ storageError: true }); assert.equal(f.addon.ready, true); f.choose('no'); assert.equal(f.submit(), false);
});
test('choice saved only during actual switcher navigation', () => {
  const f = fixture(); f.choose('yes'); f.addon.rememberForNavigation(); assert.equal(f.storage.size, 0);
  f.root.dataset.bcNavigating = 'true'; f.observers[0].fn(); const saved = JSON.parse(f.storage.get('bc-inbouw-choice-v1'));
  assert.equal(saved.group, 'cb105'); assert.equal(saved.body, '53187364356362'); assert.equal(saved.choice, 'yes');
});
test('quantity outside form uses form association and receives updates', () => {
  const f = fixture({ externalQuantity: true }); f.choose('yes'); assert.match(f.total.textContent, /174/);
  f.quantity.value = '2'; f.quantity.dispatch('input'); assert.match(f.total.textContent, /348/);
});
test('back-forward cache with pending add requires checking cart', () => {
  const f = fixture(); f.addon.busy = true; f.window.dispatch('pageshow', { persisted: true });
  assert.equal(f.addon.uncertain, true); assert.equal(f.cartLink.hidden, false);
});
test('product-form hook blocks when addon script is not initialized', () => {
  const f = fixture(); f.addon.ready = false; f.parent.onSubmitHandler({ preventDefault() {} });
  assert.equal(f.calls.length, 0); assert.equal(f.parent.errors.at(-1), 'loading');
});
test('product-form original No flow submits one form payload', async () => {
  const f = fixture({ fetch: async () => ({ ok: true, json: async () => ({ id: 53187556999434 }) }) });
  f.choose('no'); f.parent.onSubmitHandler({ preventDefault() {} });
  await new Promise(r => setImmediate(r));
  assert.equal(f.calls.length, 1); assert.equal(f.calls[0].config.body.get('id'), '53187556999434');
  assert.equal(typeof f.calls[0].config.body, 'object');
});
test('unmapped product still submits original form payload', async () => {
  const f = fixture({ fetch: async () => ({ ok: true, json: async () => ({ id: 53187556999434 }) }) });
  f.form.querySelector = () => null; f.parent.onSubmitHandler({ preventDefault() {} });
  await new Promise(r => setImmediate(r));
  assert.equal(f.calls.length, 1); assert.equal(f.calls[0].config.body.get('id'), '53187556999434');
});

(async () => {
  const results = [];
  for (const item of tests) {
    try { await item.fn(); results.push({ test: item.name, result: 'PASS' }); }
    catch (e) { results.push({ test: item.name, result: 'FAIL', error: e.stack }); }
  }
  const report = { tests: results.length, passed: results.filter(x => x.result === 'PASS').length,
    failed: results.filter(x => x.result === 'FAIL').length, environment: 'Node VM with DOM/form/transport doubles; browser QA still required', results };
  fs.writeFileSync(path.join(__dirname, 'cart-tests.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report, null, 2));
  process.exitCode = report.failed ? 1 : 0;
})();
