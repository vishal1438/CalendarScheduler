# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-24 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_event_invites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='invites',
        ),
    ]
