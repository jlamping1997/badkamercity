(() => {
  if (customElements.get('bc-brand-slider')) return;

  class BrandSlider extends HTMLElement {
    connectedCallback() {
      this.track = this.querySelector('[data-brand-track]');
      this.controls = this.querySelector('[data-brand-controls]');
      this.previous = this.querySelector('[data-brand-previous]');
      this.next = this.querySelector('[data-brand-next]');
      if (!this.track) return;

      this.events?.abort();
      this.events = new AbortController();
      const options = { signal: this.events.signal };
      this.originals = [...this.track.children].filter(item => !item.hasAttribute('data-brand-clone'));
      this.reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
      this.autoRequested = this.hasAttribute('data-brand-autoplay');
      this.focused = false;
      this.keyboardManual = false;
      this.inView = true;
      this.animationFrame = null;
      this.loopWidth = 0;
      this.boost = 0;
      this.drag = null;
      this.suppressClick = false;

      this.previous?.addEventListener('click', () => this.move(-1), options);
      this.next?.addEventListener('click', () => this.move(1), options);
      this.track.addEventListener('scroll', () => {
        if (!this.loopWidth) this.scheduleUpdate();
      }, { ...options, passive: true });
      this.track.addEventListener('pointerdown', event => this.startDrag(event), { ...options, passive: true });
      this.track.addEventListener('pointermove', event => this.dragMove(event), { ...options, passive: true });
      window.addEventListener('pointerup', event => this.endDrag(event), { ...options, passive: true });
      window.addEventListener('pointercancel', event => this.endDrag(event, true), { ...options, passive: true });
      this.track.addEventListener('lostpointercapture', event => this.endDrag(event, true), options);
      this.track.addEventListener('dragstart', event => {
        if (this.loopWidth) event.preventDefault();
      }, options);
      this.track.addEventListener('mousedown', event => {
        if (event.target.closest('[data-brand-clone]')) event.preventDefault();
      }, options);
      this.track.addEventListener('click', event => {
        if (this.suppressClick && event.detail !== 0) {
          this.suppressClick = false;
          event.preventDefault();
          event.stopPropagation();
        }
      }, { ...options, capture: true });
      this.track.addEventListener('keydown', event => {
        if (event.target !== this.track || !['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
        event.preventDefault();
        if (this.loopWidth) {
          this.keyboardManual = true;
          this.clearLoop();
          this.update();
        }
        const rtl = getComputedStyle(this.track).direction === 'rtl';
        if (event.key === 'Home' || event.key === 'End') {
          this.track.scrollTo({ left: event.key === 'Home' ? 0 : (rtl ? -1 : 1) * this.track.scrollWidth, behavior: this.behavior() });
        } else this.move((event.key === 'ArrowRight' ? 1 : -1) * (rtl ? -1 : 1));
      }, options);
      this.addEventListener('focusin', event => {
        this.focused = event.target.matches(':focus-visible');
        this.syncMotion();
      }, options);
      this.addEventListener('focusout', event => {
        if (event.relatedTarget && this.contains(event.relatedTarget)) return;
        this.focused = false;
        if (this.keyboardManual) {
          this.keyboardManual = false;
          this.configure();
        } else this.syncMotion();
      }, options);
      document.addEventListener('visibilitychange', () => this.syncMotion(), options);
      const resize = () => this.scheduleLayout();
      window.addEventListener('resize', resize, options);
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
      return this.autoRequested && !this.reduced.matches && this.originals.length > 1;
    }

    configure() {
      const position = this.loopWidth ? Math.abs(this.track.scrollLeft) % this.loopWidth : Math.abs(this.track.scrollLeft);
      this.clearLoop();
      if (this.eligible() && !this.keyboardManual) {
        const gap = parseFloat(getComputedStyle(this.track).columnGap) || 0;
        const width = this.originals.reduce((total, item) => total + item.getBoundingClientRect().width + gap, 0);
        if (width > 0 && this.track.clientWidth > 0) {
          this.loopWidth = width;
          this.setAttribute('data-brand-looping', '');
          const fragment = document.createDocumentFragment();
          const copies = Math.ceil(this.track.clientWidth / width) + 1;
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
          this.cyclePosition = position % width;
          this.shift(0);
        }
      }
      this.update();
      this.syncMotion();
    }

    shift(pixels) {
      if (!this.loopWidth) return;
      const direction = getComputedStyle(this.track).direction === 'rtl' ? -1 : 1;
      this.cyclePosition = ((this.cyclePosition - direction * pixels) % this.loopWidth + this.loopWidth) % this.loopWidth;
      this.track.scrollLeft = direction * this.cyclePosition;
    }

    startDrag(event) {
      if (!this.loopWidth || this.drag || event.isPrimary === false || (event.pointerType === 'mouse' && event.button !== 0)) return;
      this.suppressClick = false;
      this.focused = false;
      this.boost = 0;
      this.drag = { id: event.pointerId, x: event.clientX, y: event.clientY, lastX: event.clientX, time: event.timeStamp, velocity: 0, active: false, type: event.pointerType };
      this.syncMotion();
    }

    dragMove(event) {
      const drag = this.drag;
      if (!drag || event.pointerId !== drag.id) return;
      if (!drag.active) {
        const x = event.clientX - drag.x, y = event.clientY - drag.y;
        if (Math.max(Math.abs(x), Math.abs(y)) < 6) return;
        if (drag.type !== 'mouse' && Math.abs(y) > Math.abs(x)) {
          this.drag = null;
          return;
        }
        drag.active = true;
        this.suppressClick = true;
        this.track.setPointerCapture?.(event.pointerId);
        this.setAttribute('data-brand-dragging', '');
      }
      const pixels = event.clientX - drag.lastX;
      const seconds = Math.max(8, event.timeStamp - drag.time) / 1000;
      drag.velocity = Math.max(-1600, Math.min(1600, pixels / seconds));
      drag.lastX = event.clientX;
      drag.time = event.timeStamp;
      this.shift(pixels);
    }

    endDrag(event, cancelled = false) {
      const drag = this.drag;
      if (!drag || event.pointerId !== drag.id) return;
      this.drag = null;
      this.removeAttribute('data-brand-dragging');
      if (this.track.hasPointerCapture?.(event.pointerId)) this.track.releasePointerCapture(event.pointerId);
      this.boost = !cancelled && drag.active && event.timeStamp - drag.time < 120 ? drag.velocity : 0;
      this.syncMotion();
    }

    canRun() {
      return this.loopWidth > 0 && !this.focused && this.inView && !document.hidden;
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
        const decay = Math.exp(-5 * seconds);
        this.shift(22 * seconds + this.boost * (1 - decay) / 5);
        this.boost *= decay;
        if (Math.abs(this.boost) < 0.1) this.boost = 0;
      }
      this.lastTime = time;
      this.animationFrame = requestAnimationFrame(next => this.animate(next));
    }

    stopMotion() {
      if (this.animationFrame != null) cancelAnimationFrame(this.animationFrame);
      this.animationFrame = null;
      this.lastTime = null;
      this.boost = 0;
      this.removeAttribute('data-brand-moving');
    }

    clearLoop() {
      this.stopMotion();
      this.drag = null;
      this.removeAttribute('data-brand-dragging');
      if (!this.loopWidth) return;
      const position = Math.abs(this.track.scrollLeft) % this.loopWidth;
      const direction = getComputedStyle(this.track).direction === 'rtl' ? -1 : 1;
      this.track.querySelectorAll('[data-brand-clone]').forEach(node => node.remove());
      this.loopWidth = 0;
      this.removeAttribute('data-brand-looping');
      this.track.scrollLeft = direction * Math.min(position, Math.max(0, this.track.scrollWidth - this.track.clientWidth));
    }

    behavior() {
      return this.reduced.matches ? 'auto' : 'smooth';
    }

    move(direction) {
      const first = this.track.firstElementChild;
      if (!first) return;
      const gap = parseFloat(getComputedStyle(this.track).columnGap) || 0;
      const step = first.getBoundingClientRect().width + gap;
      const rtl = getComputedStyle(this.track).direction === 'rtl' ? -1 : 1;
      if (this.loopWidth) {
        if (this.focused) this.shift(-direction * rtl * step);
        else this.boost = -direction * rtl * step * 5;
        this.syncMotion();
        return;
      }
      const visible = Math.max(1, Math.floor((this.track.clientWidth + gap) / Math.max(step, 1)));
      this.track.scrollBy({ left: direction * rtl * visible * step, behavior: this.behavior() });
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
      if (this.controls) this.controls.hidden = !this.loopWidth && maximum <= 2;
      if (this.previous) this.previous.disabled = !this.loopWidth && position <= 2;
      if (this.next) this.next.disabled = !this.loopWidth && position >= maximum - 2;
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
