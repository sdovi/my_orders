# Generated by Django 5.0.4 on 2024-05-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Главный текст  ')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Статьи',
                'verbose_name_plural': 'Статья',
            },
        ),
        migrations.AlterField(
            model_name='info_email',
            name='description',
            field=models.TextField(blank=True, default='Нету комента', verbose_name='Коментарии'),
        ),
        migrations.AlterField(
            model_name='info_email',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Емаил  '),
        ),
    ]
