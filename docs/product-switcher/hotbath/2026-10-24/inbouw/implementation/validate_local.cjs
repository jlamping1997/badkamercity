/* Local-only validation. Does not read user instructions or invoke toolkit wrappers. */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { fileURLToPath } = require('node:url');
const { createRequire } = require('node:module');
const { spawnSync } = require('node:child_process');
const root = __dirname;
const packageRoot = path.join(root, '../tmp/shopify-validation');
const localRequire = createRequire(path.join(packageRoot, 'package.json'));

// Defense in depth: deny outbound access before loading the validator dependency tree.
const blockedNetworkAttempts = [];
function denyNetwork(api) {
  return () => { blockedNetworkAttempts.push(api); throw new Error('LOCAL_ONLY_NETWORK_DISABLED:' + api); };
}
globalThis.fetch = denyNetwork('fetch');
for (const name of ['node:http', 'node:https']) {
  const mod = require(name);
  mod.request = denyNetwork(name + '.request');
  mod.get = denyNetwork(name + '.get');
}
require('node:net').Socket.prototype.connect = denyNetwork('net.Socket.connect');
require('node:tls').connect = denyNetwork('tls.connect');
require('node:dgram').Socket.prototype.send = denyNetwork('dgram.Socket.send');
process.env.OPT_OUT_INSTRUMENTATION = 'true';
process.env.DO_NOT_TRACK = '1';

// Bypass docs updater entirely: all documentation and schemas come from installed JSON.
const docs = localRequire('@shopify/theme-check-docs-updater');
const docsData = path.join(packageRoot, 'node_modules/@shopify/theme-check-docs-updater/data');
const readBundled = name => fs.promises.readFile(path.join(docsData, name), 'utf8');
docs.ThemeLiquidDocsManager.prototype.loaders = function (name) {
  return [() => readBundled(name + '.json')];
};
docs.ThemeLiquidDocsManager.prototype.schemaLoaders = function (relativeUri) {
  return [() => readBundled(path.basename(relativeUri))];
};

const checker = localRequire('@shopify/theme-check-node');
const postcss = localRequire('postcss');
const scratch = path.join(root, 'local-validation-snapshots');
fs.mkdirSync(scratch, { recursive: true });
const baseline = path.join(scratch, 'baseline');
const candidate = path.join(scratch, 'candidate');
for (const target of [baseline, candidate]) {
  fs.rmSync(target, { recursive: true, force: true });
  fs.cpSync(path.join(root, 'source-theme'), target, { recursive: true });
}
fs.cpSync(path.join(root, 'theme'), candidate, { recursive: true });

function walk(dir, rel = '') {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const name = path.join(rel, entry.name);
    return entry.isDirectory() ? walk(path.join(dir, entry.name), name) : [name];
  });
}
const files = walk(path.join(root, 'theme')).sort();
function normalize(offense, base) {
  return { ...offense, uri: path.relative(base, fileURLToPath(offense.uri)) };
}
const key = offense => JSON.stringify([offense.uri, offense.code, offense.message, offense.severity]);

