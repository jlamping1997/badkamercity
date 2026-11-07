"""Semantic checks for the actual API planner and product response contract.

The portable fixtures are the reviewed API functions, without credentials or
catalog data. When the uploaded runtime is present, all checks use that source.
"""
import ast
import asyncio
from pathlib import Path
from types import SimpleNamespace
import unittest

from variant_api_patch import patch_variant_api

BASELINE_PLAN = r'''def plan(body):
    p = _bc_snapshot()['profiles'].get(body.collection)
    if p is None:
        raise HTTPException(404, 'Onbekende collectie')
    allowed = {f['field']: f for f in p['allowed_filters']}
    clauses = {}
    for field, values in body.filters.items():
        f = allowed.get(field)
        if not f or f['type'] != 'choice':
            raise HTTPException(400, 'Onbekend of ongeldig keuzefilter: ' + field)
        if len(values) > 100:
            raise HTTPException(400, 'Te veel filterwaarden')
        vals = []
        for v in values:
            if f['data_type'] == 'bool':
                if v is True or v == 'true':
                    vals.append('true')
                elif v is False or v == 'false':
                    vals.append('false')
                else:
                    raise HTTPException(400, 'Booleaan verwacht: ' + field)
            else:
                if not isinstance(v, str) or len(v) > 300:
                    raise HTTPException(400, 'Tekstwaarde verwacht: ' + field)
                if v.strip():
                    vals.append(quote(v))
        if vals:
            clauses[field] = field + (':=' + vals[0] if len(vals) == 1 else ':=[' + ','.join(vals) + ']')
    for field, r in body.ranges.items():
        f = allowed.get(field)
        if not f or f['type'] != 'range':
            raise HTTPException(400, 'Onbekend of ongeldig bereikfilter: ' + field)
        if r.min is not None and r.max is not None and (r.min > r.max):
            raise HTTPException(400, 'Minimum ligt boven maximum')

        def bound(value):
            if value is None:
                return None
            if f['data_type'] in ['int32', 'int64']:
                if not value.is_integer():
                    raise HTTPException(400, 'Heel getal verwacht: ' + field)
                return str(int(value))
            return str(value)
        minimum, maximum = (bound(r.min), bound(r.max))
        if minimum is not None and maximum is not None:
            clauses[field] = f'{field}:[{minimum}..{maximum}]'
        elif minimum is not None:
            clauses[field] = f'{field}:>={minimum}'
        elif maximum is not None:
            clauses[field] = f'{field}:<={maximum}'
    exact = body.q.strip().casefold() in _bc_snapshot()['exact']
    base = ['published:=true']
    if body.collection != '__all__':
        base.append('collection_handles:=' + quote(body.collection))
    if exact:
        base.append('sku_exact:=' + quote(body.q.strip().casefold()))
    elif not p['service_category']:
        base.append('general_shopping:=true')

    def filters(exclude=None):
        return ' && '.join(base + [c for f, c in clauses.items() if f != exclude])
    sort = {'relevance': None, 'price_asc': 'price_cents:asc', 'price-asc': 'price_cents:asc', 'price_desc': 'price_cents:desc', 'price-desc': 'price_cents:desc'}
    if body.sort not in sort:
        raise HTTPException(400, 'Onbekende sortering')
    common = {'collection': _bc_snapshot()['collection'], 'q': '*' if exact else body.q.strip() or '*', 'query_by': 'title,sku,vendor,f_productsoort', 'filter_by': filters(), 'drop_tokens_threshold': 0, 'enable_overrides': False}
    main = {**common, 'page': body.page, 'per_page': body.per_page, 'include_fields': 'id,shopify_product_id,sku,title,handle,vendor,product_type,price_cents,url,image_url'}
    if sort[body.sort]:
        main['sort_by'] = sort[body.sort]
    visible = p['filters'] if body.include_facets else []
    searches = [main] + [{**common, 'filter_by': filters(f['field']), 'facet_by': f['field'], 'max_facet_values': 100, 'per_page': 1, 'include_fields': 'id'} for f in visible]
    return (p, visible, searches, exact)
'''

