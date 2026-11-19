const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const assert = require('node:assert/strict');

class Element {
  constructor(tag) {
    this.tagName = tag.toUpperCase();
    this.children = [];
    this.dataset = {};
    this.attributes = {};
    this.listeners = {};
    this.hidden = false;
    this.disabled = false;
    this.isConnected = true;
    this.className = '';
    this.classList = {
      toggle: (name, active) => {
        const names = new Set(this.className.split(' ').filter(Boolean));
        if (active) names.add(name); else names.delete(name);
        this.className = [...names].join(' ');
      },
      add: name => this.classList.toggle(name, true),
      remove: name => this.classList.toggle(name, false),
      contains: name => this.className.split(' ').includes(name)
    };
  }
  append(...elements) {
    for (const element of elements) {
      if (element.tagName === 'FRAGMENT') this.children.push(...element.children);
      else this.children.push(element);
    }
  }
  set innerHTML(_) { this.children = []; }
  setAttribute(k, v) { this.attributes[k] = String(v); }
  getAttribute(k) { return this.attributes[k]; }
  addEventListener(k, fn) { this.listeners[k] = fn; }
  closest() { return null; }
  get options() { return this.children; }
  querySelectorAll(selector) {
    const all = this.children.flatMap(child => [child, ...child.querySelectorAll('*')]);
    if (selector === '*') return all;
    const predicates = {
      'button[data-switch-field][data-switch-value]': x => x.tagName === 'BUTTON' && x.dataset.switchField && x.dataset.switchValue,
      '[data-hotbath-selected-color]': x => x.dataset.hotbathSelectedColor,
      'select[data-switch-field]': x => x.tagName === 'SELECT' && x.dataset.switchField
    };
    return all.filter(predicates[selector] || (() => false));
  }
}
const document = {
  readyState: 'complete',
  querySelectorAll: () => [],
  createElement: tag => new Element(tag),
  createDocumentFragment: () => new Element('fragment'),
  createTextNode: value => Object.assign(new Element('text'), {textContent: value})
};
const window = {
  location: {origin: 'https://badkamercity.nl', assign(url) { this.lastAssigned = url; }},
  addEventListener() {},
  removeEventListener() {},
  matchMedia() { return {matches: true, addEventListener() {}, removeEventListener() {}}; }
};
const context = {window, document, URL, console: {info() {},warn() {}}, Set, Map};
vm.createContext(context);
const source = fs.readFileSync(path.join(__dirname, '../after/assets/bc-product-switcher.js'), 'utf8')
  .replace('function init(root = document)', 'globalThis.SwitcherTest = BCProductSwitcherV2; function init(root = document)');
