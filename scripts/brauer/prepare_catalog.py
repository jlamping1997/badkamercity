"""Prepare BRAUER catalog proposals from a read-only audit, never write Shopify.

All outputs contain supplier rows and must remain private. Source groups are
mapped explicitly; unresolved technical properties never become assertions.
"""
import argparse
import json
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


def gross_price(net):
    """Dutch preparation basis: 21% VAT, commercial half-up cent rounding."""
    return str((Decimal(str(net)) * Decimal('1.21')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def classify(group):
    direct = {
        'Accessoiresets':'Accessoiresets','Afvoer':'Douchebaksifons',
        'Afvoerpluggen':'Afvoerpluggen','Klikwastes':'Afvoerpluggen',
        'Afvoerroosters':'Afvoerroosters','Afvoerroosters douchegoten':'Afvoerroosters',
        'Afwerking':'Meubelonderdelen','Bevestiging bodemplaten':'Meubelonderdelen',
        'Bevestiging planchet':'Meubelonderdelen','Bijkasten':'Bijkasten',
        'Binnenlades':'Binnenlades','Bodemplaten voor onderkasten':'Bodemplaten',
        'Deurfronten':'Deurfronten','Ladefronten':'Ladefronten','Douchebakken':'Douchebakken',
        'Douchegoten':'Douchegoten','Douchepanelen':'Douchepanelen','Doucherekken':'Doucherekken',
        'Elektra':'Meubelonderdelen','Fonteinbakken opbouw':'Fonteinen',
        'Fonteinbakken vrijhangend':'Fonteinen','Glascoating':'Onderhoudsmiddelen',
        'Handdoekbeugels':'Handdoekrekken','Handdoekrekken':'Handdoekrekken',
        'Handdoekbeugels met planchet':'Handdoekrekken met planchet',
        'Planchetten,Handdoekrekken':'Handdoekrekken met planchet',
        'Handdoekhaken':'Handdoekhaken','Handdoekhouders':'Handdoekhouders',
        'Handdoekradiator':'Handdoekradiatoren','Handdouches en houders':'Handdouches en houders',
        'Hoekstopkranen':'Hoekstopkranen','Hoofddouches':'Hoofddouches',
        'Inbouw badkranen':'Inbouwbadkranen','Inbouw fonteinkranen':'Inbouwfonteinkranen',
        'Inbouw nissen':'Inbouwnissen','Inbouwnissen':'Inbouwnissen',
        'Inbouw wastafelkranen':'Inbouwwastafelkranen',
        'Lichtlijsten voor spiegelkasten':'Lichtlijsten voor spiegelkasten',
        'Los beslag':'Glasbeslag','Beslagpakket':'Glasbeslagpakketten',
        'Losse thermostaatkranen':'Losse inbouwthermostaten',
        'Meubelgrepen':'Meubelgrepen','Meubeltopbladen en vrijhangend':'Topbladen',
        'Montage':'Toiletonderdelen','Opbouw badkranen':'Opbouwbadkranen',
        'Opbouw douchekranen':'Opbouwdouchekranen','Opbouw fonteinkranen':'Opbouwfonteinkranen',
        'Opbouw nissen':'Opbouwnissen','Opbouwnissen':'Opbouwnissen',
        'Opbouw verlichting':'Opbouwverlichting','Opbouw wastafelkranen':'Opbouwwastafelkranen',
        'Overloopringen':'Overloopringen','Pedaalemmers':'Prullenbakken','Prullenbakken':'Prullenbakken',
        'Plafond- en muurarmen':'Douchearmen','Planchethouders':'Meubelonderdelen',
        'Planchetten':'Planchetten','Planchetten voor meubels':'Meubelonderdelen',
        'Raamtrekkers':'Douchewissers','Scharnieren':'Meubelonderdelen',
        'Schoonmaakdoeken':'Onderhoudsmiddelen','Sifonnen':'Sifons','Slangen':'Doucheslangen',
        'Spiegeldeuren':'Spiegeldeuren','Spiegeldeurgrepen':'Spiegeldeurgrepen',
        'Spiegelverwarming':'Spiegelverwarming','Toilet bedieningsplaten':'Bedieningsplaten',
        'Toiletborstels':'Toiletborstels','Toiletrolhouders':'Toiletrolhouders',
        'Toiletten hangend':'Hangtoiletten','Topbladbeugels':'Topbladbeugels',
        'Topbladen vrijhangend':'Topbladen','Uitlopen en vullers':'Uitlopen',
        'Verlichting':'Meubelonderdelen','Vrijstaande badkranen':'Vrijstaande badkranen',
        'WC-brillen':'Toiletzittingen','Waskommen opbouw':'Waskommen',
        'Wastafels opbouw':'Meubelwastafels','Wastafels opbouw en vrijhangend':'Meubelwastafels',
        'Wastafels vrijhangend':'Vrijhangende wastafels','Zeepdispensers':'Zeepdispensers',
        'Deur':'Setgebonden glasdelen','Deur 2-delig':'Setgebonden glasdelen',
        'Zijwand':'Setgebonden glasdelen','Draaibare zijwand':'Losse glasdelen',
    }
    if group in direct:
        return direct[group]
    # Prefixes are applied only to the recorded supplier groups, never titles.
    for prefix, category in [
        ('Onderkasten ', 'Onderkasten'),('Fonteinkasten ', 'Fonteinkasten'),
        ('Hoge kasten ', 'Hoge kasten'),('Spiegelkasten ', 'Spiegelkasten'),
        ('Spiegels ', 'Spiegels'),('Inbouw douchekranen', 'Inbouwdouchesets'),
        ('Inloopdouche ', 'Inloopdouches'),('Nisdeur ', 'Nisdeuren'),
        ('Pendeldeuren ', 'Nisdeuren'),('Douchecabine ', 'Douchecabines'),
    ]:
        if group.startswith(prefix):
            return category
    if group in ('Badwand met profiel', 'Badwand profielloos'):
        return 'Badwanden'
    if group.startswith(('Badwand zonder ', 'Badwand met enkelzijdige ',
                         'Deur voor ', 'Wand met ', 'Wand zonder ')):
        return 'Losse glasdelen'
    return None


def prepare(audit_dir, output_dir):
    observations = json.loads((audit_dir / 'source-observations.json').read_text())
    master = json.loads((audit_dir / 'master.json').read_text())
    by_sku = defaultdict(list)
    for record in observations:
        by_sku[record['fields']['Artikelcode']].append(record)
    proposals, group_mapping, exceptions = [], {}, []
    for product in master:
        sku = product['sku']; source = by_sku[sku]; candidates = set(); corrections = []
        for row in source:
            fields = row['fields']; group = fields['Productgroep']; category = classify(group)
            if not group and fields['Productcategorie'] == 'Topbladbeugels':
                category = 'Topbladbeugels'; corrections.append('Empty group; explicit product category Topbladbeugels')
            if group == 'Spiegeldeuren' and fields['Productomschrijving'].startswith('Lichtlijst '):
                category = 'Lichtlijsten voor spiegelkasten'
                corrections.append('Title Light list vs supplier group Mirror doors; classification correction proposal')
            if not category:
                exceptions.append({'sku':sku,'reason':'Unmapped supplier group','group':group})
            else:
                candidates.add(category)
            group_mapping.setdefault(group or '[LEEG]', set()).add(category)
        # Explicit multi-function source label supports primary shelf/towel rail.
        if candidates == {'Planchetten', 'Handdoekrekken met planchet'}:
            candidates = {'Handdoekrekken met planchet'}
            corrections.append('Combined shelf/towel rail explicit in other source group')
        titles = {r['fields']['Productomschrijving'] for r in source}
        if (candidates == {'Handdoekrekken', 'Topbladbeugels'}
                and len(titles) == 1 and next(iter(titles)).startswith('Topbladbeugel ')):
            candidates = {'Topbladbeugels'}
            corrections.append('Topbladbeugel explicit in identical titles and source category; not a towel rail')
        if (sku == '5-S-221' and candidates == {'Handdoekhaken', 'Handdoekrekken'}
                and titles == {'Handdoekbeugel mat zwart'}):
            candidates = {'Handdoekrekken'}
            corrections.append('Exact source correction proposal: handdoekbeugel title, not handdoekhaak')
        category = next(iter(candidates)) if len(candidates) == 1 else None
        if not category:
            exceptions.append({'sku':sku,'reason':'Conflicting category candidates','candidates':sorted(candidates)})
        fields=product['fields']; price=gross_price(fields['Adviesverkoopprijs ex. Btw'])
        # Independent integer cent computation verifies all prepared prices.
        cents=int(Decimal(fields['Adviesverkoopprijs ex. Btw'])*100)
        check=(cents*121+50)//100
        if Decimal(price)*100 != check:
            raise ValueError(f'Price rounding mismatch {sku}')
        future = '1-2-2027' in fields['Levertijd']
        proposals.append({'sku':sku,'brand':'BRAUER','ean':fields['EAN'],
            'source_title':fields['Productomschrijving'],'source_advice_ex_vat':fields['Adviesverkoopprijs ex. Btw'],
            'vat_rate':'0.21','advice_incl_vat':price,'prepared_consumer_price':price,
            'price_policy':'Advice incl 21% VAT as preparation basis; no discount assigned',
            'category_type_proposal':category,'category_candidates':sorted(candidates),
            'category_proposal_notes':sorted(set(corrections)),
            'source_field_conflicts':product['conflict_fields'],
            'availability_source':fields['Levertijd'],'future_available_date':'2027-02-01' if future else None,
            'publish_state':'HOLD_FUTURE' if future else 'DRAFT_PREPARATION_ONLY',
            'stock_count':None,'ready_to_import':False,'ready_to_publish':False,
            'source_refs':product['source_refs']})
    output_dir.mkdir(parents=True,exist_ok=True)
    summary={'date':'2026-11-06','unique_skus':len(proposals),'prepared_prices':len(proposals),
       'vat_rate':'0.21','category_mapping_status':'PROPOSED_NOT_APPLIED',
       'category_type_counts':dict(sorted(Counter(x['category_type_proposal'] for x in proposals).items(),key=lambda v:str(v[0]))),
       'category_exception_count':len(exceptions),
       'future_holds':sum(x['future_available_date'] is not None for x in proposals),
       'light_list_correction_proposals':sum(any('Light list' in n for n in x['category_proposal_notes']) for x in proposals),
       'empty_group_correction_proposals':sum(any('Empty group' in n for n in x['category_proposal_notes']) for x in proposals),
       'top_bracket_correction_proposals':sum(any('not a towel rail' in n for n in x['category_proposal_notes']) for x in proposals),
       'towel_rail_correction_proposals':sum(any('not handdoekhaak' in n for n in x['category_proposal_notes']) for x in proposals),
       'shopify_writes':0}
    for filename,data in [('catalog-proposal.json',proposals),('preparation-summary.json',summary),
                          ('category-exceptions.json',exceptions),
                          ('source-group-map.json',{k:sorted(v,key=str) for k,v in sorted(group_mapping.items())})]:
        (output_dir/filename).write_text(json.dumps(data,ensure_ascii=False,indent=2))
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(); prepare(args.audit_dir,args.output)
