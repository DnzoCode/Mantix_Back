from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.permission import Permission


from mantix_pro.serializer import PermissionSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class PermissionView(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            permission = self.get_object()
            mensaje =  ""
            if permission.status.id == 1:
                permission.status = Status.objects.get(id=2)
                mensaje = f'Permiso del menu {permission.menu.menu_name} desactivado correctamente'
            elif permission.status.id == 2:
                permission.status = Status.objects.get(id=1)
                mensaje = f'Permiso del menu {permission.menu.menu_name} activado correctamente'
            permission.save()
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})