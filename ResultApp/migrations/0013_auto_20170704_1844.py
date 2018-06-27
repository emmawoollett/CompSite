# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-04 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0012_fieldeventrecord_trackeventrecord_trackrelayrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crosscountryresult',
            name='house_points',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fieldeventresult',
            name='house_points',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='swimmingrelayresult',
            name='house_points',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='swimmingresult',
            name='house_points',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trackeventresult',
            name='house_points',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='trackrelayresult',
            name='house_points',
            field=models.FloatField(),
        ),
    ]
