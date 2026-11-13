const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const KEY = 'bc:product-switcher:position:v1';
const helper = fs.readFileSync(path.join(__dirname, 'scroll_position.js'), 'utf8');
const engine = fs.readFileSync(path.join(__dirname, 'preview-theme/assets/bc-product-switcher.js'), 'utf8');

function env({ optIn = true, complete = false } = {}) {
  let now = 1000, serial = 0, accesses = 0;
  const jobs = new Map(), values = new Map(), listeners = new Map();
  const scrolls = [], navigations = [];
  const document = { readyState: complete ? 'complete' : 'interactive', documentElement: { style: { scrollBehavior: 'smooth' } }, querySelectorAll: () => [], addEventListener() {} };
  const window = {
    location: { href: 'https://badkamercity.nl/products/source', origin: 'https://badkamercity.nl', assign: (url) => navigations.push(url) },
    history: { scrollRestoration: 'auto' }, scrollX: 0, scrollY: 800,
    setTimeout(callback, delay) { const id = ++serial; jobs.set(id, { at: now + delay, callback }); return id; },
    clearTimeout(id) { jobs.delete(id); },
    requestAnimationFrame(callback) { return this.setTimeout(() => callback(now), 16); },
    cancelAnimationFrame(id) { this.clearTimeout(id); },
    scrollTo(options, top) { this.scrollY = typeof options === 'object' ? options.top : top; scrolls.push(this.scrollY); },
    addEventListener(type, handler, options) { const items = listeners.get(type) || []; items.push({ handler, capture: options === true || !!options?.capture }); listeners.set(type, items); },
    removeEventListener(type, handler, options) { const capture = options === true || !!options?.capture; listeners.set(type, (listeners.get(type) || []).filter(item => item.handler !== handler || item.capture !== capture)); },
  };
  const storage = {
    failGet: false, failSet: false, failRemove: false,
    getItem(key) { accesses++; if (this.failGet) throw Error('get blocked'); return values.get(key) || null; },
    setItem(key, value) { accesses++; if (this.failSet) throw Error('set blocked'); values.set(key, value); },
    removeItem(key) { accesses++; if (this.failRemove) throw Error('remove blocked'); values.delete(key); },
  };
  window.sessionStorage = storage;
  const root = { dataset: { switchGroup: 'pilot', ...(optIn ? { bcPreservePosition: 'true' } : {}) }, docTop: 1200, isConnected: true, getBoundingClientRect() { return { top: this.docTop - window.scrollY }; } };
  class FakeDate extends Date { static now() { return now; } }
  const context = { window, document, URL, Date: FakeDate, console: { warn() {}, info() {} }, fetch() { throw Error('unexpected fetch'); } };
  const keeper = vm.runInNewContext(helper + '\ncreateSwitcherPositionKeeper;', context)(window, document);
  function advance(ms) {
    const target = now + ms; let guard = 0;
    while (true) {
      const next = [...jobs.entries()].filter(([, j]) => j.at <= target).sort((a, b) => a[1].at - b[1].at || a[0] - b[0])[0];
      if (!next) break;
      if (++guard > 10000) throw Error('timer runaway');
      const [id, job] = next; jobs.delete(id); now = job.at; job.callback();
    }
    now = target;
  }
  function emit(type, captureOnly = false) { for (const item of [...(listeners.get(type) || [])]) if (!captureOnly || item.capture) item.handler({ type }); }
  function arrive(url = 'https://badkamercity.nl/products/target') { window.location.href = url; window.scrollY = 0; root.docTop = 1400; }
  function pending(overrides = {}) { values.set(KEY, JSON.stringify({ version: 1, group: 'pilot', target: '/products/target', top: 400, savedAt: now, ...overrides })); }
  return { window, document, root, context, keeper, storage, values, scrolls, navigations, jobs, advance, emit, arrive, pending, get accesses() { return accesses; } };
}

