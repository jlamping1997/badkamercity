const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { JSDOM } = require('jsdom');

const root = path.resolve(__dirname, '../..');
const before = fs.readFileSync(path.join(__dirname, 'fixtures/pre-fix-switcher.js'), 'utf8');
const after = fs.readFileSync(path.join(root, 'shopify/current/assets/bc-product-switcher.js'), 'utf8');
const fixtures = JSON.parse(fs.readFileSync(path.join(__dirname, 'fixtures/menu-groups.json'), 'utf8'));
const translations = Object.fromEntries(['nl', 'en.default'].map(locale => { const source = fs.readFileSync(path.join(root, `shopify/current/locales/${locale}.json`), 'utf8'); return [locale, JSON.parse(source.slice(source.indexOf('{')))]; }));
const results = [];
const clone = (value) => JSON.parse(JSON.stringify(value));

function labelsFor(locale = 'nl') {
  const values = translations[locale].bc_verlavio_choices;
  return {
    color: values.color,
    set_shape: values.set_shape,
    head_shape: values.head_shape,
    head_mount: values.head_mount,
    head_size: values.head_size,
    with_overflow: values.with_overflow,
    without_overflow: values.without_overflow,
    wall: values.wall,
    ceiling: values.ceiling,
    round: values.round,
    square: values.square,
    colors: {
      Chroom: values.chrome,
      'Mat Zwart': values.matte_black,
      'Brushed Gold': values.brushed_gold,
      'Gun Metal': values.gunmetal,
      RVS: values.stainless_steel,
      'Brushed Copper': values.brushed_copper
    }
  };
}

function render(source, fixture, options = {}) {
  const dom = new JSDOM('<!doctype html><html><body><product-info><div id="choices"></div><button class="product-form__submit">Toevoegen</button></product-info></body></html>', {
    url: options.url || `https://badkamercity.nl/products/${fixture.handle}`,
    pretendToBeVisual: true
  });
  const document = dom.window.document;
  Object.defineProperty(document, 'readyState', { configurable: true, value: 'complete' });
  const element = document.querySelector('#choices');
  const scoped = options.scoped !== false;
  element.dataset.bcProductSwitcherV2 = '';
  element.dataset.bcCompactColors = 'true';
  element.dataset.bcPreservePosition = 'true';
  element.dataset.switchGroup = fixture.group.id;
  element.dataset.productHandle = fixture.handle;
  element.dataset.productUrl = `/products/${fixture.handle}`;
  element.dataset.sectionId = 'test-section';
  element.dataset.labelAllColors = 'Bekijk alle __COUNT__ kleuren';
  element.dataset.labelLessColors = 'Minder kleuren';
  if (scoped) {
    element.dataset.bcVerlavioChoices = 'true';
    element.dataset.bcVerlavioContext = options.context === undefined ? 'shower_set' : options.context;
    element.dataset.bcVerlavioLabels = options.labels || JSON.stringify(labelsFor(options.locale));
  }
  if (options.hotbath) {
    delete element.dataset.bcCompactColors;
    element.dataset.hotbathMobileA = 'true';
  }
  const inline = document.createElement('script');
  inline.type = 'application/json';
  inline.dataset.bcSwitcherInline = '';
  inline.textContent = JSON.stringify({ groups: [fixture.group] });
  element.append(inline);
  const navigations = [];
  const errors = [];
  const currentUrl = new URL(dom.window.location.href);
  const window = {
    document,
    location: {
      origin: currentUrl.origin,
      pathname: currentUrl.pathname,
      href: currentUrl.href,
      assign: (url) => navigations.push(url)
    },
    sessionStorage: dom.window.sessionStorage,
    innerWidth: 390,
    addEventListener: dom.window.addEventListener.bind(dom.window),
    removeEventListener: dom.window.removeEventListener.bind(dom.window)
  };
  vm.runInNewContext(source, {
    window,
    document,
    URL,
    console: { info() {}, warn: (...args) => errors.push(args), error: (...args) => errors.push(args) },
    requestAnimationFrame: (callback) => callback(),
    fetch: () => { throw new Error('Fixture must use inline data without network requests'); }
  }, { filename: 'bc-product-switcher.js' });
  assert.equal(element.dataset.bcProductSwitcherV2Initialized, 'true');
  assert.equal(element.hidden, false);
  return {
    dom,
    document,
    element,
    navigations,
    errors,
    button: (field, value) => Array.from(element.querySelectorAll('button[data-switch-field]'))
      .find((node) => node.dataset.switchField === field && node.dataset.switchValue === value),
    close: () => dom.window.close()
  };
}

