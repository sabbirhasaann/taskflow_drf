from django.urls import path
from .views.l34_viewsets_view import ProjectViewSets

# api/v1/m5-viewsets-and-routers/
# api/v1/m5-viewsets-and-routers/projects/

project_list = ProjectViewSets.as_view({
    "get": "list",
    "post": "create"
})

project_detail = ProjectViewSets.as_view({
    "get": "retrieve",
})

urlpatterns = [
    path('projects/', project_list, name="projects-viewsets-l34"),
    path('projects/<int:pk>/', project_detail, name='project-detail-l34')
]
