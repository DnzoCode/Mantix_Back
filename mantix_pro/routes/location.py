from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.LocationController import LocationView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'location', LocationView, 'location')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', LocationView.as_view({'post': 'activar_desactivar'})),
]