from django.conf.urls import url
from .views import MyProfile, CreateCharacter, UpdateMyProfile, CharacterDetail, UpdateCharacterProfile, DeleteCharacter
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add_character/(?P<character_owner>[^/]+)', login_required(CreateCharacter), name='add-character'),
    url(r'^profile/', login_required(MyProfile), name='user-profile'),
    url(r'^update_profile/(?P<pk>[^/]+)', login_required(UpdateMyProfile.as_view()), name='update-profile'),
    url(r'^character_details/(?P<pk>[^/]+)', login_required(CharacterDetail), name='character-details'),
    url(r'^update_character_details/(?P<pk>[^/]+)', login_required(UpdateCharacterProfile.as_view()), name='update-character-details'),
    url(r'^delete_character/(?P<pk>[^/]+)', login_required(DeleteCharacter), name='delete-character'),
]

