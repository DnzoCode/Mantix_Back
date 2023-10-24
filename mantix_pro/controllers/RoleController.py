from rest_framework import viewsets
from mantix_pro.models.role import Role
from mantix_pro.models.status import Status

from mantix_pro.serializer import RoleSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            rol = self.get_object()
            mensaje =  ""
            if rol.status.id == 1:
                rol.status = Status.objects.get(id=2)
                mensaje = f'Rol {rol.role} desactivado correctamente'
            elif rol.status.id == 2:
                rol.status = Status.objects.get(id=1)
                mensaje = f'Rol {rol.role} activado correctamente'
            rol.save()
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})
