from django.contrib import admin
from .models import CourseCategory, Courses
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk','category', 'name','course_length', 'modules', 'lessons')

admin.site.register(CourseCategory)
admin.site.register(Courses, CourseAdmin)