BASELINE_SEARCH = r'''async def search(body: SearchRequest):
    p, visible, searches, exact = plan(body)
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(HOST + '/multi_search', headers={'X-TYPESENSE-API-KEY': KEY}, json={'searches': searches})
        if r.status_code != 200:
            raise ValueError()
        results = r.json()['results']
        if len(results) != len(searches) or any((x.get('error') for x in results)):
            raise ValueError()
    except Exception:
        raise HTTPException(502, 'Zoekindex gaf geen geldige resultaten') from None
    main = results[0]
    products = []
    for h in main.get('hits', []):
        d = h['document']
        products.append({**d, 'product_url': d.get('url'), 'image_alt': d.get('title', '')})
    facets = []
    for f, result in zip(visible, results[1:]):
        fc = next((x for x in result.get('facet_counts', []) if x['field_name'] == f['field']), {})
        counts = fc.get('counts', [])
        stats = fc.get('stats')
        facets.append({**public_filter(f), 'values': counts, 'stats': stats, 'min': (stats or {}).get('min', f.get('min')), 'max': (stats or {}).get('max', f.get('max'))})
    return _bc_b2c_annotate({'found': main.get('found', 0), 'page': body.page, 'per_page': body.per_page, 'collection': {'handle': body.collection, 'title': p['title'], 'profile_products': p['products'], 'shopping_products': p['shopping_products']}, 'products': products, 'facets': facets, 'exact_sku': exact}, _bc_snapshot())
'''

BASELINE_QUOTE = r'''def quote(value):
    return '`' + str(value).replace('\\', '\\\\').replace('`', '\\`') + '`'
'''

BASELINE = '\n\n'.join((BASELINE_QUOTE, BASELINE_PLAN, BASELINE_SEARCH)) + '\n'
UPLOADED = Path(__file__).resolve().parents[3] / 'search-runtime-current' / 'app.py'
SOURCE = UPLOADED.read_text() if UPLOADED.exists() else BASELINE


class HttpFailure(Exception):
    def __init__(self, status_code, detail):
        self.status_code, self.detail = status_code, detail
        super().__init__(detail)


def snapshot(flag=True):
    color = {'field': 'f_kleur', 'label': 'Kleur', 'type': 'choice',
             'data_type': 'string'}
    vendor = {'field': 'vendor', 'label': 'Merk', 'type': 'choice',
              'data_type': 'string'}
    price = {'field': 'price_cents', 'label': 'Prijs', 'type': 'range',
             'data_type': 'int64', 'min': 0, 'max': 50000}
    profile = {'title': 'Alle producten', 'products': 2,
               'shopping_products': 2, 'service_category': False,
               'allowed_filters': [vendor, color, price],
               'filters': [color, price]}
    value = {'collection': 'test_generation', 'exact': {'n8270ch', 'n8271pg'},
             'profiles': {'__all__': profile, 'douches': profile}}
    if flag is not None:
        value['variant_aliases_v1'] = flag
    return value


def body(**overrides):
    values = dict(collection='__all__', q='*', page=1, per_page=24,
                  sort='relevance', filters={}, ranges={}, include_facets=True)
    values.update(overrides)
    return SimpleNamespace(**values)


def functions(source, current, httpx=None):
    tree = ast.parse(source)
    nodes = []
    for name in ('quote', 'plan', 'search', 'public_filter'):
        candidates = [n for n in tree.body
                      if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                      and n.name == name]
        if candidates:
            node = candidates[0]
            node.decorator_list = []
            nodes.append(node)
    ns = {'_bc_snapshot': lambda: current, 'HTTPException': HttpFailure,
          'SearchRequest': object, 'httpx': httpx,
          '_bc_b2c_annotate': lambda value, state: {**value, 'policy_kept': True}}
    if not any(getattr(n, 'name', '') == 'public_filter' for n in nodes):
        ns['public_filter'] = lambda f: {**f, 'type': 'number_decimal' if f['type'] == 'range' else 'string'}
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[])),
                 '<api-functions>', 'exec'), ns)
    return ns


