from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from mantix_pro import views


#api versioning
router = routers.DefaultRouter()
router.register(r'role', views.RoleView, 'role')
router.register(r'status', views.StatusView, 'status')
router.register(r'location', views.LocationView, 'location')
router.register(r'tecnico', views.TecnicoView, 'tecnico')



urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Docs API"))
]