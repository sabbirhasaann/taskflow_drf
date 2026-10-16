from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.serializers.project_own_serializer import ProjectOwnSerializer


class ProjectOwnAPIView(APIView):

    def post(self, request):

        serializer = ProjectOwnSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        print("User:...", request.user)

        if not request.user.is_authenticated:
            return Response(
                {
                    'detail': 'authentication details were not provider.'
                }
            )

        project = serializer.save(owner=request.user)

        return Response(
            ProjectOwnSerializer(project).data,
            status=status.HTTP_201_CREATED,
        )
# {
#     "name": "This is kashim 1"
# }