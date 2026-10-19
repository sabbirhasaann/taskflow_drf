from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectWriteSerializer, ProjectReadSerializer


class ProjectCreateAPIView(CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ProjectReadSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# {
#     "name": "Project 1 Kashim",
#     "description": "Description 1 Kashim",
#     "status": "active"
# }
