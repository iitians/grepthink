# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 02:09
from __future__ import unicode_literals

import teamwork.apps.profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('msg', models.CharField(max_length=500)),
                ('read', models.BooleanField(default=False)),
                ('url', models.CharField(default='', max_length=500)),
                ('slug', models.CharField(default='', max_length=20)),
                ('alertType', models.CharField(default='basic', max_length=30)),
            ],
            options={
                'verbose_name': 'Alert',
                'verbose_name_plural': 'Alerts',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='', max_length=255)),
                ('start_time_hour', models.SmallIntegerField()),
                ('start_time_min', models.SmallIntegerField()),
                ('end_time_hour', models.SmallIntegerField()),
                ('end_time_min', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ('day',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('name', models.TextField(blank=True, max_length=75)),
                ('institution', models.TextField(blank=True, max_length=100)),
                ('location', models.TextField(blank=True, max_length=100)),
                ('jsonavail', models.TextField(default='[]')),
                ('avatar', models.ImageField(blank=True, default='', null=True, upload_to='avatars/%Y/%m/%d/', validators=[teamwork.apps.profiles.models.validate_image])),
                ('isProf', models.BooleanField(default=False)),
                ('isGT', models.BooleanField(default=False)),
                ('isTa', models.BooleanField(default=False)),
                ('avail', models.ManyToManyField(to='profiles.Events')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ('skill',),
            },
        ),
    ]
