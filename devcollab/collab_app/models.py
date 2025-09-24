from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    github_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    admins = models.ManyToManyField(User, related_name='admin_teams')
    created_at = models.DateTimeField(auto_now_add=True)
    repository_url = models.URLField(max_length=200, blank=True)
    profile_picture = models.ImageField(upload_to='team_pictures/', blank=True)

    def __str__(self):
        return self.name  

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient_profile = models.ForeignKey(Profile, related_name='received_messages', on_delete=models.CASCADE, blank=True, null=True)
    recipient_team = models.ForeignKey(Team, related_name='team_messages', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:20] + '...'
  
          
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_by = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    team = models.ForeignKey(Team, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.title    