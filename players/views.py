from players.api_functions import get_full_character_information, get_oauth_character_names
from .models import Realms, Characters, Factions, Classes, Races
from guilds.models import RecruitmentPosts, Guilds
from frontdoor.models import WebsiteAPISettings
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialToken
from django.db import IntegrityError


def MyProfile(request):
    character_filters = {'character_owner_id': request.user.id, 'is_character_active': True}
    context = {
        'my_guilds': Guilds.objects.filter(guild_created_by=request.user),
        'my_recruitment_posts': RecruitmentPosts.objects.select_related('guild_name').filter(guild_name__guild_created_by=request.user),
        'my_characters': Characters.objects.filter(**character_filters).order_by('character_realm'),
        'website_settings': WebsiteAPISettings.objects.get(pk=1),
    }
    return render(request, 'players/profile.html', context)


def CharacterDetail(request, pk):
    context = {
        'site_settings': WebsiteAPISettings.objects.all().get(),
        'character_info': Characters.objects.get(pk=pk)
    }
    return render(request, 'players/character_detail.html', context)


def CreateCharacter(request):
    # Flow
    # User clicks Add/Update my characters.
    # Pull Token
    AccessToken = SocialToken.objects.filter(account__user=request.user.id, account__provider='battlenet').get()
    # Get all characters from api build a list from the api of character|realm
    full_character_list_from_api = get_oauth_character_names(AccessToken.token)
    for toon_name, toon_realm in full_character_list_from_api:
        character_info = get_full_character_information(toon_name, toon_realm)
        # Loop through full character list. 
        # Insert records for new characters that are in the api pull that aren't in the db
        try:
            new_character, created = Characters.objects.update_or_create(
                    character_owner_id = request.user.id,
                    character_name = character_info['character_name'].title(),
                    character_realm = Realms.objects.get(realm_name = character_info['character_realm']),
                    character_faction = Factions.objects.get(faction_id = character_info['character_faction']),
                    character_class = Classes.objects.get(blizzard_class_id = character_info['class_id']),
                    character_race = Races.objects.get(race_id = character_info['race_id']), 
                    character_level = character_info['level'], 
                    equipped_ilevel = character_info['equipped_ilevel'],
                    max_ilevel = character_info['max_ilevel'],
                    character_armory_url_simple = character_info['armory_simple'], 
                    character_armory_url_advanced = character_info['armory_advanced'], 
                    character_profile_image_url = character_info['profile_image'], 
                    character_profile_avatar_url = character_info['avatar_image'], 
                    character_profile_inset_url = character_info['inset_image'], 
                    defaults = {
                        'character_level': character_info['level'], 
                        'character_race': Races.objects.get(race_id = character_info['race_id']),
                        'equipped_ilevel': character_info['equipped_ilevel'],
                        'max_ilevel': character_info['max_ilevel'],
                        }
                    )
        except IntegrityError:
            Characters.objects.filter(
                    character_owner_id = request.user.id, 
                    character_name = character_info['character_name'], 
                    character_realm = Realms.objects.get(realm_name = character_info['character_realm'])
                    ).update(
                            character_level = character_info['level'],
                            character_race = Races.objects.get(race_id = character_info['race_id']),
                            equipped_ilevel = character_info['equipped_ilevel'],
                            max_ilevel = character_info['max_ilevel'],
                            )

    # Leave old characters for users to deactivate
    # Get all toons for this player
    account_characters = Characters.objects.filter(character_owner = request.user)
    return redirect('user-profile')


class UpdateCharacterProfile(UpdateView):
    model = Characters
    template_name = 'players/update_character_profile.html'
    fields = 'looking_for_guild', 'looking_for_guild_advertisement', 'main_role', 'alt_role', 'is_character_active'
    success_url = '/players/profile'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateCharacterProfile, self).get_context_data(**kwargs)
        ctx['character_profile_object'] = Characters.objects.get(id=self.kwargs['pk'])
        return ctx

