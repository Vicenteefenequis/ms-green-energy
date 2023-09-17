import uuid
from django.db import models

from core_apps.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class State(TimeStampedModel):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sigla = models.CharField(verbose_name=_("sigla"), max_length=2)
    nome = models.CharField(verbose_name=_("nome"), max_length=50)

    class Meta:
        verbose_name = _("state")
        verbose_name_plural = _("states")

    def __str__(self):
        return self.sigla
