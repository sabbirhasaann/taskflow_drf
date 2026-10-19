from django.urls import path
from .views import ProjectRetrieveAPIView

# api/v1/m4-generic-views/l28-retrieve-api-view/
# api/v1/m4-generic-views/l28-retrieve-api-view/projects/1/

urlpatterns = [
    path('projects/<int:pk>/', ProjectRetrieveAPIView.as_view(),
         name="get-project-l28"),
]
