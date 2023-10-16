from django.db import models

class Status(models.Model):
    status_name = models.CharField(max_length=200, null=True)
    active = models.CharField(max_length=1, default='S')
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.status_name