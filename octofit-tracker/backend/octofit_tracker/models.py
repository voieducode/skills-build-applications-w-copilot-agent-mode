from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    id = None  # Remove the default id field
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # Add other fields as needed

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()  # Use JSONField to store a list of user IDs as strings
    # Add other fields as needed

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    # Add other fields as needed

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    # Add other fields as needed

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()
    # Add other fields as needed
