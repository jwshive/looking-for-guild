from django.contrib import admin
from .models import FrontDoorNews, Feedback


class FrontDoorNewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_author', 'news_creation_date', 'news_published')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_subject', 'feedback_submitted_by', 'feedback_submitted_on', 'feedback_read', 'feedback_responded_to')


admin.site.register(FrontDoorNews, FrontDoorNewsAdmin)
admin.site.register(Feedback, FeedbackAdmin)

