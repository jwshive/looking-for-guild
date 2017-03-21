# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:56
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0015_auto_20170321_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guilds',
            name='guild_slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=('guild_realm.realm_name', 'guild_name', 'guild_faction.faction_name'), unique=True),
        ),
    ]
