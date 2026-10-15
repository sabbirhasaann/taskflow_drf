from rest_framework.views import APIView
from apps.core.serializers.task_preview_field_level_validation_serializer import TaskPreviewFieldLevelValidataionSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskPreviewFieldLevelValidationView(APIView):

    def post(self, request):

        serializer = TaskPreviewFieldLevelValidataionSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
