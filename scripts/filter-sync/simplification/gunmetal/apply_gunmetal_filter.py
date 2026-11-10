#!/usr/bin/env python3
"""Extend the pinned existing staging/activation/rollback lifecycle for Gunmetal.

Only the derived worker changes. The API, Shopify data and eight existing filter
layers stay intact. The release builder embeds the reviewed public dependencies;
no private runtime or catalog is distributed. A target hash is calculated from
the exactly allowlisted input and deterministic insertion before taking the lock.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import types

LIFECYCLE_SOURCE = None
PATCH_SOURCE = None
BASE_API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'


def dependencies():
    here = Path(__file__).resolve().parent
    lifecycle_source = LIFECYCLE_SOURCE
    patch_source = PATCH_SOURCE
    if lifecycle_source is None:
        lifecycle_source = (here.parent / 'tile-looks/release/apply_tile_look_filter.py').read_text()
    if patch_source is None:
        patch_source = (here / 'gunmetal_worker_patch.py').read_text()
    lifecycle = types.ModuleType('bc_gunmetal_existing_lifecycle')
    lifecycle.__file__ = str(here / 'embedded_lifecycle.py')
    sys.modules[lifecycle.__name__] = lifecycle
    exec(compile(lifecycle_source, '<existing-filter-lifecycle>', 'exec'), lifecycle.__dict__)
    patch = types.ModuleType('bc_gunmetal_reviewed_patch')
    exec(compile(patch_source, '<reviewed-gunmetal-patch>', 'exec'), patch.__dict__)
    return lifecycle, patch


def configure(lifecycle, patch, original):
    text = original.decode('utf-8')
    candidate = patch.patch_worker(text).encode('utf-8')
    lifecycle.BASE_WORKER_SHA256 = patch.BASE_WORKER_SHA256
    lifecycle.TARGET_WORKER_SHA256 = hashlib.sha256(candidate).hexdigest()
    lifecycle.BASE_API_SHA256 = BASE_API_SHA256
    lifecycle.TARGET_API_SHA256 = BASE_API_SHA256
    lifecycle.PRIOR_FLAGS = tuple(dict.fromkeys((*lifecycle.PRIOR_FLAGS, 'tile_looks_v1')))
    lifecycle.REQUIRED_FLAGS = (*lifecycle.PRIOR_FLAGS, 'gunmetal_v1', 'recommendations_v1', 'cinto_widths_v1')
    lifecycle.PATCH_SOURCES = {'worker':'reviewed deterministic Gunmetal insertion'}
    lifecycle.compose_worker = lambda source, sources: patch.patch_worker(source.decode('utf-8')).encode('utf-8')
    old_validate = lifecycle.validate_look_snapshot

    def validate(snapshot):
        old_validate(snapshot)
        previews=snapshot.get('recommendation_preview')
        if (snapshot.get('recommendations_v1') is not True or snapshot.get('cinto_widths_v1') is not True or
                not isinstance(previews,dict) or '__all__' not in previews or
                any(not isinstance(values,list) or len(values)!=len(set(values)) for values in previews.values())):
            raise RuntimeError('Aanbevolen volgorde of Cinto-breedtes niet bevestigd in de nieuwe index')
        total = snapshot.get('gunmetal_products')
        counts = snapshot.get('gunmetal_scope_counts')
        aliases = snapshot.get('filter_color_aliases', {})
        if (snapshot.get('gunmetal_v1') is not True or type(total) is not int or total <= 0 or
                not isinstance(counts, dict) or counts.get('__all__') != total or
                any(type(value) is not int or value < 0 or value > total for value in counts.values()) or
                snapshot.get('simple_color_counts', {}).get('Gunmetal') != total or
                aliases.get('Gunmetal') != 'Gunmetal' or aliases.get('Grijs') != 'Grijs'):
            raise RuntimeError('Gunmetal-index mist de exacte kleurtoewijzing, aantallen of aliases')
        for raw, value in aliases.items():
            # Mixed source colors retain the original primary-color semantics.
            if '/' not in raw and '+' not in raw:
                import re
                if re.search(r'(?:^|[^a-z])gun[\s_-]*metal(?=$|[^a-z])', raw, re.I) and value != 'Gunmetal':
                    raise RuntimeError('Een Gunmetal-alias wijst nog naar een andere basiskleur')
        return True

    lifecycle.validate_look_snapshot = validate
    old_routes = lifecycle.verify_live_look_routes

    def routes(worker, snapshot):
        checks = old_routes(worker, snapshot)
        for base,label in [('http://127.0.0.1:8082','Lokale'),('https://vps-7ffd625d.vps.ovh.net/verified','Publieke')]:
            for handle in ('__all__','badgrepen','wastafelkranen'):
                if handle != '__all__' and handle not in snapshot['profiles']:
                    continue
                expected = snapshot['gunmetal_scope_counts'].get(handle,0)
                for value in ('Gunmetal','Gun metal','Geborsteld gunmetal PVD'):
                    # Exact finish aliases are checked only if that finish is present.
                    if value == 'Geborsteld gunmetal PVD' and snapshot['filter_color_aliases'].get(value) != 'Gunmetal':
                        continue
                    data,_ = worker.probe(base+'/api/v1/search',{'collection':handle,'per_page':1,'include_facets':False,'filters':{'f_kleur':[value]}})
                    checks.append({'name':label+' Gunmetal-keuze: '+handle+'/'+value,
                        'passed':data.get('found')==expected and (data.get('collection') or {}).get('handle')==handle,
                        'expected_count':expected,'actual_count':data.get('found')})
            data,_ = worker.probe(base+'/api/v1/search',{'collection':'__all__','per_page':1,'include_facets':False,'filters':{'f_kleur':['Grijs']}})
            expected=snapshot['simple_color_counts'].get('Grijs',0)
            checks.append({'name':label+' Grijs blijft afzonderlijk selecteerbaar','passed':data.get('found')==expected,'expected_count':expected,'actual_count':data.get('found')})
            for handle,expected_ids in snapshot['recommendation_preview'].items():
                if not expected_ids:continue
                for page in (1,2):
                    wanted=expected_ids[(page-1)*24:page*24]
                    if not wanted:continue
                    data,_=worker.probe(base+'/api/v1/search',{'collection':handle,'q':'*','sort':'relevance','per_page':24,'page':page,'include_facets':False})
                    actual=[str(product.get('id')) for product in data.get('products',[])]
                    checks.append({'name':label+' stabiele aanbevolen volgorde '+handle+'/pagina '+str(page),'passed':actual==list(map(str,wanted))})
            for sku,width in [('38.4177',600),('38.4178',800)]:
                for selected_width in (30,width):
                    data,_=worker.probe(base+'/api/v1/search',{'collection':'badkamerspiegels','q':sku,'per_page':10,'include_facets':False,'ranges':{'f_breedte_mm':{'min':selected_width,'max':selected_width}}})
                    expected=0 if selected_width==30 else 1
                    checks.append({'name':label+' Cinto-breedte '+sku+'/'+str(selected_width)+'mm','passed':data.get('found')==expected and (not expected or all(product.get('sku')==sku for product in data.get('products',[])))})
        return checks

    lifecycle.verify_live_look_routes = routes
    return candidate


def main():
    lifecycle,patch=dependencies()
    original=lifecycle.read_regular(lifecycle.ROOT/'sync.py')
    configure(lifecycle,patch,original)
    result=lifecycle.repair()
    snapshot=json.loads(lifecycle.read_regular(lifecycle.LIVE/'bc_sync/active.json'))
    lifecycle.validate_look_snapshot(snapshot)
    if result['status'].startswith('already_applied'):
        worker=lifecycle.load_worker(original)
        checks=lifecycle.verify_live_look_routes(worker,snapshot)
        if not all(check['passed'] for check in checks):
            raise RuntimeError('Gunmetal was geinstalleerd maar publieke nacontrole is niet geslaagd')
    result.update(gunmetal_v1=True,gunmetal_products=snapshot['gunmetal_products'],recommendations_v1=True,cinto_widths_v1=True)
    if result.get('backup'):
        lifecycle.write_atomic(Path(result['backup'])/'REPAIR_RESULT.json',json.dumps(result,indent=2).encode())
    lifecycle.say('GUNMETAL GECONTROLEERD | '+str(snapshot['gunmetal_products'])+' producten | Grijs blijft apart')
    lifecycle.say('AANBEVOLEN VOLGORDE EN CINTO-BREEDTES GECONTROLEERD')
    lifecycle.say(json.dumps(result,sort_keys=True))
    return result


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('GUNMETAL NIET VOLTOOID | '+str(error),flush=True)
        raise SystemExit(1)
