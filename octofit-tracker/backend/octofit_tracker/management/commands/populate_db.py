import logging
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from datetime import timedelta
from bson import ObjectId

logger = logging.getLogger(__name__)
logger.debug('populate_db.py script loaded')

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
        users = [User(_id=ObjectId(), **user) for user in test_users]
        User.objects.bulk_create(users)

        # Create teams
        teams = [Team(_id=ObjectId(), **team) for team in test_teams]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(
                _id=ObjectId(),
                user=User.objects.get(username=activity['username']),
                activity_type=activity['activity_type'],
                duration=timedelta(hours=int(activity['duration'].split(':')[0]), minutes=int(activity['duration'].split(':')[1]))
            ) for activity in test_activities
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(
                _id=ObjectId(),
                user=User.objects.get(username=entry['username']),
                score=entry['score']
            ) for entry in test_leaderboard
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [Workout(_id=ObjectId(), **workout) for workout in test_workouts]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
