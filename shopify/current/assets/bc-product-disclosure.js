if (!customElements.get('bc-product-disclosure')) {
  customElements.define('bc-product-disclosure', class extends HTMLElement {
    connectedCallback() {
      this.viewport = this.querySelector('[data-disclosure-viewport]');
      this.content = this.querySelector('[data-disclosure-content]');
      this.button = this.querySelector('[data-disclosure-toggle]');
      if (!this.viewport || !this.content || !this.button || this.abort) return;

      this.abort = new AbortController();
      this.phone = matchMedia('(max-width: 749px)');
      this.reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
      this.specs = this.dataset.disclosureMode === 'specs';
      this.expanded = false;
      this.savedTabIndexes = new Map();
      const options = { signal: this.abort.signal };
      this.button.addEventListener('click', () => this.toggle(), options);
      this.phone.addEventListener('change', () => {
        this.expanded = false;
        this.measure();
      }, options);
      window.addEventListener('pageshow', event => {
        if (!event.persisted) return;
        this.expanded = false;
        this.measure();
      }, options);
      this.content.addEventListener('load', () => this.scheduleMeasure(), { ...options, capture: true });
      this.observer = new ResizeObserver(() => this.scheduleMeasure());
      this.observer.observe(this.content);
      this.measure();
      document.fonts.ready.then(() => {
        if (this.isConnected) this.scheduleMeasure();
      });
    }

    disconnectedCallback() {
      this.abort?.abort();
      this.abort = null;
      this.observer?.disconnect();
      cancelAnimationFrame(this.frame);
      this.animation?.cancel();
      this.restoreFocus();
    }

    scheduleMeasure() {
      cancelAnimationFrame(this.frame);
      this.frame = requestAnimationFrame(() => this.measure());
    }

    measure() {
      this.animation?.cancel();
      this.animation = null;
      const contentRect = this.content.getBoundingClientRect();
      this.fullHeight = Math.ceil(contentRect.height);
      this.active = !this.specs || this.phone.matches;

      if (this.specs) {
        const rows = this.content.querySelectorAll('.bc-product-specs__row, .bc-test-specs__row');
        this.collapsedHeight = rows.length > 10
          ? Math.ceil(rows[9].getBoundingClientRect().bottom - contentRect.top)
          : this.fullHeight;
      } else {
        const lineHeight = parseFloat(getComputedStyle(this.viewport).lineHeight) || 28;
        this.collapsedHeight = Math.ceil(lineHeight * 4);
      }

      this.hasMore = this.fullHeight > this.collapsedHeight + 4;
      this.viewport.style.setProperty('--bc-disclosure-collapsed', `${this.collapsedHeight}px`);
      this.button.hidden = !this.active || !this.hasMore;
      this.classList.toggle('is-short', !this.hasMore);
      this.syncState();
      this.viewport.style.height = this.isOpen() ? 'auto' : `${this.collapsedHeight}px`;
      this.syncFocus();
      this.dataset.disclosureReady = 'true';
    }

    isOpen() {
      return !this.active || !this.hasMore || this.expanded;
    }

    syncState() {
      this.classList.toggle('is-expanded', this.expanded && this.active && this.hasMore);
      this.button.setAttribute('aria-expanded', String(this.expanded && this.active && this.hasMore));
    }

    toggle() {
      if (!this.active || !this.hasMore) return;
      const startHeight = this.viewport.getBoundingClientRect().height;
      this.animation?.cancel();
      this.animation = null;
      this.expanded = !this.expanded;
      this.syncState();
      this.syncFocus();

      if (!this.expanded && this.getBoundingClientRect().top < 96) {
        this.scrollIntoView({ block: 'start', behavior: this.reduceMotion.matches ? 'instant' : 'smooth' });
      }

      const targetHeight = this.expanded ? Math.ceil(this.content.getBoundingClientRect().height) : this.collapsedHeight;
      this.viewport.style.height = `${targetHeight}px`;
      if (this.reduceMotion.matches || typeof this.viewport.animate !== 'function') {
        if (this.expanded) this.viewport.style.height = 'auto';
        return;
      }

      const animation = this.viewport.animate(
        [{ height: `${startHeight}px` }, { height: `${targetHeight}px` }],
        { duration: 320, easing: 'cubic-bezier(0.22, 1, 0.36, 1)' }
      );
      this.animation = animation;
      animation.finished.then(() => {
        if (this.animation !== animation) return;
        this.animation = null;
        this.viewport.style.height = this.isOpen() ? 'auto' : `${this.collapsedHeight}px`;
        this.syncFocus();
      }).catch(() => {});
    }

    restoreFocus() {
      this.savedTabIndexes?.forEach((value, element) => {
        if (value === null) element.removeAttribute('tabindex');
        else element.setAttribute('tabindex', value);
      });
      this.savedTabIndexes?.clear();
    }

    syncFocus() {
      this.restoreFocus();
      if (this.isOpen()) return;
      const bottom = this.viewport.getBoundingClientRect().top + this.collapsedHeight;
      this.content.querySelectorAll('a[href], button, input, select, textarea, [tabindex]').forEach(element => {
        if (element.getBoundingClientRect().bottom <= bottom) return;
        this.savedTabIndexes.set(element, element.getAttribute('tabindex'));
        element.setAttribute('tabindex', '-1');
      });
    }
  });
}
