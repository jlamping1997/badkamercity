import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';

const { values: args } = parseArgs({ options: {
  plan: { type: 'string' }, source: { type: 'string' }, output: { type: 'string' }
} });
if (!args.plan || !args.source) {
  throw new Error('Usage: node scripts/fabriecio/test-plan.mjs --plan PLAN.json --source normalized-catalog.json [--output REPORT.json]');
}
const require = createRequire(new URL('../component-audit/package.json', import.meta.url));
const { Window } = await import(require.resolve('happy-dom'));
const { Liquid } = await import(require.resolve('liquidjs'));
const theme = fileURLToPath(new URL('../../shopify/current/', import.meta.url));
const enginePath = path.join(theme, 'assets/bc-product-switcher.js');
const snippetPath = path.join(theme, 'snippets/bc-fabriecio-choices.liquid');
const engineSource = fs.readFileSync(enginePath, 'utf8');
const marker = 'function init(root = document)';
assert.equal(engineSource.split(marker).length, 2, 'Shared switcher constructor instrumentation marker must be unique');
const instrumentedEngine = engineSource.replace(marker, 'window.TestSwitcher = BCProductSwitcherV2; ' + marker);
const snippetSource = fs.readFileSync(snippetPath, 'utf8').replace(/{% doc %}[\s\S]*?{% enddoc %}/, '');
const locale = JSON.parse(fs.readFileSync(path.join(theme, 'locales/nl.json'), 'utf8').replace(/^\s*\/\*[\s\S]*?\*\//, ''));
const liquid = new Liquid({ strictFilters: true });
liquid.registerFilter('json', value => JSON.stringify(value));
liquid.registerFilter('asset_url', value => '/assets/' + value);
liquid.registerFilter('stylesheet_tag', value => '<link rel="stylesheet" href="' + value + '">');
liquid.registerFilter('t', (key, ...parameters) => {
  let value = key.split('.').reduce((parent, part) => parent?.[part], locale) || key;
  for (const parameter of parameters) {
    if (Array.isArray(parameter)) value = value.replaceAll('{{ ' + parameter[0] + ' }}', parameter[1]);
  }
  return value;
});
const plan = JSON.parse(fs.readFileSync(args.plan, 'utf8'));
const source = JSON.parse(fs.readFileSync(args.source, 'utf8'));
const text = value => String(value ?? '').replace(/\s+/g, ' ').trim();
const key = value => text(value).replace(/^pa_/, '');
const canonicalSource = value => {
  const url = new URL(value);
  assert.equal(url.protocol, 'https:');
  assert(['fabriecio.nl', 'www.fabriecio.nl', 'b2b.fabriecio.nl'].includes(url.hostname));
  return 'https://fabriecio.nl' + url.pathname.replace(/\/+$/, '') + '/';
};
const uniqueMap = (items, getKey, label) => {
  const result = new Map();
  for (const item of items) {
    const identity = getKey(item);
    assert(identity && !result.has(identity), 'Duplicate or missing ' + label + ': ' + identity);
    result.set(identity, item);
  }
  return result;
};
const sourcesBySku = uniqueMap(source.products, record => text(record.sku), 'source SKU');
const sourcesByUrl = uniqueMap(source.products, record => canonicalSource(record.source_url), 'source URL');
const plannedBySku = uniqueMap(plan.updates, row => text(row.sku), 'planned SKU');
const skippedBySku = new Map((plan.skipped || []).map(row => [text(row.sku), row]));
const results = [];
const failures = [];
let optionChecks = 0;
let navigationChecks = 0;
let currentSelectionChecks = 0;
let archivedDisabledChecks = 0;

for (const row of plan.updates.filter(item => item.choices)) {
  const record = sourcesBySku.get(text(row.sku));
  const countBefore = optionChecks;
  const perProduct = { sku: row.sku, optionChecks: 0, navigations: 0, currentSelections: 0, archivedDisabled: 0 };
  let window;
  try {
    assert(record, 'Planned product must have an exact source SKU');
    assert.equal(row.choices.groups.length, 1);
    const group = row.choices.groups[0];
    assert.equal(group.menus.length, record.menus.length, 'Every observed source menu must be present');
    for (const [index, menu] of group.menus.entries()) {
      const observed = record.menus[index];
      assert.equal(menu.key, key(observed.key), 'Source menu order/key');
      assert.equal(menu.label, text(observed.label), 'Source menu label');
      assert.deepEqual(menu.values, observed.values.map(choice => text(choice.value)), 'Source option order/values');
    }
    const origin = 'https://badkamercity.nl';
    const currentUrl = '/products/' + row.handle;
    const rendered = await liquid.parseAndRender(snippetSource, {
      product: { vendor: 'Fabriecio', handle: row.handle, url: currentUrl, variants: [{}],
        metafields: { custom: { fabriecio_choices: { value: row.choices } } } },
      section: { id: 'fabriecio-plan-' + results.length }
    });
    window = new Window({ url: origin + currentUrl });
    window.console.info = () => {};
    window.console.warn = (...messages) => { throw new Error(messages.map(text).join(' ')); };
    window.matchMedia = () => ({ matches: false, addEventListener() {}, removeEventListener() {} });
    window.eval(instrumentedEngine);
    const container = window.document.createElement('div');
    container.innerHTML = rendered;
    window.document.body.append(container);
    const root = container.querySelector('[data-bc-product-switcher-v2]');
    assert(root, 'Actual Liquid adapter must render this product');
    assert.equal(root.dataset.productHandle, row.handle);
    assert.equal(root.dataset.bcCompactColors, 'true');
    const inline = root.querySelector('script[data-bc-switcher-inline]');
    const renderedData = JSON.parse(inline.textContent);
    assert.deepEqual(renderedData, row.choices, 'Actual Liquid JSON must preserve the one-hop payload');
    const instance = new window.TestSwitcher(root, renderedData);
    assert(!root.hidden, 'Real shared engine must show the menu');
    for (const toggle of root.querySelectorAll('.bc-hotbath-colors__toggle')) {
      if (toggle.getAttribute('aria-expanded') === 'false') toggle.click();
    }
    for (const menu of record.menus) {
      const field = key(menu.key);
      const controls = [...root.querySelectorAll('button[data-switch-field][data-switch-value]')]
        .filter(button => button.dataset.switchField === field);
      const select = [...root.querySelectorAll('select[data-switch-field]')]
        .find(element => element.dataset.switchField === field);
      assert.equal(controls.length || select?.options.length, menu.values.length, 'Every source option needs one control');
      const active = controls.find(button => button.getAttribute('aria-pressed') === 'true');
      assert.equal(active?.dataset.switchValue ?? select?.value, text(menu.selected), 'Selected option must match source');
      for (const choice of menu.values) {
        const value = text(choice.value);
        const sourceTarget = sourcesByUrl.get(canonicalSource(choice.target_url));
        assert(sourceTarget, 'Source choice must have a resolved source target');
        const plannedTarget = plannedBySku.get(text(sourceTarget.sku));
        const button = controls.find(element => element.dataset.switchValue === value);
        const option = select && [...select.options].find(element => element.value === value);
        assert(button || option, 'Source option control must exist');
        assert.equal(window.location.pathname, currentUrl, 'Replay must start from the current product URL');
        if (!plannedTarget) {
          const skipped = skippedBySku.get(text(sourceTarget.sku));
          assert.equal(skipped?.reason, 'shopify_not_active', 'Only explicitly inactive destinations may be disabled');
          assert.equal(skipped?.status, 'ARCHIVED', 'Excluded source destination must be archived');
          assert.equal(button?.disabled ?? option?.disabled, true, 'Archived destination must be disabled');
          if (button) button.click();
          assert.equal(window.location.pathname, currentUrl, 'Disabled choice must not navigate');
          archivedDisabledChecks++;
          perProduct.archivedDisabled++;
        } else {
          assert.equal(button?.disabled ?? option?.disabled, false, 'Active source destination must be enabled');
          assert(group.products.some(product => product.handle === plannedTarget.handle), 'Source destination must exist in the actual one-hop payload');
          if (button) button.click();
          else {
            select.value = value;
            select.dispatchEvent(new window.Event('change', { bubbles: true }));
          }
          assert.equal(window.location.pathname, '/products/' + plannedTarget.handle, 'Actual shared engine must open the exact source-linked Shopify product');
          if (plannedTarget.handle === row.handle) {
            assert.equal(instance.isNavigating, false);
            currentSelectionChecks++;
            perProduct.currentSelections++;
          } else {
            assert.equal(instance.isNavigating, true);
            navigationChecks++;
            perProduct.navigations++;
            window.location.href = origin + currentUrl;
            window.dispatchEvent(new window.Event('pageshow'));
            assert.equal(instance.isNavigating, false, 'Actual pageshow handler must restore controls for replay');
            for (const [fieldName, selected] of Object.entries(instance.state)) {
              assert.equal(selected, text(record.selected_options[fieldName]), 'Actual pageshow handler must restore source selection');
            }
          }
        }
        optionChecks++;
        perProduct.optionChecks++;
      }
    }
    perProduct.status = 'PASS';
  } catch (error) {
    perProduct.status = 'FAIL';
    perProduct.error = error.message;
    failures.push({ sku: row.sku, message: error.message, completedOptionChecks: optionChecks - countBefore });
  } finally {
    if (window) await window.happyDOM.close();
  }
  results.push(perProduct);
}
const summary = {
  status: failures.length ? 'FAIL' : 'PASS', products: results.length, optionChecks,
  navigationChecks, currentSelectionChecks, archivedDisabledChecks, failures: failures.length
};
assert.equal(results.length, plan.summary.choice_products, 'All planned choice products must be covered');
const report = {
  schema_version: 1, created_at: new Date().toISOString(), summary,
  sourceProductCount: source.products.length,
  inputs: { plan: path.basename(args.plan), source: path.basename(args.source) },
  sourceHashes: {
    switcherSha256: crypto.createHash('sha256').update(engineSource).digest('hex'),
    adapterSha256: crypto.createHash('sha256').update(fs.readFileSync(snippetPath)).digest('hex')
  },
  method: 'Actual Liquid adapter rendered for every planned one-hop payload; unchanged shared product-switcher engine executed in Happy DOM; every observed source menu option clicked or verified disabled against its exact source-linked SKU.',
  limitations: ['Offline DOM and Liquid fixture replay; no live browser, CSS/layout, physical mobile device, Shopify preview, cart, checkout or network requests.'],
  failures, products: results
};
if (args.output) {
  fs.mkdirSync(path.dirname(path.resolve(args.output)), { recursive: true });
  fs.writeFileSync(args.output, JSON.stringify(report, null, 2) + '\n');
}
console.log(JSON.stringify(summary));
if (failures.length) process.exitCode = 1;
