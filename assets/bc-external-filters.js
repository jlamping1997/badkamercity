(() => {
  'use strict';

  const ready = (fn) => {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn, { once: true });
    } else {
      fn();
    }
  };

  ready(() => {
    const root = document.getElementById('BcExternalFilters');
    if (!root) return;

    const apiBase = root.dataset.apiBase;
    const collectionHandle = root.dataset.collection;
    const isSearch = root.dataset.searchMode === 'true';
    const sectionRoot = root.closest(isSearch ? '.template-search' : '.bc-collection');
    const searchTypes = new URL(window.location.href).searchParams.get('type');
    if (isSearch && searchTypes && !searchTypes.split(',').includes('product')) return;
    if (!apiBase || !collectionHandle || !sectionRoot) return;

    const layout =
      sectionRoot.querySelector('.facets-vertical.page-width') ||
      sectionRoot.querySelector('.facets-vertical');

    const productContainer = sectionRoot.querySelector('#ProductGridContainer');
    const productGrid = productContainer?.querySelector('#product-grid');

    if (!layout || !productContainer || !productGrid) {
      console.error('[BadkamerCity filters] Benodigde collectie-elementen niet gevonden.');
      return;
    }

    const nativeAside = sectionRoot.querySelector(isSearch ? '#main-search-filters' : '#main-collection-filters');
    const nativeSort = sectionRoot.querySelector(isSearch ? 'facet-filters-form.template-search__toolbar' : 'facet-filters-form.facets-vertical-sort');
    const nativePagination = productContainer.querySelector('.pagination-wrapper');
    const nativeNodes = [nativeAside, nativeSort, nativePagination, ...sectionRoot.querySelectorAll('[data-bc-native-search-status]')].filter(Boolean);
    const nativeDisplays = new Map(nativeNodes.map((node) => [node, node.style.display]));
    const nativeGridNodes = [...productGrid.childNodes];
    const expectedCount = isSearch ? NaN : Number(root.dataset.productsCount);
    const cardDataCache = new Map();
    let externalActive = false;
    let requestId = 0;
    let requestController;
    let filtersRendered = false;
    let rangeTimer;

    const state = {
      filters: {},
      ranges: {},
      sort: 'relevance',
      page: 1,
      perPage: 24,
      lastData: null
    };

    parseStateFromUrl();

    const sidebar = document.createElement('aside');
    sidebar.className = 'facets-wrapper bc-external-filter-sidebar';
    sidebar.setAttribute('aria-label', 'Filters');
    sidebar.innerHTML = `
      <div class="bc-filter-panel">
        <div class="bc-filter-panel__header">
          <h2>Filters</h2>
          <button type="button" class="bc-filter-panel__close" aria-label="Filters sluiten">✕</button>
        </div>
        <div class="bc-filter-groups" data-bc-filter-groups>
          <div style="padding:1.8rem">Filters laden…</div>
        </div>
        <div class="bc-filter-panel__footer">
          <button type="button" class="bc-filter-clear" data-bc-clear-all>Alles wissen</button>
        </div>
      </div>
    `;

    layout.insertBefore(sidebar, productContainer);

    const overlay = document.createElement('div');
    overlay.className = 'bc-filter-drawer-overlay';
    overlay.setAttribute('aria-hidden', 'true');
    document.body.appendChild(overlay);

    const toolbar = document.createElement('div');
    toolbar.className = 'bc-filter-toolbar';
    toolbar.innerHTML = `
      <div class="bc-filter-toolbar__left">
        <button type="button" class="bc-filter-mobile-button" data-bc-open-filters>
          Filters
        </button>
        <span class="bc-filter-count" data-bc-count>Producten laden…</span>
      </div>
      <div class="bc-filter-toolbar__right">
        <label for="BcFilterSort" class="visually-hidden">Sorteren</label>
        <select id="BcFilterSort" class="bc-filter-sort">
          <option value="relevance">Aanbevolen</option>
          <option value="price_asc">Prijs laag - hoog</option>
          <option value="price_desc">Prijs hoog - laag</option>
        </select>
      </div>
    `;

    productContainer.insertBefore(toolbar, productContainer.firstChild);

    const activeFilters = document.createElement('div');
    activeFilters.className = 'bc-filter-active';
    activeFilters.setAttribute('data-bc-active-filters', '');
    productGrid.parentNode.insertBefore(activeFilters, productGrid);

    const errorBox = document.createElement('div');
    errorBox.className = 'bc-filter-error';
    errorBox.hidden = true;
    productGrid.parentNode.insertBefore(errorBox, productGrid);

    const pagination = document.createElement('div');
    pagination.className = 'bc-filter-pagination';
    pagination.setAttribute('data-bc-pagination', '');
    productContainer.appendChild(pagination);

    const sortSelect = toolbar.querySelector('#BcFilterSort');
    sortSelect.value = state.sort;

    sidebar.addEventListener('change', onFilterChange);
    sidebar.addEventListener('input', onRangeInput);
    sidebar.addEventListener('click', onSidebarClick);
    activeFilters.addEventListener('click', onChipClick);
    pagination.addEventListener('click', onPaginationClick);

    toolbar.querySelector('[data-bc-open-filters]').addEventListener('click', openDrawer);
    sidebar.querySelector('.bc-filter-panel__close').addEventListener('click', closeDrawer);
    overlay.addEventListener('click', closeDrawer);
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') closeDrawer();
    });

    sortSelect.addEventListener('change', () => {
      state.sort = sortSelect.value;
      state.page = 1;
      syncUrl();
      runSearch();
    });

    window.addEventListener('popstate', (event) => {
      if (externalActive) event.stopImmediatePropagation();
      resetState();
      parseStateFromUrl();
      sortSelect.value = state.sort;
      runSearch();
    }, { capture: true });

    setExternalMode(false);
    runSearch();

    function resetState() {
      clearTimeout(rangeTimer);
      state.filters = {};
      state.ranges = {};
      state.sort = 'relevance';
      state.page = 1;
    }

    function parseStateFromUrl() {
      const params = new URL(window.location.href).searchParams;

      for (const key of new Set(params.keys())) {
        if (key.startsWith('bcf_')) {
          const field = key.slice(4);
          state.filters[field] = params.getAll(key);
        }

        if (key.startsWith('bcr_') && key.endsWith('_min')) {
          const field = key.slice(4, -4);
          state.ranges[field] = state.ranges[field] || {};
          const value = Number(params.get(key));
          if (Number.isFinite(value)) state.ranges[field].min = value;
        }

        if (key.startsWith('bcr_') && key.endsWith('_max')) {
          const field = key.slice(4, -4);
          state.ranges[field] = state.ranges[field] || {};
          const value = Number(params.get(key));
          if (Number.isFinite(value)) state.ranges[field].max = value;
        }
      }

      const sort = params.get('bcsort');
      if (['relevance', 'price_asc', 'price_desc'].includes(sort)) {
        state.sort = sort;
      }

      const page = Number(params.get('bcpage'));
      if (Number.isInteger(page) && page > 0) {
        state.page = page;
      }
    }

    function syncUrl() {
      const next = new URL(window.location.href);

      for (const key of [...next.searchParams.keys()]) {
        if (
          key.startsWith('bcf_') ||
          key.startsWith('bcr_') ||
          key === 'bcsort' ||
          key === 'bcpage'
        ) {
          next.searchParams.delete(key);
        }
      }

      Object.entries(state.filters).forEach(([field, values]) => {
        values.forEach((value) => next.searchParams.append(`bcf_${field}`, value));
      });

      Object.entries(state.ranges).forEach(([field, range]) => {
        if (range.min !== undefined && range.min !== null && range.min !== '') {
          next.searchParams.set(`bcr_${field}_min`, range.min);
        }
        if (range.max !== undefined && range.max !== null && range.max !== '') {
          next.searchParams.set(`bcr_${field}_max`, range.max);
        }
      });

      if (state.sort !== 'relevance') next.searchParams.set('bcsort', state.sort);
      if (state.page > 1) next.searchParams.set('bcpage', String(state.page));

      if (next.href !== window.location.href) history.pushState({}, '', next);
    }

    function setExternalMode(active) {
      document.documentElement.classList.toggle('bc-external-filters-active', active);
      nativeNodes.forEach((node) => {
        node.style.display = active ? 'none' : nativeDisplays.get(node);
      });
      [sidebar, toolbar, activeFilters, pagination, overlay].forEach((node) => {
        node.hidden = !active;
        node.style.display = active ? '' : 'none';
      });
      if (!active) {
        closeDrawer();
        if (externalActive) productGrid.replaceChildren(...nativeGridNodes);
        state.lastData = null;
      }
      externalActive = active;
    }

    async function runSearch() {
      const currentRequest = ++requestId;
      requestController?.abort();
      const controller = new AbortController();
      requestController = controller;
      const timeout = setTimeout(() => controller.abort(), 12000);
      setLoading(true);
      errorBox.hidden = true;

      try {
        const response = await fetch(`${apiBase}/api/v1/search`, {
          method: 'POST',
          mode: 'cors',
          credentials: 'omit',
          signal: controller.signal,
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            collection: collectionHandle,
            q: isSearch ? (new URL(window.location.href).searchParams.get('q') ?? root.dataset.searchQuery ?? '*') : '*',
            page: state.page,
            per_page: state.perPage,
            sort: state.sort,
            filters: state.filters,
            ranges: state.ranges
          })
        });
        if (!response.ok) throw new Error(`API antwoordde met ${response.status}`);
        const data = await response.json();
        if (currentRequest !== requestId) return;
        if (!Array.isArray(data.products) || !Array.isArray(data.facets) ||
            !Number.isInteger(data.found) || data.found < 0) {
          throw new Error('Ongeldig filterantwoord');
        }
        if (Number.isFinite(expectedCount) &&
            (!Number.isInteger(data.collection?.profile_products) ||
             data.collection.profile_products !== expectedCount)) {
          throw new Error('Filterindex en collectie komen niet overeen');
        }
        if (isSearch && data.collection?.handle !== '__all__') {
          throw new Error('Onjuiste zoekindex');
        }
        renderFilters(data.facets);
        renderActiveFilters(data.facets);
        renderProducts(data.products);
        hydrateCardTitles(data.products, currentRequest);
        renderCount(data.found);
        renderPagination(data.found);
        state.lastData = data;
        setExternalMode(true);
      } catch (error) {
        if (currentRequest !== requestId) return;
        console.error('[BadkamerCity filters]', error);
        setExternalMode(false);
        errorBox.textContent =
          'De uitgebreide filters zijn tijdelijk niet beschikbaar. Je kunt de gewone filters en productlijst blijven gebruiken.';
        errorBox.hidden = false;
      } finally {
        clearTimeout(timeout);
        if (currentRequest === requestId) setLoading(false);
      }
    }

    function renderFilters(facets) {
      const groups = sidebar.querySelector('[data-bc-filter-groups]');
      const openFields = new Set([...groups.querySelectorAll('details[open]')].map((group) => group.dataset.filterGroup));
      const focused = document.activeElement;
      const editing = groups.contains(focused) && focused.dataset.rangeField
        ? { field: focused.dataset.rangeField, kind: focused.dataset.rangeKind, value: focused.value }
        : null;

      groups.innerHTML = facets.map((facet, index) => {
        const field = facet.field;
        const selected = state.filters[field] || [];
        const range = state.ranges[field] || {};
        const isNumeric = ['number_integer', 'number_decimal'].includes(facet.type);
        const isOpen = filtersRendered ? openFields.has(field) : index < 5;

        if (isNumeric) {
          const scale = field === 'price_cents' ? 100 : 1;
          const rawMin = facet.min ?? facet.stats?.min;
          const rawMax = facet.max ?? facet.stats?.max;
          const min = rawMin == null ? '' : rawMin / scale;
          const max = rawMax == null ? '' : rawMax / scale;
          const unit = field === 'price_cents' ? '€' : facet.unit;
          const unitSuffix = unit && !String(facet.label).trim().endsWith(`(${unit})`)
            ? ` (${escapeHtml(unit)})` : '';
          const step = field === 'price_cents' ? '0.01' :
            (['int32', 'int64'].includes(facet.data_type) ? '1' : 'any');

          return `
            <details class="bc-filter-group" data-filter-group="${attr(field)}" ${isOpen ? 'open' : ''}>
              <summary>${escapeHtml(facet.label)}${unitSuffix}</summary>
              <div class="bc-filter-group__body">
                <div class="bc-filter-range">
                  <label>
                    Van
                    <input
                      type="number"
                      min="0"
                      step="${step}"
                      data-range-scale="${scale}"
                      data-range-field="${attr(field)}"
                      data-range-kind="min"
                      placeholder="${attr(min)}"
                      value="${attr(range.min == null ? '' : range.min / scale)}"
                    >
                  </label>
                  <label>
                    Tot
                    <input
                      type="number"
                      min="0"
                      step="${step}"
                      data-range-scale="${scale}"
                      data-range-field="${attr(field)}"
                      data-range-kind="max"
                      placeholder="${attr(max)}"
                      value="${attr(range.max == null ? '' : range.max / scale)}"
                    >
                  </label>
                </div>
              </div>
            </details>
          `;
        }

        const values = (facet.values || []).map((item) => {
          const rawValue = String(item.value);
          const checked = selected.includes(rawValue);
          const label = facet.type === 'boolean' || facet.data_type === 'bool'
            ? (rawValue === 'true' ? 'Ja' : 'Nee')
            : rawValue;

          return `
            <label class="bc-filter-option">
              <input
                type="checkbox"
                data-filter-field="${attr(field)}"
                value="${attr(rawValue)}"
                ${checked ? 'checked' : ''}
              >
              <span class="bc-filter-option__label">${escapeHtml(label)}</span>
              <span class="bc-filter-option__count">${Number(item.count || 0)}</span>
            </label>
          `;
        }).join('');

        if (!values) return '';

        return `
          <details class="bc-filter-group" data-filter-group="${attr(field)}" ${isOpen ? 'open' : ''}>
            <summary>${escapeHtml(facet.label)}</summary>
            <div class="bc-filter-group__body">${values}</div>
          </details>
        `;
      }).join('');
      filtersRendered = true;
      if (editing) {
        const replacement = [...groups.querySelectorAll('[data-range-field]')].find((input) =>
          input.dataset.rangeField === editing.field && input.dataset.rangeKind === editing.kind);
        if (replacement) {
          replacement.value = editing.value;
          replacement.focus({ preventScroll: true });
        }
      }
    }

    function renderActiveFilters(facets) {
      const labels = new Map(facets.map((facet) => [facet.field, facet.label]));
      const booleans = new Set(facets.filter((facet) => facet.data_type === 'bool' || facet.type === 'boolean').map((facet) => facet.field));
      const chips = [];

      Object.entries(state.filters).forEach(([field, values]) => {
        values.forEach((value) => {
          chips.push(`
            <button
              type="button"
              class="bc-filter-chip"
              data-chip-field="${attr(field)}"
              data-chip-value="${attr(value)}"
            >
              ${escapeHtml(labels.get(field) || field)}: ${escapeHtml(booleans.has(field) ? (value === 'true' ? 'Ja' : 'Nee') : value)}
            </button>
          `);
        });
      });

      Object.entries(state.ranges).forEach(([field, range]) => {
        if (range.min !== undefined || range.max !== undefined) {
          const text = [
            range.min !== undefined ? `vanaf ${field === 'price_cents' ? formatPrice(range.min) : range.min}` : '',
            range.max !== undefined ? `t/m ${field === 'price_cents' ? formatPrice(range.max) : range.max}` : ''
          ].filter(Boolean).join(' ');

          chips.push(`
            <button
              type="button"
              class="bc-filter-chip"
              data-chip-range="${attr(field)}"
            >
              ${escapeHtml(labels.get(field) || field)}: ${escapeHtml(text)}
            </button>
          `);
        }
      });

      activeFilters.innerHTML = chips.join('');
    }

    function renderProducts(products) {
      const cards = products.map((product) => {
        const href = productPath(product);
        const title = String(product.title || '').trim();
        const vendor = String(product.vendor || '').trim();
        const remainder = vendor && title.toLowerCase().startsWith(`${vendor.toLowerCase()} `)
          ? title.slice(vendor.length).trim() : title;
        const cardTitle = remainder || title;
        const image = product.image_url
          ? `<img src="${attr(product.image_url)}" alt="${attr(product.image_alt || product.title || '')}" loading="lazy" width="600" height="600">`
          : '';

        return `
          <li class="grid__item">
            <article class="bc-filter-card">
              <a class="bc-filter-card__media" href="${attr(href)}">
                ${image}
              </a>
              <div class="bc-filter-card__info">
                ${product.vendor ? `<p class="bc-filter-card__vendor">${escapeHtml(product.vendor)}</p>` : ''}
                <h3 class="bc-filter-card__title">
                  <a href="${attr(href)}" title="${attr(title)}">${escapeHtml(cardTitle)}</a>
                </h3>
                <dl class="bc-card-specs">
                  ${product.product_type ? `<div><dt>${escapeHtml(root.dataset.cardType || 'Productsoort')}:</dt><dd>${escapeHtml(product.product_type)}</dd></div>` : ''}
                  ${product.sku ? `<div><dt>${escapeHtml(root.dataset.cardSku || 'Artikelnummer')}:</dt><dd>${escapeHtml(product.sku)}</dd></div>` : ''}
                </dl>
                <div class="bc-filter-card__price">${formatPrice(product.price_cents)}</div>
                ${root.dataset.taxIncluded === 'true' ? `<span class="bc-card-tax">${escapeHtml(root.dataset.cardTax)}</span>` : ''}
                <a class="bc-card-view" href="${attr(href)}">${escapeHtml(root.dataset.cardView || 'Bekijk product')} <span aria-hidden="true">&rarr;</span></a>
              </div>
            </article>
          </li>
        `;
      }).join('');
      const empty = `<li class="grid__item bc-filter-empty" role="status">${escapeHtml(root.dataset.emptyLabel || 'Geen producten gevonden.')}</li>`;
      productGrid.innerHTML = isSearch
        ? `<ul class="grid product-grid" role="list">${cards || empty}</ul>`
        : cards || empty;
    }

    async function hydrateCardTitles(products, currentRequest) {
      if (!root.dataset.cardDataSection) return;
      const queue = [...products];
      const worker = async () => {
        while (queue.length && currentRequest === requestId) {
          const product = queue.shift();
          const href = productPath(product);
          if (!product.handle) continue;
          if (!cardDataCache.has(href)) {
            if (cardDataCache.size >= 200) cardDataCache.delete(cardDataCache.keys().next().value);
            cardDataCache.set(href, loadCardTitle(href));
          }
          const data = await cardDataCache.get(href);
          if (currentRequest !== requestId || !externalActive || !data) continue;
          if (String(data.id) !== String(product.shopify_product_id || product.id).split('/').pop()) continue;
          const link = [...productGrid.querySelectorAll('.bc-filter-card__title a')]
            .find((node) => node.getAttribute('href') === href);
          if (link && typeof data.short_title === 'string' && data.short_title.trim()) {
            link.textContent = data.short_title.trim();
          }
        }
      };
      await Promise.all(Array.from({ length: Math.min(4, queue.length) }, worker));
    }

    async function loadCardTitle(href) {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 5000);
      try {
        const url = new URL(href, window.location.origin);
        url.searchParams.set('sections', root.dataset.cardDataSection);
        const response = await fetch(url, { signal: controller.signal, credentials: 'omit' });
        if (!response.ok) return null;
        const sections = await response.json();
        const html = sections[root.dataset.cardDataSection];
        if (typeof html !== 'string') return null;
        const doc = new DOMParser().parseFromString(html, 'text/html');
        const data = doc.querySelector('[data-bc-card-data]');
        return data ? JSON.parse(data.textContent) : null;
      } catch (_) {
        return null;
      } finally {
        clearTimeout(timeout);
      }
    }

    function renderCount(found) {
      toolbar.querySelector('[data-bc-count]').textContent =
        `${found} ${found === 1 ? 'product' : 'producten'}`;
    }

    function renderPagination(found) {
      const totalPages = Math.max(1, Math.ceil(found / state.perPage));

      if (totalPages <= 1) {
        pagination.innerHTML = '';
        return;
      }

      pagination.innerHTML = `
        <button type="button" data-page="${state.page - 1}" ${state.page <= 1 ? 'disabled' : ''} aria-label="Vorige pagina">‹</button>
        <span class="bc-filter-pagination__status">Pagina ${state.page} van ${totalPages}</span>
        <button type="button" data-page="${state.page + 1}" ${state.page >= totalPages ? 'disabled' : ''} aria-label="Volgende pagina">›</button>
      `;
    }

    function onFilterChange(event) {
      const checkbox = event.target.closest('[data-filter-field]');

      if (checkbox) {
        const field = checkbox.dataset.filterField;
        const value = checkbox.value;
        const values = new Set(state.filters[field] || []);

        if (checkbox.checked) values.add(value);
        else values.delete(value);

        if (values.size) state.filters[field] = [...values];
        else delete state.filters[field];

        state.page = 1;
        syncUrl();
        runSearch();
        return;
      }

      const rangeInput = event.target.closest('[data-range-field]');

      if (rangeInput) {
        clearTimeout(rangeTimer);
        if (!rangeInput.checkValidity()) {
          rangeInput.reportValidity();
          return;
        }
        const field = rangeInput.dataset.rangeField;
        const kind = rangeInput.dataset.rangeKind;
        const value = rangeInput.value.trim();

        state.ranges[field] = state.ranges[field] || {};

        if (value === '') delete state.ranges[field][kind];
        else {
          const scale = Number(rangeInput.dataset.rangeScale) || 1;
          const numeric = Number(value) * scale;
          state.ranges[field][kind] = field === 'price_cents' ? Math.round(numeric) : numeric;
        }

        if (Object.keys(state.ranges[field]).length === 0) {
          delete state.ranges[field];
        }

        state.page = 1;
        syncUrl();
        runSearch();
      }
    }

    function onRangeInput(event) {
      const input = event.target.closest('[data-range-field]');
      if (!input) return;
      clearTimeout(rangeTimer);
      if (!input.checkValidity()) return;
      const field = input.dataset.rangeField;
      const kind = input.dataset.rangeKind;
      const value = input.value.trim();
      const scale = Number(input.dataset.rangeScale) || 1;
      state.ranges[field] = state.ranges[field] || {};
      if (value === '') delete state.ranges[field][kind];
      else state.ranges[field][kind] = field === 'price_cents'
        ? Math.round(Number(value) * scale) : Number(value) * scale;
      if (!Object.keys(state.ranges[field]).length) delete state.ranges[field];
      rangeTimer = setTimeout(() => {
        state.page = 1;
        syncUrl();
        runSearch();
      }, 300);
    }

    function onSidebarClick(event) {
      if (event.target.closest('[data-bc-clear-all]')) {
        clearTimeout(rangeTimer);
        state.filters = {};
        state.ranges = {};
        state.page = 1;
        syncUrl();
        runSearch();
      }
    }

    function onChipClick(event) {
      const chip = event.target.closest('.bc-filter-chip');
      if (!chip) return;

      if (chip.dataset.chipField) {
        const field = chip.dataset.chipField;
        const value = chip.dataset.chipValue;
        const values = (state.filters[field] || []).filter((item) => item !== value);

        if (values.length) state.filters[field] = values;
        else delete state.filters[field];
      }

      if (chip.dataset.chipRange) {
        clearTimeout(rangeTimer);
        delete state.ranges[chip.dataset.chipRange];
      }

      state.page = 1;
      syncUrl();
      runSearch();
    }

    function onPaginationClick(event) {
      const button = event.target.closest('[data-page]');
      if (!button || button.disabled) return;

      const nextPage = Number(button.dataset.page);
      if (!Number.isInteger(nextPage) || nextPage < 1) return;

      state.page = nextPage;
      syncUrl();
      runSearch();
      productContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function openDrawer() {
      document.documentElement.classList.add('bc-filter-drawer-open');
    }

    function closeDrawer() {
      document.documentElement.classList.remove('bc-filter-drawer-open');
    }

    function setLoading(loading) {
      productContainer.classList.toggle('bc-filter-loading', loading);
    }

    function formatPrice(cents) {
      if (cents === null || cents === undefined || Number.isNaN(Number(cents))) {
        return 'Prijs op aanvraag';
      }

      return new Intl.NumberFormat('nl-NL', {
        style: 'currency',
        currency: 'EUR'
      }).format(Number(cents) / 100);
    }

    function productPath(product) {
      if (product.handle) return `${window.Shopify?.routes?.root || '/'}products/${encodeURIComponent(product.handle)}`;

      if (product.product_url) {
        try {
          return new URL(product.product_url, window.location.origin).pathname;
        } catch (_) {
          return product.product_url;
        }
      }

      return '#';
    }

    function escapeHtml(value) {
      return String(value ?? '')
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');
    }

    function attr(value) {
      return escapeHtml(value);
    }
  });
})();
