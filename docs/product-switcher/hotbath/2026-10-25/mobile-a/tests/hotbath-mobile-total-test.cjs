const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');

const sourcePath = path.resolve(process.argv[2] || path.join(__dirname, '../after/assets/bc-hotbath-mobile.js'));
const source = fs.readFileSync(sourcePath, 'utf8');
const injectionPoint = '  const mount = scope => {';
assert.equal(source.split(injectionPoint).length, 2, 'Expected exactly one class-export injection point');
const instrumentedSource = source.replace(injectionPoint,
  '  window.__MobilePurchaseForTest = MobilePurchase;\n' + injectionPoint);
const sandbox = {
  window: {},
  document: {
    readyState: 'loading',
    documentElement: { lang: 'nl-NL' },
    addEventListener() {}
  },
  Intl, Map, Number, String, Array
};
vm.runInNewContext(instrumentedSource, sandbox, { filename: sourcePath });
const calculate = sandbox.window.__MobilePurchaseForTest.prototype.calculate;
assert.equal(typeof calculate, 'function', 'The actual production calculate() method must be available');

function evaluate({
  qty = '1', choice = 'yes', bodyAvailable = 'true', valid = 'true',
  currency = 'EUR', addonCurrency = 'EUR', variant = '100', price = '28700',
  bodyPrice = '9500', multiplier = '1', inputValid = true, uncertain = false,
  sellingPlan = '', withAddon = true, disabled = false
} = {}) {
  const addon = {
    dataset: {
      valid, parentVariant: '100', currency: addonCurrency, bodyPrice,
      quantityPerTrim: multiplier, bodyAvailable
    },
    uncertain,
    querySelector: () => choice ? { value: choice, disabled } : null,
    validIdentity: () => valid === 'true'
  };
  const fields = {
    id: { value: variant },
    quantity: { value: qty, checkValidity: () => inputValid },
    selling_plan: { value: sellingPlan }
  };
  return calculate.call({
    root: { dataset: { productPrice: price, currency, productVariant: '100' } },
    form: {
      elements: { namedItem: name => fields[name] },
      querySelector: () => withAddon ? addon : null
    }
  });
}

const cases = [
  { name: 'yes one: trim plus body', input: {}, state: 'ready', cents: 38200 },
  { name: 'yes two: two trims plus two bodies', input: { qty: '2' }, state: 'ready', cents: 76400 },
  { name: 'no two: trims only', input: { qty: '2', choice: 'no' }, state: 'ready', cents: 57400 },
  { name: 'product without addon', input: { qty: '2', withAddon: false }, state: 'ready', cents: 57400 },
  { name: 'no paid preselection', input: { choice: '' }, state: 'pending' },
  { name: 'zero quantity rejected', input: { qty: '0' }, state: 'invalid' },
  { name: 'fractional quantity rejected', input: { qty: '1.5' }, state: 'invalid' },
  { name: 'empty quantity rejected', input: { qty: '' }, state: 'invalid' },
  { name: 'native validity rule respected', input: { inputValid: false }, state: 'invalid' },
  { name: 'stale variant price rejected', input: { variant: '101' }, state: 'invalid' },
  { name: 'mixed currencies rejected', input: { addonCurrency: 'USD' }, state: 'invalid' },
  { name: 'missing price rejected', input: { price: '' }, state: 'invalid' },
  { name: 'unsafe integer total rejected', input: { qty: '9007199254740991' }, state: 'invalid' },
  { name: 'unavailable selected addon rejected', input: { bodyAvailable: 'false' }, state: 'invalid' },
  { name: 'uncertain cart operation rejected', input: { uncertain: true }, state: 'invalid' },
  { name: 'unsupported selling plan rejected', input: { sellingPlan: '99' }, state: 'invalid' },
  { name: 'disabled selected choice rejected', input: { disabled: true }, state: 'invalid' },
  { name: 'invalid product mapping rejected', input: { valid: 'false' }, state: 'invalid' }
];

const results = cases.map(test => {
  const actual = evaluate(test.input);
  assert.equal(actual.state, test.state, test.name);
  if (test.cents !== undefined) {
    assert.equal(actual.total, test.cents, test.name);
    assert.equal(actual.formatted,
      new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' }).format(test.cents / 100),
      test.name + ': formatted amount');
  } else {
    assert.equal(actual.total, undefined, test.name + ': must not expose a misleading total');
  }
  return { name: test.name, passed: true };
});

console.log(JSON.stringify({
  test: 'Actual production calculate() method with isolated form fixtures',
  sourcePath,
  sourceSha256: createHash('sha256').update(source).digest('hex'),
  cases: results.length,
  passed: results.length,
  results
}, null, 2));
