from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Workout, Leaderboard

class APISmokeTest(APITestCase):
	def test_users_list(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_teams_list(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_activities_list(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_workouts_list(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_leaderboards_list(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
