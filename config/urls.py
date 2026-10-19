"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/", include("apps.core.urls")),
    path("api/v1/m3-serializer-deep-dive/l21-read-write-serializer/",
         include("m3_serializer_deep_dive.l21_read_write_serializer.urls"),),
    path("api/v1/m3-serializer-deep-dive/l22-serializer-context",
         include('m3_serializer_deep_dive.l22_serializer_context.urls')),
    path("api/v1/m3-serializer-deep-dive/l23-serializer-method-field/",
         include('m3_serializer_deep_dive.l23_serializer_method_field.urls')),
    path('api/v1/m4-generic-views/l25-generic-api-view/',
         include('m4_generic_views.l25_generic_api_view.urls')),
    path('api/v1/m4-generic-views.l26-list-api-view/',
         include('m4_generic_views.l26_list_api_view.urls')),
    path('api/v1/m4-generic-views/l27-create-api-view/',
         include('m4_generic_views.l27_create_api_view.urls')),
    path('api/v1/m4-generic-views/l28-retrieve-api-view/',
         include('m4_generic_views.l28_retrieve_api_view.urls')),
    path('api/v1/m4_generic_views/l29_update_api_view/',
         include('m4_generic_views.l29_update_api_view.urls'))
]
