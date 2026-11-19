"""Pure, version-guarded patch for the reviewed product-level search worker.

This module does not read or write server files and does not contact Shopify.
The installer supplies the reviewed worker source, then injects the separately
reviewed ``patch_variant_api`` function before compiling the complete program.
"""
from __future__ import annotations

import ast
import hashlib


BASE_WORKER_SHA256 = "2064b549e173d709fe1d5e8e5fe8cb549276e817d46b111510fcc4bc12471cf2"
PATCH_MARKER = "# BC_MULTI_VARIANT_PRODUCTS_V1"


HELPERS = r'''
# BC_MULTI_VARIANT_PRODUCTS_V1
def _bc_variant_summary(product):
    from decimal import InvalidOperation
    variants = product.get('_variants')
    if not isinstance(variants, list) or not variants:
        raise RuntimeError('Geen varianten in volledige productexport voor ' + product['id'])
    choices = []
    aliases = set()
    identities = set()
    for variant in variants:
        if not isinstance(variant, dict):
            raise RuntimeError('Ongeldige variant voor ' + product['id'])
        identity = variant.get('id')
        if not isinstance(identity, str) or not re.fullmatch(r'gid://shopify/ProductVariant/[0-9]+', identity):
            raise RuntimeError('Variantidentiteit ontbreekt voor ' + product['id'])
        if identity in identities:
            raise RuntimeError('Dubbele variantidentiteit voor ' + product['id'])
        identities.add(identity)
        raw_sku = variant.get('sku') or ''
        if not isinstance(raw_sku, str):
            raise RuntimeError('Ongeldig variantartikelnummer voor ' + product['id'])
        if raw_sku.strip():
            aliases.add(raw_sku.strip().casefold())
        try:
            if isinstance(variant.get('price'), bool):
                raise ValueError('boolean price')
            cents = Decimal(variant['price']) * 100
            valid = cents.is_finite() and cents >= 0 and cents == cents.to_integral_value()
        except (InvalidOperation, ValueError, TypeError, KeyError):
            valid = False
        if not valid:
            raise RuntimeError('Onjuiste variantprijs bij ' + product['id'])
        choices.append((int(cents), int(identity.rsplit('/', 1)[-1]), variant))
    choices.sort(key=lambda item: (item[0], item[1]))
    return {'variant': choices[0][2], 'sku_aliases': sorted(aliases),
            'price_varies': len({item[0] for item in choices}) > 1,
            'variant_count': len(choices)}


def _bc_add_variant_schema(schema):
    fields = [dict(field) for field in schema['fields']]
    additions = [{'name': 'sku_aliases', 'type': 'string[]', 'facet': True, 'optional': True},
                 {'name': 'price_varies', 'type': 'bool', 'optional': True}]
    for addition in additions:
        current = [field for field in fields if field['name'] == addition['name']]
        if current:
            if len(current) != 1 or any(current[0].get(key) != value for key, value in addition.items()):
                raise RuntimeError('Bestaand variantschemaveld wijkt af: ' + addition['name'])
        else:
            fields.append(addition)
    return {**schema, 'fields': fields}


def _bc_variant_probe(docs):
    for product in sorted(docs, key=lambda item: int(item['id'])):
        secondary = [sku for sku in product.get('sku_aliases', []) if sku != product['sku_exact']]
        if not secondary:
            continue
        query = secondary[0]
        expected = {item['id']: {key: item[key] for key in
                    ('price_cents', 'price_varies', 'sku_aliases')}
                    for item in docs if query in item.get('sku_aliases', [])}
        return {'query': query, 'expected': expected}
    return None


def _bc_variant_hot_check(snapshot, base, label):
    sample = snapshot.get('variant_probe')
    if not sample:
        return []
    expected = sample['expected']
    observed = {}
    page = 1
    good = True
    while True:
        data, _ = probe(base + '/api/v1/search', {'collection': '__all__',
            'q': sample['query'], 'per_page': 100, 'page': page, 'include_facets': False})
        if data.get('found') != len(expected):
            good = False
            break
        hits = data.get('products', [])
        for product in hits:
            identity = product.get('id')
            if identity in observed or identity not in expected:
                good = False
            observed[identity] = product
        if len(observed) >= len(expected):
            break
        if not hits or page > len(expected):
            good = False
            break
        page += 1
    good = good and set(observed) == set(expected) and all(
        all(observed[identity].get(key) == value for key, value in fields.items())
        for identity, fields in expected.items())
    return [{'name': label + ' tweede variantartikelnummer vindt dezelfde productkaart',
             'passed': good, 'expected_count': len(expected), 'actual_count': len(observed)}]
'''


