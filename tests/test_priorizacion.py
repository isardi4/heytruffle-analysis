"""Regresión: la falta de evidencia cambia prioridad, nunca elegibilidad."""
import csv
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from priorizar_leads import generate_from_files, score_final, publish_final, cuisine_from_profile


class PrioridadTest(unittest.TestCase):
    def test_cuisine_uses_profile_without_matching_delivery_as_deli(self):
        for name, expected in [('Golden Boy Pizza', 'Pizza'), ('Dallas BBQ', 'Barbacoa'),
                               ("Joe's Kansas City Bar-B-Que", 'Barbacoa'),
                               ('Holland Farms Bakery & Deli', 'Deli / panadería')]:
            self.assertEqual(cuisine_from_profile({'company_name': name})[0], expected)
        self.assertEqual(cuisine_from_profile({'Keywords': 'delivery, delicious food'})[0], 'Por confirmar')
        self.assertEqual(cuisine_from_profile({'cuisine': 'Italiana', 'company_name': 'Pizza'})[0], 'Italiana')
        self.assertEqual(cuisine_from_profile({'Short Description': 'pizza and burgers'})[0], 'Por confirmar')

    def generate(self, signals=True, outside=False, publish=False):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            locales=[];results=[];evidence=[]
            cases=[('perfil',None),('pico','demand_peak'),('canal','phone_order_channel'),('problema','phone_service_issue')]
            for name,topic in cases:
                locales.append({'company_id':name,'location_id':'loc_'+name,'company_name':name,
                    'Company Country':'United States','project_verified_location_count':1000 if outside and name=='perfil' else 3,
                    'Website':'https://example.com/'+name,'phone':'3125550100'})
                labels=[]
                if signals and topic:
                    labels=[{'evidence_id':'evi_'+name,'topic':topic,'strength':'direct','attribution':'this_location',
                        'verbatim_quote':'Source '+name,'source_url':'https://example.com/'+name}]
                    evidence.append({'evidence_id':'evi_'+name,'evidence_description':'Hecho '+name,'published_at':''})
                results.append({'company_id':name,'evidence_labels_json':json.dumps(labels),
                    'phone_problem_locations_count':1 if signals and name=='problema' else 0,
                    'analysis_status':'complete' if labels else 'awaiting_source_text'})
            def write(name,fields,rows):
                with (folder/name).open('w',newline='') as f:
                    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
            write('locales.csv',list(locales[0]),locales)
            write('resultados.csv',list(results[0]),results)
            write('evidencias.csv',['evidence_id','evidence_description','published_at'],evidence)
            with redirect_stdout(io.StringIO()):
                audit=generate_from_files(folder/'locales.csv',folder/'resultados.csv',folder/'evidencias.csv',folder)
                if publish:
                    public=folder/'oficial';public.mkdir()
                    publish_final(folder,public)
                    self.assertEqual((public/'gtm-lista.csv').read_bytes(),(folder/'gtm-lista.csv').read_bytes())
                    self.assertIn('perfil determina inclusión',(public/'LISTA-EXPLICADA.md').read_text())
            with (folder/'gtm-lista.csv').open() as f:
                reader=csv.DictReader(f);columns=reader.fieldnames;final=list(reader)
            return final,audit,columns

    def test_all_profile_candidates_survive_even_without_phone_signal(self):
        final,audit,columns=self.generate()
        self.assertEqual({r['company_name'] for r in final},{'perfil','pico','canal','problema'})
        self.assertEqual(len(columns),13)
        self.assertTrue(all(r['included_in_final'] for r in audit))
        by_name={r['company_name']:r for r in final}
        self.assertIn('por validar',by_name['perfil']['signal_1'])
        self.assertIn('evidencia_telefonica_pendiente',by_name['perfil']['notes'])
        self.assertEqual(by_name['perfil']['source_url'],'https://example.com/perfil')

    def test_total_source_failure_preserves_all_profile_candidates(self):
        final,audit,_=self.generate(signals=False)
        self.assertEqual(len(final),4)
        self.assertTrue(all(int(r['priority_score'])==10 for r in final))
        self.assertTrue(all(r['evidence_status']=='evidencia_telefonica_pendiente' for r in audit))
        self.assertTrue(all(not r['evidence_ids'] for r in audit))

    def test_evidence_orders_without_becoming_inclusion_filter(self):
        final,_,_=self.generate()
        scores={r['company_name']:int(r['priority_score']) for r in final}
        self.assertGreater(scores['problema'],scores['canal'])
        self.assertGreater(scores['canal'],scores['pico'])
        self.assertGreaterEqual(scores['pico'],scores['perfil'])
        self.assertEqual([int(r['priority_score']) for r in final],sorted(scores.values(),reverse=True))

    def test_profile_exclusion_still_applies_without_forcing_row_count(self):
        final,audit,_=self.generate(outside=True)
        self.assertEqual(len(final),3)
        outside=next(r for r in audit if r['company_name']=='perfil')
        self.assertFalse(outside['included_in_final'])
        self.assertEqual(outside['status'],'fuera_de_perfil')

    def test_cross_location_problem_has_more_priority_than_demand_only(self):
        base={k:False for k in ('historical_only','explicit_phone_issue','phone_orders','phone_inquiries',
            'shared_workload','demand_peak','capacity_constraint','dedicated_phone_role','location_specific',
            'source_text_available','recent_operational_publication')}
        peak={**base,'phone_orders':True,'demand_peak':True}
        problem={**base,'phone_orders':True,'explicit_phone_issue':True,'verified_problem_locations':8}
        self.assertGreater(score_final(problem)['score'],score_final(peak)['score'])

    def test_official_publication_matches_pipeline_even_without_evidence(self):
        final,_,_=self.generate(signals=False,publish=True)
        self.assertEqual(len(final),4)


if __name__=='__main__':unittest.main()
