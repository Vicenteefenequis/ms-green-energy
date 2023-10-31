from django.contrib import admin

from .models import DataEnergetic, Location, Project


class ProjectsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectsAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)


class DataEnergeticAdmin(admin.ModelAdmin):
    pass


admin.site.register(DataEnergetic, DataEnergeticAdmin)
