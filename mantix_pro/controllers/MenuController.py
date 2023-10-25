from rest_framework import viewsets
from mantix_pro.serializer import MenuSerializer

from mantix_pro.models.menu import Menu
from mantix_pro.models.status import Status


from rest_framework.decorators import action
from rest_framework.response import Response

class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            menu = self.get_object()
            mensaje =  ""
            if menu.status.id == 1:
                menu.status = Status.objects.get(id=2)
                mensaje = f'Tecnico {menu.menu_name} desactivado correctamente'
            elif menu.status.id == 2:
                menu.status = Status.objects.get(id=1)
                mensaje = f'Tecnico {menu.menu_name} activado correctamente'
            menu.save()
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})