from django.conf.urls import url
from .views import RealmsList, CharactersList, FactionsList, RacesList, MyProfile, CreateCharacter, UpdateMyProfile
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add_character/(?P<character_owner>[^/]+)', login_required(CreateCharacter.as_view()), name='add-character'),
    url(r'^profile/', MyProfile, name='user-profile'),
    url(r'^update_profile/(?P<pk>[^/]+)', login_required(UpdateMyProfile.as_view()), name='update-profile'),
]

