(() => {
  'use strict';
  const init = () => {
    const button = document.querySelector('[data-bc-floating-filter]');
    const section = document.querySelector('.template-search, .bc-collection');
    if (!button || !section || button.dataset.initialized) return;
    button.dataset.initialized = 'true';
    document.body.appendChild(button);
    const mobile = window.matchMedia('(max-width: 749px)');
    let frame;
    let returnFocus = false;
    const trigger = () => document.documentElement.classList.contains('bc-external-filters-active')
      ? section.querySelector('[data-bc-open-filters]')
      : section.querySelector('.mobile-facets__open-wrapper');
    const update = () => {
      frame = null;
      const opener = trigger();
      const grid = section.querySelector('#product-grid');
      const open = document.documentElement.classList.contains('bc-filter-drawer-open') ||
        Boolean(section.querySelector('.mobile-facets__disclosure[open]'));
      const otherOverlay = Boolean(document.querySelector('menu-drawer details[open], cart-drawer.active, dialog[open], .search-modal[open]'));
      const rect = grid?.getBoundingClientRect();
      const show = mobile.matches && opener?.getClientRects().length && rect &&
        opener.getBoundingClientRect().bottom < 0 && rect.top < window.innerHeight && rect.bottom > 100 && !open && !otherOverlay;
      button.hidden = !show;
      if (!open && returnFocus) {
        returnFocus = false;
        (show ? button : opener)?.focus({ preventScroll: true });
      }
    };
    const schedule = () => { if (!frame) frame = window.requestAnimationFrame(update); };
    button.addEventListener('click', () => {
      const opener = trigger();
      if (!opener) return;
      returnFocus = true;
      opener.click();
      schedule();
    });
    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', schedule, { passive: true });
    document.addEventListener('toggle', schedule, true);
    mobile.addEventListener('change', schedule);
    new MutationObserver(schedule).observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    new MutationObserver(schedule).observe(section, { childList: true, subtree: true });
    update();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
