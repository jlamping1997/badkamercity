const { Liquid } = require('liquidjs');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const root = process.env.BC_THEME_PATH || path.join(__dirname, '..');
const stripDoc = (s) => s.replace(/\{%[- ]*doc[^%]*%\}[\s\S]*?\{%[- ]*enddoc[^%]*%\}/g, '');
const read = (p) => stripDoc(fs.readFileSync(p, 'utf8'));
const localeSource = fs.readFileSync(path.join(root, 'locales/nl.json'), 'utf8');
const locale = JSON.parse(localeSource.slice(localeSource.indexOf('{')));
const engine = new Liquid({
  root: path.join(root, 'snippets'), extname: '.liquid', relativeReference: false,
  globals: { request: { locale: { iso_code: 'nl' } } },
  fs: {
    exists: async (p) => fs.existsSync(p), existsSync: fs.existsSync,
    readFile: async (p) => read(p), readFileSync: read,
    resolve: (dir, name, ext) => path.resolve(dir, name.endsWith(ext) ? name : name + ext)
  }
});
engine.registerFilter('t', (key) => {
  const result = key.split('.').reduce((v, part) => v?.[part], locale);
  assert.equal(typeof result, 'string', 'Missing translation: ' + key);
  return result;
});
engine.registerFilter('metafield_text', (m) => String(m?.value ?? ''));
const mf = (type, value) => ({ type, value });
const prod = (vendor, namespace, values, sku = 'A1') => ({
  vendor, selected_or_first_available_variant: { sku }, has_only_default_variant: true,
  metafields: { [namespace]: values }, description: '', tags: []
});
const render = (name, product) => engine.renderFile(name, { product, section_id: 'spec-test', request: { locale: { iso_code: 'nl' } } });
const table = (entries) => '<h2>Specificaties</h2><table><tbody>' + entries.map(([k, v]) => '<tr><th scope="row">' + k + '</th><td>' + v + '</td></tr>').join('') + '</tbody></table>';
let checks = 0;
async function main() {
  const w = prod('Wiesbaden', 'custom', {
    materiaal: mf('single_line_text_field', 'RVS'), coldstart: mf('boolean', true),
    met_overloop: mf('boolean', false), breedte_mm: mf('number_decimal', 0),
    hoogte_mm: mf('number_decimal', 183.5), leverancier_voorraad: mf('boolean', true),
    ean: mf('single_line_text_field', 'INTERNAL-ONLY')
  });
  let html = await render('bc-product-detail-specs', w);
  for (const value of ['RVS', 'Coldstart', '>Ja<', 'Met overloop', '>Nee<', '>0<', '183,5']) assert(html.includes(value), value);
  assert(!html.includes('INTERNAL-ONLY') && !html.includes('leverancier_voorraad'));
  assert(!html.includes('Translation missing'));
  checks += 3;
  const j = prod('JEE-O', 'specs', { materiaal_kraan: mf('single_line_text_field', 'RVS 304'), kleur: mf('single_line_text_field', 'Gun Metal'), hoogte_uitloop_mm: mf('number_decimal', 250), met_plug: mf('boolean', false) });
  j.metafields.custom = { kleur: mf('single_line_text_field', 'WRONG SOURCE') };
  html = await render('bc-product-detail-specs', j);
  assert(html.includes('RVS 304') && html.includes('Gun Metal') && html.includes('Uitloophoogte (mm)') && html.includes('>250<') && html.includes('>Nee<'));
  assert(!html.includes('WRONG SOURCE') && !html.includes('Coldstart'));
  checks += 2;
  w.metafields.custom.materiaal.value = '<script>unsafe</script>';
  html = await render('bc-product-detail-specs', w);
  assert(!html.includes('<script>') && html.includes('&lt;script&gt;'));
  checks++;
  w.metafields.custom.materiaal.value = 'RVS';
  w.description = 'Eigen omschrijving' + table([['Artikelnummer', 'A1'], ['Materiaal', 'RVS'], ['Met overloop', 'Nee'], ['Breedte (mm)', '0'], ['EAN', '123']]) + '<h2>Technische documenten</h2><p>Bewaren</p>';
  const cleaned = await render('bc-product-description', w);
  assert.equal(cleaned, 'Eigen omschrijving<h2>Technische documenten</h2><p>Bewaren</p>');
  checks++;
  for (const entries of [
    [['Artikelnummer', 'WRONG'], ['Materiaal', 'RVS']],
    [['Artikelnummer', 'A1'], ['Onbekende eigenschap', 'Bewaren']],
    [['Artikelnummer', 'A1'], ['Materiaal', 'ANDERE WAARDE']],
    [['Artikelnummer', 'A1'], ['Breedte (mm)', 'onbekend']]
  ]) {
    w.description = 'Tekst' + table(entries);
    assert.equal(await render('bc-product-description', w), w.description);
    checks++;
  }
  for (const vendor of ['JEE-O', 'Hotbath', 'Sunshower']) {
    w.vendor = vendor;
    assert.equal(await render('bc-product-description', w), w.description);
    checks++;
  }
  const empty = prod('Wiesbaden', 'custom', {});
  html = await render('bc-product-detail-specs', empty);
  assert(!html.includes('Afmetingen</th>') && html.includes('Artikelnummer'));
  checks++;
  if (process.env.BC_SPEC_SNAPSHOT) {
    const sample = JSON.parse(fs.readFileSync(process.env.BC_SPEC_SNAPSHOT, 'utf8'));
    for (const [brand, data] of Object.entries(sample)) {
      for (const source of data.nodes) {
        const product = prod(source.vendor, 'custom', {}, source.metafields.nodes.find((m) => m.key === 'artikelnummer')?.value || source.handle);
        product.description = source.descriptionHtml;
        for (const m of source.metafields.nodes) {
          product.metafields[m.namespace] ||= {};
          let value = m.value;
          if (['boolean', 'number_decimal', 'number_integer', 'json'].includes(m.type) || m.type.startsWith('list.')) value = JSON.parse(value);
          product.metafields[m.namespace][m.key] = mf(m.type, value);
        }
        html = await render('bc-product-detail-specs', product);
        assert(!html.includes('Translation missing'));
        for (const row of html.matchAll(/<td class="bc-product-specs__value">([^<]*)<\/td>/g)) assert(row[1].trim());
        if (brand === 'wiesbaden') {
          const description = await render('bc-product-description', product);
          assert(!description.includes('<h2>Specificaties</h2><table>'), source.handle);
          const suffix = product.description.split('</table>').slice(1).join('</table>');
          assert(description.endsWith(suffix), 'Description suffix retained: ' + source.handle);
        }
        checks++;
      }
    }
  }
  console.log(checks + ' product specification and description checks passed.');
}
main().catch((e) => { console.error(e); process.exitCode = 1; });
