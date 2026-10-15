from rest_framework.views import APIView
from apps.core.serializers.task_preview_object_level_validation_serializer import TaskPreviewObjectLevelValidationSerializer
from rest_framework.response import Response
from rest_framework import status


class TaskPreviewObjectLevelValidationView(APIView):

    def post(self, request):

        serializer = TaskPreviewObjectLevelValidationSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
