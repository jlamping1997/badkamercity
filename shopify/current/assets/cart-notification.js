class CartNotification extends HTMLElement {
  constructor() {
    super();
    this.notification = this.querySelector('#cart-notification');
    this.cartButtonLabel = this.querySelector('#cart-notification-button')?.textContent.trim() || '';
    this.querySelectorAll('[data-cart-close]').forEach((button) => {
      button.addEventListener('click', () => this.close());
    });
    this.notification.addEventListener('cancel', (event) => {
      event.preventDefault();
      this.close();
    });
    this.notification.addEventListener('pointerdown', (event) => {
      this.pointerStartedOutside = this.isOutside(event);
    });
    this.notification.addEventListener('click', (event) => {
      if (this.pointerStartedOutside && this.isOutside(event)) this.close();
      this.pointerStartedOutside = false;
    });
    this.notification.addEventListener('close', () => {
      if (this.notification.open) return;
      this.notification.classList.remove('active');
      document.documentElement.style.overflow = this.previousOverflow ?? '';
      document.documentElement.style.scrollbarGutter = this.previousScrollbarGutter ?? '';
      if (this.activeElement?.isConnected) this.activeElement.focus({ preventScroll: true });
    });
  }

  isOutside(event) {
    if (event.target !== this.notification) return false;
    const bounds = this.notification.getBoundingClientRect();
    return event.clientX < bounds.left || event.clientX > bounds.right ||
      event.clientY < bounds.top || event.clientY > bounds.bottom;
  }

  open() {
    this.closing = false;
    clearTimeout(this.closeTimer);
    cancelAnimationFrame(this.openFrame);
    if (!this.notification.open) {
      this.previousOverflow = document.documentElement.style.overflow;
      this.previousScrollbarGutter = document.documentElement.style.scrollbarGutter;
      this.notification.showModal();
      document.documentElement.style.scrollbarGutter = 'stable';
      document.documentElement.style.overflow = 'hidden';
      this.notification.getBoundingClientRect();
    }
    this.openFrame = requestAnimationFrame(() => this.notification.classList.add('active'));
  }

  close() {
    if (!this.notification.open || this.closing) return;
    this.closing = true;
    cancelAnimationFrame(this.openFrame);
    this.notification.classList.remove('active');
    const delay = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 230;
    this.closeTimer = setTimeout(() => {
      this.closing = false;
      this.notification.close();
    }, delay);
  }

  renderContents(parsedState) {
    this.closing = false;
    this.cartItemKey = parsedState.key || parsedState.items?.[0]?.key;
    this.getSectionsToRender().forEach((section) => {
      const target = document.getElementById(section.id);
      const html = parsedState.sections?.[section.id];
      if (!target) return;
      const content = typeof html === 'string' ? this.getSectionInnerHTML(html, section.selector) : null;
      if (content !== null) target.innerHTML = content;
      else if (section.id === 'cart-notification-product') target.replaceChildren();
      else if (section.id === 'cart-notification-button') target.textContent = this.cartButtonLabel;
      else if (section.id === 'cart-icon-bubble') {
        target.querySelectorAll('.cart-count-bubble').forEach(bubble => { bubble.hidden = true; bubble.style.display = 'none'; });
      }
    });
    this.open();
  }

  getSectionsToRender() {
    return [
      { id: 'cart-notification-product', selector: `[id="cart-notification-product-${this.cartItemKey}"]` },
      { id: 'cart-notification-button' },
      { id: 'cart-icon-bubble' },
    ];
  }

  getSectionInnerHTML(html, selector = '.shopify-section') {
    return new DOMParser().parseFromString(html, 'text/html').querySelector(selector)?.innerHTML ?? null;
  }

  setActiveElement(element) {
    this.activeElement = element;
  }
}

if (!customElements.get('cart-notification')) customElements.define('cart-notification', CartNotification);
