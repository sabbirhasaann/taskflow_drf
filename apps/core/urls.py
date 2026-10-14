from django.urls import path
from apps.core.views.api_views import (
    HealthCheckView,
    RequestDemoView,
    TaskListCreateView,
)

from apps.core.views.fbvs import (
    task_summary,
    example_endpoint,
    task_status_preview,
)

app_name = "core"


urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path('request-demo/', RequestDemoView.as_view(), name='request-demo'),
    path('task-summary/', task_summary, name='task-summary'),
    path('example-endpoint/', example_endpoint, name='example-endpoint'),
    path('task-status-preview/', task_status_preview, name='task-status-preview'),
    path('v2/task-status-preview/', TaskListCreateView.as_view(),
         name='v2-task-status-preview'),
]