vm.runInContext(source, context);
const Switcher = context.SwitcherTest;
const data = JSON.parse(fs.readFileSync(process.env.HOTBATH_TEST_FIXTURE || path.join(__dirname, '../../mobile-a/tests/test-data/hotbath-groups.json'), 'utf8'));
const group = data.groups.find(g => g.id === 'hotbath-book-cb105ext-keuzes');
const root = new Element('div');
root.dataset = {
  hotbathMobileA: 'true', labelMoreColors: '+__COUNT__ kleuren', labelMoreColorsOne: '+1 kleur', labelLessColors: 'Minder kleuren',
  sectionId: 'test', switchGroup: group.id,
  productHandle: group.products.find(p => p.options.kleur === 'Gepolijst zwart PVD').handle,
  hotbathSwatchUrls: JSON.stringify(Object.fromEntries(['cr','gn','bb','ab','wh','ai','pbp','mbp','bbp','bcp'].map(c => [c, `/cdn/shop/t/1/assets/bc-hotbath-swatch-${c}.jpg`])))
};
const switcher = new Switcher(root, {groups: [group]});
const swatches = () => root.querySelectorAll('*').filter(e => e.classList.contains('bc-hotbath-swatch'));
assert.equal(swatches().length, 10);
assert.equal(swatches().filter(b => !b.hidden).length, 6);
assert.equal(swatches().find(b => b.dataset.switchValue === 'Gepolijst zwart PVD').hidden, false);
assert.equal(swatches().find(b => b.dataset.switchValue === 'Gepolijst zwart PVD').attributes['aria-pressed'], 'true');
assert.equal(root.querySelectorAll('[data-hotbath-selected-color]')[0].textContent, 'Gepolijst zwart PVD');
assert.equal(root.querySelectorAll('select[data-switch-field]').length, 0);
let toggle = root.querySelectorAll('*').find(e => e.classList.contains('bc-hotbath-colors__toggle'));
assert.equal(toggle.textContent, '+4 kleuren');
assert.equal(toggle.attributes['aria-expanded'], 'false');
toggle.listeners.click();
assert.equal(swatches().filter(b => !b.hidden).length, 10);
assert.equal(toggle.textContent, 'Minder kleuren');
assert.equal(toggle.attributes['aria-expanded'], 'true');
toggle.listeners.click();
assert.equal(swatches().filter(b => !b.hidden).length, 6);
assert.equal(toggle.textContent, '+4 kleuren');
assert.equal(toggle.attributes['aria-expanded'], 'false');
const oneMoreGroup = JSON.parse(JSON.stringify(group));
oneMoreGroup.id = 'seven-colour-fixture';
oneMoreGroup.menus[0].values = oneMoreGroup.menus[0].values.slice(0, 7);
oneMoreGroup.products = oneMoreGroup.products.filter(product => oneMoreGroup.menus[0].values.includes(product.options.kleur));
const oneMoreRoot = new Element('div');
oneMoreRoot.dataset = {...root.dataset, switchGroup: oneMoreGroup.id};
new Switcher(oneMoreRoot, {groups: [oneMoreGroup]});
const oneMoreSwatches = () => oneMoreRoot.querySelectorAll('*').filter(e => e.classList.contains('bc-hotbath-swatch'));
const oneMoreToggle = oneMoreRoot.querySelectorAll('*').find(e => e.classList.contains('bc-hotbath-colors__toggle'));
assert.equal(oneMoreSwatches().filter(button => button.hidden).length, 1);
assert.equal(oneMoreToggle.textContent, '+1 kleur');
oneMoreToggle.listeners.click();
assert.equal(oneMoreSwatches().filter(button => button.hidden).length, 0);
assert.equal(oneMoreToggle.textContent, 'Minder kleuren');
oneMoreToggle.listeners.click();
assert.equal(oneMoreSwatches().filter(button => button.hidden).length, 1);
assert.equal(oneMoreToggle.textContent, '+1 kleur');
const stateBefore = JSON.stringify(switcher.state);
switcher.mobileMedia.matches = false;
switcher.onMobileChange();
assert.equal(swatches().length, 0);
assert.equal(root.querySelectorAll('select[data-switch-field]').length, 1);
assert.equal(JSON.stringify(switcher.state), stateBefore);
switcher.mobileMedia.matches = true;
switcher.onMobileChange();
assert.equal(swatches().filter(b => !b.hidden).length, 6);
assert.equal(JSON.stringify(switcher.state), stateBefore);
switcher.products = switcher.products.filter(p => !(p.options.kleur === 'Chroom' && p.options.uitlooplengte === '18 cm'));
switcher.syncControls();
assert.equal(swatches().find(b => b.dataset.switchValue === 'Chroom').disabled, true);
const anotherRoot = new Element('div');
anotherRoot.dataset = {...root.dataset, hotbathMobileA: 'false'};
new Switcher(anotherRoot, {groups: [group]});
assert.equal(anotherRoot.querySelectorAll('select[data-switch-field]').length, 1);
assert.equal(anotherRoot.classList.contains('bc-hotbath-switcher--mobile'), false);
for (const pilotGroup of data.groups) {
  const pilotRoot = new Element('div');
  pilotRoot.dataset = {...root.dataset, switchGroup: pilotGroup.id, productHandle: pilotGroup.products[0].handle};
  const pilot = new Switcher(pilotRoot, {groups: [pilotGroup]});
  const colorMenu = pilotGroup.menus.find(menu => /^(kleur|basiskleur|color|colour)$/i.test(menu.key));
  assert.ok(colorMenu, `${pilotGroup.id}: colour menu present`);
  assert.ok(pilotRoot.classList.contains('bc-hotbath-switcher--mobile'));
  const next = pilotGroup.products.find(product => product.options[colorMenu.key] !== pilot.state[colorMenu.key] &&
    pilotGroup.menus.every(menu => menu.key === colorMenu.key || product.options[menu.key] === pilot.state[menu.key]));
  assert.ok(next, `${pilotGroup.id}: alternative colour for same configuration`);
  window.location.lastAssigned = null;
  pilot.updateSelection(colorMenu.key, next.options[colorMenu.key]);
  assert.equal(window.location.lastAssigned, new URL(next.url, window.location.origin).href,
    `${pilotGroup.id}: exact configured product URL used`);
}
console.log('PASS: 6 visible colors, selected outside first 6 retained, full name, expand/collapse, desktop restore, state retention, impossible option disabled, non-Hotbath unchanged, 3 pilot groups navigate to exact configured product.');
