# Generated by Django 4.1.7 on 2023-11-07 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0009_alter_location_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="data_energetic",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="locations",
                to="projects.dataenergetic",
            ),
        ),
    ]