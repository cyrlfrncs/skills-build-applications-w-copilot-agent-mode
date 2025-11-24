from django.core.management.base import BaseCommand
from octofit_tracker.models import UserProfile, Activity, Team, Leaderboard, WorkoutSuggestion
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        UserProfile.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        Leaderboard.objects.all().delete()
        WorkoutSuggestion.objects.all().delete()

        # Super hero test data
        marvel = ['Iron Man', 'Captain America', 'Thor', 'Black Widow']
        dc = ['Superman', 'Batman', 'Wonder Woman', 'Flash']

        # Create users
        for hero in marvel:
            UserProfile.objects.create(username=hero.lower().replace(' ', '_'), email=f"{hero.lower().replace(' ', '')}@marvel.com", team='Marvel')
        for hero in dc:
            UserProfile.objects.create(username=hero.lower().replace(' ', '_'), email=f"{hero.lower().replace(' ', '')}@dc.com", team='DC')

        # Create activities
        Activity.objects.create(user='iron_man', activity_type='Flying', duration=60, calories=500, date='2025-11-20')
        Activity.objects.create(user='superman', activity_type='Flying', duration=120, calories=1000, date='2025-11-21')
        Activity.objects.create(user='batman', activity_type='Martial Arts', duration=90, calories=700, date='2025-11-22')
        Activity.objects.create(user='thor', activity_type='Hammer Training', duration=45, calories=400, date='2025-11-23')

        # Create teams
        Team.objects.create(name='Marvel', members=marvel)
        Team.objects.create(name='DC', members=dc)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=1600)
        Leaderboard.objects.create(team='DC', points=2400)

        # Create workout suggestions
        WorkoutSuggestion.objects.create(user='iron_man', suggestion='Try interval flying.', date='2025-11-24')
        WorkoutSuggestion.objects.create(user='superman', suggestion='Add kryptonite resistance.', date='2025-11-24')
        WorkoutSuggestion.objects.create(user='batman', suggestion='Increase martial arts sessions.', date='2025-11-24')
        WorkoutSuggestion.objects.create(user='thor', suggestion='Hammer throw practice.', date='2025-11-24')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with super hero test data.'))
