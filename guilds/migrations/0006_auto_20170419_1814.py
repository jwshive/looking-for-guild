# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0005_auto_20170419_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guildmanagers',
            old_name='guild_managers',
            new_name='guild_manager',
        ),
    ]
