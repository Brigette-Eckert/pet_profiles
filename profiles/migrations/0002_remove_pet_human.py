# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 03:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='human',
        ),
    ]
