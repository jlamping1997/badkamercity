(() => {
  const selector = 'product-info[data-hotbath-mobile-a="true"]';
  if (window.bcHotbathMobilePurchase) {
    window.bcHotbathMobilePurchase.mount(document);
    return;
  }
  const instances = new Map();
  const setText = (node, text) => {
    if (node.textContent !== text) node.textContent = text;
  };
  const setHidden = (node, hidden) => {
    if (node.hidden !== hidden) node.hidden = hidden;
  };
  const readInteger = value => {
    if (!/^\d+$/.test(String(value ?? ''))) return null;
    const number = Number(value);
    return Number.isSafeInteger(number) ? number : null;
  };

  class MobilePurchase {
    constructor(root) {
      this.root = root;
      this.controller = new AbortController();
      this.media = window.matchMedia('(max-width: 749px)');
      this.schedule = () => {
        cancelAnimationFrame(this.frame);
        this.frame = requestAnimationFrame(() => this.refresh());
      };
      const options = { signal: this.controller.signal };
      this.root.addEventListener('input', this.schedule, options);
      this.root.addEventListener('change', this.schedule, options);
      this.media.addEventListener('change', this.schedule, options);
      window.addEventListener('pageshow', this.schedule, options);
      this.observer = new MutationObserver(this.schedule);
      this.buybox = root.querySelector('.product__info-container');
      if (this.buybox) this.observer.observe(this.buybox, { childList: true, subtree: true, attributes: true,
        attributeFilter: ['value', 'checked', 'disabled'] });
      this.observer.observe(root, { attributes: true,
        attributeFilter: ['data-product-price', 'data-product-variant', 'data-currency'] });
      this.refresh();
    }

    findForm() {
      return this.root.querySelector('.bc-buybox__section--actions product-form form');
    }

    refresh() {
      if (!this.root.isConnected) {
        this.destroy();
        instances.delete(this.root);
        return;
      }
      const form = this.findForm();
      if (!this.media.matches || !form || this.root.querySelector('.bc-buybox__purchase-row--volume')) {
        this.deactivate();
        return;
      }
      if (form !== this.form) {
        this.deactivate();
        if (!this.activate(form)) return;
      }
      this.updateTotal();
    }

    activate(form) {
      const submit = form.querySelector('.product-form__submit');
      if (!submit || !/^\d+$/.test(this.root.dataset.productVariant || '')) return false;
      let anchor = form.querySelector('.bc-product-form__buttons') || submit;
      while (anchor.parentElement && anchor.parentElement !== form) anchor = anchor.parentElement;
      if (anchor.parentElement !== form) return false;
      this.form = form;
      this.summary = document.createElement('div');
      this.summary.className = 'bc-hotbath-mobile-total';
      this.summary.dataset.mobileTotal = '';
      this.summary.setAttribute('role', 'status');
      this.summary.setAttribute('aria-live', 'polite');
      this.summary.setAttribute('aria-atomic', 'true');
      this.totalLine = document.createElement('div');
      this.totalLine.className = 'bc-hotbath-mobile-total__line';
      this.label = document.createElement('span');
      this.label.className = 'bc-hotbath-mobile-total__label';
      this.amount = document.createElement('strong');
      this.amount.className = 'bc-hotbath-mobile-total__amount';
      this.amount.dataset.mobileTotalValue = '';
      this.caption = document.createElement('p');
      this.caption.className = 'bc-hotbath-mobile-total__caption';
      this.totalLine.append(this.label, this.amount);
      this.summary.append(this.totalLine, this.caption);
      form.insertBefore(this.summary, anchor);
      const quantity = form.elements.namedItem('quantity');
      const quantityBlock = quantity?.closest('.bc-buybox__section--quantity');
      if (quantityBlock && this.root.contains(quantityBlock) && !form.contains(quantityBlock)) {
        this.quantityBlock = quantityBlock;
        this.quantityPlaceholder = document.createComment('');
        quantityBlock.before(this.quantityPlaceholder);
        form.insertBefore(quantityBlock, this.summary);
      }
      this.root.classList.add('bc-hotbath-mobile-active');
      return true;
    }

    calculate() {
      const parentPrice = readInteger(this.root.dataset.productPrice);
      const currency = this.root.dataset.currency || '';
      const variant = this.form.elements.namedItem('id')?.value;
      const quantityInput = this.form.elements.namedItem('quantity');
      const quantity = quantityInput ? readInteger(quantityInput.value) : 1;
      if (parentPrice === null || !/^[A-Z]{3}$/.test(currency) ||
          variant !== this.root.dataset.productVariant || quantity === null || quantity < 1 ||
          (quantityInput && !quantityInput.checkValidity()) ||
          this.form.elements.namedItem('selling_plan')?.value) return { state: 'invalid' };
      const addon = this.form.querySelector('bc-inbouw-addon');
      let bodyTotal = 0;
      if (addon) {
        if (addon.dataset.valid !== 'true' || addon.dataset.parentVariant !== variant ||
            addon.dataset.currency !== currency || addon.uncertain === true ||
            (typeof addon.validIdentity === 'function' && !addon.validIdentity())) return { state: 'invalid' };
        const choice = addon.querySelector('[data-inbouw-choice]:checked');
        if (!choice || !['yes', 'no'].includes(choice.value)) return { state: 'pending' };
        if (choice.disabled && !addon.busy) return { state: 'invalid' };
        if (choice.value === 'yes') {
          const bodyPrice = readInteger(addon.dataset.bodyPrice);
          const multiplier = readInteger(addon.dataset.quantityPerTrim);
          if (bodyPrice === null || multiplier === null || multiplier < 1 ||
              addon.dataset.bodyAvailable !== 'true') return { state: 'invalid' };
          bodyTotal = bodyPrice * multiplier * quantity;
        }
      }
      const total = parentPrice * quantity + bodyTotal;
      if (!Number.isSafeInteger(total) || !Number.isSafeInteger(bodyTotal)) return { state: 'invalid' };
      try {
        const formatted = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', {
          style: 'currency', currency
        }).format(total / 100);
        return { state: 'ready', formatted, total };
      } catch (_) {
        return { state: 'invalid' };
      }
    }

    updateTotal() {
      const result = this.calculate();
      if (this.root.dataset.mobileTotalState !== result.state) this.root.dataset.mobileTotalState = result.state;
      setHidden(this.summary, result.state === 'invalid');
      setHidden(this.totalLine, result.state !== 'ready');
      setHidden(this.amount, result.state !== 'ready');
      if (result.state === 'ready') {
        setText(this.label, this.root.dataset.mobileTotalLabel || '');
        setText(this.amount, result.formatted);
        setText(this.caption, this.root.dataset.mobileVatLabel || '');
        if (this.amount.dataset.totalCents !== String(result.total)) this.amount.dataset.totalCents = String(result.total);
      } else {
        setText(this.amount, '');
        if (this.amount.dataset.totalCents !== undefined) delete this.amount.dataset.totalCents;
        setText(this.caption, result.state === 'pending' ? this.root.dataset.mobileChooseInbouwLabel || '' : '');
        if (!this.caption.textContent) setHidden(this.summary, true);
      }
    }

    deactivate() {
      if (this.quantityPlaceholder?.parentNode && this.quantityBlock) {
        this.quantityPlaceholder.replaceWith(this.quantityBlock);
      }
      this.summary?.remove();
      this.quantityPlaceholder?.remove();
      this.form = null;
      this.summary = null;
      this.quantityBlock = null;
      this.quantityPlaceholder = null;
      this.root.classList.remove('bc-hotbath-mobile-active');
      delete this.root.dataset.mobileTotalState;
    }

    destroy() {
      this.controller.abort();
      this.observer.disconnect();
      cancelAnimationFrame(this.frame);
      this.deactivate();
    }
  }

  const mount = scope => {
    for (const [root, instance] of instances) {
      if (!root.isConnected) {
        instance.destroy();
        instances.delete(root);
      }
    }
    const roots = Array.from(scope.querySelectorAll(selector));
    if (scope.matches?.(selector)) roots.unshift(scope);
    roots.forEach(root => {
      if (!instances.has(root)) instances.set(root, new MobilePurchase(root));
      else instances.get(root).schedule();
    });
  };
  window.bcHotbathMobilePurchase = { mount };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => mount(document), { once: true });
  else mount(document);
  document.addEventListener('shopify:section:load', event => mount(event.target));
  document.addEventListener('shopify:section:unload', event => {
    for (const [root, instance] of instances) {
      if (root === event.target || event.target.contains(root)) {
        instance.destroy();
        instances.delete(root);
      }
    }
  });
})();
