from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField


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
    class_id = models.IntegerField(null=False, blank=False, primary_key=True, unique=True)
    class_name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'classes'
        verbose_name_plural = 'Character Classes'
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


class BattleNetIDs(models.Model):
    battle_net_id = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'battle_net_ids'
        verbose_name_plural = 'Battle Net IDs'
        #app_label = 'players'

    def __str__(self):
        return self.battle_net_id


class Characters(models.Model):
    character_battle_net_id = models.ForeignKey(BattleNetIDs)
    character_name = models.CharField(max_length=255)
    character_realm = models.ForeignKey(Realms)
    character_class = models.ForeignKey(Classes)
    character_race = models.ForeignKey(Races)
    character_level = models.IntegerField()
    character_faction = models.ForeignKey(Factions)
    character_ilevel = models.IntegerField()
    character_ilevel_equipped = models.IntegerField()
    character_head = models.CharField(max_length=50)
    character_neck = models.CharField(max_length=50)
    character_shoulder = models.CharField(max_length=50)
    character_back = models.CharField(max_length=50)
    character_chest = models.CharField(max_length=50)
    character_wrist = models.CharField(max_length=50)
    character_hands = models.CharField(max_length=50)
    character_waist = models.CharField(max_length=50)
    character_legs = models.CharField(max_length=50)
    character_feet = models.CharField(max_length=50)
    character_finger1 = models.CharField(max_length=50)
    character_finger2 = models.CharField(max_length=50)
    character_trinket1 = models.CharField(max_length=50)
    character_trinket2 = models.CharField(max_length=50)
    character_mainhand = models.CharField(db_column='character_mainHand', max_length=50)  # Field name made lowercase.
    character_offhand = models.CharField(db_column='character_offHand', max_length=50)  # Field name made lowercase.
    character_agility = models.IntegerField()
    character_armor = models.IntegerField()
    character_block = models.FloatField()
    character_critical_strike = models.FloatField()
    character_dodge = models.FloatField()
    character_haste = models.FloatField()
    character_health = models.IntegerField()
    character_intellect = models.IntegerField()
    character_leech = models.FloatField()
    character_mastery = models.FloatField()
    character_parry = models.FloatField()
    character_power = models.IntegerField()
    character_stamina = models.IntegerField()
    character_strength = models.IntegerField()
    character_versatility = models.IntegerField()
    load_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'characters'
        verbose_name_plural = 'Characters'
        #app_label = 'players'

    def __str__(self):
        return "%s of %s" % (self.character_name, self.character_realm)

