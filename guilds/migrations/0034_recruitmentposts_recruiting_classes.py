# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0018_auto_20170322_1442'),
        ('guilds', '0033_remove_recruitmentposts_recruiting_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitmentposts',
            name='recruiting_classes',
            field=models.ManyToManyField(to='players.Classes'),
        ),
    ]
