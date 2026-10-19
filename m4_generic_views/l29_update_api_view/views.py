from apps.core.serializers.project_serializer import ProjectReadSerializer, ProjectWirteSerializer
from rest_framework.generics import UpdateAPIView
from apps.core.models import Project
from rest_framework.response import Response
from rest_framework import status


class ProjectUpdateAPIView(UpdateAPIView):

    serializer_class = ProjectWirteSerializer

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        updated_project = serializer.save()

        
        read_serializer = ProjectReadSerializer(
            updated_project, context=self.get_serializer_context())

        return Response(read_serializer.data, status=status.HTTP_200_OK)
