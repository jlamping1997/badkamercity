if (!customElements.get('bc-product-accessories')) {
  customElements.define('bc-product-accessories', class extends HTMLElement {
    connectedCallback() {
      this.controller = new AbortController();
      this.busy = false;
      this.root = this.closest('product-info');
      this.button = this.querySelector('[data-accessory-submit]');
      this.error = this.querySelector('[data-accessory-error]');
      this.cartLink = this.querySelector('[data-accessory-cart-link]');
      this.money = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL', {
        style: 'currency', currency: this.dataset.currency || 'EUR'
      });
      const options = { signal: this.controller.signal };
      this.addEventListener('change', () => this.sync(), options);
      this.addEventListener('input', () => this.sync(), options);
      this.button.addEventListener('click', () => this.addSelected(), options);
      window.addEventListener('pageshow', event => this.resetAfterReturn(event), options);
      this.querySelector('[data-accessory-controls]').hidden = false;
      this.sync();
    }

    rows() { return Array.from(this.querySelectorAll('[data-accessory-row]')); }

    resetAfterReturn(event) {
      if (!event.persisted || !this.busy) return;
      this.rows().forEach(row => {
        const select = row.querySelector('[data-accessory-select]');
        if (select) select.checked = false;
      });
      this.busy = false;
      this.sync();
    }

    sync() {
      let count = 0;
      let total = 0;
      this.rows().forEach(row => {
        const select = row.querySelector('[data-accessory-select]');
        const quantity = row.querySelector('[data-accessory-quantity]');
        if (!select || !quantity) return;
        select.disabled = this.busy;
        quantity.disabled = this.busy || !select.checked;
        if (!select.checked) return;
        const value = Number(quantity.value);
        if (Number.isSafeInteger(value) && value > 0 && quantity.checkValidity()) {
          count += value;
          total += Number(row.dataset.price) * value;
        }
      });
      this.querySelector('[data-accessory-count]').textContent = count
        ? `${count} accessoire${count === 1 ? '' : 's'} geselecteerd`
        : 'Geen accessoires geselecteerd';
      this.querySelector('[data-accessory-total]').textContent = this.money.format(total / 100);
      this.button.disabled = this.busy || !this.rows().some(row => row.querySelector('[data-accessory-select]')?.checked);
      this.button.textContent = this.busy ? 'Toevoegen…' : 'Geselecteerde accessoires toevoegen';
      this.button.setAttribute('aria-busy', String(this.busy));
    }

    showError(message, checkCart = false) {
      this.error.textContent = message;
      this.error.hidden = false;
      this.cartLink.hidden = !checkCart;
      this.error.focus();
    }

    async addSelected() {
      if (this.busy || this.root?.dataset.bcNavigating === 'true' || !this.isConnected) return;
      const parentId = this.root?.querySelector('.product-form input[name="id"]')?.value;
      if (parentId && parentId !== this.dataset.parentVariant) {
        this.showError('De uitvoering is gewijzigd. Vernieuw de pagina om de passende accessoires te bekijken.');
        return;
      }
      const items = [];
      for (const row of this.rows()) {
        if (!row.querySelector('[data-accessory-select]')?.checked) continue;
        const quantity = row.querySelector('[data-accessory-quantity]');
        const value = Number(quantity.value);
        if (!quantity.checkValidity() || !Number.isSafeInteger(value) || value < 1) {
          this.showError('Vul voor ieder geselecteerd accessoire een geldig aantal in.');
          quantity.focus();
          quantity.reportValidity();
          return;
        }
        items.push({ id: row.dataset.variantId, quantity: value });
      }
      if (!items.length) return;
      this.error.hidden = true;
      this.cartLink.hidden = true;
      this.busy = true;
      this.sync();
      // One explicit request. Never retry automatically after an uncertain response.
      try {
        const response = await fetch(this.dataset.addUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ items })
        });
        const result = await response.json();
        if (!response.ok || result.status) {
          const detail = typeof result.description === 'string' ? result.description : 'Een geselecteerd accessoire kon niet worden toegevoegd.';
          throw new Error(`${detail} Controleer je winkelwagen voordat je opnieuw probeert.`);
        }
        if (this.isConnected) window.location.assign(this.dataset.cartUrl);
      } catch (error) {
        this.busy = false;
        this.sync();
        this.showError(error instanceof TypeError || error instanceof SyntaxError
          ? 'Toevoegen kon niet worden bevestigd. Controleer je winkelwagen voordat je opnieuw probeert.'
          : error.message, true);
      }
    }

    disconnectedCallback() { this.controller?.abort(); }
  });
}
