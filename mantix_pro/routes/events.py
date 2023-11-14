from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.EventController import EventView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'events', EventView, 'events')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', EventView.as_view({'post': 'activar_desactivar'})),
    path('api/v1/eventsByFecha/<fecha>/', EventView.as_view({'get': 'eventsByFecha'})),
    path('api/v1/uploadEvents/', EventView.as_view({'post': 'uploadEvents'})),
    path('api/v1/eventsByMonth/<initialDate>/<finalDate>/', EventView.as_view({'get': 'eventsByMonth'})),
    
]