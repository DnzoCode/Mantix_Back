from django.db import models
from mantix_pro.models.status import Status
class Menu(models.Model):
    menu_name = models.CharField(max_length=200, null=True)
    menu_icon = models.CharField(max_length=200, null=True)
    menu_to = models.CharField(max_length=200, null=True)
    menu_orden = models.IntegerField(max_length=1, null=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, null=True)
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.menu_name