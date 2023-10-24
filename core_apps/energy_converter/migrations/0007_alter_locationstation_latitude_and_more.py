# Generated by Django 4.1.7 on 2023-10-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "energy_converter",
            "0006_alter_locationstation_average_photovoltaic_irradiation",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="locationstation",
            name="latitude",
            field=models.FloatField(default=0.0, verbose_name="Latitude"),
        ),
        migrations.AlterField(
            model_name="locationstation",
            name="longitude",
            field=models.FloatField(default=0.0, verbose_name="Longitude"),
        ),
    ]
