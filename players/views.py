from players.api_functions import get_oauth_character_information, get_oauth_character_names
from .models import Realms, Characters, Factions, Classes
from guilds.models import RecruitmentPosts, Guilds
from frontdoor.models import WebsiteAPISettings
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from players.forms import AddCharacterForm
from allauth.socialaccount.models import SocialToken


def MyProfile(request):
    context = {
        'my_guilds': Guilds.objects.filter(guild_created_by=request.user),
        'my_recruitment_posts': RecruitmentPosts.objects.select_related('guild_name').filter(guild_name__guild_created_by=request.user),
        'my_characters': Characters.objects.filter(character_owner_id=request.user.id).order_by('character_realm'),
        'website_settings': WebsiteAPISettings.objects.get(pk=1),
    }
    return render(request, 'players/profile.html', context)


def CharacterDetail(request, pk):
    context = {
        'site_settings': WebsiteAPISettings.objects.all().get(),
        'character_info': Characters.objects.get(pk=pk)
    }
    return render(request, 'players/character_detail.html', context)


def CreateCharacter(request, character_owner):
    # Flow
    # User clicks Add/Update my characters.
    # Pull Token
    AccessToken = SocialToken.objects.filter(account__user=request.user.id, account__provider='battlenet').get()
    # Get all characters
    full_character_list_from_api = get_oauth_character_names(AccessToken.token)
    # build a list from the api of character|realm
    # get a list of this users toons from the db
    # dedupe
    #differences = [x for x in dev_guids if x not in prd_guids]
    # Insert records for new characters that are in the api pull that aren't in the db
    # Leave old characters for users to deactivate
    """
    new_character = form.save(commit=False)
    new_character.character_owner = request.user
    character_name = request.POST['character_name']
    new_character.character_name = character_name.title()
    new_character.character_realm = Realms.objects.get(pk=request.POST['character_realm'])
    # API TRY
    server_name = Realms.objects.get(id=request.POST['character_realm'])
    character_info = get_character_api_information(request.POST['character_name'], server_name.realm_name)
    # END API TRY
    class_id = Classes.objects.get(blizzard_class_id=character_info['class_id'])
    faction_id = Factions.objects.get(faction_id=character_info['character_faction'])
    new_character.save()
    cdo = CharactersDetails(character_link_id=new_character.id)
    cdo.character_profile_avatar_url = character_info['avatar_image']
    cdo.character_profile_image_url = character_info['profile_image']
    cdo.character_profile_inset_url = character_info['inset_image']
    cdo.character_faction_id = faction_id.faction_id
    cdo.character_class_id = class_id.id
    cdo.character_race_id = character_info['race_id']
    cdo.character_level = character_info['level']
    cdo.character_armory_url_simple = character_info['armory_simple']
    cdo.character_armory_url_advanced = character_info['armory_advanced']
    cdo.save()
    return redirect('user-profile')
    """
    return render(request, 'players/add_character.html', {'account_characters': full_character_list_from_api, 'db_toons': full_character_list_from_db})


class UpdateCharacterProfile(UpdateView):
    model = Characters
    template_name = 'players/update_character_profile.html'
    fields = 'looking_for_guild', 'looking_for_guild_advertisement', 'main_role', 'alt_role'
    success_url = '/players/profile'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateCharacterProfile, self).get_context_data(**kwargs)
        ctx['character_profile_object'] = Characters.objects.get(id=self.kwargs['pk'])
        return ctx


def DeleteCharacter(request, pk):
    Characters.objects.get(pk=pk).delete()
    return redirect('/players/profile')
