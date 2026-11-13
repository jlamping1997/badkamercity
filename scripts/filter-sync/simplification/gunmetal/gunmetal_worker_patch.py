"""Keep Gunmetal distinct in the derived filter index; preserve source data."""
import ast
import hashlib

BASE_WORKER_SHA256 = '79f676d035fdd6d250e2daec51b886d1aa54c117707718d7ea9695300c21c43d'
MARKER = '# BC_GUNMETAL_COLOR_V1'

COLOR_PATCH = r'''
_bc_gunmetal_original_classify = classify_color
_bc_gunmetal_pattern = re.compile(r'(?:^|[^a-z])gun[\s_-]*metal(?=$|[^a-z])', re.I)
if 'Gunmetal' in TAXONOMY:
    raise RuntimeError('Gunmetal staat al in de bronwoordenlijst; eerst opnieuw vergelijken')
_bc_gunmetal_gray_index = TAXONOMY.index('Grijs')
TAXONOMY = TAXONOMY[:_bc_gunmetal_gray_index] + ('Gunmetal',) + TAXONOMY[_bc_gunmetal_gray_index:]

def classify_color(raw, context=None):
    value = normalize(raw)
    if not _bc_gunmetal_pattern.search(value):
        return _bc_gunmetal_original_classify(raw, context)
    if '/' in value or '+' in value:
        parts = [classify_color(part, context) for part in re.split(r'[/+]', value)]
        colors = list(dict.fromkeys(color for part in parts for color in part['colors']))
        return _result(raw, colors, 'OWNER_CONFIRMED', 'Gunmetal is a separate filter color; separate components retained.')
    return _result(raw, ['Gunmetal'], 'OWNER_CONFIRMED', 'Gunmetal is a separate filter color; exact manufacturer finish retained.')
'''

HELPERS = '''
# BC_GUNMETAL_COLOR_V1
exec(compile(__BC_COLOR_PATCH__, '<gunmetal-color-rule>', 'exec'), _BC_SIMPLE_COLORS)
_BC_GUNMETAL_ALIASES = dict.fromkeys(('Gunmetal', 'Gun metal', 'gunmetal', 'gun metal', 'Gun-metal'), 'Gunmetal')

def _bc_gunmetal_has_source(doc):
    raw = doc.get('f_kleur_exact')
    return isinstance(raw, str) and bool(_BC_SIMPLE_COLORS['_bc_gunmetal_pattern'].search(raw))

def _bc_gunmetal_documents_ok(docs):
    return all(('Gunmetal' in _bc_simple_strings(doc.get('f_kleur'))) == _bc_gunmetal_has_source(doc) for doc in docs)

_bc_gunmetal_original_aliases = _bc_simple_aliases
def _bc_simple_aliases(docs):
    result = _bc_gunmetal_original_aliases(docs)
    result.update(_BC_GUNMETAL_ALIASES)
    return result

_bc_gunmetal_original_profiles = make_profiles
def make_profiles(docs, categories, old_profiles, definitions):
    profiles = _bc_gunmetal_original_profiles(docs, categories, old_profiles, definitions)
    for profile in profiles.values():
        aliases = profile.get('b2c_policy', {}).get('color_value_aliases')
        if isinstance(aliases, dict):
            aliases.update(_BC_GUNMETAL_ALIASES)
    return profiles

_bc_gunmetal_original_snapshot = _bc_simple_snapshot
def _bc_simple_snapshot(snapshot, docs):
    _bc_gunmetal_original_snapshot(snapshot, docs)
    if not _bc_gunmetal_documents_ok(docs):
        raise RuntimeError('Gunmetal-selectie komt niet exact overeen met de bronkleuren')
    source = [doc for doc in docs if doc.get('general_shopping') and _bc_gunmetal_has_source(doc)]
    counts = collections.Counter(handle for doc in source for handle in set(doc.get('collection_handles', [])))
    counts['__all__'] = len({doc['id'] for doc in source})
    snapshot['gunmetal_v1'] = True
    snapshot['gunmetal_products'] = counts['__all__']
    snapshot['gunmetal_scope_counts'] = dict(counts)

_bc_gunmetal_original_checks = check_b2c_profiles
def check_b2c_profiles(docs, snapshot):
    checks = _bc_gunmetal_original_checks(docs, snapshot)
    checks.append({'name': 'Gunmetal is exact gescheiden van Grijs; bronkleuren behouden',
                   'passed': snapshot.get('gunmetal_v1') is True and _bc_gunmetal_documents_ok(docs)})
    return checks

_bc_gunmetal_original_cases = make_cases
def make_cases(docs, snapshot):
    cases, facets = _bc_gunmetal_original_cases(docs, snapshot)
    for handle in ('__all__', 'badgrepen', 'wastafelkranen'):
        if handle != '__all__' and handle not in snapshot['profiles']:
            continue
        scope = [doc for doc in docs if doc.get('general_shopping') and (handle == '__all__' or handle in doc['collection_handles'])]
        for values in (['Gunmetal'], ['Grijs'], ['Gunmetal', 'Grijs']):
            expected = [doc['id'] for doc in scope if any(value in _bc_simple_strings(doc.get('f_kleur')) for value in values)]
            if values == ['Gunmetal']:
                expected = [doc['id'] for doc in scope if _bc_gunmetal_has_source(doc)]
            cases.append({'name': 'Gunmetal/Grijs exacte productset: '+handle+'/'+','.join(values),
                          'body': {'collection':handle,'include_facets':False,'filters':{'f_kleur':values}},
                          'status':200, 'expected_ids':expected})
    return cases, facets

'''

