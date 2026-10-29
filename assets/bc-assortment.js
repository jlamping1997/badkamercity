if (!customElements.get('bc-assortment')) {
  customElements.define('bc-assortment', class extends HTMLElement {
    connectedCallback() {
      if (this.abort) return;
      this.abort = new AbortController();
      const signal = this.abort.signal;
      this.input = this.querySelector('[data-bca-search]');
      this.departments = [...this.querySelectorAll('[data-bca-department]')];
      this.mobileStates = new Map(this.departments.map(d => [d, false]));
      this.savedStates = null;
      this.media = window.matchMedia('(min-width: 990px)');
      this.onMedia = () => this.layout();
      this.media.addEventListener('change', this.onMedia);
      this.departments.forEach(dept => dept.addEventListener('toggle', () => {
        if (!this.media.matches && !this.input.value.trim()) this.mobileStates.set(dept, dept.open);
      }, { signal }));
      this.input.addEventListener('input', () => this.filter(), { signal });
      this.input.addEventListener('keydown', event => {
        if (event.key === 'Escape' && this.input.value) { event.preventDefault(); this.reset(); }
        if (event.key === 'Enter') {
          event.preventDefault();
          this.querySelector('[data-bca-department]:not([hidden]) a:not([hidden])')?.focus();
        }
      }, { signal });
      this.querySelectorAll('[data-bca-clear], [data-bca-reset]').forEach(button => button.addEventListener('click', () => this.reset(), { signal }));
      this.querySelector('[data-bca-finder]').hidden = false;
      this.layout();
    }
    disconnectedCallback() {
      this.abort?.abort();
      this.media?.removeEventListener('change', this.onMedia);
      this.abort = null;
    }
    layout() {
      this.departments.forEach(dept => {
        const summary = dept.querySelector('summary');
        const fixed = this.media.matches && !dept.classList.contains('bca-department--other');
        summary.tabIndex = fixed ? -1 : 0;
        if (fixed) summary.setAttribute('aria-disabled', 'true'); else summary.removeAttribute('aria-disabled');
        dept.open = fixed || !!this.input.value.trim() || this.mobileStates.get(dept);
      });
    }
    normalize(value) {
      return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('nl').replace(/kranen/g, 'kraan').replace(/\bwc\b/g, 'toilet').replace(/wasbak/g, 'wastafel').replace(/[-&’']/g, ' ').replace(/\s+/g, ' ').trim();
    }
    reset() {
      this.input.value = '';
      this.filter();
      this.input.focus();
    }
    filter() {
      const query = this.normalize(this.input.value);
      const words = query.split(' ').filter(Boolean);
      if (query && !this.savedStates) this.savedStates = new Map(this.departments.map(d => [d, d.open]));
      this.toggleAttribute('data-searching', !!query);
      this.querySelector('[data-bca-overview]').hidden = !!query;
      this.querySelector('[data-bca-promotions]').hidden = !!query;
      this.querySelector('[data-bca-clear]').hidden = !query;
      let total = 0;
      this.departments.forEach(dept => {
        const title = dept.querySelector('summary').textContent;
        const items = [...dept.querySelectorAll('[data-bca-item]')];
        items.forEach(item => {
          const anchor = item.matches('a') ? item : item.querySelector(':scope > a');
          if (!anchor) return;
          let text = title + ' ' + anchor.textContent;
          let parent = item.parentElement?.closest('[data-bca-item]');
          while (parent && dept.contains(parent)) {
            text += ' ' + (parent.querySelector(':scope > a')?.textContent || '');
            parent = parent.parentElement?.closest('[data-bca-item]');
          }
          const normalized = this.normalize(text);
          item.hidden = !!query && !words.every(word => normalized.includes(word));
        });
        [...items].reverse().forEach(item => {
          if (item.hidden && item.querySelector('[data-bca-item]:not([hidden])')) item.hidden = false;
        });
        dept.querySelectorAll('.bca-supplement').forEach(group => { group.hidden = !!query && !group.querySelector('[data-bca-item]:not([hidden])'); });
        const count = items.filter(item => !item.hidden).length;
        total += count;
        dept.hidden = !!query && !count;
        if (query && count) dept.open = true;
        else if (!query && this.savedStates) dept.open = this.media.matches && !dept.classList.contains('bca-department--other') ? true : this.savedStates.get(dept);
      });
      this.querySelector('[data-bca-no-results]').hidden = !query || !!total;
      const status = this.querySelector('[data-bca-status]');
      status.textContent = !query ? '' : total ? status.dataset.results.replace('{count}', total) : status.dataset.empty;
      if (!query) this.savedStates = null;
    }
  });
}
