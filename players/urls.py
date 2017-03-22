from django.conf.urls import url
from .views import RealmsList, CharactersList, FactionsList, RacesList, MyProfile, CreateCharacter
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add_character/(?P<character_owner>[^/]+)', login_required(CreateCharacter.as_view()), name='add-character'),
    url(r'^realms/', RealmsList.as_view(), name='realms-list'),
    url(r'^characters/', CharactersList.as_view(), name='characters-list'),
    url(r'^factions/', FactionsList.as_view(), name='factions-list'),
    url(r'^races/', RacesList.as_view(), name='races-list'),
    url(r'^profile/', MyProfile, name='user-profile'),
]

