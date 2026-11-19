const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const themeRoot = path.resolve(process.argv[2] || path.join(__dirname, '..'));
const source = fs.readFileSync(path.join(themeRoot, 'assets/bc-sunshower-page.js'), 'utf8');
const start = source.search(/      (?:const|let) mainPhoto =/);
const end = source.indexOf('      const description =', start);
assert(start >= 0 && end > start, 'The actual production gallery block must be present');
const gallery = new vm.Script(source.slice(start, end), { filename: 'bc-sunshower-page.js:gallery' });
const imageUrl = (name, width = 1400) => `https://cdn.shopify.com/files/${name}.jpg?v=1&width=${width}`;
const flush = async () => { await Promise.resolve(); await Promise.resolve(); };

class Element {
  constructor() {
    this.attributeMap = new Map();
    this.listeners = new Map();
    this.dataset = {};
    this.isConnected = true;
    this.bounds = { left: 0, right: 100 };
    this.scrollCalls = [];
    this.classList = {
      toggle: (name, enabled) => {
        const names = new Set((this.getAttribute('class') || '').split(/\s+/).filter(Boolean));
        if (enabled) names.add(name); else names.delete(name);
        this.setAttribute('class', [...names].join(' '));
      },
      contains: name => (this.getAttribute('class') || '').split(/\s+/).includes(name),
    };
  }
  get attributes() { return [...this.attributeMap].map(([name, value]) => ({ name, value })); }
  get src() { return this.getAttribute('src') || ''; }
  set src(value) { this.setAttribute('src', value); }
  addEventListener(name, listener) {
    const listeners = this.listeners.get(name) || [];
    listeners.push(listener);
    this.listeners.set(name, listeners);
  }
  emit(name, event = {}) {
    const dispatched = { target: this, preventDefault() { this.defaultPrevented = true; }, stopPropagation() { this.propagationStopped = true; }, ...event };
    for (const listener of this.listeners.get(name) || []) listener(dispatched);
    return dispatched;
  }
  setAttribute(name, value) { this.attributeMap.set(name, String(value)); }
  getAttribute(name) { return this.attributeMap.get(name) ?? null; }
  removeAttribute(name) { this.attributeMap.delete(name); }
  click(target = this, detail = 1) { return this.emit('click', { target, detail }); }
  getBoundingClientRect() { return this.bounds; }
  scrollBy(options) { this.scrollCalls.push(options); }
  setPointerCapture(id) { this.capturedPointer = id; }
  replaceWith(photo) { this.replaceNode(photo); this.isConnected = false; }
}

