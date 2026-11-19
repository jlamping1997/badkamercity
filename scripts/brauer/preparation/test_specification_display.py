import copy
import unittest
from specification_display import project


def product(values, typ='Inbouwdouchesets'):
    return {'vendor':'BRAUER','sku':'EXACT-A','ean':'1234567890123','product_type':typ,
            'customer_specifications':[{'group':'Afmetingen','items':[
                {'key':str(i),'label':k,'value':v} for i,(k,v) in enumerate(values.items())]}]}


class DisplayTests(unittest.TestCase):
    def test_exact_same_head_size_keeps_specific_label_and_source_input(self):
        p=product({'Maat hoofddouche':'25 cm','Diameter hoofddouche':'25 cm'})
        old=copy.deepcopy(p); groups, removed=project(p)
        self.assertEqual(p,old)
        self.assertEqual([i['label'] for g in groups for i in g['items']],['Diameter hoofddouche'])
        self.assertEqual(removed[0]['rule'],'headshower_size')

    def test_different_size_units_precision_or_blank_is_not_collapsed(self):
        for a,b in [('30 cm','20 cm'),('20 cm','200 mm'),('20 cm','20,0 cm'),('','')]:
            with self.subTest(a=a,b=b):
                self.assertEqual(project(product({'Maat hoofddouche':a,'Diameter hoofddouche':b}))[1],[])

    def test_same_value_different_components_or_properties_are_retained(self):
        p=product({'Breedte':'25 cm','Diepte':'25 cm','Lengte douchearm':'25 cm',
                   'Diameter hoofddouche':'25 cm','Aansluitmaat doucheslang':'1/2"',
                   'Aansluitmaat watertoevoer':'1/2"','Thermostatisch':'Ja','Met temperatuurregeling':'Ja'})
        self.assertEqual(project(p)[1],[])

    def test_generic_thickness_and_glass_thickness_are_retained(self):
        self.assertEqual(project(product({'Dikte':'8 mm','Glasdikte':'8 mm'},'Douchecabines'))[1],[])

    def test_control_and_door_synonyms_are_scoped(self):
        for typ,values,keep in [
            ('Inbouwbadkranen',{'Bediening voor aan/uit':'Draaigreep','Bediening aan/uit':'Draaigreep'},'Bediening aan/uit'),
            ('Nisdeuren',{'Type deur':'Schuifdeur','Deursysteem':'Schuifdeur'},'Deursysteem')]:
            groups, removed=project(product(values,typ))
            self.assertEqual(len(removed),1)
            self.assertEqual(groups[0]['items'][0]['label'],keep)
            self.assertEqual(project(product(values,'Onderkasten'))[1],[])

    def test_held_fields_or_other_brand_are_not_suppressed(self):
        for hold in ['retail_review','measurement_hold','source_conflicts']:
            p=product({'Maat hoofddouche':'25 cm','Diameter hoofddouche':'25 cm'})
            p[hold]={'open_fields':['Diameter hoofddouche']} if hold=='retail_review' else {'fields':['Diameter hoofddouche']} if hold=='measurement_hold' else {'Diameter hoofddouche':[]}
            self.assertEqual(project(p)[1],[])
        p=product({'Maat hoofddouche':'25 cm','Diameter hoofddouche':'25 cm'});p['vendor']='OTHER'
        self.assertEqual(project(p)[1],[])

    def test_repeat_projection_is_stable(self):
        p=product({'Maat hoofddouche':'25 cm','Diameter hoofddouche':'25 cm'})
        groups,removed=project(p);p['customer_specifications']=groups
        self.assertEqual(project(p),(groups,[]))

    def test_duplicate_input_labels_require_review(self):
        p=product({'Diameter hoofddouche':'25 cm'});p['customer_specifications'][0]['items']*=2
        with self.assertRaises(ValueError):project(p)


if __name__=='__main__':unittest.main()
