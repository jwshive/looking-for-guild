from django.conf.urls import url
from .views import RealmsList, CharactersList, ClassesList, FactionsList, RacesList, MyProfile


urlpatterns = [
    url(r'^realms/', RealmsList.as_view(), name='realms-list'),
    url(r'^characters/', CharactersList.as_view(), name='characters-list'),
    url(r'^classes/', ClassesList.as_view(), name='classes-list'),
    url(r'^factions/', FactionsList.as_view(), name='factions-list'),
    url(r'^races/', RacesList.as_view(), name='races-list'),
    url(r'^profile/', MyProfile, name='user-profile'),
]

