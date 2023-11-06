from django.contrib import admin
from .models import State


class StateAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "population",
    ]

    list_display_links = ["name", "population"]


admin.site.register(State, StateAdmin)
