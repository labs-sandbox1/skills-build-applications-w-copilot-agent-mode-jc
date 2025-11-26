from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create superhero users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass')

        # Create activities with proper user foreign keys
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=spiderman, type='cycle', duration=45)
        Activity.objects.create(user=batman, type='swim', duration=60)
        Activity.objects.create(user=superman, type='run', duration=50)

        # Create leaderboard entries with team foreign keys
        Leaderboard.objects.create(team=marvel, points=75)
        Leaderboard.objects.create(team=dc, points=110)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Run and cycle for 30 minutes')
        Workout.objects.create(name='Strength Training', description='Pushups and squats')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
