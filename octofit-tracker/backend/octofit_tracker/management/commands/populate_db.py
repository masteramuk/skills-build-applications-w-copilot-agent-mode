from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB using CLIENT dictionary from settings
        client = MongoClient(
            host=settings.DATABASES['default']['CLIENT']['host'],
            port=settings.DATABASES['default']['CLIENT']['port'],
            username=settings.DATABASES['default']['CLIENT'].get('username'),
            password=settings.DATABASES['default']['CLIENT'].get('password'),
            authSource=settings.DATABASES['default']['CLIENT'].get('authSource', 'admin')
        )
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "ironman", "email": "ironman@octofit.edu", "password": "ironmanpassword"},
            {"_id": ObjectId(), "username": "blackwidow", "email": "blackwidow@octofit.edu", "password": "blackwidowpassword"},
            {"_id": ObjectId(), "username": "hulk", "email": "hulk@octofit.edu", "password": "hulkpassword"},
            {"_id": ObjectId(), "username": "hawkeye", "email": "hawkeye@octofit.edu", "password": "hawkeyepassword"},
            {"_id": ObjectId(), "username": "thor", "email": "thor@octofit.edu", "password": "thorpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Red Team", "members": []},
            {"_id": ObjectId(), "name": "Green Team", "members": []},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": None, "activity_type": "Yoga", "duration": 45, "date": "2025-04-01"},
            {"_id": ObjectId(), "user": None, "activity_type": "Pilates", "duration": 60, "date": "2025-04-02"},
            {"_id": ObjectId(), "user": None, "activity_type": "Running", "duration": 30, "date": "2025-04-03"},
            {"_id": ObjectId(), "user": None, "activity_type": "Weightlifting", "duration": 90, "date": "2025-04-04"},
            {"_id": ObjectId(), "user": None, "activity_type": "Swimming", "duration": 120, "date": "2025-04-05"},
        ]
        db.activities.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "team": None, "points": 150},
            {"_id": ObjectId(), "team": None, "points": 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Yoga Basics", "description": "Beginner yoga session", "difficulty": "Beginner"},
            {"_id": ObjectId(), "name": "Pilates Core", "description": "Core strengthening pilates", "difficulty": "Intermediate"},
            {"_id": ObjectId(), "name": "Running Endurance", "description": "Endurance training for runners", "difficulty": "Intermediate"},
            {"_id": ObjectId(), "name": "Weightlifting 101", "description": "Introduction to weightlifting", "difficulty": "Beginner"},
            {"_id": ObjectId(), "name": "Swimming Drills", "description": "Advanced swimming techniques", "difficulty": "Advanced"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))