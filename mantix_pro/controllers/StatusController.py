from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.serializer import StatusSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()