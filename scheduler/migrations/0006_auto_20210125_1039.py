# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-25 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_event_invites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='invites',
            field=models.CharField(default='admin', max_length=2000),
        ),
    ]
