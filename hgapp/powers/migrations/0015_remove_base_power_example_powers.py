# Generated by Django 2.2.12 on 2020-08-02 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('powers', '0014_auto_20200731_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='base_power',
            name='example_powers',
        ),
    ]
