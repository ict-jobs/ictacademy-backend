from django.db import models

# Create your models here.
from mptt.models import MPTTModel , TreeForeignKey ,TreeManager
from apps.account.models import Mentor, User

class Course(MPTTModel):  
    title = models.CharField(max_length=255)   
    course_duration = models.CharField(max_length=255, blank=True, null=True)
    moduls = models.CharField(max_length=3, null=True, blank=True)
    number_classes = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to="images", blank=True)  
    description = models.TextField(blank=True, null=True, default=None)
    detailed = models.CharField(max_length=2048, null=True, blank=True)
    
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )

    mentor = models.ManyToManyField(
        Mentor
    )
    
    student = models.ManyToManyField(
        User
    )