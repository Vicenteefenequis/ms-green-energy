from rest_framework import generics
from core_apps.projects.models import Project
from core_apps.projects.serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated


class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
