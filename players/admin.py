from django.contrib import admin
from .models import Characters, Classes, Factions, Realms, Races, BattleNetIDs
# Register your models here.
admin.site.register(Characters)
admin.site.register(Classes)
admin.site.register(Factions)
admin.site.register(Realms)
admin.site.register(Races)
admin.site.register(BattleNetIDs)
