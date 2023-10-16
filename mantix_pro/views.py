from rest_framework import viewsets
from .models.role import Role
from .serializer import RoleSerializer

# Create your views here.
class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()