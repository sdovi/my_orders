# Generated by Django 4.1 on 2024-03-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscription_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='subscription_start',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]