"""Guarded, catalog-free correction: exact Acero tile colors belong to Grijs.

Only the derived color layer changes. Source colors, other finishes, API code
and exact numeric tile-format selection remain part of the existing worker.
"""
import ast
import hashlib

BASE_WORKER_SHA256 = '25e8c3b1763171875bebd5b85e7099b26f87e36f3ece0b9f1f21e1d37b56dbe3'
PATCHED_WORKER_SHA256 = '3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb'
MARKER = '# BC_ACERO_GRAY_TILE_RULE_V1'

HELPERS = '''
# BC_ACERO_GRAY_TILE_RULE_V1
def _bc_acero_is_tile(doc):
    return any(HANDLE_GROUP.get(handle) == 'tile'
               for handle in _bc_simple_strings(doc.get('collection_handles')))

def _bc_acero_targets(docs):
    normalize_color = _BC_SIMPLE_COLORS['normalize']
    return [doc for doc in docs if _bc_acero_is_tile(doc)
            and isinstance(doc.get('f_kleur_exact'), str)
            and normalize_color(doc['f_kleur_exact']) == 'acero']

def _bc_acero_check(docs):
    return all(doc.get('f_kleur') == ['Grijs'] for doc in _bc_acero_targets(docs))
'''


def _sha(source):
    return hashlib.sha256(source.encode('utf-8')).hexdigest()


def _replace_once(source, old, new):
    if source.count(old) != 1:
        raise RuntimeError('Acero-hook ontbreekt of is niet uniek')
    return source.replace(old, new, 1)


def _offsets(source, node):
    # AST columns are UTF-8 byte offsets, not Python character offsets.
    lines = source.splitlines(keepends=True)
    before = ''.join(lines[:node.lineno - 1])
    after = ''.join(lines[:node.end_lineno - 1])
    start = len(before) + len(lines[node.lineno - 1].encode()[:node.col_offset].decode())
    end = len(after) + len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())
    return start, end


def patch_acero_worker(source):
    if not isinstance(source, str):
        raise RuntimeError('Workerbron moet tekst zijn')
    if MARKER in source:
        if source.count(MARKER) != 1 or _sha(source) != PATCHED_WORKER_SHA256:
            raise RuntimeError('Bestaande Acero-correctie wijkt af; niets gewijzigd')
        compile(source, '<existing-acero-worker>', 'exec')
        return source
    if _sha(source) != BASE_WORKER_SHA256:
        raise RuntimeError('Worker wijkt af van de beoordeelde liveversie')
    tree = ast.parse(source)
    color_literals = []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'compile' and len(node.args) >= 3
                and isinstance(node.args[1], ast.Constant)
                and node.args[1].value == '<derived-color-rules>'
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)):
            color_literals.append(node.args[0])
    if len(color_literals) != 1:
        raise RuntimeError('Geen unieke afgeleide kleurmodule')
    literal = color_literals[0]
    colors = _replace_once(literal.value,
        '    if s in NO_COLOR:\n',
        "    if s == 'acero' and ctx.get('is_tile') is True:\n"
        "        return _result(raw, ['Grijs'], 'OWNER_CONFIRMED', 'Owner-confirmed Acero tile color grouped with gray.')\n"
        '    if s in NO_COLOR:\n')
    colors = _replace_once(colors,
        "return [{'vendor': vendor, 'series': s} for s in series_values] if len(series_values) == 1 else [{'vendor': vendor}]",
        "return [{'vendor': vendor, 'series': s, 'is_tile': doc.get('_bc_tile_color_context') is True} for s in series_values] if len(series_values) == 1 else [{'vendor': vendor, 'is_tile': doc.get('_bc_tile_color_context') is True}]")
    compile(colors, '<acero-derived-color-rules>', 'exec')
    start, end = _offsets(source, literal)
    result = source[:start] + repr(colors) + source[end:]
    result = _replace_once(result,
        "color_doc = {**doc, 'f_kleur': raw}",
        "color_doc = {**doc, 'f_kleur': raw, '_bc_tile_color_context': _bc_acero_is_tile(doc)}")
    tree = ast.parse(result)
    snapshots = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name == '_bc_simple_snapshot']
    profiles = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                and node.name == 'check_b2c_profiles']
    guards = [node for node in tree.body if isinstance(node, ast.If)
              and ast.unparse(node.test) == "__name__ == '__main__'"]
    if len(snapshots) != 1 or len(profiles) != 2 or len(guards) != 1:
        raise RuntimeError('Verwachte bestaande workerhooks verschillen')
    snapshot = snapshots[0]
    checks = profiles[-1]
    returns = [node for node in checks.body if isinstance(node, ast.Return)]
    if len(returns) != 1 or checks.body[-1] is not returns[0]:
        raise RuntimeError('Geen unieke eindcontrole voor filters')
    lines = result.splitlines(keepends=True)
    positions = [
        (sum(len(line) for line in lines[:snapshot.end_lineno]),
         "    if not _bc_acero_check(docs):\n"
         "        raise RuntimeError('Acero-tegels zijn niet uitsluitend Grijs')\n"
         "    snapshot['acero_gray_v1'] = True\n"
         "    snapshot['acero_gray_products'] = len(_bc_acero_targets(docs))\n"),
        (sum(len(line) for line in lines[:returns[0].lineno - 1]),
         "    checks.append({'name': 'Exacte Acero-tegels horen bij Grijs; bronkleur behouden',\n"
         "                   'passed': snapshot.get('acero_gray_v1') is True and _bc_acero_check(docs),\n"
         "                   'products': len(_bc_acero_targets(docs))})\n"),
        (sum(len(line) for line in lines[:guards[0].lineno - 1]), HELPERS.rstrip() + '\n\n'),
    ]
    for position, text in sorted(positions, reverse=True):
        result = result[:position] + text + result[position:]
    if result.count(MARKER) != 1:
        raise RuntimeError('Acero-correctie niet eenduidig toegevoegd')
    compile(result, '<acero-corrected-worker>', 'exec')
    return result
