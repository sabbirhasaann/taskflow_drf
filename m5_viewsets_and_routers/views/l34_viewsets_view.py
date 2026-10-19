from apps.core.models import Project
from apps.core.serializers.project_serializer import ProjectReadSerializer, ProjectWirteSerializer
from rest_framework import viewsets, status
from django.shortcuts import get_list_or_404
from rest_framework.response import Response


class ProjectViewSets(viewsets.ViewSet):

    def list(self, request):

        projects = Project.objects.filter(owner=self.request.user)
        serializer = ProjectReadSerializer(projects, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
