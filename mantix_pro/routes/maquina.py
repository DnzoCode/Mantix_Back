from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.MaquinaController import MaquinaView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'maquina', MaquinaView, 'maquina')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', MaquinaView.as_view({'post': 'activar_desactivar'})),
    path('api/v1/uploadMaquinas/', MaquinaView.as_view({'post': 'uploadMaquinas'})),
    
]