test('opt-out groups never access storage or change history/styles/position', () => {
  const e = env({ optIn: false }); e.pending();
  assert.equal(e.keeper.remember(e.root, '/products/target'), null);
  assert.equal(e.keeper.prepare(e.root), null);
  assert.equal(e.accesses, 0); assert.equal(e.window.history.scrollRestoration, 'auto');
  assert.equal(e.document.documentElement.style.scrollBehavior, 'smooth'); assert.equal(e.scrolls.length, 0);
});

test('first switch restores only after delayed async menu rendering', () => {
  const e = env(); assert.equal(e.keeper.remember(e.root, '/products/target').top, 400);
  e.arrive(); const restore = e.keeper.prepare(e.root); assert.ok(restore); assert.equal(e.values.has(KEY), false);
  e.advance(5000); assert.equal(e.scrolls.length, 0); restore.activate();
  assert.equal(e.root.getBoundingClientRect().top, 400); assert.equal(e.window.scrollY, 1000);
});

test('late image/layout corrections continue until window load plus two seconds', () => {
  const e = env(); e.pending(); e.arrive(); const restore = e.keeper.prepare(e.root); restore.activate();
  e.root.docTop += 240; e.advance(3000); assert.equal(e.root.getBoundingClientRect().top, 400);
  e.emit('load'); e.advance(800); e.root.docTop += 90; e.emit('load', true); e.advance(20);
  assert.equal(e.root.getBoundingClientRect().top, 400); e.advance(1500);
  assert.equal(e.window.history.scrollRestoration, 'auto'); assert.equal(e.document.documentElement.style.scrollBehavior, 'smooth');
  const count = e.scrolls.length; e.root.docTop += 300; e.advance(500); assert.equal(e.scrolls.length, count);
});

test('all real user input cancels restoration during the async wait', () => {
  for (const type of ['pointerdown', 'touchstart', 'wheel', 'keydown']) {
    const e = env(); e.pending(); e.arrive(); const restore = e.keeper.prepare(e.root);
    e.emit(type); restore.activate(); e.advance(1000);
    assert.equal(e.scrolls.length, 0, type); assert.equal(e.window.history.scrollRestoration, 'auto', type);
  }
});

test('user scroll after initial correction wins over late layout changes', () => {
  const e = env(); e.pending(); e.arrive(); const restore = e.keeper.prepare(e.root); restore.activate();
  e.emit('wheel'); e.window.scrollY = 550; const count = e.scrolls.length;
  e.root.docTop += 100; e.advance(1000); assert.equal(e.window.scrollY, 550); assert.equal(e.scrolls.length, count);
});

test('TTL, future timestamps, group, destination, malformed top and version are checked', () => {
  for (const record of [{ savedAt: -29001 }, { savedAt: 2000 }, { group: 'other' }, { target: '/products/other' }, { top: null }, { version: 2 }, { target: 'https://evil.example/products/target' }]) {
    const e = env(); e.pending(record); e.arrive(); assert.equal(e.keeper.prepare(e.root), null, JSON.stringify(record));
    assert.equal(e.values.has(KEY), false); assert.equal(e.scrolls.length, 0);
  }
});

test('only preview_theme_id is ignored; semantic query and fragment must still match', () => {
  const e = env(); e.keeper.remember(e.root, '/products/target?variant=42&preview_theme_id=11&selling_plan=3#details');
  e.arrive('https://badkamercity.nl/products/target?selling_plan=3&preview_theme_id=99&variant=42#details');
  assert.ok(e.keeper.prepare(e.root));
  for (const suffix of ['?variant=43&selling_plan=3#details', '?variant=42&selling_plan=4#details', '?variant=42&selling_plan=3#other']) {
    const x = env(); x.keeper.remember(x.root, '/products/target?variant=42&selling_plan=3#details');
    x.arrive('https://badkamercity.nl/products/target' + suffix); assert.equal(x.keeper.prepare(x.root), null);
  }
});

test('restore is consumed once and cannot replay on back or repeated initialization', () => {
  const e = env(); e.pending(); e.arrive(); const restore = e.keeper.prepare(e.root); restore.activate();
  e.emit('pagehide'); assert.equal(e.keeper.prepare(e.root), null); assert.equal(e.window.history.scrollRestoration, 'auto');
});

