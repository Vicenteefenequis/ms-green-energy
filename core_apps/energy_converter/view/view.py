# View
import math
from rest_framework import views, status, response
from django.db import connection
from core_apps.energy_converter.model.Location import LocationSerializer
from core_apps.energy_converter.model.LocationStation import LocationStation
from core_apps.projects.models import Project
from core_apps.projects.service import IndicatorCalculator, calculate_indicators, Indicator


def update_project_indicators(project_pkid):
    # Update the project indicators to the value "2" based on project_pkid
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE projects_dataenergetic de
            SET 
                total_residential_electricity_use = total_residential_electricity_use + 25400.0,
                total_electricity_consumption_in_public_buildings = total_electricity_consumption_in_public_buildings + 25400.0,
                total_electricity_use = total_electricity_use + 25400.0
            FROM 
                projects_project p 
            INNER JOIN   
                projects_location l 
            ON 
                p.location_id = l.pkid
            WHERE 
                l.data_energetic_id = de.pkid AND p.pkid = %s;
        """, [project_pkid])


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


def get_nearest_station(user_latitude, user_longitude):
    nearest_station = None
    nearest_distance = float('inf')  # initialize with infinity

    for station in LocationStation.objects.all():
        distance = haversine(user_longitude, user_latitude, float(station.longitude), float(station.latitude))
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_station = station

    return nearest_station


class NearestLocationStationView(views.APIView):

    def post(self, request):
        project_pkid = request.data.get('project_pkid')
        user_latitude = request.data.get('latitude')
        user_longitude = request.data.get('longitude')

        if not user_latitude or not user_longitude:
            return response.Response({"detail": "Latitude and Longitude are required."},
                                     status=status.HTTP_400_BAD_REQUEST)

        nearest_station = get_nearest_station(float(user_latitude), float(user_longitude))
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
