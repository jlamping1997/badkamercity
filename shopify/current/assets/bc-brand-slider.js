(() => {
  if (customElements.get('bc-brand-slider')) return;

  class BrandSlider extends HTMLElement {
    connectedCallback() {
      this.track = this.querySelector('[data-brand-track]');
      this.controls = this.querySelector('[data-brand-controls]');
      this.previous = this.querySelector('[data-brand-previous]');
      this.next = this.querySelector('[data-brand-next]');
      this.toggle = this.querySelector('[data-brand-toggle]');
      if (!this.track || !this.controls || !this.previous || !this.next) return;

      this.events?.abort();
      this.events = new AbortController();
      const options = { signal: this.events.signal };
      this.originals = [...this.track.children].filter(item => !item.hasAttribute('data-brand-clone'));
      this.desktop = window.matchMedia('(min-width: 990px)');
      this.reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
      this.autoRequested = this.hasAttribute('data-brand-autoplay') && !!this.toggle;
      this.userPaused ??= false;
      this.manualMode = false;
      this.hovered = false;
      this.focused = this.contains(document.activeElement);
      this.inView = true;
      this.animationFrame = null;
      this.loopWidth = 0;

      this.previous.addEventListener('click', () => this.move(-1), options);
      this.next.addEventListener('click', () => this.move(1), options);
      this.toggle?.addEventListener('click', () => {
        this.userPaused = !this.userPaused;
        if (!this.userPaused) {
          this.manualMode = false;
          this.focused = false;
          this.configure();
        } else {
          this.syncMotion();
          this.update();
        }
      }, options);

      this.track.addEventListener('scroll', () => {
        if (!this.loopWidth) this.scheduleUpdate();
      }, { ...options, passive: true });
      this.track.addEventListener('pointerdown', event => {
        if (event.pointerType === 'touch' || event.pointerType === 'pen') this.enterManual();
      }, { ...options, passive: true });
      this.track.addEventListener('mousedown', event => {
        if (event.target.closest('[data-brand-clone]')) event.preventDefault();
      }, options);
      this.track.addEventListener('keydown', event => {
        if (event.target !== this.track) return;
        if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
        event.preventDefault();
        this.enterManual();
        const rtl = getComputedStyle(this.track).direction === 'rtl';
        if (event.key === 'Home' || event.key === 'End') {
          this.track.scrollTo({ left: event.key === 'Home' ? 0 : (rtl ? -1 : 1) * this.track.scrollWidth, behavior: this.behavior() });
        } else {
          this.move((event.key === 'ArrowRight' ? 1 : -1) * (rtl ? -1 : 1));
        }
      }, options);

      this.addEventListener('mouseenter', () => { this.hovered = true; this.syncMotion(); }, options);
      this.addEventListener('mouseleave', () => { this.hovered = false; this.syncMotion(); }, options);
      this.addEventListener('focusin', () => { this.focused = true; this.syncMotion(); }, options);
      this.addEventListener('focusout', event => {
        this.focused = !!event.relatedTarget && this.contains(event.relatedTarget);
        this.syncMotion();
      }, options);
      document.addEventListener('visibilitychange', () => this.syncMotion(), options);
      const resize = () => this.scheduleLayout();
      window.addEventListener('resize', resize, options);
      this.desktop.addEventListener?.('change', resize, options);
      this.reduced.addEventListener?.('change', resize, options);
      this.resizeObserver?.disconnect();
      if ('ResizeObserver' in window) {
        this.resizeObserver = new ResizeObserver(resize);
        this.resizeObserver.observe(this.track);
      }
      this.intersectionObserver?.disconnect();
      if (this.autoRequested && 'IntersectionObserver' in window) {
        this.inView = false;
        this.intersectionObserver = new IntersectionObserver(entries => {
          this.inView = entries.some(entry => entry.isIntersecting);
          this.syncMotion();
        }, { threshold: 0.01 });
        this.intersectionObserver.observe(this);
      }
      this.configure();
    }

    eligible() {
      return this.autoRequested && this.desktop.matches && !this.reduced.matches && this.originals.length > 1;
    }

    configure() {
      this.clearLoop();
      if (this.eligible() && !this.manualMode) {
        const gap = parseFloat(getComputedStyle(this.track).columnGap) || 0;
        const width = this.originals.reduce((total, item) => total + item.getBoundingClientRect().width + gap, 0);
        if (width > 0 && this.track.clientWidth > 0) {
          this.loopWidth = width;
          this.setAttribute('data-brand-looping', '');
          const copies = Math.ceil(this.track.clientWidth / width) + 1;
          const fragment = document.createDocumentFragment();
          for (let copy = 0; copy < copies; copy++) {
            for (const item of this.originals) {
              const clone = item.cloneNode(true);
              clone.setAttribute('data-brand-clone', '');
              clone.setAttribute('aria-hidden', 'true');
              clone.removeAttribute('id');
              clone.querySelectorAll('[id]').forEach(node => node.removeAttribute('id'));
              clone.querySelectorAll('a, button, input, select, textarea, [tabindex]').forEach(node => { node.tabIndex = -1; });
              fragment.appendChild(clone);
            }
          }
          this.track.appendChild(fragment);
          this.cyclePosition = Math.abs(this.track.scrollLeft) % width;
        }
      }
      this.update();
      this.syncMotion();
    }

    canRun() {
      return this.loopWidth > 0 && !this.userPaused && !this.hovered && !this.focused && this.inView && !document.hidden;
    }

    syncMotion() {
      if (this.canRun()) {
        if (this.animationFrame == null) {
          this.cyclePosition = Math.abs(this.track.scrollLeft) % this.loopWidth;
          this.lastTime = null;
          this.setAttribute('data-brand-moving', '');
          this.animationFrame = requestAnimationFrame(time => this.animate(time));
        }
      } else this.stopMotion();
    }

    animate(time) {
      this.animationFrame = null;
      if (!this.canRun()) { this.stopMotion(); return; }
      if (this.lastTime != null) {
        const seconds = Math.min(0.1, Math.max(0, (time - this.lastTime) / 1000));
        const direction = getComputedStyle(this.track).direction === 'rtl' ? -1 : 1;
        this.cyclePosition = ((this.cyclePosition - direction * 18 * seconds) % this.loopWidth + this.loopWidth) % this.loopWidth;
        this.track.scrollLeft = direction * this.cyclePosition;
      }
      this.lastTime = time;
      this.animationFrame = requestAnimationFrame(next => this.animate(next));
    }

    stopMotion() {
      if (this.animationFrame != null) cancelAnimationFrame(this.animationFrame);
      this.animationFrame = null;
      this.lastTime = null;
      this.removeAttribute('data-brand-moving');
    }

    clearLoop() {
      this.stopMotion();
      if (!this.loopWidth) return;
      const position = Math.abs(this.track.scrollLeft) % this.loopWidth;
      const direction = getComputedStyle(this.track).direction === 'rtl' ? -1 : 1;
      this.track.querySelectorAll('[data-brand-clone]').forEach(node => node.remove());
      this.loopWidth = 0;
      this.removeAttribute('data-brand-looping');
      this.track.scrollLeft = direction * Math.min(position, Math.max(0, this.track.scrollWidth - this.track.clientWidth));
    }

    enterManual() {
      if (this.autoRequested) {
        this.userPaused = true;
        this.manualMode = true;
        this.clearLoop();
        this.update();
      }
    }

    behavior() {
      return this.reduced.matches ? 'auto' : 'smooth';
    }

    move(direction) {
      this.enterManual();
      const first = this.track.firstElementChild;
      if (!first) return;
      const gap = parseFloat(getComputedStyle(this.track).columnGap) || 0;
      const step = first.getBoundingClientRect().width + gap;
      const visible = Math.max(1, Math.floor((this.track.clientWidth + gap) / Math.max(step, 1)));
      const rtl = getComputedStyle(this.track).direction === 'rtl';
      this.track.scrollBy({ left: direction * (rtl ? -1 : 1) * visible * step, behavior: this.behavior() });
    }

    scheduleUpdate() {
      if (this.updateFrame) return;
      this.updateFrame = requestAnimationFrame(() => { this.updateFrame = null; this.update(); });
    }

    scheduleLayout() {
      this.stopMotion();
      if (this.layoutFrame) return;
      this.layoutFrame = requestAnimationFrame(() => { this.layoutFrame = null; this.configure(); });
    }

    update() {
      const maximum = Math.max(0, this.track.scrollWidth - this.track.clientWidth);
      const position = Math.min(maximum, Math.max(0, Math.abs(this.track.scrollLeft)));
      this.controls.hidden = !this.loopWidth && maximum <= 2;
      this.previous.disabled = !this.loopWidth && position <= 2;
      this.next.disabled = !this.loopWidth && position >= maximum - 2;
      if (this.toggle) {
        this.toggle.hidden = !this.eligible();
        this.toggle.setAttribute('aria-label', this.userPaused ? this.toggle.dataset.labelPlay : this.toggle.dataset.labelPause);
        const icon = this.toggle.querySelector('span');
        if (icon) icon.textContent = this.userPaused ? '▶' : 'Ⅱ';
      }
    }

    disconnectedCallback() {
      this.events?.abort();
      this.resizeObserver?.disconnect();
      this.intersectionObserver?.disconnect();
      this.clearLoop();
      if (this.updateFrame) cancelAnimationFrame(this.updateFrame);
      if (this.layoutFrame) cancelAnimationFrame(this.layoutFrame);
      this.updateFrame = null;
      this.layoutFrame = null;
    }
  }

  customElements.define('bc-brand-slider', BrandSlider);
})();
