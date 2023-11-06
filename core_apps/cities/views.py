import logging

from django.db import IntegrityError
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from .models import City
from .serializers import CitySerializer

logger = logging.getLogger(__name__)


class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['name']

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"City created {serializer.data.get('name')}")


class CityDestroyView(generics.DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()

class CityComparatorIndicatorView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        my_city = City.objects.get(name=self.kwargs.get("name"))
        city_certified = City.objects.get(is_certified__exact=True)

        logger.info(my_city)