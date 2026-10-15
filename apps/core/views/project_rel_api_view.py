from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.serializers.serializer_relationship_serializer import ProjectRelSerializer


class ProjectRelAPIView(APIView):

    def post(self, request):

        serializer = ProjectRelSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        project = serializer.save()

        return Response(
            ProjectRelSerializer(project).data,
            status=status.HTTP_201_CREATED
        )
# {
#     "title": "Project Rel 1"
# }
