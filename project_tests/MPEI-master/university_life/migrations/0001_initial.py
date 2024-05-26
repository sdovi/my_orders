# Generated by Django 4.1.3 on 2022-11-28 13:30

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campus',
            },
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Culture',
                'verbose_name_plural': 'Culture',
            },
        ),
        migrations.CreateModel(
            name='HealthAndSport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Health and sport',
                'verbose_name_plural': 'Health and sport',
            },
        ),
        migrations.CreateModel(
            name='PsycoSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_oz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Psychological support at MPEI',
                'verbose_name_plural': 'Psychological support at MPEI',
            },
        ),
    ]