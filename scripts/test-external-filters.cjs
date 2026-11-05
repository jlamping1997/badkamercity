const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const source = fs.readFileSync(path.join(__dirname, '../shopify/current/assets/bc-external-filters.js'), 'utf8');
const flush = () => new Promise((resolve) => setImmediate(resolve));
test('Quick edits to both range bounds preserve both values', async () => {
  const f = await fixture();
  try {
    for (const [kind, value] of [['min', '100'], ['max', '200']]) {
      const input = f.w.document.querySelector(`[data-range-field="price_cents"][data-range-kind="${kind}"]`);
      input.value = value;
      input.dispatchEvent(new f.w.Event('input', { bubbles: true }));
    }
    await new Promise((resolve) => setTimeout(resolve, 350));
    await flush();
    assert.deepEqual(f.calls.at(-1).ranges.price_cents, { min: 10000, max: 20000 });
  } finally { f.dom.window.close(); }
});
async function fixture(searchMode = false, shortTitle = null, options = {}) {
  const dom = new JSDOM(`<div class="bc-collection"><div id="BcExternalFilters" data-api-base="https://example.test/verified" data-collection="wastafelkranen" data-products-count="1"></div><div class="facets-vertical"><aside id="main-collection-filters">Native filters</aside><facet-filters-form class="facets-vertical-sort"></facet-filters-form><div id="ProductGridContainer"><ul id="product-grid"><li id="native-product">Native product</li></ul><div class="pagination-wrapper">Native pages</div></div></div></div>`, { url: 'https://example.test/collections/wastafelkranen', runScripts: 'outside-only', pretendToBeVisual: true });
  if (searchMode) {
    dom.reconfigure({ url: 'https://example.test/search?q=wastafelkraan&options%5Bprefix%5D=last' });
    const root = dom.window.document.querySelector('#BcExternalFilters');
    root.closest('.bc-collection').className = 'template-search';
    root.dataset.searchMode = 'true';
    root.dataset.collection = '__all__';
    root.dataset.productsCount = '';
    dom.window.document.querySelector('#main-collection-filters').id = 'main-search-filters';
    dom.window.document.querySelector('facet-filters-form').className = 'template-search__toolbar';
    if (options.nativeResults !== false) dom.window.document.querySelector('#native-product').className = options.nativeClass || 'bc-search-card';
  }
  if (options.url) dom.reconfigure({ url: options.url });
  if (shortTitle !== null) dom.window.document.querySelector('#BcExternalFilters').dataset.cardDataSection = 'bc-card-data';
  const w = dom.window;
  w.matchMedia = () => ({ matches: false, addEventListener() {}, removeEventListener() {} });
  const calls = [];
  let fail = false;
  let httpFailure = false;
  let count = 1;
  let found = options.found ?? 1;
  let nativeHistoryEvents = 0;
  w.addEventListener('popstate', () => { nativeHistoryEvents += 1; });
  w.console.error = () => {};
  w.fetch = async (url, options) => {
    if (!options.body) return { ok: true, json: async () => ({ 'bc-card-data': `<script data-bc-card-data type="application/json">${JSON.stringify({ id: '123', title: 'Kraan', short_title: shortTitle }).replaceAll('<', '\\u003c')}</script>` }) };
    calls.push(JSON.parse(options.body));
    if (fail) throw new Error('API unavailable');
    if (httpFailure) return { ok: false, status: 503 };
    return { ok: true, json: async () => ({ found, collection: { handle: searchMode ? '__all__' : 'wastafelkranen', profile_products: count }, products: found ? [{ id: '123', shopify_product_id: 'gid://shopify/Product/123', handle: 'kraan', title: 'Kraan', price_cents: 16400 }] : [], facets: [
      { field: 'price_cents', label: 'Prijs', type: 'number_decimal', data_type: 'int64', unit: 'cent', min: 1000, max: 20000 },
      { field: 'f_met_hoofddouche', label: 'Met hoofddouche', type: 'string', data_type: 'bool', values: [{ value: 'true', count: 1 }, { value: 'false', count: 0 }] },
      { field: 'f_aantal_grepen', label: 'Aantal grepen', type: 'number_decimal', data_type: 'int32', min: 1, max: 2 }
    ] }) };
  };
  const native = w.document.querySelector('#native-product');
  w.eval(source);
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  await flush();
  return { dom, w, calls, native, nativeHistoryEvents: () => nativeHistoryEvents, fail: () => { fail = true; }, httpFail: () => { httpFailure = true; }, mismatch: () => { count = 2; }, empty: () => { found = 0; } };
}
test('Euro input sends integer cents and displays euro chips', async () => {
  const f = await fixture();
  try {
    const input = f.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]');
    assert.equal(input.placeholder, '200');
    assert.equal(input.closest('details').querySelector('summary').textContent, 'Prijs');
    assert.match(input.parentElement.textContent, /Tot \(€\)/);
    input.value = '200';
    input.dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    assert.equal(f.calls.at(-1).ranges.price_cents.max, 20000);
    assert.match(f.w.document.querySelector('.bc-filter-active').textContent, /€\s*200,00/);
    assert.equal(f.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]').value, '200');
  } finally { f.dom.window.close(); }
});
test('Boolean choices and chips use Ja/Nee while requests retain true/false', async () => {
  const f = await fixture();
  try {
    const checkbox = f.w.document.querySelector('[data-filter-field="f_met_hoofddouche"][value="true"]');
    assert.match(checkbox.parentElement.textContent, /Ja/);
    checkbox.checked = true;
    checkbox.dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    assert.deepEqual(f.calls.at(-1).filters.f_met_hoofddouche, ['true']);
    assert.match(f.w.document.querySelector('.bc-filter-active').textContent, /Met hoofddouche: Ja/);
  } finally { f.dom.window.close(); }
});
test('Fractional counts do not reach the API', async () => {
  const f = await fixture();
  try {
    const input = f.w.document.querySelector('[data-range-field="f_aantal_grepen"][data-range-kind="max"]');
    assert.equal(input.step, '1');
    const before = f.calls.length;
    input.value = '1.5';
    input.dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    assert.equal(f.calls.length, before);
  } finally { f.dom.window.close(); }
});
test('A refresh preserves open groups and an unfinished price edit', async () => {
  const f = await fixture();
  try {
    const input = f.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]');
    input.focus();
    input.value = '200';
    input.dispatchEvent(new f.w.Event('input', { bubbles: true }));
    const group = f.w.document.querySelector('[data-filter-group="f_met_hoofddouche"]');
    group.open = false;
    const checkbox = f.w.document.querySelector('[data-filter-field="f_met_hoofddouche"][value="true"]');
    checkbox.checked = true;
    checkbox.dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    const replacement = f.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]');
    assert.equal(replacement.value, '200');
    assert.equal(f.w.document.activeElement, replacement);
    assert.equal(f.w.document.querySelector('[data-filter-group="f_met_hoofddouche"]').open, false);
  } finally { f.dom.window.close(); }
});
test('Typing a price commits even when another filter refresh replaces the input', async () => {
  const f = await fixture();
  try {
    const input = f.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]');
    input.focus();
    input.value = '200';
    input.dispatchEvent(new f.w.Event('input', { bubbles: true }));
    f.w.document.querySelector('#BcFilterSort').dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await new Promise((resolve) => setTimeout(resolve, 350));
    await flush();
    assert.equal(f.calls.at(-1).ranges.price_cents.max, 20000);
    assert.equal(new URL(f.w.location.href).searchParams.get('bcr_price_cents_max'), '20000');
  } finally { f.dom.window.close(); }
});
for (const kind of ['fail', 'httpFail', 'mismatch']) {
  test(`${kind} restores the original product nodes and native controls`, async () => {
    const f = await fixture();
    try {
      assert.ok(f.w.document.documentElement.classList.contains('bc-external-filters-active'));
      f[kind]();
      f.w.document.querySelector('#BcFilterSort').dispatchEvent(new f.w.Event('change', { bubbles: true }));
      await flush();
      assert.equal(f.w.document.querySelector('#native-product'), f.native);
      assert.equal(f.w.document.querySelector('#main-collection-filters').style.display, '');
      assert.ok(!f.w.document.documentElement.classList.contains('bc-external-filters-active'));
      assert.equal(f.w.document.querySelector('.bc-filter-error').hidden, false);
    } finally { f.dom.window.close(); }
  });
}
test('External browser history prevents the native renderer replacing the grid', async () => {
  const f = await fixture();
  try {
    f.w.dispatchEvent(new f.w.PopStateEvent('popstate'));
    await flush();
    assert.equal(f.nativeHistoryEvents(), 0);
    assert.equal(f.w.document.querySelector('.bc-filter-card__title').textContent.trim(), 'Kraan');
  } finally { f.dom.window.close(); }
});
test('Native browser history stays available after external fallback', async () => {
  const f = await fixture();
  try {
    f.fail();
    f.w.document.querySelector('#BcFilterSort').dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    f.w.dispatchEvent(new f.w.PopStateEvent('popstate'));
    await flush();
    assert.equal(f.nativeHistoryEvents(), 1);
  } finally { f.dom.window.close(); }
});

