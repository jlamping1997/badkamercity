import { Window } from 'happy-dom';
import fs from 'node:fs';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';

const source = fs.readFileSync('theme/assets/bc-product-inbouw.js', 'utf8');
const purchase = fs.readFileSync('theme/assets/bc-hotbath-mobile.js', 'utf8');
const wait = () => new Promise(resolve => setTimeout(resolve, 60));
const windows = [];
const results = [];

async function fixture({ width = 1280, hotbath = true, volume = false, valid = true, available = true,
  saved = null, group = 'hotbath-cb105', loadPurchaseFirst = false } = {}) {
  const window = new Window({ url: 'https://badkamercity.nl/products/trim-current', width, height: 844 });
  windows.push(window);
  const document = window.document;
  window.fetch = () => { throw new Error('Network requests are forbidden in this test'); };
  if (saved) window.sessionStorage.setItem('bc-inbouw-choice-v1', JSON.stringify(saved));
  document.write(`<product-info data-hotbath-mobile-a="${hotbath}" data-product-price="28700" data-product-variant="100" data-currency="EUR" data-mobile-total-label="Totaal" data-mobile-vat-label="Incl btw" data-mobile-choose-inbouw-label="Kies inbouw"><div class="product__info-container"><div data-bc-product-switcher-v2 data-switch-group="${group}"></div><div class="bc-buybox__purchase-row${volume ? ' bc-buybox__purchase-row--volume' : ''}"><div class="bc-buybox__section--quantity"><input name="quantity" type="number" min="1" step="1" value="2" required form="p"></div><div class="bc-buybox__section--actions"><product-form><form id="p"><input name="id" value="100"><bc-inbouw-addon data-valid="${valid}" data-parent-variant="100" data-parent-sku="TRIM" data-body-variant="200" data-body-sku="HBCB105" data-body-available="${available}" data-body-price="9500" data-quantity-per-trim="1" data-currency="EUR" data-message-choice="Choose" data-message-changed="Changed" data-message-unavailable="Unavailable" data-message-uncertain="Uncertain"><fieldset data-inbouw-controls disabled hidden aria-describedby="detail"><legend>Inbouwdeel</legend><div class="bc-inbouw__radio-controls"><p id="detail">Desktop detail</p><input id="yes" type="radio" name="bc_inbouw_choice" value="yes" data-inbouw-choice required disabled><label for="yes">Yes</label><input id="no" type="radio" name="bc_inbouw_choice" value="no" data-inbouw-choice required disabled><label for="no">No</label></div><div class="bc-inbouw__toggle-row" hidden><label class="bc-inbouw__toggle-label"><input type="checkbox" data-inbouw-toggle disabled><span>Inbouwdeel toevoegen</span></label><span class="bc-inbouw__toggle-price">+ €95</span><p class="bc-inbouw__toggle-help">HBCB105</p></div></fieldset><p data-inbouw-error hidden></p><a data-inbouw-cart-link hidden></a></bc-inbouw-addon><div class="bc-product-form__buttons"><button type="submit" class="product-form__submit">In winkelwagen</button></div></form></product-form></div></div></div></product-info>`);
  const root = document.querySelector('product-info');
  const productForm = document.querySelector('product-form');
  productForm.handleErrorMessage = () => {};
  productForm.submitButton = productForm.querySelector('button');
  if (loadPurchaseFirst) {
    window.eval(purchase);
    document.dispatchEvent(new window.Event('DOMContentLoaded'));
    await wait();
    assert.equal(root.dataset.mobileTotalState, 'pending', 'Fixture starts before checkbox initialization');
  }
  window.eval(source);
  await wait();
  return { window, document, root, productForm, addon: document.querySelector('bc-inbouw-addon'),
    toggle: document.querySelector('[data-inbouw-toggle]'), form: document.getElementById('p') };
}

