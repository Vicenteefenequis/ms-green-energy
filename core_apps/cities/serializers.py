from rest_framework import serializers

from core_apps.cities.models import City


class CitySerializer(serializers.ModelSerializer):
    is_certified = serializers.BooleanField(read_only=True)

    class Meta:
        model = City
        fields = ["name", "population", "is_certified"]
