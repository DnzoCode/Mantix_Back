from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from rest_framework.response import Response
from rest_framework import status

class Day(models.Model):
    
    dayDate = models.DateTimeField(null=True)
    isClosed = models.CharField(max_length=1, null=True, default="N")
    
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.dayDate)
    