try {
  const current = await fixture({ loadPurchaseFirst: true });
  const { window, root, addon, toggle, form, productForm } = current;
  assert.equal(addon.dataset.checkboxMode, 'true');
  assert.equal(toggle.checked, false);
  assert.equal(addon.choice(), 'no');
  assert.equal(form.checkValidity(), true);
  assert.equal(root.dataset.mobileTotalState, 'ready');
  assert.equal(root.querySelector('[data-mobile-total-value]').dataset.totalCents, '57400');
  results.push('Unchecked desktop initialization selects only the unpaid no radio and notifies the earlier-loaded total enhancer');

  const submitted = [];
  addon.addItems = async items => { submitted.push(JSON.parse(JSON.stringify(items))); };
  assert.equal(addon.handleSubmit(productForm), false);
  assert.equal(submitted.length, 0);
  results.push('Unchecked checkbox delegates to the existing single-product submit path');

  toggle.click();
  await wait();
  assert.equal(toggle.checked, true);
  assert.equal(addon.choice(), 'yes');
  assert.equal(root.querySelector('[data-mobile-total-value]').dataset.totalCents, '76400');
  assert.equal(addon.handleSubmit(productForm), true);
  await addon.pendingAdd;
  assert.deepEqual(submitted, [[{ id: '100', quantity: 2 }, { id: '200', quantity: 2 }]]);
  assert.equal(toggle.disabled, true);
  assert.equal(addon.handleSubmit(productForm), true);
  assert.equal(submitted.length, 1);
  results.push('Native checkbox click reaches the real two-item handler with exact IDs, quantity 2 + 2, and a busy double-submit guard');

  addon.setBusy(false);
  toggle.click();
  await wait();
  assert.equal(addon.choice(), 'no');
  assert.equal(addon.handleSubmit(productForm), false);
  assert.equal(submitted.length, 1);
  results.push('Unchecking after selecting yes restores the single-product path without a second bundle request');

  window.happyDOM.setWindowSize({ width: 1200, height: 844 });
  window.dispatchEvent(new window.Event('resize'));
  await wait();
  assert.equal(addon.hasAttribute('data-checkbox-mode'), true);
  assert.equal(addon.choice(), 'no');
  assert.equal(addon.querySelector('.bc-inbouw__radio-controls').hidden, true);
  assert.equal(addon.querySelector('.bc-inbouw__toggle-row').hidden, false);
  assert.equal(addon.controls.getAttribute('aria-describedby'), null);
  results.push('Explicit no and compact checkbox remain unchanged across viewport changes');

  const implicit = await fixture();
  implicit.root.dataset.bcNavigating = 'true';
  implicit.addon.rememberForNavigation();
  assert.equal(implicit.window.sessionStorage.getItem('bc-inbouw-choice-v1'), null);
  implicit.window.happyDOM.setWindowSize({ width: 1200, height: 844 });
  implicit.window.dispatchEvent(new implicit.window.Event('resize'));
  await wait();
  assert.equal(implicit.addon.choice(), 'no');
  assert.equal(implicit.form.checkValidity(), true);
  results.push('Implicit unpaid no is not persisted as a user choice and remains unpaid after resize');

  const explicit = await fixture();
  explicit.toggle.click();
  explicit.root.dataset.bcNavigating = 'true';
  explicit.addon.rememberForNavigation();
  const saved = JSON.parse(explicit.window.sessionStorage.getItem('bc-inbouw-choice-v1'));
  assert.equal(saved.choice, 'yes');
  saved.from = '/products/trim-other';
  const restored = await fixture({ saved });
  assert.equal(restored.toggle.checked, true);
  assert.equal(restored.addon.choice(), 'yes');
  restored.window.happyDOM.setWindowSize({ width: 1200, height: 844 });
  restored.window.dispatchEvent(new restored.window.Event('resize'));
  await wait();
  assert.equal(restored.addon.choice(), 'yes');
  results.push('Explicit yes restores only from the existing same-group/body storage contract and survives desktop switching');

  for (const mismatch of [{ group: 'other-group' }, { body: '201' }, { savedAt: Date.now() - 60000 }]) {
    const rejected = await fixture({ saved: { ...saved, ...mismatch } });
    assert.equal(rejected.toggle.checked, false);
    assert.equal(rejected.addon.choice(), 'no');
  }
  results.push('Wrong group, wrong body, and expired storage cannot preselect the paid checkbox');

  for (const options of [{ hotbath: false }, { volume: true }]) {
    const excluded = await fixture(options);
    assert.equal(excluded.addon.hasAttribute('data-checkbox-mode'), false);
    assert.equal(excluded.addon.choice(), '');
    assert.equal(excluded.addon.querySelector('.bc-inbouw__radio-controls').hidden, false);
    assert.equal(excluded.toggle.disabled, true);
  }
  results.push('Other-brand scope and volume-priced products retain required radio behavior');

  const invalid = await fixture({ valid: false });
  assert.equal(invalid.toggle.disabled, true);
  invalid.addon.addItems = () => { throw new Error('Invalid identity must never submit'); };
  assert.equal(invalid.addon.handleSubmit(invalid.productForm), true);
  const unavailable = await fixture({ available: false });
  assert.equal(unavailable.toggle.disabled, true);
  assert.equal(unavailable.addon.choice(), 'no');
  assert.equal(unavailable.addon.handleSubmit(unavailable.productForm), false);
  results.push('Invalid identity blocks submission and unavailable optional bodies cannot be checked');

  const unavailableRestored = await fixture({ available: false, saved });
  assert.equal(unavailableRestored.toggle.checked, true);
  assert.equal(unavailableRestored.toggle.disabled, false);
  assert.equal(unavailableRestored.addon.handleSubmit(unavailableRestored.productForm), true);
  unavailableRestored.toggle.click();
  assert.equal(unavailableRestored.addon.choice(), 'no');
  assert.equal(unavailableRestored.toggle.disabled, true);
  assert.equal(unavailableRestored.addon.handleSubmit(unavailableRestored.productForm), false);
  results.push('A restored yes for a now-unavailable body can be unchecked; unavailable yes cannot submit or be reselected');

  const uncertain = await fixture();
  uncertain.toggle.click();
  uncertain.addon.uncertain = true;
  uncertain.addon.update();
  assert.equal(uncertain.toggle.disabled, true);
  assert.equal(uncertain.addon.handleSubmit(uncertain.productForm), true);
  results.push('Uncertain cart status disables the checkbox and retains the existing no-retry submit protection');

  for (const width of [320,390,750,1024,1440]) {
    const v=await fixture({width,loadPurchaseFirst:true});
    assert.equal(v.addon.dataset.checkboxMode,'true');
    assert.equal(v.toggle.checked,false);
    assert.equal(v.root.querySelector('[data-mobile-total-value]').dataset.totalCents,'57400');
    v.toggle.click(); await wait();
    assert.equal(v.root.querySelector('[data-mobile-total-value]').dataset.totalCents,'76400');
    assert.equal(v.form.elements.namedItem('quantity').form,v.form);
    const qty=v.form.elements.namedItem('quantity'); qty.value='3'; qty.dispatchEvent(new v.window.Event('input',{bubbles:true})); await wait();
    assert.equal(v.root.querySelector('[data-mobile-total-value]').dataset.totalCents,'114600');
  }
  results.push('320, 390, 750, 1024 and 1440: unpaid default, checkbox, quantity form association and totals verified');
  fs.writeFileSync('purchase-test-results.json', JSON.stringify({passed:results.length,networkRequests:0,results},null,2));
  console.log(JSON.stringify({ sourceSha256: createHash('sha256').update(source).digest('hex'),
    passed: results.length, networkRequests: 0, results }, null, 2));
} finally {
  for (const window of windows) {
    await window.happyDOM.abort();
    window.close();
  }
}
