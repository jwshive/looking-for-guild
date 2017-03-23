from django.db import models
from django.contrib.auth.models import User


class WebsiteAPISettings(models.Model):
    wow_api_key = models.CharField(max_length=100)
    wow_api_secret = models.CharField(max_length=100)
    wow_api_character_url_fields = models.CharField(max_length=200)
    wow_api_base_url = models.URLField()
    wow_api_character_image_base_url = models.URLField()
    
    class Meta:
        managed = True
        db_table = 'website_api_settings'
        verbose_name_plural = "Website API Settings"
        

class FrontDoorNews(models.Model):
    news_title = models.CharField(max_length=255, blank=False, null=False)
    news_content = models.TextField()
    news_author = models.ForeignKey(User)
    news_creation_date = models.DateTimeField(auto_now_add=True)
    news_last_updated = models.DateTimeField(auto_now=True)
    news_published = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'front_door_news'
        verbose_name_plural = 'Front Door News'
        app_label = 'frontdoor'

    def __str__(self):
        return "%s, written on %s by %s" % (self.news_title, self.news_creation_date, self.news_author.first_name + " " + self.news_author.last_name)


class Feedback(models.Model):
    feedback_submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_subject = models.CharField(max_length=100)
    feedback_body = models.TextField()
    feedback_submitted_on = models.DateTimeField(auto_now_add=True)
    feedback_read = models.BooleanField(default=False)
    feedback_responded_to = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'feedback'
        verbose_name_plural = 'User Feedback'
        app_label = 'frontdoor'

    def __str__(self):
        return "Feedback Submitted by %s (%s) on %s" % (self.feedback_submitted_by, self.feedback_submitted_by.email, self.feedback_submitted_on)
