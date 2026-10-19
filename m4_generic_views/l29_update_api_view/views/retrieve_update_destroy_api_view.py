from apps.core.serializers.project_serializer import ProjectReadSerializer, ProjectWirteSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from apps.core.models import Project
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProjectWirteSerializer
        return ProjectReadSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        project = self.get_object()
        serializer = self.get_serializer(
            project, data=request.data, partial=partial)

        serializer.is_valid(raise_exception=True)
        updated_project = serializer.save(owner=self.request.user)

        return Response(
            ProjectReadSerializer(updated_project).data,
            status=status.HTTP_200_OK
        )
