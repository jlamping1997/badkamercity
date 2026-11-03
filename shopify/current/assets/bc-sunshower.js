(() => {
  if (window.bcSunshowerLoaded) return;
  window.bcSunshowerLoaded = true;
  const isPreview = () => location.pathname.includes('products_preview') || Boolean(window.Shopify?.designMode);
  const expectedProduct = new URLSearchParams(location.search).get('bc_sunshower');
  const renderedProduct = document.querySelector('[data-sunshower-product]')?.dataset.sunshowerProduct;
  if (isPreview() && expectedProduct && renderedProduct && expectedProduct !== renderedProduct) {
    const retryKey = `bc-sunshower-preview-${expectedProduct}`;
    if (!sessionStorage.getItem(retryKey)) {
      sessionStorage.setItem(retryKey, '1');
      location.reload();
      return;
    }
  } else if (expectedProduct) {
    sessionStorage.removeItem(`bc-sunshower-preview-${expectedProduct}`);
  }
  function productUrl(item) {
    const target = new URL(isPreview() && item.preview_url ? item.preview_url : item.url, location.origin);
    const url = new URL(target.pathname + target.search, location.origin);
    const theme = new URLSearchParams(location.search).get('preview_theme_id');
    if (theme) url.searchParams.set('preview_theme_id', theme);
    if (isPreview() && item.source_product_id) url.searchParams.set('bc_sunshower', item.source_product_id);
    return url.href;
  }
  let catalogPromise;
  function initialize(root = document) {
    root.querySelectorAll('[data-sunshower-preview]').forEach(link => {
      if (isPreview() && link.dataset.sunshowerPreview) link.href = productUrl({url:link.href, preview_url:link.dataset.sunshowerPreview, source_product_id:link.dataset.sunshowerSource});
    });
    root.querySelectorAll('[data-sunshower-choices]').forEach(container => {
      if (container.dataset.initialized) return;
      container.dataset.initialized = 'true';
      const fields = [...container.querySelectorAll('[data-sunshower-field]')];
      const status = container.querySelector('[role="status"]');
      const original = fields.map(field => field.value);
      container.addEventListener('change', async () => {
        container.setAttribute('aria-busy', 'true');
        fields.forEach(field => { field.disabled = true; });
        status.textContent = container.dataset.loading;
        try {
          catalogPromise ||= fetch(container.dataset.catalog).then(response => {
            if (!response.ok) throw new Error('catalog');
            return response.json();
          }).catch(error => { catalogPromise = undefined; throw error; });
          const catalog = await catalogPromise;
          const selected = Object.fromEntries(fields.map(field => [field.dataset.sunshowerField, field.value]));
          const match = catalog.products.find(item => Object.entries(selected).every(([key,value]) => item.selection[key] === value));
          if (!match) throw new Error('configuration');
          location.assign(productUrl(match));
        } catch {
          status.textContent = container.dataset.error;
          fields.forEach((field,index) => { field.value = original[index]; field.disabled = false; });
          container.removeAttribute('aria-busy');
        }
      });
    });

  }
  initialize();
  document.addEventListener('shopify:section:load', event => initialize(event.target));
})();
