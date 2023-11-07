from django.db import models
from django.contrib.auth import get_user_model
from core_apps.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class DataEnergetic(TimeStampedModel):
    total_residential_electricity_use = models.FloatField()
    number_of_people_with_regular_connection = models.FloatField()
    total_electricity_consumption_in_public_buildings = models.FloatField()
    total_area_of_these_buildings = models.FloatField()
    total_electricity_consumption_produced_from_renewable = models.FloatField()
    total_energy_consumption = models.FloatField()
    total_electricity_use = models.FloatField()
    total_number_of_consumer_interruptions = models.FloatField()
    total_number_of_consumers_served = models.FloatField()
    sum_of_the_duration_of_all_interruptions = models.FloatField()
    total_number_of_interruptions = models.FloatField()


class Location(TimeStampedModel):
    name = models.CharField(max_length=50, blank=False,
                            null=False, unique=True)
    population = models.IntegerField()
    is_certified = models.BooleanField(default=False)
    type = models.CharField(max_length=1, default="C")
    slug = models.CharField(max_length=255, blank=True, default="S/N")
    data_energetic = models.OneToOneField(
        DataEnergetic, on_delete=models.CASCADE, related_name="locations", blank=True, null=True
    )

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects"
    )

    location = models.OneToOneField(
        Location, on_delete=models.CASCADE, related_name="projects"
    )
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.name
