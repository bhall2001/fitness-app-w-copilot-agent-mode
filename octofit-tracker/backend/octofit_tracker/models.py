from django.db import models

# User model for MongoDB (not using Django's default User)
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # Add other fields as needed

    class Meta:
        db_table = "users"

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)  # List of user IDs
    # Add other fields as needed

    class Meta:
        db_table = "teams"

class Activity(models.Model):
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField()
    # Add other fields as needed

    class Meta:
        db_table = "activity"

class Leaderboard(models.Model):
    team_id = models.CharField(max_length=100)
    points = models.IntegerField()
    # Add other fields as needed

    class Meta:
        db_table = "leaderboard"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as needed

    class Meta:
        db_table = "workouts"
