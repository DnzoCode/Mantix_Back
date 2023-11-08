from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.events import Events

from rest_framework import status
from mantix_pro.serializer import EventSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Events.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            events = self.get_object()
            mensaje =  ""
            if events.status.id == 1:
                events.status = Status.objects.get(id=2)
                mensaje = f'Mantenimiento {events.maquina.maquina_name} desactivado correctamente'
            elif events.status.id == 2:
                events.status = Status.objects.get(id=1)
                mensaje = f'Mantenimiento {events.maquina.maquina_name} activado correctamente'
            events.save()
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})
        
    @action(detail=True, methods=['GET'])
    def eventsByFecha(self, request, fecha=None):
        try:
            events = Events.objects.filter(start=fecha)
            serializer = self.get_serializer(events, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
            return Response({'mensaje': mensaje}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            