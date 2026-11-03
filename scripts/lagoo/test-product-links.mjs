import fs from 'node:fs';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(new URL('../component-audit/package.json', import.meta.url));
const { Window } = await import(require.resolve('happy-dom'));
const { Liquid } = await import(require.resolve('liquidjs'));
const inputs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const data = JSON.parse(inputs[0].metafields.find(m => m.key === 'lagoo_choices').value);
const group = data.groups[0];
const source = fs.readFileSync(new URL('../../shopify/current/assets/bc-product-switcher.js', import.meta.url), 'utf8')
  .replace('function init(root = document)', 'window.TestSwitcher = BCProductSwitcherV2; function init(root = document)');
let transitions = 0;
for (const product of group.products) {
  for (const menu of group.menus) {
    for (const value of new Set(group.products.map(p => p.options[menu.key]))) {
      if (value === product.options[menu.key]) continue;
      const expected = group.products.filter(p => group.menus.every(m =>
        p.options[m.key] === (m.key === menu.key ? value : product.options[m.key])));
      assert.equal(expected.length, 1);
      const window = new Window({ url: 'https://badkamercity.nl' + product.url });
      window.console.info = () => {};
      window.matchMedia = () => ({ matches: false, addEventListener() {}, removeEventListener() {} });
      window.eval(source);
      const root = window.document.createElement('div');
      Object.assign(root.dataset, { switchGroup: group.id, productHandle: product.handle,
        productUrl: product.url, sectionId: 'lagoo-test' });
      window.document.body.append(root);
      const instance = new window.TestSwitcher(root, data);
      const button = [...root.querySelectorAll('button[data-switch-field]')].find(b =>
        b.dataset.switchField === menu.key && b.dataset.switchValue === value);
      assert(button && !button.disabled);
      button.click();
      assert.equal(window.location.pathname, expected[0].url);
      assert.equal(window.location.search, '');
      const destination = inputs.find(p => p.handle === expected[0].handle);
      assert(destination);
      assert.equal(destination.variants.length, 1);
      assert.equal(destination.files.length, 1);
      assert.equal(destination.files[0].id, destination.variants[0].file.id);
      assert.equal(destination.variants[0].optionValues.find(v => v.optionName === 'Kleur').name,
        expected[0].options.kleur);
      transitions++;
      await window.happyDOM.close();
    }
  }
}
const liquid = new Liquid();
liquid.registerFilter('json', value => JSON.stringify(value));
liquid.registerFilter('asset_url', value => '/assets/' + value);
const snippet = fs.readFileSync(new URL('../../shopify/current/snippets/bc-lagoo-choices.liquid', import.meta.url), 'utf8')
  .replace(/{% doc %}[\s\S]*?{% enddoc %}/, '');
const product = { vendor: 'Lagoo', handle: group.products[0].handle, url: group.products[0].url,
  variants: [{}], metafields: { custom: { lagoo_choices: { value: data } } } };
const rendered = await liquid.parseAndRender(snippet, { product, section: { id: 'test' } });
assert(rendered.includes('data-bc-product-switcher-v2'));
const inline = rendered.match(/<script type="application\/json" data-bc-switcher-inline>([\s\S]*?)<\/script>/);
assert.deepEqual(JSON.parse(inline[1]), data);
for (const changed of [{ ...product, vendor: 'Hotbath' }, { ...product, variants: [{}, {}] },
  { ...product, handle: 'not-a-member' }]) {
  assert(!(await liquid.parseAndRender(snippet, { product: changed })).includes('data-bc-product-switcher-v2'));
}
const invalid = structuredClone(product);
invalid.metafields.custom.lagoo_choices.value.groups[0].products[0].url = 'https://example.invalid/products/other';
assert(!(await liquid.parseAndRender(snippet, { product: invalid })).includes('data-bc-product-switcher-v2'));
console.log(JSON.stringify({ products: inputs.length, transitions, snippetRendering: 'PASS',
  incorrectBrandMultipleVariantsUnknownProductInvalidUrl: 'PASS', actualBrowser: 'NOT_TESTED' }));
