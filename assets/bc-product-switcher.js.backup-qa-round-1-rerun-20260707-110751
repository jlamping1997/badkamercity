(function () {
  const ROOT_SELECTOR = '[data-bc-product-switcher-v2]';
  const DEFAULT_DATA_URL = '/assets/product-switcher-data.json';
  const BUTTON_THRESHOLD = 5;

  let dataPromise;

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
    return products.find((product) =>
      menus.every((menu) => getProductOption(product, menu.key) === normalize(state[menu.key]))
    );
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
    constructor(root, data) {
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
      this.render();
      this.syncControls();
      this.root.hidden = false;
      this.root.dataset.bcProductSwitcherV2Initialized = 'true';

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
      this.root.innerHTML = '';
      this.root.hidden = true;
    }

    render() {
      const fragment = document.createDocumentFragment();

      this.menus.forEach((menu) => {
        const values = getValuesForMenu.call(menu, this.products, menu.key);
        if (!values.length) return;
        if (values.length === 1 && menu.hide_if_single_value === true) return;

        const groupElement = document.createElement('div');
        groupElement.className = 'bc-buybox__option-group bc-buybox__switcher-group';
        groupElement.dataset.switcherGroup = menu.key;

        const label = document.createElement('p');
        label.className = 'form__label bc-buybox__option-label';
        label.textContent = normalize(menu.label) || menu.key;
        groupElement.append(label);

        if (getDisplayType(menu, values) === 'dropdown') {
          groupElement.append(this.renderSelect(menu, values));
        } else {
          groupElement.append(this.renderButtons(menu, values));
        }

        fragment.append(groupElement);
      });

      this.root.innerHTML = '';
      this.root.append(fragment);
    }

    renderButtons(menu, values) {
      const buttonList = document.createElement('div');
      buttonList.className = 'bc-buybox__config-buttons';
      buttonList.setAttribute('role', 'list');
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
      this.root.querySelectorAll('button[data-switch-field][data-switch-value]').forEach((button) => {
        const field = button.dataset.switchField;
        const value = normalize(button.dataset.switchValue);
        const isActive = normalize(this.state[field]) === value;
        const isEnabled = hasPartialMatch(this.products, { ...this.state, [field]: value });

        button.classList.toggle('is-active', isActive);
        button.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        button.disabled = !isEnabled;
        button.setAttribute('aria-disabled', isEnabled ? 'false' : 'true');
      });

      this.root.querySelectorAll('select[data-switch-field]').forEach((select) => {
        const field = select.dataset.switchField;
        const currentValue = normalize(this.state[field]);

        Array.from(select.options).forEach((option) => {
          option.disabled = !hasPartialMatch(this.products, { ...this.state, [field]: normalize(option.value) });
        });

        if (currentValue && select.value !== currentValue) select.value = currentValue;
      });
    }

    updateSelection(field, value) {
      const nextState = { ...this.state, [field]: normalize(value) };
      this.state = nextState;
      this.syncControls();

      const matchedProduct = findExactMatch(this.products, this.menus, this.state);
      const matchedUrl = normalize(matchedProduct?.url);
      if (!matchedUrl || matchedUrl === this.productUrl) return;

      window.location.href = matchedUrl;
    }
  }

  function init(root = document) {
    const switcherRoots = Array.from(root.querySelectorAll(ROOT_SELECTOR)).filter(
      (switcherRoot) => switcherRoot.dataset.bcProductSwitcherV2Initialized !== 'true'
    );

    if (!switcherRoots.length) return;

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
        switcherRoots.forEach((switcherRoot) => new BCProductSwitcherV2(switcherRoot, data));
      })
      .catch((error) => {
        warn('switcher data could not be loaded.', error);
        switcherRoots.forEach((switcherRoot) => {
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
