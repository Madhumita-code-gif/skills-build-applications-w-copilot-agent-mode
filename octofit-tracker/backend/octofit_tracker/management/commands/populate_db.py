from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with test data for Octofit Tracker'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name, is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name, is_superhero=True)
        diana = User.objects.create(email='diana@themyscira.com', name='Diana Prince', team=dc.name, is_superhero=True)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=diana, type='swim', duration=60, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=200)

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='Marvel')
        Workout.objects.create(name='Sprints', description='Speed training', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))
