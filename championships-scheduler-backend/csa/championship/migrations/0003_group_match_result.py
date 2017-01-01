# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0002_auto_20160925_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1, verbose_name='name')),
                ('championship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='championship.Championship', verbose_name='championship')),
                ('participates', models.ManyToManyField(to='championship.Participation', verbose_name='participates')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team_home', models.BooleanField(default=True, verbose_name='first_team_home')),
                ('second_team_home', models.BooleanField(default=False, verbose_name='second_team_home')),
                ('first_team_goals', models.IntegerField(blank=True, null=True, verbose_name='first_team_goals')),
                ('second_team_goals', models.IntegerField(blank=True, null=True, verbose_name='second_team_goals')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.Championship', verbose_name='championship')),
                ('first_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_first_team', to='championship.Participation', verbose_name='first_team')),
                ('second_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_second_team', to='championship.Participation', verbose_name='second_team')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('won', models.IntegerField(default=0, verbose_name='won')),
                ('drawn', models.IntegerField(default=0, verbose_name='drawn')),
                ('lost', models.IntegerField(default=0, verbose_name='lost')),
                ('goals_scored', models.IntegerField(default=0, verbose_name='goals_scored')),
                ('goals_lost', models.IntegerField(default=0, verbose_name='goals_lost')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.Group', verbose_name='group')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.Participation', verbose_name='team')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
        ),
    ]