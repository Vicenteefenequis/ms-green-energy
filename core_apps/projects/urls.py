from django.urls import path

from .views import (
    LocationListView,
    ProjectIndicatorCreateView,
    ProjectIndicatorView,
    ProjectListView
)


urlpatterns = [
    path("", ProjectIndicatorCreateView.as_view(), name="project-create"),
    path("<uuid:id>/city-indicator/",
         ProjectIndicatorView.as_view(), name="project-view"),
    path("location/", LocationListView.as_view(), name="location-list"),
]
