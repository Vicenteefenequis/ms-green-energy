from django.urls import path

from .views import (
    IndicatorListCreateView,
)


urlpatterns = [
    path("", IndicatorListCreateView.as_view(), name="indicator-list-create"),
]