function check(name, test) {
  try {
    test();
    results.push({ name, passed: true });
  } catch (error) {
    results.push({ name, passed: false, error: error.stack });
  }
}

check('Reproduces old wrong-shape thumbnail and selects the exact current round product after the fix', () => {
  const fixture = clone(fixtures.shower);
  const current = fixture.group.products.find((product) => product.handle === fixture.handle);
  const wrong = fixture.group.products.find((product) => product.handle === 'fabriecio-bc-2014');
  const old = render(before, fixture);
  const next = render(after, fixture);
  try {
    assert.notEqual(current.swatch_url, wrong.swatch_url);
    assert.equal(old.button('kleur', 'Brushed Copper').querySelector('img').src, wrong.swatch_url);
    assert.equal(next.button('kleur', 'Brushed Copper').querySelector('img').src, current.swatch_url);
    for (const color of fixture.group.menus.find((menu) => menu.key === 'kleur').values) {
      const target = fixture.group.products.find((product) => product.options.kleur === color && product.options.maat === '20cm' && product.options.uitvoering === 'Plafond' && product.options.vorm === 'Rond');
      assert.equal(next.button('kleur', color).querySelector('img').src, target.swatch_url);
    }
  } finally { old.close(); next.close(); }
});

check('Shows all six color buttons with translated visible and accessible labels, without an extra expander', () => {
  const next = render(after, clone(fixtures.shower));
  try {
    const colors = Array.from(next.element.querySelectorAll('.bc-hotbath-swatch'));
    assert.equal(colors.length, 6);
    assert.equal(colors.filter((button) => !button.hidden).length, 6);
    assert.equal(next.element.querySelector('.bc-hotbath-colors__toggle'), null);
    assert.equal(next.button('kleur', 'Brushed Copper').getAttribute('aria-label'), 'Geborsteld koper');
    assert.equal(next.button('kleur', 'Brushed Copper').dataset.switchValue, 'Brushed Copper');
    assert.equal(next.button('kleur', 'Brushed Copper').getAttribute('aria-pressed'), 'true');
    assert.equal(next.element.querySelector('[data-hotbath-selected-color]').textContent, 'Geborsteld koper');
  } finally { next.close(); }
});

check('Orders complete-set menus clearly and sorts sizes while keeping their raw identities', () => {
  const fixture = clone(fixtures.shower);
  fixture.group.menus.find((menu) => menu.key === 'maat').values = ['30cm', '20cm', '25cm'];
  const next = render(after, fixture);
  try {
    assert.deepEqual(Array.from(next.element.querySelectorAll('[data-switcher-group]')).map((node) => node.dataset.switcherGroup), ['kleur', 'vorm', 'uitvoering', 'maat']);
    assert.deepEqual(Array.from(next.element.querySelectorAll('.bc-buybox__option-label')).map((node) => node.textContent), [
      'Kleur: Geborsteld koper', 'Vorm doucheset', 'Bevestiging hoofddouche', 'Formaat hoofddouche'
    ]);
    const buttons = Array.from(next.element.querySelectorAll('button[data-switch-field="maat"]'));
    assert.deepEqual(buttons.map((node) => node.dataset.switchValue), ['20cm', '25cm', '30cm']);
    assert.deepEqual(buttons.map((node) => node.querySelector('.bc-buybox__option-text').textContent), ['20 cm', '25 cm', '30 cm']);
    assert.equal(next.button('uitvoering', 'Muur').querySelector('.bc-buybox__option-text').textContent, 'Wand');
    assert.equal(next.button('uitvoering', 'Muur').dataset.switchValue, 'Muur');
  } finally { next.close(); }
});

for (const [field, value, handle] of [
  ['maat', '25cm', 'fabriecio-bc-2009'],
  ['kleur', 'Chroom', 'fabriecio-ckk-2010'],
  ['vorm', 'Vierkant', 'fabriecio-bc-2014'],
  ['uitvoering', 'Muur', 'fabriecio-bc-2005']
]) {
  check(`Changing only ${field}=${value} opens its exact product and retains preview context`, () => {
    const next = render(after, clone(fixtures.shower), {
      url: `https://badkamercity.nl/products/${fixtures.shower.handle}?preview_theme_id=196341825802&_fd=0&pb=0&_ab=0&_sc=1&utm_source=test`
    });
    try {
      next.button(field, value).click();
      assert.equal(next.navigations.length, 1);
      const url = new URL(next.navigations[0]);
      assert.equal(url.origin, 'https://badkamercity.nl');
      assert.equal(url.pathname, `/products/${handle}`);
      assert.equal(url.searchParams.get('preview_theme_id'), '196341825802');
      for (const key of ['_fd', 'pb', '_ab']) assert.equal(url.searchParams.get(key), '0');
      assert.equal(url.searchParams.get('_sc'), '1');
      assert.equal(url.searchParams.has('utm_source'), false);
      assert.equal(next.document.querySelector('.product-form__submit').disabled, true);
      assert.equal(next.element.getAttribute('aria-busy'), 'true');
    } finally { next.close(); }
  });
}

