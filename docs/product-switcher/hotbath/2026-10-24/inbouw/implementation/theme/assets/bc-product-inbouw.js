if (!customElements.get('bc-inbouw-addon')) {
  customElements.define('bc-inbouw-addon', class extends HTMLElement {
    connectedCallback() {
      if (this.controller) return;
      this.controller = new AbortController();
      this.root = this.closest('product-info');
      this.form = this.closest('form');
      this.productForm = this.closest('product-form');
      this.controls = this.querySelector('[data-inbouw-controls]');
      this.error = this.querySelector('[data-inbouw-error]');
      this.cartLink = this.querySelector('[data-inbouw-cart-link]');
      this.choices = Array.from(this.querySelectorAll('[data-inbouw-choice]'));
      this.busy = this.busy || false;
      this.uncertain = this.uncertain || false;
      this.pageLeaving = false;
      this.storageKey = 'bc-inbouw-choice-v1';
      const options = { signal: this.controller.signal };
      this.addEventListener('change', () => this.update(), options);
      this.form?.addEventListener('input', () => this.updateTotal(), options);
      this.form?.addEventListener('change', () => this.updateTotal(), options);
      const quantity = this.form?.elements.namedItem('quantity');
      if (quantity && !this.form.contains(quantity)) {
        quantity.addEventListener('input', () => this.updateTotal(), options);
        quantity.addEventListener('change', () => this.updateTotal(), options);
      }
      window.addEventListener('pagehide', () => {
        this.rememberForNavigation();
        this.pageLeaving = true;
      }, options);
      window.addEventListener('pageshow', event => {
        this.pageLeaving = false;
        if (event.persisted && this.busy) this.markUncertain();
      }, options);
      this.restoreChoice();
      if (this.root) {
        this.navigationObserver = new MutationObserver(() => {
          if (this.root.dataset.bcNavigating === 'true') this.rememberForNavigation();
        });
        this.navigationObserver.observe(this.root, { attributes: true, attributeFilter: ['data-bc-navigating'] });
      }
      if (this.controls) this.controls.hidden = false;
      this.ready = true;
      this.update();
    }

    validIdentity() {
      const id = this.form?.elements.namedItem('id')?.value;
      return this.dataset.valid === 'true' && /^\d+$/.test(this.dataset.parentVariant || '') &&
        /^\d+$/.test(this.dataset.bodyVariant || '') && this.dataset.parentVariant !== this.dataset.bodyVariant &&
        Boolean(this.dataset.parentSku && this.dataset.bodySku) && id === this.dataset.parentVariant &&
        Number.isSafeInteger(Number(this.dataset.quantityPerTrim)) && Number(this.dataset.quantityPerTrim) > 0;
    }

    group() {
      return this.root?.querySelector('[data-bc-product-switcher-v2]')?.dataset.switchGroup || '';
    }

    choice() {
      return this.choices.find(input => input.checked)?.value || '';
    }

    rememberForNavigation() {
      const choice = this.choice();
      const group = this.group();
      if (!this.validIdentity() || this.busy || this.uncertain || !group ||
          this.root?.dataset.bcNavigating !== 'true' || !['yes', 'no'].includes(choice)) return;
      try {
        sessionStorage.setItem(this.storageKey, JSON.stringify({
          group, body: this.dataset.bodyVariant, choice, from: window.location.pathname, savedAt: Date.now()
        }));
      } catch (_) {}
    }

    restoreChoice() {
      let saved;
      try {
        saved = JSON.parse(sessionStorage.getItem(this.storageKey) || 'null');
        sessionStorage.removeItem(this.storageKey);
      } catch (_) { return; }
      if (!saved || !this.validIdentity() || !this.group() || saved.group !== this.group() ||
          saved.body !== this.dataset.bodyVariant || saved.from === window.location.pathname ||
          !['yes', 'no'].includes(saved.choice)) return;
      const age = Date.now() - Number(saved.savedAt);
      if (!Number.isFinite(age) || age < 0 || age > 30000) return;
      const option = this.choices.find(input => input.value === saved.choice);
      if (option) option.checked = true;
    }

    update() {
      const valid = this.validIdentity();
      if (this.controls) this.controls.disabled = !valid || this.busy || this.uncertain;
      this.choices.forEach(input => {
        input.disabled = !valid || this.busy || this.uncertain ||
          (input.value === 'yes' && this.dataset.bodyAvailable !== 'true');
      });
      if (!valid) this.showError(this.dataset.messageChanged, false, false);
      else if (this.uncertain) this.showError(this.dataset.messageUncertain, true, false);
      else if (this.choice() === 'yes' && this.dataset.bodyAvailable !== 'true') {
        this.showError(this.dataset.messageUnavailable, false, false);
      } else if (this.error && !this.busy) {
        this.error.hidden = true;
        if (this.cartLink) this.cartLink.hidden = true;
      }
      this.updateTotal();
    }

    quantity() {
      const control = this.form?.elements.namedItem('quantity');
      const quantity = control ? Number(control.value) : 1;
      if ((control && (!String(control.value).trim() || !control.checkValidity())) ||
          !Number.isSafeInteger(quantity) || quantity < 1) return null;
      const bodyQuantity = quantity * Number(this.dataset.quantityPerTrim);
      if (!Number.isSafeInteger(bodyQuantity) || bodyQuantity < 1) return null;
      return { quantity, bodyQuantity };
    }

    updateTotal() {
      const total = this.querySelector('[data-inbouw-total]');
      if (!total) return;
      const quantities = this.quantity();
      const price = Number(this.dataset.bodyPrice);
      total.hidden = this.choice() !== 'yes' || !quantities || !Number.isFinite(price) || price < 0;
      if (total.hidden) return;
      try {
        total.textContent = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', {
          style: 'currency', currency: this.dataset.currency || 'EUR'
        }).format(price * quantities.bodyQuantity / 100);
      } catch (_) { total.hidden = true; }
    }

    showError(message, checkCart = false, focus = true) {
      if (this.error) {
        this.error.textContent = message || this.dataset.messageChanged || '';
        this.error.hidden = false;
        if (focus) this.error.focus();
      }
      if (this.cartLink) this.cartLink.hidden = !checkCart;
    }

    setBusy(value) {
      this.busy = value;
      const button = this.productForm?.submitButton || this.form?.querySelector('[type="submit"]');
      if (button) {
        button.classList.toggle('loading', value);
        if (value) {
          button.setAttribute('aria-disabled', 'true');
          button.setAttribute('aria-busy', 'true');
        } else {
          button.removeAttribute('aria-busy');
          if (!this.uncertain) button.removeAttribute('aria-disabled');
        }
      }
      this.productForm?.querySelector('.loading__spinner')?.classList.toggle('hidden', !value);
      this.update();
    }

    markUncertain() {
      this.uncertain = true;
      this.setBusy(false);
      const button = this.productForm?.submitButton || this.form?.querySelector('[type="submit"]');
      button?.setAttribute('aria-disabled', 'true');
      this.showError(this.dataset.messageUncertain, true);
    }

    handleSubmit(productForm) {
      this.productForm = productForm;
      if (!this.ready || this.busy || this.uncertain || !this.isConnected || this.pageLeaving ||
          this.root?.dataset.bcNavigating === 'true') return true;
      if (!this.validIdentity()) {
        this.showError(this.dataset.messageChanged);
        return true;
      }
      const choice = this.choice();
      if (!['yes', 'no'].includes(choice)) {
        this.showError(this.dataset.messageChoice);
        this.choices.find(input => !input.disabled)?.focus();
        return true;
      }
      const quantities = this.quantity();
      if (!quantities) {
        this.showError(this.dataset.messageQuantity);
        this.form.elements.namedItem('quantity')?.focus();
        return true;
      }
      if (choice === 'no') return false;
      if (this.dataset.bodyAvailable !== 'true') {
        this.showError(this.dataset.messageUnavailable);
        return true;
      }
      const formData = new FormData(this.form);
      const trim = { id: this.dataset.parentVariant, quantity: quantities.quantity };
      const properties = {};
      for (const [name, value] of formData.entries()) {
        const match = name.match(/^properties\[(.+)\]$/);
        if (match && typeof value === 'string') properties[match[1]] = value;
      }
      if (Object.keys(properties).length) trim.properties = properties;
      if (formData.get('selling_plan')) trim.selling_plan = formData.get('selling_plan');
      const items = [trim, { id: this.dataset.bodyVariant, quantity: quantities.bodyQuantity }];
      this.productForm.handleErrorMessage();
      if (this.error) this.error.hidden = true;
      if (this.cartLink) this.cartLink.hidden = true;
      this.setBusy(true);
      this.pendingAdd = this.addItems(items);
      return true;
    }

    async addItems(items) {
      const requestController = new AbortController();
      const timeout = setTimeout(() => requestController.abort(), 30000);
      try {
        const response = await fetch(this.dataset.addUrl, {
          method: 'POST', credentials: 'same-origin', signal: requestController.signal,
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ items })
        });
        const result = await response.json();
        const expected = new Map([
          [this.dataset.parentVariant, this.dataset.parentSku],
          [this.dataset.bodyVariant, this.dataset.bodySku]
        ]);
        if (!response.ok || result.status || !Array.isArray(result.items) ||
            !items.every(requested => result.items.some(item =>
              String(item.variant_id || item.id) === requested.id && item.sku === expected.get(requested.id) &&
              Number.isSafeInteger(item.quantity) && item.quantity >= requested.quantity))) {
          throw new Error('unconfirmed-cart-add');
        }
        if (this.isConnected && !this.pageLeaving) window.location.assign(this.dataset.cartUrl);
      } catch (_) {
        this.markUncertain();
      } finally {
        clearTimeout(timeout);
      }
    }

    disconnectedCallback() {
      this.controller?.abort();
      this.navigationObserver?.disconnect();
      this.controller = null;
    }
  });
}
