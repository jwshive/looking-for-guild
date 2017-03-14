from django.db import models


class Guilds(models.Model):
    guild_name = models.CharField(max_length=255)
    guild_realm = models.CharField(max_length=50)
    guild_battlegroup = models.CharField(max_length=50)
    guild_level = models.IntegerField()
    guild_faction = models.IntegerField()
    load_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'guilds'
        verbose_name_plural = 'Player Guilds'
        app_label = 'guilds'

    def __str__(self):
        return "%s of %s" % (self.guild_name, self.guild_realm)
