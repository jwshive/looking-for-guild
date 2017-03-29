from django.contrib import admin
from .models import Characters, CharactersDetails, Classes, Factions, Realms, Races, Timezones, Regions, Profile
from django.contrib.auth import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

username_regex_field = forms.RegexField(
    label="Username",
    max_length=30,
    regex=r"^[\w.]+#\d+$",
    help_text="Required. 30 characters or fewer. Letters, apostrophes, periods, hyphens and at signs.",
    error_message="This value must contain only letters, apostrophes, periods, hyphens and at signs."
)


class UserCreationForm(UserCreationForm):
    username = username_regex_field


class UserChangeForm(UserChangeForm):
    username = username_regex_field


class UserProfileAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


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
