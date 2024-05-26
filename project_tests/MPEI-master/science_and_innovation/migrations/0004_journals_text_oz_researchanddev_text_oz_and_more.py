# Generated by Django 4.1.3 on 2022-11-27 11:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('science_and_innovation', '0003_rename_eduprogram_scientinfrastructure'),
    ]

    operations = [
        migrations.AddField(
            model_name='journals',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='researchanddev',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='scienteventdetail',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='scientevents',
            name='name_oz',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='scientificcert',
            name='name_oz',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='scientinfrastructure',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
    ]