"""
URL configuration for parser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .settings import DEBUG

from core.views import *


schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version='v1',
        description="Rss parser",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hemrayevdovletgeldi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', API.as_view()),
    path('api2/', API2.as_view()),
    path('api1/', API1.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # path('swagger1/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # path('swagger2/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
)

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
