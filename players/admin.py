from django.contrib import admin
from .models import Characters, CharactersDetails, Classes, Factions, Realms, Races, Timezones, Regions, Profile
# Register your models here.


class RaceAdmin(admin.ModelAdmin):
    list_display = ('race_id', 'race_name', 'race_faction')


class TimezonesAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name')


class RealmAdmin(admin.ModelAdmin):
    list_display = ('realm_name', 'realm_locale', 'realm_timezone', 'realm_type')


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('character_name', 'character_realm', 'character_owner')


class CharactersDetailsAdmin(admin.ModelAdmin):
    list_display = ('character_link', 'character_level', 'character_class', 'character_race', 'looking_for_guild', 'character_faction')
    

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'battle_net_id', 'user_timezone')
    

admin.site.register(Characters, CharacterAdmin)
admin.site.register(CharactersDetails, CharactersDetailsAdmin)
admin.site.register(Classes)
admin.site.register(Factions)
admin.site.register(Realms, RealmAdmin)
admin.site.register(Races, RaceAdmin)
admin.site.register(Timezones, TimezonesAdmin)
admin.site.register(Regions)
admin.site.register(Profile, ProfileAdmin)
