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
  emit(name, event = {}) { for (const listener of this.listeners.get(name) || []) listener({ target: this, ...event }); }
  setAttribute(name, value) { this.attributeMap.set(name, String(value)); }
  getAttribute(name) { return this.attributeMap.get(name) ?? null; }
  removeAttribute(name) { this.attributeMap.delete(name); }
  click(target = this) { this.emit('click', { target }); }
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
  const elements = {
    '.ss-gallery__photo': hasPhoto ? initialPhoto : null,
    '[data-ss-lightbox]': lightbox,
    '[data-ss-open-image]': openButton,
    '[data-ss-close-image]': closeButton,
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
  gallery.runInNewContext({ page, Image, window, URL, location: { href: 'https://badkamercity.nl/products/sunshower' } });
  const selected = index => buttons.forEach((button, actual) => {
    assert.equal(button.getAttribute('aria-pressed'), String(actual === index));
    assert.equal(button.classList.contains('is-selected'), actual === index);
  });
  const finish = async index => { pending[index].load(); pending[index].finishDecode?.(); await flush(); };
  return { get mainPhoto() { return elements['.ss-gallery__photo']; }, initialPhoto, buttons, pending, selected, finish, page, window, lightbox, lightboxPhoto, openButton, closeButton };
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
};

(async () => {
  for (const [name, run] of Object.entries(cases)) {
    await run();
    console.log(`PASS ${name}`);
  }
  console.log(`${Object.keys(cases).length} Sunshower gallery behavior tests passed`);
})().catch(error => { console.error(error); process.exitCode = 1; });
