import ast
import os
from pathlib import Path
from types import SimpleNamespace
import unittest

from simple_api_patch import patch_simple_api

SOURCE = Path(os.environ.get('BC_FILTER_RUNTIME_DIR', '/not-configured')) / 'app.py'


class HttpError(Exception):
    def __init__(self, status, message):
        self.status_code = status
        super().__init__(message)


class Body(SimpleNamespace):
    def copy(self, update):
        return Body(**{**vars(self), **update})


def body(**kwargs):
    return Body(**{'collection': 'tegels', 'filters': {}, 'ranges': {}, 'q': '*',
                   'sort': 'relevance', 'page': 1, 'per_page': 24,
                   'include_facets': True, **kwargs})


def namespace(source, enabled=True):
    definitions = [{'field': 'f_kleur', 'type': 'choice', 'data_type': 'string'},
                   {'field': 'f_tegel_formaat', 'type': 'choice', 'data_type': 'string'},
                   {'field': 'price_cents', 'type': 'range', 'data_type': 'int64'}]
    profile = {'title': 'Tegels', 'allowed_filters': definitions,
               'filters': definitions[:2], 'service_category': False}
    snapshot = {'profiles': {'tegels': profile}, 'collection': 'stage', 'exact': ['other-sku'],
                'variant_aliases_v1': True, 'filter_simplification_v1': enabled,
                'tile_format_codes_v1': enabled,
                'tile_format_codes': {'60 × 60 cm':1,'60 × 120 cm':2,'60 × 150 cm':3},
                'filter_color_aliases': {'Mat goud': 'Goud', 'Geborsteld goud PVD': 'Goud',
                                        'RVS': 'RVS', 'Geborsteld RVS': 'RVS',
                                        'Geborsteld RVS PVD': 'RVS', 'Copper Green': 'Groen'}}
    selected = [n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                and n.name in {'quote', 'plan', '_bc_simple_request', '_bc_simple_facet_limit', '_bc_simple_choice_clause'}]
    ns = {'_bc_snapshot': lambda: snapshot, 'HTTPException': HttpError}
    exec(compile(ast.Module(body=selected, type_ignores=[]), '<planner-test>', 'exec'), ns)
    return ns, snapshot


