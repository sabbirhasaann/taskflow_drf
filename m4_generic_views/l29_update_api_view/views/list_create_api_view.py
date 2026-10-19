from apps.core.serializers.project_serializer import ProjectReadSerializer, ProjectWriteSerializer
from rest_framework.generics import ListCreateAPIView
from apps.core.models import Project
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ProjectListCreateAPIView(ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ProjectReadSerializer

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
