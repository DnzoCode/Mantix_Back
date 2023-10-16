from django.db import models

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=200, blank=True)
    status= models.CharField(max_length=1, default='S')
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.role
    