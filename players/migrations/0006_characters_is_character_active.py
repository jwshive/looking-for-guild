# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20170330_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='characters',
            name='is_character_active',
            field=models.BooleanField(default=True),
        ),
    ]