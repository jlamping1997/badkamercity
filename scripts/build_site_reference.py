#!/usr/bin/env python3
"""Offline, metadata-only site reference. Does not execute source or call Shopify.

Inputs are a separately obtained theme snapshot and manifest.
Admin.md is maintained separately from sanitized read-only evidence. Reports distinguish indexed bytes, manifest-only files and mismatches.
No product records, settings values, HTML bodies or credentials are emitted.
"""
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path

from architecture_scan import parse_json, static_references, classify, mask_comments


def cell(value):
    if value is None:
        return '—'
    return str(value).replace('|', '&#124;').replace('\n', ' ').replace('\r', '')


def code_list(values):
    return ', '.join('`' + cell(v) + '`' for v in sorted(set(values))) or '—'


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def dossier(name):
    n = name.lower()
    if 'footer' in n and not any(x in n for x in ('cart', 'password')):
        return 'FOOTER'
    if any(x in n for x in ('glossary', 'begrip', 'article', 'blog', 'contact', 'advice')):
        return 'CONTENT_AND_FORMS'
    if any(x in n for x in ('customers/', 'account', 'login', 'register', 'password', 'gift_card', '404', 'addresses', 'main-order')):
        return 'ACCOUNTS_AND_SYSTEM_PAGES'
    if any(x in n for x in ('home-', 'index.json')):
        return 'HOMEPAGE'
    if any(x in n for x in ('meubelhub', 'category', 'list-collections', 'brand-directory', 'content-without-styles')):
        return 'COLLECTIONS_AND_HUBS'
    if any(x in n for x in ('external-filter', 'facets', 'mobile-listing', 'search', 'card-', 'card.', 'collection-product-grid')):
        return 'PRODUCT_CARDS_AND_FILTERS'
    if any(x in n for x in ('cart', 'product-form', 'buy-buttons', 'quantity', 'price')):
        return 'CART_AND_FEEDBACK'
    if any(x in n for x in ('choice-data', 'switcher', 'inbouw', 'wiesbaden-color', 'hotbath-menu', 'choice-position', 'sunshower-choice')):
        return 'PRODUCT_CHOICES'
    if any(x in n for x in ('header', 'wishlist', 'localization')):
        return 'NAVIGATION_AND_STORAGE'
    if any(x in n for x in ('product', 'sunshower', 'media', 'photoswipe', 'zoom', 'video', 'pickup', 'swatch')):
        return 'PRODUCT_PAGES'
    if 'locales/' in n or 'meta-tags' in n:
        return 'SEO_AND_LOCALIZATION'
    if n.endswith('.css') or any(x in n for x in ('animation', 'slider', 'slideshow')):
        return 'MOTION_AND_STYLES'
    return 'FOUNDATIONS_AND_TOOLING'


