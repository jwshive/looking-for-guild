from django.contrib import admin
from .models import FrontDoorNews


class FrontDoorNewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_author', 'news_creation_date', 'news_published')

admin.site.register(FrontDoorNews, FrontDoorNewsAdmin)