test('Search passes the query to the global verified profile and keeps it while filtering', async () => {
  const f = await fixture(true);
  try {
    assert.equal(f.calls[0].collection, '__all__');
    assert.equal(f.calls[0].q, 'wastafelkraan');
    assert.equal(f.w.document.querySelector('#main-search-filters').style.display, 'none');
    const input = f.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]');
    input.value = '200';
    input.dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    assert.equal(f.calls.at(-1).q, 'wastafelkraan');
    assert.equal(new URL(f.w.location.href).searchParams.get('q'), 'wastafelkraan');
    assert(f.w.document.querySelector('#product-grid > ul > li .bc-filter-card'));
    f.fail();
    f.w.document.querySelector('#BcFilterSort').dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    assert.equal(f.w.document.querySelector('#native-product'), f.native);
    assert.equal(f.w.document.querySelector('#main-search-filters').style.display, '');
  } finally { f.dom.window.close(); }
});
test('External cards read current short titles from Shopify and escape markup', async () => {
  const f = await fixture(true, 'BadkamerCity kraan <img onerror=alert(1)>');
  try {
    await flush();
    assert.equal(f.w.document.querySelector('.bc-filter-card__title a').textContent, 'BadkamerCity kraan <img onerror=alert(1)>');
    assert(!f.w.document.querySelector('.bc-filter-card__title img'));
    assert.equal(f.w.document.querySelector('.bc-filter-card__title a').title, 'Kraan');
  } finally { f.dom.window.close(); }
});

