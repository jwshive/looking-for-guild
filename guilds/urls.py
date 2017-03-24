from django.conf.urls import url
from .views import GuildList, CreateGuild, GuildDetail, RecruitmentPostDetail, CreateRecruitmentPost, UpdateGuildProfile, UpdateRecruitmentPost
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', GuildList.as_view(), name='guild-list'),
    url(r'^add_guild/(?P<pk>[^/]+)', login_required(CreateGuild.as_view()), name='add-guild'),
    url(r'^guild_detail/(?P<pk>[^/]+)', login_required(GuildDetail.as_view()), name = 'guild-detail'),
    url(r'^add_recruitment_post/(?P<guild_pk>[^/]+)', login_required(CreateRecruitmentPost.as_view()), name='add-recruitment-post'),
    url(r'^recruitment_post/(?P<pk>[^/]+)', login_required(RecruitmentPostDetail.as_view()), name = 'recruitment-post'),
    url(r'^update_guild_profile/(?P<pk>[^/]+)', login_required(UpdateGuildProfile.as_view()), name='update-guild-profile'),
    url(r'^update_recruitment_post/(?P<pk>[^/]+)', login_required(UpdateRecruitmentPost.as_view()), name='update-recruitment-post'),
]
