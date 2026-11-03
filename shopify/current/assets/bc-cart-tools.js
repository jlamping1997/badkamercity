(() => {
  if (window.BCCartTools) return;
  const storageKey = `bc-saved-cart-v1:${location.hostname}`;
  const maxAge = 30 * 24 * 60 * 60 * 1000;
  let pending = false;
  const config = () => document.querySelector('[data-bc-cart-tools]') || document.querySelector('[data-bc-restore-wrap]');
  const saved = () => {
    try {
      const value = JSON.parse(localStorage.getItem(storageKey) || 'null');
      if (!value || value.version !== 1 || !Array.isArray(value.items) || !value.items.length || Date.now() - value.savedAt > maxAge) return null;
      if (!value.items.every(item => Number.isSafeInteger(item.id) && item.id > 0 && Number.isInteger(item.quantity) && item.quantity > 0)) return null;
      return value;
    } catch { return null; }
  };
  const sync = () => {
    document.querySelectorAll('[data-bc-save], [data-bc-quote]').forEach(button => { button.hidden = false; });
    document.querySelectorAll('[data-bc-restore-wrap]').forEach(wrap => { wrap.hidden = !saved(); });
  };
  const status = (text, error = false) => {
    const root = document.querySelector('cart-items.is-empty .bc-cart-empty') || document.querySelector('#main-cart-items');
    const node = root?.querySelector('[data-bc-tools-status]');
    if (node) { node.textContent = text; node.dataset.error = String(error); }
  };
  const cart = async () => {
    const response = await fetch(`${window.routes.cart_url.replace(/\/$/, '')}.js`, { cache: 'no-store', headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error('cart');
    const value = await response.json();
    if (!Array.isArray(value.items)) throw new Error('cart');
    return value;
  };
  const save = async () => {
    const data = await cart();
    if (!data.items.length) throw new Error('empty');
    if (data.items.some(item => item.parent_relationship?.parent)) throw new Error('nested');
    const value = { version: 1, savedAt: Date.now(), items: data.items.map(item => ({ id: item.variant_id || item.id, quantity: item.quantity, properties: item.properties || {}, ...(item.selling_plan_allocation?.selling_plan?.id ? { selling_plan: item.selling_plan_allocation.selling_plan.id } : {}) })) };
    localStorage.setItem(storageKey, JSON.stringify(value));
    status(config()?.dataset.saved || '');
    sync();
  };
  const quote = async () => {
    const data = await cart();
    const el = config();
    const currency = data.currency || el.dataset.currency || 'EUR';
    const formatter = new Intl.NumberFormat(el.dataset.locale || 'nl-NL', { style: 'currency', currency });
    const lines = [el.dataset.quoteIntro, ''];
    data.items.forEach(item => {
      lines.push(`${item.quantity} × ${item.product_title || item.title}`);
      if (item.variant_title && item.variant_title !== 'Default Title') lines.push(item.variant_title);
      if (item.sku) lines.push(`SKU: ${item.sku}`);
      lines.push(`${formatter.format(item.final_price / 100)} ${el.dataset.perItem || ''}`);
      for (const [name, value] of Object.entries(item.properties || {})) if (!name.startsWith('_') && value) lines.push(`${name}: ${value}`);
      if (item.url) lines.push(new URL(item.url, location.origin).href);
      lines.push('');
    });
    const url = `mailto:${encodeURIComponent(el.dataset.quoteEmail)}?subject=${encodeURIComponent(el.dataset.quoteSubject)}&body=${encodeURIComponent(lines.join('\r\n'))}`;
    if (url.length > 16000) throw new Error('length');
    location.href = url;
  };
  const restore = async () => {
    const value = saved();
    if (!value) throw new Error('saved');
    const current = await cart();
    if (current.item_count) throw new Error('not-empty');
    status(config()?.dataset.restoring || '');
    const response = await fetch(window.routes.cart_add_url, { method: 'POST', headers: { Accept: 'application/json', 'Content-Type': 'application/json' }, body: JSON.stringify({ items: value.items }) });
    if (!response.ok) throw new Error('restore');
    localStorage.removeItem(storageKey);
    location.reload();
  };
  document.addEventListener('click', async event => {
    const button = event.target instanceof Element ? event.target.closest('[data-bc-save], [data-bc-quote], [data-bc-restore]') : null;
    if (!button) return;
    event.preventDefault();
    if (pending || window.BCCartPage?.busy) return;
    pending = true;
    button.disabled = true;
    const messageConfig = config();
    const action = button.hasAttribute('data-bc-save') ? 'save' : button.hasAttribute('data-bc-restore') ? 'restore' : 'quote';
    try {
      await ({ save, quote, restore })[action]();
    } catch {
      status(messageConfig?.dataset[`${action}Error`] || '', true);
    } finally {
      pending = false;
      button.disabled = false;
    }
  });
  window.BCCartTools = { sync };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', sync, { once: true }) : sync();
})();
