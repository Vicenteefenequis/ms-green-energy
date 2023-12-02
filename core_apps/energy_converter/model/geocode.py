from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    road = serializers.CharField(allow_blank=True, default='')
    suburb = serializers.CharField(allow_blank=True, default='')
    city = serializers.CharField(allow_null=True, required=False)
    town = serializers.CharField(allow_null=True, required=False)
    village = serializers.CharField(allow_null=True, required=False)
    municipality = serializers.CharField(allow_blank=True, default='')
    state_district = serializers.CharField(allow_blank=True, default='')
    state = serializers.CharField(allow_blank=True, default='')
    postcode = serializers.CharField(allow_blank=True, default='')
    country = serializers.CharField(allow_blank=True, default='')
    country_code = serializers.CharField(allow_blank=True, default='')


class GeocodeDataSerializer(serializers.Serializer):
    place_id = serializers.IntegerField()
    licence = serializers.CharField()
    osm_type = serializers.CharField()
    osm_id = serializers.IntegerField()
    lat = serializers.CharField()
    lon = serializers.CharField()
    display_name = serializers.CharField()
    address = AddressSerializer()
    boundingbox = serializers.ListField(child=serializers.CharField())
