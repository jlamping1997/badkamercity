"""Pure, guarded patch for the existing product-level search API.

The installer embeds ``patch_variant_api`` into the worker. It only changes
request planning; the existing generation, B2C and RVS middleware stay intact.
"""


def patch_variant_api(source: str) -> str:
    """Add generation-gated SKU aliases without changing legacy requests."""
    import ast
    import hashlib

    marker = '# BC_VARIANT_ALIASES_V1'
    original_fingerprint = '8caafe524fbe3b01b96217e7ce1c67673afd688e3d4da187b06438ea05026467'
    patched_fingerprint = '275c494351dbf4152da8f18d34babd028a110be7e9739249d078b79d9fe990d6'

    def fingerprint(node):
        # Python 3.12 adds an empty type_params field to function nodes. Ignore
        # only that empty field so the guard also works on the VPS interpreter.
        def canonical(value):
            if isinstance(value, ast.AST):
                return (type(value).__name__, tuple(
                    (key, canonical(child)) for key, child in ast.iter_fields(value)
                    if not (key == 'type_params' and not child)))
            if isinstance(value, list):
                return tuple(canonical(child) for child in value)
            return value
        return hashlib.sha256(repr(canonical(node)).encode('utf-8')).hexdigest()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        raise RuntimeError('Zoek-API bevat ongeldige Python-code') from None
    plans = [node for node in tree.body
             if isinstance(node, ast.FunctionDef) and node.name == 'plan']
    if len(plans) != 1:
        raise RuntimeError('Zoek-API mist de verwachte unieke planfunctie')
    plan = plans[0]
    current = fingerprint(plan)
    if marker in source:
        if source.count(marker) != 1 or current != patched_fingerprint:
            raise RuntimeError('Bestaande variantpatch wijkt af; geen wijziging')
        return source
    if current != original_fingerprint:
        raise RuntimeError('Zoek-API planfunctie wijkt af van de beoordeelde versie')

    variable = '_bc_variant_aliases_v1'
    flag = ast.parse(
        variable + " = _bc_snapshot().get('variant_aliases_v1') is True"
    ).body[0]
    plan.body.insert(0, flag)
    replacements = {'exact': 0, 'query': 0, 'fields': 0}

    class Rewrite(ast.NodeTransformer):
        def visit_BinOp(self, node):
            self.generic_visit(node)
            if (isinstance(node.op, ast.Add) and
                    isinstance(node.left, ast.Constant) and
                    node.left.value == 'sku_exact:='):
                node.left = ast.IfExp(
                    test=ast.Name(id=variable, ctx=ast.Load()),
                    body=ast.Constant(value='sku_aliases:='),
                    orelse=ast.Constant(value='sku_exact:='))
                replacements['exact'] += 1
            return node

        def visit_Dict(self, node):
            self.generic_visit(node)
            for position, key in enumerate(node.keys):
                if not isinstance(key, ast.Constant):
                    continue
                value = node.values[position]
                if (key.value == 'query_by' and isinstance(value, ast.Constant)
                        and value.value == 'title,sku,vendor,f_productsoort'):
                    suffix = ',sku_aliases'
                    replacements['query'] += 1
                elif (key.value == 'include_fields' and
                      isinstance(value, ast.Constant) and value.value ==
                      'id,shopify_product_id,sku,title,handle,vendor,product_type,price_cents,url,image_url'):
                    suffix = ',sku_aliases,price_varies'
                    replacements['fields'] += 1
                else:
                    continue
                node.values[position] = ast.BinOp(
                    left=value, op=ast.Add(), right=ast.IfExp(
                        test=ast.Name(id=variable, ctx=ast.Load()),
                        body=ast.Constant(value=suffix),
                        orelse=ast.Constant(value='')))
            return node

    Rewrite().visit(plan)
    if replacements != {'exact': 1, 'query': 1, 'fields': 1}:
        raise RuntimeError('Niet alle verwachte variantzoekvelden zijn gevonden')
    ast.fix_missing_locations(plan)
    if fingerprint(plan) != patched_fingerprint:
        raise RuntimeError('Variantzoekpatch is niet gelijk aan de beoordeelde versie')
    lines = source.splitlines(keepends=True)
    start = sum(len(line) for line in lines[:plan.lineno - 1])
    end = sum(len(line) for line in lines[:plan.end_lineno])
    result = source[:start] + ast.unparse(plan) + '\n' + source[end:]
    result = result.rstrip() + '\n\n' + marker + '\n'
    compile(result, '<variant-search-api>', 'exec')
    return result
