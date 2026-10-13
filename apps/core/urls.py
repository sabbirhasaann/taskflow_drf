from django.urls import path
from apps.core.views import (
    HealthCheckView,
    RequestDemoView,
)

app_name = "core"
urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path('request-demo/', RequestDemoView.as_view(), name='request-demo'),
]
