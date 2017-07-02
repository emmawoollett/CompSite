# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-01 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_auto_20160928_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Boys'), ('F', 'Girls')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_group',
            field=models.CharField(choices=[('07', 'Year 7'), ('08', 'Year 8'), ('09', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11')], default=None, max_length=2),
        ),
    ]