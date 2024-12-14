from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    message_type = models.CharField(max_length=20)  # e.g., 'error' or 'success'
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.message_type.capitalize()} - {self.message[:50]}"



# from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Unique username
    email = models.EmailField(unique=True)  # Unique email
    password = models.CharField(max_length=128)  # Encrypted password

    def __str__(self):
        return self.username

# Create your models here.