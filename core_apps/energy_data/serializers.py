
from rest_framework import serializers

from core_apps.energy_data.models import DataEnergetic


class DataEnergeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEnergetic
        fields = "__all__"