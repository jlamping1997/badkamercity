(function () {
  'use strict';

  if (window.BCSunshowerShop) {
    window.BCSunshowerShop.init(document);
    return;
  }

  var instances = new Map();
  var selector = '[data-bcsse-shop-card]';
  var cartQueue = Promise.resolve();

  function queueCart(task) {
    cartQueue = cartQueue.catch(function () {}).then(task);
    return cartQueue;
  }

  function cartEndpoint() {
    var path = window.routes && window.routes.cart_add_url;
    if (!path) path = ((window.Shopify && window.Shopify.routes && window.Shopify.routes.root) || '/') + 'cart/add';
    return path.replace(/\.js$/, '') + '.js';
  }

  function cartUI() {
    return document.querySelector('cart-notification') || document.querySelector('cart-drawer');
  }

  function cartSections(cart) {
    if (!cart) return [];
    if (cart.tagName === 'CART-NOTIFICATION') return ['cart-icon-bubble'];
    if (typeof cart.getSectionsToRender !== 'function') return [];
    try {
      return cart.getSectionsToRender().map(function (section) { return section.id; }).filter(Boolean);
    } catch (error) {
      return [];
    }
  }

  function updateCartBadge(result) {
    var html = result.sections && result.sections['cart-icon-bubble'];
    var badge = document.getElementById('cart-icon-bubble');
    if (!badge || typeof html !== 'string' || !html.trim()) return;
    var content = new DOMParser().parseFromString(html, 'text/html').querySelector('.shopify-section');
    if (content) badge.innerHTML = content.innerHTML;
  }

  function publishCart(choice, response) {
    if (typeof publish !== 'function' || typeof PUB_SUB_EVENTS === 'undefined' || !PUB_SUB_EVENTS.cartUpdate) return Promise.resolve();
    try {
      return Promise.resolve(publish(PUB_SUB_EVENTS.cartUpdate, {
        source: 'bc-sunshower-shop',
        productVariantId: choice.id,
        cartData: response
      })).catch(function () {});
    } catch (error) {
      return Promise.resolve();
    }
  }

  function createController(root) {
    var data;
    var source = root.querySelector('[data-bcsse-shop-data]');
    var image = root.querySelector('[data-bcsse-shop-image]');
    var color = root.querySelector('[data-bcsse-shop-color]');
    var price = root.querySelector('[data-bcsse-shop-price]');
    var form = root.querySelector('[data-bcsse-shop-form]');
    var input = form && form.querySelector('[name="id"]');
    var button = root.querySelector('[data-bcsse-shop-submit]');
    var buttonLabel = root.querySelector('[data-bcsse-shop-button-label]');
    var status = root.querySelector('[data-bcsse-shop-status]');
    var cartLink = root.querySelector('[data-bcsse-shop-cart-link]');
    var links = Array.from(root.querySelectorAll('[data-bcsse-shop-link]'));
    var swatches = Array.from(root.querySelectorAll('[data-bcsse-shop-choice]'));
    if (!source || !image || !price || !form || !input || !button || !buttonLabel || !status) return null;

    try {
      data = JSON.parse(source.textContent);
      if (!data || !Array.isArray(data.choices) || !data.choices.length) return null;
      if (!data.choices.every(function (choice) {
        return choice && typeof choice.key === 'string' && /^\d+$/.test(String(choice.id)) && typeof choice.available === 'boolean' &&
          typeof choice.url === 'string' && typeof choice.title === 'string' &&
          choice.image && typeof choice.image.src === 'string' && choice.image.src;
      })) return null;
    } catch (error) {
      return null;
    }

    var choices = new Map(data.choices.map(function (choice) { return [choice.key, choice]; }));
    var current = choices.get(data.initial) || data.choices.find(function (choice) { return String(choice.id) === input.value; }) || data.choices[0];
    var pending = false;
    var imageLoading = false;
    var destroyed = false;
    var imageToken = 0;
    var cancelImage = null;
    var originalSwatchAttributes = swatches.map(function (swatch) {
      return ['role', 'aria-pressed', 'aria-disabled'].map(function (name) { return [name, swatch.getAttribute(name)]; });
    });

    function label(name) {
      return root.dataset[name] || '';
    }

    function setStatus(message, showCart) {
      if (destroyed) return;
      status.textContent = message || '';
      status.hidden = !message;
      if (cartLink) cartLink.hidden = !showCart;
    }

    function updateControls() {
      if (destroyed) return;
      button.disabled = pending || imageLoading || !current.available;
      button.setAttribute('aria-disabled', String(button.disabled));
      if (pending || imageLoading) {
        button.setAttribute('aria-busy', 'true');
        root.dataset.bcsseShopBusy = pending ? 'cart' : 'image';
      } else {
        button.removeAttribute('aria-busy');
        delete root.dataset.bcsseShopBusy;
      }
      buttonLabel.textContent = pending ? label('bcsseLoadingLabel') : imageLoading ? label('bcsseLoadingImageLabel') :
        current.available ? label('bcsseAddLabel') : label('bcsseSoldOutLabel');
      swatches.forEach(function (swatch) {
        var selected = swatch.dataset.bcsseShopChoice === current.key;
        swatch.classList.toggle('bcsse-swatch--selected', selected);
        swatch.setAttribute('aria-pressed', String(selected));
        swatch.removeAttribute('aria-current');
        if (pending) swatch.setAttribute('aria-disabled', 'true');
        else swatch.removeAttribute('aria-disabled');
      });
    }

    function setImageAttributes(target, next) {
      if (next.sizes) target.setAttribute('sizes', next.sizes);
      else target.removeAttribute('sizes');
      if (next.srcset) target.setAttribute('srcset', next.srcset);
      else target.removeAttribute('srcset');
      if (next.width) target.setAttribute('width', String(next.width));
      else target.removeAttribute('width');
      if (next.height) target.setAttribute('height', String(next.height));
      else target.removeAttribute('height');
      target.setAttribute('alt', next.alt || '');
      target.setAttribute('src', next.src);
    }

    function commitChoice(choice) {
      current = choice;
      setImageAttributes(image, choice.image);
      root.dataset.bcsseImageMode = choice.image.mode || 'product';
      links.forEach(function (link) {
        link.href = choice.url;
        link.setAttribute('aria-label', choice.title);
      });
      if (color) color.textContent = choice.label || '';
      price.textContent = choice.price || '';
      input.value = choice.id;
      updateControls();
      window.BCWishlist?.refresh(root);
    }

    function preload(nextImage) {
      return new Promise(function (resolve, reject) {
        var probe = new Image();
        var settled = false;
        function finish(error) {
          if (settled) return;
          settled = true;
          probe.onload = null;
          probe.onerror = null;
          if (cancelImage === cancel) cancelImage = null;
          if (error) reject(error);
          else resolve();
        }
        function cancel() { finish(new Error('cancelled')); }
        cancelImage = cancel;
        probe.onload = function () { finish(probe.naturalWidth ? null : new Error('image')); };
        probe.onerror = function () { finish(new Error('image')); };
        if (nextImage.sizes) probe.sizes = nextImage.sizes;
        if (nextImage.srcset) probe.srcset = nextImage.srcset;
        probe.src = nextImage.src;
        if (probe.complete && probe.naturalWidth) finish();
      });
    }

    function selectChoice(key) {
      if (pending || destroyed || !choices.has(key)) return;
      imageToken += 1;
      var token = imageToken;
      if (cancelImage) cancelImage();
      if (current.key === key) {
        imageLoading = false;
        updateControls();
        setStatus('');
        return;
      }
      var choice = choices.get(key);
      imageLoading = true;
      setStatus(label('bcsseLoadingImageLabel'));
      updateControls();
      preload(choice.image).then(function () {
        if (destroyed || token !== imageToken) return;
        imageLoading = false;
        commitChoice(choice);
        setStatus('');
      }).catch(function () {
        if (destroyed || token !== imageToken) return;
        imageLoading = false;
        updateControls();
        setStatus(label('bcsseImageErrorLabel'));
      });
    }

    function onClick(event) {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      var swatch = event.target.closest('[data-bcsse-shop-choice]');
      if (!swatch || !root.contains(swatch) || !choices.has(swatch.dataset.bcsseShopChoice)) return;
      event.preventDefault();
      selectChoice(swatch.dataset.bcsseShopChoice);
    }

    function onKeyDown(event) {
      if (event.defaultPrevented || (event.key !== ' ' && event.code !== 'Space') || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      var swatch = event.target.closest('[data-bcsse-shop-choice]');
      if (!swatch || !root.contains(swatch) || !choices.has(swatch.dataset.bcsseShopChoice)) return;
      event.preventDefault();
      selectChoice(swatch.dataset.bcsseShopChoice);
    }

    async function addToCart(choice) {
      if (destroyed) return;
      var cart = cartUI();
      var sections = cartSections(cart);
      var body = { id: choice.id, quantity: 1 };
      if (sections.length) {
        body.sections = sections;
        body.sections_url = window.location.pathname;
      }
      var response;
      var result;
      try {
        response = await fetch(cartEndpoint(), {
          method: 'POST',
          credentials: 'same-origin',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
          body: JSON.stringify(body)
        });
        result = await response.json();
      } catch (error) {
        setStatus(label('bcsseErrorLabel'), true);
        return;
      }

      if (!response.ok || !result || result.status || !result.id) {
        setStatus((result && typeof result.description === 'string' && result.description) || label('bcsseErrorLabel'), true);
        return;
      }

      setStatus(label('bcsseAddedLabel').split('__product__').join(choice.title), true);
      if (cart && cart.tagName === 'CART-NOTIFICATION') {
        try { updateCartBadge(result); } catch (error) {}
      } else if (cart && typeof cart.renderContents === 'function' && sections.length && result.sections &&
          sections.every(function (id) { return typeof result.sections[id] === 'string' && result.sections[id].trim(); }) &&
          result.id) {
        try {
          if (typeof cart.setActiveElement === 'function' && button.isConnected) cart.setActiveElement(button);
          if (cart.classList.contains('is-empty')) cart.classList.remove('is-empty');
          cart.renderContents(result);
        } catch (error) {}
      }
      await publishCart(choice, result);
    }

    function onSubmit(event) {
      event.preventDefault();
      if (pending || imageLoading || !current.available || destroyed) return;
      var restoreButtonFocus = document.activeElement === button;
      pending = true;
      var choice = current;
      setStatus(label('bcsseLoadingLabel'));
      updateControls();
      queueCart(function () { return addToCart(choice); }).catch(function () {
        setStatus(label('bcsseErrorLabel'), true);
      }).finally(function () {
        pending = false;
        updateControls();
        if (restoreButtonFocus && !destroyed && button.isConnected && !button.disabled && document.activeElement === document.body) {
          button.focus({ preventScroll: true });
        }
      });
    }

    swatches.forEach(function (swatch) { swatch.setAttribute('role', 'button'); });
    root.addEventListener('click', onClick);
    root.addEventListener('keydown', onKeyDown);
    form.addEventListener('submit', onSubmit);
    root.dataset.bcsseShopReady = 'true';
    commitChoice(current);

    return {
      destroy: function () {
        destroyed = true;
        imageToken += 1;
        if (cancelImage) cancelImage();
        root.removeEventListener('click', onClick);
        root.removeEventListener('keydown', onKeyDown);
        form.removeEventListener('submit', onSubmit);
        swatches.forEach(function (swatch, index) {
          originalSwatchAttributes[index].forEach(function (attribute) {
            if (attribute[1] === null) swatch.removeAttribute(attribute[0]);
            else swatch.setAttribute(attribute[0], attribute[1]);
          });
        });
        button.disabled = !current.available;
        button.setAttribute('aria-disabled', String(button.disabled));
        button.removeAttribute('aria-busy');
        buttonLabel.textContent = current.available ? label('bcsseAddLabel') : label('bcsseSoldOutLabel');
        delete root.dataset.bcsseShopReady;
        delete root.dataset.bcsseShopBusy;
      }
    };
  }

  function init(scope) {
    var roots = Array.from(scope.querySelectorAll(selector));
    if (scope.matches && scope.matches(selector)) roots.unshift(scope);
    roots.forEach(function (root) {
      if (instances.has(root)) return;
      var controller = createController(root);
      if (controller) instances.set(root, controller);
    });
  }

  document.addEventListener('shopify:section:load', function (event) { init(event.target); });
  document.addEventListener('shopify:section:unload', function (event) {
    instances.forEach(function (controller, root) {
      if (event.target === root || event.target.contains(root)) {
        controller.destroy();
        instances.delete(root);
      }
    });
  });
  window.BCSunshowerShop = { init: init };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(document); }, { once: true });
  else init(document);
})();
