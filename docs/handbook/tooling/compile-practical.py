#!/usr/bin/env python3
"""Compile only practical chapters 48–79; retain all other master content."""
import json
from pathlib import Path
import re
import sys

repo = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
source = repo / 'docs/handbook/2026-10-31'
master = repo / 'docs/MASTER_SITE_REFERENCE.md'


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
master.write_text(content)
print(json.dumps({'chapters': len(numbers), 'tasks': len(tasks),
                  'diagnoses': len(diagnoses), 'cases': len(cases)}))