function fixture({ hasPhoto = true, metadata = true, decode = true, initialShown = 0, initialComplete = true } = {}) {
  const initialPhoto = new Element();
  initialPhoto.src = imageUrl('landscape');
  initialPhoto.currentSrc = imageUrl(['landscape', 'drawing', 'detail'][initialShown], 720);
  initialPhoto.width = 1200;
  initialPhoto.height = 800;
  initialPhoto.complete = initialComplete;
  initialPhoto.naturalWidth = initialComplete ? 1200 : 0;
  initialPhoto.setAttribute('srcset', `${imageUrl('landscape', 720)} 720w`);
  initialPhoto.setAttribute('sizes', '(min-width: 990px) 560px, 100vw');
  initialPhoto.setAttribute('class', 'ss-gallery__photo retained-class');
  initialPhoto.setAttribute('alt', 'Sunshower product title');
  initialPhoto.setAttribute('role', 'presentation');
  initialPhoto.setAttribute('data-extra', 'retained');
  initialPhoto.setAttribute('loading', 'eager');
  const buttons = ['landscape', 'drawing', 'detail'].map((name, index) => {
    const button = new Element();
    button.dataset.ssPhoto = imageUrl(name);
    if (metadata) {
      button.dataset.ssPhotoWidth = ['1200', '700', '1600'][index];
      button.dataset.ssPhotoHeight = ['800', '2000', '900'][index];
    }
    button.setAttribute('aria-pressed', String(index === 0));
    button.classList.toggle('is-selected', index === 0);
    return button;
  });
  const lightboxPhoto = new Element();
  const lightbox = new Element();
  lightbox.querySelector = selector => selector === 'img' ? lightboxPhoto : null;
  lightbox.showModal = () => { lightbox.open = true; };
  lightbox.close = () => { lightbox.open = false; };
  const openButton = new Element();
  const closeButton = new Element();
  const photoStrip = new Element();
  const elements = {
    '.ss-gallery__photo': hasPhoto ? initialPhoto : null,
    '[data-ss-lightbox]': lightbox,
    '[data-ss-open-image]': openButton,
    '[data-ss-close-image]': closeButton,
    '.ss-gallery__thumbs': photoStrip,
  };
  const install = photo => {
    elements['.ss-gallery__photo'] = photo;
    photo.isConnected = true;
    photo.replaceNode = install;
  };
  initialPhoto.replaceNode = install;
  const page = {
    isConnected: true,
    querySelector: selector => elements[selector] ?? null,
    querySelectorAll: selector => selector === '[data-ss-photo]' ? buttons : [],
  };
  const pending = [];
  class Image extends Element {
    constructor() {
      super();
      this.isConnected = false;
      this.complete = false;
      this.decoded = false;
      if (!decode) this.decode = undefined;
      pending.push(this);
    }
    load(width = 350, height = 1000) {
      this.complete = true;
      this.naturalWidth = width;
      this.naturalHeight = height;
      this.currentSrc = this.src;
      this.onload?.();
    }
    decode() {
      this.decodeStarted = true;
      return new Promise((resolve, reject) => {
        this.finishDecode = () => { this.decoded = true; resolve(); };
        this.rejectDecode = () => reject(new Error('decode failed'));
      });
    }
    fail() { this.onerror?.(); }
  }
  const window = new Element();
  const document = new Element();
  gallery.runInNewContext({ page, Image, window, document, URL, location: { href: 'https://badkamercity.nl/products/sunshower' } });
  const selected = index => buttons.forEach((button, actual) => {
    assert.equal(button.getAttribute('aria-pressed'), String(actual === index));
    assert.equal(button.classList.contains('is-selected'), actual === index);
  });
  const finish = async index => { pending[index].load(); pending[index].finishDecode?.(); await flush(); };
  const pointer = (name, { target = openButton, pointerType = 'touch', pointerId = 1, isPrimary = true, button = 0, clientX = 200, clientY = 100 } = {}) => {
    const event = { target, pointerType, pointerId, isPrimary, button, clientX, clientY };
    document.emit(name,event);
    return target.emit(name,event);
  };
  const swipe = (direction = 'left', options = {}) => {
    pointer('pointerdown',options);
    pointer('pointerup',{ ...options, clientX: direction === 'left' ? 100 : 300 });
  };
  return { get mainPhoto() { return elements['.ss-gallery__photo']; }, initialPhoto, buttons, pending, selected, finish, pointer, swipe, page, window, document, lightbox, lightboxPhoto, openButton, closeButton, photoStrip };
}

