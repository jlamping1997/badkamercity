const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const source = fs.readFileSync(path.join(__dirname, '../assets/bc-external-filters.js'), 'utf8');
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
async function fixture() {
  const dom = new JSDOM(`<div class="bc-collection"><div id="BcExternalFilters" data-api-base="https://example.test/verified" data-collection="wastafelkranen" data-products-count="1"></div><div class="facets-vertical"><aside id="main-collection-filters">Native filters</aside><facet-filters-form class="facets-vertical-sort"></facet-filters-form><div id="ProductGridContainer"><ul id="product-grid"><li id="native-product">Native product</li></ul><div class="pagination-wrapper">Native pages</div></div></div></div>`, { url: 'https://example.test/collections/wastafelkranen?bcfilters=1', runScripts: 'outside-only' });
  const w = dom.window;
  const calls = [];
  let fail = false;
  let count = 1;
  let nativeHistoryEvents = 0;
  w.addEventListener('popstate', () => { nativeHistoryEvents += 1; });
  w.console.error = () => {};
  w.fetch = async (url, options) => {
    calls.push(JSON.parse(options.body));
    if (fail) throw new Error('API unavailable');
    return { ok: true, json: async () => ({ found: 1, collection: { profile_products: count }, products: [{ handle: 'kraan', title: 'Kraan', price_cents: 16400 }], facets: [
      { field: 'price_cents', label: 'Prijs', type: 'number_decimal', data_type: 'int64', unit: 'cent', min: 1000, max: 20000 },
      { field: 'f_met_hoofddouche', label: 'Met hoofddouche', type: 'string', data_type: 'bool', values: [{ value: 'true', count: 1 }, { value: 'false', count: 0 }] },
      { field: 'f_aantal_grepen', label: 'Aantal grepen', type: 'number_decimal', data_type: 'int32', min: 1, max: 2 }
    ] }) };
  };
  const native = w.document.querySelector('#native-product');
  w.eval(source);
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  await flush();
  return { dom, w, calls, native, nativeHistoryEvents: () => nativeHistoryEvents, fail: () => { fail = true; }, mismatch: () => { count = 2; } };
}
test('Euro input sends integer cents and displays euro chips', async () => {
  const f = await fixture();
  try {
    const input = f.w.document.querySelector('[data-range-field="price_cents"][data-range-kind="max"]');
    assert.equal(input.placeholder, '200');
    assert.match(input.closest('details').textContent, /Prijs \(€\)/);
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
for (const kind of ['fail', 'mismatch']) {
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
