const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { Liquid } = require('liquidjs');
const { JSDOM } = require('jsdom');

const root = path.resolve(__dirname, '..');
const candidate = process.env.BC_THEME_PATH;
const baseline = process.env.BC_BASELINE_THEME_PATH;
assert(candidate && baseline, 'Supply isolated candidate and fresh baseline theme paths');
const dossier = JSON.parse(fs.readFileSync(path.join(root, 'docs/product-content/wiesbaden/24.3710.json'), 'utf8'));
const proposal = dossier.proposal;
function engine(themePath) {
  const text = fs.readFileSync(path.join(themePath, 'locales/nl.json'), 'utf8');
  const locale = JSON.parse(text.slice(text.indexOf('{')));
  const stripDoc = s => s.replace(/{%[- ]*doc[^%]*%}[\s\S]*?{%[- ]*enddoc[^%]*%}/g, '');
  const e = new Liquid({
    root: path.join(themePath, 'snippets'), extname: '.liquid', relativeReference: false,
    fs: {
      exists: async p => fs.existsSync(p), existsSync: fs.existsSync,
      readFile: async p => stripDoc(fs.readFileSync(p, 'utf8')),
      readFileSync: p => stripDoc(fs.readFileSync(p, 'utf8')),
      resolve: (dir, name, ext) => path.resolve(dir, name.endsWith(ext) ? name : name + ext)
    }
  });
  e.registerFilter('t', key => {
    const value = key.split('.').reduce((v, k) => v?.[k], locale);
    assert.equal(typeof value, 'string', key);
    return value;
  });
  e.registerFilter('metafield_text', field => String(field?.value ?? ''));
  return e;
}
const e = engine(candidate), old = engine(baseline);
const mf = (type, value) => ({type, value});
const product = () => ({
  vendor: 'Wiesbaden', selected_or_first_available_variant: {sku: '24.3710'},
  has_only_default_variant: true, description: proposal.description_html, tags: [],
  metafields: {custom: {
    serie: mf('single_line_text_field', '304'),
    garantie: mf('single_line_text_field', '5 jaar'),
    materiaal: mf('single_line_text_field', 'RVS'),
    complete_specificaties: mf('json', structuredClone(proposal.complete_specifications.value))
  }}
});
const render = (eng,p) => eng.renderFile('bc-product-detail-specs', {
  product:p,section_id:'pilot-test',request:{locale:{iso_code:'nl'}},routes:{collections_url:'/collections'}
});
let groups = 0;
(async () => {
  let p=product();
  const html=await render(e,p);
  const dom = new JSDOM(html).window.document;
  assert.equal(dom.querySelectorAll('.bc-product-specs').length,1);
  const rows=[...dom.querySelectorAll('tr')].filter(r=>r.querySelector('td'));
  assert.equal(rows.length,33);
  for(const [label,value] of proposal.specifications) {
    assert(rows.some(r=>r.querySelector('th').textContent.trim()===label && r.querySelector('td').textContent.trim()===value),label);
  }
  for(const forbidden of ['5 jaar','Grant','EAN','Keramisch','leverancier_voorraad']) assert(!html.includes(forbidden),forbidden);
  assert.equal(dom.querySelectorAll('.bc-product-specs__category a').length,3);
  groups++;
  const cleaned=await e.renderFile('bc-product-description',{product:p});
  assert.equal(cleaned.trim(),proposal.description_html.trim());
  assert(!cleaned.includes('<table>'));
  groups++;
  for(const change of [
    p=>{delete p.metafields.custom.complete_specificaties},
    p=>{p.metafields.custom.complete_specificaties=mf('json',[])},
    p=>{p.metafields.custom.complete_specificaties.type='single_line_text_field'},
    p=>{p.selected_or_first_available_variant.sku='24.3711'},
    p=>{p.has_only_default_variant=false},
    p=>{p.metafields.custom.complete_specificaties.value[0].items[0].value='OTHER'},
    p=>{p.vendor='JEE-O';p.metafields.specs={}},
    p=>{p.vendor='Other'}
  ]) {
    p=product();change(p);
    assert.equal(await render(e,p),await render(old,p),'Fallback must preserve existing output exactly');
    groups++;
  }
  p=product();
  p.metafields.custom.complete_specificaties.value[0].items.push(
    {key:'ean',label:'PRIVATE',value:'DO-NOT-SHOW'},
    {key:'garantie',label:'Garantie',value:'5 jaar'},
    {key:'leverancier_voorraad',label:'Voorraad',value:'DO-NOT-SHOW'}
  );
  assert(!(await render(e,p)).includes('DO-NOT-SHOW'));
  assert(!(await render(e,p)).includes('5 jaar'));
  groups++;
  p=product();
  const items=p.metafields.custom.complete_specificaties.value[0].items;
  items.push({key:'coldstart',label:'Bool false',value:false},{key:'aantal_grepen',label:'Numeric zero',value:0});
  const typed=new JSDOM(await render(e,p)).window.document;
  const typedRows=[...typed.querySelectorAll('tr')];
  assert(typedRows.some(r=>r.textContent.includes('Bool false')&&r.textContent.includes('Nee')));
  assert(typedRows.some(r=>r.textContent.includes('Numeric zero')&&r.querySelector('td')?.textContent.trim()==='0'));
  groups++;
  p=product();
  p.metafields.custom.complete_specificaties.value[1].group='<script>group</script>';
  p.metafields.custom.complete_specificaties.value[1].items[0].label='<script>label</script>';
  p.metafields.custom.complete_specificaties.value[1].items[0].value='<img src=x onerror=alert(1)>';
  const escaped=await render(e,p);
  assert(!escaped.includes('<script>')&&!escaped.includes('<img'));
  assert(escaped.includes('&lt;script&gt;'));
  groups++;
  assert.equal(proposal.handle_change,false);
  assert.equal(proposal.filters.proposed_values.serie,'304');
  assert.equal(proposal.filters.proposed_values.materiaal,'RVS');
  assert.equal(proposal.filters.proposed_values.aantal_kraangaten,1);
  assert(!('values_sha256' in proposal.filters.candidate_without_digest));
  assert(!/Grant|EAN|\b\d{13}\b/.test(JSON.stringify(proposal)));
  groups++;
  if(process.env.BC_RENDER_OUTPUT) fs.writeFileSync(process.env.BC_RENDER_OUTPUT,html,'utf8');
  console.log(`PASS: ${groups} test groups; 33 rows, fallback equivalence, false/zero, escaping, no unverified claims.`);
})().catch(err=>{console.error(err);process.exitCode=1});
