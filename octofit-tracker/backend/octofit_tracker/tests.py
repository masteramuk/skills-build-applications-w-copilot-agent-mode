from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password")
        self.assertEqual(user.username, "testuser")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date="2025-04-09")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team A")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Push-ups", description="Do 20 push-ups", difficulty="Easy")
        self.assertEqual(workout.name, "Push-ups")

class UserAPITest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamAPITest(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Team A', 'members': []}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityAPITest(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password")
        url = reverse('activity-list')
        data = {'user': str(user._id), 'activity_type': 'Running', 'duration': 30, 'date': '2025-04-09'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardAPITest(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team A")
        url = reverse('leaderboard-list')
        data = {'team': str(team._id), 'points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutAPITest(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Push-ups', 'description': 'Do 20 push-ups', 'difficulty': 'Easy'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)