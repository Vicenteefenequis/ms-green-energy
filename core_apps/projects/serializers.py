from rest_framework import serializers

from .models import DataEnergetic, Location, Project


class DataEnergeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEnergetic
        fields = [
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


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ProjectCreateSerializer(serializers.ModelSerializer):
    data_energetic = DataEnergeticSerializer()
    location = LocationSerializer()

    class Meta:
        model = Project
        fields = [
            "id",
            "created_at",
            "updated_at",
            "name",
            "description",
            "data_energetic",
            "location",
        ]
        read_only_fields = ('user', )

    def create(self, validated_data):
        data_energetic_data = validated_data.pop('data_energetic')
        location_data = validated_data.pop('location')

        # Create DataEnergetic and Location instances
        data_energetic_instance = DataEnergetic.objects.create(
            **data_energetic_data)
        location_instance = Location.objects.create(**location_data)

        # Get the user from the request and add it to the project data
        user = self.context['request'].user
        project = Project.objects.create(
            user=user, data_energetic=data_energetic_instance, location=location_instance, **validated_data)

        return project


class ProjectListSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(
        source='location.name', read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "created_at",
            "updated_at",
            "name",
            "description",
            "location_name",
        ]
