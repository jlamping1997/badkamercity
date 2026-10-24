#!/usr/bin/env python3
import copy
import json
import re
import tempfile
import unittest
from pathlib import Path

from build_rollout_theme import (
    HELD_SKUS, bounded_routing_helpers, build, clean_group, is_spom, pack_assets,
    patch_main, prepare_groups, validate_group,
)


def product(pid, sku, color='Chroom', group=None, status='ACTIVE', published=True, title=None):
    return {
        'id': f'gid://shopify/Product/{pid}', 'handle': f'product-{pid}',
        'title': title or f'Hotbath {sku} {color}', 'status': status,
        'publishedAt': '2026-10-24T00:00:00Z' if published else None,
        'group': {'value': group} if group else None,
        'variants': {'nodes': [{'sku': sku, 'price': '99.00'}], 'pageInfo': {'hasNextPage': False}},
    }


def group(gid, products, colors=None):
    return {
        'id': gid, 'label': gid,
        'menus': [{'key': 'kleur', 'label': 'Kleur', 'order': 1, 'display_type': 'dropdown', 'hide_if_single_value': True, 'values': colors or [p['color'] for p in products]}],
        'products': [{'handle': p['handle'], 'url': '/products/' + p['handle'], 'title': p['title'], 'sort_order': (i+1)*10, 'options': {'kleur': p['color']}} for i, p in enumerate(products)],
    }


def colored(pid, sku, color, **kwargs):
    p = product(pid, sku, color, **kwargs)
    p['color'] = color
    return p


