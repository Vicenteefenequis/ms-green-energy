from rest_framework import serializers

from core_apps.energy_converter.model.LocationStation import LocationStation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationStation
        fields = ["nome_usina", "latitude", "longitude", "city", "state", "average_photovoltaic_irradiation"]
