"""Guarded finite tile-color corrections and source-empty recoveries.

Frozen public rules contain no catalog IDs or private runtime sources. Exact
manufacturer colors remain intact; source-empty recoveries retain a blank raw
color and record their provenance only in the private generation snapshot.
"""
import ast
import hashlib

BASE_WORKER_SHA256 = 'a8dd54597a2a372a7b0fcce9357a6bcc31a406fca2631cb9b24918f5fea0ff17'
PATCHED_WORKER_SHA256 = None
SCOPED_RULES = None
FALLBACK_RULES = None
MARKER = '# BC_MORE_TILE_COLORS_V1'

HELPERS = '''
# BC_MORE_TILE_COLORS_V1
_BC_MORE_COLOR_RECOVERED = {}

def _bc_more_empty_color(value):
    return value is None or (isinstance(value, str) and not value.strip()) or (isinstance(value, (list, tuple)) and not value)

def _bc_more_expected_color(doc):
    if not _bc_acero_is_tile(doc):
        return None
    colors = _BC_SIMPLE_COLORS
    raw = doc.get('f_kleur_exact')
    series = _bc_simple_strings(doc.get('f_serie')) or _bc_simple_strings(doc.get('series'))
    if not isinstance(raw, str) or not raw.strip() or len(series) != 1:
        return None
    key = (colors['normalize'](doc.get('vendor')), colors['normalize_series'](series[0]), colors['normalize'](raw))
    return colors['MORE_TILE_SCOPED_RULES'].get(key)

def _bc_more_scoped_targets(docs):
    return [doc for doc in docs if _bc_more_expected_color(doc) is not None]

def _bc_more_scoped_check(docs):
    return all(doc.get('f_kleur') == _bc_more_expected_color(doc) for doc in _bc_more_scoped_targets(docs))

def _bc_more_matching_fallback(doc, original_raw, original_exact):
    if not _bc_more_empty_color(original_raw) or not _bc_more_empty_color(original_exact):
        return None
    if _BC_SIMPLE_COLORS['normalize'](doc.get('vendor')) != 'cottoceramix' or not _bc_acero_is_tile(doc):
        return None
    rule = _BC_MORE_COLOR_FALLBACKS.get(doc.get('handle'))
    if rule is None or not isinstance(doc.get('title'), str):
        return None
    if hashlib.sha256(doc['title'].encode('utf-8')).hexdigest() != rule['title_sha256']:
        return None
    aliases = doc.get('sku_aliases')
    if aliases is not None and not isinstance(aliases, (list, tuple)):
        return None
    if aliases and any(not isinstance(sku, str) or not sku for sku in aliases):
        return None
    skus = list(aliases) if aliases else _bc_simple_strings(doc.get('sku_exact'))
    if doc.get('price_varies') is True or {sku.casefold() for sku in skus} != {rule['sku'].casefold()}:
        return None
    return rule

_bc_more_original_enrich = enrich_b2c_documents
def enrich_b2c_documents(docs, definitions, schema):
    original_colors = {doc['id']: (copy.deepcopy(doc.get('f_kleur')), copy.deepcopy(doc.get('f_kleur_exact'))) for doc in docs}
    stats = _bc_more_original_enrich(docs, definitions, schema)
    _BC_MORE_COLOR_RECOVERED.clear()
    for doc in docs:
        if not _bc_more_empty_color(doc.get('f_kleur')):
            continue
        rule = _bc_more_matching_fallback(doc, *original_colors[doc['id']])
        if rule is None:
            continue
        # A derived color is not a copied manufacturer color: retain the blank.
        doc['f_kleur'] = list(rule['colors'])
        doc['f_kleur_exact'] = ''
        _BC_MORE_COLOR_RECOVERED[doc['id']] = {
            'provenance': rule['provenance'], 'matched_sku': rule['sku'],
            'handle': rule['handle'], 'title_sha256': rule['title_sha256'],
            'colors': list(rule['colors']), 'source_color_missing': True}
    stats['more_color_scoped_products'] = len(_bc_more_scoped_targets(docs))
    stats['more_color_missing_recovered'] = len(_BC_MORE_COLOR_RECOVERED)
    return stats

def _bc_more_recovery_check(docs):
    by_id = {doc['id']: doc for doc in docs}
    for identity, record in _BC_MORE_COLOR_RECOVERED.items():
        doc = by_id.get(identity)
        if doc is None or doc.get('f_kleur_exact') != '' or doc.get('f_kleur') != record['colors']:
            return False
        rule = _bc_more_matching_fallback(doc, None, None)
        if rule is None or record['provenance'] != rule['provenance'] or record['source_color_missing'] is not True:
            return False
    return True
'''


