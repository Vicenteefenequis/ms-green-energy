from django.db import models
from django.contrib.auth import get_user_model

from core_apps.cities.models import City
from core_apps.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

User = get_user_model()



class Project(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects"
    )

    city = models.OneToOneField(
        City, on_delete=models.CASCADE, related_name="projects"
    )
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.name
