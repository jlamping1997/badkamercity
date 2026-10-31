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
    let nativeFallback = false;
    let requestId = 0;
    let requestController;
    let filtersRendered = false;
    let rangeTimer;

    const drawerMedia = window.matchMedia('(max-width: 989px)');
    let drawerTrigger;

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
    sidebar.id = 'BcFilterDrawer';
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
        <button type="button" class="bc-filter-mobile-button" aria-controls="BcFilterDrawer" aria-expanded="false" data-bc-open-filters>
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
      if (!document.documentElement.classList.contains('bc-filter-drawer-open')) return;
      if (event.key === 'Escape') { event.preventDefault(); closeDrawer(); }
      if (event.key === 'Tab') {
        const focusable = [...sidebar.querySelectorAll('button, input, select, summary, a[href]')]
          .filter((node) => !node.disabled && node.getClientRects().length);
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (event.shiftKey && (document.activeElement === first || !sidebar.contains(document.activeElement))) {
          event.preventDefault(); last?.focus();
        } else if (!event.shiftKey && (document.activeElement === last || !sidebar.contains(document.activeElement))) {
          event.preventDefault(); first?.focus();
        }
      }
    });

    sortSelect.addEventListener('change', () => {
      state.sort = sortSelect.value;
      state.page = 1;
      syncUrl();
      runSearch();
    });

    window.addEventListener('popstate', (event) => {
      if (nativeFallback) return;
      if (externalActive) event.stopImmediatePropagation();
      resetState();
      parseStateFromUrl();
      sortSelect.value = state.sort;
      runSearch();
    }, { capture: true });

    drawerMedia.addEventListener('change', () => { closeDrawer(); syncDrawerAccessibility(); });
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
      syncDrawerAccessibility();
    }

    async function runSearch() {
      if (nativeFallback) return;
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
        const aliases = data.filter_policy?.color_value_aliases || {};
        if (state.filters.f_kleur) state.filters.f_kleur = [...new Set(state.filters.f_kleur.map(v => aliases[v] || v))];
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
        nativeFallback = true;
        clearTimeout(rangeTimer);
        setExternalMode(false);
        errorBox.textContent =
          'De uitgebreide filters zijn tijdelijk niet beschikbaar. Je kunt de gewone filters en productlijst blijven gebruiken.';
        errorBox.hidden = false;
      } finally {
        clearTimeout(timeout);
        if (currentRequest === requestId) setLoading(false);
      }
    }

    const filterMemory = new Map();
    const cardModels = new WeakMap();
    const choiceCache = new Map();
    const uiText = (key, fallback) => root.dataset[key] || fallback;

    function swatch(value, imageUrl = '') {
      if (imageUrl) {
        try {
          const asset = new URL(imageUrl, location.origin);
          if ((asset.origin === location.origin || asset.hostname === 'cdn.shopify.com') &&
              /^https?:$/.test(asset.protocol) && /\/bc-wiesbaden-swatch-[a-z0-9]+(?:-[a-z0-9]+)*\.svg$/.test(asset.pathname)) {
            return `url("${asset.href}") center / cover`;
          }
        } catch (_) { /* Keep the named-color fallback. */ }
      }
      const name = String(value || '').toLowerCase();
      if (/zwart|black/.test(name)) return 'linear-gradient(120deg,#1e2023,#45474a,#151719)';
      if (/gun.?metal|verouderd ijzer/.test(name)) return 'linear-gradient(120deg,#747578,#43474c,#97999a)';
      if (/koper|copper|brons|bronze/.test(name)) return 'linear-gradient(120deg,#916647,#d7ac85,#78513e)';
      if (/messing|goud|gold|brass/.test(name)) return 'linear-gradient(120deg,#a98137,#dfc57d,#a27935)';
      if (/wit|white/.test(name)) return '#f8f8f6';
      if (/rvs|staal|steel|nikkel|chroom|chrome|zilver/.test(name)) return 'linear-gradient(120deg,#8b9093,#ebeded,#a3a7aa)';
      if (/beige|zand|sand/.test(name)) return '#cfbfa8';
      if (/grijs|grey|gray/.test(name)) return '#93979b';
      if (/eik|oak|hout/.test(name)) return 'linear-gradient(100deg,#ac8960,#d4b78e,#b39067)';
      if (/blauw|blue/.test(name)) return '#6f8ea7';
      if (/groen|green/.test(name)) return '#81957b';
      if (/roze|pink/.test(name)) return '#d8aeb5';
      return 'linear-gradient(135deg,#e8e4df,#b7b2ad)';
    }

    function renderFilters(facets) {
      const groups = sidebar.querySelector('[data-bc-filter-groups]');
      for (const node of groups.querySelectorAll('[data-filter-group]')) {
        filterMemory.set(node.dataset.filterGroup, { open: node.open,
          expanded: node.dataset.expanded === 'true' });
      }
      const active = document.activeElement;
      const focused = groups.contains(active) && active.matches('[data-range-field]') ? {field: active.dataset.rangeField, kind: active.dataset.rangeKind} : null;
      const moreOpen = groups.querySelector('[data-bc-more-filters]')?.open;
      const render = (facet) => {
        const field = facet.field;
        const ui = facet.ui || {};
        const memory = filterMemory.get(field);
        const selected = state.filters[field] || [];
        const range = state.ranges[field] || {};
        const numeric = ['number_integer', 'number_decimal'].includes(facet.type);
        const exact = ui.control === 'single_select';
        const scale = Number(ui.display_divisor) || (field === 'price_cents' ? 100 : 1);
        const unit = ui.display_unit || (field === 'price_cents' ? '€' : facet.unit) || '';
        const label = `${facet.label}${unit && unit !== '€' && !String(facet.label).includes(`(${unit})`) ? ` (${unit})` : ''}`;
        const selectedCount = selected.length || (range.min != null || range.max != null ? 1 : 0);
        const open = memory ? memory.open : Boolean(ui.default_open || selectedCount);
        let body;
        if (numeric && !exact) {
          const min = facet.min ?? facet.stats?.min;
          const max = facet.max ?? facet.stats?.max;
          body = `<div class="bc-filter-range">${['min', 'max'].map((kind, i) => `<label>${i ? 'Tot' : 'Van'}${unit === '€' ? ' (€)' : ''}<input type="number" min="0" step="${scale > 1 ? '0.1' : '1'}" data-range-scale="${scale}" data-range-field="${attr(field)}" data-range-kind="${kind}" value="${range[kind] == null ? '' : attr(range[kind] / scale)}" placeholder="${attr((i ? max : min) == null ? '' : (i ? max : min) / scale)}"></label>`).join('')}</div>`;
        } else {
          let values = (facet.values || []).map(v => ({value: String(v.value), count: Number(v.count) || 0, raw: [String(v.value)]}));
          if (ui.option_groups?.length) {
            const seen = new Set();
            const merged = ui.option_groups.map(g => {
              const members = values.filter(v => g.exact_values.includes(v.value));
              members.forEach(v => seen.add(v.value));
              return {value: g.label, count: members.reduce((n,v) => n + v.count, 0), raw: g.exact_values};
            }).filter(v => v.count || v.raw.some(x => selected.includes(x)));
            values = [...merged, ...values.filter(v => !seen.has(v.value))];
          }
          values.sort((a,b) => numeric ? Number(a.value)-Number(b.value) : a.value.localeCompare(b.value,'nl',{numeric:true}));
          const limit = Math.max(1, Math.floor(Number(ui.visible_values) || 6));
          body = '';
          body += `<div class="bc-filter-options">${values.map((v,i) => {
            const checked = exact ? range.min === Number(v.value) && range.max === Number(v.value) : v.raw.some(x => selected.includes(x));
            const text = facet.data_type === 'bool' ? (v.value === 'true' ? 'Ja' : 'Nee') : exact ? String(Number(v.value)/scale) : v.value;
            return `<label class="bc-filter-option${field === 'f_kleur' ? ' bc-filter-option--color' : ''}" data-option-index="${i}" data-option-label="${attr(text.toLowerCase())}" data-option-selected="${checked}" ${!checked && i >= limit && !memory?.expanded ? 'hidden' : ''}>
              <input type="checkbox" ${exact ? `data-exact-field="${attr(field)}"` : `data-filter-field="${attr(field)}" data-filter-values="${attr(JSON.stringify(v.raw))}"`} value="${attr(v.value)}" ${checked ? 'checked' : ''} ${!v.count && !checked ? 'disabled' : ''}>
              ${field === 'f_kleur' ? `<span class="bc-color-dot" aria-hidden="true" style="--bc-swatch:${swatch(v.value)}"></span>` : ''}<span class="bc-filter-option__label">${escapeHtml(text)}</span><span class="bc-filter-option__count">${v.count}</span></label>`;
          }).join('')}</div>`;
          if (values.length > limit) body += `<button type="button" class="bc-filter-more" data-bc-show-values data-bc-visible-values="${limit}" aria-expanded="${Boolean(memory?.expanded)}">${escapeHtml(memory?.expanded ? uiText('labelLess','Toon minder') : uiText('labelMore','Toon meer'))}</button>`;
        }
        return `<details class="bc-filter-group" data-filter-group="${attr(field)}" data-expanded="${Boolean(memory?.expanded)}" ${open ? 'open' : ''}><summary>${escapeHtml(label)}${selectedCount ? `<span class="bc-filter-selected-count">${selectedCount}</span>` : ''}</summary><div class="bc-filter-group__body">${body}</div></details>`;
      };
      const primary = facets.filter(f => f.ui?.section !== 'more' || ['f_serie','vendor','price_cents'].includes(f.field));
      const more = facets.filter(f => !primary.includes(f));
      const moreActive = more.some(f => state.filters[f.field]?.length || state.ranges[f.field]);
      groups.innerHTML = primary.map(render).join('') + (more.length ? `<details class="bc-filter-more-group" data-bc-more-filters ${moreOpen || moreActive ? 'open' : ''}><summary>${escapeHtml(uiText('labelMoreFilters','Meer filters'))}</summary>${more.map(render).join('')}</details>` : '');
      filtersRendered = true;
      if (focused) {
        const replacement = [...groups.querySelectorAll('[data-range-field]')].find(n => n.dataset.rangeField === focused.field && n.dataset.rangeKind === focused.kind);
        replacement?.focus({preventScroll:true});
      }
    }

    sidebar.addEventListener('change', event => {
      const input = event.target.closest('[data-exact-field]');
      if (!input) return;
      const value = Number(input.value);
      if (input.checked) state.ranges[input.dataset.exactField] = {min:value,max:value};
      else delete state.ranges[input.dataset.exactField];
      state.page = 1; syncUrl(); runSearch();
    });
    sidebar.addEventListener('click', event => {
      const more = event.target.closest('[data-bc-show-values]');
      if (!more) return;
      const group = more.closest('[data-filter-group]');
      const expanded = group.dataset.expanded !== 'true';
      group.dataset.expanded = String(expanded);
      more.setAttribute('aria-expanded', String(expanded));
      more.textContent = expanded ? uiText('labelLess','Toon minder') : uiText('labelMore','Toon meer');
      const limit = Math.max(1, Number(more.dataset.bcVisibleValues) || 6);
      for (const option of group.querySelectorAll('[data-option-label]')) option.hidden = !expanded && option.dataset.optionSelected !== 'true' && Number(option.dataset.optionIndex) >= limit;
    });


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
          const descriptor = facets.find(f => f.field === field);
          const scale = Number(descriptor?.ui?.display_divisor) || 1;
          const unit = descriptor?.ui?.display_unit || descriptor?.unit || '';
          const show = v => field === 'price_cents' ? formatPrice(v) : `${new Intl.NumberFormat('nl-NL').format(v/scale)}${unit ? ' '+unit : ''}`;
          const text = range.min != null && range.min === range.max ? show(range.min) : [
            range.min != null ? `vanaf ${show(range.min)}` : '',
            range.max != null ? `t/m ${show(range.max)}` : ''
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

    function canonicalColor(value) {
      return /^(rvs|rvs geborsteld|geborsteld rvs)$/i.test(String(value || '').trim()) ? 'Geborsteld RVS' : String(value || '');
    }

    function productTitle(product, data = {}) {
      let title = String(data.short_title || data.title || product.title || '').trim();
      const vendor = String(data.vendor || product.vendor || '').trim();
      if (vendor && title.toLowerCase().startsWith(vendor.toLowerCase()+' ')) title = title.slice(vendor.length).trim();
      const color = String(data.color || '').trim();
      for (const separator of [' – ', ' - ']) {
        if (color && title.toLowerCase().endsWith(separator+color.toLowerCase())) title = title.slice(0,-color.length-separator.length).trim();
      }
      return title;
    }

    function renderProducts(products) {
      const cards = products.map(product => {
        const href = productPath(product);
        return `<li class="grid__item"><article class="bc-filter-card" data-bc-card-handle="${attr(product.handle)}">
          <a class="bc-filter-card__media" href="${attr(href)}" tabindex="-1" aria-hidden="true">${product.image_url ? `<img src="${attr(product.image_url)}" alt="${attr(product.title)}" loading="lazy" width="600" height="600">` : ''}</a>
          <div class="bc-filter-card__info"><p class="bc-filter-card__vendor">${escapeHtml(product.vendor || '')}</p>
          <h3 class="bc-filter-card__title"><a href="${attr(href)}" title="${attr(product.title)}">${escapeHtml(productTitle(product))}</a></h3>
          <p class="bc-card-color" aria-live="polite"></p><div class="bc-card-colors" data-bc-card-colors></div>
          <div class="bc-card-buy"><div class="bc-filter-card__price">${formatPrice(product.price_cents)}</div>${root.dataset.taxIncluded === 'true' ? `<span class="bc-card-tax">${escapeHtml(root.dataset.cardTax || 'incl. btw')}</span>` : ''}
          <p class="bc-card-delivery" data-bc-card-delivery>${escapeHtml(root.dataset.cardDelivery || '')}</p>
          <div class="bc-card-actions"><a class="bc-card-view" href="${attr(href)}">${escapeHtml(root.dataset.cardView || 'Bekijk product')} <span aria-hidden="true">→</span></a><button type="button" class="bc-card-cart" data-bc-card-cart disabled aria-label="${attr(uiText('labelAdd','In winkelwagen'))}"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M2 3h3l2.3 12h11.5l2.2-9H6M9 20h.01M18 20h.01" stroke-linecap="round" stroke-linejoin="round"/><circle cx="9" cy="20" r="1"/><circle cx="18" cy="20" r="1"/></svg></button></div></div>
          <p class="bc-card-feedback" role="status"></p></div></article></li>`;
      }).join('');
      const empty = `<li class="grid__item bc-filter-empty" role="status">${escapeHtml(root.dataset.emptyLabel || 'Geen producten gevonden.')}</li>`;
      productGrid.innerHTML = isSearch ? `<ul class="grid product-grid" role="list">${cards || empty}</ul>` : cards || empty;
      const elements = [...productGrid.querySelectorAll('.bc-filter-card')];
      products.forEach((product,i) => cardModels.set(elements[i], {product, data:null, options:[], version:0}));
    }

    async function cardData(href) {
      if (!cardDataCache.has(href)) {
        if (cardDataCache.size >= 200) cardDataCache.delete(cardDataCache.keys().next().value);
        cardDataCache.set(href, loadCardTitle(href).then(data => { if (!data) cardDataCache.delete(href); return data; }));
      }
      return cardDataCache.get(href);
    }

    function updateCard(card, data) {
      const model = cardModels.get(card);
      if (!model || !data) return;
      model.data = data;
      model.product = {...model.product,handle:data.handle,title:data.title,price_cents:data.price_cents,image_url:data.image_url};
      const href = productPath(model.product);
      card.dataset.bcCardHandle = data.handle;
      card.querySelectorAll('a').forEach(a => a.href = href);
      const title = card.querySelector('.bc-filter-card__title a');
      title.textContent = productTitle(model.product,data);
      title.title = data.title;
      const media = card.querySelector('.bc-filter-card__media');
      media.classList.remove('bc-card-media--hover-ready');
      media.querySelector('[data-bc-card-hover]')?.remove();
      if (data.image_url) {
        let image = media.querySelector('img');
        if (!image) { image = document.createElement('img'); image.width=600;image.height=600;media.append(image); }
        image.src=data.image_url; image.alt=data.title; image.loading='lazy';
      } else media.replaceChildren();
      if (window.matchMedia('(hover: hover) and (pointer: fine)').matches && data.image_url && data.hover_image_url && data.hover_image_url !== data.image_url) {
        const hoverImage=document.createElement('img');
        hoverImage.dataset.bcCardHover='';hoverImage.alt='';hoverImage.setAttribute('aria-hidden','true');
        hoverImage.width=600;hoverImage.height=600;hoverImage.loading='lazy';hoverImage.decoding='async';
        hoverImage.addEventListener('load',()=>{if(hoverImage.parentElement===media)media.classList.add('bc-card-media--hover-ready');},{once:true});
        hoverImage.addEventListener('error',()=>{if(hoverImage.parentElement===media)media.classList.remove('bc-card-media--hover-ready');},{once:true});
        hoverImage.src=data.hover_image_url;media.append(hoverImage);
        if(hoverImage.complete && hoverImage.naturalWidth)media.classList.add('bc-card-media--hover-ready');
      }
      const delivery=card.querySelector('[data-bc-card-delivery]');
      delivery.textContent=data.delivery_text || root.dataset.cardDelivery || '';
      delivery.classList.toggle('bc-card-delivery--stock',data.delivery_in_stock===true);
      card.querySelector('.bc-card-color').textContent = canonicalColor(data.color);
      card.querySelector('.bc-filter-card__price').textContent = formatPrice(data.price_cents);
      const cart = card.querySelector('[data-bc-card-cart]');
      cart.disabled = !data.available;
      cart.setAttribute('aria-label', `${uiText('labelAdd','In winkelwagen')}: ${data.title}`);
      const wish = card.querySelector('[data-bc-wishlist-toggle]');
      if (wish) {
        wish.dataset.bcWishlistHandle=data.handle;wish.dataset.bcWishlistVariant=String(data.variant_id || '');
        wish.dataset.bcWishlistTitle=data.title;wish.dataset.bcWishlistImage=data.image_url || '';
      }
      window.BCWishlist?.refresh();
      renderCardColors(card);
    }

    async function hydrateCardTitles(products, currentRequest) {
      if (!root.dataset.cardDataSection) return;
      const cards = [...productGrid.querySelectorAll('.bc-filter-card')];
      const queue = cards.map((card,i) => ({card,product:products[i]}));
      const worker = async () => {
        while (queue.length && currentRequest === requestId) {
          const {card,product}=queue.shift();
          const data=await cardData(productPath(product));
          if (currentRequest !== requestId || !card.isConnected || !data) continue;
          if (String(data.id) !== String(product.shopify_product_id || product.id).split('/').pop()) continue;
          updateCard(card,data);
          loadCardColors(card,data).catch(() => {});
        }
      };
      await Promise.all(Array.from({length:Math.min(4,queue.length)},worker));
    }

    async function loadCardColors(card,data) {
      if (!data.switcher_html) return;
      const doc=new DOMParser().parseFromString(data.switcher_html,'text/html');
      const source=doc.querySelector('[data-bc-product-switcher-v2]');
      if (!source) return;
      const inline = source.querySelector('[data-bc-switcher-inline]');
      let payload;
      if (inline) {
        try { payload = JSON.parse(inline.textContent); } catch (_) { return; }
      } else {
        if (!source.dataset.switcherDataUrl) return;
        const url=new URL(source.dataset.switcherDataUrl,location.origin);
        if (url.origin !== location.origin && url.hostname !== 'cdn.shopify.com') return;
        if (!choiceCache.has(url.href)) {
          const promise=fetch(url.href,{credentials:'omit'}).then(r=>{if(!r.ok)throw new Error('Kleuren niet beschikbaar');return r.json();}).catch(e=>{choiceCache.delete(url.href);throw e;});
          choiceCache.set(url.href,promise);
        }
        payload=await choiceCache.get(url.href);
      }
      if (!payload || typeof payload !== 'object') return;
      const groups=Array.isArray(payload.groups) ? payload.groups : Object.values(payload.groups || {});
      const group=groups.find(g=>g.id===source.dataset.switchGroup);
      if (!group || !Array.isArray(group.products)) return;
      const current=group.products.find(p=>p.handle===data.handle);
      const menu=(group.menus || []).find(m=>/^(kleur|basiskleur|color|colour)$/i.test(m.key));
      if (!current || !menu) return;
      if (!data.color && current.options?.[menu.key]) {
        data.color=current.options[menu.key];
        card.querySelector('.bc-card-color').textContent=canonicalColor(data.color);
        card.querySelector('.bc-filter-card__title a').textContent=productTitle(cardModels.get(card).product,data);
      }
      const options=group.products.filter(p=>p.handle && p.options?.[menu.key] && Object.entries(current.options || {}).every(([key,value])=>key===menu.key || p.options?.[key]===value));
      const unique=[];const seen=new Set();
      for(const option of options){const color=canonicalColor(option.options[menu.key]);if(!seen.has(color)){seen.add(color);unique.push({...option,color});}}
      const model=cardModels.get(card);
      if (!model || !card.isConnected) return;
      model.colorGroup=group.id;
      model.allColorsLabel=source.dataset.labelAllColors || '';
      model.options=unique.length>1 ? unique : [];
      renderCardColors(card);
    }

    function renderCardColors(card) {
      const model=cardModels.get(card);if(!model)return;
      const row=card.querySelector('[data-bc-card-colors]');
      const selected=model.product.handle;
      const compact=window.matchMedia('(max-width: 749px)').matches;
      const width=Math.max(0,(row.clientWidth || 180)-(compact ? 0 : 6));
      const slot=compact ? 36 : 30;
      const moreWidth=compact ? 34 : 38;
      const allFit=Math.floor((width+(compact ? 0 : 7))/slot);
      const limit=model.options.length<=Math.min(4,allFit) ? model.options.length : Math.min(4,Math.max(1,Math.floor((width-moreWidth)/slot)));
      const visible=model.options.slice(0,limit);
      const active=model.options.find(option=>option.handle===selected);
      if(active && !visible.includes(active) && visible.length)visible[visible.length-1]=active;
      const hidden=model.options.length-visible.length;
      let more='';
      if(hidden>0){
        const url=new URL(productPath(model.product),location.origin);
        url.searchParams.set('bc_colors',model.colorGroup);
        url.hash='bc-product-colors';
        const label=model.allColorsLabel ? model.allColorsLabel.replace('__COUNT__',String(model.options.length)) : `${uiText('labelMore','Toon meer')} (${hidden})`;
        more=`<a class="bc-card-color-more" data-bc-card-more-colors href="${attr(url.pathname+url.search+url.hash)}" aria-label="${attr(label)}" title="${attr(label)}">+${hidden}</a>`;
      }
      row.innerHTML=visible.map(option=>`<button type="button" class="bc-card-swatch" data-bc-card-color="${attr(option.handle)}" aria-label="${attr(option.color)}" title="${attr(option.color)}" aria-pressed="${option.handle===selected}" style="--bc-swatch:${attr(swatch(option.color, model.colorGroup?.startsWith('wiesbaden-colors-') ? option.swatch_url : ''))}"><span class="visually-hidden">${escapeHtml(option.color)}</span></button>`).join('')+more;
    }

    let colorResizeFrame;
    window.addEventListener('resize',()=>{
      if(colorResizeFrame)cancelAnimationFrame(colorResizeFrame);
      colorResizeFrame=requestAnimationFrame(()=>productGrid.querySelectorAll('.bc-filter-card').forEach(renderCardColors));
    },{passive:true});

    let cardPointer=null;
    productGrid.addEventListener('pointerdown',e=>{cardPointer={x:e.clientX,y:e.clientY,moved:false};},{passive:true});
    productGrid.addEventListener('pointermove',e=>{if(cardPointer && Math.hypot(e.clientX-cardPointer.x,e.clientY-cardPointer.y)>8)cardPointer.moved=true;},{passive:true});
    productGrid.addEventListener('pointercancel',()=>{if(cardPointer)cardPointer.moved=true;},{passive:true});
    productGrid.addEventListener('click',async event=>{
      const card=event.target.closest('.bc-filter-card');if(!card)return;
      if(cardPointer?.moved && event.detail){event.preventDefault();event.stopPropagation();cardPointer=null;return;}
      cardPointer=null;
      const model=cardModels.get(card);if(!model)return;
      const color=event.target.closest('[data-bc-card-color]');
      if(color){
        event.preventDefault();event.stopPropagation();
        const option=model.options.find(p=>p.handle===color.dataset.bcCardColor);if(!option)return;
        const version=++model.version;
        card.setAttribute('aria-busy','true');
        card.querySelector('[data-bc-card-cart]').disabled=true;
        try {
          const data=await cardData(productPath(option));
          if(!data || data.handle!==option.handle)throw new Error('Kleur niet beschikbaar');
          if(model.version===version && card.isConnected){updateCard(card,data);card.querySelector('.bc-card-feedback').textContent='';}
        }catch(_){if(model.version===version){card.querySelector('.bc-card-feedback').textContent=uiText('labelColorError','Deze kleur kon niet worden geladen. Probeer opnieuw.');if(model.data)updateCard(card,model.data);}}
        finally{if(model.version===version)card.removeAttribute('aria-busy');}
        return;
      }
      const cart=event.target.closest('[data-bc-card-cart]');
      if(cart){
        event.preventDefault();event.stopPropagation();
        if(cart.disabled || !model.data)return;
        const data=model.data;
        if(!data.can_add){location.assign(productPath(model.product));return;}
        const notification=document.querySelector('cart-notification') || document.querySelector('cart-drawer');
        const sections=notification?.getSectionsToRender?.().map(x=>x.id) || ['cart-icon-bubble'];
        cart.disabled=true;cart.setAttribute('aria-busy','true');
        const feedback=card.querySelector('.bc-card-feedback');
        try {
          const response=await fetch(`${window.Shopify?.routes?.root || '/'}cart/add.js`,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify({items:[{id:data.variant_id,quantity:1}],sections,sections_url:location.pathname})});
          const result=await response.json();
          if(!response.ok || result.status)throw new Error(result.description || uiText('labelCartError','Toevoegen is niet gelukt. Probeer opnieuw.'));
          feedback.textContent=uiText('labelAdded','Toegevoegd aan je winkelwagen');
          try {notification?.setActiveElement?.(cart);notification?.renderContents?.({...result.items?.[0],...result,sections:result.sections});}catch(_){ }
        }catch(error){feedback.textContent=error.message;}
        finally{cart.disabled=!model.data?.available;cart.removeAttribute('aria-busy');}
        return;
      }
      if(event.target.closest('a,button,input,select,summary,label') || event.ctrlKey || event.metaKey || event.shiftKey || String(window.getSelection()).trim())return;
      location.assign(productPath(model.product));
    });


    async function loadCardTitle(href) {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 5000);
      try {
        const url = new URL(href, window.location.origin);
        url.searchParams.set('sections', root.dataset.cardDataSection);
        const previewTheme = new URL(location.href).searchParams.get('preview_theme_id');
        if (previewTheme) url.searchParams.set('preview_theme_id', previewTheme);
        const response = await fetch(url, { signal: controller.signal, credentials: 'same-origin' });
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
        const chosen = checkbox.dataset.filterValues ? JSON.parse(checkbox.dataset.filterValues) : [checkbox.value];
        const values = new Set(state.filters[field] || []);
        chosen.forEach(value => { if (checkbox.checked) values.add(value); else values.delete(value); });

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

    function syncDrawerAccessibility() {
      const open = document.documentElement.classList.contains('bc-filter-drawer-open');
      sidebar.inert = drawerMedia.matches && !open;
      if (drawerMedia.matches) {
        sidebar.setAttribute('role', 'dialog');
        sidebar.setAttribute('aria-modal', 'true');
      } else {
        sidebar.removeAttribute('role');
        sidebar.removeAttribute('aria-modal');
      }
      toolbar.querySelector('[data-bc-open-filters]').setAttribute('aria-expanded', String(open));
    }

    function openDrawer() {
      if (!externalActive || !drawerMedia.matches) return;
      drawerTrigger = document.activeElement;
      document.documentElement.classList.add('bc-filter-drawer-open');
      syncDrawerAccessibility();
      sidebar.querySelector('.bc-filter-panel__close').focus({ preventScroll: true });
    }

    function closeDrawer() {
      const wasOpen = document.documentElement.classList.contains('bc-filter-drawer-open');
      document.documentElement.classList.remove('bc-filter-drawer-open');
      syncDrawerAccessibility();
      if (wasOpen && drawerTrigger?.isConnected) drawerTrigger.focus({ preventScroll: true });
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
