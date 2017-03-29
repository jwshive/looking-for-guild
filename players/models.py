from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


ROLES = (
    ('MELEE_DPS', 'Melee DPS'),
    ('RANGED_DPS', 'Ranged DPS'),
    ('TANK', 'Tank'),
    ('HEALER', 'Healer'),
    ('NO_ROLE_SELECTED', 'No Role Selected'),
)


class Timezones(models.Model):
    short_name = models.CharField(max_length=10, null=False, blank=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'timezones'
        verbose_name_plural = 'Timezone Listings'

    def __str__(self):
        return "%s - %s" % (self.short_name, self.full_name)


class Factions(models.Model):
    faction_id = models.IntegerField(null=False, blank=False, primary_key=True, unique=True)
    faction_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'factions'
        verbose_name_plural = 'Character Factions'

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

    def __str__(self):
        return self.race_name


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
    battle_net_id = models.CharField(max_length=50, null=True, blank=True, unique=True)
    user_timezone = models.ForeignKey(Timezones, blank=True, null=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s's Profile Details" % self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Characters(models.Model):
    character_owner = models.ForeignKey(User)
    character_name = models.CharField(max_length=255)
    character_realm = models.ForeignKey(Realms)
    insert_date = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'characters'
        verbose_name_plural = 'Characters'
        unique_together = ('character_owner', 'character_name', 'character_realm')

    def __str__(self):
        return "%s of %s" % (self.character_name, self.character_realm)


class CharactersDetails(models.Model):
    character_link = models.ForeignKey(Characters)
    character_faction = models.ForeignKey(Factions)
    character_class = models.ForeignKey(Classes, null=True, blank=True)
    character_race = models.ForeignKey(Races, null=True, blank=True)
    character_level = models.IntegerField(null=True, blank=True)
    main_role = models.CharField(max_length=30, choices=ROLES, default="NO_ROLE_SELECTED", null=True, blank=True)
    alt_role = models.CharField(max_length=30, choices=ROLES, default="NO_ROLE_SELECTED", null=True, blank=True)
    looking_for_guild = models.BooleanField(default=False)
    looking_for_guild_advertisement = models.TextField(null=True, blank=True)
    character_armory_url_simple = models.URLField(null=True, blank=True)
    character_armory_url_advanced = models.URLField(null=True, blank=True)
    character_profile_image_url = models.CharField(max_length=100, null=True, blank=True)
    character_profile_avatar_url = models.CharField(max_length=100, null=True, blank=True)
    character_profile_inset_url = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        managed = True
        db_table = 'characters_details'
        verbose_name_plural = 'Character Details'
        
    def __str__(self):
        return "%s of %s (%s) Details" % (
            self.character_link.character_name,
            self.character_link.character_realm,
            self.character_faction
        )

    def create_character_slug(self):
        return "%s-%s-%s" % (
            self.character_link.character_name.lower(),
            self.character_link.character_realm.realm_name.lower().replace(' ', '-'),
            self.character_faction.faction_name.lower()
        )