from rest_framework import serializers

from .models import DataEnergetic, Location, Project
from core_apps.locations.serializers import LocationSerializer


class DataEnergeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEnergetic
        fields = [
            "id",
            "total_residential_electricity_use",
            "number_of_people_with_regular_connection",
            "total_electricity_consumption_in_public_buildings",
            "total_area_of_these_buildings",
            "total_electricity_consumption_produced_from_renewable",
            "total_energy_consumption",
            "total_electricity_use",
            "total_number_of_consumer_interruptions",
            "total_number_of_consumers_served",
            "sum_of_the_duration_of_all_interruptions",
            "total_number_of_interruptions",
        ]


class ProjectCreateSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
    )
    data_energetic = DataEnergeticSerializer()

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "location",
            "data_energetic"
        ]
        read_only_fields = ('user', )

    def create(self, validated_data):
        data_energetic_data = validated_data.pop('data_energetic')

        data_energetic_instance = DataEnergetic.objects.create(
            **data_energetic_data
        )

        user = self.context['request'].user
        project = Project.objects.create(
            user=user,
            data_energetic=data_energetic_instance,
            **validated_data
        )

        return project


class ProjectListSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(
        source='location.name', read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "location_name",
            "is_certified",
            "created_at",
            "updated_at"
        ]


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "name",
            "slug"
        ]
