from django.contrib import admin
from .models import Mentors, About, Feedback, Projects
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'company')
admin.site.register(Mentors)
admin.site.register(About)
admin.site.register(Projects)
admin.site.register(Feedback, FeedbackAdmin)