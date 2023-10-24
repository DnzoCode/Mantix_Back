from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.TecnicoController import TecnicoView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'tecnico', TecnicoView, 'tecnico')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', TecnicoView.as_view({'post': 'activar_desactivar'}), name='role-activar-desactivar'),
]