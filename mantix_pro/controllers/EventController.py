from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.events import Events
from mantix_pro.models.maquina import Maquina
from mantix_pro.models.day import Day


from rest_framework import status
from mantix_pro.serializer import EventSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from django.db import IntegrityError, transaction
import base64
import pandas as pd
from datetime import datetime, timedelta

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Events.objects.all()
    
    @action(detail=True, methods=['post'])
    def activar_desactivar(self, request, pk=None, acc=None):
        try:
            events = self.get_object()
            mensaje =  ""
            if events.status.id == 1:
                events.status = Status.objects.get(id=2)
                mensaje = f'Mantenimiento {events.maquina.maquina_name} desactivado correctamente'
            elif events.status.id == 2:
                events.status = Status.objects.get(id=1)
                mensaje = f'Mantenimiento {events.maquina.maquina_name} activado correctamente'
            events.save()
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
        finally:
            return Response({'mensaje': mensaje})
        
    @action(detail=True, methods=['GET'])
    def eventsByFecha(self, request, fecha=None):
        try:
            events = Events.objects.filter(start=fecha)
            serializer = self.get_serializer(events, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
            return Response({'mensaje': mensaje}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True, methods=['post'])
    def uploadEvents(self, request):
        try:
            base64_data = request.data.get('event_file')
            decoded_data = base64.b64decode(base64_data)
            df = pd.read_excel(decoded_data)

            errors = []
            
            for index, row in df.iterrows():
                maquina_name = row['Nombre_Maquina']

                existing_maquina = Maquina.objects.filter(maquina_name=maquina_name.strip().upper()).first()
                if not existing_maquina:
                    errors.append({"error": f"No existe una maquina registrada con los datos en la fila {index+2}, campo 'Nombre_Maquina': {maquina_name}, recuerda que el sistema es sensible a tildes"})
                    continue

            # Si hay errores, se realiza un rollback y no se confirma la transacción
            if errors:
                return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                for index, row in df.iterrows():
                    maquina_name = row['Nombre_Maquina']
                    start_str = row['Fecha_Inicio']
                    end_str = row['Fecha_Fin']
                    ejecucion = row['Tipo_Ejecucion']
                    turno = row['Turno']
                    

                    if pd.isna(maquina_name):
                        continue

                    
                    status_value = 3
                    status_instance = Status.objects.get(id=status_value)
                    maquina_instance = Maquina.objects.get(maquina_name=maquina_name.upper())
                    
                    # Convertir las cadenas de fecha a objetos de fecha
                    start = pd.to_datetime(start_str, errors='coerce')
                    end = pd.to_datetime(end_str, errors='coerce')

                    # Verificar si hay errores en la conversión de fecha
                    if pd.isna(start) or pd.isna(end):
                        # Manejar el error o continuar con el próximo ciclo según sea necesario
                        continue

                    # Formatear las fechas según 'AAAA-MM-DD'
                    start_formatted = start.strftime('%Y-%m-%d')
                    end_formatted = end.strftime('%Y-%m-%d')

                    # Convertir las cadenas formateadas a objetos datetime.date
                    start_date = datetime.strptime(start_formatted, '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_formatted, '%Y-%m-%d').date()
                    
                    endnew = datetime.combine(end_date, datetime.max.time()) - timedelta(microseconds=1)
                    day, created = Day.objects.get_or_create(dayDate=start_formatted)
                    if created:
                        day.save()

                    Events.objects.create(
                        start=start_date,
                        end=endnew,
                        turno=turno,
                        maquina=maquina_instance,
                        status=status_instance,
                        title="Mantenimiento",
                        description=None,
                        mensaje_reprogramado=None,
                        tecnico=None,
                        ejecucion="P",
                        day=day
                    )

            # Confirmar transacción si no hay errores después de la validación
            return Response({"message": "Mantenimientos programados exitosamente"},status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    @action(detail=True, methods=['GET'])
    def eventsByMonth(self, request, initialDate=None, finalDate=None):
        try:
            # Parsea las fechas a objetos datetime si no están en ese formato ya
            initial_date = datetime.strptime(initialDate, "%Y-%m-%d")
            final_date = datetime.strptime(finalDate, "%Y-%m-%d")

            # Usa Q objects para combinar las condiciones OR
            events = Events.objects.filter(
                Q(start__gte=initial_date, start__lte=final_date)
            )
            
            serializer = self.get_serializer(events, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            mensaje = f'Exception: {ex}'
            return Response({'mensaje': mensaje}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            