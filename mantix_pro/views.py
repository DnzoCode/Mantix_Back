from rest_framework import viewsets

from .models.role import Role
from .models.status import Status
from .models.location import Location
from .models.tecnico import Tecnico


from .serializer import RoleSerializer, StatusSerializer, LocationSerializer, TecnicoSerializer


# Create your views here.
class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

class LocationView(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class TecnicoView(viewsets.ModelViewSet):
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()