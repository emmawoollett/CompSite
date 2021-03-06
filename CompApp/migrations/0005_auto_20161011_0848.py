# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-11 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('CompApp', '0004_auto_20160920_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crosscountry',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cross_country_events',
                                    to='CompApp.Competition'),
        ),
        migrations.AlterField(
            model_name='crosscountry',
            name='year_group',
            field=models.CharField(
                choices=[('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11')],
                default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='fieldevent',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_events',
                                    to='CompApp.Competition'),
        ),
        migrations.AlterField(
            model_name='fieldevent',
            name='year_group',
            field=models.CharField(
                choices=[('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11')],
                default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='swimming',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swimming_events',
                                    to='CompApp.Competition'),
        ),
        migrations.AlterField(
            model_name='swimming',
            name='year_group',
            field=models.CharField(
                choices=[('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11')],
                default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='swimmingrelay',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swimming_relay_events',
                                    to='CompApp.Competition'),
        ),
        migrations.AlterField(
            model_name='swimmingrelay',
            name='year_group',
            field=models.CharField(
                choices=[('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11')],
                default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='trackevent',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_events',
                                    to='CompApp.Competition'),
        ),
        migrations.AlterField(
            model_name='trackevent',
            name='year_group',
            field=models.CharField(
                choices=[('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11')],
                default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='trackrelay',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_relay_events',
                                    to='CompApp.Competition'),
        ),
        migrations.AlterField(
            model_name='trackrelay',
            name='year_group',
            field=models.CharField(
                choices=[('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11')],
                default=None, max_length=2),
        ),
    ]
