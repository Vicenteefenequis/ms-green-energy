# Generated by Django 4.1.7 on 2023-10-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0006_alter_location_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="slug",
            field=models.CharField(blank=True, default="S/N", max_length=255),
        ),
    ]
