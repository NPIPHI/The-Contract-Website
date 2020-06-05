# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20171212_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='relevant_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='relevant_power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relevant_power', to='powers.Power'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='rewarded_character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character'),
        ),
    ]