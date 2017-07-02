# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-01 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompApp', '0011_auto_20170501_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimming',
            name='stroke',
            field=models.CharField(choices=[('BS', 'Breaststroke'), ('BA', 'Backstroke'), ('FR', 'Freestyle'), ('OP', 'Open')], default='FR', max_length=2),
        ),
    ]