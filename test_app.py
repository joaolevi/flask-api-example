import unittest
import json

from src.api.atadosapi import AtadosAPI

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.client = AtadosAPI().app.test_client()
        self.atados_api = AtadosAPI()
    
    def test_get_volunteers(self):
        response = self.client.get('/api/v1/volunteers')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.atados_api.get_volunteers(), '[]')

    def test_get_social_causes(self):
        response = self.client.get('/api/v1/socialcauses')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.atados_api.get_social_causes(), '[]')

    def test_post_new_volunteer(self):
        data = {"name": "Isaac", "surname": "Newton", "neighborhood": "Woolsthorpe-by-Colsterworth", "city": "Lincolnshire"}
        response = self.client.post('/api/v1/newvolunteer', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'voluntario salvo')

    def test_post_new_social_cause(self):
        data = {"name": "Doação de roupas", "institution_name": "Riachuelo", "adress": "Avenida Paulista, 2277, São Paulo", "description": "Evento para recolhimento e doação de roupas"}
        response = self.client.post('/api/v1/newsocialcause', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'acao social salva')

if __name__ == '__main__':
    unittest.main()
