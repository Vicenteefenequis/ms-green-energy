import django_filters as filters

from core_apps.cities.models import City


class CityFilter(filters.FilterSet):
    class Meta:
        model = City
        fields = {
            "name": ["exact", "icontains"],
        }