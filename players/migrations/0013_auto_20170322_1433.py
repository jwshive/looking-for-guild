# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0012_auto_20170322_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_id',
            field=models.IntegerField(),
        ),
    ]
