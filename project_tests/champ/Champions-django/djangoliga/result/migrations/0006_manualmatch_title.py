# Generated by Django 5.0.4 on 2024-04-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_remove_manualmatch_game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualmatch',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='название турнира'),
            preserve_default=False,
        ),
    ]
