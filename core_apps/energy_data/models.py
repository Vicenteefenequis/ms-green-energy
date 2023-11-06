from django.db import models

from core_apps.common.models import TimeStampedModel

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
