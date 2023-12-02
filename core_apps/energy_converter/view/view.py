# View
import math

import requests
from django.db import connection
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import views, status, response

from core_apps.energy_converter.model.Location import LocationSerializer
from core_apps.energy_converter.model.LocationStation import getAnyLocation
from core_apps.energy_converter.model.geocode import GeocodeDataSerializer
from core_apps.projects.models import Project
from core_apps.projects.service import IndicatorCalculator, Indicator


def update_project_indicators(project_pkid):
    value = 1
    # Atualizar os indicadores do projeto para o valor "2" com base no project_pkid
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE projects_dataenergetic de
            SET 
                total_residential_electricity_use = total_residential_electricity_use + %s,
                total_electricity_consumption_in_public_buildings = total_electricity_consumption_in_public_buildings + %s,
                total_electricity_use = total_electricity_use + %s
            FROM 
                projects_project p 
            INNER JOIN   
                projects_location l 
            ON 
                p.location_id = l.pkid
            WHERE 
                l.data_energetic_id = de.pkid AND p.pkid = %s;
        """, [value, value, value, project_pkid])


def get_project_indicators(project_pkid):
    # Fetch indicators using a raw query
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                de.total_residential_electricity_use,
                de.total_electricity_consumption_in_public_buildings,
                de.total_electricity_use 
            FROM 
                projects_project p 
            INNER JOIN   
                projects_location l 
            ON 
                p.location_id = l.pkid
            INNER JOIN
                projects_dataenergetic de
            ON
                l.data_energetic_id = de.pkid
            WHERE 
                p.pkid = %s;
        """, [project_pkid])
        row = cursor.fetchone()

    if row:
        return {
            "total_residential_electricity_use": row[0],
            "total_electricity_consumption_in_public_buildings": row[1],
            "total_electricity_use": row[2]
        }
    return {}


def haversine(lon1, lat1, lon2, lat2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # Distance in km
    return distance


def get_nearest_station(user_latitude, user_longitude, project_city_name):
    nearest_station = None
    nearest_distance = float('inf')  # initialize with infinity

    for station in getAnyLocation():
        distance = haversine(user_longitude, user_latitude, float(station.longitude), float(station.latitude))
        if distance < nearest_distance and station.city == project_city_name:
            nearest_distance = distance
            nearest_station = station

    return nearest_station is None, nearest_station


class NearestLocationStationView(views.APIView):

    def post(self, request):
        project_pkid = request.data.get('project_pkid')
        user_latitude = request.data.get('latitude')
        user_longitude = request.data.get('longitude')

        if not user_latitude or not user_longitude:
            return response.Response({"detail": "Latitude and Longitude are required."},
                                     status=status.HTTP_400_BAD_REQUEST)

        nearest_station = get_nearest_station(float(user_latitude), float(user_longitude), "Goiânia")
        if not nearest_station:
            return response.Response({"detail": "No station found."}, status=status.HTTP_404_NOT_FOUND)
        update_project_indicators(project_pkid)

        projects = Project.objects.filter(pk=project_pkid)

        locations = [project.location for project in projects if hasattr(project, 'location')]

        calculator = IndicatorCalculator(locations)

        indicators = Indicator.to_response(calculator)

        serializer = LocationSerializer(nearest_station)
        serialized_data = serializer.data
        serialized_data["indicators"] = indicators

        return response.Response(serialized_data, status=status.HTTP_200_OK)


def reverse_geocode_view(request):
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')
    project_city_name = request.GET.get('project_city_name')

    if not latitude or not longitude:
        return JsonResponse({'error': 'Missing latitude or longitude parameters'}, status=400)

    try:
        response = requests.get(
            "https://geocode.maps.co/reverse",
            params={'lat': latitude, 'lon': longitude}
        )
        response.raise_for_status()
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=502)

    geocode_data = response.json()
    serializer = GeocodeDataSerializer(data=geocode_data)
    nearest_station = get_nearest_station(float(latitude), float(longitude), project_city_name)

    if serializer.is_valid():
        address_data = serializer.validated_data.get('address')
        city_name = address_data.get('city') or address_data.get('town') or address_data.get('village')

        is_valid_location = nearest_station and city_name == project_city_name

        # Return JsonResponse with the boolean value
        return JsonResponse({'is_registered_station': is_valid_location}, status=200)
    else:
        return JsonResponse(serializer.errors, status=400)
