from django.contrib import admin
from .models import Characters, Classes, Factions, Realms, Races, BattleNetIDs
# Register your models here.


class RaceAdmin(admin.ModelAdmin):
    list_display = ('race_id', 'race_name', 'race_faction')


admin.site.register(Characters)
admin.site.register(Classes)
admin.site.register(Factions)
admin.site.register(Realms)
admin.site.register(Races, RaceAdmin)
admin.site.register(BattleNetIDs)
