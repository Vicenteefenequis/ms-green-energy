from rest_framework import generics, permissions, status
from core_apps.indicators.models import Indicator
from core_apps.indicators.serializers import IndicatorSerializer
from rest_framework.response import Response
import numpy as np


class IndicatorListCreateView(generics.ListCreateAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = [
        "created_at",
        "updated_at",
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        try:

            indicator_all = Indicator.objects.filter(
                is_certified=True
            )
            indicator_certified = IndicatorSerializer(
                indicator_all,
                many=True
            ).data

            indicator_user = Indicator.objects.get(
                user__id=self.request.user.id
            )

            indicator_user = IndicatorSerializer(indicator_user).data

            response_certifieds = np.array(indicator_certified)
            response_user = np.array(indicator_user)

            response = np.append(response_certifieds, response_user)

            return Response(response, status=status.HTTP_200_OK)
        except Indicator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