class RolloutThemeTests(unittest.TestCase):
    def test_spom_anywhere_in_sku_title_or_handle_is_excluded_without_mutating_input(self):
        a = colored(1001, 'XXSPOM99CR', 'Chroom')
        b = colored(1002, 'BAA09GN', 'Nikkel', title='Hotbath onderdeel sPoM 99')
        c = colored(1003, 'BAA09BB', 'Messing'); c['handle'] = 'legacy-spom-record'
        d = colored(1004, 'BAA09WH', 'Wit')
        e = colored(1005, 'BAA09AI', 'IJzer')
        catalog = {p['handle']: p for p in [a, b, c, d, e]}
        incoming = group('new', [a,b,c,d,e]); original = copy.deepcopy(incoming)
        groups, details = prepare_groups([incoming], [], catalog)
        self.assertEqual(incoming, original)
        self.assertEqual(len(groups[0]['products']), 2)
        self.assertEqual(set(details['spom_input_records_removed']), {a['handle'],b['handle'],c['handle']})
        self.assertFalse(any(is_spom(catalog[r['handle']]) for r in groups[0]['products']))

    def test_existing_group_is_augmented_only_with_old_records_preserved(self):
        a = colored(1001, 'BAA03CR', 'Chroom', group='existing')
        b = colored(1002, 'BAA03GN', 'Nikkel', group='existing')
        c = colored(1003, 'BAA03BGP', 'Gunmetal')
        catalog = {p['handle']: p for p in [a,b,c]}
        old = group('existing', [a,b]); proposed = group('existing', [a,b,c])
        groups, details = prepare_groups([proposed], [old], catalog)
        self.assertEqual(groups[0]['products'][:2], old['products'])
        self.assertEqual(details['augmented_existing_group_ids'], ['existing'])
        broken = copy.deepcopy(proposed); broken['products'][0]['options']['kleur'] = 'Zwart'
        with self.assertRaisesRegex(ValueError, 'existing record changed'):
            prepare_groups([broken], [old], catalog)

    def test_same_existing_group_emits_no_new_asset_or_routing(self):
        a = colored(1, 'M1CR', 'Chroom', group='existing')
        b = colored(2, 'M1GN', 'Nikkel', group='existing')
        old = group('existing', [a,b])
        groups, details = prepare_groups([copy.deepcopy(old)], [old], {p['handle']:p for p in [a,b]})
        self.assertEqual(groups, [])
        self.assertEqual(details['unchanged_existing_group_ids'], ['existing'])

    def test_only_explicit_archie_colour_additions_can_extend_existing_options(self):
        gid='hotbath-archie-ar105ext-inbouw-wastafelmengkraan-rvs316'
        a=colored(1001,'AR105EXT18IX','RVS 316',group=gid)
        b=colored(1002,'AR105EXT25IX','RVS 316',group=gid)
        c=colored(1003,'AR105EXT18BBP','Geborsteld messing PVD')
        old=group(gid,[a,b]); old['menus']=[{'key':'lengte_uitloop','label':'Lengte uitloop','values':['18 cm','25 cm']}]
        for row,length in zip(old['products'],['18 cm','25 cm']): row['options']={'lengte_uitloop':length}
        proposed=copy.deepcopy(old)
        proposed['menus'].append({'key':'kleur','label':'Kleur','values':['RVS 316','Geborsteld messing PVD']})
        for row in proposed['products']:row['options']['kleur']='RVS 316'
        row=group(gid,[c])['products'][0];row['options']['lengte_uitloop']='18 cm';proposed['products'].append(row)
        sidecar={'additions':[{'group_id':gid,'handle':p['handle'],'sku':p['variants']['nodes'][0]['sku'],'key':'kleur','value':'RVS 316'} for p in [a,b]]}
        catalog={p['handle']:p for p in [a,b,c]}
        result,details=prepare_groups([proposed],[old],catalog,option_additions=sidecar)
        self.assertEqual(len(details['authorized_existing_colour_additions']),2)
        self.assertEqual(result[0],proposed)
        with self.assertRaisesRegex(ValueError,'existing record changed'):
            prepare_groups([proposed],[old],catalog)
        for mutate in [
            lambda g,s:g['products'][0].update(title='changed'),
            lambda g,s:g['products'][0]['options'].update(lengte_uitloop='25 cm'),
            lambda g,s:s['additions'][0].update(value='Geborsteld RVS'),
            lambda g,s:s['additions'][0].update(sku='AR105EXT25IX'),
            lambda g,s:s['additions'][0].update(group_id='not-authorized'),
            lambda g,s:s['additions'].pop(),
        ]:
            g,s=copy.deepcopy(proposed),copy.deepcopy(sidecar);mutate(g,s)
            with self.assertRaises(ValueError):prepare_groups([g],[old],catalog,option_additions=s)
        with self.assertRaisesRegex(ValueError,'Unused'):
            prepare_groups([], [old],catalog,option_additions=sidecar)

    def test_all_five_unresolved_title_sku_conflicts_fail_closed(self):
        a=colored(1001,'OKCR','Chroom')
        for sku in HELD_SKUS:
            b=colored(1002,sku,'Nikkel')
            with self.assertRaisesRegex(ValueError,'on hold'):
                prepare_groups([group('new',[a,b])],[],{p['handle']:p for p in [a,b]})

    def test_spom_cleanup_of_existing_group_retains_real_siblings(self):
        a = colored(1, 'M1CR', 'Chroom', group='existing')
        b = colored(2, 'M1GN', 'Nikkel', group='existing')
        service = colored(3, 'SPOM99WH', 'Wit', group='existing')
        old = group('existing', [a,b,service])
        groups, details = prepare_groups([], [old], {p['handle']:p for p in [a,b,service]})
        self.assertEqual([r['handle'] for r in groups[0]['products']], [a['handle'],b['handle']])
        self.assertEqual(groups[0]['menus'][0]['values'], ['Chroom','Nikkel'])
        self.assertEqual(details['spom_cleaned_existing_group_ids'], ['existing'])

    def test_spom_cleanup_disables_remaining_singleton_instead_of_pointless_menu(self):
        a = colored(1, 'M1CR', 'Chroom', group='existing')
        service = colored(3, 'SPOM99WH', 'Wit', group='existing')
        old = group('existing', [a,service])
        groups, details = prepare_groups([], [old], {p['handle']:p for p in [a,service]})
        self.assertEqual(groups, [])
        self.assertEqual(details['disabled_product_handles'], [a['handle']])

    def test_unpublished_inactive_test_and_conflicting_metadata_cannot_enter_new_group(self):
        a = colored(1, 'M1CR', 'Chroom')
        for kwargs in [{'status':'DRAFT'}, {'published':False}, {'group':'another'}]:
            b = colored(2, 'M1GN', 'Nikkel', **kwargs)
            catalog = {p['handle']:p for p in [a,b]}
            with self.assertRaises(ValueError):
                prepare_groups([group('new',[a,b])], [], catalog)
        b = colored(2, 'TEST-M1GN', 'Nikkel')
        with self.assertRaises(ValueError):
            prepare_groups([group('new',[a,b])], [], {p['handle']:p for p in [a,b]})

    def test_duplicate_tuples_missing_values_and_external_urls_fail_before_build(self):
        a = colored(1, 'M1CR', 'Chroom')
        b = colored(2, 'M1GN', 'Nikkel')
        base = group('new',[a,b]); catalog = {p['handle']:p for p in [a,b]}
        bad = copy.deepcopy(base); bad['products'][1]['options']['kleur'] = 'Chroom'
        with self.assertRaises(ValueError): validate_group(bad,catalog)
        bad = copy.deepcopy(base); bad['products'][1]['options'] = {}
        with self.assertRaises(ValueError): validate_group(bad,catalog)
        bad = copy.deepcopy(base); bad['products'][1]['url'] = 'https://other.example/products/product-2'
        with self.assertRaisesRegex(ValueError,'off-origin'): validate_group(bad,catalog)

    def test_chunks_preserve_whole_groups_and_obey_bytes_and_group_count(self):
        groups=[]
        for i in range(8):
            a=colored(i*2+1,'MCR','Chroom'); b=colored(i*2+2,'MGN','Nikkel')
            groups.append(group('model-'+str(i),[a,b]))
        assets,mapping=pack_assets(groups,1500,2)
        self.assertTrue(all(len(x.encode())<=1500 for x in assets.values()))
        restored=[g for value in assets.values() for g in json.loads(value)['groups']]
        self.assertEqual(restored,groups)
        self.assertTrue(all(len(json.loads(x)['groups'])<=2 for x in assets.values()))
        self.assertEqual(len(mapping),8)
        with self.assertRaisesRegex(ValueError,'exceeds asset byte limit'):
            pack_assets(groups,100,2)

    def test_large_exact_id_index_uses_bounded_parts_without_long_handles(self):
        ids={10_000_000_000_000+i: i%600+1 for i in range(6500)}
        sources={i:f'hotbath-model-{i}-'+('x'*100)+'||bc-hotbath-menu-data-001.json' for i in range(1,601)}
        outputs,stats=bounded_routing_helpers(ids,sources,30_000)
        self.assertTrue(all(len(x.encode())<=30_000 for x in outputs.values()))
        self.assertGreater(stats['bc-hotbath-menu-route']['part_count'],1)
        extracted=[]
        for filename,content in outputs.items():
            if 'menu-route' not in filename or 'case product.id' not in content:continue
            for line in content.splitlines():
                if line.strip().startswith('when '):extracted.extend(int(x.strip()) for x in line.strip()[5:].split(','))
        self.assertEqual(set(extracted),set(ids))
        self.assertEqual(len(extracted),len(ids))
        self.assertNotIn('product.handle',''.join(outputs.values()))

    def test_section_guard_suppresses_v2_legacy_and_native_options_for_spom(self):
        source=(Path(__file__).parent/'source-theme/sections/main-product.liquid').read_text()
        result=patch_main(source)
        self.assertLess(result.index("if bc_hotbath_menu_title contains 'SPOM' or bc_hotbath_menu_handle contains 'SPOM'"),result.index('capture current_switch_group'))
        self.assertIn("if bc_hotbath_menu_excluded\n      assign current_switch_group = ''",result)
        self.assertIn("if bc_hotbath_menu_excluded or bc_hotbath_menu_disabled\n      assign current_group = ''",result)
        self.assertIn('if bc_hotbath_menu_excluded == false and bc_hotbath_menu_disabled == false and current_switch_group == blank',result)
        display=result.index('{{ bc_buybox_options_markup }}')
        self.assertIn('if bc_hotbath_menu_excluded == false and bc_hotbath_menu_disabled == false',result[display-420:display])
        self.assertNotIn("render 'bc-hotbath-preview-group'",result)
        self.assertIn("data_url: bc_switcher_data_url",result)


if __name__=='__main__':unittest.main(verbosity=2)
