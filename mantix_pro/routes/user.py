from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.UserController import UserView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'user', UserView, 'user')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/activar_desactivar/<int:pk>/', UserView.as_view({'post': 'activar_desactivar'})),
    path('api/v1/auth/', UserView.as_view({'post': 'ObtenerTokenAuth'})),
    
]