from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.workOrder import WorkOrder

from rest_framework import status
from mantix_pro.serializer import WorkOrderSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class WorkOrderView(viewsets.ModelViewSet):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()
    
    @action(detail=True, methods=['GET'])
    def ObtenerWorkOrderByEvent(self, request, eventId=None):
        try:
            workOrder = WorkOrder.objects.filter(event=eventId).first()
            serializer = self.get_serializer(workOrder)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as ex:
            mensaje =  f'Exeption: {ex}'
            return Response({'mensaje': mensaje}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)