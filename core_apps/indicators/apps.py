from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IndicatorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.indicators"
    verbose_name = _("Indicators")
