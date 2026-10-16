from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.serializers.project_own_serializer import ProjectOwnSerializer
from django.core.exceptions import ValidationError


class ProjectOwnAPIView(APIView):

    def post(self, request):

        serializer = ProjectOwnSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        print("User:...", request.user)

        if request.user.is_authenticated:
            print("Authenticated")

        # project = serializer.save(owner=request.user)

        return Response(
            # ProjectOwnSerializer(project).data,
            {
                'success': 'sucess'
            },
            status=status.HTTP_201_CREATED,
        )
