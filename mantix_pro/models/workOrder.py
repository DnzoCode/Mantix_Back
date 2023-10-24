from django.db import models
from mantix_pro.models.status import Status
from mantix_pro.models.user import User
from mantix_pro.models.events import Events
from mantix_pro.models.tecnico import Tecnico

class WorkOrder(models.Model):
    
    work_order = models.CharField(max_length=200, null=True, unique=True)
    trabajo_realizado = models.CharField(max_length=200, null=True)
    diagnostico = models.CharField(max_length=200, null=True)
    actividades = models.CharField(max_length=200, null=True)
    causas = models.CharField(max_length=200, null=True)
    observacion = models.CharField(max_length=200, null=True)
    hora_inicio = models.CharField(max_length=200, null=True)
    hora_fin = models.CharField(max_length=200, null=True)


    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    event = models.ForeignKey(Events, on_delete=models.DO_NOTHING, null=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.DO_NOTHING, null=True)
    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work_order





