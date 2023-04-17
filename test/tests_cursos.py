from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1',descricao = 'Curso teste 2', nivel = "B"
        )
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT2',descricao = 'Curso teste 2', nivel = "A"
        )
    
    # def test_fail(self):
    #     self.fail("fail test on purpose")

    def test_requisicao_get_listcursos(self):
        """teste de verificação get"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        

    def test_requisicao_post_listcursos(self):
        """teste de verificação post"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'curso teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data = data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_requisicao_delete_listcursos(self):
        """teste de verificação delete"""
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_requisicao_put_listcursos(self):
        """teste de verificação put"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'curso teste 3 att',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data = data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        