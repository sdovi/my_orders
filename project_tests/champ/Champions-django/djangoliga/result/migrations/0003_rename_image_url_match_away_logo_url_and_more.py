# Generated by Django 5.0.4 on 2024-04-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_alter_match_game_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='image_url',
            new_name='away_logo_url',
        ),
        migrations.AddField(
            model_name='match',
            name='home_logo_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
