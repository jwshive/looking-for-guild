from urllib.request import urlopen
import json
import codecs
from frontdoor.models import WebsiteAPISettings
from players.models import Realms


def get_character_faction(character_name, server_name):
    server_name = server_name.replace(' ', '%20')

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

    toon_names = []
    realm_names = []
    for result in data['characters']:
        toon_names.append(result['name'])
        realm_names.append(result['realm'])

    characters = list(zip(toon_names, realm_names))

    return characters

def get_full_character_information(toon_name, toon_realm):

    api_settings = WebsiteAPISettings.objects.get(pk=1)

    api_pull_url = api_settings.wow_api_base_url + toon_realm.replace(' ', '%20') + "/" + toon_name + "?fields=" + api_settings.wow_api_character_url_fields + "&local=en_US&apikey=" + api_settings.wow_api_key
    
    response = urlopen(api_pull_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    try:
        character_name = data['name']
        character_realm = data['realm']
        character_faction = data['faction']
        avatar_image = data['thumbnail']
        profile_image = avatar_image.replace('avatar', 'profilemain')
        inset_image = avatar_image.replace('avatar', 'inset')

        class_id = data['class']
        race_id = data['race']
        level = data['level']

        armory_simple = api_settings.wow_armory_base_url_simple % (toon_realm, toon_name)
        armory_advanced = api_settings.wow_armory_base_url_advanced % (toon_realm, toon_name)

        equipped_ilevel = data['items']['averageItemLevelEquipped']
        max_ilevel = data['items']['averageItemLevel']

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
                'equipped_ilevel': equipped_ilevel,
                'max_ilevel': max_ilevel,
                'api_pull_url': api_pull_url,
                }
    except KeyError:
        return api_pull_url, data


def get_guild_information(guild_name, guild_realm_id):

    guild_realm = Realms.objects.get(id=guild_realm_id)
    api_settings = WebsiteAPISettings.objects.get(pk=1)

    api_pull_url = api_settings.wow_api_base_url_guild + guild_realm.realm_name.lower().replace(' ', '%20') + "/" + guild_name.replace(' ', '%20') + "?locale=en_US&apikey=" + api_settings.wow_api_key

    response = urlopen(api_pull_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    try:
        guild_name = data['name']
        guild_realm = data['realm']
        guild_faction = data['side']

        return {
                'guild_name': guild_name,
                'guild_realm': guild_realm_id,
                'guild_faction': guild_faction,
                }


    except KeyError:
        return api_pull_url, data
