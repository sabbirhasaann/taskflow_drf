from django.urls import path
from .views import ProjectL25ListView, ProjectL25DetailView

# api/v1/m4-generic-views/l25-generic-api-view/
app_name = 'l25'

urlpatterns = [
    # api/v1/m4-generic-views/l25-generic-api-view/projectsl25/
    path('projectsl25/', ProjectL25ListView.as_view(), name="list-projectsl25"),
    path('projectsl25/<int:pk>/', ProjectL25DetailView.as_view(),
         name='detail-projectl25'),

]
