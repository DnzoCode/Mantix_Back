from rest_framework import viewsets
from mantix_pro.models.location import Location
from mantix_pro.serializer import LocationSerializer
from mantix_pro.models.status import Status

from rest_framework.decorators import action
from rest_framework.response import Response


class LocationView(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            location = self.get_object()
            mensaje =  ""
            if location.status.id == 1:
                location.status = Status.objects.get(id=2)
                mensaje = f'Location {location.location_name} desactivado correctamente'
            elif location.status.id == 2:
                location.status = Status.objects.get(id=1)
                mensaje = f'Location {location.location_name} activado correctamente'
            location.save()
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})