from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.MenuController import MenuView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'menu', MenuView, 'menu')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', MenuView.as_view({'post': 'activar_desactivar'})),
]