from django.db import models
from mantix_pro.models.status import Status

class Location(models.Model):
    location_name = models.CharField(max_length=200, null=True, unique=True)
    status = models.OneToOneField(Status, on_delete=models.DO_NOTHING)

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location_name