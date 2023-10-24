from rest_framework import viewsets
from mantix_pro.models.location import Location
from mantix_pro.serializer import LocationSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


class LocationView(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()