# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-20 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='username',
            field=models.TextField(default='admin'),
        ),
    ]
