# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-26 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompApp', '0007_auto_20161011_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='crosscountry',
            name='slug',
            field=models.SlugField(default='event'),
        ),
        migrations.AddField(
            model_name='fieldevent',
            name='slug',
            field=models.SlugField(default='event'),
        ),
        migrations.AddField(
            model_name='swimming',
            name='slug',
            field=models.SlugField(default='event'),
        ),
        migrations.AddField(
            model_name='swimmingrelay',
            name='slug',
            field=models.SlugField(default='event'),
        ),
        migrations.AddField(
            model_name='trackevent',
            name='slug',
            field=models.SlugField(default='event'),
        ),
        migrations.AddField(
            model_name='trackrelay',
            name='slug',
            field=models.SlugField(default='event'),
        ),
    ]
