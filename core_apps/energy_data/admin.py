from django.contrib import admin
from .models import DataEnergetic


class DataEnergeticAdmin(admin.ModelAdmin):
    list_display = [
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
    ]

admin.site.register(DataEnergetic, DataEnergeticAdmin)
