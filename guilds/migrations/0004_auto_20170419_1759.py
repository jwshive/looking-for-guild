# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0003_guildmanagers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guildmanagers',
            name='guild_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guilds.Guilds'),
        ),
    ]
