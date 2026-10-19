from django.urls import path
from .views.update_view import ProjectUpdateAPIView

# api/v1/m4-generic-views/l29-update-api-view/
# api/v1/m4-generic-views/l29-update-api-view/projects/1/update/

urlpatterns = [
    path('projects/<int:pk>/update/',
         ProjectUpdateAPIView.as_view(), name='project-update-l29'),
]
