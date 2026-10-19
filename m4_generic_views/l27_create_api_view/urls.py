from django.urls import path
from .views import ProjectCreateAPIView

# api/v1/m4-generic-views/l27-create-api-view/
# api/v1/m4-generic-views/l27-create-api-view/projects/

urlpatterns = [
    path('projects/', ProjectCreateAPIView.as_view(), name='create-project-l27'),
]
