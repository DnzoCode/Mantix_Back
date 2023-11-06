from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.permission import Permission
from rest_framework import status

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
    
    # @param roleId
    @action(detail=True, methods=['get'])
    def ConsultarPermisos(self, request, roleId=None ):
        statusCode =""
        mensaje =  ""
        try:
            permission = Permission.objects.filter(role= roleId)
            serialized_permissions  = PermissionSerializer(permission, many=True,context={'request': self.request}).data
            mensaje = serialized_permissions
            statusCode =status.HTTP_200_OK
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
            statusCode =status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            return Response({'mensaje': mensaje}, status=statusCode)