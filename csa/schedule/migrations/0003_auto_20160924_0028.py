# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0001_initial'),
        ('schedule', '0002_auto_20160923_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='teams',
        ),
        migrations.AddField(
            model_name='group',
            name='participates',
            field=models.ManyToManyField(to='championship.Participation', verbose_name='participates'),
        ),
    ]
