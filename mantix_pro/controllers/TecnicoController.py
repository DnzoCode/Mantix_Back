from rest_framework import viewsets
from mantix_pro.models.tecnico import Tecnico
from mantix_pro.serializer import TecnicoSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


class TecnicoView(viewsets.ModelViewSet):
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()