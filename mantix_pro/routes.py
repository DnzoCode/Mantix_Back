from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from mantix_pro.controllers.RoleController import RoleView
from mantix_pro.controllers.StatusController import StatusView
from mantix_pro.controllers.LocationController import LocationView
from mantix_pro.controllers.TecnicoController import TecnicoView





#api versioning
router = routers.DefaultRouter()
router.register(r'role', RoleView, 'role')
router.register(r'status', StatusView, 'status')
router.register(r'location', LocationView, 'location')
router.register(r'tecnico', TecnicoView, 'tecnico')



urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Docs API")),
    path('api/v1/activar_desactivar/<int:pk>/', RoleView.as_view({'post': 'activar_desactivar'}), name='role-activar-desactivar'),
]