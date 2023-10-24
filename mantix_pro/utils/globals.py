from rest_framework.decorators import action
from rest_framework.response import Response

def activar_desactivar(self, request, pk=None, model=None, status_field=None):
    try:
        obj = model.objects.get(id=pk)
        mensaje =  ""
        status = getattr(obj, status_field)
        if status.id == 1:
            setattr(obj, status_field, 2)
            mensaje = f'Rol {model.__name__} {obj} desactivado correctamente'
        elif status.id == 2:
            setattr(obj, status_field, 1)
            mensaje = f'Rol {model.__name__} {obj} activado correctamente'
        obj.save()
        
    except Exception as ex:
        mensaje =  f'Exeption: {ex}'
    finally:
        return Response({'mensaje': mensaje})