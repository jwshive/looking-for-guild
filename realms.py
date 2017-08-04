#!/usr/bin/env python
try:
    import urllib2
except ImportError:
    from urllib.request import urlopen
import json
import datetime
import codecs
import sys, os
import psycopg2
from urllib.parse import urlparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

key = "&apikey=k593nqk9ejznje2tev93ryaxkkhnxe3m"
secret = "ZMJk4TP7Xy6U2zZjC8xNjDMxCrw2tXr4"

realm = "/realm/status"
realm_fields = "?local=en_US"


postgresql_url = urlparse(os.environ["DATABASE_URL"])


url = "https://us.api.battle.net/wow"

url_string = url + realm + realm_fields + key

response = urlopen(url_string)
reader = codecs.getreader('utf-8')
data = json.load(reader(response))

conn = psycopg2.connect(
        database=postgresql_url.path[1:],
        user=postgresql_url.username,
        password=postgresql_url.password,
        host=postgresql_url.hostname,
        port=postgresql_url.port
        )

cur = conn.cursor()

today = datetime.datetime.now().strftime('%Y-%m-%d')

for info in data['realms']:
    realm_type = info['type']
    realm_population = info['population']
    realm_name = info['name'].replace('\'', '\\\'')
    realm_slug = info['slug'].replace('\'', '\\\'')
    realm_battlegroup = info['battlegroup']
    realm_locale = info['locale']
    realm_timezone = info['timezone']
    realm_connected_realms = ','.join(info['connected_realms'])

    sql = "INSERT INTO realms (realm_type, realm_population, realm_name, realm_slug, realm_battlegroup, realm_locale, realm_timezone, realm_connected_realms, load_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"

    cur.execute(sql, (realm_type, realm_population, realm_name, realm_slug, realm_battlegroup, realm_locale, realm_timezone, realm_connected_realms, today))
    conn.commit()

conn.close()

# Find some way to doing a first_seen and last_seen date field
