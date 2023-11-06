import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from core_apps.cities.models import City
from core_apps.energy_data.models import DataEnergetic
from core_apps.energy_data.serializers import DataEnergeticSerializer
from core_apps.projects.models import Project
from core_apps.projects.serializers import ProjectSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = [
        "created_at",
        "updated_at",
    ]

    def create(self, request, *args, **kwargs):
        user = request.user
        data_energetic_serializer = DataEnergeticSerializer(data=request.data)

        if data_energetic_serializer.is_valid():
            data_energetic = data_energetic_serializer.save()

            city_name = request.data.get("city")
            try:
                city = City.objects.get(name=city_name)
                city.data_energetic_id = data_energetic.pkid
                city.save()
            except City.DoesNotExist:
                return Response(
                    data={"detail": "City does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            project_data = {
                'user': user.pkid,
                'city': city.name,
                'name': request.data.get("name"),
                'description': request.data.get("description")
            }
            project_serializer = ProjectSerializer(data=project_data)

            if project_serializer.is_valid():
                project_serializer.save()
                return Response(
                    data={"detail": "Project created successfully"},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data_energetic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
