from rest_framework.viewsets import ModelViewSet

from locations.api.serializers import LocationSerializer
from locations.models import Location


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
