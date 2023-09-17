from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StatesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.states"
    verbose_name = _("States")
