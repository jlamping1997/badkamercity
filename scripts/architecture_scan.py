#!/usr/bin/env python3
"""Read-only theme inventory. Writes reports only; never calls Shopify or executes theme code."""

import argparse
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

THEME_DIRS = ('assets', 'blocks', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates')
TEXT_SUFFIXES = {'.liquid', '.json', '.js', '.css', '.svg', '.txt'}
OMIT_DIRS = {'.git', 'node_modules', '.venv', 'venv', '__pycache__', '_codex_runs', '.shopify'}


def parse_json(text):
    text = text.lstrip('\ufeff \r\n\t')
    while text.startswith('/*'):
        end = text.find('*/')
        if end == -1:
            raise ValueError('Unclosed leading JSON comment')
        text = text[end + 2:].lstrip()
    return json.loads(text)


def mask_comments(text):
    pattern = r'{%-?\s*(?:comment|doc)\b.*?{%-?\s*end(?:comment|doc)\s*-?%}|<!--.*?-->|/\*.*?\*/'
    return re.sub(pattern, lambda m: re.sub(r'[^\n]', ' ', m.group()), text, flags=re.S)


def classify(path):
    name = path.name.lower()
    if 'backup' in name:
        return 'backup_candidate'
    if name.startswith('bc-choice-data-') and path.suffix == '.json':
        return 'generated_choice_data_candidate'
    if path.suffix == '.json' and path.parts[0] == 'assets':
        return 'asset_data'
    if path.suffix in {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg', '.ico', '.woff', '.woff2'}:
        return 'media_or_font'
    return 'theme_source'


def git_head(root):
    try:
        result = subprocess.run(['git', '-C', str(root), 'rev-parse', 'HEAD'], capture_output=True, text=True)
    except OSError:
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def static_references(text, path):
    clean = mask_comments(text)
    refs = []
    for match in re.finditer(r"{%[-]?\s*(render|include|section|sections|layout)\s+(['\"])([^'\"]+)\2", clean):
        kind, _, name = match.groups()
        folder, suffix = {
            'render': ('snippets', '.liquid'), 'include': ('snippets', '.liquid'),
            'section': ('sections', '.liquid'), 'sections': ('sections', '.json'),
            'layout': ('layout', '.liquid'),
        }[kind]
        refs.append({'target': f'{folder}/{name}{suffix}', 'kind': kind, 'line': clean.count('\n', 0, match.start()) + 1})
    for match in re.finditer(r"(['\"])([^'\"\n]+)\1\s*\|\s*(asset_url|inline_asset_content)\b", clean):
        refs.append({'target': 'assets/' + match.group(2), 'kind': match.group(3), 'line': clean.count('\n', 0, match.start()) + 1})
    if path.suffix == '.json' and path.parts[0] in {'templates', 'sections'}:
        try:
            parsed = parse_json(text)
            for section in parsed.get('sections', {}).values():
                name = section.get('type')
                if isinstance(name, str) and not name.startswith('@'):
                    refs.append({'target': f'sections/{name}.liquid', 'kind': 'json_section', 'line': None})
        except (ValueError, AttributeError):
            pass
    return refs


def scan(theme_root, manifest=None, coverage='unknown', source_label='unknown'):
    paths = sorted(p for folder in THEME_DIRS if (theme_root / folder).is_dir()
                   for p in (theme_root / folder).rglob('*')
                   if p.is_file() and not p.is_symlink() and not OMIT_DIRS.intersection(p.relative_to(theme_root).parts))
    files, edges, signals, parse_errors = [], [], [], []
    for full in paths:
        path = full.relative_to(theme_root)
        raw = full.read_bytes()
        row = {'path': path.as_posix(), 'bytes': len(raw), 'md5': hashlib.md5(raw).hexdigest(),
               'sha256': hashlib.sha256(raw).hexdigest(), 'kind': classify(path)}
        files.append(row)
        if path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            parse_errors.append({'path': row['path'], 'kind': 'not_utf8'})
            continue
        row['lines'] = len(text.splitlines())
        edges.extend({'source': row['path'], **ref} for ref in static_references(text, path))
        if path.suffix == '.json':
            try:
                parse_json(text)
            except ValueError:
                parse_errors.append({'path': row['path'], 'kind': 'invalid_json'})
        if path.suffix not in {'.liquid', '.css', '.js'}:
            continue
        clean = mask_comments(text)
        metrics = {
            'inline_style_blocks': len(re.findall(r'<style\b', clean, re.I)),
            'inline_script_blocks': len(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>', clean, re.I)),
            'important_declarations': len(re.findall(r'!important\b', clean)),
            'media_queries': len(re.findall(r'@media\b', clean)),
            'reduced_motion_mentions': len(re.findall(r'prefers-reduced-motion', clean)),
            'fetch_mentions': len(re.findall(r'\bfetch\s*\(', clean)),
            'event_listener_mentions': len(re.findall(r'\baddEventListener\s*\(', clean)),
            'observer_mentions': len(re.findall(r'\b(?:Mutation|Resize|Intersection)Observer\b', clean)),
            'storage_mentions': len(re.findall(r'\b(?:localStorage|sessionStorage)\b', clean)),
            'literal_hash_links': len(re.findall(r'''href\s*=\s*['"]#['"]''', clean)),
        }
        metrics = {key: value for key, value in metrics.items() if value}
        signals.append({'path': row['path'], 'metrics': metrics,
                        'css_custom_properties': sorted(set(re.findall(r'(--[a-zA-Z][\w-]*)\s*:', clean))),
                        'metafield_literal_keys': sorted(set('.'.join(pair) for pair in re.findall(r'\.metafields\.([\w]+)\.([\w]+)', clean))),
                        'data_attributes': sorted(set(re.findall(r'\b(data-[a-z][\w-]*)\s*=', clean)))})
    by_path = {row['path']: row for row in files}
    remote = {row['filename']: row for row in (manifest or {}).get('files', [])}
    for edge in edges:
        edge['resolution'] = ('in_scan' if edge['target'] in by_path else
                              'in_live_manifest_only' if edge['target'] in remote else 'not_resolved')
    duplicate_hashes = collections.defaultdict(list)
    for row in files:
        duplicate_hashes[row['sha256']].append(row['path'])
    parity = None
    if manifest:
        parity = {'equal': [], 'different': [], 'live_only': [], 'scan_only': sorted(set(by_path) - set(remote))}
        for path, record in sorted(remote.items()):
            key = 'live_only' if path not in by_path else 'equal' if by_path[path]['md5'] == record['checksumMd5'] else 'different'
            parity[key].append(path)
    return {
        'schema_version': 1, 'source_label': source_label, 'coverage': coverage,
        'git_commit': git_head(theme_root), 'manifest_theme_id': (manifest or {}).get('theme_id'),
        'counts': {'files': len(files), 'edges': len(edges), 'kinds': dict(collections.Counter(row['kind'] for row in files))},
        'limitations': [
            'Static candidates only: no runtime, visual, accessibility, security or commercial correctness certification.',
            'Liquid references and JSON section types only; dynamic Liquid, JS imports, CSS URLs, app blocks and implicit layout execution are not fully resolved.',
            'No-reference and identical-byte groups do not prove unused code or justify removal.',
            'Coverage and source label are declared by the operator; hashes establish only scanned-file equality.',
        ],
        'files': files, 'edges': sorted(edges, key=lambda edge: (edge['source'], edge['target'], edge['kind'])),
        'signals': signals, 'parse_errors': parse_errors, 'parity': parity,
        'identical_byte_groups': sorted([group for group in duplicate_hashes.values() if len(group) > 1]),
    }


def markdown_report(report):
    lines = ['# Statische code-inventarisatie', '', f"Bron: `{report['source_label']}`. Dekking: **{report['coverage']}**.",
             '', f"Bestanden: **{report['counts']['files']}**. Gevonden statische verwijzingen: **{report['counts']['edges']}**.",
             '', 'Dit is een gegenereerde zoekkaart, geen vrijgave of lijst met bewezen defects.', '', '## Grenzen', '']
    lines.extend('- ' + item for item in report['limitations'])
    if report['parity']:
        lines += ['', '## Vergelijking met live manifest', '', '| Categorie | Aantal |', '| --- | ---: |']
        lines.extend(f'| {key} | {len(paths)} |' for key, paths in report['parity'].items())
    lines += ['', '## Ingangen per bestand', '', '| Bestand | Type | Regels | Uitgaande verwijzingen |', '| --- | --- | ---: | ---: |']
    outgoing = collections.Counter(edge['source'] for edge in report['edges'])
    lines.extend(f"| `{row['path']}` | {row['kind']} | {row.get('lines', '—')} | {outgoing[row['path']]} |" for row in report['files'])
    lines += ['', 'Volledige paden, hashes, afhankelijkheden en signalen staan in `inventory.json`.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--theme-root', type=Path, required=True)
    parser.add_argument('--manifest', type=Path)
    parser.add_argument('--source-label', required=True)
    parser.add_argument('--coverage', choices=('full_snapshot', 'partial_sample', 'repository_root', 'unknown'), required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--require-parity', action='store_true')
    args = parser.parse_args()
    root, output = args.theme_root.resolve(), args.output_dir.resolve()
    if output == root:
        parser.error('Reports cannot overwrite the theme root README')
    for folder in THEME_DIRS:
        if output == root / folder or (root / folder) in output.parents:
            parser.error('Reports cannot be written inside a theme directory')
    manifest = json.loads(args.manifest.read_text(encoding='utf-8')) if args.manifest else None
    report = scan(root, manifest, args.coverage, args.source_label)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'inventory.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (output / 'README.md').write_text(markdown_report(report), encoding='utf-8')
    print(json.dumps({'files': report['counts']['files'], 'edges': report['counts']['edges'],
                      'parse_errors': len(report['parse_errors']),
                      'parity': {key: len(value) for key, value in (report['parity'] or {}).items()}}, sort_keys=True))
    parity_failed = args.require_parity and (not report['parity'] or any(report['parity'][key] for key in ('different', 'live_only', 'scan_only')))
    return 2 if report['parse_errors'] or parity_failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
