from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from apps.athlete.models import Athlete


class BaseViewTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='3',
                                                         password='12test12',
                                                         email='test@example.com')
        self.token = Token.objects.get(user=self.user)

        self.athlete = {
            "athlete_id": "840001",
            "name": "Alivio Fontes Mercedes",
            "sex": "M",
            "age": 28,
            "height": 190,
            "weight": 89,
            "team": "Brazil",
            "noc": "BRA"
        }

        self.client = APIClient()

    def test_usuario_nao_pode_cadastrar_novos_atletas_sem_estar_logado(self):
        response = self.client.post('/api/v1/atletas/', self.athlete)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_usuario_nao_pode_atualizar_dados_de_um_athlete_sem_estar_logado(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.login(username='3', password='12test12')

        response = self.client.post('/api/v1/atletas/', self.athlete)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

        athlete = Athlete.objects.first()
        name = {"name": "Alivio Fontes Morais"}
        response = self.client.put(f'/api/v1/atletas/{athlete.pk}/', name)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_usuario_tem_acesso_a_listagem_de_atletas_mesmo_sem_estar_logado(self):
        response = self.client.get('/api/v1/atletas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_usuario_pode_cadastrar_novos_atletas_se_estiver_logado(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.login(username='3', password='12test12')

        response = self.client.post('/api/v1/atletas/', self.athlete)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_usuario_pode_atualizar_dados_de_um_athlete_se_estiver_logado(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.login(username='3', password='12test12')

        response = self.client.post('/api/v1/atletas/', self.athlete)

        athlete = Athlete.objects.first()
        name = {"name": "Alivio Fontes Morais"}
        response = self.client.put(f'/api/v1/atletas/{athlete.pk}/', name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        User.objects.all().delete()
        self.client.logout()
