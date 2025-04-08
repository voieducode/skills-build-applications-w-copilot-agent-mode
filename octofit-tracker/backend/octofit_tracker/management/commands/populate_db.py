from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

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
            User(_id=ObjectId(), name='thundergod', email='thundergod@mhigh.edu'),
            User(_id=ObjectId(), name='metalgeek', email='metalgeek@mhigh.edu'),
            User(_id=ObjectId(), name='zerocool', email='zerocool@mhigh.edu'),
            User(_id=ObjectId(), name='crashoverride', email='crashoverride@mhigh.edu'),
            User(_id=ObjectId(), name='sleeptoken', email='sleeptoken@mhigh.edu'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team', members=[str(users[0]._id), str(users[1]._id)])
        team2 = Team(name='Gold Team', members=[str(users[2]._id), str(users[3]._id), str(users[4]._id)])
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], description='Cycling for 1 hour'),
            Activity(user=users[1], description='Crossfit for 2 hours'),
            Activity(user=users[2], description='Running for 1.5 hours'),
            Activity(user=users[3], description='Strength training for 30 minutes'),
            Activity(user=users[4], description='Swimming for 1.25 hours'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=90),
            Leaderboard(user=users[2], score=95),
            Leaderboard(user=users[3], score=85),
            Leaderboard(user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(user=users[0], duration=60),  # Cycling Training
            Workout(user=users[1], duration=120),  # Crossfit
            Workout(user=users[2], duration=90),  # Running Training
            Workout(user=users[3], duration=30),  # Strength Training
            Workout(user=users[4], duration=75),  # Swimming Training
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
