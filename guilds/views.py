from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from .forms import CreateGuildForm
from .models import Guilds, RecruitmentPosts, GuildManagers
from players.models import Realms, Factions
from players.api_functions import get_guild_information
from django.views.generic import ListView, CreateView, DetailView


class GuildList(ListView):
    model = Guilds
    queryset = Guilds.objects.filter(is_recruiting=True, is_active=True)
    template_name = 'guilds/guilds.html'
    ordering = ['guild_realm', 'is_recruiting']
    grouping = ['guild_realm']


def GuildDetail(request, guild_realm, guild_name):
    context = {'guild_info': Guilds.objects.filter(guild_name = guild_name).filter(guild_realm = Realms.objects.get(realm_name = guild_realm))}
    return render(request, 'guilds/guild_details.html', context)

    
class RecruitmentPostDetail(DetailView):
    model = RecruitmentPosts
    template_name = 'guilds/recruitment_post_details.html'
    
    
def CreateGuild(request):
    form = CreateGuildForm()

    if request.method == 'POST':
        form = CreateGuildForm(data=request.POST)
        if form.is_valid():
            guild_information_from_api = get_guild_information(request.POST['guild_name'], request.POST['guild_realm'])

            new_guild, created = Guilds.objects.get_or_create(
                    guild_name = guild_information_from_api['guild_name'],
                    guild_realm = Realms.objects.get(id=guild_information_from_api['guild_realm']),
                    guild_faction = Factions.objects.get(faction_id = guild_information_from_api['guild_faction']),
                    guild_created_by = User.objects.get(id=request.user.id),
                    )
            new_guild_manager = GuildManagers.objects.create(guild_id = Guilds.objects.get(id = new_guild.id))
            new_guild_manager.guild_manager.add(request.user.id)

            return redirect('user-profile')
        else:

            return render(request, 'guilds/add_guild.html', {'form': form})
            
    else:
        return render(request, 'guilds/add_guild.html', {'form': form})


    fields = ['guild_name', 'guild_realm', 'guild_faction']
    #fields = ['guild_name', 'guild_realm', 'guild_faction', 'guild_information', 'guild_battlenet_website', 'guild_external_website', 'guild_wow_progress_link', 'guild_warcraft_logs_link', 'guild_world_of_logs_link', 'is_recruiting']
    success_url = '/players/profile'

    def form_valid(self, form):
        form.instance.guild_created_by = self.request.user
        return super(CreateGuild, self).form_valid(form)   
        
        
class CreateRecruitmentPost(CreateView):
    model = RecruitmentPosts
    template_name = 'guilds/add_recruitment_post.html'
    fields = 'recruiting_levels', 'recruiting_classes', 'recruitment_title', 'raid_days', 'raid_start_time', 'raid_end_time', 'recruitment_post', 'is_post_active'
    success_url = '/players/profile'
    
    def get_context_data(self, **kwargs):
        ctx = super(CreateRecruitmentPost, self).get_context_data(**kwargs)
        ctx['guild_object'] = Guilds.objects.get(pk=self.kwargs['guild_pk'])
        return ctx

    def form_valid(self, form):
        form.instance.guild_name_id = self.kwargs['guild_pk']
        return super(CreateRecruitmentPost, self).form_valid(form) 
        
    
class UpdateGuildProfile(UpdateView):
    model = Guilds
    template_name = 'guilds/update_guild_profile.html'
    fields = 'guild_information', 'guild_battlenet_website', 'guild_external_website', 'guild_wow_progress_link', 'guild_warcraft_logs_link', 'guild_world_of_logs_link', 'is_recruiting'
    success_url = '/players/profile'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateGuildProfile, self).get_context_data(**kwargs)
        ctx['guild_profile_object'] = Guilds.objects.get(id=self.kwargs['pk'])
        return ctx


class UpdateRecruitmentPost(UpdateView):
    model = RecruitmentPosts
    template_name = 'guilds/update_recreuitment_post.html'
    fields = 'recruiting_levels', 'recruiting_classes', 'recruitment_title', 'recruitment_post', 'is_post_active'
    success_url = '/players/profile'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateRecruitmentPost, self).get_context_data(**kwargs)
        ctx['recruitment_post_object'] = RecruitmentPosts.objects.select_related('guild_name').get(id=self.kwargs['pk'])
        return ctx


@login_required()
def DeleteGuild(request,pk):
    Guilds.objects.get(id=pk).delete()
    return redirect('/players/profile')