RANK_SORT_HOOK = "    _bc_recommendation_schema_default(schema)\n"
RECOMMENDATION_HELPERS = r'''
# BC_RECOMMENDATIONS_V1
import hashlib as _bc_recommendation_hashlib
_BC_RECOMMENDATION_FIELD = 'bc_recommendation_rank'

def _bc_recommendation_tie(value):
    return _bc_recommendation_hashlib.sha256(str(value).encode()).hexdigest()

def _bc_recommendation_score(doc):
    fields = sum(value is not None and value != '' and value != [] and value != {} for key,value in doc.items() if key.startswith('f_'))
    return min(fields, 20) + 2*bool(doc.get('sku_exact') or doc.get('sku'))

def _bc_recommendation_group(doc):
    values = (doc.get('vendor'), doc.get('f_productsoort') or doc.get('product_type'),
              '|'.join(sorted(_bc_simple_strings(doc.get('f_serie')))))
    return tuple(str(value or '').strip().casefold() for value in values)

def _bc_rank_recommendations(docs):
    if len({doc['id'] for doc in docs}) != len(docs) or len(docs) >= 2147483647:
        raise RuntimeError('Aanbevolen volgorde vereist unieke producten binnen int32-bereik')
    order = []
    # A known image URL is a completeness signal, not a claim that its content was reviewed.
    for has_image in (True, False):
        groups = collections.defaultdict(list)
        for doc in docs:
            if bool(doc.get('image_url')) == has_image:
                groups[_bc_recommendation_group(doc)].append(doc)
        queues = {}
        for key,items in groups.items():
            items.sort(key=lambda doc:(-_bc_recommendation_score(doc),_bc_recommendation_tie(doc['id'])))
            queues[key] = collections.deque(items)
        while queues:
            keys = sorted(queues, key=lambda key:(-_bc_recommendation_score(queues[key][0]),_bc_recommendation_tie(key)))
            for key in keys:
                order.append(queues[key].popleft())
                if not queues[key]:del queues[key]
    for position,doc in enumerate(order):
        doc[_BC_RECOMMENDATION_FIELD] = len(docs)-position
    return order

_bc_recommendation_original_schema = _bc_simple_schema
def _bc_simple_schema(schema):
    result = _bc_recommendation_original_schema(schema)
    if any(field['name'] == _BC_RECOMMENDATION_FIELD for field in result['fields']):
        raise RuntimeError('Aanbevolen sorteerveld bestaat al; eerst vergelijken')
    result['fields'].append({'name':_BC_RECOMMENDATION_FIELD,'type':'int32','facet':False})
    return result

def _bc_recommendation_schema_default(schema):
    schema['default_sorting_field'] = _BC_RECOMMENDATION_FIELD

_bc_recommendation_original_enrich = enrich_b2c_documents
def enrich_b2c_documents(docs, definitions, schema):
    stats = _bc_recommendation_original_enrich(docs, definitions, schema)
    _bc_rank_recommendations(docs)
    return stats

_bc_recommendation_original_snapshot = _bc_simple_snapshot
def _bc_simple_snapshot(snapshot, docs):
    _bc_recommendation_original_snapshot(snapshot, docs)
    ranks = [doc.get(_BC_RECOMMENDATION_FIELD) for doc in docs]
    if set(ranks) != set(range(1,len(docs)+1)) or any(type(rank) is not int for rank in ranks):
        raise RuntimeError('Aanbevolen volgorde mist unieke stabiele rangen')
    ordered = sorted(docs,key=lambda doc:-doc[_BC_RECOMMENDATION_FIELD])
    scopes = ('__all__','badkamerspiegels','wastafelkranen','tegels')
    snapshot['recommendations_v1'] = True
    snapshot['recommendation_method'] = 'image-then-data-completeness-with-vendor-type-series-round-robin-v1'
    snapshot['recommendation_preview'] = {handle:[doc['id'] for doc in ordered if doc.get('general_shopping') and
        (handle=='__all__' or handle in doc.get('collection_handles',[]))][:48] for handle in scopes}
    targets = {'38.4177':600,'38.4178':800}
    mirrors = [doc for doc in docs if doc.get('vendor')=='Wiesbaden' and
               str(doc.get('sku_exact') or doc.get('sku')) in targets]
    snapshot['cinto_widths_v1'] = (len(mirrors)==2 and len({doc.get('sku_exact') or doc.get('sku') for doc in mirrors})==2 and
        all(doc.get('f_breedte_mm')==targets[str(doc.get('sku_exact') or doc.get('sku'))] and
            doc.get('f_diameter_mm')==doc.get('f_breedte_mm') for doc in mirrors))

'''


