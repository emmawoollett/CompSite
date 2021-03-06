# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-03 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompApp', '0014_auto_20170703_1149'),
        ('StudentApp', '0003_auto_20170501_0908'),
        ('ResultApp', '0011_auto_20170703_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldEventRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('distance', models.FloatField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_record', to='CompApp.FieldEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackEventRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DurationField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_record', to='CompApp.TrackEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackRelayRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DurationField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_relay_record', to='CompApp.TrackRelay')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_track_relay_record', to='StudentApp.House')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