for (const query of ['verlavio', 'VSB_2001', 'nieuw-merk']) {
  test(`An empty external search preserves real Shopify results for ${query}`, async () => {
    const f = await fixture(true, null, { found: 0, url: `https://example.test/search?q=${query}` });
    try {
      assert.equal(f.w.document.querySelector('#native-product'), f.native);
      assert.equal(f.w.document.querySelector('#main-search-filters').style.display, '');
      assert.ok(!f.w.document.documentElement.classList.contains('bc-external-filters-active'));
      assert.equal(f.w.document.querySelector('.bc-filter-toolbar').style.display, 'none');
      assert.equal(f.w.document.querySelector('.bc-filter-error').hidden, true);
    } finally { f.dom.window.close(); }
  });
}

test('An empty search without native product or article cards remains a valid empty result', async () => {
  const f = await fixture(true, null, { found: 0, nativeResults: false });
  try {
    assert.ok(f.w.document.documentElement.classList.contains('bc-external-filters-active'));
    assert.equal(f.w.document.querySelector('#native-product'), null);
    assert.equal(f.w.document.querySelector('[data-bc-count]').textContent, '0 producten');
  } finally { f.dom.window.close(); }
});

test('Native article results are retained when the product index returns zero', async () => {
  const f = await fixture(true, null, { found: 0, nativeClass: 'article-card-wrapper' });
  try {
    assert.equal(f.w.document.querySelector('#native-product'), f.native);
    assert.ok(!f.w.document.documentElement.classList.contains('bc-external-filters-active'));
  } finally { f.dom.window.close(); }
});

for (const parameters of ['bcf_f_kleur=zwart', 'bcr_price_cents_max=0', 'filter.p.vendor=Verlavio']) {
  test(`A legitimate filtered zero is retained with ${parameters}`, async () => {
    const f = await fixture(true, null, { found: 0, url: `https://example.test/search?q=wastafelkraan&${parameters}` });
    try {
      assert.ok(f.w.document.documentElement.classList.contains('bc-external-filters-active'));
      assert.equal(f.w.document.querySelector('#native-product'), null);
      assert.equal(f.w.document.querySelector('[data-bc-count]').textContent, '0 producten');
    } finally { f.dom.window.close(); }
  });
}

test('Removing the last filter restores native results when the index still returns zero', async () => {
  const f = await fixture(true);
  try {
    f.empty();
    const checkbox = f.w.document.querySelector('[data-filter-field="f_met_hoofddouche"][value="true"]');
    checkbox.checked = true;
    checkbox.dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    assert.ok(f.w.document.documentElement.classList.contains('bc-external-filters-active'));
    const replacement = f.w.document.querySelector('[data-filter-field="f_met_hoofddouche"][value="true"]');
    replacement.checked = false;
    replacement.dispatchEvent(new f.w.Event('change', { bubbles: true }));
    await flush();
    assert.equal(f.w.document.querySelector('#native-product'), f.native);
    assert.ok(!f.w.document.documentElement.classList.contains('bc-external-filters-active'));
  } finally { f.dom.window.close(); }
});

test('A different query in browser history cannot restore the original query result cards', async () => {
  const f = await fixture(true);
  try {
    f.empty();
    f.w.history.pushState({}, '', '/search?q=ander');
    f.w.dispatchEvent(new f.w.PopStateEvent('popstate'));
    await flush();
    assert.equal(f.calls.at(-1).q, 'ander');
    assert.equal(f.w.document.querySelector('#native-product'), null);
    assert.ok(f.w.document.documentElement.classList.contains('bc-external-filters-active'));
  } finally { f.dom.window.close(); }
});
