# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-24 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0004_auto_20170424_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swimmingresult',
            name='house',
        ),
    ]
