from rest_framework.generics import GenericAPIView
from .models import ProjectL25
from .serializers import ProjectL25Serializer
from rest_framework import status
from rest_framework.response import Response


class ProjectL25ListView(GenericAPIView):

    queryset = ProjectL25.objects.all()
    serializer_class = ProjectL25Serializer

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
