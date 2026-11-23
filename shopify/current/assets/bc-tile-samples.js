(() => {
  if (window.BCTileSamples) return;

  function sampleCount(cart) {
    return cart.items.reduce((total, item) => {
      return item.product_type === 'Tegelsample' ? total + item.quantity : total;
    }, 0);
  }

  function variantCount(cart, variantId) {
    return cart.items.reduce((total, item) => {
      return String(item.variant_id) === String(variantId) ? total + item.quantity : total;
    }, 0);
  }

  async function readCart(url) {
    const response = await fetch(url.replace(/\/$/, '') + '.js', {
      headers: { Accept: 'application/json' },
      cache: 'no-store'
    });
    if (!response.ok) throw new Error('cart');
    const cart = await response.json();
    if (!Array.isArray(cart.items)) throw new Error('cart');
    return cart;
  }

  let pending = Promise.resolve();
  function withCartLock(action) {
    if (navigator.locks?.request) return navigator.locks.request('bc-tile-samples', action);
    const result = pending.then(action);
    pending = result.catch(() => {});
    return result;
  }

  const channel = typeof BroadcastChannel === 'function' ? new BroadcastChannel('bc-tile-samples') : null;
  channel?.addEventListener('message', () => {
    document.querySelectorAll('bc-tile-sample').forEach(element => element.syncFromCart());
    document.querySelectorAll('cart-items, cart-drawer-items').forEach(element => element.onCartUpdate?.());
  });

  function tellCart(cartData, productVariantId) {
    if (typeof publish === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
      publish(PUB_SUB_EVENTS.cartUpdate, { source: 'bc-sample', cartData, productVariantId });
    }
  }

  async function changeLine(cartItems, line, input, quantity, change) {
    return withCartLock(async () => {
      try {
        const cart = await readCart(window.routes.cart_url);
        const current = cart.items.find(item => item.key === input.dataset.bcSampleKey);
        if (!current) {
          await cartItems.onCartUpdate();
          return;
        }
        if (quantity > current.quantity) {
          const addsDuplicate = input.dataset.bcSampleOnce &&
            variantCount(cart, current.variant_id) - current.quantity + quantity > 1;
          if (addsDuplicate || sampleCount(cart) - current.quantity + quantity > 5) {
            input.value = current.quantity;
            cartItems.updateLiveRegions(line, addsDuplicate ? input.dataset.bcSampleOnce : input.dataset.bcSampleLimit);
            return;
          }
        }
        await change(current.key);
        channel?.postMessage('updated');
      } catch {
        input.value = input.defaultValue;
        cartItems.updateLiveRegions(line, window.cartStrings.error);
      }
    });
  }

  window.BCTileSamples = { changeLine };

  class TileSample extends HTMLElement {
    connectedCallback() {
      this.form = this.querySelector('form');
      this.button = this.form.querySelector('[type="submit"]');
      this.status = this.querySelector('[data-sample-status]');
      this.cartLink = this.querySelector('[data-sample-cart]');
      this.atLimit = this.button.disabled;
      this.form.addEventListener('submit', this.onSubmit);
      window.addEventListener('pageshow', this.syncFromCart);
      window.addEventListener('focus', this.syncFromCart);
      if (typeof subscribe === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
        this.unsubscribe = subscribe(PUB_SUB_EVENTS.cartUpdate, this.onCartUpdate);
      }
    }

    disconnectedCallback() {
      this.form?.removeEventListener('submit', this.onSubmit);
      window.removeEventListener('pageshow', this.syncFromCart);
      window.removeEventListener('focus', this.syncFromCart);
      this.unsubscribe?.();
    }

    setCount(cart) {
      const count = sampleCount(cart);
      const alreadyChosen = this.dataset.once && variantCount(cart, this.form.elements.namedItem('id').value) > 0;
      this.atLimit = count >= 5 || Boolean(alreadyChosen);
      this.querySelector('[data-sample-first]').hidden = count > 0;
      this.querySelector('[data-sample-extra]').hidden = count === 0;
      this.button.disabled = this.atLimit || this.busy === true;
      if (this.atLimit) this.message(count >= 5 ? this.dataset.atLimit : this.dataset.once, true);
      else if ([this.dataset.atLimit, this.dataset.once].includes(this.status.textContent)) this.message('', false);
    }

    message(text, showLink) {
      this.status.textContent = text;
      this.cartLink.hidden = !showLink;
    }

    syncVersion = 0;
    syncFromCart = async () => {
      if (this.busy) return;
      const version = ++this.syncVersion;
      try {
        const cart = await readCart(this.dataset.cartUrl);
        if (this.isConnected && !this.busy && this.syncVersion === version) this.setCount(cart);
      } catch {
        // The server-rendered button still posts to Shopify when the cart becomes available.
      }
    };

    onCartUpdate = (event) => {
      if (event.source === 'bc-sample') return;
      if (Array.isArray(event.cartData?.items) && Number.isInteger(event.cartData.item_count)) {
        ++this.syncVersion;
        this.setCount(event.cartData);
      } else {
        this.syncFromCart();
      }
    };

    onSubmit = async (event) => {
      event.preventDefault();
      if (this.busy || this.closest('product-info')?.dataset.bcNavigating === 'true') return;
      this.busy = true;
      ++this.syncVersion;
      this.button.disabled = true;
      this.button.setAttribute('aria-busy', 'true');
      try {
        await withCartLock(() => this.add());
      } catch {
        this.message(this.dataset.error, true);
      } finally {
        this.busy = false;
        this.button.disabled = this.atLimit;
        this.button.removeAttribute('aria-busy');
      }
    };

    async add() {
      const cart = await readCart(this.dataset.cartUrl);
      this.setCount(cart);
      if (this.atLimit || !this.isConnected || this.closest('product-info')?.dataset.bcNavigating === 'true') return;

      const notice = document.querySelector('cart-notification') || document.querySelector('cart-drawer');
      const data = new FormData(this.form);
      const canRender = typeof notice?.getSectionsToRender === 'function' && typeof notice.renderContents === 'function';
      data.delete('return_to');
      if (canRender) {
        notice.setActiveElement?.(this.button);
        data.set('sections', notice.getSectionsToRender().map(section => section.id).join(','));
        data.set('sections_url', window.location.pathname + window.location.search);
      }
      const response = await fetch(this.form.action.replace(/\/$/, '') + '.js', {
        method: 'POST',
        headers: { Accept: 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
        body: data
      });
      const added = await response.json();
      if (!response.ok || added.status || added.errors) {
        this.message(typeof added.description === 'string' ? added.description : this.dataset.error, true);
        return;
      }

      channel?.postMessage('updated');
      this.message(this.dataset.added, true);
      try {
        const updated = await readCart(this.dataset.cartUrl);
        this.setCount(updated);
        const matching = updated.items.find(item => item.key === added.key) ||
          updated.items.find(item => String(item.variant_id) === String(data.get('id')) &&
            String(item.properties?.['Artikelnummer tegel'] || '') === String(data.get('properties[Artikelnummer tegel]') || ''));
        if (matching) added.key = matching.key;
        tellCart(updated, data.get('id'));
      } catch {
        tellCart(added, data.get('id'));
      }

      if (!canRender || !added.sections) {
        window.location.assign(this.dataset.cartUrl);
        return;
      }
      try {
        notice.classList.remove('is-empty');
        notice.renderContents(added);
      } catch {
        window.location.assign(this.dataset.cartUrl);
      }
    }
  }

  if (!customElements.get('bc-tile-sample')) customElements.define('bc-tile-sample', TileSample);
})();
