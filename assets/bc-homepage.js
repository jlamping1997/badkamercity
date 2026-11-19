(() => {
  if (window.bcHomepageNavigationBound) return;
  window.bcHomepageNavigationBound = true;
  const reveal = (hash) => {
    if (!hash || hash === '#') return;
    let target;
    try { target = document.getElementById(decodeURIComponent(hash.slice(1))); } catch { return; }
    if (!target || !target.closest('[data-bch-home]')) return;
    const panel = target.matches('details') ? target : target.closest('details');
    if (panel) panel.open = true;
    const success = target.querySelector('.bch-form-success');
    if (success) success.focus({ preventScroll: true });
  };
  document.addEventListener('click', (event) => {
    const link = event.target.closest('a[href^="#"]');
    if (link) reveal(link.hash);
  });
  const restore = () => {
    reveal(window.location.hash);
    document.querySelectorAll('[data-bch-home] .bch-form-success, [data-bch-home] .bch-form-errors').forEach((message) => {
      const panel = message.closest('details');
      if (panel) panel.open = true;
    });
  };
  window.addEventListener('hashchange', restore);
  document.addEventListener('shopify:section:load', restore);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', restore, { once: true });
  else restore();
})();
