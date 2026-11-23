"""Guarded, catalog-free Cottoceramix visual color corrections.

The release builder freezes reviewed rules and the resulting worker hash.
Manufacturer fields, existing owner rules, API source and size codes are kept.
"""
import ast
import hashlib

BASE_WORKER_SHA256 = '3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb'
PATCHED_WORKER_SHA256 = None
SCOPED_RULES = None
MARKER = '# BC_COTTO_VISUAL_COLORS_V1'

HELPERS = '''
# BC_COTTO_VISUAL_COLORS_V1
def _bc_cotto_expected_color(doc):
    rules = _BC_SIMPLE_COLORS['COTTO_VISUAL_SCOPED_RULES']
    normalize_color = _BC_SIMPLE_COLORS['normalize']
    normalize_series_color = _BC_SIMPLE_COLORS['normalize_series']
    if normalize_color(doc.get('vendor')) != 'cottoceramix' or not _bc_acero_is_tile(doc):
        return None
    raw = doc.get('f_kleur_exact')
    series = _bc_simple_strings(doc.get('f_serie')) or _bc_simple_strings(doc.get('series'))
    if not isinstance(raw, str) or len(series) != 1:
        return None
    return rules.get((normalize_series_color(series[0]), normalize_color(raw)))

def _bc_cotto_targets(docs):
    return [doc for doc in docs if _bc_cotto_expected_color(doc) is not None]

def _bc_cotto_check(docs):
    return all(doc.get('f_kleur') == _bc_cotto_expected_color(doc)
               for doc in _bc_cotto_targets(docs))
'''


def _sha(source):
    return hashlib.sha256(source.encode('utf-8')).hexdigest()


def _replace_once(source, old, new):
    if source.count(old) != 1:
        raise RuntimeError('Cotto-kleurhook ontbreekt of is niet uniek')
    return source.replace(old, new, 1)


def _offsets(source, node):
    lines = source.splitlines(keepends=True)
    start = len(''.join(lines[:node.lineno - 1])) + len(lines[node.lineno - 1].encode()[:node.col_offset].decode())
    end = len(''.join(lines[:node.end_lineno - 1])) + len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())
    return start, end


def reviewed_rule_map(rules, namespace):
    if not isinstance(rules, list) or not rules:
        raise RuntimeError('Een niet-lege lijst beoordeelde Cotto-kleurregels is vereist')
    normalize_color = namespace['normalize']
    normalize_series_color = namespace['normalize_series']
    taxonomy = namespace['TAXONOMY']
    owners = {(normalize_color(v), normalize_series_color(s), normalize_color(raw)): colors
              for v, s, raw, colors, _primary in namespace['OWNER_RULES']}
    result = {}
    for rule in rules:
        if (not isinstance(rule, dict) or not isinstance(rule.get('series'), str)
                or not isinstance(rule.get('exact_color'), str)
                or not rule['series'].strip() or not rule['exact_color'].strip()):
            raise RuntimeError('Kleurregels vereisen een exacte serie en bronkleur')
        confidence = rule.get('confidence')
        if (isinstance(confidence, bool) or not isinstance(confidence, (int, float))
                or not .70 <= confidence <= 1):
            raise RuntimeError('Visuele kleurregel mist voldoende vastgelegde zekerheid')
        colors = rule.get('colors')
        if (not isinstance(colors, list) or not colors
                or any(not isinstance(color, str) or color not in taxonomy for color in colors)
                or len(colors) != len(set(colors))):
            raise RuntimeError('Visuele kleurregel bevat ongeldige basiskleuren')
        ordered = [color for color in taxonomy if color in colors]
        key = (normalize_series_color(rule['series']), normalize_color(rule['exact_color']))
        if key in result and result[key] != ordered:
            raise RuntimeError('Tegenstrijdige Cotto-regels na normalisatie van serie/kleur: ' + ' / '.join(key))
        owner = owners.get(('cottoceramix', *key))
        if owner is not None and set(owner) != set(ordered):
            raise RuntimeError('Visuele kleurregel strijdt met een expliciete eigenaarregel')
        if key[1] == 'acero' and ordered != ['Grijs']:
            raise RuntimeError('De bevestigde Acero-regel moet behouden blijven')
        result[key] = ordered
    return dict(sorted(result.items()))


