from rest_framework.serializers import ModelSerializer

from locations.models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('street', 'cep', 'city', 'country')
