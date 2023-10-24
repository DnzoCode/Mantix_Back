from django.db import models
from mantix_pro.models.menu import Menu
from mantix_pro.models.role import Role

class Permission(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    has_permission = models.CharField(max_length=1, default='S')
        #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.role.role} {self.menu.menu_name}"