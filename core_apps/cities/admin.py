from django.contrib import admin
from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "population",
        "is_certified"
    ]

    list_display_links = ["name", "population", "is_certified"]


admin.site.register(City, CityAdmin)
