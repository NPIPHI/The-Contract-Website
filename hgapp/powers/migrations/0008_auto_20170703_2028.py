# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-03 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('powers', '0007_auto_20170703_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='power_full',
            options={'permissions': (('view_power_full', 'View power full'), ('edit_power_full', 'Edit power full'))},
        ),
    ]