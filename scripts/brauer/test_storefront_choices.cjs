const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const theme = path.resolve(process.argv[2] || 'shopify/current');
const reportPath = process.argv[3];
let code = fs.readFileSync(path.join(theme, 'assets/bc-brauer-choices.js'), 'utf8');
code = code.replace('  function init(scope = document) {',
  '  globalThis.qa = { active, matches, nextState, Choices, label, orderedValues };\n  function init(scope = document) {');
class El {
  constructor(tag = 'div') { this.tagName = tag; this.style = { setProperty() {} }; this.children = []; this.dataset = {}; this.attrs = {}; this.events = {}; this.disabled = false; this.hidden = false; this._text = ''; this.classes = new Set(); this.classList = { toggle: (k, v) => v ? this.classes.add(k) : this.classes.delete(k), add: k => this.classes.add(k), remove: k => this.classes.delete(k) }; }
  set className(v) { this.classes = new Set(v.split(' ')); }
  set textContent(v) { this._text = String(v); this.children = []; }
  get textContent() { return this._text + this.children.map(x => x.textContent).join(''); }
  setAttribute(k,v) { this.attrs[k] = String(v); }
  append(...nodes) { this.children.push(...nodes); }
  replaceChildren(...nodes) { this.children = nodes; }
  addEventListener(k, fn) { this.events[k] = fn; }
  removeEventListener(k) { delete this.events[k]; }
  focus() { this.focused = true; }
  closest() { return this.product || null; }
  querySelector() { return null; }
  querySelectorAll() { return this.buttons || []; }
}
const document = { readyState: 'loading', createElement: t => new El(t), createDocumentFragment: () => new El('fragment'), addEventListener() {}, removeEventListener() {} };
const navigation = [];
const sandbox = { document, URL, sessionStorage: { getItem() {return null;}, setItem() {}, removeItem() {} }, requestAnimationFrame: fn => fn(), window: { location: { origin: 'https://badkamercity.nl', href: 'https://badkamercity.nl/products/test?preview_theme_id=196542005514', assign: url => navigation.push(url) }, scrollY: 200, addEventListener() {}, scrollTo() {} } };
vm.runInNewContext(code, sandbox);
const { active, matches, nextState, Choices, orderedValues } = sandbox.qa;
const groups = fs.readdirSync(path.join(theme, 'assets')).filter(n => /^bc-brauer-[a-f0-9]+(?:-[a-z0-9]+)*\.json$/.test(n)).map(n => JSON.parse(fs.readFileSync(path.join(theme, 'assets', n))));
const report = { groups: groups.length, products: 0, exact_starts: 0, valid_choices: 0, unavailable_choices: 0, conditional_pending_choices: 0, reachable_products: 0, conditional_cart_guard: false, native_select: false, six_colour_limit: false };
const allIds = new Set();
for (const group of groups) {
  report.products += group.products.length;
  const graph = new Map();
  for (const product of group.products) {
    assert(!allIds.has(product.id)); allIds.add(product.id);
    assert.equal(product.url, '/products/' + product.handle);
    assert(!product.image || product.image.startsWith('https://cdn.shopify.com/'));
    const starts = matches(group, product.options);
    assert.equal(starts.length, 1, group.id + ':' + product.sku);
    assert.equal(starts[0].sku, product.sku);
    report.exact_starts++;
    const reached = new Set();
    for (const axis of group.axes) {
      if (!active(group, axis, product.options)) continue;
      for (const value of axis.values) {
        const next = nextState(group, product.options, axis.key, value);
        const targets = matches(group, next);
        if (!targets.length) { report.unavailable_choices++; continue; }
        report.valid_choices++;
        assert.equal(next[axis.key], value);
        for (const other of group.axes) {
          if (other.key !== axis.key && !other.reset_on_change?.includes(axis.key)) assert.equal(next[other.key], product.options[other.key]);
        }
        if (targets.length > 1) {
          report.conditional_pending_choices++;
          assert(group.axes.some(a => a.depends_on && active(group, a, next) && !a.values.includes(next[a.key])));
        }
        for (const target of targets) reached.add(target.id);
      }
    }
    graph.set(product.id, reached);
  }
  const visited = new Set([group.products[0].id]); const queue = [...visited];
  for (let i = 0; i < queue.length; i++) for (const id of graph.get(queue[i])) if (!visited.has(id)) { visited.add(id); queue.push(id); }
  assert.equal(visited.size, group.products.length, 'unreachable choices in ' + group.id);
  report.reachable_products += visited.size;
}
function controller(group, sku) {
  const product = group.products.find(p => p.sku === sku);
  const root = new El(); root.product = new El('product-info'); root.product.buttons = [new El('button')];
  Object.assign(root.dataset, { productHandle: product.handle, productId: product.id.split('/').pop(), variantId: product.variant_id.split('/').pop(), productSku: sku, choiceGroup: group.id });
  return new Choices(root, group);
}
function descendants(node) { return node.children.flatMap(child => [child, ...descendants(child)]); }
const mirror = groups.find(g => g.products.some(p => p.sku === 'SK-IMD100HW'));
const ui = controller(mirror, 'SK-IMD100HW');
assert.equal(descendants(ui.root).some(e => e.dataset.axisGroup === 'door'), false);
ui.choose(mirror.axes.find(a => a.key === 'width'), '60');
assert.equal(ui.root.dataset.pending, 'true');
assert.equal(ui.navigating, false);
assert.equal(ui.root.product.buttons[0].disabled, true);
assert(ui.guard);
assert(descendants(ui.root).some(e => e.dataset.axisGroup === 'door'));
ui.choose(mirror.axes.find(a => a.key === 'door'), 'Rechts');
assert.equal(new URL(navigation.at(-1)).pathname, '/products/' + mirror.products.find(p => p.sku === 'SK-IMD60RHW').handle);
assert.equal(new URL(navigation.at(-1)).searchParams.get('preview_theme_id'), '196542005514');
report.conditional_cart_guard = true;
const cabinet = groups.find(g => g.products.some(p => p.sku === 'OK-AM100CH'));
const cabinetUI = controller(cabinet, 'OK-AM100CH');
const nodes = descendants(cabinetUI.root);
assert(nodes.some(e => e.tagName === 'select' && e.dataset.axis === 'width'));
report.native_select = true;
const colourButtons = nodes.filter(e => e.tagName === 'button' && e.dataset.axis === 'colour');
assert.equal(colourButtons.filter(e => !e.hidden).length, 6);
assert(colourButtons.some(e => e.dataset.value === cabinetUI.current.options.colour && !e.hidden));
for (const button of colourButtons) {
  const prospective = matches(cabinet, nextState(cabinet, cabinetUI.state, 'colour', button.dataset.value));
  const images = descendants(button).filter(e => e.tagName === 'img');
  if (images.length) { assert.equal(prospective.length, 1); assert.equal(images[0].dataset.photoSku, prospective[0].sku); assert.equal(new URL(images[0].src).pathname, new URL(prospective[0].image).pathname); assert.equal(new URL(images[0].src).searchParams.get('width'), '160'); }
}
report.six_colour_limit = true;
const taps = groups.find(g => g.id === 'BRAUER-F3F2437BF3BB2A5C');
const labels = taps.axes.find(a => a.key === 'finish').labels;
assert.equal(labels.Stripe, 'Streepjes');
assert.equal(labels.Carving, 'Gekarteld');
assert.equal(labels.Standaard, 'Glad');
let exactSpoutPhotos = 0;
let positionShapeChecks = 0;
for (const product of taps.products) {
  const tap = controller(taps, product.sku);
  const elements = descendants(tap.root);
  const handles = elements.filter(e => e.tagName === 'button' && e.dataset.axis === 'handle');
  assert.equal(handles.length, 5);
  assert(handles.every(button => descendants(button).some(e => e.tagName === 'img')));
  assert(elements.some(e => e.textContent.includes('plaatsing van de uitloop')));
  const positions = elements.filter(e => e.tagName === 'button' && e.dataset.axis === 'spout_position');
  assert.equal(positions.length, 2);
  assert.equal(product.options.spout_position, product.options.handle_code[1] === '1' ? 'Links' : 'Rechts');
  for (const button of [...handles, ...positions]) {
    const candidates = matches(taps, nextState(taps, tap.state, button.dataset.axis, button.dataset.value));
    assert.equal(button.disabled, !candidates.length);
    assert(candidates.length <= 1);
    if (!candidates.length) continue;
    const target = candidates[0];
    const expectedCode = (button.dataset.axis === 'handle' ? button.dataset.value : product.options.handle) +
      ((button.dataset.axis === 'spout_position' ? button.dataset.value : product.options.spout_position) === 'Links' ? '1' : '2');
    assert.equal(target.options.handle_code, expectedCode);
    assert.equal(target.options.colour, product.options.colour);
    assert.equal(target.options.finish, product.options.finish);
    assert.equal(target.options.spout, product.options.spout);
    assert.equal(target.options.wall_finish, product.options.wall_finish);
    positionShapeChecks++;
  }
  for (const button of elements.filter(e => e.tagName === 'button' && e.dataset.axis === 'spout')) {
    const candidates = matches(taps, nextState(taps, tap.state, 'spout', button.dataset.value));
    const photos = descendants(button).filter(e => e.tagName === 'img');
    assert.equal(button.disabled, !candidates.length);
    if (candidates.length === 1 && candidates[0].image) {
      assert.equal(photos.length, 1);
      assert.equal(photos[0].dataset.photoSku, candidates[0].sku);
      assert.equal(new URL(photos[0].src).pathname, new URL(candidates[0].image).pathname);
      exactSpoutPhotos++;
    } else assert.equal(photos.length, 0);
  }
}
const example = controller(taps, '5-S-331');
const beforeNavigation = navigation.length;
example.choose(taps.axes.find(a => a.key === 'handle'), 'B');
assert.equal(navigation.length, beforeNavigation);
assert.equal(example.current.sku, '5-S-331');
report.visual_tap_starts = taps.products.length;
report.exact_spout_photos = exactSpoutPhotos;
report.handle_choices = 5;
report.spout_position_choices = 2;
report.position_shape_checks = positionShapeChecks;
assert.equal(taps.axes.find(a => a.key === 'spout').labels.Rechte, 'Recht');
const positionExample = controller(taps, '5-S-331');
positionExample.choose(taps.axes.find(a => a.key === 'spout_position'), 'Rechts');
assert.equal(new URL(navigation.at(-1)).pathname, '/products/' + taps.products.find(p => p.sku === '5-S-335').handle);
report.handle_reference_photos = 5;
assert.equal(report.groups, 828); assert.equal(report.products, 12292);
const pricedGroups = groups.filter(g => g.price_order);
let orderedStates = 0;
for (const group of pricedGroups) {
  assert.equal(group.price_currency, 'EUR');
  for (const product of group.products) {
    assert(Number.isSafeInteger(product.price_cents));
    for (const axis of group.axes) {
      const ordered = orderedValues(group, axis, product.options);
      assert.deepEqual([...ordered].sort(), [...axis.values].sort());
      let previous = -Infinity;
      let disabledStarted = false;
      for (const value of ordered) {
        const candidates = matches(group, nextState(group, product.options, axis.key, value));
        if (!candidates.length) { disabledStarted = true; continue; }
        assert(!disabledStarted, 'available choices must precede disabled choices');
        const price = Math.min(...candidates.map(p => p.price_cents));
        assert(price >= previous, group.id + ':' + product.sku + ':' + axis.key);
        previous = price;
      }
      orderedStates++;
    }
  }
}
const exampleOrder = orderedValues(taps, taps.axes.find(a => a.key === 'colour'), example.state);
assert.equal(exampleOrder[0], 'Chroom');
assert.equal(exampleOrder[1], 'Zwart');
const opbouw = groups.find(g => g.id === 'BRAUER-46A454F9A15BDAA9');
assert.equal(opbouw.products.length, 150);
let opbouwPhotos = 0;
for (const product of opbouw.products) {
  const ui = controller(opbouw, product.sku);
  const buttons = descendants(ui.root).filter(e => e.tagName === 'button');
  const handles = buttons.filter(e => e.dataset.axis === 'handle');
  assert.equal(handles.length, 5);
  assert(handles.every(b => descendants(b).some(e => e.tagName === 'img')));
  assert(!buttons.some(e => e.dataset.axis === 'spout_position'));
  assert.equal(buttons.filter(e => e.dataset.axis === 'height_execution').length, 4);
  for (const button of buttons.filter(e => e.dataset.axis === 'height_execution')) {
    const exact = matches(opbouw, nextState(opbouw, ui.state, button.dataset.axis, button.dataset.value));
    const imgs = descendants(button).filter(e => e.tagName === 'img');
    if (exact.length === 1 && exact[0].image) {
      assert.equal(imgs.length, 1);
      assert.equal(imgs[0].dataset.photoSku, exact[0].sku);
      opbouwPhotos++;
    } else assert.equal(imgs.length, 0);
  }
}
const opbouwExample = controller(opbouw, '5-CE-001');
opbouwExample.choose(opbouw.axes.find(a => a.key === 'height_execution'), 'Verhoogd');
assert.equal(new URL(navigation.at(-1)).pathname, '/products/' + opbouw.products.find(p => p.sku === '5-CE-002').handle);
let waterPhotoChecks = 0;
for (const group of pricedGroups) {
  const ui = controller(group, group.products[0].sku);
  const buttons = descendants(ui.root).filter(e => e.tagName === 'button' && ['arm', 'handshower'].includes(e.dataset.axis));
  for (const button of buttons) {
    const candidates = matches(group, nextState(group, ui.state, button.dataset.axis, button.dataset.value));
    const photos = descendants(button).filter(e => e.tagName === 'img');
    if (candidates.length === 1 && candidates[0].image) {
      assert.equal(photos.length, 1);
      assert.equal(photos[0].dataset.photoSku, candidates[0].sku);
      assert.equal(new URL(photos[0].src).pathname, new URL(candidates[0].image).pathname);
      waterPhotoChecks++;
    } else assert.equal(photos.length, 0);
  }
}
report.water_photo_checks = waterPhotoChecks;
report.price_order_groups = pricedGroups.length;
report.price_order_products = pricedGroups.reduce((n, g) => n + g.products.length, 0);
report.price_order_states = orderedStates;
report.opbouw_starts = opbouw.products.length;
report.opbouw_execution_photos = opbouwPhotos;
const glassFamilies = new Set(['BRAUER-3C0BAEF46A48EBEB', 'BRAUER-05DF137B439F0639', 'BRAUER-27F77BA3CF0A2583']);
const nextGroups = groups.filter(g => g.axes.some(a => a.key === 'tap_holes') || glassFamilies.has(g.id));
let nextStarts = 0;
let nextPhotos = 0;
let hingePairs = 0;
for (const group of nextGroups) {
  for (const product of group.products) {
    const ui = controller(group, product.sku);
    assert.equal(ui.root.dataset.initialized, 'true');
    const buttons = descendants(ui.root).filter(e => e.tagName === 'button');
    for (const button of buttons.filter(e => ['hinge', 'bowl_position'].includes(e.dataset.axis))) {
      const candidates = matches(group, nextState(group, ui.state, button.dataset.axis, button.dataset.value));
      const photos = descendants(button).filter(e => e.tagName === 'img');
      assert.equal(button.disabled, !candidates.length);
      if (candidates.length === 1 && candidates[0].image) {
        assert.equal(photos.length, 1);
        assert.equal(photos[0].dataset.photoSku, candidates[0].sku);
        assert.equal(new URL(photos[0].src).pathname, new URL(candidates[0].image).pathname);
        nextPhotos++;
      } else {
        assert.equal(photos.length, 0);
        if (!candidates.length) assert(button.textContent.includes('Niet beschikbaar'));
      }
    }
    if (product.options.hinge) {
      const options = buttons.filter(e => e.dataset.axis === 'hinge' && !e.disabled);
      if (options.length === 2) {
        const photos = options.map(b => descendants(b).find(e => e.tagName === 'img'));
        assert.notEqual(new URL(photos[0].src).pathname, new URL(photos[1].src).pathname);
        hingePairs++;
      }
    }
    for (const button of buttons.filter(e => e.dataset.axis === 'side')) {
      assert(!descendants(button).some(e => e.tagName === 'img'));
      assert(button.textContent.includes(button.dataset.value + ' cm'));
    }
    for (const button of buttons.filter(e => e.dataset.axis === 'tap_holes')) {
      assert(button.textContent.includes({0: 'Geen kraangat', 1: '1 kraangat', 2: '2 kraangaten'}[button.dataset.value]));
    }
    nextStarts++;
  }
}
assert.equal(nextGroups.length, 25);
assert.equal(nextStarts, 635);
report.extra_groups = nextGroups.length;
report.extra_starts = nextStarts;
report.extra_exact_photos = nextPhotos;
report.distinct_hinge_pairs = hingePairs;
if (reportPath) fs.writeFileSync(reportPath, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report));
