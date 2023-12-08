from django.db import models

# Create your models here.



class Mentors(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    github = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    
    image = models.ImageField(upload_to='mentors/',)
    queue = models.IntegerField(null=True, blank=True, verbose_name="Navbati")


    def __str__(self) -> str:
        return f"{self.name} - {self.profession}"
    



class Feedback(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)
    feedback = models.TextField( null=True, blank=True)
    image = models.ImageField( null=True, blank=True)
    company = models.CharField(max_length = 50, null=True, blank=True)
    company_logo = models.ImageField(upload_to='logo/', null=True, blank=True)


class Projects(models.Model):
    product_name = models.CharField(max_length=350)
    product_image = models.ImageField(upload_to='product/')
    product_image_2 = models.ImageField(upload_to='product/')
    product_url_web = models.CharField(max_length=250, null=True, blank=True)
    product_url_ios = models.CharField(max_length=250, null=True, blank=True)
    product_url_android = models.CharField(max_length=250, null=True, blank=True)


    spend_time = models.IntegerField()
    users = models.IntegerField()

    about_customer = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.product_name)
    
    

class AboutUs(models.Model):
    main_title = models.CharField(max_length=300, null=True, blank=True)
    main_subtitle = models.CharField(max_length=300, null=True, blank=True)
    courses = models.IntegerField( null=True, blank=True)
    course_directions = models.IntegerField( null=True, blank=True)
    graduates = models.IntegerField( null=True, blank=True)
    students = models.IntegerField( null=True, blank=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    director = models.CharField(max_length = 70, null=True, blank=True)
    director_pos = models.CharField(max_length = 70, null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    


    def __str__(self) -> str:
        return str("About part on Academy")
