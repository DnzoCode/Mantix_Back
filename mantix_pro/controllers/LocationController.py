from rest_framework import viewsets
from mantix_pro.models.location import Location
from mantix_pro.serializer import LocationSerializer
from mantix_pro.models.status import Status

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status

import base64
import pandas as pd
from django.shortcuts import get_object_or_404

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
        
    @action(detail=True, methods=['post'])
    def uploadLocations(self, request):
        try:
            base64_data = request.data.get('location_file')
            decoded_data = base64.b64decode(base64_data)
            df = pd.read_excel(decoded_data)
            
            for index, row in df.iterrows():
                location_name = row['Locacion']
                if pd.isna(location_name):
                    continue
                status_value = 1
                status_instance = Status.objects.get(id=status_value)

                try:
                    # Intenta crear la instancia de Location
                    Location.objects.create(location_name=location_name.upper(), status=status_instance)
                except IntegrityError as e:
                    # Maneja la excepción de duplicados
                    return Response({"error": f"Duplicado en la celda {index+1}, campo 'Locacion': {location_name}"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Datos cargados exitosamente"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)