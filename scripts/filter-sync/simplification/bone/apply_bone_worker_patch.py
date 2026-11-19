"""Guarded owner-confirmed correction: exact Bone tile colors belong to Beige.

The existing Cottoceramix visual rules and all source fields remain intact.
"""
import ast
import hashlib

BASE_WORKER_SHA256 = 'cc13abd05c87a490bf06d0a7358ef36bc700edc0a736a48714d704df62f8dcc2'
PATCHED_WORKER_SHA256 = 'a8dd54597a2a372a7b0fcce9357a6bcc31a406fca2631cb9b24918f5fea0ff17'
MARKER = '# BC_TILE_BONE_BEIGE_V1'

HELPERS = '''
# BC_TILE_BONE_BEIGE_V1
def _bc_bone_targets(docs):
    normalize_color = _BC_SIMPLE_COLORS['normalize']
    return [doc for doc in docs if _bc_acero_is_tile(doc)
            and isinstance(doc.get('f_kleur_exact'), str)
            and normalize_color(doc['f_kleur_exact']) == 'bone']

def _bc_bone_check(docs):
    return all(doc.get('f_kleur') == ['Beige'] for doc in _bc_bone_targets(docs))
'''


def _sha(source):
    return hashlib.sha256(source.encode('utf-8')).hexdigest()


def _replace_once(source, old, new):
    if source.count(old) != 1:
        raise RuntimeError('Bone-hook ontbreekt of is niet uniek')
    return source.replace(old, new, 1)


def _offsets(source, node):
    lines = source.splitlines(keepends=True)
    start = len(''.join(lines[:node.lineno - 1])) + len(lines[node.lineno - 1].encode()[:node.col_offset].decode())
    end = len(''.join(lines[:node.end_lineno - 1])) + len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())
    return start, end


def patch_bone_worker(source):
    if not isinstance(source, str):
        raise RuntimeError('Workerbron moet tekst zijn')
    if MARKER in source:
        if source.count(MARKER) != 1 or not PATCHED_WORKER_SHA256 or _sha(source) != PATCHED_WORKER_SHA256:
            raise RuntimeError('Bestaande Bone-correctie wijkt af; niets gewijzigd')
        compile(source, '<existing-bone-worker>', 'exec')
        return source
    if _sha(source) != BASE_WORKER_SHA256:
        raise RuntimeError('Worker wijkt af van de beoordeelde Cotto-liveversie')
    tree = ast.parse(source)
    literals = [node.args[0] for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'compile' and len(node.args) >= 3
                and isinstance(node.args[1], ast.Constant) and node.args[1].value == '<derived-color-rules>'
                and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)]
    if len(literals) != 1:
        raise RuntimeError('Geen unieke afgeleide kleurmodule')
    literal = literals[0]
    colors = _replace_once(literal.value,
        "    series = normalize_series(ctx.get('series'))\n",
        "    series = normalize_series(ctx.get('series'))\n"
        "    if s == 'bone' and ctx.get('is_tile') is True and not ctx.get('_bc_bone_compound_component'):\n"
        "        return _result(raw, ['Beige'], 'OWNER_CONFIRMED', 'Latest owner-confirmed exact Bone tile color; original name retained.')\n")
    colors = _replace_once(colors,
        "components = [classify_color(part, ctx) for part in s.split('/')]",
        "components = [classify_color(part, {**ctx, '_bc_bone_compound_component': True}) for part in s.split('/')]")
    compile(colors, '<bone-derived-color-rules>', 'exec')
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
         "    if not _bc_bone_check(docs):\n"
         "        raise RuntimeError('Bone-tegels zijn niet uitsluitend Beige')\n"
         "    snapshot['tile_bone_beige_v1'] = True\n"
         "    snapshot['tile_bone_beige_products'] = len(_bc_bone_targets(docs))\n"),
        (sum(len(line) for line in lines[:returns[0].lineno - 1]),
         "    checks.append({'name': 'Exacte Bone-tegels horen bij Beige volgens laatste eigenaarcorrectie',\n"
         "                   'passed': snapshot.get('tile_bone_beige_v1') is True and _bc_bone_check(docs),\n"
         "                   'products': len(_bc_bone_targets(docs))})\n"),
        (sum(len(line) for line in lines[:guards[0].lineno - 1]), HELPERS.rstrip() + '\n\n'),
    ]
    for position, text in sorted(positions, reverse=True):
        result = result[:position] + text + result[position:]
    if result.count(MARKER) != 1:
        raise RuntimeError('Bone-correctie niet eenduidig toegevoegd')
    compile(result, '<bone-color-corrected-worker>', 'exec')
    return result
