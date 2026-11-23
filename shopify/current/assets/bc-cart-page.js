(() => {
  if (window.BCCartPage) return;

  class CartPage {
    busy = false;
    cart = null;
    stateKnown = false;
    locked = new Map();
    summaryValues = new WeakMap();
    message = '';
    messageType = '';
    quantityResult = null;
    initializing = null;
    refreshRequested = false;
    mustReload = false;

    isActive(cartItems) {
      return Boolean(document.querySelector('bc-cart-discount') && (!cartItems || cartItems.tagName === 'CART-ITEMS'));
    }

    mount(component) {
      component.hidden = false;
      this.render();
      this.lockControls();
      if (!this.cart && !this.initializing) {
        this.initializing = this.readCart()
          .then((cart) => this.acceptCart(cart))
          .catch(() => this.setMessage('error', 'error'))
          .finally(() => { this.initializing = null; });
      }
    }

    component() {
      return document.querySelector('bc-cart-discount');
    }

    text(name) {
      return this.component()?.dataset[`message${name.charAt(0).toUpperCase()}${name.slice(1)}`] || '';
    }

    codes() {
      return (this.cart?.discount_codes || []).filter((code) => code.applicable === true);
    }

    acceptCart(cart) {
      if (!cart || !Array.isArray(cart.items) || !Number.isFinite(cart.total_price)) throw new Error('cart');
      this.cart = cart;
      this.stateKnown = Array.isArray(cart.discount_codes);
      this.render();
    }

    async readCart() {
      const url = this.component()?.dataset.cartUrl || window.routes?.cart_url;
      const response = await fetch(`${url.replace(/\/$/, '')}.js`, { headers: { Accept: 'application/json' }, cache: 'no-store' });
      if (!response.ok) throw new Error('cart');
      return response.json();
    }

    sections() {
      return document.querySelector('cart-items')?.getSectionsToRender() || [];
    }

    renderSections(data, cart) {
      const parts = this.sections().map((section) => {
        const targetRoot = document.getElementById(section.id);
        const html = data?.[section.section];
        if (!targetRoot || typeof html !== 'string') throw new Error('section');
        const source = new DOMParser().parseFromString(html, 'text/html').querySelector(section.selector);
        const target = targetRoot.querySelector(section.selector) || targetRoot;
        if (!source) throw new Error('section');
        return { source, target };
      });
      if (parts.length !== 4) throw new Error('section');
      parts.forEach(({ target, source }) => { target.innerHTML = source.innerHTML; });
      document.querySelector('cart-items')?.classList.toggle('is-empty', cart.item_count === 0);
      document.getElementById('main-cart-footer')?.classList.toggle('is-empty', cart.item_count === 0);
      this.acceptCart(cart);
      this.lockControls();
    }

    async refreshSections(cart) {
      const url = new URL(this.component()?.dataset.cartUrl || window.routes.cart_url, window.location.origin);
      new URLSearchParams(window.location.search).forEach((value, key) => url.searchParams.set(key, value));
      url.searchParams.set('sections', this.sections().map((section) => section.section).join(','));
      const response = await fetch(url.pathname + url.search, { headers: { Accept: 'application/json' }, cache: 'no-store' });
      if (!response.ok) throw new Error('sections');
      this.renderSections(await response.json(), cart);
    }

    publish(cart) {
      if (typeof publish === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
        publish(PUB_SUB_EVENTS.cartUpdate, { source: 'cart-items', cartData: cart });
      }
    }

    setMessage(name, type = '') {
      this.message = name;
      this.messageType = type;
      const status = this.component()?.querySelector('[data-bc-discount-status]');
      if (status) {
        status.textContent = this.text(name);
        status.hidden = !name;
        status.dataset.state = type;
      }
    }

    monetaryCodes() {
      const applications = [...(this.cart?.cart_level_discount_applications || [])];
      (this.cart?.items || []).forEach((item) => {
        (item.line_level_discount_allocations || []).forEach((allocation) => applications.push(allocation.discount_application));
      });
      return new Set(applications.filter((application) => application?.type === 'discount_code' && application.target_type !== 'shipping_line')
        .map((application) => String(application.title).toLowerCase()));
    }

    render() {
      const component = this.component();
      if (!component) return;
      const list = component.querySelector('[data-bc-discount-codes]');
      const monetary = this.monetaryCodes();
      const hasPending = this.codes().some((code) => !monetary.has(code.code.toLowerCase()));
      if (list) {
        list.replaceChildren();
        this.codes().forEach(({ code }) => {
          const item = document.createElement('li');
          item.className = 'bc-cart-discount__code';
          const label = document.createElement('span');
          label.textContent = code;
          const remove = document.createElement('button');
          remove.type = 'button';
          remove.dataset.bcDiscountRemove = code;
          remove.setAttribute('aria-label', this.text('remove').replace('[code]', code));
          remove.textContent = '×';
          item.append(label, remove);
          list.append(item);
        });
        list.hidden = list.childElementCount === 0;
      }
      const summary = component.closest('[data-bc-cart-summary]') || component.closest('.js-contents');
      if (summary) {
        const price = summary.querySelector('[data-bc-shipping-price]');
        const total = summary.querySelector('[data-bc-order-total]');
        const label = summary.querySelector('[data-bc-total-label]');
        const promise = summary.querySelector('[data-bc-shipping-promise]');
        if (!this.summaryValues.has(summary)) this.summaryValues.set(summary, {
          price: price?.textContent, total: total?.textContent, label: label?.textContent, promiseHidden: promise?.hidden,
        });
        const saved = this.summaryValues.get(summary);
        if (price) price.textContent = hasPending ? summary.dataset.bcShippingPendingLabel : saved.price;
        if (total) total.textContent = hasPending ? summary.dataset.bcProductTotal : saved.total;
        if (label) label.textContent = hasPending ? summary.dataset.bcTotalLabel : saved.label;
        if (promise) promise.hidden = hasPending || saved.promiseHidden;
      }
      this.setMessage(this.message, this.messageType);
      window.BCCartTools?.sync();
    }

    lockControls() {
      if (!this.busy) return;
      const items = document.querySelector('cart-items');
      if (items && !this.locked.has(items)) {
        this.locked.set(items, { inert: items.inert });
        items.inert = true;
        items.setAttribute('aria-busy', 'true');
      }
      document.querySelectorAll('#main-cart-footer button, #main-cart-footer input[name="discount"]').forEach((control) => {
        if (this.locked.has(control)) return;
        if (control instanceof HTMLButtonElement) {
          this.locked.set(control, { disabled: control.disabled });
          control.disabled = true;
        } else {
          this.locked.set(control, { readOnly: control.readOnly });
          control.readOnly = true;
        }
      });
      this.component()?.setAttribute('aria-busy', 'true');
    }

    unlockControls() {
      this.locked.forEach((state, control) => {
        if ('inert' in state) { control.inert = state.inert; control.removeAttribute('aria-busy'); }
        if ('disabled' in state) control.disabled = state.disabled;
        if ('readOnly' in state) control.readOnly = state.readOnly;
      });
      this.locked.clear();
      this.component()?.removeAttribute('aria-busy');
    }

    reloadCart() {
      this.mustReload = true;
      this.stateKnown = false;
      this.setMessage('error', 'error');
      window.location.reload();
    }

    async run(operation, fallbackFocusId) {
      if (this.busy) return;
      this.busy = true;
      const activeId = document.activeElement?.id;
      this.lockControls();
      try {
        if (this.initializing) await this.initializing;
        return await operation();
      } finally {
        if (this.refreshRequested) {
          this.refreshRequested = false;
          try { await this.refreshSections(await this.readCart()); }
          catch { this.reloadCart(); }
        }
        if (this.mustReload) return;
        this.busy = false;
        this.unlockControls();
        if (document.activeElement === document.body) {
          const focus = document.getElementById(activeId) || document.getElementById(fallbackFocusId);
          focus?.focus({ preventScroll: true });
        }
      }
    }

    externalUpdate() {
      if (this.busy) { this.refreshRequested = true; return; }
      return this.run(async () => {
        try { await this.refreshSections(await this.readCart()); }
        catch { this.reloadCart(); }
      });
    }

    async quantity(cartItems, update) {
      const focusId = document.activeElement?.closest('.cart-item')?.querySelector('input[name="updates[]"]')?.id;
      return this.run(async () => {
        this.quantityResult = null;
        await update();
        if (!this.quantityResult || (!this.quantityResult.errors && !this.stateKnown)) {
          try {
            const cart = await this.readCart();
            await this.refreshSections(cart);
            this.publish(cart);
          } catch {
            this.reloadCart();
          }
        }
      }, focusId);
    }

    quantityUpdated(cart) {
      this.quantityResult = cart;
      if (!cart.errors) this.acceptCart(cart);
      this.lockControls();
    }

    async discount(code, remove = false) {
      if (this.busy) return;
      const value = code.trim();
      if (!value) { this.setMessage('empty', 'error'); return; }
      return this.run(async () => {
        this.setMessage('loading');
        let cart;
        let updated = false;
        let mutationAttempted = false;
        try {
          if (!this.stateKnown) this.acceptCart(await this.readCart());
          if (!this.stateKnown) throw new Error('codes');
          const previous = this.codes().map(({ code: existing }) => existing);
          const codes = previous.filter((existing) => existing.toLowerCase() !== value.toLowerCase());
          if (!remove) codes.push(value);
          const url = this.component().dataset.updateUrl || window.routes.cart_update_url;
          mutationAttempted = true;
          const response = await fetch(url, {
            method: 'POST',
            headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
            body: JSON.stringify({ discount: codes.join(','), sections: this.sections().map((section) => section.section), sections_url: window.location.pathname + window.location.search }),
          });
          cart = await response.json();
          if (!response.ok || cart.errors || !Array.isArray(cart.items)) throw new Error('discount');
          const renderedSections = cart.sections;
          this.acceptCart(cart);
          if (!this.stateKnown) { cart = await this.readCart(); this.acceptCart(cart); }
          try { this.renderSections(renderedSections, cart); }
          catch { await this.refreshSections(cart); }
          updated = true;
        } catch {
          try {
            cart = await this.readCart();
            await this.refreshSections(cart);
            updated = true;
          } catch {
            if (mutationAttempted) this.reloadCart();
            else { this.stateKnown = false; this.setMessage('error', 'error'); }
          }
        }
        if (!updated) return;
        this.publish(cart);
        const applied = cart.discount_codes?.find((entry) => entry.code.toLowerCase() === value.toLowerCase());
        if (remove) this.setMessage(applied?.applicable ? 'error' : 'removed', applied?.applicable ? 'error' : 'success');
        else if (applied?.applicable === false) this.setMessage('invalid', 'error');
        else if (applied?.applicable === true) {
          this.setMessage(this.monetaryCodes().has(value.toLowerCase()) ? 'success' : 'pending', 'success');
          const input = this.component()?.querySelector('input[name="discount"]');
          if (input) input.value = '';
        } else this.setMessage('error', 'error');
      });
    }
  }

  const page = new CartPage();
  window.BCCartPage = page;

  document.addEventListener('submit', (event) => {
    const form = event.target;
    if (!(form instanceof HTMLFormElement)) return;
    if (form.matches('[data-bc-discount-form]')) {
      event.preventDefault();
      page.discount(form.querySelector('input[name="discount"]')?.value || '');
    } else if (form.id === 'cart' && page.busy) event.preventDefault();
  }, true);

  document.addEventListener('click', (event) => {
    const target = event.target instanceof Element ? event.target : null;
    const remove = target?.closest('[data-bc-discount-remove]');
    if (remove) {
      event.preventDefault();
      page.discount(remove.dataset.bcDiscountRemove, true);
    }
    if (page.busy && target?.closest('#main-cart-items, button[name="checkout"], .cart__dynamic-checkout-buttons')) {
      event.preventDefault();
      event.stopImmediatePropagation();
    }
  }, true);

  if (!customElements.get('bc-cart-discount')) {
    customElements.define('bc-cart-discount', class extends HTMLElement {
      connectedCallback() { page.mount(this); }
    });
  }
})();

