from django.conf.urls import url
from .views import GuildList


urlpatterns = [
    url(r'^$', GuildList.as_view(), name='guild-list'),
]

