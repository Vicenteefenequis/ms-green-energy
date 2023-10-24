from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core_apps.energy_converter.model.Location import LocationSerializer
from core_apps.energy_converter.model.LocationStation import LocationStation
from core_apps.projects.models import Location, Project
from core_apps.projects.pagination import ProjectPagination
from core_apps.projects.serializers import ProjectCreateSerializer, ProjectListSerializer, \
    LocationListSerializer
from core_apps.projects.service import IndicatorCalculator, Indicator


class ProjectIndicatorCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ProjectPagination

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user, location__is_certified=False)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        else:
            return ProjectListSerializer


class ProjectIndicatorView(APIView):

    def get_projects(self, id, user):
        project_user = get_object_or_404(
            Project, id=id, user=user)
        projects = list(Project.objects.filter(location__is_certified=True))
        projects.insert(0, project_user)
        return projects

    def get(self, request, id):
        projects = self.get_projects(id, request.user)
        locations = [project.location for project in projects if hasattr(
            project, 'location')]
        calculator = IndicatorCalculator(locations)
        indicators = Indicator.to_response(calculator)

        return Response(indicators, status=status.HTTP_200_OK)


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


# class LocationListView(generics.ListAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#     pagination_class = ProjectPagination

#     def get_queryset(self):
#         return super().get_queryset().filter(type="E")


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        return super().get_queryset().filter(type="E")


class LocationCreateView(generics.ListCreateAPIView):
    queryset = LocationStation.objects.all()
    serializer_class = LocationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            location = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationsListStation(generics.ListAPIView):
    queryset = LocationStation.objects.all()
    serializer_class = LocationSerializer


class LocationBatchView(APIView):
    def post(self, request):
        siglas = request.data.get('siglas', [])

        if not siglas:
            return Response({"error": "Siglas não fornecidas."}, status=status.HTTP_400_BAD_REQUEST)

        # Filtrar as Locations pelas siglas
        locations = Location.objects.filter(slug__in=siglas)

        calculator = IndicatorCalculator(locations)
        indicators = Indicator.to_response(calculator)

        return Response(indicators, status=status.HTTP_200_OK)
