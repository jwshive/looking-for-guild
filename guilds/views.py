from .models import Guilds
from django.views.generic import ListView


class GuildList(ListView):
    model = Guilds
    template_name = 'guilds/guilds.html'