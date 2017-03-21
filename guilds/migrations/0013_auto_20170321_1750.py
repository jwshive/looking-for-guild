# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:50
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0012_auto_20170321_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guilds',
            options={'managed': True, 'ordering': ['guild_realm'], 'verbose_name_plural': 'Player Guilds'},
        ),
        migrations.AddField(
            model_name='guilds',
            name='guild_slug',
            field=autoslug.fields.AutoSlugField(default=0, editable=False, populate_from=('guild_realm', 'realm_name')),
            preserve_default=False,
        ),
    ]