check('Unavailable color combination remains disabled instead of silently changing shape', () => {
  const fixture = clone(fixtures.shower);
  const gold = fixture.group.products.find((product) => product.options.kleur === 'Brushed Gold');
  gold.options.vorm = 'Vierkant';
  const next = render(after, fixture);
  try {
    const button = next.button('kleur', 'Brushed Gold');
    assert.equal(button.hidden, false);
    assert.equal(button.disabled, true);
    assert.equal(button.getAttribute('aria-disabled'), 'true');
    assert.equal(button.querySelector('img'), null);
    button.click();
    assert.equal(next.navigations.length, 0);
    assert.equal(next.button('vorm', 'Rond').getAttribute('aria-pressed'), 'true');
  } finally { next.close(); }
});

check('Ambiguous matching products cannot navigate and do not pick an arbitrary thumbnail', () => {
  const fixture = clone(fixtures.shower);
  const extra = clone(fixture.group.products.find((product) => product.options.kleur === 'Chroom'));
  extra.handle = 'test-duplicate-chrome';
  extra.url = '/products/test-duplicate-chrome';
  fixture.group.products.push(extra);
  const next = render(after, fixture);
  try {
    assert.equal(next.button('kleur', 'Chroom').querySelector('img'), null);
    next.button('kleur', 'Chroom').click();
    assert.equal(next.navigations.length, 0);
    assert.match(next.element.querySelector('[role="status"]').textContent, /combinatie kan niet/);
    assert.equal(next.document.querySelector('.product-form__submit').disabled, false);
  } finally { next.close(); }
});

check('Clickwaste displays clear overflow choices and keeps Ja/Nee routing identities', () => {
  const next = render(after, clone(fixtures.clickwaste), { context: '' });
  try {
    assert.equal(next.button('overloop', 'Ja').querySelector('.bc-buybox__option-text').textContent, 'Met overloop');
    assert.equal(next.button('overloop', 'Nee').querySelector('.bc-buybox__option-text').textContent, 'Zonder overloop');
    next.button('overloop', 'Nee').click();
    assert.deepEqual(next.navigations, ['https://badkamercity.nl/products/fabriecio-clw-6002']);
  } finally { next.close(); }
});

check('Compound dimensions and decimal sizes sort numerically and are formatted for display only', () => {
  const sizes = ['120x90cm', '90x90cm', '80x80cm', '100×100cm'];
  const fixture = {
    handle: 'test-size-0',
    group: {
      id: 'test-measurements',
      menus: [{ key: 'maat', label: 'Maat', order: 1, values: sizes }],
      products: sizes.map((value, index) => ({ handle: `test-size-${index}`, url: `/products/test-size-${index}`, options: { maat: value }, sort_order: index }))
    }
  };
  const next = render(after, fixture, { context: '' });
  try {
    const buttons = Array.from(next.element.querySelectorAll('button[data-switch-field="maat"]'));
    assert.deepEqual(buttons.map((node) => node.dataset.switchValue), ['80x80cm', '90x90cm', '100×100cm', '120x90cm']);
    assert.deepEqual(buttons.map((node) => node.querySelector('.bc-buybox__option-text').textContent), ['80 × 80 cm', '90 × 90 cm', '100 × 100 cm', '120 × 90 cm']);
    buttons[0].click();
    assert.deepEqual(next.navigations, ['https://badkamercity.nl/products/test-size-2']);
  } finally { next.close(); }
  const decimalFixture = clone(fixture);
  decimalFixture.group.menus[0].values = ['2,5cm', '2,11cm', '10cm'];
  decimalFixture.group.products = decimalFixture.group.menus[0].values.map((value, index) => ({ handle: `test-size-${index}`, url: `/products/test-size-${index}`, options: { maat: value } }));
  const decimal = render(after, decimalFixture, { context: '' });
  try {
    assert.deepEqual(Array.from(decimal.element.querySelectorAll('button[data-switch-field="maat"]')).map((node) => node.dataset.switchValue), ['2,11cm', '2,5cm', '10cm']);
  } finally { decimal.close(); }
});

