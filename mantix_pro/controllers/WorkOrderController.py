from rest_framework import viewsets
from mantix_pro.models.status import Status
from mantix_pro.models.workOrder import WorkOrder

from rest_framework import status
from mantix_pro.serializer import WorkOrderSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from reportlab.lib import colors
from io import BytesIO
from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import base64
from reportlab.platypus import Spacer
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
    
    @action(detail=True, methods=['post'])
    def DescargarWorkOrderPdf(self, request, workorderId=None):
        try:
            workorder = WorkOrder.objects.get(id=workorderId)
        except WorkOrder.DoesNotExist:
            return Response({'error':"La orden de trabajo no existe"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        work_order = workorder.work_order
        trabajo_realizado = workorder.trabajo_realizado
        diagnostico = workorder.diagnostico
        actividades = workorder.actividades
        causas = workorder.causas
        observacion = workorder.observacion
        hora_inicio = workorder.hora_inicio
        hora_fin = workorder.hora_fin
        event = workorder.event
        maquina_name = event.maquina.maquina_name
        tecnico = f"{workorder.tecnico.tecnico_name} {workorder.tecnico.tecnico_apellido}"
        locacion = event.maquina.location.location_name
        
        buffer = BytesIO()
        pdf = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        # Estilo para el título
        styles = getSampleStyleSheet()
        titulo = Paragraph(f"<b>Orden de Trabajo - {work_order}</b>", styles['Title'])
        elements.append(titulo)

        # Tabla para Técnico, Máquina y Locación
        datos_info = [
            [Paragraph("<b>Técnico Asignado:</b>", styles['Normal']), tecnico],
            [Paragraph("<b>Máquina:</b>", styles['Normal']), maquina_name],
            [Paragraph("<b>Locación:</b>", styles['Normal']), locacion],
        ]
        tabla_info = Table(datos_info)
        tabla_info.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        elements.append(Spacer(1, 20)) 
        elements.append(tabla_info)

        # Tabla para Hora Inicio y Hora Fin
        datos_horas = [
            ['Hora Inicio', 'Hora Fin'],
            [hora_inicio, hora_fin],
        ]
        tabla_horas = Table(datos_horas, colWidths=200)
        tabla_horas.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color de la línea
            ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color del borde
        ]))
        elements.append(Spacer(1, 20)) 
        
        elements.append(tabla_horas)
        # Tabla para Actividades y Diagnóstico
        datos_actividades = [
            ['Actividades', 'Diagnóstico'],
            [Paragraph(f"{actividades}", styles["Normal"]), Paragraph(f"{diagnostico}", styles["Normal"])],
        ]
        tabla_actividades = Table(datos_actividades, colWidths=200)
        tabla_actividades.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color de la línea
            ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color del borde
            ('WORDWRAP', (0, 1), (-1, -1), True),
        ]))
        elements.append(Spacer(1, 20)) 
        
        elements.append(tabla_actividades)

        # Tabla para Trabajo Realizado
        datos_trabajo = [
            ['Trabajo Realizado'],
            [Paragraph(f"{trabajo_realizado}", styles["Normal"])],
        ]
        tabla_trabajo = Table(datos_trabajo, colWidths=400)
        tabla_trabajo.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color de la línea
            ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color del borde
            ('WORDWRAP', (0, 1), (-1, -1), True),
        ]))
        elements.append(Spacer(1, 20)) 
        
        elements.append(tabla_trabajo)

        # Tabla para Causas y Observaciones
        datos_causas = [
            ['Causas', 'Observaciones'],
            [Paragraph(f"{causas}", styles["Normal"]), Paragraph(f"{observacion}", styles["Normal"])],
        ]
        tabla_causas = Table(datos_causas, colWidths=200)
        tabla_causas.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color de la línea
            ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)), # Color del borde
            ('WORDWRAP', (0, 1), (-1, -1), True),
        ]))
        elements.append(Spacer(1, 20)) 
        
        elements.append(tabla_causas)

        # Construir PDF y obtener datos en base64
        pdf.build(elements)
        pdf_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        return Response({"workOrderPdf": pdf_base64}, status=status.HTTP_200_OK)