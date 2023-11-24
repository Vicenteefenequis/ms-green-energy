from django.contrib import admin

from .models import Location


class LocationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationsAdmin)
