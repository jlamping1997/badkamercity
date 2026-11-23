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
      this.quantity = this.querySelector('[data-tile-quantity]');
      this.submit = this.form?.querySelector('[type="submit"]');
      this.initialDisabled = this.submit?.disabled;
      this.money = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', { style: 'currency', currency: this.dataset.currency });
      this.number = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', { maximumFractionDigits: 4 });
      this.preview = this.dataset.preview === 'true';
      this.current = { sku: this.dataset.sku, boxUnits: Number(this.dataset.boxUnits), priceCents: Number(this.dataset.priceCents), unitPriceCents: Number(this.dataset.unitPriceCents), leadTime: this.dataset.leadTime, orderType: this.dataset.orderType };
      this.cacheKey = 'bc-tile-area:' + (this.dataset.group || this.dataset.productId);
      try {
        const saved = JSON.parse(sessionStorage.getItem(this.cacheKey));
        if (saved && this.core.units(saved.area)) { this.area.value = saved.area; this.waste.value = String(saved.waste === true ? 10 : saved.waste === false ? 0 : ([0,5,10,15,20].includes(Number(saved.waste)) ? Number(saved.waste) : 0)); this.explicitArea = true; }
      } catch (_) { }
      this.area.addEventListener('input', () => { this.explicitArea = true; this.calculate(); this.save(); });
      this.waste.addEventListener('change', () => { this.calculate(); this.save(); });
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
        if (this.explicitArea && this.core.units(this.area.value)) sessionStorage.setItem(this.cacheKey, JSON.stringify({ area: this.area.value, waste: Number(this.waste.value) }));
      } catch (_) { }
    }
    calculate() {
      const result = this.core.calculate(this.area.value, Number(this.waste.value), this.current.boxUnits, this.current.priceCents);
      const error = this.querySelector('[data-tile-error]');
      error.hidden = Boolean(result);
      error.textContent = result ? '' : this.dataset.areaError;
      this.area.setAttribute('aria-invalid', String(!result));
      if (this.submit) this.submit.disabled = this.initialDisabled || !result;
      this.page?.querySelectorAll('[data-sticky-submit]').forEach(button => { button.disabled = this.initialDisabled || !result; });
      if (!result) return;
      this.quantity.value = String(result.boxes);
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
    renderChoices() {
      this.core.fields.forEach(field => {
        const holder = this.querySelector('[data-tile-field="' + field + '"]');
        const options = this.core.choices(this.products, this.current, field).sort((a, b) => {
          if (field === 'type') return Number(b.type === 'Vloertegel') - Number(a.type === 'Vloertegel');
          if (field === 'size') return b.area - a.area || String(a.size).localeCompare(String(b.size), 'nl', { numeric: true });
          if (field === 'thickness') return Number(a.thickness) - Number(b.thickness);
          return String(a[field] || '').localeCompare(String(b[field] || ''), 'nl', { numeric: true });
        });
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
            const image = document.createElement('img');
            if (article.image) image.src = this.imageUrl(article.image, 240);
            image.alt = '';
            image.width = 72;
            image.height = 72;
            image.loading = 'lazy';
            button.append(image);
          }
          const label = document.createElement('span');
          label.textContent = field === 'thickness' ? this.number.format(Number(value)) + ' mm' : String(value);
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
        track.setAttribute('aria-hidden', 'true');
        track.append(document.createElement('span'));
        row.after(track);
      }
      const refresh = () => {
        const overflow = row.scrollWidth - row.clientWidth;
        track.hidden = overflow <= 1;
        const fraction = row.scrollWidth ? row.clientWidth / row.scrollWidth : 1;
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
      if (!this.explicitArea) this.area.value = this.number.format(next.boxUnits / this.core.scale);
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


