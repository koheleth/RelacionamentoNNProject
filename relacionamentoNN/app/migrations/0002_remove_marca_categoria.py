# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-17 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='categoria',
        ),
    ]
