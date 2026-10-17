const { Liquid } = require('liquidjs');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const root = process.env.BC_THEME_PATH || path.join(__dirname, '..');
const baseline = process.env.BC_BASELINE_THEME_PATH;
const read = p => fs.readFileSync(p, 'utf8').replace(/\{%[- ]*doc[^%]*%\}[\s\S]*?\{%[- ]*enddoc[^%]*%\}/g, '');
function engineFor(dir) {
  const engine = new Liquid({
    root: path.join(dir, 'snippets'), extname: '.liquid', relativeReference: false,
    fs: {
      exists: async p => fs.existsSync(p), existsSync: fs.existsSync,
      readFile: async p => read(p), readFileSync: read,
      resolve: (d, n, ext) => path.resolve(d, n.endsWith(ext) ? n : n + ext)
    }
  });
  engine.registerFilter('inline_asset_content', name => fs.readFileSync(path.join(dir, 'assets', name), 'utf8'));
  engine.registerFilter('handleize', value => value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''));
  engine.registerFilter('t', key => key);
  return engine;
}
function nav(dir) {
  const source = read(path.join(dir, 'snippets/header-drawer.liquid'));
  const start = source.indexOf('<nav class="bc-mobile-drawer__navigation"');
  return source.slice(start, source.indexOf('</nav>', start) + 6);
}
function routing(html) {
  return [...html.matchAll(/<(button|a)\b[^>]*>/g)].map(([tag, type]) => ({
    type,
    href: tag.match(/href="([^"]*)"/)?.[1],
    next: tag.match(/data-bc-mobile-next="([^"]*)"/)?.[1],
    current: tag.match(/aria-current="([^"]*)"/)?.[1]
  }));
}
async function main() {
  const engine = engineFor(root);
  const handles = ['badkamermeubels', 'kranen', 'toiletten', 'wastafels', 'douches', 'baden', 'spiegels', 'accessoires', 'tegels', 'badkamerverlichting', 'verwarming', 'meer', 'outlet'];
  for (const handle of handles) {
    const svg = await engine.renderFile('bc-mobile-category-icon', { handle });
    assert.equal(svg.trim(), fs.readFileSync(path.join(root, 'assets', `bc-nav-${handle}.svg`), 'utf8').trim());
    assert(svg.includes('aria-hidden="true"') && svg.includes('focusable="false"'));
    assert(!/<script|<image|href=|\bon\w+=/.test(svg));
  }
  for (const [alias, handle] of [['douche', 'douches'], ['spiegels-en-spiegelkasten', 'spiegels'], ['badkamer-verlichting', 'badkamerverlichting'], ['verlichting', 'badkamerverlichting'], ['badkameraccessoires', 'accessoires'], ['badkamer-accessoires', 'accessoires']]) {
    assert.equal(await engine.renderFile('bc-mobile-category-icon', { handle: alias }), await engine.renderFile('bc-mobile-category-icon', { handle }));
  }
  assert.equal(await engine.renderFile('bc-mobile-category-icon', { handle: 'onbekende-categorie' }), '');
  const snapshot = JSON.parse(fs.readFileSync(path.join(__dirname, '../docs/design/mobile-category-icons-2026-10-17/root-menu-snapshot.json'), 'utf8'));
  const links = snapshot.items.map((item, i) => ({
    title: item.title, object: { handle: item.url.split('/').pop() },
    url: item.url, current: i === 12,
    links: item.hasChildren ? [{ title: 'Kind', url: '/collections/kind' }] : []
  }));
  links.push({ title: 'Onbekende categorie', object: { handle: 'onbekende-categorie' }, url: '/collections/onbekende-categorie', links: [] });
  links.push({ title: 'Kranen', object: { handle: 'custom-collection-handle' }, url: '/collections/custom-collection-handle', links: [] });
  const context = { section: { id: 'mobile-test', settings: { menu: { links } } } };
  const html = await engine.parseAndRender(nav(root), context);
  assert.equal((html.match(/bc-mobile-drawer__row-icon--category/g) || []).length, 14);
  assert.equal((html.match(/viewBox="0 0 32 32"/g) || []).length, 14);
  const items = html.split('<li class="bc-mobile-drawer__item">').slice(1);
  assert(!items[13].includes('--category'), 'Unknown category must keep original styling');
  assert(items[14].includes('--category'), 'Recognized title must work with a custom collection handle');
  assert.equal(routing(html)[12].type, 'a', 'Outlet must stay a direct link');
  assert.equal(routing(html)[12].href, '/collections/outlet');
  assert.equal(routing(html)[12].current, 'page');
  if (baseline) {
    const before = await engineFor(baseline).parseAndRender(nav(baseline), context);
    assert.deepEqual(routing(html), routing(before), 'All root destinations and submenu panel targets must remain identical');
    const marker = '          {%- if localization.available_countries.size > 1';
    const source = dir => read(path.join(dir, 'snippets/header-drawer.liquid'));
    assert.equal(source(root).slice(source(root).indexOf(marker)), source(baseline).slice(source(baseline).indexOf(marker)), 'Submenus and navigation controls must stay unchanged');
    for (const file of ['snippets/header-drawer.liquid', 'sections/header.liquid', 'snippets/bc-category-icon.liquid']) {
      assert.deepEqual(fs.readFileSync(path.join(root, file)), fs.readFileSync(path.join(baseline, file)), file + ' must remain byte-identical');
    }
    for (const handle of handles.slice(0, 7)) {
      assert.deepEqual(fs.readFileSync(path.join(root, 'assets', `bc-nav-${handle}.svg`)), fs.readFileSync(path.join(baseline, 'assets', `bc-nav-${handle}.svg`)));
    }
  }
  console.log('PASS: 13 root SVGs, aliases, future fallback, identical menu routing/Outlet link, unchanged first 7 SVGs/header/drawer/shared icons');
}
main().catch(error => { console.error(error); process.exitCode = 1; });