async function main() {
  const config = path.join(packageRoot, 'node_modules/@shopify/theme-check-node/configs/recommended.yml');
  const before = await checker.themeCheckRun(baseline, config);
  const after = await checker.themeCheckRun(candidate, config);
  const inheritedKeys = new Set(before.offenses.map(o => key(normalize(o, baseline))));
  const offenses = after.offenses.map(o => normalize(o, candidate))
    .filter(o => files.includes(o.uri))
    .map(o => ({ ...o, inherited_from_fresh_source: inheritedKeys.has(key(o)) }));
  const syntaxChecks = [];
  for (const file of files) {
    const absolute = path.join(root, 'theme', file);
    if (file.endsWith('.js')) {
      const run = spawnSync(process.execPath, ['--check', absolute], { encoding: 'utf8' });
      syntaxChecks.push({ file, check: 'node --check (parse only; no execution)', pass: run.status === 0, output: run.stderr.trim() });
    } else if (file.endsWith('.css')) {
      try { postcss.parse(fs.readFileSync(absolute, 'utf8'), { from: absolute }); syntaxChecks.push({ file, check: 'PostCSS parser', pass: true }); }
      catch (error) { syntaxChecks.push({ file, check: 'PostCSS parser', pass: false, output: error.message }); }
    } else if (file.endsWith('.json')) {
      try { const source = fs.readFileSync(absolute, 'utf8'); JSON.parse(source.slice(source.indexOf('{'))); syntaxChecks.push({ file, check: 'JSON parser after Shopify generated comment header', pass: true }); }
      catch (error) { syntaxChecks.push({ file, check: 'JSON parser', pass: false, output: error.message }); }
    }
  }
  const addonLiquid = fs.readFileSync(path.join(root, 'theme/snippets/bc-product-inbouw.liquid'), 'utf8');
  const ajaxEndpoint = { file: 'snippets/bc-product-inbouw.liquid', explicit_localized_json_endpoint: /data-add-url="\{\{\s*routes\.cart_add_url\s*\}\}\.js"/.test(addonLiquid), expectation: '{{ routes.cart_add_url }}.js matches the existing accessories implementation and explicit Ajax JSON endpoint.' };
  const newErrors = offenses.filter(o => !o.inherited_from_fresh_source && o.severity === checker.Severity.ERROR);
  const report = {
    schema: 'hotbath-local-theme-validation-v1', created_at: new Date().toISOString(),
    status: newErrors.length || syntaxChecks.some(x => !x.pass) || !ajaxEndpoint.explicit_localized_json_endpoint ? 'FINDINGS_REQUIRE_REVIEW' : 'PASS_LOCAL_CHECKS_WITH_BROWSER_QA_REMAINING',
    validator: { package: '@shopify/theme-check-node', version: localRequire('@shopify/theme-check-node/package.json').version, entrypoint: 'themeCheckRun directly; no validate.mjs wrapper', docs: 'installed bundled JSON only', config: 'installed recommended.yml' },
    privacy: { user_instructions_read: false, prompt_argument_supplied: false, telemetry_wrapper_loaded: false, outbound_network_disabled: true, blocked_network_attempts: blockedNetworkAttempts },
    scope: { changed_files: files, fresh_source_files_available: walk(path.join(root, 'source-theme')).length, full_remote_theme_validated: false, production_files_edited: false },
    summary: { new_error_count: newErrors.length, new_warning_count: offenses.filter(o => !o.inherited_from_fresh_source && o.severity !== checker.Severity.ERROR).length, inherited_findings_count: offenses.filter(o => o.inherited_from_fresh_source).length, parser_checks_passed: syntaxChecks.filter(x => x.pass).length, parser_checks_failed: syntaxChecks.filter(x => !x.pass).length },
    ajax_endpoint: ajaxEndpoint, syntax_checks: syntaxChecks, changed_file_findings: offenses,
    limitations: ['Only the available 15 fresh source files plus the 8-file patch are present locally. Missing dependencies inherited from this partial snapshot are reported, not hidden.', 'Theme-check validates Liquid/JSON statically; JS and CSS are parsed separately. Browser behavior, actual Shopify Liquid rendering, inventory, transport and accessibility interactions still require browser QA.', 'Bundled documentation is installed with version 3.30.1; no online schema refresh was attempted.'],
    file_sha256: Object.fromEntries(files.map(file => [file, crypto.createHash('sha256').update(fs.readFileSync(path.join(root, 'theme', file))).digest('hex')]))
  };
  fs.writeFileSync(path.join(root, 'local-validation.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify({ status: report.status, ...report.summary, explicit_ajax_json_endpoint: ajaxEndpoint.explicit_localized_json_endpoint, blocked_network_attempts: blockedNetworkAttempts.length, findings: offenses.filter(o => !o.inherited_from_fresh_source).map(o => ({ file: o.uri, code: o.code, severity: o.severity, message: o.message, line: o.start.line + 1 })) }, null, 2));
}
main().catch(error => { console.error(error); process.exitCode = 1; });
