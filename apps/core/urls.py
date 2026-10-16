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
from apps.core.views.create_task_view import CreateTaskView
from apps.core.views.task_model_serializer_view import TaskModelSerializerView
from apps.core.views.project_rel_api_view import ProjectRelAPIView
from apps.core.views.task_rel_api_view import TaskRelAPIView
from apps.core.views.nested_serializer_view import NestedSerializerView
from apps.core.views.reverse_nested_serializer_view import ReverseNestedSerializerView
from apps.core.views.project_own_api_view import ProjectOwnAPIView
from apps.core.views.task_own_api_view import TaskOwnAPIView
from apps.core.views.get_projects_by_user_api_view import GetProjectsByUserAPIView
from apps.core.views.many_to_many_api_view import (
    TaskManyListCreateAPIView,
    LabelManyListCreateAPIView,
    TaksManyDetailAPIView,
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
    path('task-preview/', TaskPreviewView.as_view(), name='task-preview'),
    path('task-preview-fields/', TaskPreviewFieldsView.as_view(),
         name='task-preview-fields'),
    path('task-preview-field-level-validation/', TaskPreviewFieldLevelValidationView.as_view(),
         name='task-preview-field-level-validation'),
    path('task-preview-object-level-validation-view/', TaskPreviewObjectLevelValidationView.as_view(),
         name="task-preview-object-level-validation-view"),
    path('create-task/', CreateTaskView.as_view(), name="create-task"),
    path('task-model-serializer/', TaskModelSerializerView.as_view(),
         name="task-model-serializer"),
    path('create/projectrel/', ProjectRelAPIView.as_view(),
         name="create-projectrel"),
    path('create/projectrel/taskrel/',
         TaskRelAPIView.as_view(), name="create-taskrel"),
    path('nested-serializer/<int:id>/', NestedSerializerView.as_view(),
         name="nested-serializer"),
    path('reverse-nested-serializer/<int:id>/',
         ReverseNestedSerializerView.as_view(), name="reverse-nested-serializer"),
    path('create/project-own/', ProjectOwnAPIView.as_view(),
         name='create-project-own'),
    path('create/task-own/', TaskOwnAPIView.as_view(), name='create-task-own'),
    path('project-owns/',
         GetProjectsByUserAPIView.as_view(), name="project-owns"),
    path('tasksmany/', TaskManyListCreateAPIView.as_view(),
         name="task-many-list-create"),
    path('labelsmany/', LabelManyListCreateAPIView.as_view(),
         name="labels-many-list-create"),
    path('tasksmany/<int:id>/', TaksManyDetailAPIView.as_view(),
         name="task-many-detail"),
]
