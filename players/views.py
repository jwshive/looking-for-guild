from .models import Realms, Characters, Factions, Races, Profile
from guilds.models import Guilds, RecruitmentPosts
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
            'my_profile': User.objects.select_related('profile').filter(username=current_user)
            }
    return render(request, 'players/profile.html', context)


class CreateCharacter(CreateView):
    model = Characters
    template_name = 'players/add_character.html'
    fields = 'character_name', 'character_realm', 'character_class', 'character_race', 'character_level', 'character_faction', 'character_armory_url'
    success_url = '/players/profile'
    
    def get_context_data(self, **kwargs):
        ctx = super(CreateCharacter, self).get_context_data(**kwargs)
        ctx['player_object'] = User.objects.filter(pk=self.kwargs['character_owner'])
        return ctx

    def form_valid(self, form):
        form.instance.character_owner_id = self.kwargs['character_owner']
        return super(CreateCharacter, self).form_valid(form) 
        

class UpdateMyProfile(UpdateView):
    model = Profile
    template_name = 'players/update_profile.html'
    fields = 'battle_net_id', 'user_timezone', 'looking_for_guild'
    success_url = '/players/profile'
    
    def get_context_data(self, **kwargs):
        ctx = super(UpdateMyProfile, self).get_context_data(**kwargs)
        ctx['profile_object'] = Profile.objects.filter(user_id=self.kwargs['pk'])
        return ctx

    def form_valid(self, form):
        form.instance.profile_id = self.kwargs['pk']
        return super(UpdateMyProfile, self).form_valid(form)         