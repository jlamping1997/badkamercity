'use strict';
/**
 * Focused gallery regression checks against a downloaded Shopify theme.
 * Usage: NODE_PATH=/path/to/node_modules node scripts/test-sunshower-carousel.cjs /path/to/theme
 * LiquidJS adapters model Shopify image/translation helpers; native HTML/CSS,
 * scroll physics, PhotoSwipe gesture/zoom and physical touch still require browser QA.
 */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { Liquid } = require('liquidjs');

const themeRoot = path.resolve(process.argv[2] || path.join(__dirname, '..'));
const source = fs.readFileSync(path.join(themeRoot, 'assets/bc-sunshower-page.js'), 'utf8');
const section = fs.readFileSync(path.join(themeRoot, 'sections/main-sunshower.liquid'), 'utf8');
const css = fs.readFileSync(path.join(themeRoot, 'assets/bc-sunshower-configurator.css'), 'utf8');
const checks = [];
const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const attributes = tag => Object.fromEntries([...tag.matchAll(/([\w:-]+)(?:="([^"]*)")?/g)].map(m => [m[1], m[2] ?? '']));
const has = (tag, name) => Object.hasOwn(attributes(tag), name);
const tags = html => [...html.matchAll(/<([a-z][\w-]*)\b[^>]*>/gi)].map(m => ({ name: m[1], raw: m[0], attrs: attributes(m[0]) }));
const byAttribute = (html, name) => tags(html).filter(t => Object.hasOwn(t.attrs, name));
const image = index => {
  const width = index === 2 ? 1600 : 1075, height = index === 2 ? 1066 : 1613;
  return { src: `https://cdn.shopify.com/files/photo-${index}.jpg?v=1`, width, height, aspect_ratio: width / height };
};
const translate = (locale, key, pairs) => {
  const strings = JSON.parse(fs.readFileSync(path.join(themeRoot, 'locales', locale === 'nl' ? 'nl.json' : 'en.default.json'), 'utf8').replace(/^\s*\/\*[\s\S]*?\*\/\s*/, ''));
  let text = key.split('.').reduce((value, part) => value?.[part], strings);
  assert.equal(typeof text, 'string', `${locale}: translation ${key} exists`);
  for (const [name, value] of pairs) text = text.replaceAll(`{{ ${name} }}`, value).replaceAll(`{{${name}}}`, value);
  assert(!text.includes('{{'), `${locale}: translation arguments resolved for ${key}`);
  return text;
};

async function renderGallery(locale, count, sectionId = 'fixture') {
  const start = section.search(/<div\b[^>]*class="ss-gallery"/);
  const end = section.indexOf('<div class="ss-buybox', start);
  assert(start >= 0 && end > start, 'production Liquid gallery block is extractable');
  const production = section.slice(start, end);
  const photos = Array.from({ length: count }, (_, index) => ({ media_type: 'image', preview_image: image(index) }));
  const engine = new Liquid({ strictFilters: true });
  engine.registerFilter('t', (key, ...pairs) => translate(locale, key, pairs));
  engine.registerFilter('asset_url', value => `/assets/${value}`);
  engine.registerFilter('image_url', (value, ...pairs) => {
    assert(value?.src, 'image_url receives a real fixture image');
    return `${value.src}&width=${Object.fromEntries(pairs).width}`;
  });
  engine.registerFilter('image_tag', (src, ...pairs) => {
    const options = Object.fromEntries(pairs);
    const width = Number(new URL(src).searchParams.get('width'));
    const srcset = options.widths ? String(options.widths).split(',').map(n => `${src.replace(/width=\d+/, `width=${n.trim()}`)} ${n.trim()}w`).join(', ') : '';
    return `<img src="${escape(src)}"${srcset ? ` srcset="${escape(srcset)}"` : ''} ${pairs.filter(([key]) => key !== 'widths').map(([key, value]) => `${key}="${escape(value)}"`).join(' ')} data-adapter-request-width="${width}">`;
  });
  return engine.parseAndRender(production, {
    photos, first_photo: photos[0], section: { id: sectionId },
    product: { title: 'Sunshower "One" < & >', media: [...photos, { media_type: 'video' }] },
  });
}

function assertNoNestedButtons(html) {
  let depth = 0;
  for (const m of html.matchAll(/<\/?button\b[^>]*>/gi)) {
    if (m[0].startsWith('</')) depth--;
    else { assert.equal(depth, 0, 'buttons cannot be nested'); depth++; }
    assert(depth >= 0, 'balanced button tags');
  }
  assert.equal(depth, 0, 'button tags are balanced');
}

async function liquidChecks() {
  for (const locale of ['nl', 'en']) {
    for (const count of [0, 1, 5]) {
      const html = await renderGallery(locale, count);
      assertNoNestedButtons(html);
      assert(!/translation missing|NaN|undefined/.test(html), `${locale}/${count}: rendered values valid`);
      const slides = byAttribute(html, 'data-ss-gallery-slide');
      assert.equal(slides.length, count, `${locale}/${count}: one slide per photo`);
      assert.equal(byAttribute(html, 'data-ss-gallery-viewport').length, 1, 'one native viewport');
      assert.equal(new Set(tags(html).filter(t => t.attrs.id).map(t => t.attrs.id)).size, tags(html).filter(t => t.attrs.id).length, 'unique IDs within gallery');
      for (const [index, slide] of slides.entries()) {
        assert.equal(slide.name, 'a', 'each slide has a native full-image fallback link');
        assert(slide.attrs.href?.startsWith('https://cdn.shopify.com/files/photo-'), 'fallback targets real image');
        assert(Number(slide.attrs['data-ss-width']) > 0 || Number(slide.attrs['data-ss-photo-width']) > 0 || Number(slide.attrs['data-ss-full-width']) > 0, 'PhotoSwipe receives positive source width');
        assert(Number(slide.attrs['data-ss-height']) > 0 || Number(slide.attrs['data-ss-photo-height']) > 0 || Number(slide.attrs['data-ss-full-height']) > 0, 'PhotoSwipe receives positive source height');
        assert(slide.attrs['aria-label'], 'full-image link has accessible name');
        assert(slide.attrs['data-ss-full-srcset']?.includes('w'), 'full-size viewer has responsive source candidates');
        const original = image(index), width = Math.min(original.width, 2400);
        assert.equal(Number(slide.attrs['data-ss-photo-width']), width, 'viewer dimensions describe actual capped image');
        assert.equal(Number(slide.attrs['data-ss-photo-height']), Math.round(width / original.aspect_ratio), 'viewer aspect ratio matches this image rather than first image');
        const candidates = slide.attrs['data-ss-full-srcset'].replaceAll('&amp;', '&').split(',').map(part => part.trim().split(/\s+/));
        let previousWidth = 0;
        for (const [url, descriptor] of candidates) {
          const candidateWidth = Number(descriptor.replace(/w$/, ''));
          assert(candidateWidth > previousWidth && candidateWidth <= width, 'srcset candidates increase within actual source width');
          assert.equal(Number(new URL(url).searchParams.get('width')), candidateWidth, 'srcset descriptor matches requested CDN width');
          previousWidth = candidateWidth;
        }
        assert.equal(previousWidth, width, 'full-resolution source is final candidate');
      }
      const photos = tags(html).filter(t => t.name === 'img' && /\bss-gallery__photo\b/.test(t.attrs.class || ''));
      assert.equal(photos.length, count, 'each slide owns its own image node');
      photos.forEach((photo, index) => {
        assert(photo.attrs.srcset?.includes('w'), 'responsive image sources retained');
        assert(photo.attrs.sizes, 'responsive sizes supplied');
        assert.equal(photo.attrs.alt, 'Sunshower &quot;One&quot; &lt; &amp; &gt;', 'product title escaped in image alt');
        assert.notEqual(photo.attrs.draggable, 'true', 'native image dragging is not explicitly enabled');
        assert.equal(photo.attrs.loading, index === 0 ? 'eager' : 'lazy', 'only first large image is eager');
        if (index === 0) assert.equal(photo.attrs.fetchpriority, 'high', 'initial photo gets high priority');
        else assert.notEqual(photo.attrs.fetchpriority, 'high', 'later photos do not compete with initial photo priority');
      });
      const thumbs = byAttribute(html, 'data-ss-photo');
      assert.equal(thumbs.length, count > 1 ? count : 0, 'thumbnails only shown for multiple photos');
      if (thumbs.length) {
        assert.equal(thumbs.filter(t => t.attrs['aria-pressed'] === 'true').length, 1, 'single initial thumb selected');
        thumbs.forEach((thumb, index) => {
          assert.equal(thumb.name, 'button'); assert.equal(thumb.attrs.type, 'button');
          assert.equal(thumb.attrs['data-ss-photo-index'], String(index), 'thumbnail index corresponds to actual image');
          assert(thumb.attrs['aria-label'], 'thumbnail has translated accessible name');
        });
      }
      const previous = byAttribute(html, 'data-ss-gallery-previous');
      const next = byAttribute(html, 'data-ss-gallery-next');
      for (const control of [...previous, ...next, ...byAttribute(html, 'data-ss-gallery-expand')]) {
        assert.equal(control.name, 'button'); assert.equal(control.attrs.type, 'button');
        assert(control.attrs['aria-label'], 'arrow/expand has translated accessible name');
      }
      assert.equal(previous.length, next.length, 'navigation buttons are paired');
      if (count > 1) assert.equal(previous.length, 1, 'multiple photos have visible navigation controls');
      checks.push(`${locale}: ${count} images: Liquid links/images, accessible controls, unique IDs, responsive/loading contract and no nested buttons`);
    }
  }
  assert(/scroll-snap-type\s*:\s*x\s+mandatory/.test(css), 'native horizontal snap provides thumb-following movement');
  assert(/scroll-snap-align\s*:\s*start/.test(css), 'each image snaps to its start');
  assert(!/touch-action\s*:\s*none/.test(css), 'main gallery does not block native vertical scrolling/pinch');
  checks.push('CSS retains native horizontal snap and does not disable all touch actions');
  const rules = [...css.matchAll(/([^{}]+)\{([^{}]*)\}/g)];
  for (const className of ['pswp__bg', 'pswp__img--placeholder']) {
    assert(rules.some(([, selectors, declarations]) => selectors.split(',').some(selector => selector.includes('.bc-ss-viewer') && selector.includes(`.${className}`)) && /(?:^|;)\s*display\s*:\s*block\s*(?:;|$)/.test(declarations)), `viewer ${className} explicitly survives Dawn div:empty display:none`);
  }
  checks.push('PhotoSwipe empty background/placeholder remain visible despite Dawn empty-div reset');
}

class Element {
  constructor() {
    this.dataset = {};
    this.attributeMap = new Map();
    this.listeners = new Map();
    this.isConnected = true;
    this.children = [];
    this.scrollLeft = 0;
    this.scrollCalls = [];
    this.bounds = { left: 0, right: 400, top: 0, bottom: 600, width: 400, height: 600 };
    this.style = {};
    this.classList = {
      toggle: (name, active) => {
        const values = new Set((this.getAttribute('class') || '').split(/\s+/).filter(Boolean));
        if (active) values.add(name); else values.delete(name);
        this.setAttribute('class', [...values].join(' '));
      },
      contains: name => (this.getAttribute('class') || '').split(/\s+/).includes(name),
      add: name => this.classList.toggle(name, true),
      remove: name => this.classList.toggle(name, false),
    };
  }
  setAttribute(name, value) { this.attributeMap.set(name, String(value)); }
  getAttribute(name) { return this.attributeMap.get(name) ?? null; }
  removeAttribute(name) { this.attributeMap.delete(name); }
  hasAttribute(name) { return this.attributeMap.has(name); }
  addEventListener(name, listener) {
    this.listeners.set(name, [...(this.listeners.get(name) || []), listener]);
  }
  removeEventListener(name, listener) {
    this.listeners.set(name, (this.listeners.get(name) || []).filter(other => other !== listener));
  }
  emit(name, event = {}) {
    const dispatched = { target: this, currentTarget: this, defaultPrevented: false, preventDefault() { this.defaultPrevented = true; }, stopPropagation() { this.propagationStopped = true; }, ...event };
    for (const listener of this.listeners.get(name) || []) listener(dispatched);
    return dispatched;
  }
  click(detail = 1, extra = {}) { return this.disabled ? null : this.emit('click', { detail, button: 0, ...extra }); }
  getBoundingClientRect() { return this.bounds; }
  scrollTo(options) { this.scrollCalls.push(options); if (options.behavior !== 'smooth') this.scrollLeft = options.left; }
  scrollBy(options) { this.scrollCalls.push(options); }
  focus(options) { this.focusOptions = options; this.focused = true; }
  setPointerCapture(id) { this.capturedPointer = id; }
  releasePointerCapture(id) { if (this.capturedPointer === id) this.capturedPointer = null; }
  contains(node) { return node === this || this.children.some(child => child.contains(node)); }
}

const blockStart = source.indexOf("      const gallery = page.querySelector('[data-ss-gallery]');");
const blockEnd = source.indexOf('      const description =', blockStart);
assert(blockStart >= 0 && blockEnd > blockStart, 'actual production carousel block must be present');
// The only substituted operation is the external ES-module loader. Everything
// controlling selection, gestures, arrows and viewer lifecycle runs unchanged.
const galleryScript = new vm.Script(source.slice(blockStart, blockEnd).replace(/\bimport\(/g, '__import('), { filename: 'bc-sunshower-page.js:carousel' });
const flush = async () => { for (let i = 0; i < 5; i++) await Promise.resolve(); };

function fixture({ count = 3, initial = 0, width = 400, reducedMotion = false, deferredImport = false, importFails = false, complete = true, initiallyBroken = [] } = {}) {
  const gallery = new Element(), viewport = new Element(), previous = new Element(), next = new Element(), counter = new Element(), expand = new Element(), strip = new Element();
  const page = new Element(), window = new Element();
  gallery.dataset = { viewerModule: '/assets/bc-photoswipe.esm.js', closeLabel: 'Sluiten', zoomLabel: 'Inzoomen', previousLabel: 'Vorige foto', nextLabel: 'Volgende foto', loadError: 'Foto kon niet worden geladen.', galleryLabel: 'Productfoto’s' };
  viewport.clientWidth = width; viewport.scrollLeft = initial * width;
  const slides = Array.from({ length: count }, (_, index) => {
    const slide = new Element(), img = new Element(), error = new Element();
    slide.offsetLeft = index * width;
    slide.href = `https://cdn.shopify.com/files/photo-${index}.jpg?v=1&width=2400`;
    slide.dataset = { ssFullSrcset: `${slide.href} 2400w`, ssPhotoWidth: '1075', ssPhotoHeight: '1613', ssPhotoAlt: `Photo ${index + 1}` };
    img.src = `https://cdn.shopify.com/files/photo-${index}.jpg?v=1&width=720`;
    img.currentSrc = img.src; img.alt = `Photo ${index + 1}`;
    img.complete = initiallyBroken.includes(index) || complete; img.naturalWidth = complete && !initiallyBroken.includes(index) ? 720 : 0;
    error.hidden = true;
    slide.querySelector = selector => selector === 'img' ? img : selector === '[data-ss-photo-error]' ? error : null;
    slide.closest = selector => selector === '[data-ss-open-image]' ? slide : null;
    img.closest = slide.closest;
    slide.children = [img, error]; slide.image = img; slide.error = error;
    return slide;
  });
  const thumbs = count > 1 ? slides.map((slide, index) => {
    const thumb = new Element(); thumb.dataset.ssPhoto = slide.href; thumb.dataset.ssPhotoIndex = String(index); return thumb;
  }) : [];
  viewport.children = slides;
  const selectors = new Map([
    ['[data-ss-gallery-viewport]', viewport], ['[data-ss-gallery-previous]', count > 1 ? previous : null],
    ['[data-ss-gallery-next]', count > 1 ? next : null], ['[data-ss-gallery-current]', counter],
    ['[data-ss-gallery-expand]', expand], ['.ss-gallery__thumbs', count > 1 ? strip : null],
  ]);
  gallery.querySelector = selector => selectors.get(selector) ?? null;
  gallery.querySelectorAll = selector => selector === '[data-ss-gallery-slide]' ? slides : selector === '[data-ss-photo]' ? thumbs : [];
  page.querySelector = selector => selector === '[data-ss-gallery]' ? gallery : null;
  window.matchMedia = () => ({ matches: reducedMotion });
  const observers = [];
  class ResizeObserver {
    constructor(callback) { this.callback = callback; observers.push(this); }
    observe(element) { this.element = element; }
  }
  const timers = new Map(); let timerId = 0;
  const setTimeout = callback => { timers.set(++timerId, callback); return timerId; };
  const clearTimeout = id => timers.delete(id);
  const viewers = [];
  class PhotoSwipe {
    constructor(options) { this.options = options; this.currIndex = options.index; this.listeners = new Map(); this.element = new Element(); viewers.push(this); }
    on(name, callback) { this.listeners.set(name, [...(this.listeners.get(name) || []), callback]); }
    dispatch(name) { for (const callback of this.listeners.get(name) || []) callback(); }
    init() { this.initialized = true; this.dispatch('change'); this.dispatch('afterInit'); }
    goTo(index) { this.currIndex = Math.max(0, Math.min(this.options.dataSource.length - 1, index)); this.dispatch('change'); }
    close() { this.dispatch('destroy'); }
  }
  const imports = [], assignments = [];
  let resolveImport, rejectImport;
  const __import = url => {
    imports.push(url);
    if (deferredImport) return new Promise((resolve, reject) => { resolveImport = resolve; rejectImport = reject; });
    return importFails ? Promise.reject(new Error('module unavailable')) : Promise.resolve({ default: PhotoSwipe });
  };
  const location = { href: 'https://badkamercity.nl/products/sunshower', assign: url => assignments.push(url) };
  galleryScript.runInNewContext({ page, window, ResizeObserver, URL, location, setTimeout, clearTimeout, __import });
  const selected = index => {
    assert.equal(counter.textContent, String(index + 1), 'counter represents currently shown slide');
    thumbs.forEach((thumb, number) => {
      assert.equal(thumb.getAttribute('aria-pressed'), String(number === index), 'thumb aria matches visible slide');
      assert.equal(thumb.classList.contains('is-selected'), number === index, 'thumb visual selection matches visible slide');
    });
    slides.forEach((slide, number) => {
      assert.equal(slide.tabIndex, number === index ? 0 : -1, 'only actual slide is keyboard focusable');
      assert.equal(slide.getAttribute('aria-hidden'), String(number !== index), 'offscreen slides hidden from assistive technology');
    });
    if (count > 1) { assert.equal(previous.disabled, index === 0); assert.equal(next.disabled, index === count - 1); }
  };
  const settle = left => { viewport.scrollLeft = left; viewport.emit('scroll'); viewport.emit('scrollend'); };
  const clickSlide = (index, options = {}) => viewport.emit('click', { target: slides[index], detail: 1, button: 0, ...options });
  const pointer = (name, options = {}) => viewport.emit(name, { pointerId: 1, pointerType: 'touch', isPrimary: true, clientX: 200, clientY: 200, button: 0, ...options });
  return {
    page, window, gallery, viewport, previous, next, counter, expand, strip, slides, thumbs, viewers, imports, assignments, selected, settle, clickSlide, pointer,
    resize: size => { viewport.clientWidth = size; slides.forEach((slide, index) => { slide.offsetLeft = index * size; }); observers.forEach(observer => observer.callback()); },
    runTimers: () => { for (const [id, callback] of [...timers]) { timers.delete(id); callback(); } },
    resolveImport: () => resolveImport({ default: PhotoSwipe }), rejectImport: () => rejectImport(new Error('module unavailable')),
  };
}

const behaviorCases = {
  'initial/restored native position sets exactly matching thumbnail, count and focusable slide': async () => {
    const f = fixture({ initial: 2 }); f.selected(2); assert.equal(f.imports.length, 0, 'viewer is not downloaded during page initialization');
  },
  'arrow navigation keeps actual selection until native scroll crosses halfway': async () => {
    const f = fixture(); f.next.click();
    assert.equal(f.viewport.scrollCalls.at(-1).left, 400); assert.equal(f.viewport.scrollCalls.at(-1).behavior, 'smooth');
    f.selected(0); f.viewport.scrollLeft = 180; f.viewport.emit('scroll'); f.selected(0);
    f.viewport.scrollLeft = 230; f.viewport.emit('scroll'); f.selected(1);
    f.settle(400); f.selected(1);
  },
  'rapid arrows accumulate intent while selection follows rendered native position': async () => {
    const f = fixture(); f.next.click(); f.next.click();
    assert.equal(f.viewport.scrollCalls.at(-1).left, 800, 'second click advances past pending target');
    f.selected(0); f.settle(800); f.selected(2);
    f.previous.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 400); f.settle(400); f.selected(1);
  },
  'a late scrollend from an interrupted smooth scroll cannot erase a newer arrow destination': async () => {
    const f = fixture({ count: 5, initial: 1 });
    f.next.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 800);
    // Native browsers may dispatch scrollend for the previous/aborted smooth
    // scroll before the next smooth operation has moved from the old slide.
    f.viewport.emit('scrollend'); f.selected(1);
    f.next.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 1200, 'second click advances to photo 4 even before photo 3 has arrived');
    f.settle(1200); f.selected(3);
  },
  'settle fallback cannot erase an unarrived arrow destination': async () => {
    const f = fixture({ count: 5, initial: 1 }); f.next.click(); f.runTimers(); f.selected(1);
    f.next.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 1200);
    f.settle(1200); f.previous.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 800, 'actual arrival releases the old intent');
  },
  'boundaries clamp and have disabled navigation rather than wrapping': async () => {
    const f = fixture(); assert.equal(f.previous.disabled, true); f.previous.click(); assert.equal(f.viewport.scrollCalls.length, 0);
    f.next.click(); f.settle(400); f.next.click(); f.settle(800); f.selected(2);
    assert.equal(f.next.disabled, true); const calls = f.viewport.scrollCalls.length; f.next.click(); assert.equal(f.viewport.scrollCalls.length, calls);
    f.viewport.emit('keydown', { key: 'ArrowRight' }); assert.equal(f.viewport.scrollCalls.at(-1).left, 800); f.selected(2);
  },
  'thumbnail uses its actual slide and partial canceled scroll restores actual selection': async () => {
    const f = fixture(); f.thumbs[2].click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 800); f.selected(0);
    f.pointer('pointerdown'); f.settle(400); f.selected(1); f.next.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 800);
  },
  'manual input interrupts pending arrow intent and next arrow starts from actual position': async () => {
    const f = fixture(); f.next.click(); f.next.click(); f.pointer('pointerdown'); f.next.click();
    assert.equal(f.viewport.scrollCalls.at(-1).left, 400);
  },
  'scroll-end fallback reconciles actual geometry after deliberate manual cancellation': async () => {
    const f = fixture(); f.next.click(); f.next.click(); f.pointer('pointerdown'); f.viewport.scrollLeft = 400; f.viewport.emit('scroll'); f.runTimers(); f.selected(1);
    f.previous.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, 0);
  },
  'horizontal trackpad wheel cancels arrow intent while ordinary vertical wheel preserves it': async () => {
    for (const horizontal of [true, false]) {
      const f = fixture({ count: 5, initial: 1 }); f.next.click(); f.next.click();
      f.viewport.scrollLeft = 800; f.viewport.emit('scroll'); f.selected(2);
      f.viewport.emit('wheel', { deltaX: horizontal ? 50 : 0, deltaY: horizontal ? 0 : 50 });
      f.next.click(); assert.equal(f.viewport.scrollCalls.at(-1).left, horizontal ? 1200 : 1600);
    }
  },
  'Arrow keys work, unrelated keys preserve normal page behavior': async () => {
    const f = fixture(); assert.equal(f.viewport.emit('keydown', { key: 'ArrowRight' }).defaultPrevented, true);
    assert.equal(f.viewport.scrollCalls.at(-1).left, 400);
    assert.equal(f.viewport.scrollCalls.at(-1).behavior, 'instant', 'keyboard navigation does not leave focus on an aria-hidden sliding anchor');
    assert.equal(f.slides[1].focused, true); assert.equal(f.slides[1].focusOptions.preventScroll, true); f.selected(1);
    assert.equal(f.viewport.emit('keydown', { key: 'Tab' }).defaultPrevented, false);
  },
  'reduced motion uses instant navigation and immediately matching selection': async () => {
    const f = fixture({ reducedMotion: true }); f.next.click();
    assert.equal(f.viewport.scrollCalls.at(-1).behavior, 'instant'); f.selected(1);
  },
  'responsive resize preserves selected image without animating to another image': async () => {
    const f = fixture({ initial: 1 }); f.resize(500); f.selected(1);
    assert.equal(f.viewport.scrollCalls.at(-1).left, 500); assert.equal(f.viewport.scrollCalls.at(-1).behavior, 'instant');
    const calls = f.viewport.scrollCalls.length; f.resize(500); assert.equal(f.viewport.scrollCalls.length, calls);
  },
  'thumbnail reveal scrolls only its strip without scrolling the document': async () => {
    const f = fixture(); f.strip.bounds = { left: 0, right: 200 }; f.thumbs[2].bounds = { left: 250, right: 330 }; f.settle(800);
    assert(f.strip.scrollCalls.length >= 1); assert(f.strip.scrollCalls.every(call => call.left === 130));
  },
  'drag release suppresses enlargement, while next deliberate tap opens current image': async () => {
    const f = fixture(); f.pointer('pointerdown'); f.pointer('pointermove', { clientX: 120 }); f.pointer('pointerup', { clientX: 120 });
    const result = f.clickSlide(0); assert.equal(result.defaultPrevented, true); await flush(); assert.equal(f.viewers.length, 0);
    f.pointer('pointerdown'); f.pointer('pointerup'); f.clickSlide(0); await flush(); assert.equal(f.viewers.length, 1);
  },
  'vertical drags and native scroll displacement cannot accidentally open enlargement': async () => {
    for (const movement of ['vertical', 'scroll']) {
      const f = fixture(); f.pointer('pointerdown');
      if (movement === 'vertical') f.pointer('pointermove', { clientY: 280 }); else f.viewport.scrollLeft = 20;
      f.pointer('pointerup'); f.clickSlide(0); await flush(); assert.equal(f.viewers.length, 0);
    }
  },
  'cancelled gesture suppresses click but keyboard activation remains available': async () => {
    const f = fixture(); f.pointer('pointerdown'); f.pointer('pointercancel'); f.clickSlide(0); await flush(); assert.equal(f.viewers.length, 0);
    f.clickSlide(0, { detail: 0 }); await flush(); assert.equal(f.viewers.length, 1);
  },
  'modified image clicks retain normal native link behavior': async () => {
    const f = fixture();
    for (const options of [{ ctrlKey: true }, { metaKey: true }, { shiftKey: true }, { altKey: true }, { button: 1 }]) assert.equal(f.clickSlide(0, options).defaultPrevented, false);
    await flush(); assert.equal(f.imports.length, 0);
  },
  'native image dragging is prevented but pointer movement is passive': async () => {
    const f = fixture(); assert.equal(f.viewport.emit('dragstart').defaultPrevented, true);
    f.pointer('pointerdown'); assert.equal(f.pointer('pointermove', { clientY: 280 }).defaultPrevented, false);
  },
  'an image failure has explicit per-slide state and a successful retry clears it': async () => {
    const f = fixture({ complete: false }); f.slides[1].image.emit('error');
    assert.equal(f.slides[1].error.hidden, false); assert.equal(f.slides[1].classList.contains('has-photo-error'), true);
    f.slides[1].image.emit('load'); assert.equal(f.slides[1].error.hidden, true); assert.equal(f.slides[1].classList.contains('has-photo-error'), false);
  },
  'initial already-broken image is reported without another load event': async () => {
    const f = fixture({ initiallyBroken: [0] });
    assert.equal(f.slides[0].error.hidden, false); assert.equal(f.slides[0].classList.contains('has-photo-error'), true);
    assert.equal(f.slides[1].error.hidden, true, 'healthy cached image is not flagged broken');
  },
  'viewer opens current image with responsive metadata and touch/navigation options': async () => {
    const f = fixture({ initial: 1 }); f.expand.click(); await flush();
    const viewer = f.viewers[0]; assert(viewer?.initialized); assert.equal(viewer.options.index, 1);
    assert.equal(viewer.options.loop, false); assert.equal(viewer.options.allowPanToNext, false);
    assert.equal(viewer.options.arrowPrev, true); assert.equal(viewer.options.arrowNext, true); assert.equal(viewer.options.counter, true);
    assert.equal(viewer.options.trapFocus, true); assert.equal(viewer.options.returnFocus, true); assert.equal(viewer.options.pinchToClose, false);
    assert.equal(viewer.options.dataSource[1].src, f.slides[1].href); assert.equal(viewer.options.dataSource[1].srcset, f.slides[1].dataset.ssFullSrcset);
    assert.equal(viewer.options.dataSource[1].width, 1075); assert.equal(viewer.options.dataSource[1].height, 1613);
    assert.equal(viewer.element.getAttribute('aria-modal'), 'true'); assert.equal(viewer.element.getAttribute('aria-label'), 'Productfoto’s');
    assert.equal(viewer.options.closeTitle, 'Sluiten'); assert.equal(viewer.options.arrowPrevTitle, 'Vorige foto'); assert.equal(viewer.options.arrowNextTitle, 'Volgende foto');
  },
  'reduced-motion preference also removes custom viewer animation durations': async () => {
    const f = fixture({ reducedMotion: true }); f.expand.click(); await flush();
    const options = f.viewers[0].options;
    assert.equal(options.showAnimationDuration, 0); assert.equal(options.hideAnimationDuration, 0); assert.equal(options.zoomAnimationDuration, 0);
  },
  'viewer image changes sync page immediately and closing returns focus to selected image': async () => {
    const f = fixture(); f.clickSlide(0); await flush(); const viewer = f.viewers[0];
    viewer.goTo(2); f.selected(2); assert.equal(f.viewport.scrollCalls.at(-1).left, 800); assert.equal(f.viewport.scrollCalls.at(-1).behavior, 'instant');
    viewer.close(); f.selected(2); assert.equal(f.slides[2].focused, true); assert.equal(f.slides[2].focusOptions.preventScroll, true);
  },
  'expand-triggered viewer restores focus to expand control': async () => {
    const f = fixture(); f.expand.click(); await flush(); f.viewers[0].goTo(1); f.viewers[0].close(); assert.equal(f.expand.focused, true); f.selected(1);
  },
  'multiple opens while module downloads create one viewer at latest requested index': async () => {
    const f = fixture({ deferredImport: true }); f.clickSlide(0); f.clickSlide(2); assert.equal(f.imports.length, 1); assert.equal(f.viewers.length, 0);
    f.resolveImport(); await flush(); assert.equal(f.viewers.length, 1); assert.equal(f.viewers[0].currIndex, 2); f.selected(2);
  },
  'existing viewer is reused and cached module is reused after close': async () => {
    const f = fixture(); f.clickSlide(0); await flush(); f.clickSlide(2); await flush();
    assert.equal(f.viewers.length, 1); assert.equal(f.viewers[0].currIndex, 2); f.viewers[0].close(); f.expand.click(); await flush();
    assert.equal(f.viewers.length, 2); assert.equal(f.imports.length, 1); assert.equal(f.viewers[1].currIndex, 2);
  },
  'viewer import failure keeps a real image fallback and permits retry': async () => {
    const f = fixture({ deferredImport: true }); f.clickSlide(0); f.clickSlide(2); f.rejectImport(); await flush();
    assert.deepEqual(f.assignments, [f.slides[2].href]); assert.equal(f.viewers.length, 0);
    f.clickSlide(1); assert.equal(f.imports.length, 2); f.resolveImport(); await flush(); assert.equal(f.viewers.length, 1); assert.equal(f.viewers[0].currIndex, 1);
  },
  'detached page cannot open a late viewer or navigate from late import failure': async () => {
    for (const reject of [false, true]) {
      const f = fixture({ deferredImport: true }); f.clickSlide(0); f.page.isConnected = false;
      if (reject) f.rejectImport(); else f.resolveImport(); await flush(); assert.equal(f.viewers.length, 0); assert.equal(f.assignments.length, 0);
    }
  },
  'BFCache restoration reconciles actual position and clears old gesture suppression': async () => {
    const f = fixture(); f.pointer('pointerdown'); f.pointer('pointercancel'); f.viewport.scrollLeft = 800; f.window.emit('pageshow', { persisted: true }); f.selected(2);
    f.clickSlide(2); await flush(); assert.equal(f.viewers.length, 1); assert.equal(f.viewers[0].currIndex, 2);
  },
  'zero photos safely skip enhancement; one photo opens zoom with no gallery navigation': async () => {
    const empty = fixture({ count: 0 }); assert.equal(empty.viewport.listeners.size, 0); assert.equal(empty.imports.length, 0);
    const one = fixture({ count: 1 }); one.selected(0); one.expand.click(); await flush();
    assert.equal(one.viewers[0].options.arrowPrev, false); assert.equal(one.viewers[0].options.arrowNext, false); assert.equal(one.viewers[0].options.counter, false);
  },
};

async function behaviorChecks() {
  for (const [name, check] of Object.entries(behaviorCases)) {
    try { await check(); checks.push(name); }
    catch (error) { error.message = `${name}: ${error.message}`; throw error; }
  }
}

async function main() {
  await behaviorChecks();
  await liquidChecks();
  console.log(JSON.stringify({ status: 'passed', count: checks.length, checks, limits: 'Controlled DOM/scroll and PhotoSwipe API doubles plus LiquidJS image/translation adapters. Native browser paint, touch inertia, pinch/zoom, CDN responses and Shopify server rendering require separate browser/physical-device checks.' }, null, 2));
}
main().catch(error => { console.error(error); process.exitCode = 1; });
