from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Indicator, User


class IndicatorAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "total_number_of_interruptions",
        "total_residential_electricity_use",
        "number_of_people_with_regular_connection",
        "total_electricity_consumption_in_public_buildings",
        "total_area_of_these_buildings",
        "total_electricity_consumption_produced_from_renewable",
        "total_energy_consumption",
        "total_electricity_use",
        "total_number_of_consumer_interruptions",
        "total_number_of_consumers_served",
        "sum_of_the_duration_of_all_interruptions",
        "total_number_of_interruptions",
        "population",
        "city",
    ]


admin.site.register(Indicator, IndicatorAdmin)
