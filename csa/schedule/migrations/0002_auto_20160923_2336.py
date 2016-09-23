# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0001_initial'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='teams',
            field=models.ManyToManyField(to='championship.Team', verbose_name='teams'),
        ),
        migrations.AlterField(
            model_name='group',
            name='championship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.Championship', verbose_name='championship'),
        ),
    ]
