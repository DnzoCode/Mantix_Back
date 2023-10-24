from django.db import models


class Day(models.Model):
    
    dayDate = models.DateTimeField(null=True)
    isClosed = models.CharField(max_length=1, null=True)
    
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)