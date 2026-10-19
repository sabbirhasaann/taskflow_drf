from django.urls import path
from .views.update_view import ProjectUpdateAPIView
from .views.destroy_view import ProjectDestroyAPIView

# api/v1/m4-generic-views/l29-update-api-view/
# api/v1/m4-generic-views/l29-update-api-view/projects/1/update/
# api/v1/m4-generic-views/l29-update-api-view/projects/1/delete/

urlpatterns = [
    path('projects/<int:pk>/update/',
         ProjectUpdateAPIView.as_view(), name='project-update-l29'),
    path('projects/<int:pk>/delete/',
         ProjectDestroyAPIView.as_view(), name="project-delete-l29"),
]
