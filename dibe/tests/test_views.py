from rest_framework.test import APITestCase
from ..models import User
from django.shortcuts import reverse


class UserListViewTest(APITestCase):
    def setUp(self):
        self.user_list_url = reverse('user-list')

    def test_create_user(self):
        data = {
            'username': 'create_user',
            'password': 'password',
        }
        response = self.client.post(self.user_list_url, data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        data = {
            'username': 'get_user',
            'password': 'password',
        }
        self.client.post(self.user_list_url, data)
        response = self.client.get(self.user_list_url, format='json')
        self.assertEqual(len(response.data), 1)

    def test_create_user_with_short_password(self):
        data = {
            'username': 'user_with_short_password',
            'password': 'pass'
        }
        response = self.client.post(self.user_list_url, data)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, 400)

    def test_create_user_with_no_username(self):
        data = {
            'username': '',
            'password': 'password',
        }
        response = self.client.post(self.user_list_url, data)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, 400)

    # def test_create_user_with_preexisting_username(self):
    #     data = {
    #         'username': 'preexisting_username',
    #         'password': 'password',
    #     }
    #     self.client.post(self.user_list_url, data)
    #     response = self.client.post(self.user_list_url, data)
    #     self.assertEqual(User.objects.count(), 1)
    #     self.assertEqual(response.status_code, 400)
