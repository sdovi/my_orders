# Generated by Django 4.1.3 on 2022-12-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_receivedmessages_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introsection',
            name='some_text',
        ),
        migrations.RemoveField(
            model_name='introsection',
            name='some_text_en',
        ),
        migrations.RemoveField(
            model_name='introsection',
            name='some_text_oz',
        ),
        migrations.RemoveField(
            model_name='introsection',
            name='some_text_ru',
        ),
        migrations.RemoveField(
            model_name='introsection',
            name='some_text_uz',
        ),
        migrations.AddField(
            model_name='introsection',
            name='title2',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='introsection',
            name='title3',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='introsection',
            name='title4',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]
