from django.core.management.base import BaseCommand
from api.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create users (superheroes)
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        for user in users:
            Activity.objects.create(user=user, type='Running', duration=30)
            Activity.objects.create(user=user, type='Cycling', duration=45)

        # Create workouts
        for user in users:
            Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session', duration=40)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=300)
        Leaderboard.objects.create(team=dc, points=250)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
