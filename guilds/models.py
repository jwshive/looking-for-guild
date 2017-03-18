from django.db import models
from players.models import Realms, Factions


class Guilds(models.Model):
    guild_name = models.CharField(max_length=255, null=False, blank=False)
    guild_realm = models.ForeignKey(Realms)
    guild_faction = models.ForeignKey(Factions)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'guilds'
        verbose_name_plural = 'Player Guilds'
        #app_label = 'guilds'

    def __str__(self):
        return "%s of %s" % (self.guild_name, self.guild_realm)
