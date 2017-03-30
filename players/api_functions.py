from urllib.request import urlopen
import json
import codecs
from frontdoor.models import WebsiteAPISettings


def get_character_faction(character_name, server_name):
    server_name = server_name.replace('\'', '\\\'').replace(' ', '%20')

    api_settings = WebsiteAPISettings.objects.get(pk=1)

    api_pull_url = api_settings.wow_api_base_url + server_name + "/" + character_name + "?fields=" + api_settings.wow_api_character_url_fields + "&local=en_US&apikey=" + api_settings.wow_api_key
    print(api_pull_url)
    response = urlopen(api_pull_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    try:
        character_faction = data['faction']

        return {
            'character_faction': character_faction,
        }
    except KeyError:
        return False


def get_oauth_character_names(access_token):
    api_settings = WebsiteAPISettings.objects.get(pk=1)

    api_pull_url = api_settings.wow_oauth_user_profile_url + access_token

    response = urlopen(api_pull_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    characters = {}

    for result in data['characters']:
        new_dict = {'character_name': result['name'], 'character_realm': result['realm'], 'inset_image': api_settings.wow_api_character_image_base_url + result['thumbnail'].replace('avatar', 'inset')}
        characters[result['name']] = new_dict

    return characters


def get_oauth_character_information(access_token):

    api_settings = WebsiteAPISettings.objects.get(pk=1)

    api_pull_url = api_settings.wow_oauth_user_profile_url + access_token
    
    response = urlopen(api_pull_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    try:
        character_name = data['characters']['name']
        character_realm = data['characters']['realm']
        avatar_image = data['characters']['thumbnail']
        profile_image = avatar_image.replace('avatar', 'profilemain')
        inset_image = avatar_image.replace('avatar', 'inset')

        class_id = data['characters']['class']
        race_id = data['characters']['race']
        level = data['characters']['level']

        spec = data['characters']['spec']['name']
        spec_role = data['characters']['spec']['role']

        armory_simple = api_settings.wow_armory_base_url_simple % (server_name, character_name)
        armory_advanced = api_settings.wow_armory_base_url_advanced % (server_name, character_name)

        character_faction = get_character_faction(character_name, character_realm)

        return {
                'character_name': character_name,
                'character_realm': character_realm,
                'avatar_image': avatar_image or "",
                'profile_image': profile_image or "",
                'inset_image': inset_image or "",
                'class_id': class_id or "",
                'race_id': race_id or "",
                'level': level or "",
                'armory_simple': armory_simple or "",
                'armory_advanced': armory_advanced or "",
                'character_faction': character_faction,
                'spec': spec,
                'spec_role': spec_role,
                'api_pull_url': api_pull_url,
                }
    except KeyError:
        return False
