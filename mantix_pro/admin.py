from django.contrib import admin
from .models.role import Role
from .models.events import Events
from .models.location import Location
from .models.maquina import Maquina
from .models.tecnico import Tecnico
from .models.menu import Menu
from .models.status import Status
from .models.permission import Permission
from .models.user import User
from .models.workOrder import WorkOrder
from .models.historial import Historial
from .models.day import Day



# Register your models here.
admin.site.register(Events)
admin.site.register(Location)
admin.site.register(Maquina)
admin.site.register(Tecnico)
admin.site.register(Role)
admin.site.register(Menu)
admin.site.register(Status)
admin.site.register(Permission)
admin.site.register(User)
admin.site.register(WorkOrder)
admin.site.register(Historial)
admin.site.register(Day)

