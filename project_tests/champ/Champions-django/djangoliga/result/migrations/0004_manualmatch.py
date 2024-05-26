# Generated by Django 5.0.4 on 2024-04-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_rename_image_url_match_away_logo_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=50, verbose_name='время начинание матча')),
                ('one_name_command', models.CharField(max_length=255, verbose_name='название 1 команды (слева находяйщися)')),
                ('one_logo_command', models.URLField(verbose_name='логотип 1 команды')),
                ('two_name_command', models.CharField(max_length=255, verbose_name='название 2 команды (справа находяйщися)')),
                ('two_logo_command', models.URLField(verbose_name='логотип 2 команды')),
                ('game_id', models.CharField(max_length=100, unique=True)),
                ('home_goals', models.CharField(default='-', max_length=10, verbose_name='гол 1 команды')),
                ('away_goals', models.CharField(default='-', max_length=10, verbose_name='гол 2 команды')),
                ('stage', models.CharField(max_length=100, verbose_name='Номер турнира')),
            ],
        ),
    ]