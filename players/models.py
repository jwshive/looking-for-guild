from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Timezones(models.Model):
    abbrv = models.CharField(max_length=10, null=False, blank=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'timezones'
        verbose_name_plural = 'Timezone Listings'

    def __str__(self):
        return "%s - %s" % (self.abbrv, self.full_name)


class Factions(models.Model):
    faction_id = models.IntegerField(null=False, blank=False, primary_key=True, unique=True)
    faction_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'factions'
        verbose_name_plural = 'Character Factions'
        #app_label = 'players'

    def __str__(self):
        return self.faction_name

class Classes(models.Model):
        class_name = models.CharField(max_length=50)
        blizzard_class_id = models.IntegerField()
    
        class Meta:
            managed = True
            db_table = 'classes'
            verbose_name_plural = 'Character Classes'
            ordering = ['class_name']
            #app_label = 'players'
    
        def __str__(self):
            return self.class_name


class Races(models.Model):
    race_id = models.IntegerField(null=False, blank=False, primary_key=True, unique=True)
    race_name = models.CharField(max_length=50)
    race_faction = models.ForeignKey(Factions, to_field='faction_id')

    class Meta:
        managed = True
        db_table = 'races'
        verbose_name_plural = 'Character Races'
        #app_label = 'players'

    def __str__(self):
        return "%s - %s" % (self.race_faction.faction_name, self.race_name)


class Realms(models.Model):
    realm_type = models.CharField(max_length=50)
    realm_population = models.CharField(max_length=10)
    realm_name = models.CharField(max_length=50)
    realm_slug = AutoSlugField(populate_from='realm_name')
    realm_battlegroup = models.CharField(max_length=50)
    realm_locale = models.CharField(max_length=50)
    realm_timezone = models.CharField(max_length=255)
    realm_connected_realms = models.TextField()
    load_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'realms'
        verbose_name_plural = 'Realms'
        #app_label = 'players'
        ordering = ['realm_name']

    def __str__(self):
        return self.realm_name


class Regions(models.Model):
    region_name = models.CharField(max_length=3, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'regions'
        verbose_name_plural = 'Regions'
        ordering = ['region_name']

    def __str__(self):
        return self.region_name.upper()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    battle_net_id = models.CharField(max_length=50, null=False, blank=False, unique=True)
    user_timezone = models.ForeignKey(Timezones, blank=False, null=False)
    looking_for_guild = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s's Profile Details" % self.user.username


class Characters(models.Model):
    character_owner = models.ForeignKey(User)
    character_name = models.CharField(max_length=255)
    character_realm = models.ForeignKey(Realms)
    character_class = models.ForeignKey(Classes)
    character_race = models.ForeignKey(Races)
    character_level = models.IntegerField()
    character_faction = models.ForeignKey(Factions)
    character_armory_url = models.URLField()
    load_date = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'characters'
        verbose_name_plural = 'Characters'
        #app_label = 'players'

    def __str__(self):
        return "%s of %s" % (self.character_name, self.character_realm)

