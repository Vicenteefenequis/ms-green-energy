from rest_framework import serializers

from .models import Project






class ProjectSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name', read_only=True)
    population = serializers.IntegerField(source='city.population', read_only=True)


    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "city",
            "population",
            "created_at",
            "updated_at",
        )