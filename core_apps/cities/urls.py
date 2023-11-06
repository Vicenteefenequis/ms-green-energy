from django.urls import path

from .views import (
    CityListCreateView,
    CityDestroyView, CityComparatorIndicatorView
)

urlpatterns = [
    path("", CityListCreateView.as_view(), name="city-create"),
    path("<str:name>/", CityDestroyView.as_view(), name="city-destroy"),
    path("<str:name>/compare/", CityComparatorIndicatorView.as_view(), name="city-compare"),
]
