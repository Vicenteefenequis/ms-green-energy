from django.db import models

from core_apps.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Project(TimeStampedModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.name
