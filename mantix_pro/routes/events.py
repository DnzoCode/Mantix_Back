from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.EventController import EvenView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'events', EvenView, 'events')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', EvenView.as_view({'post': 'activar_desactivar'})),
]