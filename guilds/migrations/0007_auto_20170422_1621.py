# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guilds', '0006_auto_20170419_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaidDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raid_day', models.CharField(choices=[('NONE', 'No Days Specified'), ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], default='NONE', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Raid Day Listing',
                'db_table': 'raid_days',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RaidTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raid_start_time', models.DateTimeField()),
                ('raid_end_time', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Raid Time Listings',
                'db_table': 'raid_times',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='recruitmentposts',
            name='raid_days',
            field=models.ManyToManyField(blank=True, null=True, to='guilds.RaidDays'),
        ),
        migrations.AddField(
            model_name='recruitmentposts',
            name='raid_end_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RaidEndTime', to='guilds.RaidTimes'),
        ),
        migrations.AddField(
            model_name='recruitmentposts',
            name='raid_start_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RaidStartTime', to='guilds.RaidTimes'),
        ),
    ]