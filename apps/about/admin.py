from django.contrib import admin
from .models import Mentors,  Feedback, Projects, AboutUs
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'company')
    

class MentorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'queue')

admin.site.register(Mentors, MentorsAdmin)
admin.site.register(Projects)
admin.site.register(AboutUs)
admin.site.register(Feedback, FeedbackAdmin)