from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.maquina import Maquina


from mantix_pro.serializer import MaquinaSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class MaquinaView(viewsets.ModelViewSet):
    serializer_class = MaquinaSerializer
    queryset = Maquina.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            maquina = self.get_object()
            mensaje =  ""
            if maquina.status.id == 1:
                maquina.status = Status.objects.get(id=2)
                mensaje = f'Maquina {maquina.maquina_name} desactivado correctamente'
            elif maquina.status.id == 2:
                maquina.status = Status.objects.get(id=1)
                mensaje = f'Maquina {maquina.maquina_name} activado correctamente'
            maquina.save()
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})