"""Candidate patch: existing tiles.look -> a closed, generic tile-look facet.

This module contains no catalog, credentials, API source, or private worker.
It accepts only the reviewed ecfc worker. It does not execute or install it.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import unicodedata


BASE_WORKER_SHA256 = 'ecfc142a4fb15e66df297ec20884826be1bd4e8c491fb20bdb3e17cc281ba69a'
API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'
MARKER = '# BC_TILE_LOOKS_V1'
FIELD = 'f_tegel_uitstraling'
DEFAULT_TAXONOMY = ('Steenlook', 'Marmerlook', 'Houtlook', 'Betonlook',
                    'Metaallook', 'Terrazzo', 'Effen', 'Decoratief',
                    'Handvormlook', 'Terracottalook')
DEFAULT_ALIASES = {
    'stone': 'Steenlook', 'stone look': 'Steenlook', 'stonelook': 'Steenlook',
    'steen': 'Steenlook', 'steenlook': 'Steenlook', 'natuursteenlook': 'Steenlook',
    'marble': 'Marmerlook', 'marble look': 'Marmerlook', 'marmer': 'Marmerlook',
    'marmerlook': 'Marmerlook', 'wood': 'Houtlook', 'wood look': 'Houtlook',
    'hout': 'Houtlook', 'houtlook': 'Houtlook', 'keramisch parket': 'Houtlook',
    'concrete': 'Betonlook', 'concrete look': 'Betonlook', 'beton': 'Betonlook',
    'betonlook': 'Betonlook', 'cementlook': 'Betonlook',
    'metal': 'Metaallook', 'metal look': 'Metaallook', 'metaal': 'Metaallook',
    'metaallook': 'Metaallook', 'terrazzo': 'Terrazzo', 'terrazzolook': 'Terrazzo',
    'uni': 'Effen', 'effen': 'Effen', 'plain': 'Effen',
    'decor': 'Decoratief', 'decoratief': 'Decoratief', 'decoratie': 'Decoratief',
    'patroon': 'Decoratief', 'patroontegels': 'Decoratief', 'design': 'Decoratief',
    'zellige': 'Handvormlook', 'zelliges': 'Handvormlook',
    'zelligelook': 'Handvormlook', 'handvorm': 'Handvormlook',
    'handvormlook': 'Handvormlook', 'terracotta': 'Terracottalook',
    'terracottalook': 'Terracottalook',
}


def _key(value):
    if not isinstance(value, str):
        return None
    value = unicodedata.normalize('NFKC', value).casefold()
    return ' '.join(re.sub(r'[-_]+', ' ', value).split())


def reviewed_configuration(taxonomy=None, aliases=None):
    """Exact aliases only. No substring, title, image, or series classifier."""
    taxonomy = DEFAULT_TAXONOMY if taxonomy is None else taxonomy
    if not isinstance(taxonomy, (list, tuple)) or not 2 <= len(taxonomy) <= 20:
        raise RuntimeError('Uitstraling vereist een beperkte vaste woordenlijst')
    if any(not isinstance(v, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9-]{1,39}', v)
           for v in taxonomy) or len({_key(v) for v in taxonomy}) != len(taxonomy):
        raise RuntimeError('Ongeldige of dubbele canonieke uitstraling')
    taxonomy = tuple(taxonomy)
    selected = {k: v for k, v in DEFAULT_ALIASES.items() if v in taxonomy}
    if aliases is not None:
        if not isinstance(aliases, dict) or len(aliases) > 200:
            raise RuntimeError('Ongeldig exact uitstraling-aliasregister')
        selected.update(aliases)
    output = {}
    for raw, canonical in list(selected.items()) + [(v, v) for v in taxonomy]:
        normalized = _key(raw)
        if not normalized or len(normalized) > 300 or canonical not in taxonomy:
            raise RuntimeError('Uitstraling-alias wijst niet naar de vaste woordenlijst')
        if normalized in output and output[normalized] != canonical:
            raise RuntimeError('Tegenstrijdige exacte uitstraling-alias')
        output[normalized] = canonical
    return taxonomy, dict(sorted(output.items()))


HELPERS = r'''
# BC_TILE_LOOKS_V1
import unicodedata as _bc_look_unicode
_BC_TILE_LOOK_FIELD = 'f_tegel_uitstraling'
_BC_TILE_LOOK_TAXONOMY = __BC_LOOK_TAXONOMY__
_BC_TILE_LOOK_ALIASES = __BC_LOOK_ALIASES__
_BC_TILE_LOOK_SOURCE_BY_ID = {}

def _bc_tile_look_normalize(raw):
    if not isinstance(raw, str):
        return None
    value = _bc_look_unicode.normalize('NFKC', raw).casefold()
    value = ' '.join(re.sub(r'[-_]+', ' ', value).split())
    return _BC_TILE_LOOK_ALIASES.get(value)

# Preserve the original export escaping and add exactly one product-level field.
_bc_look_export_anchor = 'series: metafield(namespace: "custom", key: "serie") { value updatedAt }'
if QUERIES['bulkProducts'].count(_bc_look_export_anchor) != 1 or 'tile_look:' in QUERIES['bulkProducts']:
    raise RuntimeError('Bestaande export mist unieke gecontroleerde uitstralinghook')
_bc_look_separator = '\\n ' if '\\n ' in QUERIES['bulkProducts'] else '\n '
QUERIES['bulkProducts'] = QUERIES['bulkProducts'].replace(
    _bc_look_export_anchor, _bc_look_export_anchor + _bc_look_separator +
    'tile_look: metafield(namespace: "tiles", key: "look") { value updatedAt }', 1)

_bc_look_original_schema = _bc_simple_schema
def _bc_simple_schema(schema):
    result = _bc_look_original_schema(schema)
    fields = [field for field in result['fields'] if field.get('name') == _BC_TILE_LOOK_FIELD]
    if fields and (len(fields) != 1 or fields[0].get('type') != 'string' or
                   fields[0].get('facet') is not True or fields[0].get('optional') is not True):
        raise RuntimeError('Bestaand uitstraling-indexveld heeft een afwijkend contract')
    if not fields:
        result['fields'].append({'name': _BC_TILE_LOOK_FIELD, 'type': 'string',
                                 'facet': True, 'optional': True})
    return result

_bc_look_original_definitions = _bc_simple_definitions
def _bc_simple_definitions(definitions):
    result = _bc_look_original_definitions(definitions)
    current = [definition for definition in result if definition.get('field') == _BC_TILE_LOOK_FIELD]
    if current and (len(current) != 1 or current[0].get('type') != 'choice' or
                    current[0].get('data_type') != 'string'):
        raise RuntimeError('Bestaande uitstraling-filterdefinitie heeft een afwijkend contract')
    if not current:
        result.append({'key': 'tegel_uitstraling', 'field': _BC_TILE_LOOK_FIELD,
                       'label': 'Uitstraling', 'type': 'choice', 'data_type': 'string'})
    return result

_bc_look_original_normalize = normalize_products
def normalize_products(products, category_map, definitions, schema):
    docs, stats, issues = _bc_look_original_normalize(products, category_map, definitions, schema)
    source = {product['id'].rsplit('/', 1)[-1]: product for product in products}
    _BC_TILE_LOOK_SOURCE_BY_ID.clear()
    counts = collections.Counter()
    for doc in docs:
        # Only the existing product-level tiles.look is authoritative for this layer.
        doc.pop(_BC_TILE_LOOK_FIELD, None)
        if not _bc_acero_is_tile(doc):
            continue
        record = source[doc['id']].get('tile_look')
        raw = record.get('value') if isinstance(record, dict) else None
        value = _bc_tile_look_normalize(raw)
        _BC_TILE_LOOK_SOURCE_BY_ID[doc['id']] = {'source': 'tiles.look', 'raw': raw, 'canonical': value}
        if value is not None:
            doc[_BC_TILE_LOOK_FIELD] = value
            counts['tile_look_products'] += 1
        else:
            counts['tile_look_missing_products'] += 1
            if isinstance(raw, str) and raw.strip():
                counts['tile_look_unrecognized_source_products'] += 1
                issues.append({'id': doc['id'], 'field': _BC_TILE_LOOK_FIELD,
                               'issue': 'unrecognized_tiles_look_value'})
    stats.update(dict(counts))
    return docs, stats, issues

_bc_look_original_filter_ui = filter_ui
def filter_ui(field, definition, group, values, section, opened):
    result = _bc_look_original_filter_ui(field, definition, group, values, section, opened)
    if field == _BC_TILE_LOOK_FIELD:
        result.update(control='checkbox', section='primary', default_open=False,
                      visible_values=6, searchable=len(values) > 12,
                      value_sort='alphabetical', display_unit=None, display_divisor=1)
    return result

# Retain the original format/color ordering and at most two open groups.
PLANS['tile'] = (list(PLANS['tile'][0]) + [_BC_TILE_LOOK_FIELD], list(PLANS['tile'][1]))
LABELS[_BC_TILE_LOOK_FIELD] = 'Uitstraling'

_bc_look_original_profiles = make_profiles
def make_profiles(docs, categories, old_profiles, definitions):
    profiles = _bc_look_original_profiles(docs, categories, old_profiles, definitions)
    definition = next(item for item in definitions if item['field'] == _BC_TILE_LOOK_FIELD)
    for handle, profile in profiles.items():
        relevant = profile.get('b2c_policy', {}).get('group') == 'tile' or handle == 'cottoceramix'
        if not relevant:
            continue
        if not any(item['field'] == _BC_TILE_LOOK_FIELD for item in profile['allowed_filters']):
            profile['allowed_filters'].append(copy.deepcopy(definition))
        shopping = [doc for doc in docs if handle in doc['collection_handles'] and
                    (profile['service_category'] or doc['general_shopping'])]
        values = [doc[_BC_TILE_LOOK_FIELD] for doc in shopping if _BC_TILE_LOOK_FIELD in doc]
        unique = distinct_values(values)
        coverage = round(100 * len(values) / len(shopping), 2) if shopping else 0
        profile['filters'] = [item for item in profile['filters'] if item['field'] != _BC_TILE_LOOK_FIELD]
        suppressed = profile['b2c_policy'].setdefault('suppressed', [])
        suppressed[:] = [item for item in suppressed if item.get('field') != _BC_TILE_LOOK_FIELD]
        if len(unique) >= 2:
            facet = {**copy.deepcopy(definition), 'label': 'Uitstraling',
                     'coverage_pct': coverage, 'distinct_values': len(unique)}
            facet['ui'] = filter_ui(_BC_TILE_LOOK_FIELD, definition,
                                    profile['b2c_policy']['group'], unique, 'primary', False)
            profile['filters'].append(facet)
        else:
            suppressed.append({'field': _BC_TILE_LOOK_FIELD,
                               'reason': 'no_distinction' if values else 'missing_data',
                               'coverage_pct': coverage})
        policy = profile['b2c_policy']
        policy['tile_looks_v1'] = True
        policy['default_open_fields'] = [item['field'] for item in profile['filters'] if item['ui']['default_open']]
        policy['primary_fields'] = [item['field'] for item in profile['filters'] if item['ui']['section'] == 'primary']
        policy['more_fields'] = [item['field'] for item in profile['filters'] if item['ui']['section'] == 'more']
    return profiles

def _bc_tile_look_documents_ok(docs):
    for doc in docs:
        value = doc.get(_BC_TILE_LOOK_FIELD)
        source = _BC_TILE_LOOK_SOURCE_BY_ID.get(doc['id'])
        if not _bc_acero_is_tile(doc):
            if _BC_TILE_LOOK_FIELD in doc:
                return False
            continue
        if source is None or source.get('source') != 'tiles.look':
            return False
        expected = _bc_tile_look_normalize(source.get('raw'))
        if expected != source.get('canonical') or value != expected:
            return False
        if expected is None and _BC_TILE_LOOK_FIELD in doc:
            return False
        if value is not None and value not in _BC_TILE_LOOK_TAXONOMY:
            return False
    return True

_bc_look_original_snapshot = _bc_simple_snapshot
def _bc_simple_snapshot(snapshot, docs):
    _bc_look_original_snapshot(snapshot, docs)
    required = ('variant_aliases_v1', 'filter_simplification_v1', 'tile_format_codes_v1',
                'acero_gray_v1', 'cotto_visual_colors_v1', 'tile_bone_beige_v1', 'more_tile_colors_v1')
    if any(snapshot.get(key) is not True for key in required):
        raise RuntimeError('Een bestaande filtergeneratievlag ontbreekt bij uitstraling')
    if not _bc_tile_look_documents_ok(docs):
        raise RuntimeError('Tegeluitstraling wijkt af van het bestaande tiles.look-bronveld')
    snapshot['tile_looks_v1'] = True
    snapshot['tile_look_source'] = 'tiles.look'
    snapshot['tile_look_taxonomy'] = list(_BC_TILE_LOOK_TAXONOMY)
    eligible = [doc for doc in docs if doc['general_shopping'] and _bc_acero_is_tile(doc)]
    snapshot['tile_look_products'] = sum(_BC_TILE_LOOK_FIELD in doc for doc in eligible)
    snapshot['tile_look_missing_products'] = sum(_BC_TILE_LOOK_FIELD not in doc for doc in eligible)
    snapshot['tile_look_counts'] = dict(collections.Counter(doc[_BC_TILE_LOOK_FIELD]
                                  for doc in eligible if _BC_TILE_LOOK_FIELD in doc))

_bc_look_original_checks = check_b2c_profiles
def check_b2c_profiles(docs, snapshot):
    checks = _bc_look_original_checks(docs, snapshot)
    relevant = [profile for handle, profile in snapshot['profiles'].items()
                if profile.get('b2c_policy', {}).get('group') == 'tile' or handle == 'cottoceramix']
    correct = _bc_tile_look_documents_ok(docs) and snapshot.get('tile_looks_v1') is True
    correct = correct and all(profile['b2c_policy'].get('tile_looks_v1') is True and
        sum(item['field'] == _BC_TILE_LOOK_FIELD for item in profile['allowed_filters']) == 1 and
        all(item['ui']['default_open'] is False and item['ui']['control'] == 'checkbox'
            for item in profile['filters'] if item['field'] == _BC_TILE_LOOK_FIELD)
        for profile in relevant)
    checks.append({'name': 'Uitstraling volgt uitsluitend tiles.look en blijft een gesloten tegelkeuze',
                   'passed': bool(correct)})
    return checks

_bc_look_original_cases = make_cases
def make_cases(docs, snapshot):
    cases, facets = _bc_look_original_cases(docs, snapshot)
    for handle in ('tegels', 'cottoceramix'):
        profile = snapshot['profiles'].get(handle)
        if profile is None or not any(item['field'] == _BC_TILE_LOOK_FIELD for item in profile['allowed_filters']):
            continue
        shopping = selected(docs, snapshot, {'collection': handle})
        values = sorted({doc[_BC_TILE_LOOK_FIELD] for doc in shopping if _BC_TILE_LOOK_FIELD in doc})
        for value in values:
            body = {'collection': handle, 'include_facets': False,
                    'filters': {_BC_TILE_LOOK_FIELD: [value]}}
            cases.append({'name': 'Exacte uitstraling: ' + handle + '/' + value,
                          'body': body, 'status': 200,
                          'expected_ids': [doc['id'] for doc in selected(docs, snapshot, body)]})
        body = {'collection': handle, 'include_facets': False,
                'filters': {_BC_TILE_LOOK_FIELD: ['__bc_unknown_look__']}}
        cases.append({'name': 'Onbekende uitstraling geeft nul producten: ' + handle,
                      'body': body, 'status': 200, 'expected_ids': []})
        if len(values) >= 2:
            body = {'collection': handle, 'include_facets': False,
                    'filters': {_BC_TILE_LOOK_FIELD: values[:2]}}
            cases.append({'name': 'Uitstralingen met OF-selectie: ' + handle,
                          'body': body, 'status': 200,
                          'expected_ids': [doc['id'] for doc in selected(docs, snapshot, body)]})
        if any(item['field'] == _BC_TILE_LOOK_FIELD for item in profile['filters']):
            body = {'collection': handle, 'per_page': 1}
            facets.append({'name': 'Unieke uitstraling-facetaantallen: ' + handle,
                           'body': body, 'field': _BC_TILE_LOOK_FIELD,
                           'expected_counts': dict(collections.Counter(doc[_BC_TILE_LOOK_FIELD]
                               for doc in shopping if _BC_TILE_LOOK_FIELD in doc))})
        sample = next((doc for doc in shopping if _BC_TILE_LOOK_FIELD in doc and doc.get('f_kleur')), None)
        if sample:
            body = {'collection': handle, 'include_facets': False,
                    'filters': {_BC_TILE_LOOK_FIELD: [sample[_BC_TILE_LOOK_FIELD]],
                                'f_kleur': _bc_simple_strings(sample['f_kleur'])[:1]}}
            if sample.get('f_tegel_formaat') and any(item['field'] == 'f_tegel_formaat' for item in profile['allowed_filters']):
                body['filters']['f_tegel_formaat'] = [sample['f_tegel_formaat']]
            cases.append({'name': 'Uitstraling gecombineerd met kleur en beschikbaar formaat: ' + handle,
                          'body': body, 'status': 200,
                          'expected_ids': [doc['id'] for doc in selected(docs, snapshot, body)]})
    return cases, facets
'''


def patch_tile_look_worker(source, taxonomy=None, aliases=None):
    if not isinstance(source, str) or hashlib.sha256(source.encode('utf-8')).hexdigest() != BASE_WORKER_SHA256:
        raise RuntimeError('Worker wijkt af van de gecontroleerde basis; niets gewijzigd')
    if MARKER in source:
        raise RuntimeError('Uitstralinghook staat onverwacht al in de basis')
    taxonomy, aliases = reviewed_configuration(taxonomy, aliases)
    anchor = "if __name__ == '__main__':\n"
    if source.count(anchor) != 1:
        raise RuntimeError('Unieke worker-startgrens ontbreekt')
    helpers = HELPERS.replace('__BC_LOOK_TAXONOMY__', repr(taxonomy)).replace('__BC_LOOK_ALIASES__', repr(aliases))
    result = source.replace(anchor, helpers + '\n' + anchor, 1)
    ast.parse(result)
    return result


def describe_patch(source, taxonomy=None, aliases=None):
    """Return only aggregate hashes/configuration, never the private source."""
    patched = patch_tile_look_worker(source, taxonomy, aliases)
    vocabulary, normalized = reviewed_configuration(taxonomy, aliases)
    return {'base_worker_sha256': BASE_WORKER_SHA256,
            'candidate_worker_sha256': hashlib.sha256(patched.encode()).hexdigest(),
            'api_sha256': API_SHA256, 'api_write': False, 'theme_write': False,
            'taxonomy': list(vocabulary), 'exact_aliases': len(normalized),
            'source': 'tiles.look', 'field': FIELD, 'flag': 'tile_looks_v1'}
