from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='konstantin_mikheev@mail.ru')
        self.habit = Habit.objects.create(user=self.user, action='Read a book', place='Library', frequency=1,
                                         duration=2)
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('habits:habits-list')
        data = {
            'user': self.user.pk,
            'action': 'Read a book',
            'place': 'Library',
            'frequency': 1,
            'duration': 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_update_habit(self):
        url = reverse('habits:habits-detail', kwargs={'pk': self.habit.pk})
        data = {
            'action': 'Read a book (updated)',
            'place': 'Library (updated)',
            'frequency': 2,
            'duration': 2
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('action'), 'Read a book (updated)')

    def test_delete_habit(self):
        url = reverse('habits:habits-detail', kwargs={'pk': self.habit.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_retrieve_habit(self):
        url = reverse('habits:habits-detail', kwargs={'pk': self.habit.pk})
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('action'), 'Read a book')

    def test_list_habits(self):
        url = reverse('habits:habits-list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('results')[0].get('action'), 'Read a book')
