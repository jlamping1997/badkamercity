import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from enrich_supplier_specifications import candidates
from enrich_retail_specifications import normalized
from prepare_source_review import resolution,build as review


def product(typ='Inbouwdouchesets',text='Set met stopkranen en 20 cm douchekop en staaf handdouche'):
    p={'vendor':'BRAUER','sku':'TEST-A','ean':'1234567890123','product_type':typ,
       'source':{'Merk':'BRAUER','Artikelcode':'TEST-A','EAN':'1234567890123',
                 'Productomschrijving':text,'Productgroep':'','Uitvoering':''},
       'source_refs':[{'file':'supplier.xlsx','sheet':'Data','row':2}],
       'specifications':{},'source_conflicts':{}}
    return p


def mounting():
    p=product('Topbladen','Topblad vrijhangend met beugels')
    p['specifications']['Montage']='Vrijhangend aan de wand'
    e={'ean':p['ean'],'facts':{'Montage':{'kind':'supplier','field':'Productomschrijving',
       'fragment':'vrijhangend','source_refs':copy.deepcopy(p['source_refs']),'url':None}}}
    d={'sku':p['sku'],'field':'Montage','status':'OPEN','existing':'Vrijhangend aan de wand',
       'candidates':[{'value':'ophangen','identity':'SKU_EAN_MERK','ean':p['ean'],
                      'url':'https://www.badkamerxxl.nl/exact'}]}
    return p,e,d


class SourceReviewTests(unittest.TestCase):
    def test_literal_complete_set_component_forms(self):
        for part in ['20 cm douchekop','2-standen cilindervormige douchekop',
                     '2-standen wandmodel douchekop','2-standen inbouw plafond douche']:
            p=product(text='Set met stopkranen en '+part+' en handdouche')
            fields=[f for f in candidates(p) if f['rule']=='explicit_set_component_headshower']
            self.assertEqual(len(fields),1);self.assertEqual(fields[0]['value'],'Ja')
            self.assertIn(fields[0]['fragment'],p['source']['Productomschrijving'])

    def test_no_head_component_from_reference_title_or_other_product(self):
        for text in ['Set geschikt voor 20 cm douchekop','Set zonder hoofddouche en 20 cm douchekop','Set met handdouche']:
            p=product(text=text)
            self.assertNotIn('Hoofddouche inbegrepen',[f['label'] for f in candidates(p)])
        p=product();p['product_type']='Losse glasdelen'
        self.assertNotIn('Hoofddouche inbegrepen',[f['label'] for f in candidates(p)])

    def test_full_supplier_identity_is_required_for_new_rules(self):
        for key,value in [('Merk','OTHER'),('Artikelcode','SIBLING'),('EAN','9999999999999')]:
            p=product();p['source'][key]=value
            self.assertNotIn('Hoofddouche inbegrepen',[f['label'] for f in candidates(p)])
        p=product();p['source_refs']=[]
        self.assertNotIn('Hoofddouche inbegrepen',[f['label'] for f in candidates(p)])

    def test_door_mechanism_uses_literal_group_and_retains_compound_form(self):
        for group,expected in [('Pendeldeuren profielloos','Pendeldeur'),
                              ('Nisdeur 2-delig met schuifdeur met profiel','Schuifdeur'),
                              ('Nisdeur met draai-schuifdeur met profiel','Draai-schuifdeur')]:
            p=product('Nisdeuren','Nisdeur model 100');p['source']['Productgroep']=group
            f=next(f for f in candidates(p) if f['label']=='Deursysteem')
            self.assertEqual((f['value'],f['field'],f['fragment']),(expected,'Productgroep',group))
        p['product_type']='Losse glasdelen'
        self.assertNotIn('Deursysteem',[f['label'] for f in candidates(p)])

    def test_retail_hold_and_prior_negative_are_not_overwritten_by_supplier_extension(self):
        script=Path(__file__).with_name('enrich_supplier_specifications.py').resolve()
        for blocked in [True,False]:
            p=product();p['retail_review']={'open_fields':['Hoofddouche inbegrepen']} if blocked else {'open_fields':[]}
            e={'ean':p['ean'],'facts':{}}
            if not blocked:
                p['specifications']['Hoofddouche inbegrepen']='Nee'
                e['facts']['Hoofddouche inbegrepen']={'kind':'retailer_exact_sku_ean','url':'retained'}
            with tempfile.TemporaryDirectory() as directory:
                root=Path(directory);(root/'prepared').mkdir()
                for name,data in [('catalog.json',[p]),('specification-evidence.json',{p['sku']:e})]:
                    (root/'prepared'/name).write_text(json.dumps(data))
                run=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True)
                self.assertEqual(run.returncode,0,run.stderr)
                got=json.loads((root/'prepared/catalog.json').read_text())[0]
                self.assertEqual(got['specifications'],p['specifications'])

    def test_suspended_mounting_equivalence_is_contextual_and_not_a_location_fact(self):
        a,b='ophangen','Vrijhangend aan de wand'
        self.assertEqual(normalized('Montage',a,product_type='Topbladen'),normalized('Montage',b,product_type='Topbladen'))
        self.assertNotEqual(normalized('Montage',a),normalized('Montage',b))
        self.assertNotEqual(normalized('Montage',a,product_type='Spiegels'),normalized('Montage',b,product_type='Spiegels'))

    def test_supported_resolution_keeps_supplier_value_and_exact_source(self):
        p,e,d=mounting();r=resolution(p,e,d)
        self.assertEqual(r['value'],p['specifications']['Montage'])
        self.assertEqual(r['basis'],'SUPPLIER_AND_EXACT_RETAILER')
        self.assertEqual(r['corroborating_url'],d['candidates'][0]['url'])

    def test_uncorroborated_or_held_mounting_is_not_resolved(self):
        for change in ['wrong_ean','wrong_source','not_literal','held','opposite']:
            p,e,d=mounting()
            if change=='wrong_ean':d['candidates'][0]['ean']='9999999999999'
            if change=='wrong_source':e['facts']['Montage']['kind']='retailer_exact_sku_ean'
            if change=='not_literal':e['facts']['Montage']['fragment']='not in source'
            if change=='held':p['source_conflicts']={'Montage':['a','b']}
            if change=='opposite':d['candidates'][0]['value']='Opbouw'
            self.assertIsNone(resolution(p,e,d),change)

    def test_previous_difference_is_preserved_and_repeat_is_stable(self):
        p,e,d=mounting()
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'prepared').mkdir()
            for name,data in [('catalog.json',[p]),('specification-evidence.json',{p['sku']:e}),
                              ('retail-enrichment-report.json',{'differences':[d]}),('retail-resolutions.json',{})]:
                (root/'prepared'/name).write_text(json.dumps(data))
            result=review(root);self.assertEqual(result['new_supported_mounting_resolutions'],1)
            path=root/'prepared/source-review-history30.json';before=path.read_bytes()
            self.assertEqual(json.loads(before)['changes'][0]['previous_difference'],d)
            result=review(root);self.assertEqual(result['new_supported_mounting_resolutions'],0)
            self.assertEqual(before,path.read_bytes())


if __name__=='__main__':unittest.main(verbosity=2)
