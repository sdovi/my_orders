# Generated by Django 4.1.3 on 2022-12-01 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ads_area_ads_area_en_ads_area_oz_ads_area_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addetail',
            name='ad_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.ads', verbose_name='Ad'),
        ),
    ]
