# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20170308_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='', upload_to='avatars/'),
        ),
    ]
