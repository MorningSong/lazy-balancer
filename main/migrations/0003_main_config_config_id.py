# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160709_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_config',
            name='config_id',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
