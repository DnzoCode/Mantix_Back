from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

urlpatterns = [
    path("docs/", include_docs_urls(title="Docs API")),
]