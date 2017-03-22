from django.contrib import admin
from .models import Characters, Classes, Factions, Realms, Races, Timezones, Regions, Profile, Abilities
# Register your models here.


class RaceAdmin(admin.ModelAdmin):
    list_display = ('race_id', 'race_name', 'race_faction')


class TimezonesAdmin(admin.ModelAdmin):
    list_display = ('abbrv', 'full_name')


class RealmAdmin(admin.ModelAdmin):
    list_display = ('realm_name', 'realm_locale', 'realm_timezone', 'realm_type')


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('character_name', 'character_realm', 'character_level', 'character_class', 'character_race', 'character_owner')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'battle_net_id', 'user_timezone', 'looking_for_guild')
    

cla


admin.site.register(Characters, CharacterAdmin)
admin.site.register(Classes)
admin.site.register(Factions)
admin.site.register(Realms, RealmAdmin)
admin.site.register(Races, RaceAdmin)
admin.site.register(Timezones, TimezonesAdmin)
admin.site.register(Regions)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Abilities)