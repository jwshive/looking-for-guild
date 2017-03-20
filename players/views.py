from .models import Realms, Characters, Classes, Factions, Races, Profile
from guilds.models import Guilds, RecruitmentPosts
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class RealmsList(ListView):
    model = Realms
    template_name = 'players/realms.html'


class CharactersList(ListView):
    model = Characters
    template_name = 'players/characters.html'


class ClassesList(ListView):
    model = Classes
    template_name = 'players/classes.html'


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
            'my_profile': Profile.objects.filter(user=current_user)
            }
    return render(request, 'players/profile.html', context)
