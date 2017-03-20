from django.db import models
from players.models import Realms, Factions
from django.contrib.auth.models import User, Group


class Guilds(models.Model):
    guild_name = models.CharField(max_length=255, null=False, blank=False)
    guild_realm = models.ForeignKey(Realms)
    guild_faction = models.ForeignKey(Factions)
    guild_created_by = models.ForeignKey(User)
    guild_managers = models.ForeignKey(Group)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'guilds'
        verbose_name_plural = 'Player Guilds'
        #app_label = 'guilds'

    def __str__(self):
        return "%s of %s" % (self.guild_name, self.guild_realm)
