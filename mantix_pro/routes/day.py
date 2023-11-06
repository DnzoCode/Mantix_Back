from django.urls import path, include
from rest_framework import routers

from mantix_pro.controllers.DayController import DayView

#api versioning v1
router = routers.DefaultRouter()
router.register(r'day', DayView, 'day')

urlpatterns = [
    path("api/v1/", include(router.urls)),
]