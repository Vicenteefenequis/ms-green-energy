from django.urls import path

from .views import (
    IndicatorCertifiedListView,
    IndicatorListCreateView,
    IndicatorRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("", IndicatorListCreateView.as_view(), name="indicator-list-create"),
    path(
        "certified/", IndicatorCertifiedListView.as_view(),
        name="indicator-certified-list"
    ),
    path(
        "<uuid:id>/", IndicatorRetrieveUpdateDestroyView.as_view(),
        name="indicator-retrieve-update-destroy"
    ),
]
