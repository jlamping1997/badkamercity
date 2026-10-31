(() => {
  'use strict';
  if (window.BCWishlist) return;
  const KEY = 'bc_wishlist_v1';
  const MAX = 100;
  const HANDLE = /^[a-z0-9][a-z0-9-]{0,199}$/;
  const VARIANT = /^\d{5,20}$/;
  const cache = new Map();
  let items = load();
  let toastTimer;
  let frame;
  let rendering = 0;

  function normalise(entry) {
    if (!entry || typeof entry !== 'object') return null;
    const handle = String(entry.handle || '').trim().toLowerCase();
    const variantId = String(entry.variantId || '').trim();
    if (!HANDLE.test(handle) || !VARIANT.test(variantId)) return null;
    return {
      handle,
      variantId,
      title: String(entry.title || '').slice(0, 180),
      image: String(entry.image || '').slice(0, 800),
      source: entry.source === 'sunshower' ? 'sunshower' : entry.source === 'detail' ? 'detail' : 'card',
      savedAt: Number(entry.savedAt) || Date.now()
    };
  }

  function readStored() {
    const raw = localStorage.getItem(KEY);
    const value = raw === null ? [] : JSON.parse(raw);
    if (!Array.isArray(value)) throw new Error('wishlist');
    return value.map(normalise).filter(Boolean).slice(0, MAX);
  }

  function load() {
    try { return readStored(); } catch (error) { return []; }
  }

  async function commit(operation) {
    const apply = () => {
      try {
        const next = operation(readStored());
        return next ? save(next) : false;
      } catch (error) {
        toast('Toevoegen aan je verlanglijst is niet gelukt.');
        return false;
      }
    };
    try {
      return navigator.locks?.request ? await navigator.locks.request(KEY, apply) : apply();
    } catch (error) {
      toast('Toevoegen aan je verlanglijst is niet gelukt.');
      return false;
    }
  }

  function save(next) {
    try {
      localStorage.setItem(KEY, JSON.stringify(next));
      items = next;
      notify();
      return true;
    } catch (error) {
      toast('Opslaan is geblokkeerd in deze browser. Controleer je privacy-instellingen.');
      return false;
    }
  }

  function identity(entry) { return entry.handle + ':' + entry.variantId; }
  function has(handle, variantId) { return items.some(item => item.handle === handle && item.variantId === variantId); }
  function productUrl(entry) {
    return '/products/' + encodeURIComponent(entry.handle) + '?variant=' + encodeURIComponent(entry.variantId);
  }

  function buttonScope(button) {
    return button.closest('[data-bcsse-shop-card]') || button.closest('[data-ss-page]') ||
      button.closest('product-info') || button.closest('.bc-search-card') ||
      button.closest('.bc-filter-card') || button.closest('.bc-standard-card') || null;
  }

  function details(button) {
    const scope = buttonScope(button);
    const shopCard = button.closest('[data-bcsse-shop-card]');
    let handle = button.dataset.bcWishlistHandle || '';
    if (shopCard) {
      const link = shopCard.querySelector('[data-bcsse-shop-link]');
      if (link) {
        try { handle = new URL(link.href).pathname.split('/products/')[1]?.split('/')[0] || handle; } catch (error) {}
      }
    }
    handle = String(handle).trim().toLowerCase();
    const ownForm = button.closest('form')?.querySelector('input[name="id"]') ||
      button.closest('product-form')?.querySelector('input[name="id"]');
    const field = ownForm || (scope && (
      scope.querySelector('form[data-bcsse-shop-form] input[name="id"]') ||
      scope.querySelector('.ss-product-form input[name="id"]') ||
      scope.querySelector('product-form input[name="id"]')
    ));
    let variantId = field ? String(field.value || '') : String(button.dataset.bcWishlistVariant || '');
    if (scope?.matches('[data-ss-page]') && scope.dataset.variant) variantId = String(scope.dataset.variant);
    const title = shopCard?.querySelector('.bcsse-accessory__title')?.textContent?.trim() ||
      button.dataset.bcWishlistTitle || '';
    return {
      handle, variantId,
      title, image: button.dataset.bcWishlistImage || '',
      source: button.dataset.bcWishlistSource || 'card',
      savedAt: Date.now()
    };
  }

  function staticIcon() {
    const svgNS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNS, 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('class', 'icon icon-wishlist-bc');
    svg.setAttribute('aria-hidden', 'true');
    const d = 'M12 20.25 4.98 13.6a4.52 4.52 0 0 1 0-6.54 4.8 4.8 0 0 1 6.71 0L12 7.36l.31-.3a4.8 4.8 0 0 1 6.71 0 4.52 4.52 0 0 1 0 6.54z';
    const fill = document.createElementNS(svgNS, 'path');
    fill.setAttribute('class', 'icon-wishlist-bc__fill');
    fill.setAttribute('d', d);
    fill.setAttribute('fill', 'currentColor');
    const stroke = document.createElementNS(svgNS, 'path');
    stroke.setAttribute('class', 'icon-wishlist-bc__stroke');
    stroke.setAttribute('d', d);
    stroke.setAttribute('fill', 'none');
    stroke.setAttribute('stroke', 'currentColor');
    stroke.setAttribute('stroke-width', '1.8');
    stroke.setAttribute('stroke-linecap', 'round');
    stroke.setAttribute('stroke-linejoin', 'round');
    svg.append(fill, stroke);
    return svg;
  }

  function decorateCards(root) {
    if (!root?.querySelectorAll) return;
    root.querySelectorAll('.bc-filter-card:not([data-bc-wishlist-decorated])').forEach(card => {
      card.setAttribute('data-bc-wishlist-decorated', 'true');
      const link = card.querySelector('.bc-filter-card__title a');
      if (!link) return;
      let handle = '';
      try { handle = new URL(link.href).pathname.split('/products/')[1]?.split('/')[0] || ''; } catch (error) {}
      if (!HANDLE.test(handle)) return;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'bc-wishlist-button bc-wishlist-button--card';
      button.setAttribute('data-bc-wishlist-toggle', '');
      button.dataset.bcWishlistHandle = handle;
      button.dataset.bcWishlistTitle = link.getAttribute('title') || link.textContent.trim();
      button.dataset.bcWishlistSource = 'card';
      button.setAttribute('aria-pressed', 'false');
      button.append(staticIcon());
      card.prepend(button);
    });
  }

  function syncButtons(root = document) {
    if (!root?.querySelectorAll) return;
    root.querySelectorAll('[data-bc-wishlist-toggle]').forEach(button => {
      const d = details(button);
      const active = HANDLE.test(d.handle) && (VARIANT.test(d.variantId)
        ? has(d.handle, d.variantId)
        : items.some(entry => entry.handle === d.handle));
      const title = String(d.title || 'dit product').slice(0, 100);
      button.classList.toggle('is-saved', active);
      button.setAttribute('aria-pressed', String(active));
      const message = active ? 'Verwijder ' + title + ' uit je verlanglijst' : 'Bewaar ' + title + ' op je verlanglijst';
      button.setAttribute('aria-label', message);
      button.setAttribute('title', message);
    });
    document.querySelectorAll('[data-bc-wishlist-count]').forEach(count => {
      count.textContent = String(items.length);
      count.hidden = items.length === 0;
    });
    document.querySelectorAll('.bc-header__utility-link--wishlist').forEach(link => {
      link.classList.toggle('has-saved-items', items.length > 0);
      link.setAttribute('aria-label', items.length
        ? 'Verlanglijst: ' + items.length + (items.length === 1 ? ' bewaard product' : ' bewaarde producten')
        : 'Verlanglijst');
    });
  }

  function toast(message) {
    let status = document.getElementById('BCWishlistStatus');
    if (!status) {
      status = document.createElement('div');
      status.id = 'BCWishlistStatus';
      status.className = 'bc-wishlist-toast';
      status.setAttribute('role', 'status');
      status.setAttribute('aria-live', 'polite');
      document.body.appendChild(status);
    }
    status.textContent = message;
    status.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { status.hidden = true; }, 2900);
  }

  function notify() {
    syncButtons();
    if (document.querySelector('[data-bc-wishlist-page]')) renderPage();
    document.dispatchEvent(new CustomEvent('bc:wishlist-changed', { detail: { count: items.length } }));
  }

  async function readProduct(handle) {
    if (!HANDLE.test(handle)) throw new Error('Ongeldige productverwijzing');
    if (!cache.has(handle)) {
      const promise = fetch('/products/' + encodeURIComponent(handle) + '.js', {
        credentials: 'same-origin', headers: { Accept: 'application/json' }
      }).then(response => { if (!response.ok) throw new Error('Product niet beschikbaar'); return response.json(); });
      cache.set(handle, promise.catch(error => { cache.delete(handle); throw error; }));
    }
    return cache.get(handle);
  }

  async function toggleButton(button) {
    if (button.disabled || button.dataset.bcWishlistBusy === 'true') return;
    button.dataset.bcWishlistBusy = 'true';
    try {
      let entry = details(button);
      const removeIntent = VARIANT.test(entry.variantId)
        ? has(entry.handle, entry.variantId) : items.some(item => item.handle === entry.handle);
      if (!HANDLE.test(entry.handle)) throw new Error('Geen geldige productlink gevonden.');
      if (!VARIANT.test(entry.variantId)) {
        const existing = readStored().filter(item => item.handle === entry.handle);
        if (existing.length === 1) {
          entry.variantId = existing[0].variantId;
        } else if (existing.length > 1) {
          toast('Bekijk de productpagina om verschillende uitvoeringen te beheren.');
          return;
        } else {
          const product = await readProduct(entry.handle);
          const variant = (product.variants || []).find(item => item.available) || (product.variants || [])[0];
          if (!variant) throw new Error('Geen uitvoering beschikbaar.');
          entry.variantId = String(variant.id);
        }
      }
      entry = normalise(entry);
      if (!entry) throw new Error('Product kon niet worden opgeslagen.');
      const key = identity(entry);
      const saved = await commit(latest => {
        const existing = latest.some(item => identity(item) === key);
        if (removeIntent) return latest.filter(item => identity(item) !== key);
        if (existing) return latest;
        if (latest.length >= MAX) { toast('Je verlanglijst kan maximaal 100 producten bevatten.'); return null; }
        return [entry].concat(latest);
      });
      if (saved) toast(removeIntent ? 'Verwijderd uit je verlanglijst' : 'Toegevoegd aan je verlanglijst');
    } catch (error) {
      toast(error?.message || 'Toevoegen aan je verlanglijst is niet gelukt.');
    } finally {
      delete button.dataset.bcWishlistBusy;
    }
  }

  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = String(text);
    return node;
  }
  function safeImage(src) {
    if (!src) return '';
    try {
      const url = new URL(src, location.origin);
      if (url.protocol !== 'https:' && url.origin !== location.origin) return '';
      return url.href;
    } catch (error) { return ''; }
  }
  function formatPrice(cents) {
    const price = Number(cents);
    if (!Number.isFinite(price)) return 'Prijs op aanvraag';
    return new Intl.NumberFormat('nl-NL', { style: 'currency', currency: 'EUR' }).format(price / 100);
  }
  function imageSource(product, variant, item) {
    const image = variant?.featured_image?.src || product?.featured_image ||
      (Array.isArray(product?.images) ? product.images[0] : '') || item.image;
    const src = typeof image === 'object' ? image?.src : image;
    return safeImage(src);
  }
  function setPageCount() {
    const count = document.querySelector('[data-bc-wishlist-page-count]');
    if (count) count.textContent = items.length === 1 ? '1 bewaard product' : items.length + ' bewaarde producten';
  }

  function cardShell(entry) {
    const card = element('article', 'bc-wishlist-item');
    card.setAttribute('data-bc-wishlist-card', '');
    card.setAttribute('role', 'listitem');
    card.dataset.bcWishlistIdentity = identity(entry);
    const media = element('a', 'bc-wishlist-item__media');
    media.href = productUrl(entry);
    const img = element('img');
    img.loading = 'lazy'; img.width = 400; img.height = 400;
    img.alt = ''; img.hidden = true;
    const placeholder = element('div', 'bc-wishlist-item__placeholder', 'Productafbeelding laden…');
    media.append(img, placeholder);
    const body = element('div', 'bc-wishlist-item__body');
    const title = element('a', 'bc-wishlist-item__title', entry.title || entry.handle.replace(/-/g, ' '));
    title.href = productUrl(entry);
    const variant = element('p', 'bc-wishlist-item__variant', '');
    variant.hidden = true;
    const price = element('p', 'bc-wishlist-item__price', 'Prijs ophalen…');
    const delivery = element('p', 'bc-wishlist-item__delivery', 'Productgegevens controleren…');
    const actions = element('div', 'bc-wishlist-item__actions');
    const primary = element('a', 'bc-wishlist-item__primary', 'Bekijk product');
    primary.href = productUrl(entry);
    const remove = element('button', 'bc-wishlist-item__remove', 'Verwijderen');
    remove.type = 'button';
    remove.dataset.bcWishlistRemove = identity(entry);
    remove.setAttribute('aria-label', 'Verwijder product uit verlanglijst');
    actions.append(primary, remove);
    body.append(title, variant, price, delivery, actions);
    card.append(media, body);
    return { card, media, img, placeholder, title, variant, price, delivery, primary };
  }

  function showError(parts) {
    parts.price.textContent = 'Prijs niet beschikbaar';
    parts.delivery.textContent = 'Dit product kan niet worden opgehaald. Je kunt het uit de lijst verwijderen.';
    parts.primary.textContent = 'Bekijk product';
  }

  async function hydrate(entry, parts, renderId) {
    try {
      const product = await readProduct(entry.handle);
      if (renderId !== rendering || !parts.card.isConnected) return;
      const variants = Array.isArray(product.variants) ? product.variants : [];
      const variant = variants.find(v => String(v.id) === entry.variantId);
      if (!variant) { showError(parts); parts.delivery.textContent = 'Deze uitvoering is niet meer beschikbaar.'; return; }
      parts.title.textContent = product.title || entry.title || entry.handle.replace(/-/g, ' ');
      parts.title.href = productUrl(entry);
      parts.media.href = productUrl(entry);
      const label = variant.public_title || variant.title;
      if (label && label !== 'Default Title') {
        parts.variant.textContent = label;
        parts.variant.hidden = false;
      }
      const source = imageSource(product, variant, entry);
      if (source) {
        parts.img.src = source;
        parts.img.hidden = false;
        parts.img.alt = String(product.title || entry.title);
        parts.placeholder.hidden = true;
      } else {
        parts.placeholder.textContent = 'Geen afbeelding beschikbaar';
      }
      parts.price.textContent = formatPrice(variant.price);
      if (variant.available === false) {
        parts.delivery.textContent = 'Deze uitvoering is momenteel niet beschikbaar.';
        parts.primary.textContent = 'Bekijk product';
      } else if (entry.source === 'sunshower' || (variants.length > 1 && entry.source === 'card') ||
          product.requires_selling_plan || variant.requires_selling_plan ||
          (variant.quantity_rule?.min && Number(variant.quantity_rule.min) !== 1) ||
          (variant.quantity_rule?.increment && Number(variant.quantity_rule.increment) !== 1)) {
        parts.delivery.textContent = 'Controleer je gekozen uitvoering en de levertijd op de productpagina.';
        parts.primary.textContent = 'Bekijk uitvoering';
      } else {
        parts.delivery.textContent = 'Bekijk de actuele levertijd op de productpagina · inclusief btw';
        const add = element('button', 'bc-wishlist-item__primary', 'In winkelwagen');
        add.type = 'button';
        add.dataset.bcWishlistAdd = identity(entry);
        parts.primary.replaceWith(add);
        parts.primary = add;
      }
    } catch (error) {
      if (renderId !== rendering || !parts.card.isConnected) return;
      showError(parts);
    }
  }

  function renderPage() {
    const page = document.querySelector('[data-bc-wishlist-page]');
    if (!page) return;
    const id = ++rendering;
    const grid = page.querySelector('[data-bc-wishlist-grid]');
    const empty = page.querySelector('[data-bc-wishlist-empty]');
    const loading = page.querySelector('[data-bc-wishlist-loading]');
    if (!grid || !empty || !loading) return;
    setPageCount();
    grid.replaceChildren();
    empty.hidden = items.length !== 0;
    grid.hidden = items.length === 0;
    loading.hidden = true;
    if (!items.length) return;
    const hydrations = [];
    for (const item of items) {
      const parts = cardShell(item);
      grid.appendChild(parts.card);
      hydrations.push(() => hydrate(item, parts, id));
    }
    // A limited number of parallel product requests keeps this page light.
    let next = 0;
    for (let i = 0; i < Math.min(4, hydrations.length); i++) {
      (async () => { while (next < hydrations.length && id === rendering) await hydrations[next++](); })();
    }
  }

  async function addFromPage(button) {
    const item = items.find(entry => identity(entry) === button.dataset.bcWishlistAdd);
    if (!item || button.disabled) return;
    button.disabled = true;
    button.textContent = 'Toevoegen…';
    try {
      const product = await readProduct(item.handle);
      const variants = Array.isArray(product.variants) ? product.variants : [];
      const variant = variants.find(v => String(v.id) === item.variantId);
      if (!variant?.available || item.source === 'sunshower' || (variants.length > 1 && item.source === 'card') ||
          product.requires_selling_plan || variant.requires_selling_plan ||
          (variant.quantity_rule?.min && Number(variant.quantity_rule.min) !== 1) ||
          (variant.quantity_rule?.increment && Number(variant.quantity_rule.increment) !== 1)) {
        location.assign(productUrl(item));
        return;
      }
      const base = window.routes?.cart_add_url || '/cart/add';
      const endpoint = base.replace(/\/$/, '') + '.js';
      const response = await fetch(endpoint, {
        method: 'POST', credentials: 'same-origin',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ id: Number(item.variantId), quantity: 1 })
      });
      if (!response.ok) throw new Error('Het product kon niet aan de winkelwagen worden toegevoegd.');
      location.assign(window.routes?.cart_url || '/cart');
    } catch (error) {
      button.disabled = false;
      button.textContent = 'In winkelwagen';
      toast(error?.message || 'Toevoegen is niet gelukt.');
    }
  }

  document.addEventListener('click', event => {
    const toggle = event.target.closest('[data-bc-wishlist-toggle]');
    if (toggle) { event.preventDefault(); event.stopPropagation(); toggleButton(toggle); return; }
    const remove = event.target.closest('[data-bc-wishlist-remove]');
    if (remove) {
      if (remove.disabled) return;
      remove.disabled = true;
      commit(latest => latest.filter(entry => identity(entry) !== remove.dataset.bcWishlistRemove))
        .then(saved => { if (saved) toast('Product verwijderd'); })
        .finally(() => { if (remove.isConnected) remove.disabled = false; });
      return;
    }
    const add = event.target.closest('[data-bc-wishlist-add]');
    if (add) addFromPage(add);
  });
  function schedule() {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = null;
      decorateCards(document);
      syncButtons();
    });
  }
  document.addEventListener('change', event => {
    if (event.target.matches('select, input[name="id"], input[type="radio"]')) schedule();
  }, true);
  document.addEventListener('shopify:section:load', schedule);
  window.addEventListener('storage', event => {
    if (event.key === KEY || event.key === null) { items = load(); notify(); }
  });
  window.BCWishlist = {
    list: () => items.map(item => ({ ...item })),
    refresh: root => root?.querySelectorAll ? syncButtons(root) : schedule(),
    has,
    key: KEY
  };
  function init() {
    decorateCards(document);
    syncButtons();
    renderPage();
    const content = document.getElementById('MainContent') || document.body;
    const observer = new MutationObserver(mutations => {
      if (mutations.some(m => [...m.addedNodes].some(node => node.nodeType === 1 && (
        node.matches?.('.bc-filter-card, #product-grid, .bc-search-card, .bc-standard-card') ||
        node.querySelector?.('.bc-filter-card, .bc-standard-card, .bc-search-card')
      )))) schedule();
    });
    observer.observe(content, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();
