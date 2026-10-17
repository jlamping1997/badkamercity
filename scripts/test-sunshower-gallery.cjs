const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const themeRoot = path.resolve(process.argv[2] || path.join(__dirname, '..'));
const source = fs.readFileSync(path.join(themeRoot, 'assets/bc-sunshower-page.js'), 'utf8');
const start = source.indexOf('      const mainPhoto =');
const end = source.indexOf('      const description =', start);
assert(start >= 0 && end > start, 'The actual gallery block must be present');
const gallery = new vm.Script(source.slice(start, end), { filename: 'bc-sunshower-page.js:gallery' });

class Element {
  constructor() {
    this.attributes = new Map();
    this.listeners = new Map();
    this.classes = new Set();
    this.classList = {
      toggle: (name, enabled) => enabled ? this.classes.add(name) : this.classes.delete(name),
      contains: name => this.classes.has(name),
    };
    this.dataset = {};
  }
  addEventListener(name, listener) { this.listeners.set(name, listener); }
  setAttribute(name, value) { this.attributes.set(name, String(value)); }
  getAttribute(name) { return this.attributes.get(name) ?? null; }
  removeAttribute(name) { this.attributes.delete(name); }
  click(target = this) { this.listeners.get('click')?.({ target }); }
}

function fixture({ hasPhoto = true, metadata = true } = {}) {
  const mainPhoto = new Element();
  mainPhoto.src = 'landscape.jpg';
  mainPhoto.currentSrc = 'landscape-small.jpg';
  mainPhoto.width = 1200;
  mainPhoto.height = 800;
  mainPhoto.setAttribute('srcset', 'landscape-small.jpg 720w');
  const buttons = ['landscape.jpg', 'drawing.jpg', 'detail.jpg'].map((src, index) => {
    const button = new Element();
    button.dataset.ssPhoto = src;
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
    '.ss-gallery__photo': hasPhoto ? mainPhoto : null,
    '[data-ss-lightbox]': lightbox,
    '[data-ss-open-image]': openButton,
    '[data-ss-close-image]': closeButton,
  };
  const page = {
    querySelector: selector => elements[selector] ?? null,
    querySelectorAll: selector => selector === '[data-ss-photo]' ? buttons : [],
  };
  const pending = [];
  class Image {
    constructor() { pending.push(this); }
    load(width = 350, height = 1000) {
      this.naturalWidth = width;
      this.naturalHeight = height;
      this.onload?.();
    }
    fail() { this.onerror?.(); }
  }
  gallery.runInNewContext({ page, Image });
  const selected = index => {
    buttons.forEach((button, actual) => {
      assert.equal(button.getAttribute('aria-pressed'), String(actual === index));
      assert.equal(button.classList.contains('is-selected'), actual === index);
    });
  };
  return { mainPhoto, buttons, pending, selected, lightbox, lightboxPhoto, openButton, closeButton };
}

const cases = {
  'loads before replacing photo, dimensions and selected state': () => {
    const f = fixture();
    f.buttons[1].click();
    assert.equal(f.mainPhoto.src, 'landscape.jpg');
    assert.equal(f.mainPhoto.height, 800);
    assert.equal(f.pending[0].src, 'drawing.jpg');
    f.selected(0);
    f.pending[0].load();
    assert.equal(f.mainPhoto.src, 'drawing.jpg');
    assert.equal(f.mainPhoto.width, 700);
    assert.equal(f.mainPhoto.height, 2000);
    assert.equal(f.mainPhoto.getAttribute('srcset'), null);
    f.selected(1);
  },
  'uses loaded image dimensions when metadata is absent': () => {
    const f = fixture({ metadata: false });
    f.buttons[1].click();
    f.pending[0].load(900, 1800);
    assert.equal(f.mainPhoto.width, 900);
    assert.equal(f.mainPhoto.height, 1800);
  },
  'failed request preserves the existing image and selection': () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].fail();
    assert.equal(f.mainPhoto.src, 'landscape.jpg');
    assert.equal(f.mainPhoto.width, 1200);
    assert.equal(f.mainPhoto.height, 800);
    assert.notEqual(f.mainPhoto.getAttribute('srcset'), null);
    f.selected(0);
  },
  'earlier load does not replace a newer pending choice': () => {
    const f = fixture();
    f.buttons[1].click();
    f.buttons[2].click();
    f.pending[0].load();
    assert.equal(f.mainPhoto.src, 'landscape.jpg');
    f.selected(0);
    f.pending[1].load();
    assert.equal(f.mainPhoto.src, 'detail.jpg');
    f.selected(2);
  },
  'late earlier load cannot overwrite the latest successful choice': () => {
    const f = fixture();
    f.buttons[1].click();
    f.buttons[2].click();
    f.pending[1].load();
    f.pending[0].load();
    assert.equal(f.mainPhoto.src, 'detail.jpg');
    assert.equal(f.mainPhoto.width, 1600);
    assert.equal(f.mainPhoto.height, 900);
    f.selected(2);
  },
  'clicking the selected thumbnail cancels a pending choice': () => {
    const f = fixture();
    f.buttons[1].click();
    f.buttons[0].click();
    assert.equal(f.pending.length, 1);
    f.pending[0].load();
    assert.equal(f.mainPhoto.src, 'landscape.jpg');
    f.selected(0);
  },
  'gallery without a main photo does not load or open an image': () => {
    const f = fixture({ hasPhoto: false });
    f.buttons[1].click();
    f.openButton.click();
    assert.equal(f.pending.length, 0);
    assert.notEqual(f.lightbox.open, true);
  },
  'zoom follows the committed source despite a stale currentSrc': () => {
    const f = fixture();
    f.buttons[1].click();
    f.pending[0].load();
    f.openButton.click();
    assert.equal(f.lightboxPhoto.src, 'drawing.jpg');
    assert.equal(f.lightbox.open, true);
    f.closeButton.click();
    assert.equal(f.lightbox.open, false);
    f.openButton.click();
    f.lightbox.click();
    assert.equal(f.lightbox.open, false);
  },
};

for (const [name, run] of Object.entries(cases)) {
  run();
  console.log(`PASS ${name}`);
}
console.log(`${Object.keys(cases).length} Sunshower gallery behavior tests passed`);
