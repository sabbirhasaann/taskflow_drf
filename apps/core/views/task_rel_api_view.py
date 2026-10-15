from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.serializers.serializer_relationship_serializer import TaskRelSerializer


class TaskRelAPIView(APIView):

    def post(self, request):

        serializer = TaskRelSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        return Response(
            TaskRelSerializer(task).data,
            status=status.HTTP_201_CREATED
        )

# {
#     "project": 1,
#     "title": "Project 1 - Task 1"
# }
