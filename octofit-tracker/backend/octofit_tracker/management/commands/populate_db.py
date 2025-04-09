from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        for user in users:
            user.save()  # Save each user individually to populate primary keys

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()
        team1.members.set(users[:3])  # Add first three users to Blue Team
        team2.members.set(users[3:])  # Add remaining users to Gold Team

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=users[1], activity_type='Crossfit', duration=120, date='2025-04-02'),
            Activity(user=users[2], activity_type='Running', duration=90, date='2025-04-03'),
            Activity(user=users[3], activity_type='Strength', duration=30, date='2025-04-04'),
            Activity(user=users[4], activity_type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=300),
            Leaderboard(team=team2, points=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', difficulty='Intermediate'),
            Workout(name='Crossfit', description='Training for a crossfit competition', difficulty='Advanced'),
            Workout(name='Running Training', description='Training for a marathon', difficulty='Intermediate'),
            Workout(name='Strength Training', description='Training for strength', difficulty='Beginner'),
            Workout(name='Swimming Training', description='Training for a swimming competition', difficulty='Intermediate'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))