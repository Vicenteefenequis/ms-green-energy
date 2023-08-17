from rest_framework import serializers
import logging

from core_apps.indicators.models import Indicator
from core_apps.profiles.serializers import ProfileSerializer

logger = logging.getLogger(__name__)


class IndicatorSerializer(serializers.ModelSerializer):
    total_residential_electricity_use_per_capita = serializers.SerializerMethodField()
    percentage_electricity_supply = serializers.SerializerMethodField()
    annual_energy_consumption_of_public_buildings = serializers.SerializerMethodField()
    percentage_of_electricity_renewable_sources = serializers.SerializerMethodField()
    total_electricity_use_per_capita = serializers.SerializerMethodField()
    average_number_of_power_outages_per_consumer_per_year = serializers.SerializerMethodField()
    average_duration_of_power_outages = serializers.SerializerMethodField()

    # USER_REGISTRANTION_DATA
    name = serializers.CharField(max_length=50, write_only=True)
    total_residential_electricity_use = serializers.FloatField(
        write_only=True
    )
    number_of_people_with_regular_connection = serializers.FloatField(
        write_only=True
    )
    total_electricity_consumption_in_public_buildings = serializers.FloatField(
        write_only=True
    )
    total_area_of_these_buildings = serializers.FloatField(
        write_only=True
    )
    total_electricity_consumption_produced_from_renewable = serializers.FloatField(
        write_only=True
    )
    total_energy_consumption = serializers.FloatField(
        write_only=True
    )

    total_electricity_use = serializers.FloatField(
        write_only=True
    )
    total_number_of_consumer_interruptions = serializers.FloatField(
        write_only=True
    )
    total_number_of_consumers_served = serializers.FloatField(
        write_only=True
    )
    sum_of_the_duration_of_all_interruptions = serializers.FloatField(
        write_only=True
    )
    total_number_of_interruptions = serializers.FloatField(
        write_only=True
    )
    population = serializers.FloatField(
        write_only=True
    )
    city = serializers.CharField(max_length=50, write_only=True)

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_total_residential_electricity_use_per_capita(self, obj):
        return obj.total_residential_electricity_use / obj.population

    def get_percentage_electricity_supply(self, obj):
        return obj.number_of_people_with_regular_connection / obj.population

    def get_annual_energy_consumption_of_public_buildings(self, obj):
        return obj.total_electricity_consumption_in_public_buildings / obj.total_area_of_these_buildings

    def get_percentage_of_electricity_renewable_sources(self, obj):
        return obj.total_electricity_consumption_produced_from_renewable / obj.total_energy_consumption

    def get_average_number_of_power_outages_per_consumer_per_year(self, obj):
        return obj.total_number_of_consumer_interruptions / obj.total_number_of_consumers_served

    def get_average_duration_of_power_outages(self, obj):
        return obj.sum_of_the_duration_of_all_interruptions / obj.total_number_of_interruptions

    def get_total_electricity_use_per_capita(self, obj):
        return obj.total_electricity_use / obj.population

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y, %H:%M:%S")
        return formatted_date

    def create(self, validated_data):
        indicator = Indicator.objects.create(**validated_data)
        return indicator

    class Meta:
        model = Indicator
        fields = [
            "id",
            "name",
            "total_residential_electricity_use_per_capita",
            "percentage_electricity_supply",
            "annual_energy_consumption_of_public_buildings",
            "percentage_of_electricity_renewable_sources",
            "total_electricity_use_per_capita",
            "average_number_of_power_outages_per_consumer_per_year",
            "average_duration_of_power_outages",
            "total_number_of_interruptions",
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
            "population",
            "city",
            "updated_at",
            "created_at",
        ]
