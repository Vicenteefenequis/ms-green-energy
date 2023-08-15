from rest_framework import serializers
import logging

from core_apps.indicators.models import Indicator
from core_apps.profiles.serializers import ProfileSerializer

logger = logging.getLogger(__name__)


class IndicatorSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    total_residential_electricity_use_per_capita = serializers.SerializerMethodField()
    percentage_electricity_supply = serializers.SerializerMethodField()
    annual_energy_consumption_of_public_buildings = serializers.SerializerMethodField()
    percentage_of_electricity_renewable_sources = serializers.SerializerMethodField()
    total_electricity_use_per_capita = serializers.SerializerMethodField()
    average_number_of_power_outages_per_consumer_per_year = serializers.SerializerMethodField()
    average_duration_of_power_outages = serializers.SerializerMethodField()

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
            "total_residential_electricity_use_per_capita",
            "percentage_electricity_supply",
            "annual_energy_consumption_of_public_buildings",
            "percentage_of_electricity_renewable_sources",
            "total_electricity_use_per_capita",
            "average_number_of_power_outages_per_consumer_per_year",
            "average_duration_of_power_outages",
            "updated_at",
            "created_at",
        ]
