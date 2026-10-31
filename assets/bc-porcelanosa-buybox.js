if (!customElements.get('bc-porcelanosa-buybox')) {
  customElements.define('bc-porcelanosa-buybox', class extends HTMLElement {
    connectedCallback() {
      if (this.started) return;
      this.started = true;
      this.core = window.BCPorcelanosa;
      if (!this.core) return;
      this.page = this.closest('product-info');
      this.form = document.getElementById(this.dataset.form);
      this.area = this.querySelector('[data-tile-area]');
      this.waste = this.querySelector('[data-tile-waste]');
      this.waste.value = '10';
      this.quantity = this.querySelector('[data-tile-quantity]');
      this.boxInput = this.querySelector('[data-tile-box-input]');
      this.inputNumber = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', { useGrouping: false, maximumFractionDigits: 4 });
      this.submit = this.form?.querySelector('[type="submit"]');
      this.initialDisabled = this.submit?.disabled;
      this.money = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', { style: 'currency', currency: this.dataset.currency });
      this.number = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', { maximumFractionDigits: 4 });
      this.preview = this.dataset.preview === 'true';
      this.current = { sku: this.dataset.sku, boxUnits: Number(this.dataset.boxUnits), priceCents: Number(this.dataset.priceCents), unitPriceCents: Number(this.dataset.unitPriceCents), leadTime: this.dataset.leadTime, orderType: this.dataset.orderType };
      this.cacheKey = 'bc-tile-area:' + (this.dataset.group || this.dataset.productId);
      try {
        const saved = JSON.parse(sessionStorage.getItem(this.cacheKey));
        if (saved?.mode === 'boxes' && this.boxInput && this.core.calculateBoxes(saved.boxes, this.current.boxUnits, this.current.priceCents)) { this.boxMode = true; this.boxInput.value = String(saved.boxes); this.waste.value = '0'; this.explicitArea = true; }
        else if (saved && this.core.units(saved.area)) { this.area.value = saved.area; this.waste.value = String(saved.waste === true ? 10 : saved.waste === false ? 0 : ([0,5,10,15,20].includes(Number(saved.waste)) ? Number(saved.waste) : 10)); this.explicitArea = true; }
      } catch (_) { }
      this.area.addEventListener('input', () => { this.explicitArea = true; this.boxMode = false; this.calculate(); this.save(); });
      this.waste.addEventListener('change', () => { this.boxMode = false; this.calculate(); this.save(); });
      this.boxInput?.addEventListener('input', () => { this.boxMode = true; this.explicitArea = true; this.calculate(); this.save(); });
      this.querySelectorAll('[data-tile-box-step]').forEach(button => button.addEventListener('click', () => {
        const typed = this.boxInput.value.trim();
        const current = typed && Number.isSafeInteger(Number(typed)) && Number(typed) > 0 ? Number(typed) : 0;
        this.boxInput.value = String(Math.max(1, current + Number(button.dataset.tileBoxStep)));
        this.boxInput.dispatchEvent(new Event('input', { bubbles: true }));
      }));
      const boxControls = this.querySelector('[data-tile-box-controls]');
      const boxResult = this.querySelector('[data-tile-box-result]');
      if (boxControls) boxControls.hidden = false;
      if (boxResult && boxControls) boxResult.hidden = true;
      this.querySelector('[data-tile-calculator]').hidden = false;
      this.querySelector('[data-tile-manual]').hidden = true;
      this.calculate();
      const manual = this.querySelector('[data-tile-manual]');
      manual?.setAttribute('aria-hidden', 'true');
      this.loadChoices();
    }
    text(selector, value) { const element = this.querySelector(selector); if (element) element.textContent = value; }
    save() {
      try {
        const valid = this.boxMode ? this.core.calculateBoxes(this.boxInput?.value, this.current.boxUnits, this.current.priceCents) : this.core.units(this.area.value);
        if (this.explicitArea && valid) sessionStorage.setItem(this.cacheKey, JSON.stringify({ area: this.area.value, waste: Number(this.waste.value), mode: this.boxMode ? 'boxes' : 'area', boxes: this.boxInput?.value }));
      } catch (_) { }
    }
    calculate() {
      const manual = this.boxMode && this.boxInput;
      const result = manual ? this.core.calculateBoxes(this.boxInput.value, this.current.boxUnits, this.current.priceCents) : this.core.calculate(this.area.value, Number(this.waste.value), this.current.boxUnits, this.current.priceCents);
      if (manual && result) { this.waste.value = '0'; this.area.value = this.inputNumber.format(result.supplied / this.core.scale); }
      const error = this.querySelector('[data-tile-error]');
      const untouched = !this.explicitArea && !this.area.value.trim() && !manual;
      error.hidden = Boolean(result) || untouched;
      error.textContent = result || untouched ? '' : manual ? this.dataset.boxError : this.dataset.areaError;
      this.area.setAttribute('aria-invalid', String(!result && !manual && !untouched));
      this.boxInput?.setAttribute('aria-invalid', String(!result && Boolean(manual)));
      if (this.submit) this.submit.disabled = this.initialDisabled || !result;
      this.page?.querySelectorAll('[data-sticky-submit]').forEach(button => { button.disabled = this.initialDisabled || !result; });
      if (!result) {
        if (!manual && this.boxInput) this.boxInput.value = '';
        this.text('[data-tile-boxes]', '—');
        this.text('[data-tile-required]', '—');
        this.text('[data-tile-supplied]', '—');
        this.text('[data-tile-total]', '—');
        const decrease = this.querySelector('[data-tile-box-step="-1"]');
        if (decrease) decrease.disabled = true;
        this.page?.querySelectorAll('.bc-product-sticky__price').forEach(element => { element.textContent = '—'; });
        return;
      }
      this.quantity.value = String(result.boxes);
      if (this.boxInput) this.boxInput.value = String(result.boxes);
      const decrease = this.querySelector('[data-tile-box-step="-1"]');
      const increase = this.querySelector('[data-tile-box-step="1"]');
      if (decrease) decrease.disabled = result.boxes <= 1;
      if (increase) increase.disabled = !this.core.calculateBoxes(result.boxes + 1, this.current.boxUnits, this.current.priceCents);
      this.quantity.dispatchEvent(new Event('change', { bubbles: true }));
      this.text('[data-tile-boxes]', this.number.format(result.boxes));
      this.text('[data-tile-boxes-label]', this.querySelector(result.boxes === 1 ? '[data-tile-box-one]' : '[data-tile-box-many]').textContent);
      this.text('[data-tile-required]', this.number.format(result.required / this.core.scale) + ' m²');
      this.text('[data-tile-supplied]', this.number.format(result.supplied / this.core.scale) + ' m²');
      this.text('[data-tile-total]', this.money.format(result.total / 100));
      this.text('[data-tile-unit-price]', this.money.format(this.current.unitPriceCents / 100));
      this.text('[data-tile-box-price]', this.money.format(this.current.priceCents / 100));
      this.text('[data-tile-box-area]', this.number.format(this.current.boxUnits / this.core.scale));
      const order = this.current.orderType || '';
      const delivery = this.current.leadTime || this.dataset.deliveryUnknown;
      this.text('[data-tile-delivery-text]', result.contact ? this.dataset.contactMessage : [order, delivery].filter(Boolean).join(' · '));
      this.querySelector('[data-tile-delivery]').classList.toggle('is-order', order.toLowerCase().includes('bestel'));
      this.querySelector('[data-tile-delivery]').classList.toggle('is-unknown', !order);
      this.querySelector('[data-tile-contact]').hidden = !result.contact;
      this.querySelector('[data-tile-delivery]').classList.toggle('is-contact', result.contact);
      this.querySelector('[data-tile-property]').value = String(this.current.boxUnits / this.core.scale);
      this.page?.querySelectorAll('.bc-product-sticky__price').forEach(element => { element.textContent = this.money.format(result.total / 100); });
    }
    async loadChoices() {
      try {
        const embedded = this.querySelector('[data-tile-catalog]');
        if (!embedded) return;
        const config = JSON.parse(embedded.textContent);
        if (config.schema !== 1 || config.group !== this.dataset.group || !Array.isArray(config.products)) throw new Error('choices');
        this.products = config.products;
        const selected = this.products.find(p => p.id === this.dataset.productId);
        if (!selected) throw new Error('article');
        this.current = { ...selected, ...this.current };
        if (this.preview) {
          const sku = new URL(location.href).searchParams.get('bc_tile_sku');
          const requested = this.products.find(p => p.sku === sku);
          if (requested) { this.current = requested; this.updatePreview(); }
        }
        this.renderChoices();
        this.calculate();
        this.restorePosition();
      } catch (_) {
        const status = this.querySelector('[data-tile-choice-status]');
        status.textContent = this.dataset.choiceError;
        status.hidden = false;
      } finally {
        this.querySelector('[data-tile-choices]').setAttribute('aria-busy', 'false');
      }
    }
    restorePosition() {
      try {
        const key = 'bc-tile-position:' + this.dataset.group;
        const saved = JSON.parse(sessionStorage.getItem(key));
        sessionStorage.removeItem(key);
        if (!saved || Date.now() - saved.at > 30000) return;
        requestAnimationFrame(() => requestAnimationFrame(() => {
          const anchor = this.querySelector('[data-tile-field="' + saved.field + '"]');
          if (anchor && !anchor.hidden) window.scrollBy({ top: anchor.getBoundingClientRect().top - saved.top, behavior: 'instant' });
        }));
      } catch (_) { }
    }
    nominalSize(value) {
      const parts = String(value).match(/[0-9]+(?:[.,][0-9]+)?/g);
      if (!parts || parts.length !== 2) return String(value);
      const sizes = { '14.3':15, '19.3':20, '29.4':30, '33.3':30, '44.3':45, '59.2':60, '59.5':60, '59.6':60, '60.2':60 };
      return parts.map(part => {
        const number = Number(part.replace(',', '.'));
        return sizes[String(number)] ?? number;
      }).sort((a,b) => a-b).map(number => this.number.format(number)).join(' x ') + ' cm';
    }
    renderChoices() {
      this.core.fields.forEach(field => {
        const holder = this.querySelector('[data-tile-field="' + field + '"]');
        let options = this.core.choices(this.products, this.current, field).sort((a, b) => {
          if (field === 'type') return Number(b.type === 'Vloertegel') - Number(a.type === 'Vloertegel');
          if (field === 'size') return b.area - a.area || String(a.size).localeCompare(String(b.size), 'nl', { numeric: true });
          if (field === 'thickness') return Number(a.thickness) - Number(b.thickness);
          return String(a[field] || '').localeCompare(String(b[field] || ''), 'nl', { numeric: true });
        });
        if (field === 'size') {
          const grouped = new Map();
          options.forEach(article => {
            const key = this.nominalSize(article.size);
            if (!grouped.has(key) || String(article.size) === String(this.current.size)) grouped.set(key, article);
          });
          options = [...grouped.values()];
        }
        holder.hidden = options.length < 2;
        const container = holder.querySelector('[data-tile-options]');
        container.replaceChildren();
        options.forEach(article => {
          const value = article[field];
          const selected = String(value) === String(this.current[field]);
          const button = document.createElement('button');
          button.type = 'button';
          button.className = (field === 'color' ? 'bc-tile__color' : 'bc-tile__option') + (selected ? ' is-selected' : '');
          button.setAttribute('aria-pressed', String(selected));
          button.dataset.choice = String(value);
          if (field === 'color') {
            const destination = this.core.choose(this.products, this.current, field, value);
            const image = document.createElement('img');
            if (destination?.image) image.src = this.imageUrl(destination.image, 240);
            image.alt = '';
            image.width = 72;
            image.height = 72;
            image.loading = 'lazy';
            button.append(image);
          }
          const label = document.createElement('span');
          label.textContent = field === 'size' ? this.nominalSize(value) : field === 'thickness' ? this.number.format(Number(value)) + ' mm' : String(value);
          button.append(label);
          button.addEventListener('click', () => this.select(field, value));
          container.append(button);
        });
      });
      this.text('[data-tile-current-color]', this.current.color);
      this.querySelectorAll('.bc-tile__colors [aria-pressed="true"]').forEach(element => { const row = element.parentElement; row.scrollLeft = Math.max(0, element.offsetLeft - row.offsetLeft - 8); });
      const controls = this.querySelector('[data-tile-choices]');
      controls.hidden = !Array.from(controls.querySelectorAll('[data-tile-field]')).some(element => !element.hidden);
      this.querySelector('[data-tile-fixed-choices]').hidden = !controls.hidden;
      this.setupColorRail();
    }
    setupColorRail() {
      const row = this.querySelector('.bc-tile__colors');
      if (!row || row.closest('[data-tile-field]').hidden) return;
      const field = row.closest('[data-tile-field]');
      let track = field.querySelector('.bc-tile__scroll-track');
      if (!track) {
        track = document.createElement('div');
        track.className = 'bc-tile__scroll-track';
        row.id ||= 'TileColors-' + this.dataset.productId;
        track.setAttribute('role', 'scrollbar');
        track.setAttribute('aria-controls', row.id);
        track.setAttribute('aria-orientation', 'horizontal');
        track.setAttribute('aria-label', field.querySelector('legend')?.textContent || this.current.color);
        track.setAttribute('aria-valuemin', '0');
        track.setAttribute('aria-valuemax', '100');
        track.tabIndex = 0;
        track.append(document.createElement('span'));
        row.after(track);
        let drag = null;
        const move = event => {
          if (!drag) return;
          const rect = track.getBoundingClientRect();
          const thumb = track.firstElementChild.getBoundingClientRect();
          const fraction = Math.max(0, Math.min(1, (event.clientX - rect.left - drag.offset) / Math.max(1, rect.width - thumb.width)));
          row.scrollTo({ left: fraction * (row.scrollWidth - row.clientWidth), behavior: 'instant' });
        };
        track.addEventListener('pointerdown', event => {
          if (event.button !== 0) return;
          const thumb = track.firstElementChild.getBoundingClientRect();
          drag = { offset: event.target === track.firstElementChild ? event.clientX - thumb.left : thumb.width / 2 };
          track.setPointerCapture(event.pointerId);
          move(event);
          event.preventDefault();
        });
        track.addEventListener('pointermove', move);
        track.addEventListener('pointerup', () => { drag = null; });
        track.addEventListener('pointercancel', () => { drag = null; });
        track.addEventListener('keydown', event => {
          const maximum = row.scrollWidth - row.clientWidth;
          const positions = { ArrowRight:row.scrollLeft + row.clientWidth / 2, ArrowLeft:row.scrollLeft - row.clientWidth / 2, Home:0, End:maximum };
          if (!(event.key in positions)) return;
          event.preventDefault();
          row.scrollTo({ left:Math.max(0, Math.min(maximum, positions[event.key])), behavior:'instant' });
        });
      }
      const refresh = () => {
        const overflow = row.scrollWidth - row.clientWidth;
        track.hidden = overflow <= 1;
        const fraction = row.scrollWidth ? row.clientWidth / row.scrollWidth : 1;
        track.setAttribute('aria-valuenow', String(overflow > 0 ? Math.round(Math.max(0, Math.min(1, row.scrollLeft / overflow)) * 100) : 0));
        track.firstElementChild.style.width = Math.min(100, fraction * 100) + '%';
        track.firstElementChild.style.marginLeft = overflow > 0 ? Math.max(0, Math.min(1, row.scrollLeft / overflow)) * (1 - fraction) * 100 + '%' : '0%';
      };
      this.railObserver?.disconnect();
      if (typeof ResizeObserver !== 'undefined') {
        this.railObserver = new ResizeObserver(refresh);
        this.railObserver.observe(row);
      }
      if (this.railScrollHandler) row.removeEventListener('scroll', this.railScrollHandler);
      this.railScrollHandler = refresh;
      row.addEventListener('scroll', refresh, { passive: true });
      const selected = row.querySelector('[aria-pressed="true"]');
      if (selected && selected.offsetLeft + selected.offsetWidth > row.scrollLeft + row.clientWidth) row.scrollLeft = selected.offsetLeft + selected.offsetWidth - row.clientWidth;
      if (typeof requestAnimationFrame === 'function') requestAnimationFrame(refresh);
      else refresh();
    }
    disconnectedCallback() {
      this.railObserver?.disconnect();
    }
    imageUrl(value, width) {
      const url = new URL(value, location.origin);
      if (url.protocol !== 'https:' || !(url.hostname === 'cdn.shopify.com' || url.hostname.endsWith('.shopify.com') || url.hostname === location.hostname)) throw new Error('image');
      url.searchParams.set('width', String(width));
      return url.href;
    }
    select(field, value) {
      const next = this.core.choose(this.products, this.current, field, value);
      if (!next || next.id === this.current.id) return;
      this.save();
      if (!this.preview) {
        try {
          const anchor = this.querySelector('[data-tile-field="' + field + '"]');
          sessionStorage.setItem('bc-tile-position:' + this.dataset.group, JSON.stringify({ field, top: anchor.getBoundingClientRect().top, at: Date.now() }));
        } catch (_) { }
        const destination = new URL(this.dataset.rootUrl.replace(/\/$/, '') + '/products/' + encodeURIComponent(next.handle), location.origin);
        const theme = new URL(location.href).searchParams.get('preview_theme_id');
        if (theme) destination.searchParams.set('preview_theme_id', theme);
        location.assign(destination.href);
        return;
      }
      this.current = next;
      if (!this.explicitArea) this.area.value = '';
      this.updatePreview();
      this.renderChoices();
      this.calculate();
      const replacement = this.querySelector('[data-tile-field="' + field + '"] [aria-pressed="true"]');
      replacement?.focus({ preventScroll: true });
    }
    updatePreview() {
      const current = this.current;
      this.form?.querySelectorAll('input[name="id"]').forEach(input => { input.value = current.variant; });
      const title = this.page?.querySelector('.bc-product__title');
      if (title) title.textContent = current.title;
      const sku = this.page?.querySelector('.bc-product__sku');
      if (sku) sku.textContent = sku.textContent.replace(/PO\d+/, current.sku);
      this.page?.querySelectorAll('.bc-product-specs__value').forEach(element => {
        if (/^PO\d+$/.test(element.textContent.trim())) element.textContent = current.sku;
      });
      this.querySelectorAll('[data-bc-wishlist-toggle]').forEach(button => {
        button.dataset.bcWishlistHandle = current.handle;
        button.dataset.bcWishlistVariant = current.variant;
        button.dataset.bcWishlistTitle = current.title;
        button.dataset.bcWishlistImage = this.imageUrl(current.image, 480);
        button.setAttribute('aria-pressed', 'false');
        button.setAttribute('aria-label', current.title);
      });
      this.page?.querySelectorAll('.bc-product-sticky__title').forEach(element => { element.textContent = current.title; });
      const gallery = this.page?.querySelector('media-gallery');
      const hero = gallery?.querySelector('.product__media img');
      const thumb = gallery?.querySelector('.thumbnail img');
      const modal = document.getElementById('ProductModal-' + this.dataset.section)?.querySelector('img');
      [hero, thumb, modal, this.page?.querySelector('img.bc-product-sticky__image')].filter(Boolean).forEach(image => {
        image.src = this.imageUrl(current.image, 1946);
        image.srcset = [160, 320, 600, 900, 1200, 1600, 1946].map(width => this.imageUrl(current.image, width) + ' ' + width + 'w').join(', ');
        image.alt = current.title;
      });
      const firstMedia = gallery?.querySelector('[data-media-id]');
      if (firstMedia && typeof gallery.setActiveMedia === 'function') gallery.setActiveMedia(firstMedia.dataset.mediaId, false);
      const url = new URL(location.href);
      url.searchParams.set('bc_tile_sku', current.sku);
      history.replaceState(history.state, '', url.href);
    }
  });
}


