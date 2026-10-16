from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.models import ProjectOwn
from apps.core.serializers.project_own_serializer import ProjectOwnSerializer

# project-owns/


class GetProjectsByUserAPIView(APIView):

    def get(self, request):

        user = request.user

        if not user.is_authenticated:
            return Response(
                {
                    'details': 'Authentication details were not provided'
                }
            )
        projects = ProjectOwn.objects.filter(owner=user)

        return Response(
            ProjectOwnSerializer(projects, many=True).data,
            status=status.HTTP_200_OK
        )
