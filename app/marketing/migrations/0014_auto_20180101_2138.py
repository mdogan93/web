# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0013_slackuser_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackuser',
            name='last_unseen',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='slackuser',
            name='times_seen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='slackuser',
            name='times_unseen',
            field=models.IntegerField(default=0),
        ),
    ]
