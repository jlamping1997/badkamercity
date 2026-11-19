#!/usr/bin/env python3
"""Read-only diagnosis of one failed staged tile-format selection."""
import collections
import json
from pathlib import Path
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request

RUN = Path('/opt/badkamercity/filter-sync/runs/20261108T142600_81ee36')
CONTAINER = 'badkamercity-filter-api-verified-candidate'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise urllib.error.URLError('Redirect refused')


def diagnose():
    report = json.loads((RUN / 'RESULTAAT.json').read_text())
    snapshot = json.loads((RUN / 'snapshot.json').read_text())
    docs = json.loads((RUN / 'documents.json').read_text())
    failures = [c for c in report.get('checks', []) if c.get('passed') is not True]
    output = {'read_only': True, 'production_changes': False,
              'failed_checks': failures, 'stage_generation': snapshot.get('generation')}
    collection = snapshot['collection']
    if not re.fullmatch(r'bc_sync_[a-z0-9_]+', collection):
        raise RuntimeError('Unexpected staged collection')
    inspected = subprocess.run(['docker', 'inspect', CONTAINER], capture_output=True,
                               text=True, check=True, timeout=10)
    item = json.loads(inspected.stdout)[0]
    env = dict(v.split('=', 1) for v in item['Config']['Env'] if '=' in v)
    keys = [k for k in env if 'TYPESENSE' in k.upper() and 'KEY' in k.upper()]
    if len(keys) != 1:
        raise RuntimeError('No unambiguous existing index credential')
    key = env[keys[0]]
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    label = '60 \u00d7 60 cm'
    profile = snapshot['profiles']['tegels']
    expected = {d['id'] for d in docs if 'tegels' in d['collection_handles']
                and (profile['service_category'] or d['general_shopping'])
                and d.get('f_tegel_formaat') == label}
    clauses = ['published:=true', 'collection_handles:=`tegels`']
    if not profile['service_category']:
        clauses.append('general_shopping:=true')
    clauses.append('f_tegel_formaat:=`' + label + '`')
    ids = []
    formats = collections.Counter()
    pages = []
    for page in range(1, 51):
        params = {'q': '*', 'query_by': 'title', 'filter_by': ' && '.join(clauses),
                  'page': page, 'per_page': 100, 'enable_overrides': 'false',
                  'include_fields': 'id,f_tegel_formaat'}
        url = 'http://127.0.0.1:8108/collections/' + urllib.parse.quote(collection, safe='')
        url += '/documents/search?' + urllib.parse.urlencode(params)
        request = urllib.request.Request(url, headers={'X-TYPESENSE-API-KEY': key})
        with opener.open(request, timeout=15) as response:
            data = json.loads(response.read(2_000_000))
        hits = data.get('hits', [])
        for hit in hits:
            doc = hit['document']
            ids.append(doc['id'])
            formats[doc.get('f_tegel_formaat', '[missing]')] += 1
        pages.append({'page': page, 'found': data.get('found'), 'hits': len(hits),
                      'search_cutoff': data.get('search_cutoff')})
        if not hits or len(ids) >= data.get('found', 0):
            break
    actual = set(ids)
    by_id = {d['id']: d for d in docs}
    output.update({'format': label, 'expected_count': len(expected),
                   'returned_rows': len(ids), 'unique_returned_ids': len(actual),
                   'duplicate_rows': len(ids) - len(actual),
                   'missing_id_count': len(expected - actual),
                   'extra_id_count': len(actual - expected),
                   'returned_format_counts': dict(formats), 'pages': pages,
                   'missing_format_counts': dict(collections.Counter(
                       by_id[v].get('f_tegel_formaat', '[missing]') for v in expected - actual)),
                   'wildcard_in_exact_skus': '*' in snapshot.get('exact', [])})
    return output


if __name__ == '__main__':
    try:
        print(json.dumps(diagnose(), ensure_ascii=True, indent=2))
    except Exception as error:
        # Do not print exceptions containing request/configuration data.
        print(json.dumps({'read_only': True, 'production_changes': False,
                          'diagnostic_error': type(error).__name__}))
        raise SystemExit(2)
