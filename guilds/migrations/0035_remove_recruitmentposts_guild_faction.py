# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0034_recruitmentposts_recruiting_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruitmentposts',
            name='guild_faction',
        ),
    ]