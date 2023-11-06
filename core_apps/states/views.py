import logging

from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from .models import State
from .serializers import StateSerializer

logger = logging.getLogger(__name__)

class StateListCreateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['name']

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"City created {serializer.data.get('name')}")


class StateDestroyView(generics.DestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return State.objects.get(name=self.kwargs.get("name"))
        except State.DoesNotExist:
            raise ValidationError("City does not exist")

    def perform_destroy(self, instance):
        instance.delete()
