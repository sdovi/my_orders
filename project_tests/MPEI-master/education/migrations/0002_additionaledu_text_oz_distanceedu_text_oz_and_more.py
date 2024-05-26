# Generated by Django 4.1.3 on 2022-11-27 11:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaledu',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='distanceedu',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='eduprogram',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='empandinternship',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='name_oz',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='finalqua',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='group',
            name='name_oz',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='officialdocs',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='treresults',
            name='text_oz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text'),
        ),
    ]