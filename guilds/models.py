from django.db import models
from players.models import Realms, Factions, Classes, Factions
from django.contrib.auth.models import User, Group
from autoslug import AutoSlugField


class Guilds(models.Model):
    guild_name = models.CharField(max_length=255, null=False, blank=False)
    guild_realm = models.ForeignKey(Realms)
    guild_faction = models.ForeignKey(Factions)
    guild_created_by = models.ForeignKey(User)
    guild_information = models.TextField()
    guild_battlenet_website = models.URLField(null=True, blank=True)
    guild_external_website = models.URLField(null=True, blank=True)
    guild_wow_progress_link = models.URLField(null=True, blank=True)
    guild_warcraft_logs_link = models.URLField(null=True, blank=True)
    guild_world_of_logs_link = models.URLField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_recruiting = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'guilds'
        verbose_name_plural = 'Player Guilds'
        ordering = ['guild_realm']
        unique_together = ('guild_name', 'guild_realm', 'guild_faction')
        
    def __str__(self):
        return self.guild_name


class RecruitmentPosts(models.Model):
    guild_name = models.ForeignKey(Guilds)
    recruiting_levels = models.CharField(max_length=100)
    recruiting_classes = models.ManyToManyField(Classes)
    recruitment_title = models.CharField(max_length=200)
    recruitment_post = models.TextField()
    is_post_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'recruitment_posts'
        verbose_name_plural = 'Recruitment Postings'