def insertion():
    return HELPERS.replace('__BC_COLOR_PATCH__', repr(COLOR_PATCH)) + RECOMMENDATION_HELPERS


def original_source(source):
    patch = insertion()
    if source.count(MARKER) != 1 or source.count(patch) != 1:
        raise RuntimeError('Bestaande Gunmetal-patch wijkt af; niets overschreven')
    result = source.replace(patch, '', 1)
    if result.count(RANK_SORT_HOOK) != 1:
        raise RuntimeError('Aanbevolen schemahook is gewijzigd')
    result = result.replace(RANK_SORT_HOOK, '', 1)
    if hashlib.sha256(result.encode()).hexdigest() != BASE_WORKER_SHA256:
        raise RuntimeError('Andere serverwijziging gevonden naast Gunmetal; eerst vergelijken')
    return result


def patch_worker(source):
    if MARKER in source:
        original_source(source)
        return source
    if hashlib.sha256(source.encode()).hexdigest() != BASE_WORKER_SHA256:
        raise RuntimeError('Serverworker is gewijzigd; niets overschreven')
    tree = ast.parse(source)
    prepare = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name=='prepare']
    loops = [node for node in (prepare[0].body if len(prepare)==1 else []) if isinstance(node, ast.For) and
             isinstance(node.iter, (ast.Tuple,ast.List)) and any(isinstance(item,ast.Constant) and item.value=='default_sorting_field' for item in node.iter.elts)]
    if len(loops)!=1 or loops[0].col_offset!=4:
        raise RuntimeError('Geen unieke gecontroleerde schema-opruiming gevonden')
    hook_offset = sum(len(line) for line in source.splitlines(keepends=True)[:loops[0].end_lineno])
    source = source[:hook_offset]+RANK_SORT_HOOK+source[hook_offset:]
    tree = ast.parse(source)
    guards = [node for node in tree.body if isinstance(node, ast.If) and '__name__' in ast.unparse(node.test)]
    if len(guards) != 1:
        raise RuntimeError('Geen unieke workerstart gevonden')
    offset = sum(len(line) for line in source.splitlines(keepends=True)[:guards[0].lineno-1])
    result = source[:offset] + insertion() + source[offset:]
    compile(result, '<gunmetal-worker>', 'exec')
    return result
