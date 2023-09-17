from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from core_apps.states.models import State
from core_apps.states.serializers import StateSerializer
from rest_framework.permissions import IsAuthenticated


class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticated]
