from rest_framework import viewsets
from mantix_pro.models.day import Day
from mantix_pro.serializer import DaySerializer
from mantix_pro.models.status import Status
from rest_framework import status

from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import timedelta, datetime

class DayView(viewsets.ModelViewSet):
    serializer_class = DaySerializer
    queryset = Day.objects.all()
    
    @action(detail=True, methods=['GET'])
    def ObtenerDiaAnterior(self, request, dayDate):
        try:
            fecha_actual = datetime.strptime(dayDate, '%Y-%m-%d').date()
            
            # Buscar la fecha anterior más cercana
            fecha_anterior = None
            diferencia_dias = 1  # Iniciar con un día de diferencia
            
            while fecha_anterior is None:
                fecha_anterior = fecha_actual - timedelta(days=diferencia_dias)
                dia_anterior = Day.objects.filter(dayDate=fecha_anterior).first()
                if not dia_anterior:
                    fecha_anterior = None
                    diferencia_dias += 1
            
            serializer = self.get_serializer(dia_anterior)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({'mensaje': 'Fecha no válida'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            mensaje = f'Exeption: {ex}'
            return Response({'mensaje': mensaje}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True, methods=['GET'])
    def ObtenerDiaPorFecha(self, request, dayDate):
        try:
            day = Day.objects.filter(dayDate=dayDate).first()
            serializer = self.get_serializer(day)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'mensaje': 'Fecha no válida'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            mensaje = f'Exeption: {ex}'
            return Response({'mensaje': mensaje}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    