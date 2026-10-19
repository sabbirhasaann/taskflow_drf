from apps.core.serializers.project_serializer import ProjectReadSerializer, ProjectWirteSerializer
from rest_framework.generics import DestroyAPIView
from apps.core.models import Project
from rest_framework.response import Response
from rest_framework import status


class ProjectDestroyAPIView(DestroyAPIView):

    serializer_class = ProjectReadSerializer

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
