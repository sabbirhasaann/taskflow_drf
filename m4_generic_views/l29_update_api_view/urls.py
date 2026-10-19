from django.urls import path
from .views.update_view import ProjectUpdateAPIView
from .views.destroy_view import ProjectDestroyAPIView
from .views.list_create_api_view import ProjectListCreateAPIView
from .views.retrieve_update_destroy_api_view import ProjectRetrieveUpdateDestroyAPIView

# api/v1/m4-generic-views/l29-update-api-view/
# api/v1/m4-generic-views/l29-update-api-view/projects/1/update/
# api/v1/m4-generic-views/l29-update-api-view/projects/1/delete/
# api/v1/m4-generic-views/l29-update-api-view/projects/
# api/v1/m4-generic-views/l29-update-api-view/projects/4/

urlpatterns = [
    path('projects/<int:pk>/update/',
         ProjectUpdateAPIView.as_view(), name='project-update-l29'),
    path('projects/<int:pk>/delete/',
         ProjectDestroyAPIView.as_view(), name="project-delete-l30"),
    path('projects/', ProjectListCreateAPIView.as_view(),
         name='project-list-create-l31'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(),
         name='project-detail-l32')
]
