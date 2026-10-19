from django.urls import path
from .views import ProjectL26ListAPIView

# api/v1/m4-generic-views.l26-list-api-view/

# api/v1/m4-generic-views.l26-list-api-view/projectsm4/

urlpatterns = [
    path('projectsm4/', ProjectL26ListAPIView.as_view(), name='list-projectsm4'),
]
