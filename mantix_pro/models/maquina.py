from django.db import models
from mantix_pro.models.status import Status
from mantix_pro.models.location import Location

class Maquina(models.Model):
    location = models.OneToOneField(Location, on_delete=models.DO_NOTHING)
    status = models.OneToOneField(Status, on_delete=models.DO_NOTHING)
    maquina_name = models.CharField(max_length=250, null=True)
    maquina_modelo = models.CharField(max_length=250, null=True)
    numero_serial = models.CharField(max_length=250, null=True)
    ultimo_mantenimiento = models.DateTimeField()                                                   
    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.maquina_name