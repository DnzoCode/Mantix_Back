from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.WorkOrderController import WorkOrderView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'workOrder', WorkOrderView, 'workOrder')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/ObtenerWorkOrderByEvent/<int:eventId>/', WorkOrderView.as_view({'get': 'ObtenerWorkOrderByEvent'})),
    
]