from django.test import TestCase
from .models import UserProfile, Activity, Team, Leaderboard, WorkoutSuggestion

class TestDataPopulation(TestCase):
    def setUp(self):
        UserProfile.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        Leaderboard.objects.all().delete()
        WorkoutSuggestion.objects.all().delete()

    def test_populate_and_verify(self):
        # Populate test data
        UserProfile.objects.create(username='alice', email='alice@example.com', team='TeamA')
        UserProfile.objects.create(username='bob', email='bob@example.com', team='TeamA')
        UserProfile.objects.create(username='carol', email='carol@example.com', team='TeamB')

        Activity.objects.create(user='alice', activity_type='Running', duration=30, calories=250, date='2025-11-20')
        Activity.objects.create(user='bob', activity_type='Cycling', duration=45, calories=400, date='2025-11-21')
        Activity.objects.create(user='carol', activity_type='Swimming', duration=60, calories=500, date='2025-11-22')

        Team.objects.create(name='TeamA', members=['alice', 'bob'])
        Team.objects.create(name='TeamB', members=['carol'])

        Leaderboard.objects.create(team='TeamA', points=650)
        Leaderboard.objects.create(team='TeamB', points=500)

        WorkoutSuggestion.objects.create(user='alice', suggestion='Try interval running.', date='2025-11-23')
        WorkoutSuggestion.objects.create(user='bob', suggestion='Add hill cycling.', date='2025-11-23')
        WorkoutSuggestion.objects.create(user='carol', suggestion='Swim longer distances.', date='2025-11-23')

        # Verify
        self.assertEqual(UserProfile.objects.count(), 3)
        self.assertEqual(Activity.objects.count(), 3)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Leaderboard.objects.count(), 2)
        self.assertEqual(WorkoutSuggestion.objects.count(), 3)