test('a page that never finishes loading has a hard fifteen-second restore deadline', () => {
  const e = env(); e.pending(); e.arrive(); const restore = e.keeper.prepare(e.root); restore.activate();
  e.advance(15100); assert.equal(e.window.history.scrollRestoration, 'auto'); assert.equal(e.jobs.size, 0);
});

test('already loaded page still gets two seconds after delayed rendering', () => {
  const e = env({ complete: true }); e.pending(); e.arrive(); const restore = e.keeper.prepare(e.root);
  e.advance(5000); restore.activate(); e.advance(1000); e.root.docTop += 100; e.advance(100);
  assert.equal(e.root.getBoundingClientRect().top, 400); e.advance(1100); assert.equal(e.window.history.scrollRestoration, 'auto');
});

test('storage errors never throw and off-origin destinations cannot be remembered', () => {
  for (const method of ['failGet', 'failSet', 'failRemove']) {
    const e = env(); e.storage[method] = true; assert.doesNotThrow(() => e.keeper.remember(e.root, '/products/target'));
    e.pending(); e.arrive(); assert.doesNotThrow(() => e.keeper.prepare(e.root));
  }
  const e = env(); assert.equal(e.keeper.remember(e.root, 'https://evil.example/products/target'), null); assert.equal(e.accesses, 0);
});

function navigable(e) {
  const source = engine.replace("  if (document.readyState === 'loading') {", "  globalThis.__BC_TEST = { BCProductSwitcherV2 };\n  if (document.readyState === 'loading') {");
  vm.runInNewContext(source, e.context);
  const instance = Object.create(e.context.__BC_TEST.BCProductSwitcherV2.prototype);
  Object.assign(instance, {
    root: e.root, productRoot: { querySelector: () => null }, productHandle: 'source',
    products: [{ handle: 'source', url: '/products/source', options: { kleur: 'Chroom' } }, { handle: 'target', url: '/products/target', options: { kleur: 'Koper' } }],
    menus: [{ key: 'kleur' }], state: { kleur: 'Chroom' }, isNavigating: false, status: { textContent: '' }, syncControls() {},
    setNavigating(value) { this.isNavigating = value; if (value) e.root.docTop += 77; }, buildInitialState() { return { kleur: 'Chroom' }; },
  });
  return instance;
}

test('real engine captures before disabling, while opt-out navigation stays unchanged', () => {
  for (const optIn of [true, false]) {
    const e = env({ optIn }); const instance = navigable(e); instance.updateSelection('kleur', 'Koper');
    assert.deepEqual(e.navigations, ['https://badkamercity.nl/products/target']);
    if (optIn) assert.equal(JSON.parse(e.values.get(KEY)).top, 400); else assert.equal(e.accesses, 0);
  }
});

test('real engine navigation survives storage failure and still blocks external origins', () => {
  const e = env(); e.storage.failSet = true; navigable(e).updateSelection('kleur', 'Koper'); assert.equal(e.navigations.length, 1);
  const x = env(); const external = navigable(x); external.products[1].url = 'https://evil.example/products/target';
  external.updateSelection('kleur', 'Koper'); assert.equal(x.navigations.length, 0); assert.equal(x.accesses, 0);
});

test('a storage getter security error does not block navigation', () => {
  const e = env();
  Object.defineProperty(e.window, 'sessionStorage', { get() { throw Error('SecurityError'); } });
  assert.doesNotThrow(() => navigable(e).updateSelection('kleur', 'Koper'));
  assert.equal(e.navigations.length, 1);
  assert.equal(e.keeper.prepare(e.root), null);
});

test('failed real navigation discards the saved position and unlocks the selector', () => {
  const e = env(); e.window.location.assign = () => { throw Error('navigation blocked'); };
  const instance = navigable(e); instance.updateSelection('kleur', 'Koper');
  assert.equal(e.values.has(KEY), false); assert.equal(instance.isNavigating, false);
  assert.equal(instance.state.kleur, 'Chroom');
});
