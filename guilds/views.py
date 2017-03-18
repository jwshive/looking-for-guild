from .models import Guilds
from django.views.generic import ListView, CreateView


class GuildList(ListView):
    model = Guilds
    template_name = 'guilds/guilds.html'


class CreateGuild(CreateView):
    model = Guilds
    fields = ['guild_name', 'guild_realm', 'guild_level', 'guild_faction']
