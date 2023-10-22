from django.db import models
from mantix_pro.models.status import Status
from mantix_pro.models.role import Role
from mantix_pro.models.location import Location



class User(models.Model):
    status = models.OneToOneField(Status, on_delete=models.DO_NOTHING, null=True)
    role = models.OneToOneField(Role, on_delete=models.DO_NOTHING, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)

    user_name = models.CharField(max_length=200, null=True)
    user_lastname = models.CharField(max_length=200, null=True)
    user_login= models.CharField(max_length=200, null=True)
    user_email = models.CharField(max_length=200, null=True, unique=True)
    user_password = models.CharField(max_length=200, null=True)
    user_token = models.CharField(max_length=200, null=True)
    is_owner = models.CharField(max_length=1, null=True)

    #Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_login} - {self.user_name} {self.user_lastname} | {self.location.location_name}"