#!/usr/bin/env python3
"""Build the standalone reviewed installer without embedding private runtime files."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def build(worker_path, api_path, output):
    folder = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('bc_repair_builder_base', folder / 'apply_variant_repair.py')
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    sources = {'worker': (folder / 'variant_worker_patch.py').read_text(),
               'api': (folder / 'variant_api_patch.py').read_text()}
    original_worker = worker_path.read_bytes()
    original_api = api_path.read_bytes()
    if base.sha256(original_api) != base.BASE_API_SHA256:
        raise RuntimeError('API source does not match the reviewed uploaded version')
    patched_worker = base.compose_worker(original_worker, sources)
    worker = base.load_worker(patched_worker)
    patched_api = worker.patch_api(original_api.decode('utf-8')).encode('utf-8')
    if patched_api == original_api:
        raise RuntimeError('API alias patch was not applied')
    text = (folder / 'apply_variant_repair.py').read_text()
    replacements = {'PATCH_SOURCES = None': 'PATCH_SOURCES = ' + repr(sources),
                    'TARGET_WORKER_SHA256 = None': 'TARGET_WORKER_SHA256 = ' + repr(base.sha256(patched_worker)),
                    'TARGET_API_SHA256 = None': 'TARGET_API_SHA256 = ' + repr(base.sha256(patched_api)),
                    'TARGET_API_AST_SHA256 = None': 'TARGET_API_AST_SHA256 = ' + repr(base.ast_digest(patched_api))}
    for old, new in replacements.items():
        if text.count(old) != 1:
            raise RuntimeError('Installer template changed unexpectedly')
        text = text.replace(old, new, 1)
    # Windows PowerShell 5 may pipe text through an ASCII encoder. Escaping
    # Unicode in Python literals keeps the reviewed strings byte-exact after
    # Python parses them, without requiring global PowerShell encoding changes.
    text = text.encode('ascii', 'backslashreplace').decode('ascii')
    compile(text, '<standalone-variant-index-repair>', 'exec')
    output.write_text(text, encoding='utf-8')
    return {'installer': output.name, 'installer_sha256': base.sha256(output.read_bytes()),
            'base_worker_sha256': base.BASE_WORKER_SHA256, 'base_api_sha256': base.BASE_API_SHA256,
            'target_worker_sha256': base.sha256(patched_worker),
            'target_api_sha256': base.sha256(patched_api), 'deadline_seconds': base.DEADLINE_SECONDS,
            'target_api_ast_sha256': base.ast_digest(patched_api),
            'private_runtime_sources_embedded': False, 'transport_ascii': text.isascii()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--worker-source', required=True, type=Path)
    parser.add_argument('--api-source', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--manifest', type=Path)
    args = parser.parse_args()
    result = build(args.worker_source, args.api_source, args.output)
    if args.manifest:
        args.manifest.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
