'use strict';
// BC_THEME_PATH must point at the fresh theme export with this release applied.
// Liquid filters below adapt Shopify-only rendering; runtime checks use a small
// event/DOM double. They do not claim full browser layout or cart-network proof.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const base = process.env.BC_THEME_PATH || path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(base, 'assets/bc-sunshower-mobile.js'), 'utf8');
const checks = [];

class Events {
  constructor() { this.events = new Map(); }
  addEventListener(type, listener) {
    if (!this.events.has(type)) this.events.set(type, new Set());
    this.events.get(type).add(listener);
  }
  removeEventListener(type, listener) { this.events.get(type)?.delete(listener); }
  emit(type, event = {}) { for (const fn of this.events.get(type) || []) fn(event); }
  count(type) { return this.events.get(type)?.size || 0; }
}
class Element extends Events {
  constructor(doc, attributes = {}, dataset = {}) {
    super(); this.doc = doc; this.attributes = {...attributes}; this.dataset = dataset;
    this.parent = null; this.hidden = false; this.open = true;
  }
  getAttribute(key) { return this.attributes[key] ?? null; }
  setAttribute(key, value) { this.attributes[key] = String(value); }
  removeAttribute(key) { delete this.attributes[key]; }
  get tabIndex() { return Number(this.getAttribute('tabindex') ?? -1); }
  set tabIndex(value) { this.setAttribute('tabindex', value); }
  closest(selector) { return selector === 'a' && this.getAttribute('href') ? this : this.parent?.closest(selector); }
  contains(target) { for (let n = target; n; n = n.parent) if (n === this) return true; return false; }
  focus(options) { this.doc.activeElement = this; this.lastFocusOptions = options; }
  matches(selector) { return selector === '[data-bcsse-mobile-light]' && Boolean(this.dataset.bcsseSectionId); }
  querySelectorAll() { return []; }
}
function environment({hash = '', mobile = true, legacyMedia = false, readyState = 'complete', minimal = false} = {}) {
  const doc = new Events(); doc.activeElement = null; doc.readyState = readyState;
  const roots = [], mqs = [];
  function root(id) {
    const r = new Element(doc, {}, {bcsseSectionId: id});
    const n = {};
    for (const key of ['overview', 'mobileContent', 'models', 'summary', 'shelf', 'hero', 'title', 'modelControl']) n[key] = new Element(doc);
    n.shelf.setAttribute('tabindex', '0');
    for (const key of Object.keys(n)) n[key].parent = r;
    n.summary.parent = n.models; n.modelControl.parent = n.models;
    n.title.parent = n.hero;
    n.desktopCta = new Element(doc, {href: '/products/one#sunshower-configurator'}); n.desktopCta.parent = n.hero;
    n.ir = new Element(doc, {href: '/products/one#sunshower-configurator'}); n.ir.parent = n.mobileContent;
    n.uv = new Element(doc, {href: '/products/plus#sunshower-configurator'}); n.uv.parent = n.mobileContent;
    n.modelLink = new Element(doc, {href: '#bcsse-models-' + id}); n.modelLink.parent = r;
    n.nestedModelLabel = new Element(doc); n.nestedModelLabel.parent = n.modelLink;
    n.models.querySelector = selector => selector === 'summary' ? n.summary : null;
    const selectors = {'[data-bcsse-light-overview]': n.overview, '.bcsse-mobile-light': n.mobileContent, '[data-bcsse-model-disclosure]': n.models, '[data-bcsse-accessory-shelf]': n.shelf, '.bcsse-hero__copy': n.hero};
    r.querySelector = selector => minimal ? null : selectors[selector] || null;
    r.nodes = n; roots.push(r); return r;
  }
  const alpha = root('alpha'), beta = root('beta');
  doc.querySelectorAll = () => roots;
  doc.getElementById = id => minimal ? null : roots.find(r => id === 'bcsse-title-' + r.dataset.bcsseSectionId)?.nodes.title || null;
  const win = new Events(); win.location = {hash};
  win.matchMedia = () => {
    const mq = new Events(); mq.matches = mobile;
    if (legacyMedia) {
      mq.addListener = listener => Events.prototype.addEventListener.call(mq, 'change', listener);
      mq.removeListener = listener => Events.prototype.removeEventListener.call(mq, 'change', listener);
      mq.addEventListener = undefined; mq.removeEventListener = undefined;
    }
    mqs.push(mq); return mq;
  };
  // Navigation/history interception would be a regression: no history API is
  // supplied, and preventDefault is checked on both plain and modifier clicks.
  const context = {window: win, document: doc, Map, Array};
  vm.runInNewContext(source, context);
  function click(r, target, overrides = {}) {
    const event = {target, button: 0, defaultPrevented: false, preventDefault() { this.defaultPrevented = true; }, ...overrides};
    r.emit('click', event); return event;
  }
  function resize(index, matches) { mqs[index].matches = matches; mqs[index].emit('change'); }
  return {doc, win, roots, alpha, beta, mqs, click, resize, context};
}
function controllers() {
  let e = environment(), n = e.alpha.nodes;
  assert.equal(n.models.open, false); assert.equal(n.overview.hidden, false); assert.equal(n.shelf.tabIndex, 0);
  for (const card of [n.ir, n.uv]) {
    for (const modifiers of [{}, {ctrlKey: true}, {metaKey: true}, {shiftKey: true}, {button: 1}]) assert.equal(e.click(e.alpha, card, modifiers).defaultPrevented, false);
  }
  assert.equal(n.ir.getAttribute('href'), '/products/one#sunshower-configurator');
  assert.equal(n.uv.getAttribute('href'), '/products/plus#sunshower-configurator');
  assert.equal(e.win.location.hash, ''); assert.equal(e.doc.activeElement, null);
  checks.push('IR and UV links remain native with correct seeds, plain/modifier/middle clicks, no history or focus interception');
  for (const hash of ['#bcsse-light-infrared-alpha', '#bcsse-light-uv-alpha', '#bcsse-lights-alpha', '#bcsse-accessories-alpha', '']) {
    e.win.location.hash = hash; e.win.emit('hashchange'); e.win.emit('popstate');
    assert.equal(n.overview.hidden, false); assert.equal(e.alpha.dataset.bcsseLightView, undefined);
    assert.equal(e.doc.activeElement, null);
  }
  checks.push('Obsolete detail hashes, accessory anchors and browser Back never hide direct cards or steal focus');
  assert.equal(e.click(e.alpha, n.nestedModelLabel).defaultPrevented, false); assert.equal(n.models.open, true);
  n.models.open = false; e.win.location.hash = '#bcsse-models-alpha'; e.win.emit('hashchange'); assert.equal(n.models.open, true); assert.equal(e.beta.nodes.models.open, false);
  checks.push('Nested model-anchor click opens only its own native disclosure; hashchange/Back opens target');
  n.ir.focus(); e.resize(0, false); assert.equal(e.doc.activeElement, n.title); assert.equal(n.title.lastFocusOptions.preventScroll, true);
  assert.equal(n.models.open, true); assert.equal(n.shelf.tabIndex, -1); assert.equal(n.overview.hidden, false);
  e.win.location.hash = ''; n.desktopCta.focus(); e.resize(0, true); assert.equal(e.doc.activeElement, n.title); assert.equal(n.models.open, false); assert.equal(n.shelf.tabIndex, 0);
  checks.push('Viewport change keeps desktop models open, phone models closed and shelf keyboard access appropriate; hidden card/hero focus moves without scrolling');
  e.resize(0, false); n.modelControl.focus(); e.resize(0, true); assert.equal(e.doc.activeElement, n.summary); assert.equal(n.summary.lastFocusOptions.preventScroll, true);
  e.resize(0, false); n.summary.focus(); e.resize(0, true); n.summary.focus(); e.resize(0, false); assert.equal(e.doc.activeElement, n.title);
  e.win.location.hash = '#bcsse-models-alpha'; n.modelControl.focus(); e.resize(0, true); assert.equal(n.models.open, true); assert.equal(e.doc.activeElement, n.modelControl);
  n.shelf.focus(); e.resize(0, false); assert.equal(e.doc.activeElement, n.title);
  checks.push('Closing mobile models moves inner focus to summary; hidden desktop summary/shelf moves to title; deep-linked open model controls retain focus');
  e.win.BCSunshowerMobileLight.init(e.doc); vm.runInNewContext(source, e.context);
  assert.equal(e.alpha.count('click'), 1); assert.equal(e.beta.count('click'), 1); assert.equal(e.mqs.length, 2);
  assert.equal(e.win.count('hashchange'), 2); assert.equal(e.win.count('popstate'), 2);
  checks.push('Repeated initialization and repeated script loading install one controller per root');
  e.doc.emit('shopify:section:unload', {target: e.alpha}); assert.equal(e.alpha.count('click'), 0); assert.equal(e.mqs[0].count('change'), 0);
  assert.equal(e.win.count('hashchange'), 1); assert.equal(n.shelf.getAttribute('tabindex'), '0'); assert.equal(n.models.open, true); assert.equal(n.overview.hidden, false);
  assert.equal(e.alpha.dataset.bcsseMobileReady, undefined); assert.equal(e.beta.dataset.bcsseMobileReady, 'true');
  e.doc.emit('shopify:section:load', {target: e.alpha}); assert.equal(e.alpha.count('click'), 1);
  const container = {contains: target => target === e.alpha || target === e.beta};
  e.doc.emit('shopify:section:unload', {target: container}); assert.equal(e.win.count('hashchange'), 0); assert.equal(e.win.count('popstate'), 0);
  checks.push('Editor root/container unload removes listeners and restores native shelf/model fallback; reload remains isolated');
  e = environment({hash: '#bcsse-light-uv-alpha'}); assert.equal(e.alpha.nodes.overview.hidden, false); assert.equal(e.alpha.nodes.models.open, false);
  e = environment({hash: '#bcsse-models-alpha'}); assert.equal(e.alpha.nodes.models.open, true); assert.equal(e.beta.nodes.models.open, false);
  e = environment({mobile: false}); assert.equal(e.alpha.nodes.models.open, true); assert.equal(e.alpha.nodes.shelf.tabIndex, -1);
  checks.push('Cold initialization handles stale detail hash, native model deep link and desktop without transient detail state');
  e = environment({legacyMedia: true}); e.resize(0, false); assert.equal(e.alpha.nodes.shelf.tabIndex, -1); e.doc.emit('shopify:section:unload', {target: e.alpha}); assert.equal(e.mqs[0].count('change'), 0);
  e = environment({minimal: true}); e.resize(0, false); e.win.emit('hashchange'); e.doc.emit('shopify:section:unload', {target: e.alpha});
  e = environment({readyState: 'loading'}); assert.equal(e.alpha.count('click'), 0); e.doc.emit('DOMContentLoaded'); assert.equal(e.alpha.count('click'), 1);
  checks.push('Legacy matchMedia, missing optional nodes and deferred DOM initialization remain safe');
}
async function renderedRoutes() {
  const {Liquid} = require('liquidjs');
  const section = fs.readFileSync(path.join(base, 'sections/bc-sunshower-landing.liquid'), 'utf8').replace(/{% schema %}[\s\S]*?{% endschema %}/, '');
  const esc = x => String(x ?? '').replace(/[&<>\"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
  for (const locale of ['nl', 'en']) {
    const strings = JSON.parse(fs.readFileSync(path.join(base, 'locales', locale === 'nl' ? 'nl.json' : 'en.default.json'), 'utf8').replace(/^\s*\/\*[\s\S]*?\*\/\s*/, ''));
    const engine = new Liquid({strictFilters: true});
    engine.registerFilter('t', key => { const value = String(key).split('.').reduce((v, k) => v?.[k], strings); assert.equal(typeof value, 'string', 'translation ' + key); return value; });
    engine.registerFilter('asset_url', value => '/assets/' + value);
    engine.registerFilter('stylesheet_tag', value => '<link rel="stylesheet" href="' + esc(value) + '">');
    engine.registerFilter('image_url', (value, ...pairs) => value?.src + '?' + new URLSearchParams(Object.fromEntries(pairs)));
    engine.registerFilter('image_tag', (src, ...pairs) => '<img src="' + esc(src) + '" ' + pairs.filter(([key]) => key !== 'widths').map(([key, value]) => key + '="' + esc(value) + '"').join(' ') + '>');
    engine.registerFilter('money', value => '€' + (value / 100).toFixed(2));
    // Actual source dimensions from the CDN readback on 18 October. Keeping
    // distinct ratios catches accidental reuse of one image's crop region.
    const image = {src: '/images/infrared.jpg', width: 1586, height: 992};
    const uvImage = {src: '/images/uv.jpg', width: 2172, height: 724};
    const product = name => ({id: name, url: '/products/' + name, featured_image: image, price: 100});
    const settings = {one_product: product('one'), plus_product: product('plus'), one_image: image, plus_image: uvImage, hero_image: image};
    for (const configuration of [settings, {...settings, configurator_url: '/pages/custom-configurator'}]) {
      const html = await engine.parseAndRender(section, {section: {id: 'fixture', settings: configuration, blocks: []}, pages: {contact: {url: '/pages/contact'}}});
      const cards = [...html.matchAll(/<a\b[^>]*class="[^"]*\bbcsse-light-card\b[^>]*>/g)].map(match => match[0]);
      assert.equal(cards.length, 2);
      const ir = cards.find(card => /bcsse-light-card--infrared/.test(card));
      const uv = cards.find(card => /bcsse-light-card--uv/.test(card));
      assert(ir.includes('href="/products/one#sunshower-configurator"'), 'IR has its actual product seed, independent of generic CTA override');
      assert(uv.includes('href="/products/plus#sunshower-configurator"'), 'UV has PLUS product seed');
      assert(!html.includes('data-bcsse-light-link')); assert(!html.includes('data-bcsse-light-panel'));
      assert(!html.includes('class="bcsse-light-detail')); assert.equal((html.match(/<h1\b/g) || []).length, 1);
      assert(html.includes('data-bcsse-light-overview')); assert(html.includes('data-bcsse-model-disclosure open'));
      const configurator = fs.readFileSync(path.join(base, 'sections/main-sunshower.liquid'), 'utf8');
      assert(configurator.includes('id="sunshower-configurator"'), 'destination anchor exists on actual configurator');
    }
    checks.push(locale + ': rendered direct IR/UV product seeds survive generic CTA override; no intermediate panel/interceptor; actual destination anchor retained');

    for (const [fixture, ir, uv] of [
      ['actual sources', image, uvImage],
      ['small sources', {src: '/images/tiny-ir.jpg', width: 120, height: 80}, {src: '/images/tiny-uv.jpg', width: 90, height: 100}],
      ['portrait sources', {src: '/images/portrait-ir.jpg', width: 240, height: 600}, {src: '/images/portrait-uv.jpg', width: 300, height: 900}]
    ]) {
      const html = await engine.parseAndRender(section, {section: {id: 'photos', settings: {...settings, one_image: ir, plus_image: uv}, blocks: []}, pages: {contact: {url: '/pages/contact'}}});
      const cards = [...html.matchAll(/<a\b[^>]*class="[^"]*\bbcsse-light-card\b[^>]*>[\s\S]*?<\/a>/g)].map(match => match[0]);
      for (const [index, original] of [ir, uv].entries()) {
        const card = cards[index];
        const sourceTag = card.match(/<source\b[^>]*>/)?.[0];
        const srcset = sourceTag?.match(/srcset="([^"]+)"/)?.[1];
        assert(srcset, fixture + ': responsive card source exists');
        assert(sourceTag.includes('media="(max-width: 749px)"'), 'mobile photo stays out of desktop picture selection');
        assert(/<img\b[^>]*loading="eager"[^>]*fetchpriority="high"/.test(card), 'above-fold cards load eagerly at high priority');
        const candidates = srcset.split(',').map(item => {
          const match = item.trim().match(/^(\S+) (\d+)w$/);
          assert(match, 'valid width-descriptor candidate');
          return {url: new URL(match[1].replace(/&amp;/g, '&'), 'https://fixture.invalid'), descriptor: Number(match[2])};
        });
        const widths = candidates.map(candidate => candidate.descriptor);
        assert.equal(new Set(widths).size, widths.length, 'no duplicate width descriptors');
        assert.deepEqual([...widths].sort((a, b) => a - b), widths, 'candidates are ordered');
        for (const {url, descriptor} of candidates) {
          const p = url.searchParams;
          const cropWidth = Number(p.get('crop_width')), cropHeight = Number(p.get('crop_height'));
          const left = Number(p.get('crop_left')), top = Number(p.get('crop_top'));
          assert.equal(url.pathname, original.src, 'each card uses its own source');
          // Shopify Liquid rejects quality overrides for these PNG sources;
          // direct CDN acceptance of the same query is not sufficient proof.
          assert.equal(p.get('crop'), 'region'); assert.equal(p.get('quality'), null);
          assert.equal(Number(p.get('width')), descriptor, 'descriptor matches requested pixels');
          assert(cropWidth > 0 && cropHeight > 0 && left >= 0 && top >= 0, 'positive crop inside source');
          assert(left + cropWidth <= original.width && top + cropHeight <= original.height, 'crop never exceeds actual source');
          assert.equal(cropHeight, original.height); assert.equal(top, 0, 'full image height retained');
          assert(descriptor <= cropWidth, 'never label an upscaled/capped source as a larger candidate');
          const focal = index === 0 ? 0.58 : 0.78;
          assert(Math.abs(left - (original.width - cropWidth) * focal) <= 0.5, 'same horizontal focal point within pixel rounding');
        }
        const maximum = candidates.at(-1);
        assert.equal(maximum.descriptor, Number(maximum.url.searchParams.get('crop_width')), 'last candidate reaches true cropped resolution');
        if (fixture === 'actual sources') {
          const expected = index === 0 ? {width: 893, left: 402} : {width: 652, left: 1186};
          assert.equal(maximum.descriptor, expected.width); assert.equal(Number(maximum.url.searchParams.get('crop_left')), expected.left);
          const sizes = sourceTag.match(/sizes="([^"]+)"/)?.[1];
          assert(sizes, 'responsive display size exists');
          // Image cover sizing depends on card HEIGHT, because the source is
          // wider than these portrait cards. A half-viewport sizes value would
          // select insufficient detail. Check the supplied sizes against the
          // actual min-height clamp over the whole supported phone range.
          const clauses = sizes.split(',').map(value => value.trim());
          function suppliedSize(viewport) {
            for (const clause of clauses) {
              const match = clause.match(/^(?:\(max-width: (\d+)px\) )?([\d.]+)(px|vw)$/);
              assert(match, 'supported responsive sizes clause');
              if (!match[1] || viewport <= Number(match[1])) return Number(match[2]) * (match[3] === 'vw' ? viewport / 100 : 1);
            }
            assert.fail('sizes covers every phone width');
          }
          for (let viewport = 320; viewport <= 749; viewport++) {
            const height = Math.min(400, Math.max(290, viewport * 0.86));
            const cardWidth = (viewport - 2 * (viewport < 360 ? 14 : 18) - (viewport < 360 ? 8 : 10)) / 2;
            const cropRatio = expected.width / original.height;
            assert(cropRatio >= cardWidth / height, 'crop retains every visible pixel at every phone width');
            assert(Math.abs(suppliedSize(viewport) - height * cropRatio) < 0.3, 'sizes reflects effective image width under object-fit:cover');
          }
        }
      }
      checks.push(locale + ': ' + fixture + ' keep valid bounded region crops, honest unique srcset widths, focal points and eager high-priority loading' + (fixture === 'actual sources' ? '; full 320–749px cover-sizing check' : ''));
    }
  }
}
(async () => {
  controllers();
  if (!process.argv.includes('--controller-only')) await renderedRoutes();
  console.log(JSON.stringify({status: 'passed', checks, limitations: 'Controller uses an event/DOM double; Liquid uses Shopify filter adapters. Actual route navigation, viewport layout and photo/network performance require browser checks.'}, null, 2));
})().catch(error => { console.error(error); process.exitCode = 1; });
