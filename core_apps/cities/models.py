from django.db import models

from core_apps.common.models import TimeStampedModel
from core_apps.energy_data.models import DataEnergetic


class City(TimeStampedModel):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    population = models.IntegerField()
    is_certified = models.BooleanField(default=False)
    data_energetic = models.OneToOneField(DataEnergetic, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s the city" % self.name
