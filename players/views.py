from .models import Realms, Characters, Factions, Races, Profile
from guilds.models import Guilds, RecruitmentPosts
from django.views.generic import ListView, DetailView, CreateView
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
            'my_profile': User.objects.filter(username=current_user)
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