@unittest.skipUnless(SOURCE.exists(), 'private uploaded runtime source is not bundled')
class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = SOURCE.read_text()
        cls.patched = patch_simple_api(cls.original)

    def test_patch_is_idempotent(self):
        self.assertEqual(patch_simple_api(self.patched), self.patched)

    def test_unknown_source_is_refused(self):
        with self.assertRaises(RuntimeError):
            patch_simple_api(self.original.replace("'max_facet_values': 100", "'max_facet_values': 101"))

    def test_changed_patch_is_refused(self):
        with self.assertRaises(RuntimeError):
            patch_simple_api(self.patched.replace("len(values) > 100", "len(values) > 101"))

    def test_existing_behavior_is_generation_gated(self):
        old, _ = namespace(self.original)
        new, _ = namespace(self.patched, enabled=False)
        request = body(filters={'f_kleur': ['Mat goud']})
        self.assertEqual(old['plan'](request), new['plan'](request))

    def test_gold_aliases_become_one_group(self):
        ns, _ = namespace(self.patched)
        request = body(filters={'f_kleur': ['Mat goud', 'Geborsteld goud PVD', 'Goud']})
        result = ns['plan'](request)
        self.assertIn('f_kleur:=`Goud`', result[2][0]['filter_by'])
        self.assertEqual(request.filters['f_kleur'], ['Mat goud', 'Geborsteld goud PVD', 'Goud'])

    def test_or_colors_and_tile_pair_are_combined_with_and(self):
        ns, _ = namespace(self.patched)
        query = ns['plan'](body(filters={'f_kleur': ['Mat goud', 'Groen'],
                                        'f_tegel_formaat': ['60 × 60 cm']}))[2][0]
        self.assertIn('f_kleur:=[`Goud`,`Groen`]', query['filter_by'])
        self.assertIn(' && f_tegel_formaat_code:=1', query['filter_by'])

    def test_exact_variant_lookup_and_price_sort_are_preserved(self):
        ns, _ = namespace(self.patched)
        result = ns['plan'](body(q='other-sku', sort='price_asc'))
        self.assertTrue(result[3])
        self.assertIn('sku_aliases:=`other-sku`', result[2][0]['filter_by'])
        self.assertEqual(result[2][0]['sort_by'], 'price_cents:asc')
        self.assertIn('price_varies', result[2][0]['include_fields'])

    def test_disjunctive_facet_excludes_own_selection(self):
        ns, _ = namespace(self.patched)
        result = ns['plan'](body(filters={'f_kleur': ['Mat goud'], 'f_tegel_formaat': ['60 × 60 cm']}))
        color_facet = next(q for q in result[2][1:] if q['facet_by'] == 'f_kleur')
        self.assertNotIn('f_kleur:=', color_facet['filter_by'])
        self.assertIn('f_tegel_formaat_code:=1', color_facet['filter_by'])
        format_facet = next(q for q in result[2][1:] if q['facet_by'] == 'f_tegel_formaat')
        self.assertNotIn('f_tegel_formaat_code:', format_facet['filter_by'])
        self.assertIn('f_kleur:=`Goud`', format_facet['filter_by'])

    def test_three_similar_formats_use_distinct_numeric_equality(self):
        ns, _ = namespace(self.patched)
        for label, code in [('60 × 60 cm',1),('60 × 120 cm',2),('60 × 150 cm',3)]:
            query = ns['plan'](body(filters={'f_tegel_formaat':[label]}))[2][0]['filter_by']
            self.assertIn('f_tegel_formaat_code:='+str(code),query)
            self.assertNotIn('f_tegel_formaat:=',query)
            self.assertNotIn(label,query)

    def test_format_or_uses_numeric_exact_union(self):
        ns, _ = namespace(self.patched)
        query = ns['plan'](body(filters={'f_tegel_formaat':['60 × 60 cm','60 × 120 cm']}))[2][0]['filter_by']
        self.assertIn('f_tegel_formaat_code:[1,2]',query)
        self.assertNotIn('3',query)

    def test_unknown_format_is_an_impossible_reserved_code(self):
        ns, _ = namespace(self.patched)
        query = ns['plan'](body(filters={'f_tegel_formaat':['not a format']}))[2][0]['filter_by']
        self.assertIn('f_tegel_formaat_code:=0',query)

    def test_code_map_is_generation_local(self):
        ns, snapshot = namespace(self.patched)
        request = body(filters={'f_tegel_formaat':['60 × 60 cm']})
        self.assertIn('f_tegel_formaat_code:=1',ns['plan'](request)[2][0]['filter_by'])
        snapshot['tile_format_codes']['60 × 60 cm']=40
        self.assertIn('f_tegel_formaat_code:=40',ns['plan'](request)[2][0]['filter_by'])
        self.assertEqual(request.filters['f_tegel_formaat'],['60 × 60 cm'])

    def test_missing_or_corrupt_format_map_is_rejected(self):
        for mapping in [None, {'60 × 60 cm': True}, {'a':1,'b':1}, {'x':0}, {'x':2147483648}]:
            ns,snapshot=namespace(self.patched)
            snapshot['tile_format_codes']=mapping
            with self.assertRaises(RuntimeError):ns['plan'](body(filters={'f_tegel_formaat':['60 × 60 cm']}))
        ns,snapshot=namespace(self.patched)
        snapshot['tile_format_codes_v1']=False
        with self.assertRaises(RuntimeError):ns['plan'](body(filters={'f_tegel_formaat':['60 × 60 cm']}))

    def test_private_code_field_is_not_publicly_allowlisted(self):
        ns,_=namespace(self.patched)
        with self.assertRaises(HttpError) as e:ns['plan'](body(filters={'f_tegel_formaat_code':['1']}))
        self.assertEqual(e.exception.status_code,400)

    def test_complete_tile_format_facets_use_larger_bounded_limit(self):
        ns, _ = namespace(self.patched)
        result = ns['plan'](body())
        limits = {q['facet_by']: q['max_facet_values'] for q in result[2][1:]}
        self.assertEqual(limits['f_tegel_formaat'], 500)
        self.assertEqual(limits['f_kleur'], 100)
        self.assertEqual(ns['_bc_simple_facet_limit']({'field':'f_serie','distinct_values':1500}), 1000)
        self.assertEqual(ns['_bc_simple_facet_limit']({'field':'f_serie','distinct_values':230}), 230)
        self.assertEqual(ns['_bc_simple_facet_limit']({'field':'f_materiaal','distinct_values':140}), 140)
        self.assertEqual(ns['_bc_simple_facet_limit']({'field':'price_cents','type':'range','distinct_values':15000}), 100)

    def test_old_rvs_links_use_simplified_rvs(self):
        ns, _ = namespace(self.patched)
        for value in ['RVS', 'Geborsteld RVS', 'Geborsteld RVS PVD']:
            self.assertIn('f_kleur:=`RVS`', ns['plan'](body(filters={'f_kleur': [value]}))[2][0]['filter_by'])

    def test_invalid_values_and_unknown_fields_stay_rejected(self):
        ns, _ = namespace(self.patched)
        for filters in [{'f_kleur': [True]}, {'bad_field': ['Goud']}, {'f_kleur': ['Goud'] * 101}]:
            with self.assertRaises(HttpError) as e:
                ns['plan'](body(filters=filters))
            self.assertEqual(e.exception.status_code, 400)

    def test_opaque_legacy_name_does_not_silently_match_all_other_colors(self):
        ns, _ = namespace(self.patched)
        self.assertIn('f_kleur:=`Unknown label`', ns['plan'](body(filters={'f_kleur': ['Unknown label']}))[2][0]['filter_by'])

    def test_mutating_legacy_api_after_patch_stops_next_sync(self):
        with self.assertRaises(RuntimeError):
            patch_simple_api(self.patched.replace("'price_cents:asc'", "'price_cents:desc'"))


if __name__ == '__main__':
    unittest.main()
