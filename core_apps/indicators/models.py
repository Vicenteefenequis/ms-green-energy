from django.db import models

from core_apps.common.models import TimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Indicator(TimeStampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="indicators"
    )
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
    population = models.FloatField()
    city = models.CharField(
        max_length=50, default="Goiânia", blank=False, null=False
    )
    is_certified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Indicator:{self.city}"
