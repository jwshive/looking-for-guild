from django.db import models
from django.contrib.auth.models import User


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