check('Standalone shower heads receive their own context labels, without mounting or set labels', () => {
  const fixture = clone(fixtures.shower);
  fixture.group.menus = fixture.group.menus.filter((menu) => menu.key !== 'uitvoering');
  fixture.group.products = fixture.group.products.filter((product) => product.options.uitvoering === 'Plafond');
  const next = render(after, fixture, { context: 'shower_head' });
  try {
    assert.deepEqual(Array.from(next.element.querySelectorAll('.bc-buybox__option-label')).map((node) => node.textContent), ['Kleur: Geborsteld koper', 'Vorm hoofddouche', 'Formaat hoofddouche']);
  } finally { next.close(); }
});

check('Inbouwbox or other color-only product keeps a single color menu', () => {
  const fixture = clone(fixtures.shower);
  fixture.group.menus = fixture.group.menus.filter((menu) => menu.key === 'kleur');
  fixture.group.products = fixture.group.products.filter((product) => product.options.maat === '20cm' && product.options.vorm === 'Rond' && product.options.uitvoering === 'Plafond');
  const next = render(after, fixture, { context: '' });
  try {
    assert.deepEqual(Array.from(next.element.querySelectorAll('[data-switcher-group]')).map((node) => node.dataset.switcherGroup), ['kleur']);
  } finally { next.close(); }
});

check('English translations change only the visible labels, not the raw selections', () => {
  const next = render(after, clone(fixtures.shower), { locale: 'en.default' });
  try {
    assert.deepEqual(Array.from(next.element.querySelectorAll('.bc-buybox__option-label')).map((node) => node.textContent), ['Color: Brushed copper', 'Shower set shape', 'Shower head mounting', 'Shower head size']);
    assert.equal(next.button('uitvoering', 'Muur').querySelector('.bc-buybox__option-text').textContent, 'Wall');
    next.button('uitvoering', 'Muur').click();
    assert.deepEqual(next.navigations, ['https://badkamercity.nl/products/fabriecio-bc-2005']);
  } finally { next.close(); }
});

check('Malformed optional display labels fall back to the original data without breaking navigation', () => {
  const next = render(after, clone(fixtures.shower), { labels: '{invalid' });
  try {
    assert.equal(next.button('kleur', 'Brushed Copper').getAttribute('aria-label'), 'Brushed Copper');
    next.button('maat', '25cm').click();
    assert.deepEqual(next.navigations, ['https://badkamercity.nl/products/fabriecio-bc-2009']);
  } finally { next.close(); }
});

check('Active cart submission still blocks a product switch', () => {
  const next = render(after, clone(fixtures.shower));
  try {
    next.document.querySelector('.product-form__submit').setAttribute('aria-busy', 'true');
    next.button('maat', '25cm').click();
    assert.equal(next.navigations.length, 0);
    assert.equal(next.button('maat', '20cm').getAttribute('aria-pressed'), 'true');
    assert.match(next.element.querySelector('[role="status"]').textContent, /Wacht tot/);
  } finally { next.close(); }
});

for (const [name, fixture, options] of [
  ['Hotbath compact switcher', fixtures.hotbath, { scoped: false, hotbath: true }],
  ['Other compact-color brand', fixtures.shower, { scoped: false }],
  ['Generic unscoped preview navigation', fixtures.shower, { scoped: false, url: `https://badkamercity.nl/products/${fixtures.shower.handle}?preview_theme_id=196341825802` }]
]) {
  check(`${name} retains byte-identical rendered controls and the same destination behavior`, () => {
    const old = render(before, clone(fixture), options);
    const next = render(after, clone(fixture), options);
    try {
      assert.equal(next.element.innerHTML, old.element.innerHTML);
      const candidate = Array.from(old.element.querySelectorAll('button[data-switch-field]')).find((node) => !node.disabled && node.getAttribute('aria-pressed') !== 'true');
      assert.ok(candidate);
      const equivalent = next.button(candidate.dataset.switchField, candidate.dataset.switchValue);
      candidate.click();
      equivalent.click();
      assert.deepEqual(next.navigations, old.navigations);
      assert.equal(next.element.innerHTML, old.element.innerHTML);
    } finally { old.close(); next.close(); }
  });
}

const report = {
  verifiedAt: new Date().toISOString(),
  runtime: `Node ${process.version} with jsdom ${require('jsdom/package.json').version}`,
  runsActualSharedScript: true,
  noNetworkRequests: true,
  cssLayoutVerified: false,
  total: results.length,
  passed: results.filter((test) => test.passed).length,
  failed: results.filter((test) => !test.passed).length,
  results
};
if (process.env.VERLAVIO_TEST_OUTPUT) fs.writeFileSync(process.env.VERLAVIO_TEST_OUTPUT, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ total: report.total, passed: report.passed, failed: report.failed, failures: results.filter((test) => !test.passed) }, null, 2));
if (report.failed) process.exitCode = 1;
