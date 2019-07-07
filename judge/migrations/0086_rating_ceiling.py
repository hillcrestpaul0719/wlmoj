# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-20 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0086_external_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='rating_ceiling',
            field=models.IntegerField(blank=True, help_text='Rating ceiling for contest', null=True, verbose_name='rating ceiling'),
        ),
        migrations.AddField(
            model_name='contest',
            name='rating_floor',
            field=models.IntegerField(blank=True, help_text='Rating floor for contest', null=True, verbose_name='rating floor'),
        ),
    ]
