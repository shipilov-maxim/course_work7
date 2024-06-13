from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тест кейс для модели привычки"""

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.user2 = User.objects.create(email='test2@test.ru')
        self.habit = Habit.objects.create(action='Test action',
                                          place='Test place',
                                          time='19:00',
                                          is_nice=False,
                                          reward='Test reward',
                                          is_public=True,
                                          duration=timedelta(minutes=1),
                                          user=self.user)
        self.nice_habit = Habit.objects.create(action='Test enjoyable action',
                                               place='Test enjoyable place',
                                               time='19:00',
                                               is_nice=True,
                                               is_public=True,
                                               duration=timedelta(minutes=1),
                                               user=self.user)

    def test_habit_list_public(self):
        """Тест вывода списка публичных привычек"""
        url = reverse('habits:habits_public_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list_for_owner(self):
        """Тест вывода списка привычек определенного пользователя"""
        url = reverse('habits:habits_list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }
                         )

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data.get('results')), 2)

    def test_habit_retrieve(self):
        """Тест вывода одной привычки пользователя"""
        url = reverse('habits:habits_detail', args=(self.habit.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('id'), self.habit.pk)

    def test_habit_update(self):
        """Тест обновления привычки"""
        url = reverse('habits:habits_update', args=(self.habit.pk,))
        data = {'action': 'Updated test action'}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('action'), 'Updated test action')

    def test_habit_delete(self):
        """Тест удаления привычки"""
        url = reverse('habits:habits_delete', args=(self.habit.pk,))

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_create(self):
        """Тест создания привычки"""
        url = reverse('habits:habits_create')
        data = {
            'place': 'Test place 2',
            'time': '19:00:00',
            'action': 'Test action 2',
            'is_nice': False,
            'periodicity': 1,
            'reward': 'Test reward',
            'duration': '00:01:00',
            'is_public': True
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 3)
        self.assertEqual(response.json().get('action'), 'Test action 2')

        data_incorrect = {
            'place': 'Test place 2',
            'time': '19:00:00',
            'action': 'Test action 2',
            'is_nice': False,
            'periodicity': 1,
            'reward': 'Test reward',
            'duration': '00:03:00',
            'is_public': True,
            'related_habit': self.habit.pk
        }
        response = self.client.post(url, data_incorrect)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.json(), {'duration': ['Убедитесь, что это значение меньше либо равно 0:02:00.'],
                                           }
                         )

        data_enjoyable_incorrect = {
            'place': 'Test place 2',
            'time': '19:00:00',
            'action': 'Test action 2',
            'is_nice': True,
            'periodicity': 1,
            'reward': 'Test reward',
            'duration': '00:01:00',
            'is_public': True,
            'related_habit': self.habit.pk
        }
        response = self.client.post(url, data_enjoyable_incorrect)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            'non_field_errors': ['У приятной привычки не может быть вознаграждения',
                                 'В связанные привычки могут попадать только привычки с признаком приятной привычки.']
        }
                         )
