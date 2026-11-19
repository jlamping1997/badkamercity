(() => {
  if (customElements.get('bc-brand-slider')) return;

  class BrandSlider extends HTMLElement {
    connectedCallback() {
      this.track = this.querySelector('[data-brand-track]');
      this.controls = this.querySelector('[data-brand-controls]');
      this.previous = this.querySelector('[data-brand-previous]');
      this.next = this.querySelector('[data-brand-next]');
      if (!this.track || !this.controls || !this.previous || !this.next) return;

      this.events?.abort();
      this.events = new AbortController();
      const options = { signal: this.events.signal };
      this.previous.addEventListener('click', () => this.move(-1), options);
      this.next.addEventListener('click', () => this.move(1), options);
      this.track.addEventListener('scroll', () => this.scheduleUpdate(), { ...options, passive: true });
      this.track.addEventListener('keydown', (event) => {
        if (event.target !== this.track) return;
        const keys = ['ArrowLeft', 'ArrowRight', 'Home', 'End'];
        if (!keys.includes(event.key)) return;
        event.preventDefault();
        const rtl = getComputedStyle(this.track).direction === 'rtl';
        if (event.key === 'Home' || event.key === 'End') {
          this.track.scrollTo({ left: event.key === 'Home' ? 0 : (rtl ? -1 : 1) * this.track.scrollWidth, behavior: this.behavior() });
        } else {
          this.move((event.key === 'ArrowRight' ? 1 : -1) * (rtl ? -1 : 1));
        }
      }, options);
      window.addEventListener('resize', () => this.scheduleUpdate(), options);
      this.resizeObserver?.disconnect();
      if ('ResizeObserver' in window) {
        this.resizeObserver = new ResizeObserver(() => this.scheduleUpdate());
        this.resizeObserver.observe(this.track);
      }
      this.update();
    }

    behavior() {
      return window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
    }

    move(direction) {
      const first = this.track.firstElementChild;
      if (!first) return;
      const gap = parseFloat(getComputedStyle(this.track).columnGap) || 0;
      const step = first.getBoundingClientRect().width + gap;
      const visible = Math.max(1, Math.floor((this.track.clientWidth + gap) / Math.max(step, 1)));
      const rtl = getComputedStyle(this.track).direction === 'rtl';
      this.track.scrollBy({ left: direction * (rtl ? -1 : 1) * visible * step, behavior: this.behavior() });
    }

    scheduleUpdate() {
      if (this.frame) return;
      this.frame = requestAnimationFrame(() => {
        this.frame = null;
        this.update();
      });
    }

    update() {
      const maximum = Math.max(0, this.track.scrollWidth - this.track.clientWidth);
      const position = Math.min(maximum, Math.max(0, Math.abs(this.track.scrollLeft)));
      this.controls.hidden = maximum <= 2;
      this.previous.disabled = position <= 2;
      this.next.disabled = position >= maximum - 2;
    }

    disconnectedCallback() {
      this.events?.abort();
      this.resizeObserver?.disconnect();
      if (this.frame) cancelAnimationFrame(this.frame);
      this.frame = null;
    }
  }

  customElements.define('bc-brand-slider', BrandSlider);
})();
