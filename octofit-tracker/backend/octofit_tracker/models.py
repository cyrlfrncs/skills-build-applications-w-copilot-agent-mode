from djongo import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.username

class Activity(models.Model):
    user = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    calories = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team}: {self.points}"

class WorkoutSuggestion(models.Model):
    user = models.CharField(max_length=150)
    suggestion = models.TextField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.date}"