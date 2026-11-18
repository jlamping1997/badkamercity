(() => {
  if (customElements.get('bc-brand-slider')) return;

  const pixelsPerSecond = 22;
  const wrap = (value, width) => ((value % width) + width) % width;

  class BrandSlider extends HTMLElement {
    connectedCallback() {
      this.track = this.querySelector('[data-brand-track]');
      this.viewport = this.querySelector('[data-brand-viewport]');
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
      this.animation = null;
      this.loopWidth = 0;
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
      window.addEventListener('pointercancel', event => this.endDrag(event), { ...options, passive: true });
      this.track.addEventListener('lostpointercapture', event => this.endDrag(event), options);
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
        if (this.focused && this.loopWidth && this.track.contains(event.target)) {
          this.keyboardManual = true;
          this.clearLoop();
          if (event.target !== this.track) event.target.scrollIntoView({ block: 'nearest', inline: 'nearest' });
          this.update();
        }
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
        this.resizeObserver.observe(this.viewport || this.track);
      }
      this.intersectionObserver?.disconnect();
      if (this.autoRequested && 'IntersectionObserver' in window) {
        this.inView = false;
        this.intersectionObserver = new IntersectionObserver(entries => {
          this.inView = entries.some(entry => entry.isIntersecting);
          this.syncMotion();
        }, { threshold: 0.01 });
        this.intersectionObserver.observe(this.viewport || this.track);
      }
      this.configure();
    }

    configure() {
      const fraction = this.loopWidth ? this.position() / this.loopWidth : null;
      const scrollPosition = Math.abs(this.track.scrollLeft);
      this.clearLoop();
      this.layoutWidth = (this.viewport || this.track).clientWidth;
      this.motionPreference = this.reduced.matches;
      if (this.autoRequested && this.viewport && this.track.animate && !this.motionPreference &&
          !this.keyboardManual && this.originals.length > 1 && this.layoutWidth > 0) {
        this.createLoop(fraction, scrollPosition);
      }
      this.update();
      this.syncMotion();
    }

    createLoop(fraction, scrollPosition) {
      const style = getComputedStyle(this.track);
      const gap = parseFloat(style.columnGap) || 0;
      const width = this.originals.reduce((total, item) => total + item.getBoundingClientRect().width + gap, 0);
      if (width <= 0) return;
      this.direction = style.direction === 'rtl' ? -1 : 1;
      this.setAttribute('data-brand-looping', '');
      const fragment = document.createDocumentFragment();
      const copies = Math.ceil(this.layoutWidth / width) + 1;
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
      const firstClone = fragment.firstElementChild;
      this.track.appendChild(fragment);
      const first = this.originals[0];
      this.loopWidth = Math.abs(firstClone.getBoundingClientRect().left - first.getBoundingClientRect().left);
      if (!this.loopWidth) {
        this.clearLoop();
        return;
      }
      this.track.scrollLeft = 0;
      this.duration = this.loopWidth / pixelsPerSecond * 1000;
      this.animation = this.track.animate([
        { transform: `translate3d(${-this.direction * this.loopWidth}px, 0, 0)` },
        { transform: 'translate3d(0, 0, 0)' }
      ], { duration: this.duration, iterations: Infinity, easing: 'linear' });
      this.animation.pause();
      this.seek(fraction === null ? scrollPosition : fraction * this.loopWidth);
    }

    position() {
      const elapsed = wrap(this.animation?.currentTime || 0, this.duration);
      return wrap(this.loopWidth * (1 - elapsed / this.duration), this.loopWidth);
    }

    seek(position) {
      const elapsed = wrap(-position / this.loopWidth, 1) * this.duration;
      this.animation.currentTime = elapsed;
    }

    shift(pixels) {
      if (this.animation) this.seek(this.position() - this.direction * pixels);
    }

    startDrag(event) {
      if (!this.loopWidth || this.drag || event.isPrimary === false || (event.pointerType === 'mouse' && event.button !== 0)) return;
      this.suppressClick = false;
      this.focused = false;
      this.drag = { id: event.pointerId, x: event.clientX, y: event.clientY, lastX: event.clientX, active: false, type: event.pointerType };
      this.syncMotion();
    }

    dragMove(event) {
      const drag = this.drag;
      if (!drag || event.pointerId !== drag.id) return;
      if (!drag.active) {
        const x = event.clientX - drag.x, y = event.clientY - drag.y;
        if (Math.max(Math.abs(x), Math.abs(y)) < 6) return;
        if (drag.type !== 'mouse' && Math.abs(y) > Math.abs(x)) {
          this.endDrag(event);
          return;
        }
        drag.active = true;
        this.suppressClick = true;
        this.track.setPointerCapture?.(event.pointerId);
        this.setAttribute('data-brand-dragging', '');
      }
      const pixels = event.clientX - drag.lastX;
      drag.lastX = event.clientX;
      this.shift(pixels);
    }

    endDrag(event) {
      const drag = this.drag;
      if (!drag || event.pointerId !== drag.id) return;
      this.drag = null;
      this.removeAttribute('data-brand-dragging');
      if (this.track.hasPointerCapture?.(event.pointerId)) this.track.releasePointerCapture(event.pointerId);
      this.syncMotion();
    }

    syncMotion() {
      if (!this.animation) return;
      const playing = !this.drag && !this.focused && this.inView && !document.hidden;
      this.toggleAttribute('data-brand-moving', playing);
      if (playing && this.animation.playState !== 'running') this.animation.play();
      else if (!playing && this.animation.playState !== 'paused') this.animation.pause();
    }

    clearLoop() {
      if (!this.hasAttribute('data-brand-looping')) return;
      const position = this.animation ? this.position() : 0;
      this.animation?.cancel();
      this.animation = null;
      const pointerId = this.drag?.id;
      this.drag = null;
      if (pointerId != null && this.track.hasPointerCapture?.(pointerId)) this.track.releasePointerCapture(pointerId);
      this.removeAttribute('data-brand-dragging');
      this.removeAttribute('data-brand-moving');
      this.track.querySelectorAll('[data-brand-clone]').forEach(node => node.remove());
      this.loopWidth = 0;
      this.removeAttribute('data-brand-looping');
      this.track.scrollLeft = this.direction * Math.min(position, Math.max(0, this.track.scrollWidth - this.track.clientWidth));
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
        this.shift(-direction * rtl * step);
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
      if (this.layoutFrame) return;
      this.layoutFrame = requestAnimationFrame(() => {
        this.layoutFrame = null;
        if ((this.viewport || this.track).clientWidth !== this.layoutWidth ||
            this.reduced.matches !== this.motionPreference) this.configure();
      });
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
