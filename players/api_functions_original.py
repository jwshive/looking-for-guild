from urllib.request import urlopen
from allauth.socialaccount.models import SocialToken
import json
import codecs
from frontdoor.models import WebsiteAPISettings


def get_character_api_information(character_name, server_name):
    server_name = server_name.replace('\'', '\\\'').replace(' ', '%20')

    api_settings = WebsiteAPISettings.objects.get(pk=1)

    api_pull_url = api_settings.wow_api_base_url + server_name + "/" + character_name + "?fields=" + api_settings.wow_api_character_url_fields + "&local=en_US&apikey=" + api_settings.wow_api_key
    print(api_pull_url)
    response = urlopen(api_pull_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    try:
        avatar_image = data['thumbnail']
        profile_image = avatar_image.replace('avatar', 'profilemain')
        inset_image = avatar_image.replace('avatar', 'inset')

        class_id = data['class']
        race_id = data['race']
        level = data['level']

        armory_simple = api_settings.wow_armory_base_url_simple % (server_name, character_name)
        armory_advanced = api_settings.wow_armory_base_url_advanced % (server_name, character_name)

        character_faction = data['faction']

        return {
            'avatar_image': avatar_image or "",
            'profile_image': profile_image or "",
            'inset_image': inset_image or "",
            'class_id': class_id or "",
            'race_id': race_id or "",
            'level': level or "",
            'armory_simple': armory_simple or "",
            'armory_advanced': armory_advanced or "",
            'character_faction': character_faction,
            'api_pull_url': api_pull_url,
        }
    except KeyError:
        return False


def get_oauth_character_information(access_token, battlenet_id):
    access_token = SocialToken.objects.filter(account__user=user, account__provider='battlenet').get()
    api_pull_url = api_settings.wow_oauth_user_profile_url + access_token.token
    
    response = urlopen(api_pull_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    try:



