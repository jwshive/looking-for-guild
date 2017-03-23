from .models import Realms, Characters, Factions, Races, Profile, CharactersDetails, Classes
from guilds.models import Guilds, RecruitmentPosts
from frontdoor.models import WebsiteAPISettings
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from players.forms import AddCharacterForm


class RealmsList(ListView):
    model = Realms
    template_name = 'players/realms.html'


class CharactersList(ListView):
    model = Characters
    template_name = 'players/characters.html'


class FactionsList(ListView):
    model = Factions
    template_name = 'players/factions.html'


class RacesList(ListView):
    model = Races
    template_name = 'players/races.html'


@login_required
def MyProfile(request):
    current_user = request.user
    context = {
            'my_guilds': Guilds.objects.filter(guild_created_by=current_user), 
            'my_characters': Characters.objects.filter(character_owner=current_user),
            'my_profile': User.objects.select_related('profile').get(username=current_user),
            }
    return render(request, 'players/profile.html', context)
    
@login_required
def CharacterDetail(request, pk):
    context = {
        'site_settings': WebsiteAPISettings.objects.all().get(),
        'character_info': CharactersDetails.objects.select_related('character_link').get(character_link_id=pk)
    }
    return render(request, 'players/character_detail.html', context)

@login_required
def CreateCharacter(request, character_owner):
    if request.method == "POST":
        form = AddCharacterForm(request.POST)
        if form.is_valid():
            new_character = form.save(commit=False)
            new_character.character_owner = request.user
            new_character.character_name = request.POST['character_name']
            new_character.character_realm = Realms.objects.get(pk=request.POST['character_realm'])
            new_character.character_faction = Factions.objects.get(pk=request.POST['character_faction'])
            new_character.save()
            cdo = CharactersDetails(character_link_id=new_character.id)
            cdo.save()
            return redirect('user-profile')
    else:
        form = AddCharacterForm()
    return render(request, 'players/add_character.html', {'form': form})
        

class UpdateMyProfile(UpdateView):
    model = Profile
    template_name = 'players/update_profile.html'
    fields = 'battle_net_id', 'user_timezone', 'biography'
    success_url = '/players/profile'
    
    def get_context_data(self, **kwargs):
        ctx = super(UpdateMyProfile, self).get_context_data(**kwargs)
        ctx['profile_object'] = Profile.objects.filter(user_id=self.kwargs['pk'])
        return ctx

    def form_valid(self, form):
        form.instance.profile_id = self.kwargs['pk']
        return super(UpdateMyProfile, self).form_valid(form)     
        
        
class UpdateCharacterProfile(UpdateView):
    model = CharactersDetails
    template_name = 'players/update_character_profile.html'
    fields = 'character_class', 'character_race', 'character_level', 'looking_for_guild', 'looking_for_guild_advertisement'
    success_url = '/players/profile'
  
    def get_context_data(self, **kwargs):
        ctx = super(UpdateCharacterProfile, self).get_context_data(**kwargs)
        ctx['character_profile_object'] = CharactersDetails.objects.select_related('character_link').get(id=self.kwargs['pk'])
        return ctx
