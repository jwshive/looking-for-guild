# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0033_remove_recruitmentposts_recruiting_classes'),
        ('players', '0016_auto_20170322_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characters',
            name='character_class',
        ),
        migrations.DeleteModel(
            name='Classes',
        ),
    ]