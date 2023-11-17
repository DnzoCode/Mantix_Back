from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.maquina import Maquina
from mantix_pro.models.location import Location


from mantix_pro.serializer import MaquinaSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import IntegrityError, transaction
import base64
import pandas as pd
from django.shortcuts import get_object_or_404
from rest_framework import status
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
        
    @action(detail=True, methods=['post'])
    def uploadMaquinas(self, request):
        try:
            base64_data = request.data.get('maquina_file')
            decoded_data = base64.b64decode(base64_data)
            df = pd.read_excel(decoded_data)

            errors = []

            # Validación del archivo Excel
            for index, row in df.iterrows():
                maquina_name = row['Nombre_Maquina']
                maquina_modelo = row['Modelo_Maquina']
                numero_serial = row['Numero_Serial']
                location_name = row['Locacion']

                if pd.isna(maquina_name) or pd.isna(location_name):
                    continue

                status_value = 1
                status_instance = Status.objects.get(id=status_value)

                existing_maquina = Maquina.objects.filter(maquina_name=maquina_name.upper()).first()
                if existing_maquina:
                    errors.append({"error": f"Duplicado en la fila {index+2}, campo 'Nombre_Maquina': {maquina_name}"})
                    continue

                existing_location = Location.objects.filter(location_name=location_name.upper()).first()
                if not existing_location:
                    errors.append({"error": f"No existe una locacion registrada en la fila {index+2}, campo 'Locacion': {location_name}"})
                    continue

            # Si hay errores, se realiza un rollback y no se confirma la transacción
            if errors:
                return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

            # Creación de máquinas
            with transaction.atomic():
                for index, row in df.iterrows():
                    maquina_name = row['Nombre_Maquina']
                    maquina_modelo = row['Modelo_Maquina']
                    numero_serial = row['Numero_Serial']
                    location_name = row['Locacion']

                    if pd.isna(maquina_name) or pd.isna(location_name):
                        continue

                    status_value = 1
                    status_instance = Status.objects.get(id=status_value)

                    location_instance = Location.objects.get(location_name=location_name.upper())

                    Maquina.objects.create(
                        maquina_name=maquina_name.upper(),
                        maquina_modelo=maquina_modelo,
                        numero_serial=numero_serial,
                        location=location_instance,
                        status=status_instance,
                        ultimo_mantenimiento=None
                    )

            # Confirmar transacción si no hay errores después de la validación
            return Response({"message": "Datos de máquinas cargados exitosamente"},status=status.HTTP_200_OK)

        except IntegrityError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)