def _sha(source):
    return hashlib.sha256(source.encode('utf-8')).hexdigest()


def _replace_once(source, old, new):
    if source.count(old) != 1:
        raise RuntimeError('Kleurhook ontbreekt of is niet uniek')
    return source.replace(old, new, 1)


def _offsets(source, node):
    lines = source.splitlines(keepends=True)
    start = len(''.join(lines[:node.lineno - 1])) + len(lines[node.lineno - 1].encode()[:node.col_offset].decode())
    end = len(''.join(lines[:node.end_lineno - 1])) + len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())
    return start, end


def _ordered_colors(value, namespace):
    taxonomy = namespace['TAXONOMY']
    if (not isinstance(value, list) or not value
            or any(not isinstance(color, str) or color not in taxonomy for color in value)
            or len(value) != len(set(value))):
        raise RuntimeError('Kleurregel bevat ongeldige basiskleuren')
    return [color for color in taxonomy if color in value]


def reviewed_scoped_rules(rules, namespace):
    if not isinstance(rules, list) or not rules:
        raise RuntimeError('Een niet-lege lijst beoordeelde serie/kleurregels is vereist')
    result = {}
    for rule in rules:
        if (not isinstance(rule, dict) or any(not isinstance(rule.get(key), str) or not rule[key].strip()
                for key in ('vendor', 'series', 'exact_color'))):
            raise RuntimeError('Kleurregels vereisen exact merk, serie en bronkleur')
        confidence = rule.get('confidence')
        if isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not .70 <= confidence <= 1:
            raise RuntimeError('Visuele kleurregel mist voldoende vastgelegde zekerheid')
        colors = _ordered_colors(rule.get('colors'), namespace)
        key = (namespace['normalize'](rule['vendor']), namespace['normalize_series'](rule['series']),
               namespace['normalize'](rule['exact_color']))
        if key in result and result[key] != colors:
            raise RuntimeError('Tegenstrijdige serie/kleurregels na normalisatie: ' + ' / '.join(key))
        prior = namespace['classify_color'](rule['exact_color'], {'vendor': rule['vendor'], 'series': rule['series'],
                    'is_tile': True, 'cotto_explicit_series': True})
        if prior.get('confidence') in ('OWNER_CONFIRMED', 'INFERRED_VISUAL') and set(prior['colors']) != set(colors):
            raise RuntimeError('Nieuwe kleurregel strijdt met een bestaande bevestigde of beoordeelde regel')
        result[key] = colors
    return dict(sorted(result.items()))


def reviewed_fallback_rules(rules, namespace):
    if not isinstance(rules, list) or not rules:
        raise RuntimeError('Een niet-lege lijst gecontroleerde ontbrekende-kleurregels is vereist')
    result = {}
    for rule in rules:
        if (not isinstance(rule, dict) or any(not isinstance(rule.get(key), str) or not rule[key].strip()
                for key in ('vendor', 'sku', 'handle', 'title_sha256', 'provenance'))):
            raise RuntimeError('Ontbrekende-kleurregel mist verplichte identiteit of herkomst')
        if namespace['normalize'](rule['vendor']) != 'cottoceramix':
            raise RuntimeError('Ontbrekende-kleurherstel is uitsluitend voor de gecontroleerde Cotto-producten')
        if rule['provenance'] not in ('OFFICIAL_COTTO_BMN', 'TITLE_EXPLICIT_COLOR'):
            raise RuntimeError('Onbekende herkomst voor ontbrekende-kleurherstel')
        digest = rule['title_sha256']
        if len(digest) != 64 or any(char not in '0123456789abcdef' for char in digest):
            raise RuntimeError('Ontbrekende-kleurregel mist een exacte titelhash')
        core = {key: rule[key] for key in ('vendor', 'sku', 'handle', 'title_sha256', 'provenance')}
        core['colors'] = _ordered_colors(rule.get('colors'), namespace)
        if rule['handle'] in result and result[rule['handle']] != core:
            raise RuntimeError('Tegenstrijdige ontbrekende-kleurregels voor dezelfde producthandle')
        result[rule['handle']] = core
    return dict(sorted(result.items()))


