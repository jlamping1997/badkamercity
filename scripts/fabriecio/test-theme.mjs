import fs from 'node:fs';
import assert from 'node:assert/strict';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(new URL('../component-audit/package.json', import.meta.url));
const { Window } = await import(require.resolve('happy-dom'));
const { Liquid } = await import(require.resolve('liquidjs'));
const theme = path.resolve(new URL('../../shopify/current/', import.meta.url).pathname);
const locale = name => JSON.parse(fs.readFileSync(path.join(theme, 'locales', name), 'utf8').replace(/^\s*\/\*[\s\S]*?\*\//, ''));
const locales = { nl: locale('nl.json'), en: locale('en.default.json') };
const engine = new Liquid({ strictFilters: true });
engine.registerFilter('json', value => JSON.stringify(value));
engine.registerFilter('asset_url', value => '/assets/' + value);
engine.registerFilter('stylesheet_tag', value => '<link rel="stylesheet" href="' + value + '">');
engine.registerFilter('t', key => key.split('.').reduce((value, part) => value?.[part], locales.nl) || key);
const snippet = name => fs.readFileSync(path.join(theme, 'snippets', name), 'utf8').replace(/{% doc %}[\s\S]*?{% enddoc %}/, '');
const choicesSnippet = snippet('bc-fabriecio-choices.liquid');
const deliverySnippet = snippet('bc-fabriecio-delivery.liquid');
const source = fs.readFileSync(path.join(theme, 'assets/bc-product-switcher.js'), 'utf8')
  .replace('function init(root = document)', 'window.TestSwitcher = BCProductSwitcherV2; function init(root = document)');
const family = {
  groups: [{
    id: 'fabriecio-malmo',
    menus: [
      { key: 'kleur', label: 'Kleur', order: 1, display_type: 'buttons', values: ['Wit', 'Mat Wit'] },
      { key: 'maat', label: 'Maat', order: 2, display_type: 'buttons', values: ['170×80cm', '180×85cm'] }
    ],
    products: [
      ['vsb-2001', 'Wit', '170×80cm'], ['vsb-2002', 'Wit', '180×85cm'],
      ['vsb-2003', 'Mat Wit', '170×80cm'], ['vsb-2004', 'Mat Wit', '180×85cm']
    ].map(([sku, kleur, maat], index) => ({
      handle: 'fabriecio-' + sku,
      url: '/products/fabriecio-' + sku,
      title: `Fabriecio Malmö ${maat} ${kleur}`,
      sort_order: index,
      options: { kleur, maat },
      swatch_url: `https://cdn.shopify.com/s/files/1/0941/7959/0410/files/${sku}.jpg`
    }))
  }]
};
const group = family.groups[0];
const currentProduct = (choice = group.products[0], data = family) => ({
  vendor: 'Fabriecio', handle: choice.handle, url: choice.url, variants: [{}],
  metafields: { custom: { fabriecio_choices: { value: data } } }
});
const renderChoices = product => engine.parseAndRender(choicesSnippet, { product, section: { id: 'fabriecio-test' } });
let transitions = 0;
for (const vendor of ['Fabriecio', 'Verlavio']) {
for (const choice of group.products) {
  const rendered = await renderChoices({ ...currentProduct(choice), vendor });
  assert.match(rendered, /data-bc-compact-colors="true"/);
  assert.match(rendered, /data-bc-preserve-position="true"/);
  assert.match(rendered, /bc-hotbath-swatches\.css/);
  assert.match(rendered, /aria-current="page"/);
  const inline = rendered.match(/<script type="application\/json" data-bc-switcher-inline>([\s\S]*?)<\/script>/);
  assert.deepEqual(JSON.parse(inline[1]), family);
  for (const menu of group.menus) {
    for (const value of menu.values) {
      if (value === choice.options[menu.key]) continue;
      const expected = group.products.find(target => group.menus.every(field =>
        target.options[field.key] === (field.key === menu.key ? value : choice.options[field.key])));
      assert(expected);
      const window = new Window({ url: 'https://badkamercity.nl' + choice.url });
      window.console.info = () => {};
      window.matchMedia = () => ({ matches: false, addEventListener() {}, removeEventListener() {} });
      window.eval(source);
      const root = window.document.createElement('div');
      Object.assign(root.dataset, { switchGroup: group.id, productHandle: choice.handle, productUrl: choice.url,
        sectionId: 'fabriecio-test', bcCompactColors: 'true' });
      window.document.body.append(root);
      new window.TestSwitcher(root, family);
      const selectedColor = root.querySelector('.bc-hotbath-swatch.is-active');
      assert(selectedColor && selectedColor.getAttribute('aria-label') === choice.options.kleur);
      assert.equal(root.querySelectorAll('.bc-hotbath-swatch__surface img').length, 2);
      const button = [...root.querySelectorAll('button[data-switch-field]')].find(element =>
        element.dataset.switchField === menu.key && element.dataset.switchValue === value);
      assert(button && !button.disabled);
      button.click();
      assert.equal(window.location.pathname, expected.url);
      transitions++;
      await window.happyDOM.close();
    }
  }
}
}
const blocked = [
  { ...currentProduct(), vendor: 'Hotbath' },
  { ...currentProduct(), variants: [{}, {}] },
  { ...currentProduct(), handle: 'not-in-group' }
];
for (const product of blocked) assert(!((await renderChoices(product)).includes('data-bc-product-switcher-v2')));
for (const mutate of [
  data => { data.groups[0].products[0].url = 'https://example.invalid/products/another'; },
  data => { data.groups[0].products[0].url = '/products/wrong-handle'; },
  data => { data.groups[0].products.push(data.groups[0].products[0]); },
  data => { data.groups[0].menus = []; },
  data => { data.groups[0].id = ''; }
]) {
  const data = structuredClone(family);
  mutate(data);
  assert(!((await renderChoices(currentProduct(group.products[0], data))).includes('data-bc-product-switcher-v2')));
}
const escapedData = structuredClone(family);
escapedData.groups[0].products[0].title = '</script><script>alert(1)</script>';
const escaped = await renderChoices(currentProduct(group.products[0], escapedData));
assert(!escaped.includes('<script>alert(1)</script>'));
assert.deepEqual(JSON.parse(escaped.match(/data-bc-switcher-inline>([\s\S]*?)<\/script>/)[1]), escapedData);
const largeFamily = structuredClone(family);
largeFamily.groups[0].menus = [{ key: 'maat', label: 'Maat', order: 1, display_type: 'dropdown' }];
largeFamily.groups[0].products = Array.from({ length: 72 }, (_, index) => ({
  handle: 'fabriecio-large-' + index,
  url: '/products/fabriecio-large-' + index,
  title: 'Fabriecio product ' + index,
  options: { maat: String(index) },
  sort_order: index
}));
const largeCurrent = largeFamily.groups[0].products.at(-1);
const largeRendered = await renderChoices(currentProduct(largeCurrent, largeFamily));
assert.match(largeRendered, /data-bc-product-switcher-v2/);
assert.equal([...largeRendered.matchAll(/<li><a href=/g)].length, 72);
assert.equal(JSON.parse(largeRendered.match(/data-bc-switcher-inline>([\s\S]*?)<\/script>/)[1]).groups[0].products.length, 72);
largeFamily.groups[0].products.at(-1).url = 'https://example.invalid/last-item';
assert(!((await renderChoices(currentProduct(largeCurrent, largeFamily))).includes('data-bc-product-switcher-v2')));
const sparse = structuredClone(family);
sparse.groups[0].products.pop();
const window = new Window({ url: 'https://badkamercity.nl' + group.products[2].url });
window.console.info = () => {};
window.matchMedia = () => ({ matches: false, addEventListener() {}, removeEventListener() {} });
window.eval(source);
const root = window.document.createElement('div');
Object.assign(root.dataset, { switchGroup: group.id, productHandle: group.products[2].handle,
  productUrl: group.products[2].url, sectionId: 'sparse', bcCompactColors: 'true' });
window.document.body.append(root);
new window.TestSwitcher(root, sparse);
const absentSize = [...root.querySelectorAll('button[data-switch-field="maat"]')].find(button =>
  button.dataset.switchValue === '180×85cm');
assert(absentSize?.disabled);
assert.equal(window.location.pathname, group.products[2].url);
await window.happyDOM.close();
const delivery = async (value, legacy, vendor = 'Fabriecio') => engine.parseAndRender(deliverySnippet, {
  product: { vendor, metafields: { custom: { fabriecio_delivery: { value }, leverancier_voorraad: { value: legacy } } } }
});
assert.match(await delivery({ in_stock: true, expected_text: 'Verwacht: Week 28' }), /Op voorraad bij leverancier/);
assert(!(await delivery({ in_stock: true, expected_text: 'Verwacht: Week 28' })).includes('Week 28'));
const expected = await delivery({ in_stock: false, expected_text: 'Verwacht: Week 50' });
assert.match(expected, /Verwacht bij leverancier/);
assert.match(expected, /Verwacht: Week 50/);
assert.match(await delivery({ in_stock: false, expected_text: '' }), /Levertijd op aanvraag/);
assert.match(await delivery({ in_stock: null, expected_text: null }), /Levertijd op aanvraag/);
assert.match(await delivery(undefined, true), /Op voorraad bij leverancier/);
assert.match(await delivery({ in_stock: false, expected_text: '' }, true), /Levertijd op aanvraag/);
assert.equal((await delivery({ in_stock: true }, true, 'Hotbath')).trim(), '');
assert(!(await delivery({ in_stock: false, expected_text: '<img src=x onerror=alert(1)>' })).includes('<img'));
assert.match(await delivery({ in_stock: true }, false, 'Verlavio'), /Op voorraad bij leverancier/);
assert.match(await delivery({ in_stock: false, expected_text: 'Verwacht: Week 50' }, false, 'Verlavio'), /Week 50/);
assert.match(await delivery({ in_stock: false, discontinued: true }, false, 'Verlavio'), /Niet meer leverbaar/);
const discontinued = await delivery({ in_stock: true, expected_text: 'Verwacht: Week 50', discontinued: true }, true);
assert.match(discontinued, /Niet meer leverbaar/);
assert(!discontinued.includes('Op voorraad bij leverancier'));
assert(!discontinued.includes('Week 50'));
assert(!discontinued.includes('Levertijd op aanvraag'));
for (const dictionary of Object.values(locales)) {
  assert(dictionary.bc_delivery.supplier_expected);
  assert(dictionary.bc_delivery.discontinued);
}
const section = fs.readFileSync(path.join(theme, 'sections/main-product.liquid'), 'utf8');
assert.match(section, /if bc_fabriecio_supplier_product[\s\S]*?render 'bc-fabriecio-delivery'[\s\S]*?elsif bc_delivery_vendor == 'wiesbaden'/);
assert.match(section, /bc_mobile_vendor == 'fabriecio' or bc_mobile_vendor == 'verlavio'/);
assert.match(section, /bc_fabriecio_supplier_product and product\.metafields\.custom\.fabriecio_choices\.value != blank/);
const outputGate = section.match(/\{%- if bc_hotbath_menu_excluded == false and bc_hotbath_menu_disabled == false -%\}[\s\S]*?\{\{ bc_buybox_options_markup \}\}[\s\S]*?\{%- endif -%\}\s*\{%- endif -%\}/)?.[0];
assert(outputGate, 'Read the actual final buybox output gate from the product section');
const singleSku = { ...currentProduct(), has_only_default_variant: true };
const outputContext = {
  product: singleSku,
  current_switch_group: '', current_group: '',
  bc_hotbath_menu_excluded: false, bc_hotbath_menu_disabled: false,
  bc_buybox_options_markup: await renderChoices(singleSku)
};
assert.match(await engine.parseAndRender(outputGate, outputContext), /data-bc-product-switcher-v2/,
  'A default single-SKU Fabriecio product without legacy groups displays the captured choices');
assert.match(await engine.parseAndRender(outputGate, { ...outputContext, product: { ...singleSku, vendor: 'Verlavio' } }), /data-bc-product-switcher-v2/);
const noChoices = { ...singleSku, metafields: { custom: {} } };
assert.equal((await engine.parseAndRender(outputGate, { ...outputContext, product: noChoices })).trim(), '');
for (const flag of ['bc_hotbath_menu_excluded', 'bc_hotbath_menu_disabled']) {
  assert.equal((await engine.parseAndRender(outputGate, { ...outputContext, [flag]: true })).trim(), '');
}
assert.match(await engine.parseAndRender(outputGate, { ...outputContext,
  product: { ...noChoices, has_only_default_variant: false } }), /data-bc-product-switcher-v2/,
  'The existing native-variant condition still displays its captured markup');
console.log(JSON.stringify({ products: 8, supportedBrands: 2, transitions, sparseCombinationDisabled: 'PASS',
  actualSingleSkuFinalOutputGateAndExistingExclusionGuards: 'PASS',
  seventyTwoProductValidationAndNoScriptLinks: 'PASS',
  invalidBrandVariantCurrentDestinationAndDuplicateHandleGuards: 'PASS', inlineJsonEscaping: 'PASS',
  deliveryCases: 12, discontinuedPriority: 'PASS', supplierStockFallbackAndStaleExpectationHidden: 'PASS',
  liveBrowserMobileAndCart: 'NOT_TESTED' }));
