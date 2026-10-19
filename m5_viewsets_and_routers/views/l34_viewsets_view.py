from apps.core.models import Project
from apps.core.serializers.project_serializer import ProjectReadSerializer, ProjectWirteSerializer
from rest_framework import viewsets, status
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProjectViewSets(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request):

        projects = Project.objects.filter(owner=self.request.user)
        serializer = ProjectReadSerializer(projects, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def create(self, request):

        serializer = ProjectWirteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save(owner=self.request.user)

        return Response(
            ProjectReadSerializer(project).data,
            status=status.HTTP_201_CREATED
        )
