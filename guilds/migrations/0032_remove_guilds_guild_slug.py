# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0031_auto_20170321_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guilds',
            name='guild_slug',
        ),
    ]