from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.username + " " + self.phone_number
    
class Mentor(models.Model):
    role = models.CharField(max_length=100)
    image = models.FileField(upload_to='Image', null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='Mentor',
        null=True, blank=True
    )
    def __str__(self):
        return self.username + " " + self.role
