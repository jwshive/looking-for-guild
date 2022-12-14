# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guilds', '0002_auto_20170331_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildManagers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guilds.Guilds', unique=True)),
                ('guild_managers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'guild_managers',
                'ordering': ['guild_id__guild_name'],
                'verbose_name_plural': 'Guild Managers',
                'managed': True,
            },
        ),
    ]
