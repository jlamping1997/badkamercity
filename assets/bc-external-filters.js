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

    const url = new URL(window.location.href);

    // Veilig testen op het live theme:
    // zonder ?bcfilters=1 verandert er helemaal niets.
    if (url.searchParams.get('bcfilters') !== '1') return;

    const apiBase = root.dataset.apiBase;
    const collectionHandle = root.dataset.collection;
    const sectionRoot = root.closest('.bc-collection');
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

    document.documentElement.classList.add('bc-external-filters-active');

    const nativeAside = sectionRoot.querySelector('#main-collection-filters');
    if (nativeAside) nativeAside.style.display = 'none';

    const nativeSort = sectionRoot.querySelector('facet-filters-form.facets-vertical-sort');
    if (nativeSort) nativeSort.style.display = 'none';

    const nativePagination = productContainer.querySelector('.pagination-wrapper');
    if (nativePagination) nativePagination.style.display = 'none';

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
    sidebar.addEventListener('click', onSidebarClick);
    activeFilters.addEventListener('click', onChipClick);
    pagination.addEventListener('click', onPaginationClick);

    toolbar.querySelector('[data-bc-open-filters]').addEventListener('click', openDrawer);
    sidebar.querySelector('.bc-filter-panel__close').addEventListener('click', closeDrawer);
    overlay.addEventListener('click', closeDrawer);

    sortSelect.addEventListener('change', () => {
      state.sort = sortSelect.value;
      state.page = 1;
      syncUrl();
      runSearch();
    });

    window.addEventListener('popstate', () => {
      resetState();
      parseStateFromUrl();
      sortSelect.value = state.sort;
      runSearch();
    });

    runSearch();

    function resetState() {
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

      history.replaceState({}, '', next);
    }

    async function runSearch() {
      setLoading(true);
      errorBox.hidden = true;

      try {
        const response = await fetch(`${apiBase}/api/v1/search`, {
          method: 'POST',
          mode: 'cors',
          credentials: 'omit',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            collection: collectionHandle,
            page: state.page,
            per_page: state.perPage,
            sort: state.sort,
            filters: state.filters,
            ranges: state.ranges
          })
        });

        if (!response.ok) {
          throw new Error(`API antwoordde met ${response.status}`);
        }

        const data = await response.json();
        state.lastData = data;

        renderFilters(data.facets || []);
        renderActiveFilters(data.facets || []);
        renderProducts(data.products || []);
        renderCount(data.found || 0);
        renderPagination(data.found || 0);
      } catch (error) {
        console.error('[BadkamerCity filters]', error);
        errorBox.textContent =
          'De filters konden niet worden geladen. De normale productweergave blijft beschikbaar.';
        errorBox.hidden = false;
      } finally {
        setLoading(false);
      }
    }

    function renderFilters(facets) {
      const groups = sidebar.querySelector('[data-bc-filter-groups]');

      groups.innerHTML = facets.map((facet, index) => {
        const field = facet.field;
        const selected = state.filters[field] || [];
        const range = state.ranges[field] || {};
        const isNumeric = ['number_integer', 'number_decimal'].includes(facet.type);

        if (isNumeric) {
          const min = facet.min ?? facet.stats?.min ?? '';
          const max = facet.max ?? facet.stats?.max ?? '';

          return `
            <details class="bc-filter-group" ${index < 5 ? 'open' : ''}>
              <summary>${escapeHtml(facet.label)}${facet.unit ? ` (${escapeHtml(facet.unit)})` : ''}</summary>
              <div class="bc-filter-group__body">
                <div class="bc-filter-range">
                  <label>
                    Van
                    <input
                      type="number"
                      step="any"
                      data-range-field="${attr(field)}"
                      data-range-kind="min"
                      placeholder="${attr(min)}"
                      value="${attr(range.min ?? '')}"
                    >
                  </label>
                  <label>
                    Tot
                    <input
                      type="number"
                      step="any"
                      data-range-field="${attr(field)}"
                      data-range-kind="max"
                      placeholder="${attr(max)}"
                      value="${attr(range.max ?? '')}"
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
          const label = facet.type === 'boolean'
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
          <details class="bc-filter-group" ${index < 5 ? 'open' : ''}>
            <summary>${escapeHtml(facet.label)}</summary>
            <div class="bc-filter-group__body">${values}</div>
          </details>
        `;
      }).join('');
    }

    function renderActiveFilters(facets) {
      const labels = new Map(facets.map((facet) => [facet.field, facet.label]));
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
              ${escapeHtml(labels.get(field) || field)}: ${escapeHtml(value)}
            </button>
          `);
        });
      });

      Object.entries(state.ranges).forEach(([field, range]) => {
        if (range.min !== undefined || range.max !== undefined) {
          const text = [
            range.min !== undefined ? `vanaf ${range.min}` : '',
            range.max !== undefined ? `t/m ${range.max}` : ''
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
      productGrid.innerHTML = products.map((product) => {
        const href = productPath(product);
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
                  <a href="${attr(href)}">${escapeHtml(product.title || '')}</a>
                </h3>
                <div class="bc-filter-card__price">${formatPrice(product.price_cents)}</div>
              </div>
            </article>
          </li>
        `;
      }).join('');
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
        const field = rangeInput.dataset.rangeField;
        const kind = rangeInput.dataset.rangeKind;
        const value = rangeInput.value.trim();

        state.ranges[field] = state.ranges[field] || {};

        if (value === '') delete state.ranges[field][kind];
        else state.ranges[field][kind] = Number(value);

        if (Object.keys(state.ranges[field]).length === 0) {
          delete state.ranges[field];
        }

        state.page = 1;
        syncUrl();
        runSearch();
      }
    }

    function onSidebarClick(event) {
      if (event.target.closest('[data-bc-clear-all]')) {
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
      if (product.handle) return `/products/${encodeURIComponent(product.handle)}`;

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
