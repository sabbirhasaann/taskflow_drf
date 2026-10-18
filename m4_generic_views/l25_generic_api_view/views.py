from rest_framework.generics import GenericAPIView
from .models import ProjectL25
from .serializers import ProjectL25Serializer, ProjectL25WriteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProjectL25ListView(GenericAPIView):

    queryset = ProjectL25.objects.all()
    serializer_class = ProjectL25Serializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        projects = self.get_queryset()
        serializer = self.get_serializer(
            projects,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        serializer.save(
            owner=request.user
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

# {
#     "name": "Project 2",
#     "description": "Description 2",
#     "status": "active"
# }


class ProjectL25DetailView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'POST']:
            return ProjectL25WriteSerializer
        return ProjectL25Serializer

    def get(self, request, *args, **kwargs):

        project = self.get_object()
        serializer = self.get_serializer(project)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def get_queryset(self):
        return ProjectL25.objects.filter(owner=self.request.user)

    def put(self, request, *args, **kwargs):

        project = self.get_object()
        serializer = self.get_serializer(
            project, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        updated_project = serializer.save()

        return Response(
            ProjectL25Serializer(updated_project).data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, *args, **kwargs):

        project = self.get_object()
        serializer = self.get_serializer(
            project, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_project = serializer.save()

        return Response(
            ProjectL25Serializer(updated_project).data,
            status=status.HTTP_200_OK
        )