class FakeTypesense:
    """Captures real API requests and returns filtered product documents."""
    def __init__(self):
        self.calls = []
        self.docs = [
            {'id': '123', 'shopify_product_id': 'gid://shopify/Product/123',
             'sku': 'N8270CH', 'sku_aliases': ['n8270ch', 'n8271pg'],
             'title': 'Test plafondbuis', 'handle': 'test-plafondbuis',
             'vendor': 'Lagoo', 'product_type': 'Doucheaccessoires',
             'price_cents': 7800, 'price_varies': True,
             'url': '/products/test-plafondbuis', 'image_url': ''},
            {'id': '456', 'shopify_product_id': 'gid://shopify/Product/456',
             'sku': 'OTHER', 'sku_aliases': ['other'], 'title': 'Ander product',
             'handle': 'ander', 'vendor': 'Test', 'product_type': 'Accessoires',
             'price_cents': 9900, 'price_varies': False,
             'url': '/products/ander', 'image_url': ''}]

    def AsyncClient(self, **kwargs):
        return self

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def post(self, url, headers, json):
        self.calls.append((url, json))
        searches = json['searches']
        main = searches[0]
        documents = self.docs
        for field in ('sku_aliases', 'sku_exact'):
            prefix = field + ':=`'
            if prefix in main['filter_by']:
                query = main['filter_by'].split(prefix, 1)[1].split('`', 1)[0]
                documents = [d for d in documents if query in
                             (d['sku_aliases'] if field == 'sku_aliases'
                              else [d['sku'].casefold()])]
        include = main['include_fields'].split(',')
        data = {'results': [{'found': len(documents),
                            'hits': [{'document': {k: v for k, v in d.items() if k in include}}
                                     for d in documents]}] +
                           [{'facet_counts': [{'field_name': s['facet_by'],
                                               'counts': [], 'stats': {'min': 7800, 'max': 9900}}]}
                            for s in searches[1:]]}
        return SimpleNamespace(status_code=200, json=lambda: data)


