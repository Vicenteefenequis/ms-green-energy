from django.contrib import admin

from .models import DataEnergetic, Project


class ProjectsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectsAdmin)


class DataEnergeticAdmin(admin.ModelAdmin):
    pass


admin.site.register(DataEnergetic, DataEnergeticAdmin)
