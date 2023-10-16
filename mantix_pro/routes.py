from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from mantix_pro import views


#api versioning
router = routers.DefaultRouter()
router.register(r'role', views.RoleView, 'role')
router.register(r'status', views.StatusView, 'status')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Role API"))
]