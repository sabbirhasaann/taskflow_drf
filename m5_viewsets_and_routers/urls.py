from django.urls import path
from .views.l34_viewsets_view import ProjectViewSets

# api/v1/m5-viewsets-and-routers/
# api/v1/m5-viewsets-and-routers/projects/

project_list = ProjectViewSets.as_view({
    "get": "list",
})

urlpatterns = [
    path('projects/', project_list, name="projects-viewsets-l34"),
]
