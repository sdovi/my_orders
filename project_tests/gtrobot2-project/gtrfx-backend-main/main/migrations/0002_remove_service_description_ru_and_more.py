# Generated by Django 4.1 on 2024-03-27 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='service',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='service',
            name='name_uz',
        ),
    ]