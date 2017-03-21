from django.conf.urls import url
from .views import GuildList, CreateGuild, GuildDetail, RecruitmentPostDetail


urlpatterns = [
    url(r'^$', GuildList.as_view(), name='guild-list'),
    url(r'^add_guild', CreateGuild.as_view(), name='add-guild'),
    url(r'^guild_detail/(?P<pk>[^/]+)', GuildDetail.as_view(), name = 'guild-detail'),
    url(r'^recruitment_post/(?P<pk>[^/]+)', RecruitmentPostDetail.as_view(), name = 'recruitment-post'),
]

