from apps.core.serializers.task_preview_fields_serializer import TaskPreviewFieldsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TaskPreviewFieldsView(APIView):
    """Validate task input and return its representation."""

    def post(self, request):
        serializer = TaskPreviewFieldsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
