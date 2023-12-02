from .serializers import LocationSerializer
from rest_framework import viewsets
from .models import Location
from rest_framework.views import APIView
from rest_framework.response import Response


class LocationView(APIView):
    def get(self, request, format=None):
        location_type = request.query_params.get('type')
        if location_type in ['E', 'C']:
            locations = Location.objects.filter(type=location_type)
        else:
            locations = Location.objects.all()

        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
