# Generated by Django 4.1.3 on 2022-12-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_scientificcouncil_about_scientificcouncil_about_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpeiuzleaders',
            name='some_text',
            field=models.CharField(max_length=255, null=True, verbose_name='Some text'),
        ),
        migrations.AddField(
            model_name='mpeiuzleaders',
            name='some_text_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Some text'),
        ),
        migrations.AddField(
            model_name='mpeiuzleaders',
            name='some_text_oz',
            field=models.CharField(max_length=255, null=True, verbose_name='Some text'),
        ),
        migrations.AddField(
            model_name='mpeiuzleaders',
            name='some_text_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Some text'),
        ),
        migrations.AddField(
            model_name='mpeiuzleaders',
            name='some_text_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Some text'),
        ),
    ]
