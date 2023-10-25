from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.RoleController import RoleView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'role', RoleView, 'role')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', RoleView.as_view({'post': 'activar_desactivar'})),
]