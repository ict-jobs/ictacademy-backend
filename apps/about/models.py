from django.db import models

# Create your models here.



class Mentors(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    github = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.name} - {self.profession}"
    
