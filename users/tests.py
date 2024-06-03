from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class HabitTestCase(APITestCase):
    """Тест модели позователя"""
    def setUp(self):
        self.user = User.objects.create(email='test@test.ru', password='1234')

    def test_user_register_login(self):
        """Тест регистрации и аутентификации пользователя"""
        data = {
            'email': 'test1@test.ru',
            'password': 'password',
            'is_active': 'true'
        }

        response = self.client.post('/users/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(response.json().get('email'), 'test1@test.ru')

        response = self.client.post('/users/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
