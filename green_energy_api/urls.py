from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core_apps.energy_converter.view.view import NearestLocationStationView, reverse_geocode_view
from core_apps.projects.views import LocationCreateView, LocationsListStation
from core_apps.users.views import CustomUserDetailsView

schema_view = get_schema_view(
    openapi.Info(
        title="Green Energy API",
        default_version="v1",
        description="API endpoints for Green Api",
        contact=openapi.Contact(email="vicente.19981@live.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(), name="user-details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/projects/", include("core_apps.projects.urls")),
    path("api/v1/locations/", include("core_apps.locations.urls")),
    path('api/v1/sendStationLocations/',
         LocationCreateView.as_view(), name='location-create'),
    path('api/v1/locationsStations/',
         LocationsListStation.as_view(), name='location-list'),
    path('api/v1/nearest_station/',
         NearestLocationStationView.as_view(), name='nearest-station'),
    path('api/v1/reverse-geocode/', reverse_geocode_view, name='reverse-geocode'),

]


admin.site.site_header = "Green Energy API Admin"

admin.site.site_title = "Green Energy API Admin Portal"

admin.site.index_title = "Welcome to Green Energy API Portal"
