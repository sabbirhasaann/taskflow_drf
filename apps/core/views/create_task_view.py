from rest_framework.views import APIView
from apps.core.serializers.task_serializer import CreateTaskSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateTaskView(APIView):

    def post(self, request):

        serializer = CreateTaskSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        task = serializer.save()

        return Response(
            {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'priority': task.priority,
                'is_completed': task.is_completed
            },
            status=status.HTTP_200_OK

        )
