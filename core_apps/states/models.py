from django.db import models

from core_apps.energy_data.models import DataEnergetic


class State(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True, primary_key=True)
    acronym = models.CharField(max_length=2, blank=False, null=False, unique=True)
    population = models.IntegerField()
    data_energetic = models.OneToOneField(DataEnergetic, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "%s the state" % self.name
