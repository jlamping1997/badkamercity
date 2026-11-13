import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';

const require = createRequire(import.meta.url);
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const core = require(path.join(root, 'shopify/current/assets/bc-porcelanosa-core.js'));
const directory = process.argv[2];
if (!directory) throw new Error('Usage: node scripts/cottoceramix/audit_choice_matrix.mjs PRIVATE_PLAN_DIRECTORY');
const rows = JSON.parse(fs.readFileSync(fs.statSync(directory).isFile() ? directory : path.join(directory, 'products.json'), 'utf8'));
const groups = new Map();
for (const row of rows) {
  const mf = Object.fromEntries(row.input.metafields.map(value => [value.namespace + '.' + value.key, value.value]));
  const product = {
    sku: row.sku, type: mf['tiles.application'], color: mf['tiles.color'],
    finish: mf['tiles.execution'].split(' · ').filter(value => !value.includes(' mm')).join(' · '),
    size: mf['tiles.size'], thickness: Number(mf['bc_filters.tegel_dikte_mm'] || 0),
    area: Number(mf['bc_filters.tegel_breedte_mm'] || 0) * Number(mf['bc_filters.tegel_lengte_mm'] || 0) / 100,
  };
  if (!groups.has(row.group_key)) groups.set(row.group_key, []);
  groups.get(row.group_key).push(product);
}
let choices = 0;
let exactPreservationChecks = 0;
const fallbackChanges = [];
for (const [key, products] of groups) {
  assert(products.length <= 50, key + ': group exceeds renderer limit');
  assert.equal(new Set(products.map(product => JSON.stringify(core.fields.map(field => product[field])))).size, products.length, key + ': ambiguous runtime choice vectors');
  for (const current of products) {
    for (const field of core.fields) {
      const index = core.fields.indexOf(field);
      for (const option of core.choices(products, current, field)) {
        const result = core.choose(products, current, field, option[field]);
        assert(result && products.includes(result), key + ': choice left group');
        assert.equal(String(result[field]), String(option[field]), key + ': selected value mismatch');
        for (const prefix of core.fields.slice(0, index)) assert.equal(String(result[prefix]), String(current[prefix]), key + ': upstream selection changed');
        const exact = products.find(candidate => core.fields.every(name => String(candidate[name]) === String(name === field ? option[field] : current[name])));
        if (exact) {
          assert.equal(result.sku, exact.sku, key + ': available combination not preserved');
          exactPreservationChecks++;
        } else {
          const changed = core.fields.filter(name => name !== field && String(result[name]) !== String(current[name]));
          fallbackChanges.push({group: key, from: current.sku, field, value: option[field], to: result.sku, otherDimensionsChanged: changed});
        }
        choices++;
      }
    }
  }
}
console.log(JSON.stringify({status: 'PASS', groups: groups.size, products: rows.length, choiceChecks: choices, exactCombinationPreservationChecks: exactPreservationChecks, nonCartesianFallbacks: fallbackChanges.length, fallbackChanges, scope: 'Real deployed selection core with planned Shopify metafield values; no source-menu equivalence, media-ready or browser claim.'}, null, 2));
