"""API simulada: flujo real de scripts, recuperación y entradas nuevas, sin red."""
import csv
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import comprobar_pipeline
from resolver_llm import resolve, api_answer


class OrquestacionTest(unittest.TestCase):
    def prepare(self, folder, text='Call us to order pizza.'):
        local={'company_id':'cmp_prueba','location_id':'loc_prueba','company_name':'Nueva Pizza',
               'Company Country':'United States','project_verified_location_count':'4','Website':'https://example.com'}
        doc={'evidence_id':'doc_prueba','company_id':'cmp_prueba','location_id':'loc_prueba',
             'company_name':'Nueva Pizza','source_url':'https://example.com','source_type':'sitio_oficial',
             'source_text':text,'location_label':'Sucursal de prueba'}
        for name, row in [('entrada.csv',local),('evidencia_locales.csv',doc)]:
            with (folder/name).open('w',newline='') as stream:
                writer=csv.DictWriter(stream,fieldnames=list(row));writer.writeheader();writer.writerow(row)
        (folder/'textos_originales').mkdir()
        (folder/'textos_originales/doc_prueba.txt').write_text(text)
        (folder/'locales.csv').write_bytes((folder/'entrada.csv').read_bytes())
        (folder/'origen.json').write_text(json.dumps({'sha256':comprobar_pipeline.sha(folder/'locales.csv'),
            'execution_mode':'fresh','run_id':'fixture_run'}))
        (folder/'estado_ejecucion.json').write_text(json.dumps({'run_id':'fixture_run','status':'pendiente_codex','events':[]}))

    def fake_api(self, bundle, request_input, key, model, timeout):
        # Fixture de pruebas solamente; las respuestas dependen del texto recibido.
        if 'source_text' in request_input:
            text=request_input['source_text']
            answer={'claims':[{'evidence_description':text,'source_quote':text,
                    'topic':'phone_order_channel','scope':'company_wide','location_label':''}]} if 'Call' in text else {'claims':[]}
        else:
            answer={'labels':[{'evidence_id':r['evidence_id'],'topic':'phone_order_channel',
                'strength':'direct','sentiment':'neutral','attribution':'company_wide',
                'verbatim_quote':r['content'].split('VALIDATED EXACT SOURCE QUOTE: ')[1],
                'rationale':'Pedidos telefónicos publicados.'} for r in request_input['evidence']]}
        return answer,{'provider':'openai_api','model':model,'response_id':'mock','usage':{}}

    def run_pipeline(self, folder, mode='auto', action='--resume'):
        with patch.object(sys,'argv',['comprobar_pipeline.py','--input',str(folder/'entrada.csv'),
                       '--out-dir',str(folder),action,'--llm-mode',mode,'--model','modelo-de-prueba']), \
             patch('comprobar_pipeline.load_local_env'), \
             patch.dict('os.environ',{'OPENAI_API_KEY':'test-key'},clear=False),redirect_stdout(io.StringIO()):
            comprobar_pipeline.main()

    def test_auto_runs_both_stages_and_reuses_responses(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp);self.prepare(folder)
            with patch('resolver_llm.api_answer',side_effect=self.fake_api) as api:
                self.run_pipeline(folder)
                self.assertEqual(api.call_count,2)
            summary=json.loads((folder/'verificacion.json').read_text())
            self.assertEqual(summary['final_prospects'],1)
            self.assertEqual(summary['api_responses_saved'],2)
            with patch('resolver_llm.api_answer',side_effect=AssertionError('No repetir llamadas')):
                self.run_pipeline(folder,action='--replay')
            with (folder/'gtm-lista.csv').open() as f:
                row=next(csv.DictReader(f))
            self.assertEqual(row['company_name'],'Nueva Pizza')
            self.assertGreater(int(row['priority_score']),10)

    def test_api_failure_pauses_and_codex_can_resume(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp);self.prepare(folder)
            with patch('resolver_llm.api_answer',side_effect=URLError('no network')) as api:
                self.run_pipeline(folder)
                self.assertEqual(api.call_count,1)
            self.assertFalse((folder/'gtm-lista.csv').exists())
            for kind in ('extraccion','clasificacion'):
                bundle=json.loads((folder/f'solicitudes_{kind}_pendientes_codex.json').read_text())
                responses=[{'request_id':r['request_id'],'response':self.fake_api(bundle,r['input'],'','',1)[0]}
                           for r in bundle['requests']]
                (folder/f'respuestas_{kind}_codex.json').write_text(json.dumps(responses))
                with patch('resolver_llm.api_answer',side_effect=URLError('no network')):
                    self.run_pipeline(folder)
            self.assertTrue((folder/'gtm-lista.csv').exists())

    def test_changed_source_changes_result_and_rejects_old_answers(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp);self.prepare(folder,'Welcome to our restaurant.')
            with patch('resolver_llm.api_answer',side_effect=self.fake_api) as api:
                self.run_pipeline(folder)
                self.assertEqual(api.call_count,1)  # No evidencia: no hay clasificación LLM.
            with (folder/'gtm-lista.csv').open() as f:
                self.assertEqual(next(csv.DictReader(f))['priority_score'],'10')
            with (folder/'evidencia_locales.csv').open() as stream:
                doc=list(csv.DictReader(stream))[0]
            doc['source_text']='Call for orders.'
            with (folder/'evidencia_locales.csv').open('w',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=list(doc));writer.writeheader();writer.writerow(doc)
            with self.assertRaisesRegex(ValueError,'otra entrada'):
                self.run_pipeline(folder,'codex',action='--replay')

    def test_transport_sends_prompt_text_and_schema(self):
        bundle={'instructions':'Extract facts','response_schema':{'type':'object','properties':{'claims':{'type':'array','items':{'type':'string'}}},'required':['claims'],'additionalProperties':False}}
        body={'status':'completed','id':'resp_test','output':[{'type':'message','content':[{'type':'output_text','text':'{"claims": []}'}]}]}
        with patch('resolver_llm.urlopen') as network:
            network.return_value.__enter__.return_value=io.StringIO(json.dumps(body))
            answer,metadata=api_answer(bundle,{'source_text':'Unique input'},'test-key','test-model',3)
        payload=json.loads(network.call_args.args[0].data)
        self.assertEqual(json.loads(payload['input'])['source_text'],'Unique input')
        self.assertEqual(payload['instructions'],'Extract facts')
        self.assertEqual(payload['text']['format']['schema'],bundle['response_schema'])
        self.assertFalse(payload['store'])
        self.assertEqual(metadata['model'],'test-model')

    def test_partial_api_progress_is_saved_and_not_billed_again(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            schema={'type':'object','properties':{'claims':{'type':'array','items':{'type':'string'}}},
                    'required':['claims'],'additionalProperties':False}
            requests=folder/'solicitudes.json';responses=folder/'respuestas.json'
            requests.write_text(json.dumps({'instructions':'Extract','response_schema':schema,
                'requests':[{'request_id':str(i),'input':{'source_text':str(i)}} for i in range(3)]}))
            with patch('resolver_llm.api_answer',side_effect=[({'claims':[]},{'provider':'openai_api','model':'test'}),URLError('offline')]):
                with redirect_stdout(io.StringIO()):
                    outcome=resolve(requests,responses,api_key='key',model='test')
            self.assertFalse(outcome['complete'])
            self.assertEqual(outcome['pending'],2)
            self.assertEqual(len(json.loads(responses.read_text())),1)
            with patch('resolver_llm.api_answer',return_value=({'claims':[]},{'provider':'openai_api','model':'test'})) as api:
                outcome=resolve(requests,responses,api_key='key',model='test')
            self.assertTrue(outcome['complete'])
            self.assertEqual(api.call_count,2)

    def test_codex_mode_never_calls_api_even_with_key(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp);self.prepare(folder)
            with patch('resolver_llm.api_answer',side_effect=AssertionError('API prohibida')):
                self.run_pipeline(folder,'codex')
            self.assertTrue((folder/'solicitudes_extraccion_pendientes_codex.json').exists())
            self.assertFalse((folder/'gtm-lista.csv').exists())

    def start_fresh(self, source, output, mode='auto'):
        with patch.object(sys,'argv',['comprobar_pipeline.py','--input',str(source),
                       '--out-dir',str(output),'--llm-mode',mode,'--model','modelo-de-prueba']), \
             patch('comprobar_pipeline.load_local_env'), \
             patch.dict('os.environ',{'OPENAI_API_KEY':'test-key'},clear=False),redirect_stdout(io.StringIO()):
            comprobar_pipeline.main()

    def fresh_collector(self, folder, env):
        # Simula solo la respuesta HTTP. Ningún artefacto anterior entra al proceso.
        self.assertFalse((folder/'evidencia_locales.csv').exists())
        self.assertFalse((folder/'.pipeline').exists())
        self.assertFalse((folder/'respuestas_extraccion_codex.json').exists())
        with (folder/'locales.csv').open() as stream:
            local=next(csv.DictReader(stream))
        text='Call us to order pizza.'
        row={'evidence_id':'doc_fresh','company_id':local['company_id'],
             'location_id':local['location_id'],'company_name':local['company_name'],
             'source_url':local['Website'],'source_type':'sitio_oficial','source_text':text}
        with (folder/'evidencia_locales.csv').open('w',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=list(row));writer.writeheader();writer.writerow(row)
        (folder/'textos_originales').mkdir()
        (folder/'textos_originales/doc_fresh.txt').write_text(text)

    def test_two_fresh_runs_recollect_and_reinterpret_even_identical_sources(self):
        with tempfile.TemporaryDirectory() as temp:
            parent=Path(temp);self.prepare(parent)
            with patch('comprobar_pipeline.collect_sources',side_effect=self.fresh_collector) as collector, \
                 patch('resolver_llm.api_answer',side_effect=self.fake_api) as api:
                self.start_fresh(parent/'entrada.csv',parent/'run1')
                self.start_fresh(parent/'entrada.csv',parent/'run2')
            self.assertEqual(collector.call_count,2)
            self.assertEqual(api.call_count,4)
            requests=[]
            for name in ('run1','run2'):
                folder=parent/name
                self.assertEqual(json.loads((folder/'estado_ejecucion.json').read_text())['status'],'completada')
                self.assertEqual(json.loads((folder/'verificacion.json').read_text())['run_origin'],'fresh')
                requests.append(json.loads((folder/'solicitudes_extraccion.json').read_text())['requests'][0]['request_id'])
            self.assertNotEqual(*requests)
            before=(parent/'run1/gtm-lista.csv').read_bytes()
            with self.assertRaisesRegex(ValueError,'carpeta vacía'):
                self.start_fresh(parent/'entrada.csv',parent/'run1')
            self.assertEqual(before,(parent/'run1/gtm-lista.csv').read_bytes())

    def test_fresh_codex_run_is_explicitly_incomplete(self):
        with tempfile.TemporaryDirectory() as temp:
            parent=Path(temp);self.prepare(parent);folder=parent/'new'
            with patch('comprobar_pipeline.collect_sources',side_effect=self.fresh_collector), \
                 patch('resolver_llm.api_answer',side_effect=AssertionError('No API')):
                self.start_fresh(parent/'entrada.csv',folder,'codex')
            state=json.loads((folder/'estado_ejecucion.json').read_text())
            self.assertEqual(state['status'],'pendiente_codex')
            self.assertEqual(state['current_stage'],'extraccion')
            self.assertFalse((folder/'evidencia_llm_procesada.csv').exists())
            self.assertFalse((folder/'gtm-lista.csv').exists())
            self.assertFalse((folder/'verificacion.json').exists())
            raw=folder/'textos_originales/doc_fresh.txt'
            original=raw.read_text();raw.write_text('Texto alterado fuera del recolector')
            with self.assertRaisesRegex(ValueError,'fuente capturada'):
                self.run_pipeline(folder,'codex')
            raw.write_text(original)
            origin=json.loads((folder/'origen.json').read_text())
            origin['implementation_hashes']['scripts/comprobar_pipeline.py']='hash_modificado'
            (folder/'origen.json').write_text(json.dumps(origin))
            with self.assertRaisesRegex(ValueError,'código o prompt cambió'):
                self.run_pipeline(folder,'codex')

    def test_another_locales_file_generates_only_its_own_companies(self):
        with tempfile.TemporaryDirectory() as temp:
            parent=Path(temp);self.prepare(parent)
            with patch('comprobar_pipeline.collect_sources',side_effect=self.fresh_collector), \
                 patch('resolver_llm.api_answer',side_effect=self.fake_api):
                self.start_fresh(parent/'entrada.csv',parent/'original')
                with (parent/'entrada.csv').open() as stream:
                    template=next(csv.DictReader(stream))
                different=[{**template,'company_id':'cmp_tacos','location_id':'loc_tacos',
                            'company_name':'Otros Tacos','project_verified_location_count':'7'},
                           {**template,'company_id':'cmp_chinese','location_id':'loc_chinese',
                            'company_name':'Otra Chinese Kitchen','project_verified_location_count':'2'}]
                with (parent/'entrada.csv').open('w',newline='') as stream:
                    writer=csv.DictWriter(stream,fieldnames=list(template));writer.writeheader();writer.writerows(different)
                self.start_fresh(parent/'entrada.csv',parent/'different')
            with (parent/'different/gtm-lista.csv').open() as stream:
                final={r['company_name']:r for r in csv.DictReader(stream)}
            self.assertEqual(set(final),{'Otros Tacos','Otra Chinese Kitchen'})
            self.assertNotIn('Nueva Pizza',final)
            self.assertEqual(final['Otros Tacos']['locations_count'],'7')
            self.assertEqual(final['Otros Tacos']['cuisine'],'Tacos / mexicana')
            self.assertEqual(final['Otra Chinese Kitchen']['locations_count'],'2')
            self.assertEqual(final['Otra Chinese Kitchen']['priority_score'],'10')
            summary=json.loads((parent/'different/verificacion.json').read_text())
            self.assertEqual(summary['candidates'],2)
            self.assertTrue(summary['code_and_prompts_unchanged_during_run'])
            self.assertTrue(summary['captured_sources_unchanged_during_run'])


if __name__=='__main__':
    unittest.main()
