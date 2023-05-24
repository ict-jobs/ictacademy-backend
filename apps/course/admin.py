from django.contrib import admin
from .models import CourseCategory, Courses, KursgaYozilish
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk','category', 'name','course_length', 'modules', 'lessons')
class KursgaYozilishAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name', 'profession', 'phone', 'date')

admin.site.register(CourseCategory)
admin.site.register(Courses, CourseAdmin)
admin.site.register(KursgaYozilish, KursgaYozilishAdmin)