def build(args):
    root, out = args.snapshot.resolve(), args.output.resolve()
    if out == root or root in out.parents:
        raise ValueError('Output may not be inside snapshot')
    manifest = json.loads(args.manifest.read_text())
    records = manifest['files']
    if len({f['filename'] for f in records}) != len(records):
        raise ValueError('Duplicate manifest paths')
    rows, texts, edges, schemas, errors = [], {}, [], {}, []
    for f in sorted(records, key=lambda f: f['filename']):
        name = f['filename']
        if Path(name).is_absolute() or '..' in Path(name).parts:
            raise ValueError('Unsafe source path')
        p = root / name
        row = {'path': name, 'kind': classify(Path(name)), 'expectedMd5': f['checksumMd5'],
               'expectedBytes': int(f['size']), 'dossier': dossier(name), 'sourceStatus': 'MANIFEST_ONLY'}
        if p.is_file():
            raw = p.read_bytes()
            row.update(bytes=len(raw), md5=hashlib.md5(raw).hexdigest(), sha256=hashlib.sha256(raw).hexdigest())
            row['sourceStatus'] = 'BYTE_MATCH' if row['md5'] == f['checksumMd5'] and row['bytes'] == int(f['size']) else 'BYTE_MISMATCH'
            if name.endswith(('.liquid', '.json', '.css', '.js')):
                text = raw.decode('utf-8-sig')
                texts[name] = text
                edges.extend({'source': name, **e} for e in static_references(text, Path(name)))
                row['lines'] = len(text.splitlines())
                if name.endswith('.json'):
                    try:
                        parse_json(text)
                    except ValueError:
                        errors.append({'path': name, 'error': 'JSON_PARSE'})
                match = re.search(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', text, re.S)
                if match:
                    try:
                        schemas[name] = json.loads(match.group(1))
                    except ValueError:
                        errors.append({'path': name, 'error': 'SCHEMA_PARSE'})
        rows.append(row)
    names = {f['path'] for f in rows}
    incoming, outgoing = collections.defaultdict(list), collections.defaultdict(list)
    for e in edges:
        e['resolution'] = 'MANIFEST' if e['target'] in names else 'UNRESOLVED'
        incoming[e['target']].append(e['source'])
        outgoing[e['source']].append(e['target'])
    counts = dict(collections.Counter(f['sourceStatus'] for f in rows))
    common = ('Bronmoment 28 oktober 2026. Gegenereerde letterlijke zoekkaart; geen volledige parser, '
              'runtimebewijs of handmatige review. Dynamische refs, CSS-cascade en platforminjecties apart volgen. '
              'Paden/regelnummers horen bij [bronhashes](source-index.json), niet automatisch bij Git-root.\n')
    write(out/'source-index.json', {'schemaVersion': 1, 'themeId': manifest['theme_id'], 'checkedAt': manifest.get('checkedAt'),
          'counts': counts, 'files': rows, 'parseErrors': errors, 'scope': 'Static byte/source indexing, not runtime or commercial correctness.'})
    write(out/'dependencies.json', {'schemaVersion': 1, 'edges': edges, 'limitations': ['Literal Liquid and JSON section references only.', 'No-reference does not mean unused.', 'Disabled JSON sections are indexed too.']})
    tpl = ['# Alle templates en sectiegroepen', '', common]
    for name, text in sorted(texts.items()):
        if not (name.startswith('templates/') or name in ('sections/header-group.json', 'sections/footer-group.json')):
            continue
        tpl += ['## ' + name, '', '[Functionele uitleg](../components/' + dossier(name) + '.md).', '']
        if name.endswith('.json'):
            d = parse_json(text)
            tpl += ['| Volgorde / ID | Sectie | Uitgeschakeld | Blokken |', '| --- | --- | --- | ---: |']
            for key in d.get('order', []):
                s = d['sections'][key]
                typ = s.get('type', '')
                tpl += [f"| `{cell(key)}` | [{cell(typ)}](sections/{typ}.md) | {str(s.get('disabled',False)).lower()} | {len(s.get('blocks',{}))} |"]
            tpl += ['', 'Aanwezigheid/volgorde is configuratiebewijs. Interne Liquid-guards kunnen een niet-uitgeschakelde sectie alsnog leeg laten.', '']
        else:
            tpl += ['Liquid-template; letterlijke refs: ' + code_list(outgoing[name]) + '.', '', 'QA-/reviewnamen zijn geen bewijs van een actieve publieke producttoewijzing.', '']
    write(out/'TEMPLATES.md', '\n'.join(tpl))
    section_count = sum(n.startswith('sections/') and n.endswith('.liquid') for n in texts)
    section_index = [f'# Alle {section_count} Liquid-secties', '', common, '| Sectie | Dossier | Instellingen | Blocktypen |', '| --- | --- | ---: | --- |']
    def setting_table(settings):
        lines = ['| ID | Type | Label / opties |', '| --- | --- | --- |']
        for s in settings:
            if 'id' not in s:
                continue
            opts = '; '.join(str(x.get('value')) + ': ' + str(x.get('label')) for x in s.get('options', []))
            lines += [f"| `{cell(s['id'])}` | `{cell(s['type'])}` | {cell(s.get('label'))}" + (': ' + cell(opts) if opts else '') + ' |']
        return lines
    for name in sorted(n for n in texts if n.startswith('sections/') and n.endswith('.liquid')):
        stem = Path(name).stem
        text = texts[name]
        clean = mask_comments(text)
        schema = schemas.get(name, {})
        page = ['# ' + stem, '', '**Bron:** `' + name + '`. Bronstatus: ' + next(r['sourceStatus'] for r in rows if r['path']==name) + '.', '',
                '[Functioneel dossier](../../components/' + dossier(name) + '.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)', '',
                'Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.', '',
                '## Koppelingen', '', 'Letterlijke callers: ' + code_list(incoming[name]) + '.', '',
                'Letterlijke uitgaande refs: ' + code_list(outgoing[name]) + '.', '',
                'Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.', '',
                '## Schema-instellingen', ''] + setting_table(schema.get('settings', []))
        for block in schema.get('blocks', []):
            page += ['', '## Blocktype ' + cell(block.get('type')), ''] + setting_table(block.get('settings', []))
        forms = re.findall(r"{%[-]?\s*form\s+['\"]([^'\"]+)", clean)
        events = re.findall(r"addEventListener\s*\(\s*['\"]([^'\"]+)", clean)
        fields = ['.'.join(x) for x in re.findall(r'metafields\.([\w]+)\.([\w]+)', clean)]
        hooks = re.findall(r'\b(data-[a-z][\w-]*)\s*=', clean)
        page += ['', '## Technische ingangen', '', 'Formtypen: ' + code_list(forms) + '.', '', 'Letterlijke events in deze bron: ' + code_list(events) + '.', '',
                 'Letterlijke metafieldkeys: ' + code_list(fields) + '.', '', 'DOM-hooks: ' + code_list(hooks) + '.', '',
                 'Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.', '']
        write(out/'sections'/(stem+'.md'), '\n'.join(page))
        section_index += [f"| [{stem}](sections/{stem}.md) | [{dossier(name)}](../components/{dossier(name)}.md) | {sum('id' in x for x in schema.get('settings',[]))} | {code_list(b.get('type','') for b in schema.get('blocks',[]))} |"]
    write(out/'SECTIONS.md', '\n'.join(section_index)+'\n')
    snippets = ['# Alle snippets', '', common]
    for name in sorted(n for n in texts if n.startswith('snippets/')):
        snippets += ['## ' + name, '', '[Dossier](../components/' + dossier(name) + '.md). Callers: ' + code_list(incoming[name]) + '.', '', 'Uitgaand: ' + code_list(outgoing[name]) + '.', '']
    write(out/'SNIPPETS.md', '\n'.join(snippets))
    assets = ['# Assets, datafamilies en bronstatus', '', common, '| Bestand | Type | Dossier | Bronstatus | Letterlijke callers |', '| --- | --- | --- | --- | --- |']
    groups = collections.Counter()
    for r in rows:
        name = r['path']
        if not name.startswith('assets/'):
            continue
        if r['kind'] in ('generated_choice_data_candidate', 'backup_candidate', 'media_or_font'):
            groups[r['kind']] += 1
            continue
        assets += [f"| `{name}` | {r['kind']} | [{r['dossier']}](../components/{r['dossier']}.md) | {r['sourceStatus']} | {code_list(incoming[name])} |"]
    assets += ['', '## Gegroepeerde families', '', '| Familie | Bestanden | Onderhoud |', '| --- | ---: | --- |']
    for kind, count in sorted(groups.items()):
        assets += [f'| {kind} | {count} | Individuele paden/hashes in source-index.json; keuzedata via DATA_PIPELINES.md, backups niet automatisch verwijderen, media via betrokken renderer. |']
    write(out/'ASSETS.md', '\n'.join(assets)+'\n')
    settings = ['# Globale instellingen en talen', '', common, 'Geen huidige settings_data.json-waarden gepubliceerd. Die body wijkt nog van de Shopify-metadata af.', '']
    for group in parse_json(texts['config/settings_schema.json']):
        if 'settings' in group:
            settings += ['## ' + cell(group.get('name')), ''] + setting_table(group['settings']) + ['']
    locale_rows = [r for r in rows if r['path'].startswith('locales/')]
    settings += ['## Locale-assets', '', 'Er zijn ' + str(len(locale_rows)) + ' locale-assets inclusief editor-schema’s. Dit is niet het aantal gepubliceerde winkeltalen. De actuele Admin-taal is `nl` (primair/gepubliceerd).', '']
    write(out/'SETTINGS.md', '\n'.join(settings))
    write(out/'README.md', '# Technische naslag van de winkel\n\nBronmoment 28 oktober 2026.\n\n'
          + f"Alle **{len(rows)}** manifestpaden zijn geclassificeerd. **{counts.get('BYTE_MATCH',0)}** lokale bronbestanden zijn bytegelijk, **{counts.get('BYTE_MISMATCH',0)}** wijkt af; **{counts.get('MANIFEST_ONLY',0)}** is in deze reconstructie uitsluitend metadata.\n\n"
          + 'Dit is een aanvulling op de eerdere volledige DOC-01-capture en DOC-02-datacontroles bij hetzelfde manifest. Geen nieuwe volledige inhoudsdownload of runtimevrijgave.\n\n'
          + '- [Templates en sectiegroepen](TEMPLATES.md)\n- [Alle secties met instellingen en blocktypen](SECTIONS.md)\n- [Alle snippets en callers](SNIPPETS.md)\n- [Assets en datafamilies](ASSETS.md)\n- [Globale instellingen](SETTINGS.md)\n- [Admin-toewijzingen](ADMIN.md)\n- [Bronstatus per bestand](source-index.json)\n- [Letterlijke afhankelijkheden](dependencies.json)\n\n'
          + 'Rebuild: scripts/build_site_reference.py op de actieve codebranch, met expliciete snapshot/manifest/output. Geen broncode wordt uitgevoerd en geen netwerk of Admin-write wordt gedaan.\n')
    return {'manifestFiles': len(rows), 'sourceCounts': counts, 'sections': len(schemas), 'parseErrors': errors, 'literalEdges': len(edges)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = build(args)
    print(json.dumps(result))
    raise SystemExit(bool(result['parseErrors']))
