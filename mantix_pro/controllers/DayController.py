from rest_framework import viewsets
from mantix_pro.models.day import Day
from mantix_pro.serializer import DaySerializer
from mantix_pro.models.status import Status

from rest_framework.decorators import action
from rest_framework.response import Response


class DayView(viewsets.ModelViewSet):
    serializer_class = DaySerializer
    queryset = Day.objects.all()