"""Freeze only reviewed public Cotto color rules into a guarded pure patch."""
import argparse
import importlib.util
import json
from pathlib import Path


def build(worker_source, rules_path, output):
    template = Path(__file__).with_name('cotto_worker_patch_template.py').read_text()
    value = json.loads(rules_path.read_text())
    rules = value.get('rules') if isinstance(value, dict) else value
    if not isinstance(rules, list):
        raise RuntimeError('Rules must be a list or an object containing rules')
    # Evidence and private analysis paths stay outside the runtime patch.
    core = [{key: rule[key] for key in ('series', 'exact_color', 'colors', 'confidence')}
            for rule in rules]
    core.sort(key=lambda rule: (rule['series'].casefold(), rule['exact_color'].casefold()))
    text = template.replace('SCOPED_RULES = None', 'SCOPED_RULES = ' + repr(core), 1)
    namespace = {'__name__': 'bc_build_cotto_worker_patch'}
    exec(compile(text, '<cotto-worker-patch-build>', 'exec'), namespace)
    source = worker_source.read_text()
    target = namespace['patch_cotto_worker'](source)
    target_hash = namespace['_sha'](target)
    text = text.replace('PATCHED_WORKER_SHA256 = None',
                        'PATCHED_WORKER_SHA256 = ' + repr(target_hash), 1)
    compile(text, '<frozen-cotto-worker-patch>', 'exec')
    output.write_text(text)
    return {'worker_patch': output.name, 'rule_rows': len(core),
            'target_worker_sha256': target_hash,
            'worker_patch_sha256': namespace['_sha'](text)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--worker-source', required=True, type=Path)
    parser.add_argument('--rules', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.worker_source, args.rules, args.output)))
