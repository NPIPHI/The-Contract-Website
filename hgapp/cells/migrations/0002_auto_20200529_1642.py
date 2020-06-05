# Generated by Django 2.2.12 on 2020-05-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cell',
            old_name='world_description',
            new_name='setting_description',
        ),
        migrations.RenameField(
            model_name='cell',
            old_name='world_name',
            new_name='setting_name',
        ),
        migrations.AddField(
            model_name='cell',
            name='name',
            field=models.CharField(default='name', max_length=200),
            preserve_default=False,
        ),
    ]