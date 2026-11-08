#!/usr/bin/env python3
"""Rebuild historical chapters 48–79 to an explicit, separate output file."""
import argparse
import json
from pathlib import Path
import re
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('repo', nargs='?', default='.')
parser.add_argument('--output', required=True, help='Separate rebuilt Markdown file; never the current index or immutable archive')
args = parser.parse_args()
repo = Path(args.repo).resolve()
source = repo / 'docs/handbook/2026-10-31'
master = repo / 'docs/MASTER_SITE_REFERENCE_2026-10-31.md'
target = Path(args.output).resolve()
protected = {master.resolve(), (repo / 'docs/MASTER_SITE_REFERENCE.md').resolve()}
if target in protected:
    parser.error('The current index and historical source archive are protected; choose a separate --output')


def table(headers, rows):
    def cell(value):
        return str(value).replace('|', '/').replace('\n', ' ')
    return '\n'.join([
        '| ' + ' | '.join(headers) + ' |',
        '| ' + ' | '.join(['---'] * len(headers)) + ' |',
        *['| ' + ' | '.join(map(cell, row)) + ' |' for row in rows],
    ])


tasks = json.loads((source / 'practical-tasks.json').read_text())
diagnoses = json.loads((source / 'diagnosis.json').read_text())
cases = json.loads((source / 'acceptance.json').read_text())
text = (source / 'PRACTICAL_REFERENCE.md').read_text()
replacements = {
    '<!-- TASK_TABLE -->': table(
        ['ID / taak', 'Eigenaar', 'Waar', 'Controle / hoofdstuk', 'Stand'],
        [[t['id']+' '+t['question'], t['owner'], t['where'],
          t['check']+'; '+str(t['chapter']), t['status']] for t in tasks]),
    '<!-- DIAGNOSIS_TABLE -->': table(
        ['ID / symptoom', 'Eerste broncontrole', 'Eigenaar', 'Regressie'],
        [[t['id']+' '+t['symptom'], t['source'], t['owner'], t['regression']]
         for t in diagnoses]),
    '<!-- ACCEPTANCE_TABLE -->': table(
        ['ID / familie', 'Uitvoeren', 'Verwacht', 'Bewijsstatus / bron'],
        [[t['id']+' '+t['group'], t['action'], t['expected'],
          t['status']+' — '+t['evidence']] for t in cases]),
}
for marker, content in replacements.items():
    if text.count(marker) != 1:
        raise ValueError('Expected exactly one marker: '+marker)
    text = text.replace(marker, content)
content = master.read_text()
content, count = re.subn(
    r'^## 48 Leesroutes[\s\S]*?(?=^## 80 )', text.rstrip()+'\n\n\n',
    content, count=1, flags=re.M)
if count != 1:
    raise ValueError('Expected practical range 48–79 in existing master')
numbers = [int(x) for x in re.findall(r'^## (\d+) ', content, re.M)]
if numbers != list(range(1, 81)):
    raise ValueError('Master chapter sequence must be exactly 1–80')
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(content)
print(json.dumps({'chapters': len(numbers), 'tasks': len(tasks),
                  'diagnoses': len(diagnoses), 'cases': len(cases)}))
