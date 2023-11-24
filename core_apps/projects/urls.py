from django.urls import path

from .views import (
    ProjectIndicatorCreateView,
    ProjectIndicatorView,
    ProjectStateComparation
)


urlpatterns = [
    path("", ProjectIndicatorCreateView.as_view(), name="project-create"),
    path("<uuid:id>/city-indicator/",
         ProjectIndicatorView.as_view(), name="project-view"),
    path("states/", ProjectStateComparation.as_view(),
         name="project-view-state-comparation"),

]
