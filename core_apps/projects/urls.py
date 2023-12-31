from django.urls import path

from .views import (
    LocationListView,
    ProjectIndicatorCreateView,
    ProjectIndicatorView,
    ProjectListView,
    LocationBatchView
)


urlpatterns = [
    path("", ProjectIndicatorCreateView.as_view(), name="project-create"),
    path("<uuid:id>/city-indicator/",
         ProjectIndicatorView.as_view(), name="project-view"),
    path("states/", LocationListView.as_view(), name="location-list"),
    path("states/batch", LocationBatchView.as_view(), name="location-batch"),
]
