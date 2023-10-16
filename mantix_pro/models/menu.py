from django.db import models

class Menu(models.Model):
    menu_name = models.CharField(max_length=200, null=True)
    active = models.CharField(max_length=1, default='S')
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.menu_name