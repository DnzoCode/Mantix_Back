from django.db import models
from mantix_pro.models.menu import Menu
from mantix_pro.models.role import Role

class Permission(models.Model):
    menu = models.ManyToManyField(Menu)
    role = models.ManyToManyField(Role)
    has_permission = models.CharField(max_length=1, default='S')
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.has_permission