def patch_cotto_worker(source):
    if not isinstance(source, str):
        raise RuntimeError('Workerbron moet tekst zijn')
    if MARKER in source:
        if source.count(MARKER) != 1 or not PATCHED_WORKER_SHA256 or _sha(source) != PATCHED_WORKER_SHA256:
            raise RuntimeError('Bestaande Cotto-kleurcorrectie wijkt af; niets gewijzigd')
        compile(source, '<existing-cotto-worker>', 'exec')
        return source
    if _sha(source) != BASE_WORKER_SHA256:
        raise RuntimeError('Worker wijkt af van de beoordeelde liveversie')
    tree = ast.parse(source)
    literals = [node.args[0] for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'compile' and len(node.args) >= 3
                and isinstance(node.args[1], ast.Constant) and node.args[1].value == '<derived-color-rules>'
                and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)]
    if len(literals) != 1:
        raise RuntimeError('Geen unieke afgeleide kleurmodule')
    literal = literals[0]
    namespace = {'__name__': 'reviewed_cotto_color_source'}
    exec(compile(literal.value, '<reviewed-cotto-color-source>', 'exec'), namespace)
    rules = reviewed_rule_map(SCOPED_RULES, namespace)
    colors = _replace_once(literal.value,
        '\ndef classify_color(raw, context=None):\n',
        '\nCOTTO_VISUAL_SCOPED_RULES = ' + repr(rules) + '\n\ndef classify_color(raw, context=None):\n')
    colors = _replace_once(colors,
        "    if vendor == 'porcelanosa' and s == 'caliza':\n",
        "    if vendor == 'cottoceramix' and ctx.get('is_tile') is True and ctx.get('cotto_explicit_series') is True:\n"
        "        visual = COTTO_VISUAL_SCOPED_RULES.get((series, s))\n"
        "        if visual is not None:\n"
        "            return _result(raw, visual, 'INFERRED_VISUAL', 'Reviewed exact series/color product swatch; manufacturer name retained.')\n"
        "    if vendor == 'porcelanosa' and s == 'caliza':\n")
    colors = _replace_once(colors,
        "    series_values = _strings(doc.get('f_serie')) or _strings(doc.get('series'))\n",
        "    series_values = _strings(doc.get('f_serie')) or _strings(doc.get('series'))\n"
        "    cotto_explicit_series = len(series_values) == 1\n")
    old_context = "return [{'vendor': vendor, 'series': s, 'is_tile': doc.get('_bc_tile_color_context') is True} for s in series_values] if len(series_values) == 1 else [{'vendor': vendor, 'is_tile': doc.get('_bc_tile_color_context') is True}]"
    new_context = "return [{'vendor': vendor, 'series': s, 'is_tile': doc.get('_bc_tile_color_context') is True, 'cotto_explicit_series': cotto_explicit_series} for s in series_values] if len(series_values) == 1 else [{'vendor': vendor, 'is_tile': doc.get('_bc_tile_color_context') is True, 'cotto_explicit_series': False}]"
    colors = _replace_once(colors, old_context, new_context)
    compile(colors, '<cotto-visual-color-rules>', 'exec')
    start, end = _offsets(source, literal)
    result = source[:start] + repr(colors) + source[end:]
    tree = ast.parse(result)
    snapshots = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == '_bc_simple_snapshot']
    checks = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'check_b2c_profiles']
    guards = [node for node in tree.body if isinstance(node, ast.If) and ast.unparse(node.test) == "__name__ == '__main__'"]
    if len(snapshots) != 1 or len(checks) != 2 or len(guards) != 1:
        raise RuntimeError('Verwachte bestaande workerhooks verschillen')
    check = checks[-1]
    returns = [node for node in check.body if isinstance(node, ast.Return)]
    if len(returns) != 1 or check.body[-1] is not returns[0]:
        raise RuntimeError('Geen unieke eindcontrole voor filters')
    lines = result.splitlines(keepends=True)
    positions = [
        (sum(len(line) for line in lines[:snapshots[0].end_lineno]),
         "    if not _bc_cotto_check(docs):\n"
         "        raise RuntimeError('Cotto-tegelkleuren voldoen niet aan beoordeelde serieregels')\n"
         "    snapshot['cotto_visual_colors_v1'] = True\n"
         "    snapshot['cotto_visual_color_products'] = len(_bc_cotto_targets(docs))\n"),
        (sum(len(line) for line in lines[:returns[0].lineno - 1]),
         "    checks.append({'name': 'Cotto-seriekleuren volgen beoordeelde productstalen; bronkleur behouden',\n"
         "                   'passed': snapshot.get('cotto_visual_colors_v1') is True and _bc_cotto_check(docs),\n"
         "                   'products': len(_bc_cotto_targets(docs))})\n"),
        (sum(len(line) for line in lines[:guards[0].lineno - 1]), HELPERS.rstrip() + '\n\n'),
    ]
    for position, text in sorted(positions, reverse=True):
        result = result[:position] + text + result[position:]
    if result.count(MARKER) != 1:
        raise RuntimeError('Cotto-kleurcorrectie niet eenduidig toegevoegd')
    compile(result, '<cotto-color-corrected-worker>', 'exec')
    return result
