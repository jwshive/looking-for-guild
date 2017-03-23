key = "&apikey=8cbxb9ejytju6w4tu5bxnnjq8xnyfgv7"
secret = "KAXcy2drj9ButU6YpFM4dBTQVp5sJGZC"
stat_fields = "?fields=items,stats&local=en_US"

url = "https://us.api.battle.net/wow/character/"



for info in character_and_server:
    server_name = info.split('|')[1].replace('\'', '\\\'')
    character_name = info.split('|')[0]
    toon_url = url + server_name.replace('\'', '\\\'').replace(' ', '%20') + "/" + character_name + stat_fields + key

    #  response = urllib2.urlopen(toon_url)
    #  data = json.load(response)
    response = urlopen(toon_url)
    reader = codecs.getreader('utf-8')
    data = json.load(reader(response))

    # GEAR

    iLevel = data['items']['averageItemLevel']
    iLevelEquipped = data['items']['averageItemLevelEquipped']
    head = data['items']['head']['name']
    neck = data['items']['neck']['name']
    shoulder = data['items']['shoulder']['name']
    back = data['items']['back']['name']
    chest = data['items']['chest']['name']
    wrist = data['items']['wrist']['name']
    hands = data['items']['hands']['name']
    waist = data['items']['waist']['name']
    legs = data['items']['legs']['name']
    feet = data['items']['feet']['name']
    finger1 = data['items']['finger1']['name']
    finger2 = data['items']['finger2']['name']
    trinket1 = data['items']['trinket1']['name']
    trinket2 = data['items']['trinket2']['name']
    mainHand = data['items']['mainHand']['name']
    offHand = data['items']['offHand']['name'] if 'offhand' in data['items'] else "No Offhand Item."

    # STATS
    character_class = data['class']
    faction = data['faction']
    level = data['level']
    agility = data['stats']['agi']
    armor = data['stats']['armor']
    block = data['stats']['block']
    critical_strike = data['stats']['crit']
    dodge = data['stats']['dodge']
    haste = data['stats']['haste']
    health = data['stats']['health']
    intellect = data['stats']['int']
    leech = data['stats']['leech']
    mastery = data['stats']['mastery']
    parry = data['stats']['parry']
    power = data['stats']['power']
    stamina = data['stats']['sta']
    strength = data['stats']['str']
    versatility = data['stats']['versatility']

    #  print json.dumps(data, indent=4, sort_keys=True)
    # DB STUFF
    sql = """INSERT INTO characters (character_name,character_realm,character_class,character_level,character_faction,character_ilevel,character_ilevel_equipped,character_head,character_neck,character_shoulder,character_back,character_chest,character_wrist,character_hands,character_waist,character_legs,character_feet,character_finger1,character_finger2,character_trinket1,character_trinket2,character_mainHand,character_offHand,character_agility,character_armor,character_block,character_critical_strike,character_dodge,character_haste,character_health,character_intellect,character_leech,character_mastery,character_parry,character_power,character_stamina,character_strength,character_versatility,load_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

    cursor.execute(sql, (character_name.lower(), server_name.lower(), character_class, level, faction, iLevel, iLevelEquipped, head, neck, shoulder, back,
    chest, wrist, hands, waist, legs, feet, finger1, finger2, trinket1, trinket2, mainHand, offHand, agility, armor,
    block, critical_strike, dodge, haste, health, intellect, leech, mastery, parry, power, stamina, strength,
    versatility, today))
    conn.commit()
conn.close()
