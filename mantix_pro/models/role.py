from django.db import models
from mantix_pro.models.status import Status

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=200, blank=True)
    status= models.ForeignKey(Status, on_delete=models.DO_NOTHING)
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.role
    