def patch_more_worker(source):
    if not isinstance(source, str):
        raise RuntimeError('Workerbron moet tekst zijn')
    if MARKER in source:
        if source.count(MARKER) != 1 or not PATCHED_WORKER_SHA256 or _sha(source) != PATCHED_WORKER_SHA256:
            raise RuntimeError('Bestaande extra-kleurcorrectie wijkt af; niets gewijzigd')
        compile(source, '<existing-more-color-worker>', 'exec')
        return source
    if _sha(source) != BASE_WORKER_SHA256:
        raise RuntimeError('Worker wijkt af van de beoordeelde Bone-liveversie')
    tree = ast.parse(source)
    literals = [node.args[0] for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'compile'
                and len(node.args) >= 3 and isinstance(node.args[1], ast.Constant)
                and node.args[1].value == '<derived-color-rules>' and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)]
    if len(literals) != 1:
        raise RuntimeError('Geen unieke afgeleide kleurmodule')
    literal = literals[0]
    namespace = {'__name__': 'reviewed_more_color_source'}
    exec(compile(literal.value, '<reviewed-more-color-source>', 'exec'), namespace)
    scoped = reviewed_scoped_rules(SCOPED_RULES, namespace)
    fallbacks = reviewed_fallback_rules(FALLBACK_RULES, namespace)
    colors = _replace_once(literal.value, '\ndef classify_color(raw, context=None):\n',
        '\nMORE_TILE_SCOPED_RULES = ' + repr(scoped) + '\n\ndef classify_color(raw, context=None):\n')
    colors = _replace_once(colors, '    if s in NO_COLOR:\n',
        "    if ctx.get('is_tile') is True and ctx.get('cotto_explicit_series') is True and not ctx.get('_bc_bone_compound_component'):\n"
        "        visual = MORE_TILE_SCOPED_RULES.get((vendor, series, s))\n"
        "        if visual is not None:\n"
        "            return _result(raw, visual, 'INFERRED_VISUAL', 'Reviewed exact vendor/series/color product swatch; manufacturer name retained.')\n"
        '    if s in NO_COLOR:\n')
    compile(colors, '<more-tile-color-rules>', 'exec')
    start, end = _offsets(source, literal)
    result = source[:start] + repr(colors) + source[end:]
    tree = ast.parse(result)
    snapshots = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == '_bc_simple_snapshot']
    checks = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'check_b2c_profiles']
    guards = [node for node in tree.body if isinstance(node, ast.If) and ast.unparse(node.test) == "__name__ == '__main__'"]
    if len(snapshots) != 1 or len(checks) != 2 or len(guards) != 1:
        raise RuntimeError('Verwachte bestaande workerhooks verschillen')
    returns = [node for node in checks[-1].body if isinstance(node, ast.Return)]
    if len(returns) != 1 or checks[-1].body[-1] is not returns[0]:
        raise RuntimeError('Geen unieke eindcontrole voor filters')
    lines = result.splitlines(keepends=True)
    helpers = '_BC_MORE_COLOR_FALLBACKS = ' + repr(fallbacks) + '\n' + HELPERS.rstrip() + '\n\n'
    positions = [
        (sum(len(line) for line in lines[:snapshots[0].end_lineno]),
         "    if not _bc_more_scoped_check(docs) or not _bc_more_recovery_check(docs):\n"
         "        raise RuntimeError('Extra tegelkleuren voldoen niet aan beoordeelde regels of herkomstcontroles')\n"
         "    snapshot['more_tile_colors_v1'] = True\n"
         "    snapshot['more_scoped_color_products'] = len(_bc_more_scoped_targets(docs))\n"
         "    snapshot['more_missing_color_products'] = len(_BC_MORE_COLOR_RECOVERED)\n"
         "    snapshot['more_missing_color_provenance'] = copy.deepcopy(_BC_MORE_COLOR_RECOVERED)\n"
         "    snapshot['more_missing_color_counts'] = dict(collections.Counter(record['provenance'] for record in _BC_MORE_COLOR_RECOVERED.values()))\n"),
        (sum(len(line) for line in lines[:returns[0].lineno - 1]),
         "    checks.append({'name': 'Extra tegel-seriekleuren volgen beoordeelde productstalen',\n"
         "                   'passed': snapshot.get('more_tile_colors_v1') is True and _bc_more_scoped_check(docs),\n"
         "                   'products': len(_bc_more_scoped_targets(docs))})\n"
         "    checks.append({'name': 'Ontbrekende tegelkleuren uitsluitend hersteld met exacte identiteit en vastgelegde herkomst',\n"
         "                   'passed': snapshot.get('more_tile_colors_v1') is True and _bc_more_recovery_check(docs),\n"
         "                   'products': len(_BC_MORE_COLOR_RECOVERED)})\n"),
        (sum(len(line) for line in lines[:guards[0].lineno - 1]), helpers),
    ]
    for position, text in sorted(positions, reverse=True):
        result = result[:position] + text + result[position:]
    if result.count(MARKER) != 1:
        raise RuntimeError('Extra-kleurcorrectie niet eenduidig toegevoegd')
    compile(result, '<more-tile-color-worker>', 'exec')
    return result
