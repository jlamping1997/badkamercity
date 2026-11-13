"""Guarded request normalization for the existing search API; no deployment."""

_BC_SIMPLE_API_BASE_AST = '76a5ab7e741528d0aa5327b64988fd57d5f3b5fb7f54e952f76ce2bd50e0a938'
_BC_SIMPLE_API_MARKER = '# BC_FILTER_SIMPLIFICATION_V1'
_BC_SIMPLE_API_REQUEST_HELPER = '''def _bc_simple_request(body):
    snapshot = _bc_snapshot()
    if snapshot.get('filter_simplification_v1') is not True:
        return body
    aliases = snapshot.get('filter_color_aliases') or {}
    values = body.filters.get('f_kleur')
    if not isinstance(values, list) or len(values) > 100:
        return body
    normalized = []
    seen = set()
    for value in values:
        if not isinstance(value, str):
            normalized.append(value)
            continue
        canonical = aliases.get(value, value)
        if not isinstance(canonical, str):
            raise RuntimeError('Ongeldige kleurregels in actieve filtergeneratie')
        if canonical not in seen:
            normalized.append(canonical)
            seen.add(canonical)
    if normalized == values:
        return body
    filters = {**body.filters, 'f_kleur': normalized}
    return body.copy(update={'filters': filters})

def _bc_simple_facet_limit(facet):
    if _bc_snapshot().get('filter_simplification_v1') is not True:
        return 100
    if facet.get('field') == 'f_tegel_formaat':
        return 500
    if facet.get('type') == 'range':
        return 100
    count = facet.get('distinct_values', 100)
    if isinstance(count, int) and not isinstance(count, bool):
        return min(1000, max(100, count))
    return 100

def _bc_simple_choice_clause(field, values, quoted_values):
    snapshot = _bc_snapshot()
    if field != 'f_tegel_formaat' or snapshot.get('filter_simplification_v1') is not True:
        return field + (':=' + quoted_values[0] if len(quoted_values) == 1 else ':=[' + ','.join(quoted_values) + ']')
    if snapshot.get('tile_format_codes_v1') is not True:
        raise RuntimeError('Exacte formaatcodes ontbreken in actieve filtergeneratie')
    mapping = snapshot.get('tile_format_codes')
    if not isinstance(mapping, dict) or any(not isinstance(label, str) or type(code) is not int or not 1 <= code <= 2147483647 for label, code in mapping.items()):
        raise RuntimeError('Ongeldige formaatcodekaart in actieve filtergeneratie')
    if len(set(mapping.values())) != len(mapping):
        raise RuntimeError('Dubbele formaatcodes in actieve filtergeneratie')
    codes = list(dict.fromkeys(mapping.get(value, 0) for value in values if isinstance(value, str) and value.strip()))
    # Code zero is reserved and never assigned to a document.
    if len(codes) == 1:
        return 'f_tegel_formaat_code:=' + str(codes[0])
    return 'f_tegel_formaat_code:[' + ','.join(str(code) for code in codes) + ']'
'''


