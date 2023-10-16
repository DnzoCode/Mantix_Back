from rest_framework import viewsets
from .models.role import Role
from .models.status import Status
from .serializer import RoleSerializer
from .serializer import StatusSerializer

# Create your views here.
class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()