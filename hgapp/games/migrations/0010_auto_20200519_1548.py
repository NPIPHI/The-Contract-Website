# Generated by Django 2.2.12 on 2020-05-19 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_auto_20171213_0657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'permissions': (('edit_game', 'Edit game'),)},
        ),
        migrations.AlterModelOptions(
            name='scenario',
            options={'permissions': (('edit_scenario', 'Edit scenario'),)},
        ),
        migrations.AlterField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.Scenario'),
        ),
        migrations.AlterField(
            model_name='game_attendance',
            name='attending_character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='game_attendance',
            name='relevant_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.Game'),
        ),
        migrations.AlterField(
            model_name='game_invite',
            name='invited_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game_invite',
            name='relevant_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.Game'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scenario_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='cycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='games.Cycle'),
        ),
    ]