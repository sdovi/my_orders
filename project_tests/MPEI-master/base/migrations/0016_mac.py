# Generated by Django 4.1.3 on 2023-06-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_faqs'),
    ]

    operations = [
        migrations.CreateModel(
            name='mac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('photo', models.FileField(upload_to='img')),
            ],
            options={
                'verbose_name': 'фото каруселя',
                'verbose_name_plural': 'фото каруселей',
            },
        ),
    ]
