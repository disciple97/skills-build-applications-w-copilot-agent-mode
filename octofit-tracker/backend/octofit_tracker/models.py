from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.FloatField()
    calories = models.FloatField()
    date = models.DateField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField('User', related_name='suggested_workouts', blank=True)

class Leaderboard(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE, related_name='leaderboard')
    total_points = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

