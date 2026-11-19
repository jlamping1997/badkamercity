const { Liquid } = require('liquidjs');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const root = process.env.BC_THEME_PATH || path.join(__dirname, '..');
const baseline = process.env.BC_BASELINE_THEME_PATH;
assert(baseline, 'Set BC_BASELINE_THEME_PATH to compare the navigation contract');
const menu = JSON.parse(fs.readFileSync(path.join(__dirname, '../docs/design/mobile-subcategories-2026-10-17/menu-snapshot.json'), 'utf8')).menu;
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
function source(dir, part) {
  const code = read(path.join(dir, 'snippets/header-drawer.liquid'));
  if (part === 'panels') {
    // LiquidJS lacks Shopify's forloop.parentloop; emulate it only in this fixture.
    // Real Shopify panel IDs are checked separately through the storefront DOM.
    return code.slice(code.indexOf('\n        {%- for link in section.settings.menu.links -%}'))
      .replace('{%- for link in section.settings.menu.links -%}', '{%- for link in section.settings.menu.links -%}{% assign fixture_parent_index = forloop.index %}')
      .replaceAll('forloop.parentloop.index', 'fixture_parent_index');
  }
  const start = code.indexOf('<nav class="bc-mobile-drawer__navigation"');
  return code.slice(start, code.indexOf('</nav>', start) + 6);
}
const attribute = (tag, name) => tag.match(new RegExp(`${name}="([^"]*)"`))?.[1];
function contract(html) {
  return [...html.matchAll(/<(button|a|div)\b[^>]*>/g)].filter(([tag, type]) => type !== 'div' || tag.includes('data-bc-mobile-panel-id')).map(([tag, type]) => ({
    type, href: attribute(tag, 'href'), next: attribute(tag, 'data-bc-mobile-next'),
    panel: attribute(tag, 'data-bc-mobile-panel-id'), back: tag.includes('data-bc-mobile-back'), current: attribute(tag, 'aria-current')
  }));
}
const makeLink = (item, activeUrl) => ({
  title: item.title, url: item.url, current: item.url === activeUrl,
  object: { handle: item.url.split('/').pop() }, links: (item.items || []).map(child => makeLink(child, activeUrl))
});
async function main() {
  let checkedPanels = 0;
  for (const activeUrl of ['/collections/keukenkranen', '/collections/douchesets']) {
    const context = { section: { id: 'submenu-test', settings: { menu: { links: menu.items.map(item => makeLink(item, activeUrl)) } } } };
    const after = await engineFor(root).parseAndRender(source(root, 'panels'), context);
    const before = await engineFor(baseline).parseAndRender(source(baseline, 'panels'), context);
    assert.deepEqual(contract(after), contract(before), 'All destinations, panel IDs, back controls and active links must be preserved');
    const controls = contract(after);
    const panels = controls.filter(x => x.panel).map(x => x.panel);
    assert.equal(new Set(panels).size, panels.length, 'No duplicate panel IDs');
    assert.equal(controls.filter(x => x.back).length, panels.length, 'Each submenu needs its original back control');
    const rootHtml = await engineFor(root).parseAndRender(source(root, 'root'), context);
    for (const item of [...controls, ...contract(rootHtml)].filter(x => x.next)) assert(panels.includes(item.next), `Unresolved target: ${item.next}`);
    assert(!after.includes('<svg'), 'Submenus must contain no category SVGs');
    assert(!after.includes('row-icon') && !after.includes('--with-icon'));
    assert(controls.some(x => x.href === activeUrl && x.current === 'page'), `Active link preserved for ${activeUrl}`);
    assert(after.includes('Bekijk alle kranen'));
    assert(after.includes('Bekijk alles in Douche') && !after.includes('Bekijk alle douche<'));
    assert(after.includes('Bekijk alles in Meer') && !after.includes('Bekijk alle meer<'));
    checkedPanels = panels.length;
  }
  const special = { title: 'Kranen & accessoires <nieuw>', url: '/collections/example?tag=a&sort=b', items: [{ title: 'Een bijzonder lange categorie met extra uitleg', url: '/collections/long', items: [] }] };
  const html = await engineFor(root).parseAndRender(source(root, 'panels'), { section: { id: 'escape-test', settings: { menu: { links: [makeLink(special, '')] } } } });
  assert(html.includes('Kranen &amp; accessoires &lt;nieuw&gt;'));
  assert(!html.includes('<nieuw>'), 'Labels must remain escaped');
  console.log(`PASS: ${checkedPanels} subpanels; all menu targets/back controls and 2 active-link cases preserved; no submenu SVGs; CTA grammar/escaping checked`);
}
main().catch(error => { console.error(error); process.exitCode = 1; });
