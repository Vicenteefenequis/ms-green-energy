# Generated by Django 4.1.7 on 2023-10-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("energy_converter", "0005_locationstation_average_photovoltaic_irradiation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="locationstation",
            name="average_photovoltaic_irradiation",
            field=models.FloatField(default=0.0, verbose_name="Media por ano KhW"),
        ),
    ]
