# Generated by Django 4.1.7 on 2023-10-19 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataEnergetic",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("total_residential_electricity_use", models.FloatField()),
                ("number_of_people_with_regular_connection", models.FloatField()),
                (
                    "total_electricity_consumption_in_public_buildings",
                    models.FloatField(),
                ),
                ("total_area_of_these_buildings", models.FloatField()),
                (
                    "total_electricity_consumption_produced_from_renewable",
                    models.FloatField(),
                ),
                ("total_energy_consumption", models.FloatField()),
                ("total_electricity_use", models.FloatField()),
                ("total_number_of_consumer_interruptions", models.FloatField()),
                ("total_number_of_consumers_served", models.FloatField()),
                ("sum_of_the_duration_of_all_interruptions", models.FloatField()),
                ("total_number_of_interruptions", models.FloatField()),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=50)),
                ("population", models.IntegerField()),
                ("is_certified", models.BooleanField(default=False)),
                ("type", models.CharField(max_length=1)),
            ],
            options={
                "verbose_name": "location",
                "verbose_name_plural": "locations",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="user",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="data_energetic",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="projects.dataenergetic",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="location",
            field=models.OneToOneField(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="projects.location",
            ),
            preserve_default=False,
        ),
    ]
