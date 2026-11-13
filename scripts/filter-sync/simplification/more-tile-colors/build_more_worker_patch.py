"""Freeze only reviewed public tile-color and finite identity-guarded rules."""
import argparse
import json
from pathlib import Path


def _rules(path):
    value = json.loads(path.read_text())
    result = value.get('rules') if isinstance(value, dict) else value
    if not isinstance(result, list):
        raise RuntimeError('Expected a list or an object containing rules')
    return result


def build(worker_source, scoped_rules, fallback_rules, output):
    text = Path(__file__).with_name('more_worker_patch_template.py').read_text()
    scoped = [{key: rule[key] for key in ('vendor', 'series', 'exact_color', 'colors', 'confidence')}
              for rule in _rules(scoped_rules)]
    fallback = [{key: rule[key] for key in ('vendor', 'sku', 'handle', 'title_sha256', 'colors', 'provenance')}
                for rule in _rules(fallback_rules)]
    scoped.sort(key=lambda rule: (rule['vendor'].casefold(), rule['series'].casefold(), rule['exact_color'].casefold()))
    fallback.sort(key=lambda rule: rule['handle'])
    text = text.replace('SCOPED_RULES = None', 'SCOPED_RULES = ' + repr(scoped), 1)
    text = text.replace('FALLBACK_RULES = None', 'FALLBACK_RULES = ' + repr(fallback), 1)
    namespace = {'__name__': 'bc_build_more_worker_patch'}
    exec(compile(text, '<more-worker-patch-build>', 'exec'), namespace)
    target = namespace['patch_more_worker'](worker_source.read_text())
    digest = namespace['_sha'](target)
    text = text.replace('PATCHED_WORKER_SHA256 = None', 'PATCHED_WORKER_SHA256 = ' + repr(digest), 1)
    compile(text, '<frozen-more-worker-patch>', 'exec')
    output.write_text(text)
    return {'worker_patch': output.name, 'scoped_rule_rows': len(scoped), 'fallback_rule_rows': len(fallback),
            'target_worker_sha256': digest, 'worker_patch_sha256': namespace['_sha'](text)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--worker-source', required=True, type=Path)
    parser.add_argument('--scoped-rules', required=True, type=Path)
    parser.add_argument('--fallback-rules', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.worker_source, args.scoped_rules, args.fallback_rules, args.output)))
