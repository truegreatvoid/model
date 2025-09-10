from django.contrib import admin
from django.urls import path

from apps.docs.views import (
    ProtectedRedocView,
    ProtectedSpectacularAPIView,
    ProtectedSwaggerView,
)

url_docs = [
    path('api/schema/', ProtectedSpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', ProtectedSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', ProtectedRedocView.as_view(url_name='schema'), name='redoc'),
]
url_urls = [
    path('admin/', admin.site.urls),
]

urlpatterns = []
urlpatterns += url_docs
urlpatterns += url_urls
