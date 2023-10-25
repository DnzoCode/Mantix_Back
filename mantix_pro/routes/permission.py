from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.PermissionController import PermissionView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'permission', PermissionView, 'permission')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', PermissionView.as_view({'post': 'activar_desactivar'})),
]