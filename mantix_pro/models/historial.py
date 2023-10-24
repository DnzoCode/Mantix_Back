from django.db import models
from mantix_pro.models.user import User
from mantix_pro.models.events import Events
from mantix_pro.models.status import Status



class Historial(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Events, on_delete=models.DO_NOTHING)
    status = models.OneToOneField(Status, on_delete=models.DO_NOTHING, null=True)
    date_change = models.DateField(null=True)
    
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)