from django.urls import path
from apps.core.views.api_views import (
    HealthCheckView,
    RequestDemoView,
    TaskListCreateView,
    TaskPreviewView,
)

from apps.core.views.fbvs import (
    task_summary,
    example_endpoint,
    task_status_preview,
)

from apps.core.views.task_preview_serializer_fields_view import TaskPreviewFieldsView
from apps.core.views.task_preview_field_level_validation_view import TaskPreviewFieldLevelValidationView
from apps.core.views.task_preview_object_level_validation_view import TaskPreviewObjectLevelValidationView

app_name = "core"


urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path('request-demo/', RequestDemoView.as_view(), name='request-demo'),
    path('task-summary/', task_summary, name='task-summary'),
    path('example-endpoint/', example_endpoint, name='example-endpoint'),
    path('task-status-preview/', task_status_preview, name='task-status-preview'),
    path('v2/task-status-preview/', TaskListCreateView.as_view(),
         name='v2-task-status-preview'),
    path('task-preview/', TaskPreviewView.as_view(), name='task-preview'),
    path('task-preview-fields/', TaskPreviewFieldsView.as_view(),
         name='task-preview-fields'),
    path('task-preview-field-level-validation/', TaskPreviewFieldLevelValidationView.as_view(),
         name='task-preview-field-level-validation'),
    path('task-preview-object-level-validation-view/', TaskPreviewObjectLevelValidationView.as_view(),
         name="task-preview-object-level-validation-view"),
]
