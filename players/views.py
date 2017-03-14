from .models import Realms, Characters, Classes, Factions, Races
from django.views.generic import ListView


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

