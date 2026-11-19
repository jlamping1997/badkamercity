(function () {
  const ROOT_SELECTOR = '[data-bc-product-switcher-v2]';
  const DEFAULT_DATA_URL = '/assets/product-switcher-data.json';
  const BUTTON_THRESHOLD = 5;
  const HOTBATH_SWATCHES = {
    'chroom': 'cr',
    'geborsteld nikkel': 'gn',
    'geborsteld messing': 'bb',
    'verouderd messing': 'ab',
    'mat wit': 'wh',
    'verouderd ijzer': 'ai',
    'gepolijst zwart pvd': 'pbp',
    'geborsteld zwart pvd': 'mbp',
    'geborsteld messing pvd': 'bbp',
    'geborsteld koper pvd': 'bcp',
    'geborsteld gunmetal pvd': 'bgp',
    'rvs 316': 'ix',
    'tuscan bronze': 'tb'
  };

  function isColorMenu(menu) {
    return /^(kleur|basiskleur|color|colour)$/i.test(normalize(menu.key));
  }

  function swatchUrl(value, urls) {
    const code = HOTBATH_SWATCHES[normalize(value).toLowerCase()];
    if (!code || !urls[code]) return '';
    try {
      const pageOrigin = window.location.origin === 'null' ? new URL(document.baseURI).origin : window.location.origin;
      const url = new URL(urls[code], pageOrigin);
      return url.protocol === 'https:' &&
        (url.origin === pageOrigin || url.hostname === 'cdn.shopify.com') ? url.href : '';
    } catch (_) {
      return '';
    }
  }

  let dataPromise;

  function createSwitcherPositionKeeper(window, document) {
    const storageKey = 'bc:product-switcher:position:v1';
    const ttl = 30000;
    const maxRestoreTime = 15000;
    const settleTime = 2000;
    const inputEvents = ['pointerdown', 'touchstart', 'wheel', 'keydown'];

    function optedIn(root) {
      return root?.dataset?.bcPreservePosition === 'true';
    }

    function routeKey(value) {
      try {
        const url = new URL(value, window.location.origin);
        if (url.origin !== window.location.origin || !url.pathname.includes('/products/')) return null;
        url.searchParams.delete('preview_theme_id');
        url.searchParams.sort();
        return url.pathname + url.search + url.hash;
      } catch (_) {
        return null;
      }
    }

    function discard(token) {
      if (!token) return;
      try {
        const saved = JSON.parse(window.sessionStorage.getItem(storageKey) || 'null');
        if (saved?.savedAt === token.savedAt && saved?.group === token.group && saved?.target === token.target) {
          window.sessionStorage.removeItem(storageKey);
        }
      } catch (_) {}
    }

    function remember(root, destination) {
      if (!optedIn(root)) return null;
      const target = routeKey(destination);
      const group = String(root.dataset.switchGroup || '').trim();
      if (!target || !group) return null;
      let token;
      try {
        const top = root.getBoundingClientRect().top;
        if (!Number.isFinite(top)) return null;
        token = { version: 1, group, target, top, savedAt: Date.now() };
        window.sessionStorage.setItem(storageKey, JSON.stringify(token));
        return token;
      } catch (_) {
        discard(token);
        return null;
      }
    }

    function prepare(root) {
      if (!optedIn(root)) return null;
      let saved;
      try {
        const value = window.sessionStorage.getItem(storageKey);
        if (!value) return null;
        window.sessionStorage.removeItem(storageKey);
        saved = JSON.parse(value);
      } catch (_) {
        return null;
      }
      const age = Date.now() - saved?.savedAt;
      const currentRoute = routeKey(window.location.href);
      if (saved?.version !== 1 || !Number.isFinite(saved?.top) || !Number.isFinite(age) ||
          age < 0 || age > ttl || saved.group !== String(root.dataset.switchGroup || '').trim() ||
          !currentRoute || saved.target !== currentRoute) return null;

      let active = true;
      let ready = false;
      let frame;
      let timer;
      const deadline = Date.now() + maxRestoreTime;
      let stopAt = deadline;
      let loaded = document.readyState === 'complete';
      let previousRestoration;
      const style = document.documentElement?.style;
      const previousBehavior = style?.scrollBehavior;
      try {
        previousRestoration = window.history.scrollRestoration;
        window.history.scrollRestoration = 'manual';
      } catch (_) {}
      if (style) style.scrollBehavior = 'auto';

      function cancel() {
        if (!active) return;
        active = false;
        if (frame !== undefined) window.cancelAnimationFrame(frame);
        if (timer !== undefined) window.clearTimeout(timer);
        inputEvents.forEach((type) => window.removeEventListener(type, cancel, true));
        window.removeEventListener('load', onWindowLoad);
        window.removeEventListener('load', schedule, true);
        window.removeEventListener('pagehide', cancel);
        try {
          if (previousRestoration !== undefined) window.history.scrollRestoration = previousRestoration;
        } catch (_) {}
        if (style) style.scrollBehavior = previousBehavior;
      }

      function correct() {
        frame = undefined;
        if (!active || !ready) return;
        if (!root.isConnected || Date.now() > deadline) {
          cancel();
          return;
        }
        const currentTop = root.getBoundingClientRect().top;
        const target = window.scrollY + currentTop - saved.top;
        if (Number.isFinite(target) && Math.abs(currentTop - saved.top) > 0.5) {
          try {
            window.scrollTo({ left: window.scrollX || 0, top: Math.max(0, target), behavior: 'instant' });
          } catch (_) {
            window.scrollTo(window.scrollX || 0, Math.max(0, target));
          }
        }
      }

      function schedule() {
        if (!active || !ready || frame !== undefined) return;
        frame = window.requestAnimationFrame(correct);
      }

      function tick() {
        timer = undefined;
        if (!active) return;
        if (Date.now() >= (ready ? stopAt : deadline)) {
          cancel();
          return;
        }
        schedule();
        timer = window.setTimeout(tick, 100);
      }

      function onWindowLoad() {
        loaded = true;
        if (ready) stopAt = Math.min(deadline, Date.now() + settleTime);
        schedule();
      }

      inputEvents.forEach((type) => window.addEventListener(type, cancel, { capture: true, passive: true }));
      window.addEventListener('load', onWindowLoad);
      window.addEventListener('load', schedule, true);
      window.addEventListener('pagehide', cancel);
      timer = window.setTimeout(tick, 100);

      return {
        cancel,
        activate() {
          if (!active) return;
          ready = true;
          if (loaded) stopAt = Math.min(deadline, Date.now() + settleTime);
          correct();
          schedule();
        },
      };
    }

    return { remember, prepare, discard };
  }

  const switcherPosition = createSwitcherPositionKeeper(window, document);

  // Bewaar de uitgeklapte kleurkeuzes alleen tijdens het navigeren naar een andere uitvoering.
  const EXPANDED_COLORS_KEY = 'bc:product-switcher:expanded-colors:v1';
  const EXPANDED_COLORS_TTL = 30000;

  function restoreExpandedColors(group, menus) {
    let saved;
    try {
      saved = JSON.parse(window.sessionStorage.getItem(EXPANDED_COLORS_KEY) || 'null');
      if (saved) window.sessionStorage.removeItem(EXPANDED_COLORS_KEY);
    } catch (_) {
      return new Set();
    }
    const age = Date.now() - Number(saved?.savedAt);
    if (saved?.version !== 1 || saved.group !== group ||
        saved.target !== window.location.pathname || !Array.isArray(saved.keys) ||
        !Number.isFinite(age) || age < 0 || age > EXPANDED_COLORS_TTL) return new Set();
    const available = new Set(menus.filter(isColorMenu).map((menu) => menu.key));
    return new Set(saved.keys.filter((key) => typeof key === 'string' && available.has(key)));
  }

  function rememberExpandedColors(group, expanded, destination) {
    if (!expanded.size) return null;
    try {
      const url = new URL(destination, window.location.origin);
      if (url.origin !== window.location.origin || !url.pathname.startsWith('/products/')) return null;
      const token = {
        version: 1, group, target: url.pathname, keys: Array.from(expanded), savedAt: Date.now()
      };
      window.sessionStorage.setItem(EXPANDED_COLORS_KEY, JSON.stringify(token));
      return token;
    } catch (_) {
      return null;
    }
  }

  function discardExpandedColors(token) {
    if (!token) return;
    try {
      const saved = JSON.parse(window.sessionStorage.getItem(EXPANDED_COLORS_KEY) || 'null');
      if (saved?.group === token.group && saved?.target === token.target &&
          saved?.savedAt === token.savedAt) {
        window.sessionStorage.removeItem(EXPANDED_COLORS_KEY);
      }
    } catch (_) {}
  }

  function normalize(value) {
    return String(value ?? '').trim();
  }

  function warn(message, detail) {
    if (detail !== undefined) {
      console.warn(`BCProductSwitcherV2: ${message}`, detail);
    } else {
      console.warn(`BCProductSwitcherV2: ${message}`);
    }
  }

  function debug(message, detail) {
    if (detail !== undefined) {
      console.info(`BCProductSwitcherV2 debug: ${message}`, detail);
    } else {
      console.info(`BCProductSwitcherV2 debug: ${message}`);
    }
  }

  function fetchJson(url) {
    return fetch(url, { credentials: 'same-origin' }).then((response) => {
      if (!response.ok) throw new Error(`Could not load ${url}: ${response.status}`);
      return response.json();
    });
  }

  function loadSwitcherData(dataUrl) {
    const primaryUrl = dataUrl || DEFAULT_DATA_URL;

    if (!dataPromise) {
      dataPromise = fetchJson(primaryUrl).catch((error) => {
        if (primaryUrl === DEFAULT_DATA_URL) throw error;
        return fetchJson(DEFAULT_DATA_URL);
      });
    }

    return dataPromise;
  }

  function getProductOption(product, key) {
    return normalize(product?.options?.[key]);
  }

  function getMenus(group) {
    return Array.isArray(group?.menus)
      ? [...group.menus]
          .filter((menu) => normalize(menu?.key))
          .sort((a, b) => Number(a.order || 0) - Number(b.order || 0))
      : [];
  }

  function getProducts(group) {
    return Array.isArray(group?.products)
      ? [...group.products].sort((a, b) => Number(a.sort_order || 0) - Number(b.sort_order || 0))
      : [];
  }

  function getValuesForMenu(products, key) {
    const menuValues = Array.isArray(this?.values) ? this.values.map(normalize).filter(Boolean) : [];
    if (menuValues.length) return menuValues;

    const values = [];
    const seen = new Set();

    products.forEach((product) => {
      const value = getProductOption(product, key);
      if (!value || seen.has(value)) return;
      values.push(value);
      seen.add(value);
    });

    return values;
  }

  function hasPartialMatch(products, state) {
    return products.some((product) =>
      Object.entries(state).every(([key, value]) => {
        const normalizedValue = normalize(value);
        if (!normalizedValue) return true;
        return getProductOption(product, key) === normalizedValue;
      })
    );
  }

  function findExactMatch(products, menus, state) {
    const matches = products.filter((product) =>
      menus.every((menu) => getProductOption(product, menu.key) === normalize(state[menu.key]))
    );
    return matches.length === 1 ? matches[0] : undefined;
  }

  function getDisplayType(menu, values) {
    const displayType = normalize(menu.display_type).toLowerCase();
    if (displayType === 'buttons' || displayType === 'dropdown') return displayType;
    return values.length > BUTTON_THRESHOLD ? 'dropdown' : 'buttons';
  }

  function createCheck() {
    const check = document.createElement('span');
    check.className = 'bc-buybox__option-check';
    check.setAttribute('aria-hidden', 'true');
    check.textContent = '\u2713';
    return check;
  }

  function createText(value) {
    const text = document.createElement('span');
    text.className = 'bc-buybox__option-text';
    text.textContent = value;
    return text;
  }

  class BCProductSwitcherV2 {
    constructor(root, data, positionRestore) {
      this.root = root;
      this.data = data;
      this.groupId = normalize(root.dataset.switchGroup);
      this.productHandle = normalize(root.dataset.productHandle);
      this.productUrl = normalize(root.dataset.productUrl);
      this.group = this.findGroup();
      this.menus = getMenus(this.group);
      this.products = getProducts(this.group);
      this.currentProduct = this.findCurrentProduct();
      this.state = {};
      this.productRoot = root.closest('product-info');
      this.isNavigating = false;
      this.positionRestore = positionRestore;

      debug('container found', {
        currentHandle: this.productHandle,
        currentSwitchGroup: this.groupId,
        productUrl: this.productUrl,
        groupFound: Boolean(this.group),
        menuCount: this.menus.length,
        productCount: this.products.length,
      });

      if (!this.group) {
        warn(`group "${this.groupId}" was not found.`, {
          currentHandle: this.productHandle,
          currentSwitchGroup: this.groupId,
          availableGroups: Array.isArray(this.data?.groups) ? this.data.groups.length : 0,
        });
        this.hide();
        return;
      }

      if (!this.currentProduct) {
        warn(`current product "${this.productHandle}" was not found in group "${this.groupId}".`, {
          currentHandle: this.productHandle,
          currentSwitchGroup: this.groupId,
          groupFound: true,
          menuCount: this.menus.length,
          productCount: this.products.length,
          firstHandles: this.products.slice(0, 5).map((product) => normalize(product.handle)),
        });
        this.hide();
        return;
      }

      if (!this.menus.length || this.products.length < 2) {
        warn(`group "${this.groupId}" does not contain enough switcher data.`, {
          currentHandle: this.productHandle,
          currentSwitchGroup: this.groupId,
          groupFound: true,
          menuCount: this.menus.length,
          productCount: this.products.length,
        });
        this.hide();
        return;
      }

      this.state = this.buildInitialState();
      this.mobileMedia = this.root.dataset.hotbathMobileA === 'true'
        ? window.matchMedia('(max-width: 749px)') : null;
      try {
        this.swatchUrls = JSON.parse(this.root.dataset.hotbathSwatchUrls || '{}');
        if (!this.swatchUrls || typeof this.swatchUrls !== 'object') this.swatchUrls = {};
      } catch (_) {
        this.swatchUrls = {};
      }
      this.expandedColors = this.mobileMedia?.matches
        ? restoreExpandedColors(this.groupId, this.menus) : new Set();
      this.onMobileChange = () => {
        if (!this.root.isConnected) {
          this.mobileMedia?.removeEventListener('change', this.onMobileChange);
          return;
        }
        const status = this.status?.textContent || '';
        this.render();
        this.syncControls();
        this.status.textContent = status;
      };
      this.mobileMedia?.addEventListener('change', this.onMobileChange);
      this.render();
      this.syncControls();
      this.root.hidden = false;
      this.root.dataset.bcProductSwitcherV2Initialized = 'true';
      this.positionRestore?.activate();
      this.onPageShow = () => {
        if (!this.root.isConnected) {
          window.removeEventListener('pageshow', this.onPageShow);
          return;
        }
        if (!this.isNavigating) return;
        this.setNavigating(false);
        this.state = this.buildInitialState();
        this.syncControls();
        this.status.textContent = '';
      };
      window.addEventListener('pageshow', this.onPageShow);

      debug('rendered', {
        currentHandle: this.productHandle,
        currentSwitchGroup: this.groupId,
        groupFound: true,
        menuCount: this.menus.length,
        productCount: this.products.length,
      });
    }

    findGroup() {
      const groups = Array.isArray(this.data?.groups) ? this.data.groups : [];
      return groups.find((group) => normalize(group.id) === this.groupId);
    }

    findCurrentProduct() {
      return this.products.find((product) => {
        if (normalize(product.handle) === this.productHandle) return true;
        return this.productUrl && normalize(product.url) === this.productUrl;
      });
    }

    buildInitialState() {
      return this.menus.reduce((state, menu) => {
        state[menu.key] = getProductOption(this.currentProduct, menu.key);
        return state;
      }, {});
    }

    hide() {
      this.positionRestore?.cancel();
      this.root.innerHTML = '';
      this.root.hidden = true;
    }

    render() {
      const fragment = document.createDocumentFragment();
      const mobile = this.mobileMedia?.matches === true;
      this.root.classList.toggle('bc-hotbath-switcher--mobile', mobile);

      const menus = mobile ? [...this.menus].sort((a, b) => Number(isColorMenu(b)) - Number(isColorMenu(a))) : this.menus;
      menus.forEach((menu) => {
        const values = getValuesForMenu.call(menu, this.products, menu.key);
        if (!values.length) return;
        if (values.length === 1 && menu.hide_if_single_value === true) return;

        const groupElement = document.createElement('div');
        groupElement.className = 'bc-buybox__option-group bc-buybox__switcher-group';
        groupElement.dataset.switcherGroup = menu.key;

        const label = document.createElement('p');
        label.className = 'form__label bc-buybox__option-label';
        label.textContent = normalize(menu.label) || menu.key;
        if (mobile && isColorMenu(menu)) {
          const selected = document.createElement('strong');
          selected.className = 'bc-hotbath-selected-color';
          selected.dataset.hotbathSelectedColor = menu.key;
          selected.textContent = normalize(this.state[menu.key]);
          label.append(document.createTextNode(': '), selected);
        }
        groupElement.append(label);

        if (mobile && isColorMenu(menu)) {
          groupElement.append(this.renderSwatches(menu, values));
        } else if (!mobile && getDisplayType(menu, values) === 'dropdown') {
          groupElement.append(this.renderSelect(menu, values));
        } else {
          groupElement.append(this.renderButtons(menu, values));
        }

        fragment.append(groupElement);
      });

      this.root.innerHTML = '';
      this.status = document.createElement('p');
      this.status.className = 'bc-buybox__switch-status';
      this.status.setAttribute('role', 'status');
      this.status.setAttribute('aria-live', 'polite');
      this.status.setAttribute('aria-atomic', 'true');
      this.root.append(fragment, this.status);
    }

    renderSwatches(menu, values) {
      const wrapper = document.createElement('div');
      wrapper.className = 'bc-hotbath-colors';
      const list = document.createElement('div');
      list.className = 'bc-hotbath-swatches';
      list.id = `bc-hotbath-colors-${this.root.dataset.sectionId || this.productHandle}-${menu.key}`;
      list.setAttribute('role', 'group');
      list.setAttribute('aria-label', normalize(menu.label) || menu.key);
      const selectedValue = normalize(this.state[menu.key]);
      const visibleValues = new Set(values.slice(0, 4));
      if (!visibleValues.has(selectedValue) && values.includes(selectedValue)) {
        visibleValues.delete(values[3]);
        visibleValues.add(selectedValue);
      }
      const buttons = values.map((value) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'bc-hotbath-swatch';
        button.dataset.switchField = menu.key;
        button.dataset.switchValue = value;
        button.setAttribute('aria-label', value);
        button.setAttribute('aria-pressed', 'false');
        const chip = document.createElement('span');
        chip.className = 'bc-hotbath-swatch__chip';
        chip.setAttribute('aria-hidden', 'true');
        const surface = document.createElement('span');
        surface.className = 'bc-hotbath-swatch__surface';
        const fallback = document.createElement('span');
        fallback.className = 'bc-hotbath-swatch__fallback';
        fallback.textContent = (HOTBATH_SWATCHES[normalize(value).toLowerCase()] ||
          value.split(/\s+/).map((word) => word.charAt(0)).join('').slice(0, 3)).toUpperCase();
        const colorName = document.createElement('span');
        colorName.className = 'bc-hotbath-swatch__label';
        colorName.textContent = value;
        const url = swatchUrl(value, this.swatchUrls);
        if (url) {
          const img = document.createElement('img');
          img.src = url;
          img.alt = '';
          img.width = 80;
          img.height = 80;
          img.loading = 'lazy';
          img.decoding = 'async';
          img.addEventListener('load', () => button.classList.add('has-swatch-image'));
          img.addEventListener('error', () => {
            button.classList.remove('has-swatch-image');
            img.remove();
          });
          surface.append(img);
        }
        const check = document.createElement('span');
        check.className = 'bc-hotbath-swatch__check';
        check.setAttribute('aria-hidden', 'true');
        check.textContent = '\u2713';
        surface.append(fallback);
        chip.append(surface, check);
        button.append(chip, colorName);
        button.addEventListener('click', () => this.updateSelection(menu.key, value));
        return button;
      });
      list.append(...buttons);
      wrapper.append(list);
      let toggle;
      let toggleLabel;
      let badge;
      const syncExpansion = () => {
        const expanded = this.expandedColors.has(menu.key);
        buttons.forEach((button) => {
          button.hidden = !expanded && !visibleValues.has(button.dataset.switchValue);
        });
        if (!toggle) return;
        toggle.setAttribute('aria-expanded', String(expanded));
        toggleLabel.textContent = expanded
          ? normalize(this.root.dataset.labelLessColors || 'Minder kleuren')
          : normalize(this.root.dataset.labelAllColors || 'Bekijk alle __COUNT__ kleuren')
            .replace('__COUNT__', String(values.length));
        badge.hidden = expanded;
      };
      if (values.length > 4) {
        toggle = document.createElement('button');
        toggle.type = 'button';
        toggle.className = 'bc-hotbath-colors__toggle';
        toggle.setAttribute('aria-controls', list.id);
        toggleLabel = document.createElement('span');
        toggleLabel.className = 'bc-hotbath-colors__toggle-label';
        badge = document.createElement('span');
        badge.className = 'bc-hotbath-colors__count';
        badge.setAttribute('aria-hidden', 'true');
        badge.textContent = `+${values.length - visibleValues.size}`;
        toggle.append(toggleLabel, badge);
        toggle.addEventListener('click', () => {
          if (this.expandedColors.has(menu.key)) this.expandedColors.delete(menu.key);
          else this.expandedColors.add(menu.key);
          syncExpansion();
          toggle.focus({ preventScroll: true });
        });
        wrapper.append(toggle);
      }
      syncExpansion();
      return wrapper;
    }

    renderButtons(menu, values) {
      const buttonList = document.createElement('div');
      buttonList.className = 'bc-buybox__config-buttons';
      buttonList.setAttribute('role', 'group');
      buttonList.setAttribute('aria-label', normalize(menu.label) || menu.key);

      values.forEach((value) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'bc-buybox__config-button';
        button.dataset.switchField = menu.key;
        button.dataset.switchValue = value;
        button.setAttribute('aria-pressed', 'false');
        button.append(createCheck(), createText(value));
        button.addEventListener('click', () => this.updateSelection(menu.key, value));
        buttonList.append(button);
      });

      return buttonList;
    }

    renderSelect(menu, values) {
      const wrapper = document.createElement('div');
      const select = document.createElement('select');

      wrapper.className = 'bc-buybox__config-select-wrap';
      wrapper.dataset.switchField = menu.key;
      select.className = 'bc-buybox__config-select';
      select.dataset.switchField = menu.key;
      select.setAttribute('aria-label', normalize(menu.label) || menu.key);

      values.forEach((value) => {
        const option = document.createElement('option');
        option.value = value;
        option.textContent = value;
        select.append(option);
      });

      select.addEventListener('change', () => this.updateSelection(menu.key, select.value));
      wrapper.append(select);
      return wrapper;
    }

    syncControls() {
      this.root.querySelectorAll('[data-hotbath-selected-color]').forEach((label) => {
        label.textContent = normalize(this.state[label.dataset.hotbathSelectedColor]);
      });
      this.root.querySelectorAll('button[data-switch-field][data-switch-value]').forEach((button) => {
        const field = button.dataset.switchField;
        const value = normalize(button.dataset.switchValue);
        const isActive = normalize(this.state[field]) === value;
        const isEnabled = hasPartialMatch(this.products, { ...this.state, [field]: value });

        button.classList.toggle('is-active', isActive);
        button.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        button.disabled = this.isNavigating || !isEnabled;
        button.title = isEnabled ? '' : 'Niet mogelijk met de overige keuzes.';
        button.setAttribute('aria-disabled', String(button.disabled));
      });

      this.root.querySelectorAll('select[data-switch-field]').forEach((select) => {
        const field = select.dataset.switchField;
        const currentValue = normalize(this.state[field]);
        select.disabled = this.isNavigating;

        Array.from(select.options).forEach((option) => {
          option.disabled = !hasPartialMatch(this.products, { ...this.state, [field]: normalize(option.value) });
        });

        if (currentValue && select.value !== currentValue) select.value = currentValue;
      });
    }

    setNavigating(navigating) {
      this.isNavigating = navigating;
      this.root.setAttribute('aria-busy', String(navigating));
      if (!this.productRoot) return;
      if (navigating) {
        this.productRoot.dataset.bcNavigating = 'true';
        this.lockedButtons = Array.from(this.productRoot.querySelectorAll('.product-form__submit'))
          .map((button) => ({ button, disabled: button.disabled }));
        this.lockedButtons.forEach(({ button }) => { button.disabled = true; });
      } else {
        delete this.productRoot.dataset.bcNavigating;
        this.lockedButtons?.forEach(({ button, disabled }) => { button.disabled = disabled; });
        this.lockedButtons = [];
      }
    }

    updateSelection(field, value) {
      if (this.isNavigating) return;
      const submit = this.productRoot?.querySelector('.product-form__submit');
      if (submit?.getAttribute('aria-busy') === 'true' || submit?.classList.contains('loading')) {
        this.syncControls();
        this.status.textContent = 'Wacht tot het toevoegen aan de winkelwagen klaar is.';
        return;
      }
      const nextState = { ...this.state, [field]: normalize(value) };
      const matchedProduct = findExactMatch(this.products, this.menus, nextState);
      const matchedUrl = normalize(matchedProduct?.url);
      let destination;
      try {
        destination = new URL(matchedUrl, window.location.origin);
      } catch (_) {
        destination = null;
      }
      if (!matchedUrl || !destination || destination.origin !== window.location.origin ||
          !destination.pathname.includes('/products/') ||
          destination.pathname.split('/').pop() !== normalize(matchedProduct?.handle)) {
        this.syncControls();
        this.status.textContent = 'Deze combinatie kan niet worden geopend. Kies een andere uitvoering.';
        return;
      }
      if (normalize(matchedProduct.handle) === this.productHandle) {
        this.syncControls();
        this.status.textContent = '';
        return;
      }

      const positionToken = switcherPosition.remember(this.root, destination.href);
      const expandedToken = this.mobileMedia?.matches
        ? rememberExpandedColors(this.groupId, this.expandedColors, destination.href) : null;
      this.state = nextState;
      this.setNavigating(true);
      this.syncControls();
      this.status.textContent = 'De gekozen uitvoering wordt geopend…';
      try {
        window.location.assign(destination.href);
      } catch (_) {
        switcherPosition.discard(positionToken);
        discardExpandedColors(expandedToken);
        this.setNavigating(false);
        this.state = this.buildInitialState();
        this.syncControls();
        this.status.textContent = 'Openen is niet gelukt. Probeer de uitvoering opnieuw te kiezen.';
      }
    }
  }

  function init(root = document) {
    const switcherRoots = Array.from(root.querySelectorAll(ROOT_SELECTOR)).filter(
      (switcherRoot) => switcherRoot.dataset.bcProductSwitcherV2Initialized !== 'true'
    );

    if (!switcherRoots.length) return;
    const positionRestores = new Map(switcherRoots.map((switcherRoot) => [switcherRoot, switcherPosition.prepare(switcherRoot)]));

    const dataUrl = switcherRoots.map((switcherRoot) => switcherRoot.dataset.switcherDataUrl).find(Boolean);

    debug('initializing roots', {
      rootCount: switcherRoots.length,
      dataUrl: dataUrl || DEFAULT_DATA_URL,
    });

    loadSwitcherData(dataUrl)
      .then((data) => {
        debug('data loaded', {
          groupCount: Array.isArray(data?.groups) ? data.groups.length : 0,
        });
        switcherRoots.forEach((switcherRoot) => new BCProductSwitcherV2(switcherRoot, data, positionRestores.get(switcherRoot)));
      })
      .catch((error) => {
        warn('switcher data could not be loaded.', error);
        switcherRoots.forEach((switcherRoot) => {
          positionRestores.get(switcherRoot)?.cancel();
          switcherRoot.innerHTML = '';
          switcherRoot.hidden = true;
        });
      });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => init());
  } else {
    init();
  }
})();
