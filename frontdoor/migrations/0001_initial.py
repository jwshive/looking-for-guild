# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 16:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_subject', models.CharField(max_length=100)),
                ('feedback_body', models.TextField()),
                ('feedback_submitted_on', models.DateTimeField(auto_now_add=True)),
                ('feedback_read', models.BooleanField(default=False)),
                ('feedback_responded_to', models.BooleanField(default=False)),
                ('feedback_submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'feedback',
                'managed': True,
                'verbose_name_plural': 'User Feedback',
            },
        ),
        migrations.CreateModel(
            name='FrontDoorNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255)),
                ('news_content', models.TextField()),
                ('news_creation_date', models.DateTimeField(auto_now_add=True)),
                ('news_last_updated', models.DateTimeField(auto_now=True)),
                ('news_published', models.BooleanField(default=False)),
                ('news_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'front_door_news',
                'managed': True,
                'verbose_name_plural': 'Front Door News',
            },
        ),
        migrations.CreateModel(
            name='WebsiteAPISettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_settings_name', models.CharField(max_length=100)),
                ('wow_api_key', models.CharField(max_length=100)),
                ('wow_api_secret', models.CharField(max_length=100)),
                ('wow_api_character_url_fields', models.CharField(max_length=200)),
                ('wow_api_base_url', models.URLField()),
                ('wow_api_character_image_base_url', models.URLField()),
                ('wow_armory_base_url_simple', models.URLField()),
                ('wow_armory_base_url_advanced', models.URLField()),
            ],
            options={
                'db_table': 'website_api_settings',
                'managed': True,
                'verbose_name_plural': 'Website API Settings',
            },
        ),
    ]
