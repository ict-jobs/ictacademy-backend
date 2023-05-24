from django.db import models

# Create your models here.


class Contact(models.Model):


    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=80)

    website = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return "ICT Academy Contacts"
