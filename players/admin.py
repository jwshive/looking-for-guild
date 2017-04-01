from django.contrib import admin
from .models import Characters, Classes, Factions, Realms, Races, Timezones, Regions


class RaceAdmin(admin.ModelAdmin):
    list_display = ('race_id', 'race_name', 'race_faction')


class TimezonesAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name')


class RealmAdmin(admin.ModelAdmin):
    list_display = ('realm_name', 'realm_locale', 'realm_timezone', 'realm_type')


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('character_name', 'character_realm', 'character_owner', 'character_level', 'is_character_active', 'looking_for_guild')



admin.site.register(Characters, CharacterAdmin)
admin.site.register(Classes)
admin.site.register(Factions)
admin.site.register(Realms, RealmAdmin)
admin.site.register(Races, RaceAdmin)
admin.site.register(Timezones, TimezonesAdmin)
admin.site.register(Regions)
