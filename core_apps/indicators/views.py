from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from core_apps.indicators.models import Indicator
from core_apps.indicators.pagination import IndicatorPagination
from core_apps.indicators.renderers import IndicatorJSONRenderer
from core_apps.indicators.serializers import IndicatorSerializer
from rest_framework.response import Response
import logging


logger = logging.getLogger(__name__)


class IndicatorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        indicator_id = self.kwargs.get("id")
        logger.info("ID: %s", request.user.id)
        indicator = get_object_or_404(Indicator, id=indicator_id, user=user)
        indicator.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = Indicator.objects.select_related("user")
        return queryset

    def get_object(self):
        user = self.request.user
        indicator = self.get_queryset().get(user=user, id=self.kwargs.get("id"))
        return indicator


class IndicatorListCreateView(generics.ListCreateAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = [
        "created_at",
        "updated_at",
    ]
    renderer_classes = [IndicatorJSONRenderer]
    pagination_class = IndicatorPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = Indicator.objects.filter(user=self.request.user)
        return queryset


class IndicatorCertifiedListView(generics.ListAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = [
        "created_at",
        "updated_at",
    ]

    def get_queryset(self):
        queryset = Indicator.objects.filter(is_certified=True)
        return queryset
