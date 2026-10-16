from django.urls import path
from .views import TaskL23CreateView, TaskL23DetailView


urlpatterns = [
    # api/v1/m3-serializer-deep-dive/l23-serializer-method-field/taskl23/create/
    path('taskl23/create/', TaskL23CreateView.as_view(), name="create-taskl23"),
    # api/v1/m3-serializer-deep-dive/l23-serializer-method-field/taskl23/1
    path('taskl23/<int:id>/', TaskL23DetailView.as_view(),
         name="taskl23-detail-view")
]
