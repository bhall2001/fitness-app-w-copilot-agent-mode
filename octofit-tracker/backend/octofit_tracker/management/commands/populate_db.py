# Copilot agent mode: Test data population script for octofit_db
# This Django management command populates the MongoDB database with test data for users, teams, activities, leaderboard, and workouts.
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams (convert ObjectId to str for JSONField)
        team1 = Team.objects.create(name='Team Alpha', members=[str(user1.id), str(user2.id)])
        team2 = Team.objects.create(name='Team Beta', members=[str(user3.id)])

        # Activities
        Activity.objects.create(user_id=str(user1.id), activity_type='run', duration=30, date=timezone.now())
        Activity.objects.create(user_id=str(user2.id), activity_type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user_id=str(user3.id), activity_type='strength', duration=20, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(team_id=str(team1.id), points=100)
        Leaderboard.objects.create(team_id=str(team2.id), points=80)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Jogging', description='Jog for 15 minutes')
        Workout.objects.create(name='Plank', description='Hold a plank for 1 minute')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
