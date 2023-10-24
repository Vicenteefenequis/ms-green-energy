from rest_framework import serializers

from core_apps.energy_converter.model.Location import Location


class Locations(serializers.ModelSerializer):
    latitude = serializers.CharField(source="latitude")
    longitude = serializers.CharField(source="longitude")
    city = serializers.CharField(source="city")
    state = serializers.CharField(source="state")

    class Meta:
        model = Location
        fields = [
            "nome_usina",
            "latitude",
            "longitude",
            "city",
            "state",
        ]

