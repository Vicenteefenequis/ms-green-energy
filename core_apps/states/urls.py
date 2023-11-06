from django.urls import path

from .views import (
    StateListCreateView,
    StateDestroyView
)

urlpatterns = [
    path("", StateListCreateView.as_view(), name="state-create"),
    path("<str:name>/", StateDestroyView.as_view(), name="state-destroy")
]
