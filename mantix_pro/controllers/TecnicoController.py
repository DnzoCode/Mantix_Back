from rest_framework import viewsets
from mantix_pro.models.tecnico import Tecnico
from mantix_pro.serializer import TecnicoSerializer

from mantix_pro.models.status import Status

from rest_framework.decorators import action
from rest_framework.response import Response


class TecnicoView(viewsets.ModelViewSet):
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            tecnico = self.get_object()
            mensaje =  ""
            if tecnico.status.id == 1:
                tecnico.status = Status.objects.get(id=2)
                mensaje = f'Tecnico {tecnico.tecnico_name} {tecnico.tecnico_apellido} desactivado correctamente'
            elif tecnico.status.id == 2:
                tecnico.status = Status.objects.get(id=1)
                mensaje = f'Tecnico {tecnico.tecnico_name} {tecnico.tecnico_apellido} activado correctamente'
            tecnico.save()
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})
