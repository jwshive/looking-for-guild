from .models import Guilds, RecruitmentPosts
from players.models import Classes
from django.views.generic import ListView, CreateView, DetailView


class GuildList(ListView):
    model = Guilds
    queryset = Guilds.objects.filter(is_recruiting=True, is_active=True)
    template_name = 'guilds/guilds.html'
    ordering = ['guild_realm', 'is_recruiting']
    grouping = ['guild_realm']


class GuildDetail(DetailView):
    model = Guilds
    template_name = 'guilds/guild_details.html'

    
class RecruitmentPostDetail(DetailView):
    model = RecruitmentPosts
    template_name = 'guilds/recruitment_post_details.html'
    
    
class CreateGuild(CreateView):
    model = Guilds
    template_name = 'guilds/add_guild.html'
    fields = ['guild_name', 'guild_realm', 'guild_faction', 'guild_information', 'guild_battlenet_website', 'guild_external_website', 'guild_wow_progress_link', 'guild_warcraft_logs_link', 'guild_world_of_logs_link', 'is_recruiting']
    success_url = '/'

    def form_valid(self, form):
        form.instance.guild_created_by = self.request.user
        return super(CreateGuild, self).form_valid(form)   
        
        
class CreateRecruitmentPost(CreateView):
    model = RecruitmentPosts
    template_name = 'guilds/add_recruitment_post.html'
    fields = 'guild_faction', 'recruiting_levels', 'recruiting_classes', 'recruitment_title', 'recruitment_post'
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        ctx = super(CreateRecruitmentPost, self).get_context_data(**kwargs)
        ctx['guild_object'] = Guilds.objects.filter(pk=self.kwargs['guild_pk'])
        return ctx

    def form_valid(self, form):
        form.instance.guild_name_id = self.kwargs['guild_pk']
        return super(CreateRecruitmentPost, self).form_valid(form) 
        
    
