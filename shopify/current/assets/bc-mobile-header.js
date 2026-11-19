(() => {
  if (window.BCMobileHeader) return;

  class BCMobileHeader {
    constructor(section) {
      this.section = section;
      this.header = section.querySelector('.bc-header');
      this.search = section.querySelector('.bc-header__search');
      if (!this.header || !this.search) return;
      this.media = window.matchMedia('(max-width: 989px)');
      this.abort = new AbortController();
      this.frame = null;
      this.measureFrame = null;
      this.lastY = this.scrollY();
      this.direction = 0;
      this.distance = 0;
      this.compact = false;
      this.section.dataset.bcInput = 'pointer';
      const signal = this.abort.signal;

      this.onScroll = () => {
        if (this.frame !== null) return;
        this.frame = requestAnimationFrame(() => {
          this.frame = null;
          this.updateScroll();
        });
      };
      this.onMedia = () => this.updateMedia();
      this.onResize = () => this.queueMeasure();
      this.onPointer = () => { this.section.dataset.bcInput = 'pointer'; };
      this.onKey = event => {
        if (['Tab', 'Enter', ' ', 'Escape', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) {
          this.section.dataset.bcInput = 'keyboard';
        }
      };
      this.onFocus = event => {
        if (this.media.matches && this.search.contains(event.target)) this.setCompact(false);
      };
      this.onPageShow = () => {
        this.lastY = this.scrollY();
        this.direction = 0;
        this.distance = 0;
        if (this.lastY <= 24) this.setCompact(false);
        this.queueMeasure();
      };

      window.addEventListener('scroll', this.onScroll, { passive: true, signal });
      window.addEventListener('resize', this.onResize, { passive: true, signal });
      window.addEventListener('pageshow', this.onPageShow, { signal });
      document.addEventListener('pointerdown', this.onPointer, { capture: true, passive: true, signal });
      document.addEventListener('keydown', this.onKey, { capture: true, signal });
      this.section.addEventListener('focusin', this.onFocus, { signal });
      this.media.addEventListener('change', this.onMedia);
      if (typeof ResizeObserver !== 'undefined') {
        this.observer = new ResizeObserver(() => this.queueMeasure());
        this.observer.observe(this.header);
      }
      this.updateMedia();
      section.bcMobileHeader = this;
    }

    scrollY() {
      const maximum = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
      return Math.max(0, Math.min(maximum, window.scrollY || document.documentElement.scrollTop || 0));
    }

    updateMedia() {
      if (this.media.matches && !this.ownsHeight) {
        this.previousHeight = document.documentElement.style.getPropertyValue('--header-height');
        this.previousOffset = document.documentElement.style.getPropertyValue('--bc-mobile-drawer-offset');
        this.ownsHeight = true;
      }
      this.setCompact(false);
      this.lastY = this.scrollY();
      this.direction = 0;
      this.distance = 0;
      if (this.media.matches) this.queueMeasure();
      else this.restoreMetrics();
    }

    updateScroll() {
      const y = this.scrollY();
      const delta = y - this.lastY;
      this.lastY = y;
      if (!this.media.matches) return;
      if (this.section.querySelector('.bc-mobile-drawer.is-open') ||
          this.search.contains(document.activeElement) ||
          this.search.querySelector('predictive-search[open]') ||
          document.querySelector('dialog[open]')) {
        this.direction = 0;
        this.distance = 0;
        return;
      }
      if (y <= 24) {
        this.setCompact(false);
        this.direction = 0;
        this.distance = 0;
        return;
      }
      if (delta === 0) return;
      const direction = Math.sign(delta);
      if (direction !== this.direction) {
        this.direction = direction;
        this.distance = 0;
      }
      this.distance += Math.abs(delta);
      const expandedHeight = this.section.offsetHeight;
      if (direction > 0 && y > expandedHeight + 24 && this.distance >= 24) this.setCompact(true);
      else if (direction < 0 && this.distance >= 32) this.setCompact(false);
    }

    setCompact(compact) {
      compact = Boolean(compact && this.media.matches);
      if (compact && this.search.contains(document.activeElement)) return;
      this.compact = compact;
      this.section.dataset.bcScrollState = compact ? 'compact' : 'expanded';
      this.search.inert = compact;
      if (compact) this.search.setAttribute('aria-hidden', 'true');
      else this.search.removeAttribute('aria-hidden');
      this.queueMeasure();
    }

    queueMeasure() {
      if (this.measureFrame !== null) return;
      this.measureFrame = requestAnimationFrame(() => {
        this.measureFrame = null;
        if (!this.media.matches) return;
        const bounds = this.header.getBoundingClientRect();
        this.lastHeight = `${Math.round(bounds.height * 100) / 100}px`;
        this.lastOffset = `${Math.max(0, Math.round(bounds.bottom * 100) / 100)}px`;
        document.documentElement.style.setProperty('--header-height', this.lastHeight);
        document.documentElement.style.setProperty('--bc-mobile-drawer-offset', this.lastOffset);
      });
    }

    restoreMetrics() {
      if (!this.ownsHeight) return;
      const style = document.documentElement.style;
      if (style.getPropertyValue('--header-height') === this.lastHeight) {
        if (this.previousHeight) style.setProperty('--header-height', this.previousHeight);
        else style.removeProperty('--header-height');
      }
      if (style.getPropertyValue('--bc-mobile-drawer-offset') === this.lastOffset) {
        if (this.previousOffset) style.setProperty('--bc-mobile-drawer-offset', this.previousOffset);
        else style.removeProperty('--bc-mobile-drawer-offset');
      }
      this.ownsHeight = false;
    }

    destroy() {
      this.abort.abort();
      this.media.removeEventListener('change', this.onMedia);
      this.observer?.disconnect();
      if (this.frame !== null) cancelAnimationFrame(this.frame);
      if (this.measureFrame !== null) cancelAnimationFrame(this.measureFrame);
      this.search.inert = false;
      this.search.removeAttribute('aria-hidden');
      this.restoreMetrics();
      delete this.section.dataset.bcInput;
      delete this.section.dataset.bcScrollState;
      delete this.section.bcMobileHeader;
    }
  }

  window.BCMobileHeader = BCMobileHeader;
  const roots = scope => {
    const found = [...scope.querySelectorAll('.section-header')];
    if (scope.matches?.('.section-header')) found.unshift(scope);
    return found;
  };
  const scan = scope => roots(scope).forEach(section => {
    if (!section.bcMobileHeader) new BCMobileHeader(section);
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => scan(document), { once: true });
  else scan(document);
  document.addEventListener('shopify:section:load', event => scan(event.target));
  document.addEventListener('shopify:section:unload', event => roots(event.target).forEach(section => section.bcMobileHeader?.destroy()));
})();
