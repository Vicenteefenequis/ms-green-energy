from core_apps.common.models import TimeStampedModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(TimeStampedModel):
    name = models.CharField(max_length=50, blank=False,
                            null=False, unique=True)
    population = models.IntegerField()
    type = models.CharField(max_length=1, default="C")
    acronym = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return f'Project from {self.name}'
