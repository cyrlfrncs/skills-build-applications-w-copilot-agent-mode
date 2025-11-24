from rest_framework import viewsets
from .models import UserProfile, Activity, Team, Leaderboard, WorkoutSuggestion
from .serializers import (
    UserProfileSerializer, ActivitySerializer, TeamSerializer,
    LeaderboardSerializer, WorkoutSuggestionSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer

@api_view(['POST'])
def populate_test_data(request):
    # Clear existing data
    UserProfile.objects.all().delete()
    Activity.objects.all().delete()
    Team.objects.all().delete()
    Leaderboard.objects.all().delete()
    WorkoutSuggestion.objects.all().delete()

    # Create test users
    u1 = UserProfile.objects.create(username='alice', email='alice@example.com', team='TeamA')
    u2 = UserProfile.objects.create(username='bob', email='bob@example.com', team='TeamA')
    u3 = UserProfile.objects.create(username='carol', email='carol@example.com', team='TeamB')

    # Create test activities
    Activity.objects.create(user='alice', activity_type='Running', duration=30, calories=250, date='2025-11-20')
    Activity.objects.create(user='bob', activity_type='Cycling', duration=45, calories=400, date='2025-11-21')
    Activity.objects.create(user='carol', activity_type='Swimming', duration=60, calories=500, date='2025-11-22')

    # Create test teams
    Team.objects.create(name='TeamA', members=['alice', 'bob'])
    Team.objects.create(name='TeamB', members=['carol'])

    # Create leaderboard
    Leaderboard.objects.create(team='TeamA', points=650)
    Leaderboard.objects.create(team='TeamB', points=500)

    # Create workout suggestions
    WorkoutSuggestion.objects.create(user='alice', suggestion='Try interval running.', date='2025-11-23')
    WorkoutSuggestion.objects.create(user='bob', suggestion='Add hill cycling.', date='2025-11-23')
    WorkoutSuggestion.objects.create(user='carol', suggestion='Swim longer distances.', date='2025-11-23')

    return Response({'status': 'Test data populated'})
