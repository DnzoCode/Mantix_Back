from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.StatusController import StatusView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'status', StatusView, 'status')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    # path('api/v1/activar_desactivar/<int:pk>/', RoleView.as_view({'post': 'activar_desactivar'}), name='role-activar-desactivar'),
]