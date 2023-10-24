from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LocationsStations",
            fields=[
                (
                    "pkid", models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("latitude", models.CharField(max_length=50)),
                ("longitude", models.CharField(max_length=50)),
                ("nome_usina", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "locations_stations",
                "verbose_name_plural": "locations_stations",
            },
        ),
    ]


class LocationsStations(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    nome_usina = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        verbose_name = "locations_station"
        verbose_name_plural = "locations_stations"
