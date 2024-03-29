from django.db import models
from mantix_pro.models.status import Status
from mantix_pro.models.tecnico import Tecnico
from mantix_pro.models.maquina import Maquina
from mantix_pro.models.day import Day



class Events(models.Model):
    tecnico = models.ForeignKey(Tecnico, on_delete=models.DO_NOTHING, null=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, null=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.DO_NOTHING, null=True)
    day = models.ForeignKey(Day, on_delete=models.DO_NOTHING, null=True)
    
    title = models.CharField(max_length=100, null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    description = models.CharField(max_length=200, null=True)
    turno = models.CharField(max_length=1, null=True)
    mensaje_reprogramado = models.CharField(max_length=200, null=True)
    ejecucion = models.CharField(max_length=200, null=True)

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} {self.maquina.maquina_name}"