def _replace_once(value: str, before: str, after: str, label: str) -> str:
    if value.count(before) != 1:
        raise RuntimeError("Workerfragment wijkt af: " + label)
    return value.replace(before, after, 1)


def _replace_function(source: str, name: str, replacements: list[tuple[str, str]]) -> str:
    tree = ast.parse(source)
    matches = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name]
    if len(matches) != 1:
        raise RuntimeError("Workerfunctie ontbreekt of is dubbel: " + name)
    node = matches[0]
    lines = source.splitlines(keepends=True)
    text = "".join(lines[node.lineno - 1:node.end_lineno])
    for index, (before, after) in enumerate(replacements):
        text = _replace_once(text, before, after, name + ":" + str(index))
    lines[node.lineno - 1:node.end_lineno] = [text]
    return "".join(lines)


def patch_worker(source: str) -> str:
    """Return a patched copy only for the exact reviewed deployed worker."""
    if not isinstance(source, str):
        raise TypeError("Workerbron moet tekst zijn")
    if hashlib.sha256(source.encode("utf-8")).hexdigest() != BASE_WORKER_SHA256:
        raise RuntimeError("Workerhash wijkt af van de gecontroleerde versie; niets gewijzigd")
    source = _replace_function(source, "normalize_products", [
        ("""        if len(variants) != 1:
            raise RuntimeError('Meer of minder dan één variant voor ' + p['id'] + '; eerst variantlogica beoordelen')
        variant = variants[0]; sku = variant.get('sku') or ''""",
         """        variant_info = _bc_variant_summary(p)
        variant = variant_info['variant']; sku = variant.get('sku') or ''"""),
        ("verified = (isinstance(manifest, dict)", "verified = (len(variants) == 1 and isinstance(manifest, dict)"),
        ("general = not (sku.upper().startswith('SPOM') or discovery.get('general_filters') == 'excluded')",
         """service_only = (sku.upper().startswith('SPOM') if len(variants) == 1 else
            bool(variant_info['sku_aliases']) and all(value.startswith('spom') for value in variant_info['sku_aliases']))
        general = not (service_only or discovery.get('general_filters') == 'excluded')"""),
        ("        stats['verified_manifests' if verified else 'without_verified_manifest'] += 1",
         """        d['sku_aliases'] = variant_info['sku_aliases']
        d['price_varies'] = variant_info['price_varies']
        stats['multi_variant_products'] += int(len(variants) > 1)
        stats['variants'] += len(variants)
        stats['verified_manifests' if verified else 'without_verified_manifest'] += 1"""),
    ])
    source = _replace_function(source, "patch_api", [
        ("return patch_rvs_api(patch_b2c_api(patch_generation_api(source)))",
         "return patch_variant_api(patch_rvs_api(patch_b2c_api(patch_generation_api(source))))")
    ])
    source = _replace_function(source, "selected", [
        ("if d['sku_exact'] != q: continue",
         "if q not in (d.get('sku_aliases', []) if snapshot.get('variant_aliases_v1') else [d['sku_exact']]): continue")
    ])
    source = _replace_function(source, "make_cases", [
        ("    for case in cases:\n        case['expected_ids']",
         """    variant_probe = snapshot.get('variant_probe')
    if variant_probe:
        cases.append({'name': 'Tweede variantartikelnummer vindt één productdocument',
            'body': {'collection': '__all__', 'q': variant_probe['query'], 'include_facets': False}, 'status': 200})
    for case in cases:
        case['expected_ids']""")
    ])
    source = _replace_function(source, "check_api", [
        ("('price_cents', 'title', 'handle', 'image_url')",
         "('price_cents', 'title', 'handle', 'image_url', 'sku_aliases', 'price_varies')")
    ])
    source = _replace_function(source, "prepare", [
        ("    for key in ('default_sorting_field'", "    schema = _bc_add_variant_schema(schema)\n    for key in ('default_sorting_field'"),
        ("'exact': sorted({d['sku_exact'] for d in docs if d['sku_exact']}),",
         """'exact': sorted({alias for d in docs for alias in d['sku_aliases']}),
        'variant_aliases_v1': True, 'variant_probe': _bc_variant_probe(docs),"""),
    ])
    source = _replace_function(source, "hot_checks", [
        ("    return checks", "        checks += _bc_variant_hot_check(snapshot, base, label)\n    return checks")
    ])
    source = _replace_once(source, "def normalize_products(", HELPERS.strip() + "\n\n\ndef normalize_products(", "helper insertion")
    compile(source, "<patched-search-worker>", "exec")
    return source
