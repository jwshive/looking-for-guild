from django.db import models
from players.models import Realms, Factions, Classes, Factions
from django.contrib.auth.models import User, Group


class Guilds(models.Model):
    guild_name = models.CharField(max_length=255, null=False, blank=False)
    guild_realm = models.ForeignKey(Realms)
    guild_faction = models.ForeignKey(Factions)
    guild_created_by = models.ForeignKey(User)
    guild_information = models.TextField(null=True, blank=True)
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


class GuildManagers(models.Model):
    guild_id = models.ForeignKey(Guilds, on_delete=models.CASCADE)
    guild_manager = models.ManyToManyField(User)

    class Meta:
        managed = True
        db_table = 'guild_managers'
        verbose_name_plural = 'Guild Managers'
        ordering =['guild_id']

    def __str__(self):
        return "%s - %s - %s" % (self.guild_id, self.guild_id.guild_realm.realm_name, self.guild_id.guild_faction.faction_name)


class RaidDays(models.Model):
    raid_day = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'raid_days'
        verbose_name_plural = 'Raid Day Listing'

    def __str__(self):
        return self.raid_day


class RaidTimes(models.Model):
    time_value = models.TimeField()

    class Meta:
        managed = True
        db_table = 'raid_times'
        verbose_name_plural = 'Raid Time Listings'

    def __str__(self):
        return str(self.time_value)


class RecruitmentPosts(models.Model):
    guild_name = models.ForeignKey(Guilds)
    recruiting_levels = models.CharField(max_length=100)
    recruiting_classes = models.ManyToManyField(Classes)
    raid_days = models.ManyToManyField(RaidDays)
    raid_start_time = models.ForeignKey(RaidTimes, blank=True, null=True, related_name='RaidStartTime')
    raid_end_time = models.ForeignKey(RaidTimes, blank=True, null=True, related_name='RaidEndTime')
    recruitment_title = models.CharField(max_length=200)
    recruitment_post = models.TextField()
    is_post_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'recruitment_posts'
        verbose_name_plural = 'Recruitment Postings'

