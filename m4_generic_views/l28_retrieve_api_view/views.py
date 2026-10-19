from rest_framework.generics import RetrieveAPIView
from .serializers import ProjectReadSerializer
from apps.core.models import Project


class ProjectRetrieveAPIView(RetrieveAPIView):

    serializer_class = ProjectReadSerializer

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
