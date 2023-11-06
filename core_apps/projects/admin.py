from django.contrib import admin

from .models import  Project


class ProjectsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectsAdmin)