class VariantApiPatchTests(unittest.TestCase):
    def setUp(self):
        self.patched = patch_variant_api(SOURCE)

    def test_secondary_sku_uses_alias_filter_and_one_product(self):
        state = snapshot()
        engine = FakeTypesense()
        ns = functions(self.patched, state, engine)
        ns.update(HOST='http://local-typesense', KEY='test-key')
        result = asyncio.run(ns['search'](body(q='  N8271PG  ')))
        request = engine.calls[0][1]['searches'][0]
        self.assertEqual(request['q'], '*')
        self.assertIn('sku_aliases:=`n8271pg`', request['filter_by'])
        self.assertNotIn('general_shopping', request['filter_by'])
        self.assertEqual(result['found'], 1)
        self.assertEqual(len(result['products']), 1)
        product = result['products'][0]
        self.assertEqual(product['id'], '123')
        self.assertEqual(product['product_url'], '/products/test-plafondbuis')
        self.assertEqual(product['sku_aliases'], ['n8270ch', 'n8271pg'])
        self.assertIs(product['price_varies'], True)
        self.assertEqual(product['price_cents'], 7800)
        self.assertTrue(result['exact_sku'])
        self.assertTrue(result['policy_kept'])

    def test_primary_sku_also_uses_alias_filter(self):
        request = functions(self.patched, snapshot())['plan'](body(q='N8270CH'))[2][0]
        self.assertIn('sku_aliases:=`n8270ch`', request['filter_by'])

    def test_text_query_adds_aliases_without_changing_existing_field_order(self):
        for source, expected in [(SOURCE, 'title,sku,vendor,f_productsoort'),
                                 (self.patched, 'title,sku,vendor,f_productsoort,sku_aliases')]:
            searches = functions(source, snapshot())['plan'](body(q='Verlavio'))[2]
            for request in searches:
                self.assertEqual(request['query_by'], expected)
                self.assertNotIn('query_by_weights', request)
                self.assertIn('general_shopping:=true', request['filter_by'])
                self.assertEqual(request['q'], 'Verlavio')

    def test_legacy_snapshots_keep_all_existing_request_values(self):
        cases = [body(q='Verlavio'), body(q='N8270CH'),
                 body(collection='douches', q='kraan', page=3, per_page=12,
                      sort='price_desc', filters={'vendor': ['Lagoo']},
                      ranges={'price_cents': SimpleNamespace(min=0.0, max=21500.0)})]
        for flag in (None, False, 'true'):
            for request in cases:
                with self.subTest(flag=flag, query=request.q):
                    state = snapshot(flag)
                    self.assertEqual(functions(SOURCE, state)['plan'](request),
                                     functions(self.patched, state)['plan'](request))

    def test_legacy_product_response_omits_new_fields(self):
        state = snapshot(None)
        engine = FakeTypesense()
        ns = functions(self.patched, state, engine)
        ns.update(HOST='http://local-typesense', KEY='test-key')
        product = asyncio.run(ns['search'](body(q='N8270CH')))['products'][0]
        self.assertNotIn('sku_aliases', product)
        self.assertNotIn('price_varies', product)

    def test_zero_price_bounds_sort_pagination_and_disjunctive_facets_stay_correct(self):
        request = body(page=4, per_page=9, sort='price_asc',
                       filters={'vendor': ['Lagoo'], 'f_kleur': ['Geborsteld RVS']},
                       ranges={'price_cents': SimpleNamespace(min=0.0, max=21500.0)})
        profile, visible, searches, exact = functions(self.patched, snapshot())['plan'](request)
        main = searches[0]
        self.assertEqual((main['page'], main['per_page'], main['sort_by']), (4, 9, 'price_cents:asc'))
        self.assertIn('price_cents:[0..21500]', main['filter_by'])
        self.assertEqual(len(searches), 3)
        color_facet = next(s for s in searches[1:] if s['facet_by'] == 'f_kleur')
        self.assertNotIn('f_kleur:=', color_facet['filter_by'])
        self.assertIn('vendor:=`Lagoo`', color_facet['filter_by'])
        price_facet = next(s for s in searches[1:] if s['facet_by'] == 'price_cents')
        self.assertNotIn('price_cents:[', price_facet['filter_by'])
        self.assertIn('f_kleur:=`Geborsteld RVS`', price_facet['filter_by'])

    def test_filter_literals_keep_baseline_escaping_for_exact_aliases_and_choices(self):
        malicious = 'ab` \\ || published:=false'
        state = snapshot(); state['exact'].add(malicious)
        old = functions(SOURCE, state)
        new = functions(self.patched, state)
        request = body(q=malicious, filters={'vendor': [malicious]})
        before = old['plan'](request)[2][0]['filter_by']
        after = new['plan'](request)[2][0]['filter_by']
        self.assertEqual(after, before.replace('sku_exact:=', 'sku_aliases:='))
        self.assertIn('\\`', after)
        self.assertIn('\\\\', after)

    def test_invalid_filters_and_sorts_keep_existing_errors(self):
        for request in (body(filters={'unknown': ['x']}), body(sort='invalid')):
            with self.subTest(request=request):
                with self.assertRaises(HttpFailure) as error:
                    functions(self.patched, snapshot())['plan'](request)
                self.assertEqual(error.exception.status_code, 400)

    def test_patch_is_idempotent_and_preserves_every_other_function_and_middleware(self):
        self.assertEqual(patch_variant_api(self.patched), self.patched)
        original_nodes = ast.parse(SOURCE).body
        patched_nodes = ast.parse(self.patched).body
        original_other = [ast.dump(n, include_attributes=False) for n in original_nodes
                          if not isinstance(n, ast.FunctionDef) or n.name != 'plan']
        patched_other = [ast.dump(n, include_attributes=False) for n in patched_nodes
                         if not isinstance(n, ast.FunctionDef) or n.name != 'plan']
        self.assertEqual(original_other, patched_other)
        if UPLOADED.exists():
            for marker in ('BC_B2C_POLICY_V1', 'BC_RVS_COLOR_ALIASES_V1', 'BC_SYNC_GENERATIONS_V1'):
                self.assertIn(marker, self.patched)

    def test_changed_or_partial_api_code_is_refused(self):
        changed = SOURCE.replace("'drop_tokens_threshold': 0", "'drop_tokens_threshold': 1")
        with self.assertRaises(RuntimeError):
            patch_variant_api(changed)
        with self.assertRaises(RuntimeError):
            patch_variant_api(SOURCE + '\n# BC_VARIANT_ALIASES_V1\n')
        with self.assertRaises(RuntimeError):
            patch_variant_api(self.patched.replace("'sku_aliases:='", "'unknown:='"))

    def test_portable_fixture_matches_actual_planner(self):
        original = next(n for n in ast.parse(SOURCE).body
                        if isinstance(n, ast.FunctionDef) and n.name == 'plan')
        fixture = ast.parse(BASELINE_PLAN).body[0]
        self.assertEqual(ast.dump(original, include_attributes=False),
                         ast.dump(fixture, include_attributes=False))
        self.assertEqual(patch_variant_api(BASELINE).count('# BC_VARIANT_ALIASES_V1'), 1)


if __name__ == '__main__':
    unittest.main()
