from django.shortcuts import get_object_or_404
from core_apps.projects.models import Location, Project
from core_apps.projects.pagination import ProjectPagination
from core_apps.projects.serializers import LocationSerializer, ProjectCreateSerializer, ProjectListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from core_apps.projects.service import IndicatorCalculator


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
        calculator = IndicatorCalculator(projects)

        indicators = [
            {
                "name": "Uso de energia elétrica residencial per capita",
                "unit": "kWh/ano",
                "data": calculator.residential_electricity_per_capita(),
                "average": calculator.calculate_average(calculator.residential_electricity_per_capita())
            },
            {
                "name": "Porcentagem de habitantes da cidade com fornecimento regular de energia elétrica",
                "unit": "%",
                "data": calculator.percentage_habitants_with_regular_connection(),
                "average": calculator.calculate_average(calculator.percentage_habitants_with_regular_connection())
            },
            {
                "name": "Consumo de energia de edificios publicos por ano(kWh/m2)",
                "unit": "kWh/m2",
                "data": calculator.electricity_consumption_in_public_buildings(),
                "average": calculator.calculate_average(calculator.electricity_consumption_in_public_buildings())
            },
            {
                "name": "Porcentagem de energia total proveniente de fontes renováveis, como parte do consumo total da energia da cidade",
                "unit": "%",
                "data": calculator.percentage_of_renewable_energy(),
                "average": calculator.calculate_average(calculator.percentage_of_renewable_energy())
            },
            {
                "name": "Uso total de energia elétrica per capita(kWh/ano)",
                "unit": "kWh/ano",
                "data": calculator.total_electricity_per_capita(),
                "average": calculator.calculate_average(calculator.total_electricity_per_capita())
            },
            {
                "name": "Número médio de interrupções de energia elétrica por consumidor por ano",
                "unit": "número",
                "data": calculator.average_interruptions_energy_consumer(),
                "average": calculator.calculate_average(calculator.average_interruptions_energy_consumer())
            },
            {
                "name": "Duração média das interrupções de energia elétrica (em horas)",
                "unit": "número",
                "data": calculator.duration_average_interruptions_energy(),
                "average": calculator.calculate_average(calculator.duration_average_interruptions_energy())
            },
        ]

        return Response(indicators, status=status.HTTP_200_OK)


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        return super().get_queryset().filter(type="E")