def patch_simple_api(source):
    import ast
    import copy
    import hashlib

    def canonical(value):
        if isinstance(value, ast.AST):
            return (type(value).__name__, tuple((key, canonical(child))
                for key, child in ast.iter_fields(value)
                if not (key == 'type_params' and not child)))
        if isinstance(value, list):
            return tuple(canonical(child) for child in value)
        return value

    def digest(tree):
        return hashlib.sha256(repr(canonical(tree)).encode()).hexdigest()

    tree = ast.parse(source)
    plans = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'plan']
    if len(plans) != 1:
        raise RuntimeError('Geen unieke gecontroleerde filterplanner')
    plan = plans[0]
    assignment = ast.parse('body = _bc_simple_request(body)').body[0]
    expected_helpers = ast.parse(_BC_SIMPLE_API_REQUEST_HELPER).body
    helper_names = {n.name for n in expected_helpers}
    helpers = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in helper_names]

    class FormatClause(ast.NodeTransformer):
        def __init__(self, restore=False):
            self.restore = restore
            self.count = 0

        def visit_Assign(self, node):
            self.generic_visit(node)
            old = ast.parse("clauses[field] = field + (':=' + vals[0] if len(vals) == 1 else ':=[' + ','.join(vals) + ']')").body[0]
            new = ast.parse('clauses[field] = _bc_simple_choice_clause(field, values, vals)').body[0]
            expected, replacement = (new, old) if self.restore else (old, new)
            if canonical(node) == canonical(expected):
                self.count += 1
                return ast.copy_location(replacement, node)
            return node

    class FacetLimit(ast.NodeTransformer):
        def __init__(self, restore=False):
            self.restore = restore
            self.count = 0

        def visit_Dict(self, node):
            self.generic_visit(node)
            for i, key in enumerate(node.keys):
                if isinstance(key, ast.Constant) and key.value == 'max_facet_values':
                    value = node.values[i]
                    expected = ast.parse('_bc_simple_facet_limit(f)', mode='eval').body
                    if self.restore:
                        if canonical(value) != canonical(expected):
                            raise RuntimeError('Onverwachte wijziging in facetlimiet')
                        node.values[i] = ast.Constant(value=100)
                    else:
                        if not isinstance(value, ast.Constant) or value.value != 100:
                            raise RuntimeError('Onverwachte bestaande facetlimiet')
                        node.values[i] = expected
                    self.count += 1
            return node
    if _BC_SIMPLE_API_MARKER in source:
        if source.count(_BC_SIMPLE_API_MARKER) != 1 or len(helpers) != len(expected_helpers):
            raise RuntimeError('Onverwachte bestaande vereenvoudigingspatch')
        if canonical(helpers) != canonical(expected_helpers) or canonical(plan.body[0]) != canonical(assignment):
            raise RuntimeError('Bestaande filtervereenvoudiging is gewijzigd')
        restored = copy.deepcopy(tree)
        restored.body = [n for n in restored.body if not (isinstance(n, ast.FunctionDef) and n.name in helper_names)]
        restored_plan = next(n for n in restored.body if isinstance(n, ast.FunctionDef) and n.name == 'plan')
        restored_plan.body.pop(0)
        clauses = FormatClause(restore=True)
        clauses.visit(restored_plan)
        if clauses.count != 1:
            raise RuntimeError('Exacte formaatplanner is gewijzigd')
        limits = FacetLimit(restore=True)
        limits.visit(restored_plan)
        if limits.count != 1:
            raise RuntimeError('Facetplanner mist de gecontroleerde limiet')
        if digest(restored) != _BC_SIMPLE_API_BASE_AST:
            raise RuntimeError('Overige API-code is tussentijds gewijzigd')
        return source
    if helpers or digest(tree) != _BC_SIMPLE_API_BASE_AST:
        raise RuntimeError('API-bron wijkt af van de beoordeelde actieve versie')
    plan.body.insert(0, assignment)
    clauses = FormatClause()
    clauses.visit(plan)
    if clauses.count != 1:
        raise RuntimeError('Geen unieke keuzeclausule in bestaande planner')
    limits = FacetLimit()
    limits.visit(plan)
    if limits.count != 1:
        raise RuntimeError('Geen unieke facetplannerlimiet')
    ast.fix_missing_locations(plan)
    lines = source.splitlines(keepends=True)
    start = sum(len(line) for line in lines[:plan.lineno - 1])
    end = sum(len(line) for line in lines[:plan.end_lineno])
    result = source[:start] + ast.unparse(plan) + '\n' + source[end:]
    result = result.rstrip() + '\n\n' + _BC_SIMPLE_API_MARKER + '\n' + _BC_SIMPLE_API_REQUEST_HELPER
    compile(result, '<simplified-filter-api>', 'exec')
    # Prove that the added helper and the exact original program can be recovered.
    return patch_simple_api(result)
