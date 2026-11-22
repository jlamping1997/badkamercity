(() => {
  if (customElements.get('bc-kitkat-guide')) return;

  const queryKeys = { material: 'kg_materiaal', size: 'kg_maat', series: 'kg_serie', color: 'kg_kleur', finish: 'kg_afwerking' };
  const dimensions = Object.keys(queryKeys);

  class KitKatGuide extends HTMLElement {
    connectedCallback() {
      if (this.ready) return;
      this.form = this.querySelector('[data-kg-form]');
      this.list = this.querySelector('[data-kg-list]');
      if (!this.form || !this.list) return;
      this.ready = true;
      this.controls = Object.fromEntries(dimensions.map(key => [key, this.form.querySelector('[data-kg-filter="' + key + '"]')]));
      this.totalPages = Number(this.dataset.kgPages) || 1;
      this.startPage = Number(this.dataset.kgPage) || 1;
      this.pages = new Map([[this.startPage, this.records(this.list)]]);
      this.allFetched = this.totalPages === 1;
      this.loading = false;
      this.failed = false;
      this.status = this.querySelector('[data-kg-result]');
      this.empty = this.querySelector('[data-kg-empty]');
      this.pager = this.querySelector('[data-kg-pager]');
      this.clear = this.querySelector('[data-kg-clear]');

      const params = new URL(window.location.href).searchParams;
      for (const [key, select] of Object.entries(this.controls)) {
        for (const option of select.options) option.dataset.label = option.textContent.trim();
        let requested = params.get(queryKeys[key]);
        if (key === 'size' && requested === '22') requested = '22-145';
        if (requested && Array.from(select.options).some(option => option.value === requested)) select.value = requested;
      }

      this.form.addEventListener('submit', event => event.preventDefault());
      this.form.addEventListener('change', () => this.change());
      this.form.addEventListener('reset', event => {
        event.preventDefault();
        this.resetSelection();
      });
      this.querySelector('[data-kg-reset]').addEventListener('click', () => {
        this.resetSelection();
        this.controls.size.focus();
      });
      for (const choice of this.querySelectorAll('[data-kg-choose]')) {
        choice.hidden = false;
        choice.addEventListener('click', () => {
          for (const select of Object.values(this.controls)) select.value = '';
          this.controls.series.value = choice.dataset.kgChoose;
          this.change();
          const head = this.querySelector('.kg-catalog h2');
          head.focus({ preventScroll: true });
          this.querySelector('.kg-catalog').scrollIntoView({ block: 'start' });
        });
      }
      for (const fallback of this.querySelectorAll('[data-kg-fallback]')) fallback.hidden = true;
      this.form.hidden = false;
      this.refresh();
    }

    records(list) {
      return Array.from(list.querySelectorAll('[data-kg-item]'), node => ({
        node,
        id: node.dataset.kgItem,
        material: [node.dataset.kgMaterial],
        size: [node.dataset.kgSize],
        series: [node.dataset.kgSeries],
        color: node.dataset.kgColor.split(','),
        finish: [node.dataset.kgFinish]
      }));
    }

    resetSelection() {
      for (const select of Object.values(this.controls)) select.value = '';
      this.change();
    }

    change() {
      const url = new URL(window.location.href);
      for (const [key, select] of Object.entries(this.controls)) {
        if (select.value) url.searchParams.set(queryKeys[key], select.value);
        else url.searchParams.delete(queryKeys[key]);
      }
      history.replaceState(history.state, '', url);
      this.failed = false;
      this.refresh();
    }

    matches(item, choices, except) {
      return dimensions.every(key => key === except || !choices[key] || item[key].includes(choices[key]));
    }

    refresh() {
      const choices = Object.fromEntries(dimensions.map(key => [key, this.controls[key].value]));
      const filtering = Object.values(choices).some(Boolean);
      const rows = Array.from(this.pages.values()).flat();
      let shown = 0;
      for (const [page, pageRows] of this.pages) {
        for (const row of pageRows) {
          row.node.hidden = filtering ? !this.matches(row, choices) : page !== this.startPage;
          if (!row.node.hidden) shown++;
        }
      }
      for (const key of dimensions) {
        const eligible = new Map();
        for (const row of rows) {
          if (!this.matches(row, choices, key)) continue;
          for (const value of row[key]) eligible.set(value, (eligible.get(value) || 0) + 1);
        }
        for (const option of this.controls[key].options) {
          if (!option.value) continue;
          const count = eligible.get(option.value) || 0;
          option.disabled = this.allFetched && count === 0 && option.value !== choices[key];
          option.hidden = option.value === 'overig' && this.allFetched && !rows.some(row => row[key].includes('overig'));
          option.textContent = this.allFetched ? option.dataset.label + ' (' + count + ')' : option.dataset.label;
        }
      }
      const count = filtering ? shown : Number(this.dataset.kgTotal);
      this.status.textContent = count + ' ' + (count === 1 ? this.dataset.kgOne : this.dataset.kgMany);
      this.clear.disabled = !filtering;
      this.empty.hidden = !filtering || !this.allFetched || shown > 0;
      if (this.pager) this.pager.hidden = filtering && this.allFetched;
      if (filtering && !this.allFetched) {
        this.status.textContent += '. ' + (this.failed ? this.dataset.kgPartial : this.dataset.kgLoading);
        if (!this.loading && !this.failed) this.loadPages();
      }
    }

    async loadPages() {
      this.loading = true;
      const seen = new Set(Array.from(this.pages.values()).flat().map(row => row.id));
      try {
        for (let page = 1; page <= this.totalPages; page++) {
          if (this.pages.has(page)) continue;
          const url = new URL(window.location.href);
          url.hash = '';
          for (const param of Object.values(queryKeys)) url.searchParams.delete(param);
          url.searchParams.set(this.dataset.kgPageParam, String(page));
          url.searchParams.set('section_id', this.dataset.kgSection);
          const response = await fetch(url, { headers: { Accept: 'text/html' } });
          if (!response.ok) throw new Error('Page unavailable');
          const documentPage = new DOMParser().parseFromString(await response.text(), 'text/html');
          const source = documentPage.querySelector('[data-kg-list]');
          const section = source && source.closest('[data-kg-page]');
          if (!section || Number(section.dataset.kgPage) !== page) throw new Error('Unexpected collection page');
          const rows = this.records(source).filter(row => {
            if (seen.has(row.id)) return false;
            seen.add(row.id);
            row.node.hidden = true;
            return true;
          });
          this.pages.set(page, rows);
          this.list.append(...rows.map(row => row.node));
        }
        const ordered = [...this.pages].sort((a,b) => a[0] - b[0]);
        this.list.replaceChildren(...ordered.flatMap(([, rows]) => rows.map(row => row.node)));
        this.allFetched = true;
      } catch {
        this.failed = true;
      } finally {
        this.loading = false;
        this.refresh();
      }
    }
  }

  customElements.define('bc-kitkat-guide', KitKatGuide);
})();
