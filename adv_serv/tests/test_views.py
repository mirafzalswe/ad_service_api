from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ..models import Ad

class AdDetailViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='samandar', password='samandar1234')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.ad = Ad.objects.create(
            title='smthing smthing',
            ad_id=1,
            author='Mr Sm',
            views=100,
            position=1
        )
        self.url = reverse('ad-detail', kwargs={'ad_id': self.ad.ad_id})

    def test_get_ad_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.ad.title)

class CreateUserViewTest(APITestCase):

    def test_create_user(self):
        url = reverse('create_user')
        data = {
            'username': 'samandar',
            'password': 'samandar1234'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'samandar')
        self.assertIn('token', response.data)
