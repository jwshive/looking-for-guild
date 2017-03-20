from .models import Guilds
from django.views.generic import ListView, CreateView


class GuildList(ListView):
    model = Guilds
    template_name = 'guilds/guilds.html'
    ordering = ['is_recruiting']


class CreateGuild(CreateView):
    model = Guilds
    fields = ['guild_created_by', 'guild_name', 'guild_realm', 'guild_level', 'guild_faction']
