from django.conf.urls import url
from .views import MyProfile, CreateCharacter, CharacterDetail, UpdateCharacterProfile
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add_character', login_required(CreateCharacter), name='add-character'),
    url(r'^profile/', login_required(MyProfile), name='user-profile'),
    url(r'^character_details/(?P<character_realm>[^/]+)/(?P<character_name>[^/]+)', CharacterDetail, name='character-details'),
    url(r'^update_character_details/(?P<pk>[^/]+)', login_required(UpdateCharacterProfile.as_view()), name='update-character-details'),
]