const cases = {
  'waits for decode, then installs the decoded image with the matching thumbnail': async () => {
    const f = fixture();
    f.buttons[2].click();
    f.pending[0].load();
    assert.equal(f.mainPhoto, f.initialPhoto, 'load alone must not advance the visible image');
    assert.equal(f.initialPhoto.src, imageUrl('landscape'), 'never retarget the existing rendered image');
    f.selected(0);
    assert.equal(f.pending[0].decodeStarted, true);
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto, f.pending[0], 'insert the actual decoded node');
    assert.equal(f.mainPhoto.currentSrc, imageUrl('detail'));
    assert.equal(f.mainPhoto.decoded, true);
    assert.equal(f.initialPhoto.isConnected, false);
    f.selected(2);
  },
  'preserves presentation attributes and selected image dimensions without stale responsive sources': async () => {
    const f = fixture();
    f.buttons[1].click();
    await f.finish(0);
    assert.equal(f.mainPhoto.width, 700);
    assert.equal(f.mainPhoto.height, 2000);
    for (const name of ['class', 'alt', 'role', 'data-extra', 'loading']) assert.equal(f.mainPhoto.getAttribute(name), f.initialPhoto.getAttribute(name));
    assert.equal(f.mainPhoto.getAttribute('srcset'), null);
    assert.equal(f.mainPhoto.getAttribute('sizes'), null);
    assert.equal(f.mainPhoto.src, imageUrl('drawing'));
    f.selected(1);
  },
  'uses loaded dimensions when metadata is absent': async () => {
    const f = fixture({ metadata: false });
    f.buttons[1].click();
    f.pending[0].load(900, 1800);
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto.width, 900);
    assert.equal(f.mainPhoto.height, 1800);
  },
  'load failure preserves the installed photo and selected thumbnail': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].fail();
    await flush();
    assert.equal(f.mainPhoto, f.initialPhoto);
    assert.notEqual(f.mainPhoto.getAttribute('srcset'), null);
    f.selected(0);
  },
  'decode failure preserves the installed photo and selected thumbnail': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.pending[0].rejectDecode();
    await flush();
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(0);
  },
  'late earlier load cannot replace the latest decoded choice': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.buttons[2].click();
    await f.finish(1);
    f.pending[0].load();
    await flush();
    assert.equal(f.pending[0].decodeStarted, undefined, 'stale load should not start decode');
    assert.equal(f.mainPhoto, f.pending[1]);
    f.selected(2);
  },
  'late earlier decode cannot replace the latest decoded choice': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.buttons[2].click();
    await f.finish(1);
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto, f.pending[1]);
    f.selected(2);
  },
  'earlier decode cannot commit while the newer choice is pending': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.buttons[2].click();
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(0);
    await f.finish(1);
    f.selected(2);
  },
  'clicking the selected thumbnail cancels a pending load': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.buttons[0].click();
    f.pending[0].load();
    await flush();
    assert.equal(f.pending.length, 1);
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(0);
  },
  'clicking the selected thumbnail cancels a pending decode': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.buttons[0].click();
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(0);
  },
  'repeated selection replaces the currently installed node and zoom follows it': async () => {
    const f = fixture();
    f.buttons[1].click();
    await f.finish(0);
    f.buttons[2].click();
    await f.finish(1);
    assert.equal(f.mainPhoto, f.pending[1]);
    assert.equal(f.pending[0].isConnected, false);
    f.openButton.click();
    assert.equal(f.lightboxPhoto.src, f.mainPhoto.src);
    assert.equal(f.lightbox.open, true);
    f.closeButton.click();
    assert.equal(f.lightbox.open, false);
    f.openButton.click();
    f.lightbox.click();
    assert.equal(f.lightbox.open, false);
    f.selected(2);
  },
  'zoom uses the still installed photo while another choice is decoding': async () => {
    const f = fixture();
    f.buttons[2].click();
    f.pending[0].load();
    f.openButton.click();
    assert.equal(f.lightboxPhoto.src, f.initialPhoto.src);
    f.selected(0);
    f.pending[0].finishDecode();
    await flush();
  },
  'missing main image neither loads nor opens an image': async () => {
    const f = fixture({ hasPhoto: false });
    f.buttons[1].click();
    f.openButton.click();
    assert.equal(f.pending.length, 0);
    assert.notEqual(f.lightbox.open, true);
  },
  'browsers without decode retain the loaded image fallback': async () => {
    const f = fixture({ decode: false });
    f.buttons[1].click();
    f.pending[0].load();
    await flush();
    assert.equal(f.mainPhoto, f.pending[0]);
    f.selected(1);
  },
  'initial selected thumbnail reconciles to an already visible responsive source': async () => {
    const f = fixture({ initialShown: 2 });
    assert.equal(f.mainPhoto.currentSrc, imageUrl('detail', 720));
    assert.equal(f.pending.length, 0, 'reconciliation should not fetch');
    f.selected(2);
  },
  'an initially loading image reconciles only after it loads': async () => {
    const f = fixture({ initialShown: 2, initialComplete: false });
    f.selected(0);
    f.initialPhoto.complete = true;
    f.initialPhoto.naturalWidth = 1600;
    f.initialPhoto.emit('load');
    f.selected(2);
  },
  'persisted pageshow reconciles visible source and invalidates pending decode': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.initialPhoto.currentSrc = imageUrl('detail', 1000);
    f.window.emit('pageshow', { persisted: true });
    f.selected(2);
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(2);
  },
  'a detached page cannot commit a pending decoded image': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.page.isConnected = false;
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(0);
  },
  'a removed image cannot be replaced after its decode completes': async () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.initialPhoto.isConnected = false;
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(0);
  },
  'persisted pageshow ignores a disconnected page': async () => {
    const f = fixture();
    f.page.isConnected = false;
    f.initialPhoto.currentSrc = imageUrl('detail', 1000);
    f.window.emit('pageshow', { persisted: true });
    f.selected(0);
  },
  'left and right touch swipes load adjacent images and preserve atomic selection': async () => {
    const f = fixture();
    f.swipe('left');
    assert.equal(f.pending.length, 1);
    assert.equal(f.pending[0].src, imageUrl('drawing'));
    f.selected(0);
    await f.finish(0);
    f.selected(1);
    f.swipe('right');
    assert.equal(f.pending[1].src, imageUrl('landscape'));
    await f.finish(1);
    f.selected(0);
  },
  'rapid swipes advance from the latest requested image and late results cannot win': async () => {
    const f = fixture();
    f.swipe('left');
    f.pending[0].load();
    f.swipe('left');
    assert.equal(f.pending[1].src, imageUrl('detail'));
    await f.finish(1);
    f.pending[0].finishDecode();
    await flush();
    f.selected(2);
    assert.equal(f.mainPhoto, f.pending[1]);
  },
  'reversing a pending swipe to the visible photo cancels that pending choice': async () => {
    const f = fixture();
    f.swipe('left');
    f.pending[0].load();
    f.swipe('right');
    f.pending[0].finishDecode();
    await flush();
    assert.equal(f.pending.length, 1);
    assert.equal(f.mainPhoto, f.initialPhoto);
    f.selected(0);
  },
  'latest load or decode failure resets the next swipe to the visible image': async () => {
    for (const failure of ['load', 'decode']) {
      const f = fixture();
      f.swipe('left');
      f.swipe('left');
      if (failure === 'load') f.pending[1].fail();
      else { f.pending[1].load(); f.pending[1].rejectDecode(); await flush(); }
      f.swipe('left');
      assert.equal(f.pending[2].src, imageUrl('drawing'));
      await f.finish(2);
      f.selected(1);
    }
  },
  'an outdated failure cannot reset the latest requested swipe cursor': async () => {
    const f = fixture();
    f.swipe('left');
    f.swipe('left');
    f.pending[0].fail();
    f.swipe('right');
    assert.equal(f.pending[2].src, imageUrl('drawing'));
    await f.finish(2);
    f.selected(1);
  },
  'swipe bounds clamp without wrapping or accidentally opening zoom': async () => {
    for (const [initialShown, direction] of [[0, 'right'], [2, 'left']]) {
      const f = fixture({ initialShown });
      f.swipe(direction);
      assert.equal(f.pending.length, 0);
      const click = f.openButton.click();
      assert.equal(click.defaultPrevented, true);
      assert.notEqual(f.lightbox.open, true);
      f.selected(initialShown);
    }
  },
  'one gesture advances at most one photo regardless of distance': async () => {
    const f = fixture();
    f.pointer('pointerdown', { clientX: 1000 });
    f.pointer('pointermove', { clientX: 500 });
    f.pointer('pointerup', { clientX: -1000 });
    f.pointer('pointerup', { clientX: -1200 });
    assert.equal(f.pending.length, 1);
    assert.equal(f.pending[0].src, imageUrl('drawing'));
  },
  'vertical and diagonal movements keep the photo while a small tap opens zoom': async () => {
    const f = fixture();
    f.pointer('pointerdown');
    f.pointer('pointerup', { clientX: 150, clientY: 300 });
    f.openButton.click();
    assert.notEqual(f.lightbox.open, true, 'vertical drag must not become a zoom tap');
    f.pointer('pointerdown');
    f.pointer('pointerup', { clientX: 140, clientY: 150 });
    assert.equal(f.pending.length, 0, 'diagonal 60/50 must not satisfy the horizontal ratio');
    f.openButton.click();
    assert.notEqual(f.lightbox.open, true, 'diagonal drag must not become a zoom tap');
    f.pointer('pointerdown');
    f.pointer('pointerup', { clientX: 190, clientY: 102 });
    f.openButton.click();
    assert.equal(f.lightbox.open, true);
  },
  'pointer cancellation and lost capture do not navigate or zoom': async () => {
    for (const name of ['pointercancel', 'lostpointercapture']) {
      const f = fixture();
      f.pointer('pointerdown');
      f.pointer(name);
      f.pointer('pointerup', { clientX: 100 });
      assert.equal(f.pending.length, 0);
      f.openButton.click();
      assert.notEqual(f.lightbox.open, true);
    }
  },
  'a second touch outside the photo cancels the whole gesture and permits the next single touch': async () => {
    const f = fixture();
    const outside = new Element();
    f.pointer('pointerdown');
    f.pointer('pointerdown', { target: outside, pointerId: 2, isPrimary: false });
    f.pointer('pointerup', { clientX: 100 });
    f.pointer('pointerup', { target: outside, pointerId: 2, isPrimary: false });
    assert.equal(f.pending.length, 0);
    f.openButton.click();
    assert.notEqual(f.lightbox.open, true);
    f.swipe('left');
    await f.finish(0);
    f.selected(1);
  },
  'a gesture starting with a non-primary touch never navigates': async () => {
    const f = fixture();
    f.swipe('left', { isPrimary: false });
    assert.equal(f.pending.length, 0);
  },
  'primary mouse and pen drags work while right mouse drags do not': async () => {
    for (const pointerType of ['mouse', 'pen']) {
      const f = fixture();
      f.swipe('left', { pointerType });
      await f.finish(0);
      f.selected(1);
    }
    const f = fixture();
    f.swipe('left', { pointerType: 'mouse', button: 2 });
    assert.equal(f.pending.length, 0);
  },
  'a swipe suppresses its synthetic click but the next deliberate tap immediately zooms': async () => {
    const f = fixture();
    f.swipe('left');
    f.openButton.click();
    assert.notEqual(f.lightbox.open, true);
    f.swipe('right');
    // A browser may omit the synthetic click; the next actual tap must still work.
    f.pointer('pointerdown');
    f.pointer('pointerup');
    f.openButton.click();
    assert.equal(f.lightbox.open, true);
  },
  'keyboard zoom remains available immediately after a swipe': async () => {
    const f = fixture();
    f.swipe('left');
    f.openButton.click(f.openButton, 0);
    assert.equal(f.lightbox.open, true);
  },
  'swipe selection reveals only the horizontal thumbnail strip after the image commits': async () => {
    const f = fixture();
    f.photoStrip.bounds = { left: 20, right: 180 };
    f.buttons[1].bounds = { left: 160, right: 240 };
    f.swipe('left');
    assert.equal(f.photoStrip.scrollCalls.length, 0);
    await f.finish(0);
    assert.equal(f.photoStrip.scrollCalls.length, 1);
    assert.equal(f.photoStrip.scrollCalls[0].left, 60);
    assert.equal('top' in f.photoStrip.scrollCalls[0], false);
    assert.equal(f.photoStrip.scrollCalls[0].behavior, 'auto');
  },
  'swipes follow a thumbnail click and the displayed responsive source': async () => {
    const f = fixture({ initialShown: 2 });
    f.swipe('right');
    assert.equal(f.pending[0].src, imageUrl('drawing'));
    f.buttons[0].click();
    f.swipe('left');
    assert.equal(f.pending[2].src, imageUrl('drawing'));
    await f.finish(2);
    f.selected(1);
  },
  'initial image load while a swipe is pending does not reset the requested cursor': async () => {
    const f = fixture({ initialComplete: false });
    f.swipe('left');
    f.initialPhoto.complete = true;
    f.initialPhoto.naturalWidth = 1200;
    f.initialPhoto.emit('load');
    f.swipe('left');
    assert.equal(f.pending[1].src, imageUrl('detail'));
  },
  'persisted page restoration cancels an unfinished gesture and restores the swipe cursor': async () => {
    const f = fixture();
    f.swipe('left');
    f.pointer('pointerdown');
    f.window.emit('pageshow', { persisted: true });
    f.pointer('pointerup', { clientX: 100 });
    assert.equal(f.pending.length, 1);
    f.swipe('left');
    assert.equal(f.pending[1].src, imageUrl('drawing'));
  },
  'native image dragging is prevented while a missing image cannot swipe': async () => {
    const f = fixture();
    assert.equal(f.openButton.emit('dragstart').defaultPrevented, true);
    const missing = fixture({ hasPhoto: false });
    missing.swipe('left');
    assert.equal(missing.pending.length, 0);
  },
};

(async () => {
  for (const [name, run] of Object.entries(cases)) {
    await run();
    console.log(`PASS ${name}`);
  }
  console.log(`${Object.keys(cases).length} Sunshower gallery behavior tests passed`);
})().catch(error => { console.error(error); process.exitCode = 1; });
