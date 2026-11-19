#!/usr/bin/env python3
"""Build a catalog-free installer from the frozen reviewed Cotto worker patch."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def build(worker_path, api_path, worker_patch_path, output):
    folder = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location('bc_cotto_release_builder', folder / 'apply_cotto_color_correction.py')
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    sources = {'worker': worker_patch_path.read_text()}
    original_worker = worker_path.read_bytes()
    original_api = api_path.read_bytes()
    if not base.base_api_matches(original_api):
        raise RuntimeError('API source is not the exact reviewed deployed version')
    patched_worker = base.compose_worker(original_worker, sources)
    worker = base.load_worker(patched_worker)
    patched_api = worker.patch_api(original_api.decode()).encode()
    if patched_worker == original_worker:
        raise RuntimeError('The Cotto worker patch was not applied')
    if patched_api != original_api:
        raise RuntimeError('The Cotto color correction must preserve the complete API source')
    text = (folder / 'apply_cotto_color_correction.py').read_text()
    replacements = {
        'PATCH_SOURCES = None': 'PATCH_SOURCES = ' + repr(sources),
        'TARGET_WORKER_SHA256 = None': 'TARGET_WORKER_SHA256 = ' + repr(base.sha256(patched_worker)),
        'TARGET_API_SHA256 = None': 'TARGET_API_SHA256 = ' + repr(base.sha256(patched_api)),
        'TARGET_API_AST_SHA256 = None': 'TARGET_API_AST_SHA256 = ' + repr(base.ast_digest(patched_api)),
    }
    for old, new in replacements.items():
        if text.count(old) != 1:
            raise RuntimeError('Installer template changed unexpectedly')
        text = text.replace(old, new, 1)
    text = text.encode('ascii', 'backslashreplace').decode('ascii')
    compile(text, '<standalone-cotto-color-correction>', 'exec')
    output.write_text(text)
    return {
        'installer': output.name, 'installer_bytes': len(text.encode()),
        'installer_sha256': base.sha256(output.read_bytes()),
        'base_worker_sha256': base.BASE_WORKER_SHA256,
        'base_api_sha256': base.BASE_API_SHA256,
        'base_api_ast_sha256': base.BASE_API_AST_SHA256,
        'target_worker_sha256': base.sha256(patched_worker),
        'target_api_sha256': base.sha256(patched_api),
        'target_api_ast_sha256': base.ast_digest(patched_api),
        'api_source_unchanged': patched_api == original_api,
        'reviewed_rule_keys': len(worker._BC_SIMPLE_COLORS['COTTO_VISUAL_SCOPED_RULES']),
        'deadline_seconds': base.DEADLINE_SECONDS,
        'recovery_seconds': base.RECOVERY_SECONDS,
        'required_snapshot_flags': ['variant_aliases_v1', 'filter_simplification_v1',
                                    'tile_format_codes_v1', 'acero_gray_v1', 'cotto_visual_colors_v1'],
        'private_runtime_sources_embedded': False,
        'transport_ascii': text.isascii(),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--worker-source', required=True, type=Path)
    parser.add_argument('--api-source', required=True, type=Path)
    parser.add_argument('--worker-patch', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--manifest', type=Path)
    args = parser.parse_args()
    result = build(args.worker_source, args.api_source, args.worker_patch, args.output)
    if args.manifest:
        args.manifest.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
