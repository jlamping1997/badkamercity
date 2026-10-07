/* Mirrors the existing product controls; no separate cart request or variant state. */
if (!customElements.get('bc-product-sticky')) {
  customElements.define('bc-product-sticky', class extends HTMLElement {
    connectedCallback() {
      this.root = this.closest('product-info');
      this.buybox = this.root?.querySelector('.product__info-container');
      if (!this.buybox) return;
      this.controller = new AbortController();
      const options = { signal: this.controller.signal };
      this.submit = this.querySelector('[data-sticky-submit]');
      this.quantity = this.querySelector('[data-sticky-quantity]');
      this.price = this.querySelector('[data-sticky-price]');
      this.label = this.querySelector('[data-sticky-label]');
      this.error = this.querySelector('[data-sticky-error]');
      this.refresh = () => {
        cancelAnimationFrame(this.frame);
        this.frame = requestAnimationFrame(() => this.sync());
      };
      this.submit.addEventListener('click', () => {
        const original = this.originalSubmit();
        if (!original || original.disabled || original.getAttribute('aria-disabled') === 'true' ||
            this.root.dataset.bcNavigating === 'true') return;
        const input = this.originalQuantity();
        if (input && !this.quantity.checkValidity()) {
          this.quantity.reportValidity();
          return;
        }
        if (input && !input.checkValidity()) {
          input.scrollIntoView({ block: 'center' });
          input.reportValidity();
          return;
        }
        original.click();
        this.refresh();
      }, options);
      this.quantity.addEventListener('change', () => {
        if (!this.quantity.reportValidity()) return;
        const original = this.originalQuantity();
        if (!original) return;
        original.value = this.quantity.value;
        original.dispatchEvent(new Event('change', { bubbles: true }));
        this.refresh();
      }, options);
      [['minus', '[data-sticky-minus]'], ['plus', '[data-sticky-plus]']].forEach(([name, selector]) => {
        this.querySelector(selector).addEventListener('click', () => {
          this.buybox.querySelector(`quantity-input button[name="${name}"]`)?.click();
          this.refresh();
        }, options);
      });
      this.buybox.addEventListener('change', this.refresh, options);
      this.buybox.addEventListener('input', this.refresh, options);
      window.addEventListener('scroll', this.refresh, { ...options, passive: true });
      window.addEventListener('resize', this.refresh, options);
      this.observer = new MutationObserver(this.refresh);
      this.observer.observe(this.buybox, { subtree: true, childList: true, characterData: true, attributes: true });
      this.sync();
    }

    originalSubmit() {
      return this.buybox.querySelector('.product-form__submit');
    }

    originalQuantity() {
      return this.buybox.querySelector('input[name="quantity"]');
    }

    sync() {
      const original = this.originalSubmit();
      const actions = this.buybox.querySelector('.bc-buybox__section--actions');
      if (!original || !actions) {
        this.hidden = true;
        return;
      }
      this.hidden = actions.getBoundingClientRect().bottom > 0 || this.root.getBoundingClientRect().bottom < 120;
      const disabled = original.disabled || original.getAttribute('aria-disabled') === 'true';
      const navigating = this.root.dataset.bcNavigating === 'true';
      const busy = navigating || original.classList.contains('loading');
      this.submit.disabled = disabled || busy;
      this.submit.setAttribute('aria-busy', String(busy));
      const state = original.querySelector('[data-submit-state]');
      this.label.textContent = navigating ? 'Uitvoering laden…' : busy ? 'Toevoegen…' : disabled ? (state?.textContent.trim() || 'Niet beschikbaar') : 'In winkelwagen';
      const currentPrice = this.buybox.querySelector('.bc-buybox__price-current');
      this.price.textContent = currentPrice?.textContent.trim() || '';
      const sourceError = this.buybox.querySelector('.product-form__error-message');
      const errorWrapper = this.buybox.querySelector('.product-form__error-message-wrapper');
      const errorText = errorWrapper && !errorWrapper.hidden ? sourceError?.textContent.trim() : '';
      if (this.error.textContent !== (errorText || '')) this.error.textContent = errorText || '';
      this.error.hidden = !errorText;
      const input = this.originalQuantity();
      this.querySelector('.bc-product-sticky__quantity').hidden = !input;
      if (!input) return;
      if (document.activeElement !== this.quantity) this.quantity.value = input.value;
      this.quantity.required = input.required;
      ['min', 'max', 'step'].forEach(name => {
        const value = input.getAttribute(name);
        if (value === null) this.quantity.removeAttribute(name);
        else this.quantity.setAttribute(name, value);
      });
      ['minus', 'plus'].forEach(name => {
        const source = this.buybox.querySelector(`quantity-input button[name="${name}"]`);
        this.querySelector(`[data-sticky-${name}]`).disabled = !source || source.disabled || source.classList.contains('disabled');
      });
    }

    disconnectedCallback() {
      this.controller?.abort();
      this.observer?.disconnect();
      cancelAnimationFrame(this.frame);
    }
  });
}
