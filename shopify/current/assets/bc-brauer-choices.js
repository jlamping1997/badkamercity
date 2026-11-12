(() => {
  'use strict';
  const cache = new Map();
  const text = value => value == null ? '' : String(value).trim();
  const same = (a, b) => text(a) === text(b);

  function active(group, axis, state) {
    if (!axis.show_only_if_multiple || !axis.depends_on) return true;
    const candidates = group.products.filter(product =>
      axis.depends_on.every(key => same(product.options[key], state[key])));
    return new Set(candidates.map(product => text(product.options[axis.key])).filter(Boolean)).size > 1;
  }

  function matches(group, state) {
    const activeAxes = new Set(group.axes.filter(axis => active(group, axis, state)).map(axis => axis.key));
    return group.products.filter(product => group.axes.every(axis => {
      if (!activeAxes.has(axis.key)) return true;
      if (axis.depends_on && !axis.values.some(value => same(value, state[axis.key]))) return true;
      return same(product.options[axis.key], state[axis.key]);
    }));
  }

  function nextState(group, state, key, value) {
    const next = { ...state, [key]: value };
    if (!same(state[key], value)) {
      group.axes.forEach(axis => {
        if (axis.reset_on_change?.includes(key)) next[axis.key] = null;
      });
    }
    return next;
  }

  function orderedValues(group, axis, state) {
    if (!group.price_order) return axis.values;
    return axis.values.map((value, index) => {
      const candidates = matches(group, nextState(group, state, axis.key, value));
      const prices = candidates.map(p => p.price_cents).filter(Number.isSafeInteger);
      return { value, index, price: prices.length === candidates.length && prices.length ? Math.min(...prices) : Infinity };
    }).sort((a, b) => a.price - b.price ||
      (axis.key === 'colour' ? Number(b.value === 'Chroom') - Number(a.value === 'Chroom') : 0) || a.index - b.index)
      .map(option => option.value);
  }

  function make(tag, className, label) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (label != null) node.textContent = label;
    return node;
  }

  function label(axis, value) {
    const raw = text(value);
    if (axis.labels?.[raw]) return axis.labels[raw];
    return ['width', 'depth', 'side', 'head_size'].includes(axis.key) && /^\d+(?:[.,]\d+)?$/.test(raw)
      ? `${raw} cm` : raw;
  }

  class Choices {
    constructor(root, group) {
      this.root = root;
      this.group = group;
      this.current = group.products.find(product => product.handle === root.dataset.productHandle);
      if (!this.current || group.id !== root.dataset.choiceGroup || group.products.length < 2 ||
          this.current.id.split('/').pop() !== root.dataset.productId ||
          this.current.variant_id.split('/').pop() !== root.dataset.variantId ||
          this.current.sku !== root.dataset.productSku) return;
      this.state = { ...this.current.options };
      this.expanded = new Set();
      this.product = root.closest('product-info');
      this.locks = new Map();
      this.navigating = false;
      this.render();
      root.hidden = false;
      root.dataset.initialized = 'true';
      window.addEventListener('pageshow', event => {
        if (!event.persisted || !root.isConnected) return;
        this.navigating = false;
        this.state = { ...this.current.options };
        this.lock(false);
        this.render();
      });
      try {
        const saved = JSON.parse(sessionStorage.getItem('bc:brauer:position') || 'null');
        if (saved?.handle === this.current.handle && saved.group === group.id && Date.now() - saved.at < 20000) {
          sessionStorage.removeItem('bc:brauer:position');
          requestAnimationFrame(() => window.scrollTo({ top: saved.y, behavior: 'instant' }));
        }
      } catch (_) {}
    }

    lock(locked) {
      const buttons = this.product?.querySelectorAll('.product-form__submit, .shopify-payment-button__button') || [];
      buttons.forEach(button => {
        if (locked && !this.locks.has(button)) this.locks.set(button, button.disabled);
        if (locked) button.disabled = true;
        else if (this.locks.has(button)) {
          button.disabled = this.locks.get(button);
          this.locks.delete(button);
        }
      });
      if (locked && !this.guard) {
        this.guard = event => {
          if (event.target.matches('form[action*="/cart/add"]')) {
            event.preventDefault();
            event.stopImmediatePropagation();
          }
        };
        document.addEventListener('submit', this.guard, true);
      } else if (!locked && this.guard) {
        document.removeEventListener('submit', this.guard, true);
        this.guard = null;
      }
    }

    choose(axis, value) {
      if (this.navigating) return;
      const busy = this.product?.querySelector('.product-form__submit[aria-busy="true"], .product-form__submit.loading');
      if (busy) return;
      const state = nextState(this.group, this.state, axis.key, value);
      const candidates = matches(this.group, state);
      if (!candidates.length) return;
      this.state = state;
      if (candidates.length !== 1) {
        this.lock(true);
        this.render(axis.key);
        return;
      }
      const target = candidates[0];
      if (target.handle === this.current.handle) {
        this.state = { ...this.current.options };
        this.lock(false);
        this.render(axis.key);
        return;
      }
      let url;
      try { url = new URL(target.url, window.location.origin); } catch (_) { return; }
      if (url.origin !== window.location.origin || url.pathname !== `/products/${target.handle}`) return;
      const currentUrl = new URL(window.location.href);
      ['preview_theme_id', '_fd', 'pb', '_ab', '_sc'].forEach(key => {
        if (currentUrl.searchParams.has(key)) url.searchParams.set(key, currentUrl.searchParams.get(key));
      });
      try {
        sessionStorage.setItem('bc:brauer:position', JSON.stringify({
          handle: target.handle, group: this.group.id, y: window.scrollY, at: Date.now()
        }));
      } catch (_) {}
      this.navigating = true;
      this.lock(true);
      this.render();
      try { window.location.assign(url.href); }
      catch (_) {
        this.navigating = false;
        this.state = { ...this.current.options };
        this.lock(false);
        this.render();
        this.status.textContent = 'Openen is niet gelukt. Probeer de uitvoering opnieuw te kiezen.';
      }
    }

    option(axis, value, colour) {
      const candidates = matches(this.group, nextState(this.group, this.state, axis.key, value));
      const selected = same(this.state[axis.key], value);
      const handlePhoto = axis.kind === 'handle_detail_photo' ? axis.images?.[value] : null;
      const productPhoto = ['spout', 'height_execution', 'handshower', 'arm'].includes(axis.key) && axis.kind === 'product_first_image';
      const visual = Boolean(handlePhoto || productPhoto);
      const button = make('button', colour ? 'bc-hotbath-swatch' : visual
        ? 'bc-buybox__config-button bc-brauer-photo-choice' : 'bc-buybox__config-button');
      button.type = 'button';
      button.dataset.axis = axis.key;
      button.dataset.value = value;
      button.setAttribute('aria-label', label(axis, value));
      button.setAttribute('aria-pressed', String(selected));
      button.classList.toggle('is-active', selected);
      button.disabled = this.navigating || !candidates.length;
      button.setAttribute('aria-disabled', String(button.disabled));
      if (!candidates.length) button.title = 'Niet mogelijk met de overige keuzes.';
      if (colour) {
        const chip = make('span', 'bc-hotbath-swatch__chip');
        const surface = make('span', 'bc-hotbath-swatch__surface');
        const fallback = make('span', 'bc-hotbath-swatch__fallback', label(axis, value));
        const exact = candidates.length === 1 ? candidates[0] : null;
        if (exact?.image) {
          const image = make('img');
          const photo = new URL(exact.image);
          photo.searchParams.set('width', '160');
          image.src = photo.href;
          image.alt = '';
          image.width = 80;
          image.height = 80;
          image.loading = 'lazy';
          image.decoding = 'async';
          image.dataset.photoSku = exact.sku;
          image.addEventListener('load', () => button.classList.add('has-swatch-image'));
          image.addEventListener('error', () => { image.remove(); button.classList.remove('has-swatch-image'); });
          surface.append(image);
        }
        surface.append(fallback);
        chip.append(surface, make('span', 'bc-hotbath-swatch__check', '✓'));
        button.append(chip, make('span', 'bc-hotbath-swatch__label', label(axis, value)));
      } else if (visual) {
        const exact = candidates.length === 1 ? candidates[0] : null;
        const source = handlePhoto || exact;
        const frame = make('span', 'bc-brauer-photo-choice__frame');
        if (handlePhoto) frame.classList.add('bc-brauer-photo-choice__frame--handle');
        if (handlePhoto?.crop) {
          const crop = handlePhoto.crop;
          const size = Math.max(crop.width, crop.height);
          frame.style.setProperty('--crop-width', `${100 * crop.width / size}%`);
          frame.style.setProperty('--crop-height', `${100 * crop.height / size}%`);
          frame.style.setProperty('--photo-width', `${100 * crop.source_width / crop.width}%`);
          frame.style.setProperty('--photo-height', `${100 * crop.source_height / crop.height}%`);
          frame.style.setProperty('--photo-left', `${-100 * crop.x / crop.width}%`);
          frame.style.setProperty('--photo-top', `${-100 * crop.y / crop.height}%`);
        }
        const photoFrame = handlePhoto ? make('span', 'bc-brauer-photo-choice__crop') : frame;
        if (handlePhoto) frame.append(photoFrame);
        const fallback = make('span', 'bc-brauer-photo-choice__fallback', 'Foto volgt');
        if (source?.image) {
          const photo = new URL(source.image);
          photo.searchParams.set('width', handlePhoto ? '400' : '200');
          const image = make('img');
          image.src = photo.href;
          image.alt = '';
          image.width = 100;
          image.height = 100;
          image.loading = 'lazy';
          image.decoding = 'async';
          image.dataset.photoSku = source.sku;
          image.addEventListener('load', () => { fallback.hidden = true; });
          image.addEventListener('error', () => { image.remove(); fallback.hidden = false; });
          photoFrame.append(image);
        }
        frame.append(fallback);
        button.append(frame, make('span', 'bc-brauer-photo-choice__label', label(axis, value)),
          make('span', 'bc-buybox__option-check', selected ? '✓' : ''));
      } else {
        button.append(make('span', 'bc-buybox__option-check', selected ? '✓' : ''),
                      make('span', 'bc-buybox__option-text', label(axis, value)));
      }
      button.addEventListener('click', () => this.choose(axis, value));
      return button;
    }

    render(focusKey) {
      const fragment = document.createDocumentFragment();
      this.group.axes.forEach(axis => {
        if (!active(this.group, axis, this.state) || axis.values.length < 2) return;
        const group = make('div', 'bc-buybox__option-group bc-buybox__switcher-group');
        group.dataset.axisGroup = axis.key;
        const heading = make('p', 'form__label bc-buybox__option-label', axis.label + ': ');
        heading.append(make('strong', 'bc-hotbath-selected-color', label(axis, this.state[axis.key]) || 'Maak een keuze'));
        group.append(heading);
        const values = orderedValues(this.group, axis, this.state);
        if (['width', 'depth', 'head_size'].includes(axis.key) && axis.values.length > 3) {
          const select = make('select', 'bc-buybox__config-select');
          select.dataset.axis = axis.key;
          select.setAttribute('aria-label', axis.label);
          select.disabled = this.navigating;
          values.forEach(value => {
            const option = make('option', '', label(axis, value));
            option.value = value;
            option.disabled = !matches(this.group, nextState(this.group, this.state, axis.key, value)).length;
            option.selected = same(value, this.state[axis.key]);
            select.append(option);
          });
          select.addEventListener('change', () => this.choose(axis, select.value));
          group.append(select);
        } else {
          const colour = axis.key === 'colour';
          const visual = axis.kind === 'handle_detail_photo' ||
            (['spout', 'height_execution', 'handshower', 'arm'].includes(axis.key) && axis.kind === 'product_first_image');
          const list = make('div', colour ? 'bc-hotbath-swatches' : visual
            ? 'bc-brauer-photo-choices' : 'bc-buybox__config-buttons');
          if (axis.kind === 'handle_detail_photo') list.classList.add('bc-brauer-photo-choices--handles');
          list.setAttribute('role', 'group');
          list.setAttribute('aria-label', axis.label);
          const visible = values.slice(0, 6);
          const selected = values.find(value => same(value, this.state[axis.key]));
          if (selected && !visible.includes(selected)) visible[5] = selected;
          values.forEach(value => {
            const button = this.option(axis, value, colour);
            button.hidden = colour && !this.expanded.has(axis.key) && !visible.includes(value);
            list.append(button);
          });
          group.append(list);
          if (axis.kind === 'handle_detail_photo') {
            group.append(make('p', 'bc-brauer-choice-help',
              axis.help || 'De foto toont de hendelvorm in chroom. Kleur en afwerking kies je hierboven; de plaatsing van de uitloop kies je hieronder. Grijze opties zijn niet combineerbaar met je andere keuzes.'));
          }
          if (colour && axis.values.length > 6) {
            const toggle = make('button', 'bc-hotbath-colors__toggle', this.expanded.has(axis.key) ? 'Minder kleuren' : 'Bekijk meer kleuren');
            toggle.type = 'button';
            toggle.dataset.expandAxis = axis.key;
            toggle.setAttribute('aria-expanded', String(this.expanded.has(axis.key)));
            toggle.addEventListener('click', () => {
              if (this.expanded.has(axis.key)) this.expanded.delete(axis.key); else this.expanded.add(axis.key);
              this.render();
              this.root.querySelector('[data-expand-axis]')?.focus({ preventScroll: true });
            });
            group.append(toggle);
          }
        }
        fragment.append(group);
      });
      const candidates = matches(this.group, this.state);
      const pending = candidates.length !== 1;
      this.root.dataset.pending = String(pending);
      this.root.setAttribute('aria-busy', String(this.navigating));
      this.status = make('p', 'bc-buybox__switch-status');
      this.status.setAttribute('role', 'status');
      this.status.setAttribute('aria-live', 'polite');
      if (pending) {
        const axis = this.group.axes.find(item => item.depends_on && active(this.group, item, this.state) &&
          !item.values.some(value => same(value, this.state[item.key])));
        this.status.textContent = `Kies ${axis ? axis.label.toLowerCase() : 'de volledige uitvoering'} om de nieuwe uitvoering te openen.`;
      } else if (this.navigating) this.status.textContent = 'De gekozen uitvoering wordt geopend…';
      fragment.append(this.status);
      this.root.replaceChildren(fragment);
      if (focusKey) this.root.querySelector(`[data-axis="${focusKey}"]`)?.focus({ preventScroll: true });
    }
  }

  function init(scope = document) {
    scope.querySelectorAll('[data-bc-brauer-choices]').forEach(root => {
      if (root.dataset.loading) return;
      root.dataset.loading = 'true';
      const source = root.dataset.choiceSource;
      if (!cache.has(source)) cache.set(source, fetch(source).then(response => {
        if (!response.ok) throw new Error('Keuzemenu kon niet worden geladen.');
        return response.json();
      }));
      cache.get(source).then(group => new Choices(root, group)).catch(() => { root.hidden = true; });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => init());
  else init();
  document.addEventListener('shopify:section:load', event => init(event.target));
})();
